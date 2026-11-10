#!/usr/bin/env python3
"""Pre-scenario geometry model (UNCALIBRATED, advisory) for task_inputsN2.

Scores whole policies and single misses on a *planned* gradable surface, then simulates six-run Opus baselines and
grades each simulated baseline with the bundle's own gate math (Task_Authoring/tools/difficulty_stats._gates) under the
assigned mode (medium) and task type (long-horizon). Every landing rate in the config is an assumption, not a
measurement (Opus 5.5 ledger priors for these families are Beta(1,1)-Beta(1.86,2) with n_eff <= 1.9). /create-scenario
replaces this with hardness_forecast.py on the real 01_Gradable_Surface.json.

Config (JSON, default research/00_geometry_config.json):
  slots:    [{id, weight, channel}]   channel = a channel id, "ANY:<a>,<b>" (fails if any listed channel is missed),
                                      "ALL:<a>,<b>" (fails only if every listed channel is missed), or null (ordinary row,
                                      fails only at the slip rate for its weight)
  channels: {id: {miss, members?: [ids], rho?}}  members: sub-channels that miss together with probability rho
  slip:     {"1": p, "3": p, "5": p}
  thoroughness: per-run latent loading (a thorough run catches more traps: positive correlation across channels)
  policies: {name: [missed channel ids]}

Run:  python3 -B Task_Authoring/task_inputsN2/Working_Files/research/geometry_mc.py [--config C] [--draws 20000]
Read-only; imports difficulty_stats without writing bytecode.
"""
from __future__ import annotations

import argparse
import itertools
import json
import random
import statistics
import sys
from pathlib import Path

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "Task_Authoring" / "tools"))
import difficulty_stats as ds  # noqa: E402  (gate math has one owner)

MODE, TASK_TYPE = "medium", "long-horizon"
GATES = ("avg_weighted_pass_rate", "pass_at_1", "per_rollout_sd", "failure_patterns")


def load(path: Path) -> dict:
    cfg = json.loads(path.read_text())
    leaves = []
    for cid, c in cfg["channels"].items():
        leaves += c.get("members") or [cid]
    cfg["_leaves"] = leaves
    return cfg


def slot_fails(ch, missed: set) -> bool:
    if ch is None:
        return False
    if ch.startswith("ANY:"):
        return any(x in missed for x in ch[4:].split(","))
    if ch.startswith("ALL:"):
        return all(x in missed for x in ch[4:].split(","))
    return ch in missed


def score(cfg: dict, missed: set) -> float:
    total = sum(s["weight"] for s in cfg["slots"])
    lost = sum(s["weight"] for s in cfg["slots"] if slot_fails(s["channel"], missed))
    return 1 - lost / total


def nd() -> statistics.NormalDist:
    return statistics.NormalDist()


def run_missed(cfg: dict, rng: random.Random, scale: float) -> set:
    theta = rng.gauss(0, 1)
    k = cfg.get("thoroughness", 0.5)
    missed = set()
    for cid, c in cfg["channels"].items():
        p = min(0.97, c["miss"] * scale)
        p_run = nd().cdf(nd().inv_cdf(min(max(p, 1e-9), 1 - 1e-9)) - k * theta)
        members = c.get("members")
        if not members:
            if rng.random() < p_run:
                missed.add(cid)
            continue
        shared = rng.random() < p_run
        rho = c.get("rho", 0.8)
        for m in members:
            own = rng.random() < p_run
            if (shared if rng.random() < rho else own):
                missed.add(m)
    return missed


def run_results(cfg: dict, rng: random.Random, scale: float) -> dict:
    missed = run_missed(cfg, rng, scale)
    slip = {int(k): v for k, v in cfg.get("slip", {"1": 0.03, "3": 0.06, "5": 0.06}).items()}
    res = {}
    for s in cfg["slots"]:
        if s["channel"] is None:
            res[s["id"]] = rng.random() >= slip[s["weight"]]
        else:
            res[s["id"]] = not slot_fails(s["channel"], missed)
    return res


def simulate(cfg: dict, draws: int, seed: int, scale: float) -> dict:
    rng = random.Random(seed)
    rubrics = [{"id": s["id"], "weight": s["weight"]} for s in cfg["slots"]]
    avgs, sds, pats, full, allok = [], [], [], 0, 0
    gate_ok = {g: 0 for g in GATES}
    allfail = {s["id"]: 0 for s in cfg["slots"]}
    for _ in range(draws):
        runs = [{"id": f"R{i}", "status": "completed", "tool_calls": 200, "results": run_results(cfg, rng, scale)}
                for i in range(1, 7)]
        out = ds._gates(runs, [], 6, rubrics, TASK_TYPE, MODE)
        rates = [r["weighted_pass_rate"] for r in out["per_rollout"]]
        avgs.append(sum(rates) / 6)
        sds.append(statistics.pstdev(rates))
        pats.append(len(out["patterns"]))
        full += len(out["golden_runs"])
        ok = True
        for g in GATES:
            p = out["gates"][g]["verdict"] == "PASS"
            gate_ok[g] += p
            ok &= p
        allok += ok
        for s in out["all_fail_rubrics"]:
            allfail[s] += 1
    avgs.sort()
    return {"scale": scale, "E_avg": statistics.mean(avgs), "p10": avgs[int(0.1 * draws)],
            "p90": avgs[int(0.9 * draws)], "E_sd": statistics.mean(sds),
            "P_gate": {g: v / draws for g, v in gate_ok.items()}, "P_all": allok / draws,
            "E_full": full / draws, "E_patterns": statistics.mean(pats),
            "allfail": {k: round(v / draws, 3) for k, v in allfail.items() if v / draws >= 0.01}}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default=str(HERE / "00_geometry_config.json"))
    ap.add_argument("--draws", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--scales", default="1.0,0.75,0.5,0.35,0.25")
    a = ap.parse_args()
    cfg = load(Path(a.config))
    total = sum(s["weight"] for s in cfg["slots"])
    print(f"PLANNED SURFACE ({Path(a.config).name}; pre-scenario sketch, UNCALIBRATED; mode {MODE}, {TASK_TYPE})")
    print(f"  slots {len(cfg['slots'])}  total weight {total}  weight-5 slots "
          f"{sum(1 for s in cfg['slots'] if s['weight'] == 5)}")
    share = {}
    for s in cfg["slots"]:
        ch = s["channel"]
        key = "ordinary" if ch is None else ("multi" if ":" in ch else next(
            (cid for cid, c in cfg["channels"].items() if ch == cid or ch in (c.get("members") or [])), ch))
        share[key] = share.get(key, 0) + s["weight"]
    print("  weight decided by channel:", {k: f"{v}/{total}={v / total:.0%}" for k, v in sorted(share.items())})
    print("\nWHOLE POLICIES (deterministic, no slips)")
    for name, missed in cfg.get("policies", {}).items():
        print(f"  {score(cfg, set(missed)):6.1%}  {name}")
    print("\nSINGLE MISSES (everything else right)")
    for cid, c in cfg["channels"].items():
        m = set(c.get("members") or [cid])
        print(f"  {score(cfg, m):6.1%}  miss {cid}" + (f" (all {len(m)} members)" if c.get("members") else ""))
        if c.get("members"):
            print(f"  {score(cfg, {c['members'][0]}):6.1%}  miss one {cid} member only")
    pairs = sorted((score(cfg, set(cfg["channels"][x].get("members") or [x]) | set(cfg["channels"][y].get("members") or [y])), x, y)
                   for x, y in itertools.combinations(cfg["channels"], 2))
    print("\nPAIRS (worst three and best three two-channel misses)")
    for s, x, y in pairs[:3] + pairs[-3:]:
        print(f"  {s:6.1%}  miss {x}+{y}")
    print(f"\nSIX-RUN BASELINES ({a.draws} draws per scale; gate math = difficulty_stats._gates, {MODE}, {TASK_TYPE})")
    print("  scale = multiplier on every design miss rate (1.0 = design rates; < 1 = a stronger Opus)")
    for sc in (float(x) for x in a.scales.split(",")):
        r = simulate(cfg, a.draws, a.seed, sc)
        g = r["P_gate"]
        print(f"  scale {sc:4.2f}: E[avg] {r['E_avg']:.1%} (p10-p90 {r['p10']:.1%}-{r['p90']:.1%})  E[SD] {r['E_sd']:.3f}"
              f"  P(avg<85%) {g['avg_weighted_pass_rate']:.2f}  P(<5 full) {g['pass_at_1']:.2f}"
              f"  P(SD band) {g['per_rollout_sd']:.2f}  P(patterns) {g['failure_patterns']:.2f}"
              f"  P(all four) {r['P_all']:.2f}  E[full passes] {r['E_full']:.2f}")
        if r["allfail"]:
            print(f"           P(row fails all six) >= 1%: {r['allfail']}")


if __name__ == "__main__":
    main()
