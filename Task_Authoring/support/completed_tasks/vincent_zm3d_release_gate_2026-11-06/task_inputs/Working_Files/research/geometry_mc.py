#!/usr/bin/env python3
"""Pre-scenario geometry model for storyline A (UNCALIBRATED, advisory).

Scores whole policies and single misses on the *planned* gradable surface, then simulates six-run baselines and grades
each simulated baseline with the bundle's own gate math (Task_Authoring/tools/difficulty_stats._gates, assigned mode
easy, long-horizon). Every landing rate below is an assumption, not a measurement: Opus 5.5 ledger priors for these
families are Beta(1,1)/n_eff 1 (hardness_ledger.py priors), so the rates are design targets that /create-scenario must
replace with hardness_forecast.py on the real surface.

Run:  python3 -B Task_Authoring/task_inputs/Working_Files/research/geometry_mc.py [--draws 20000] [--seed 7]
Read-only; imports difficulty_stats without writing bytecode.
"""
from __future__ import annotations

import argparse
import itertools
import json
import math
import random
import statistics
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / "Task_Authoring" / "tools"))
import difficulty_stats as ds  # noqa: E402  (gate math has one owner)

# ---------------------------------------------------------------- planned surface (slot ids, weight, channel)
# channel = the mechanism whose miss flips the slot; None = ordinary row (fails only at a slip rate)
SLOTS = [
    # C1 done-gap: fix merged after the submission build was cut (Linear Done + merged PR say "in")
    ("S1_reg_X1", 5, "C1"), ("L1_blocker_X1", 5, "C1"),
    # C2 done-gap: client fix in build, server half merged but never deployed to prod
    ("S2_reg_X2", 5, "C2"), ("L2_blocker_X2", 5, "C2"),
    # C3 correction elsewhere: "fixed" in #zombie-bugs, later re-test on the candidate in another place reproduces it
    ("S3_reg_X3", 5, "C3"), ("L3_blocker_X3", 5, "C3"),
    # C4 hidden house rule: update-path column failure blocks although fresh-install is green and a summary says green
    ("S4_matrix_update_path", 5, "C4"), ("L4_filed_bug_source_build", 3, "C4"),
    # C5 alias: player-facing report maps to an existing, differently titled ticket (reuse, no duplicate)
    ("L5_blocker_is_existing_ticket", 5, "C5"), ("S5_reg_X5_ref", 3, "C5"),
    # C6 outside the obvious filter: two in-scope bugs without the Bug label / outside the ZOM Bug view
    ("S6a_reg_X6a", 5, "C6a"), ("S6b_reg_X6b", 5, "C6b"), ("S13_register_volume", 3, "C6any"),
    # C7 completion elsewhere: open in Linear, verified fixed in the candidate in a record away from the ticket
    ("S7_reg_X7", 5, "C7"),
    # ordinary sampled verdict rows (<= 5) and delivery / core rows
    ("S8_sample", 3, None), ("S9_sample", 3, None), ("S10_sample", 3, None), ("S11_sample", 3, None),
    ("S12_sample", 3, None),
    ("K1_no_go_verdict", 3, "ALL_BLOCKERS"), ("D1_signoff_post", 1, None), ("D2_register_owner", 1, None),
]
CHANNELS = ["C1", "C2", "C3", "C4", "C5", "C6", "C7"]
# design miss rates (UNCALIBRATED): graded findability so runs fail different subsets
BASE_MISS = {"C1": 0.45, "C2": 0.60, "C3": 0.50, "C4": 0.40, "C5": 0.45, "C6": 0.50, "C7": 0.50}
SLIP = {3: 0.06, 1: 0.03, 5: 0.06}
C6_MEMBER_RHO = 0.8   # the two outside-filter members share one filter policy
THOROUGHNESS = 0.5    # per-run latent loading: a thorough run catches more traps (positive correlation)

RUBRICS = [{"id": s, "weight": w} for s, w, _ in SLOTS]
TOTAL = sum(w for _, w, _ in SLOTS)


def phi_inv(p: float) -> float:
    return statistics.NormalDist().inv_cdf(min(max(p, 1e-9), 1 - 1e-9))


def phi(x: float) -> float:
    return statistics.NormalDist().cdf(x)


def score(missed: set[str]) -> float:
    """Weighted score of one run given the set of missed channels (no slips)."""
    lost = 0
    for sid, w, ch in SLOTS:
        if ch is None:
            continue
        if ch == "C6any":
            hit = "C6a" in missed or "C6b" in missed
        elif ch == "ALL_BLOCKERS":
            hit = {"C1", "C2", "C3", "C4"} <= missed
        else:
            hit = ch in missed
        lost += w if hit else 0
    return 1 - lost / TOTAL


def run_results(rng: random.Random, scale: float) -> dict[str, bool]:
    theta = rng.gauss(0, 1)
    missed = set()
    for c in CHANNELS:
        p = min(0.97, BASE_MISS[c] * scale)
        p_run = phi(phi_inv(p) - THOROUGHNESS * theta)
        if c == "C6":
            shared = rng.random() < p_run
            for m in ("C6a", "C6b"):
                own = rng.random() < p_run
                if (shared if rng.random() < C6_MEMBER_RHO else own):
                    missed.add(m)
        elif rng.random() < p_run:
            missed.add(c)
    res = {}
    for sid, w, ch in SLOTS:
        if ch is None:
            res[sid] = rng.random() >= SLIP[w]
        elif ch == "C6any":
            res[sid] = not ("C6a" in missed or "C6b" in missed)
        elif ch == "ALL_BLOCKERS":
            res[sid] = not ({"C1", "C2", "C3", "C4"} <= missed)
        else:
            res[sid] = ch not in missed
    return res


def simulate(draws: int, seed: int, scale: float) -> dict:
    rng = random.Random(seed)
    tally = {"avg": [], "sd": [], "gates": {}, "all": 0, "full_pass_runs": 0, "patterns": []}
    gate_names = ("avg_weighted_pass_rate", "pass_at_1", "per_rollout_sd", "failure_patterns")
    for g in gate_names:
        tally["gates"][g] = 0
    allfail_rows = {s: 0 for s, _, _ in SLOTS}
    for _ in range(draws):
        runs = [{"id": f"R{i}", "status": "completed", "tool_calls": 300, "results": run_results(rng, scale)}
                for i in range(1, 7)]
        out = ds._gates(runs, [], 6, RUBRICS, "long-horizon", "easy")
        rates = [r["weighted_pass_rate"] for r in out["per_rollout"]]
        tally["avg"].append(sum(rates) / 6)
        tally["sd"].append(statistics.pstdev(rates))
        tally["full_pass_runs"] += len(out["golden_runs"])
        tally["patterns"].append(len(out["patterns"]))
        ok = True
        for g in gate_names:
            passed = out["gates"][g]["verdict"] == "PASS"
            tally["gates"][g] += passed
            ok &= passed
        tally["all"] += ok
        for s in out["all_fail_rubrics"]:
            allfail_rows[s] += 1
    avg = sorted(tally["avg"])
    return {
        "scale": scale,
        "E_avg": statistics.mean(avg),
        "avg_p10_p90": (avg[int(0.1 * draws)], avg[int(0.9 * draws)]),
        "E_sd": statistics.mean(tally["sd"]),
        "P_gate": {g: v / draws for g, v in tally["gates"].items()},
        "P_all_gates": tally["all"] / draws,
        "E_full_passes": tally["full_pass_runs"] / draws,
        "E_patterns": statistics.mean(tally["patterns"]),
        "P_row_fails_all_six": {s: round(v / draws, 3) for s, v in allfail_rows.items() if v / draws >= 0.01},
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--draws", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    print("PLANNED SURFACE (pre-scenario sketch, UNCALIBRATED)")
    print(f"  slots {len(SLOTS)}  total weight {TOTAL}  weight-5 slots {sum(1 for _, w, _ in SLOTS if w == 5)}")
    share = {}
    for _, w, ch in SLOTS:
        key = "C6" if ch and ch.startswith("C6") else (ch or "ordinary")
        share[key] = share.get(key, 0) + w
    print("  weight by channel:", {k: f"{v}/{TOTAL}={v / TOTAL:.0%}" for k, v in sorted(share.items())})
    print("\nWHOLE POLICIES (deterministic, no slips)")
    policies = {
        "P0 lazy: Linear states + labels only": set(CHANNELS[:5]) | {"C6a", "C6b", "C7"},
        "P1 Linear + GitHub merges (no #builds, no deploy check, no re-tests)": {"C1", "C2", "C3", "C4", "C6a", "C6b", "C7"},
        "P2 + #builds change lists": {"C2", "C3", "C4", "C5", "C6a", "C6b", "C7"},
        "P3 + every ticket comment and PR review (no DMs, no runbook rule)": {"C2", "C3", "C4", "C6a", "C6b"},
        "P4 everything retrieved, house rule not applied": {"C4"},
        "P5 everything retrieved, obvious filter kept": {"C6a", "C6b"},
        "P6 perfect": set(),
    }
    for name, missed in policies.items():
        print(f"  {score(missed):6.1%}  {name}")
    print("\nSINGLE MISSES (everything else right)")
    for c in CHANNELS:
        m = {"C6a", "C6b"} if c == "C6" else {c}
        print(f"  {score(m):6.1%}  miss {c}" + ("  (both outside-filter members)" if c == "C6" else ""))
    print(f"  {score({'C6a'}):6.1%}  miss one outside-filter member only")
    print("\nPAIRS (worst and best two-channel misses)")
    pairs = sorted((score({x, y} if not x.startswith('C6') else {x, y}), x, y)
                   for x, y in itertools.combinations(["C1", "C2", "C3", "C4", "C5", "C6a", "C7"], 2))
    for s, x, y in pairs[:3] + pairs[-3:]:
        print(f"  {s:6.1%}  miss {x}+{y}")

    print(f"\nSIX-RUN BASELINES ({a.draws} draws per scale; gate math = difficulty_stats._gates, easy, long-horizon)")
    print("  scale = multiplier on every design miss rate (1.0 = the design rates; <1 = a stronger Opus)")
    rows = []
    for scale in (1.0, 0.75, 0.5, 0.35, 0.25):
        r = simulate(a.draws, a.seed, scale)
        rows.append(r)
        g = r["P_gate"]
        print(f"  scale {scale:4.2f}: E[avg] {r['E_avg']:.1%} (p10-p90 {r['avg_p10_p90'][0]:.1%}-{r['avg_p10_p90'][1]:.1%})"
              f"  E[SD] {r['E_sd']:.3f}  P(avg<90%) {g['avg_weighted_pass_rate']:.2f}  P(<5 full) {g['pass_at_1']:.2f}"
              f"  P(SD band) {g['per_rollout_sd']:.2f}  P(patterns) {g['failure_patterns']:.2f}"
              f"  P(all four) {r['P_all_gates']:.2f}  E[full passes] {r['E_full_passes']:.2f}")
        if r["P_row_fails_all_six"]:
            print(f"           P(row fails all six) >= 1%: {r['P_row_fails_all_six']}")
    if a.json:
        print(json.dumps(rows, indent=1))


if __name__ == "__main__":
    main()
