#!/usr/bin/env python3
"""F1 acceptance protocol, fourth revision (2026-10-28): all 13 manifest assertions, pre-registered Bonferroni gate.

Every manifest id is emitted once per seed with a status in {PASS, FAIL, STUB, ABSENT}. A STUB or ABSENT record carries
a reason, has pass=false, and never counts as a pass. Assertions use the production hardness_forecast path
(_rate_draw, _sample_channel, Outcomes, simulate) and analytic targets computed here, not through the forecast; the
exact failed sets of the f4 fixture and the geometry of f8 are exact checks.

Gate (pre-registered in f1_acceptance/F1_PROTOCOL_MANIFEST.json): m = 13 ids x 3 seeds = 39; familywise alpha = 0.01;
z_crit = Phi^-1(1 - alpha/(2m)) = 3.6558. A z assertion passes iff |z| <= z_crit; a cell with n*p0 < 5 uses the exact
binomial and passes iff p >= alpha/m. The seed set, draw count and manifest ids are read from the manifest, never
chosen after seeing a result.

Usage (workspace root):
  python3 -B .../scripts/f1_protocol.py OUT_DIR --seed N [--draws 20000]
  python3 -B .../scripts/f1_protocol.py --summarize LOG1 LOG2 LOG3 [--acceptance-dir DIR]
  python3 -B .../scripts/f1_protocol.py --write-sums
"""
import argparse
import hashlib
import json
import math
import platform
import random
import shutil
import sys
from pathlib import Path
from statistics import NormalDist

B = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(B / "tools"))
sys.path.insert(0, str(HERE))
import difficulty_mutation as dm                    # noqa: E402
import hardness_forecast as hf                     # noqa: E402
import oracle_kit as ok                             # noqa: E402
import selftest_sandbox as sx                       # noqa: E402
import f1_audited_ledger as fal                     # noqa: E402

ACCEPT = B / "support" / "fix_session_2026-10-25" / "f1_acceptance"
MANIFEST = ACCEPT / "F1_PROTOCOL_MANIFEST.json"
AUDIT = ACCEPT / "F1_PROVENANCE_AUDIT.txt"
LEDGER = ACCEPT / "F1_AUDITED_LEDGER.jsonl"
MODEL = "claude-opus-4-8"
RUNS = hf.RUNS                                            # 6 baselines runs
TASK_TYPE, CALLS = "long-horizon", 550
STATUSES = ("PASS", "FAIL", "STUB", "ABSENT")
ABSENT_BY_DESIGN = {"f6_chain"}       # no chain channel ships in any solver: reported, never implemented as a pass
REQUIRED_PROD = ("rate_draw_once_per_baseline", "sampled_members_reach_solver",
                 "sampled_subset_reaches_solver_through_simulate")


def pooled_verdict(rows, aid: str) -> str | None:
    """FAIL beats STUB beats an ABSENT that is allowed for this id; any other ABSENT is a failure."""
    st = [r["status"] for r in rows]
    if "FAIL" in st:
        return "FAIL"
    if "STUB" in st:
        return "STUB"
    if "ABSENT" in st:
        return "ABSENT" if aid in ABSENT_BY_DESIGN else "FAIL"
    return None


def protocol_self_test() -> int:
    """Planted: a missing or false production-path check is never a pass (it fails the seed exit and the summary)."""
    good = {"production_path": {
        "rate_draw_once_per_baseline": {"calls": 14, "want": 14, "draws": 7, "channels": 2},
        "sampled_members_reach_solver": {"one_member": ["S1"], "full_set": ["S1", "S2"]},
        "sampled_subset_reaches_solver_through_simulate": {
            "subset_member_latent": ["A-01"], "subset_run_latent": ["A-01"],
            "member": {"S1": {"P_fail": 1.0}, "S2": {"P_fail": 0.0}},
            "run": {"S1": {"P_fail": 1.0}, "S2": {"P_fail": 0.0}},
            "one_in_six": {"P_fail": round(1 / RUNS, 4), "P_fails_all_six": 0.0}}}}
    missing = {"production_path": {k: v for k, v in good["production_path"].items() if k != REQUIRED_PROD[1]}}
    false = json.loads(json.dumps(good))
    false["production_path"]["rate_draw_once_per_baseline"]["calls"] = 84      # the forbidden per-run count
    empty = {"production_path": {}}
    assert production_ok(good) and not production_ok(missing) and not production_ok(false) and not production_ok(empty)
    assert not production_ok({})
    # the by-design exemption covers ABSENT only: a FAIL or STUB on f6 still fails, and an ABSENT on another id fails
    assert pooled_verdict([{"status": "ABSENT"}, {"status": "ABSENT"}, {"status": "ABSENT"}], "f6_chain") == "ABSENT"
    assert pooled_verdict([{"status": "PASS"}, {"status": "FAIL"}, {"status": "ABSENT"}], "f6_chain") == "FAIL"
    assert pooled_verdict([{"status": "PASS"}, {"status": "STUB"}, {"status": "ABSENT"}], "f6_chain") == "STUB"
    assert pooled_verdict([{"status": "PASS"}, {"status": "ABSENT"}, {"status": "ABSENT"}], "f7_sd") == "FAIL"
    # summarization REVALIDATES every cell: a genuinely failed zero cell cannot be turned into a PASS by a cached flag
    g = gate_params(manifest())
    ok_row = {"status": "PASS", "n": 20000, "hits": 14000,
              "cells": {k: {"n": 20000, "hits": int(t * 20000)} for k, t in F5_TARGETS.items()}}
    assert revalidate(ok_row, "f5_joint", 20000, g)["pass"] is True
    bad_row = json.loads(json.dumps(ok_row))
    bad_row["cells"]["01"]["hits"] = 1
    assert revalidate(bad_row, "f5_joint", 20000, g)["pass"] is False
    bad_row2 = {"status": "PASS", "n": 20000, "hits": 12000, "baselines": 20000, "se": 1.0}
    assert revalidate(bad_row2, "f7_e2e", 20000, g)["pass"] is False   # SE is derived, never trusted
    # f9: every cell and the distinct-source gate are revalidated
    f9_row = {"status": "PASS", "sources": {"rule:late": "s1", "rule:quiet": "s2"}, "cells": {
        "independent": {"n": 20000 * RUNS, "baselines": 20000, "hits": 0.25 * 20000 * RUNS},
        "correlated": {"n": 20000 * RUNS, "baselines": 20000, "hits": (1 / 3) * 20000 * RUNS}}}
    assert revalidate(f9_row, "f9_mechanisms", 20000, g)["pass"] is True
    for mutate in ("cell", "source"):
        bad9 = json.loads(json.dumps(f9_row))
        if mutate == "cell":
            bad9["cells"]["correlated"]["hits"] = 0.5 * 20000 * RUNS
        else:
            bad9["sources"]["rule:quiet"] = "s1"
        assert revalidate(bad9, "f9_mechanisms", 20000, g)["pass"] is False, mutate
    # f10: the canonical check set is required (a deleted check cannot pass)
    f10_row = {"status": "PASS", "checks": {k: True for k in F10_CHECKS},
               "statistic": len(F10_CHECKS), "target": len(F10_CHECKS)}
    assert revalidate(f10_row, "f10_fail_closed", 20000, g)["pass"] is True
    assert revalidate(dict(f10_row, checks={"all simulated outputs finite": True}, statistic=1, target=1),
                      "f10_fail_closed", 20000, g)["pass"] is False
    # sample budgets are canonical: a forged denominator/baseline count is never accepted
    assert revalidate({"hits": 1, "n": 50}, "f1_linked", 20000, g)["pass"] is False
    bad9b = json.loads(json.dumps(f9_row))
    bad9b["cells"]["independent"]["baselines"] = 1
    assert revalidate(bad9b, "f9_mechanisms", 20000, g)["pass"] is False
    bad5 = {"cells": {k: {"n": (20000 if k == "00" else 1), "hits": int(t * (20000 if k == "00" else 1))}
                      for k, t in F5_TARGETS.items()}}
    assert revalidate(bad5, "f5_joint", 20000, g)["pass"] is False
    forged = json.loads(json.dumps(good))
    forged["production_path"]["rate_draw_once_per_baseline"].update(draws=7, channels=12, calls=84)
    assert production_ok(forged) is False
    print("protocol self-test: ok (both mandatory production-path checks must exist and pass; missing/false/empty "
          "never pass)")
    return 0

# The exact per-baseline variance of each statistic that is an AVERAGE over the six runs of one baseline. The six runs
# share the baseline-scoped rate (the production-path property the harness asserts), so the variance of the average is
# not p(1-p): a binomial SE over draws*6 would overstate the precision (f9) or understate it (f7_shared).
#   f7_e2e    avg of 6 runs of a run-latent e=0.25 channel with one slot of weight 1/2: (0.5/6)^2 * 6*.25*.75 = 1/128
#   f7_shared avg of 6 runs, q~U(0,1) per baseline: (0.5/6)^2 * (E[Var K|q] + Var E[K|q]) = 4/144 = 1/36
#   f9_indep  p = th1*th2: Var(p) = 7/144; E[p(1-p)]/6 = 5/216; total 31/432
#   f9_corr   p = min(th1,th2): Var(p) = 1/18; E[p(1-p)]/6 = 1/36; total 1/12
VAR_PER_BASELINE = {"f7_e2e": 1 / 128, "f7_shared": 1 / 36,
                    "f9_independent": 31 / 432, "f9_correlated": 1 / 12}

TRUTH_FIELDS = {"class": "class", "groups": "groups"}
CHANNEL_SURFACE = {"truth_fields": TRUTH_FIELDS,
                   "slots": [{"id": "S", "weight": 1, "class": "direct", "selector": ["field", "A-01", "status"]},
                             {"id": "C", "weight": 1, "class": "direct", "selector": ["field", "B-01", "status"]}]}
A_SURFACE = {"truth_fields": TRUTH_FIELDS,
             "slots": [{"id": "S1", "weight": 1, "class": "direct", "selector": ["field", "A-01", "status"]},
                       {"id": "S2", "weight": 1, "class": "direct", "selector": ["field", "A-02", "status"]}]}
CANCEL_SURFACE = {"truth_fields": TRUTH_FIELDS,
                  "slots": [{"id": "SB1", "weight": 1, "class": "direct", "selector": ["field", "B-01", "status"]},
                            {"id": "SB2", "weight": 1, "class": "direct", "selector": ["field", "B-02", "status"]},
                            {"id": "SB", "weight": 1, "class": "direct", "selector": ["total", "HOLD"]}]}
SCALE_SURFACE = {"truth_fields": TRUTH_FIELDS,
                 "slots": [{"id": "S1", "weight": 1, "class": "direct", "selector": ["field", "K-01", "class"]},
                           {"id": "S2", "weight": 1, "class": "direct", "selector": ["field", "K-02", "class"]},
                           {"id": "D1", "weight": 1, "class": "delivery",
                            "selector": ["delivery", "slide_updated"]}]}
CHANNEL_OVERRIDES = ("scale:a=0.02@f1 fixture", "linked:a=0.02@f1 fixture", "deleg:a=0.3@f1 fixture",
                     "pair:b=0.5@f1 fixture", "duo:ind=0.3@f1 fixture", "duo:link=0.3@f1 fixture",
                     "surface:deck=0.4@f1 fixture")
BRIEFS = [{"keys": [f"A-{n:02d}" for n in range(1, 17)]},
          {"keys": [f"A-{n:02d}" for n in range(17, 33)]},
          {"keys": [f"A-{n:02d}" for n in range(33, 41)]}]


class _EmptyLedger:
    def current(self):
        return []


# ------------------------------------------------------------------ manifest and gate

def manifest() -> dict:
    return json.loads(MANIFEST.read_text())


def gate_params(man: dict) -> dict:
    ids = [a["id"] for a in man["assertions"]]
    seeds = list(man["seeds"])
    m = len(ids) * len(seeds)
    alpha = float(man["familywise_alpha"])
    return {"ids": ids, "seeds": seeds, "draws": int(man["draws_per_seed"]), "m": m, "alpha": alpha,
            "z_crit": NormalDist().inv_cdf(1 - alpha / (2 * m)),
            "rule": "Bonferroni: z assertion passes iff |z| <= z_crit; exact binomial iff n*p0 < 5 and p >= alpha/m"}


# ------------------------------------------------------------------ fixtures and statistics

def _solver(tmp, name: str, text: str):
    path = Path(tmp) / f"{name}.py"
    path.write_text(text)
    return ok.load_solver(path)


def fixture(tmp, name: str, text: str, surface: dict, sql: str = ""):
    mod = _solver(tmp, name, text)
    eng = dm.Engine(mod, sql)
    slots = dm.Slots(surface["slots"], surface)
    return mod, eng, slots


def gates_for(slots):
    return hf.Gates(slots, {"V2": {"cap": 0.75, "mode": None}}, TASK_TYPE, CALLS)


def channel_fixture(tmp):
    """_CHANNEL_SOLVER with the two-slot surface and every fixture channel rate disclosed as an override."""
    mod, eng, slots = fixture(tmp, "f1_channel_solver", hf._CHANNEL_SOLVER, CHANNEL_SURFACE)
    outs = hf.Outcomes(eng, slots)
    over = dict(hf.parse_rate(x) for x in CHANNEL_OVERRIDES)
    specs, missing = hf.channel_specs(eng, mod, slots, _EmptyLedger(), MODEL, over, briefs=BRIEFS)
    return {"mod": mod, "eng": eng, "slots": slots, "outs": outs, "gates": gates_for(slots),
            "by": {c["id"]: c for c in specs}, "missing": {c["id"]: c for c in missing}}


def zstat(phat, p0, n):
    if not n or p0 in (0, 1):
        return None
    return (phat - p0) / math.sqrt(p0 * (1 - p0) / n)


def exact_binom_two_sided(k: int, n: int, p0: float) -> float:
    """Two-sided exact binomial p-value: the total mass of outcomes no more likely than k."""
    if p0 <= 0:
        return 1.0 if k <= 0 else 0.0
    if p0 >= 1:
        return 1.0 if k >= n else 0.0
    logs = [math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1) + j * math.log(p0)
            + (n - j) * math.log1p(-p0) for j in range(n + 1)]
    top = max(logs)
    w = [math.exp(x - top) for x in logs]
    keep = [wi <= w[k] * (1 + 1e-9) for wi, _ in zip(w, range(n + 1))]
    return min(1.0, sum(wi for wi, kp in zip(w, keep) if kp) / sum(w))


def rec_z(aid, hits, target, n, gate, detail=None, var=None, baselines=None):
    """A Bernoulli-style assertion, or one whose statistic is an average over the six runs of a baseline.

    For an average, the six runs share the baseline-scoped rate, so a binomial SE over n = draws*6 is not the analytic
    variance. `var` is that statistic's exact per-baseline variance (VAR_PER_BASELINE) and `baselines` is the number of
    independent baselines; the SE is sqrt(var/baselines)."""
    phat = hits / n if n else None
    if var is not None and baselines:
        se = math.sqrt(var / baselines)
        rule = "analytic variance of the per-baseline statistic (six correlated runs share the rate)"
    else:
        se = math.sqrt(target * (1 - target) / n) if n else None
        rule = "binomial at n (one independent baseline per draw)"
    z = (phat - target) / se if (se and phat is not None) else None
    ok_ = z is not None and abs(z) <= gate["z_crit"]
    return {"id": aid, "status": "PASS" if ok_ else "FAIL", "statistic": round(phat, 6) if phat is not None else None,
            "hits": hits, "target": target, "n": n, "z": round(z, 4) if z is not None else None,
            "se": round(se, 6) if se else None, "se_rule": rule,
            "var": var, "baselines": baselines,
            "exact_p": None, "pass": ok_, "reason": None if ok_ else
            f"|z|={abs(z):.4f} > z_crit={gate['z_crit']:.4f}" if z is not None else "no statistic", **(detail or {})}


def rec_cell(target, hits, n, gate, tolerance="two-sided normal z"):
    """One binomial cell: z when n*p0 >= 5, exact binomial (p >= alpha/m) when n*p0 < 5."""
    phat = hits / n if n else None
    if target * n < 5:
        p = exact_binom_two_sided(int(hits), int(n), target)
        return {"statistic": round(phat, 6), "hits": hits, "target": target, "n": n, "z": None,
                "exact_p": p, "pass": p >= gate["alpha"] / gate["m"], "tolerance": "exact binomial"}
    z = zstat(phat, target, n)
    return {"statistic": round(phat, 6), "hits": hits, "target": target, "n": n, "z": round(z, 4),
            "exact_p": None, "pass": z is not None and abs(z) <= gate["z_crit"], "tolerance": tolerance}


# ------------------------------------------------------------------ assertions

def f1(cid, draws, seed, by):
    spec, rng, hits = by[cid], random.Random(seed), 0
    for _ in range(draws):
        hit, _ = hf._sample_channel(spec, 0.02, rng)      # one baseline = one draw of the baseline-scoped latent
        hits += bool(hit)
    return hits


def f2(draws, seed):
    rng, hits = random.Random(seed), 0
    rate = {"alpha": 1.0, "beta": 1.0, "mean": 0.5}
    ch = {"latent": "member", "members": ["a", "b"], "slots": [], "batches": None}
    for _ in range(draws):
        e = hf._rate_draw(rate, rng)
        hit, _ = hf._sample_channel(ch, e, rng)
        hits += bool(hit)                                  # P(any of the two members fails) = 2/3, not P(both)
    return hits


def f3(draws, seed, shared):
    rng, hits = random.Random(seed), 0
    rate = {"alpha": 1.0, "beta": 1.0, "mean": 0.5}
    ch = {"latent": "member", "members": ["a"], "slots": [], "batches": None}
    for _ in range(draws):
        e = hf._rate_draw(rate, rng)
        a = hf._sample_channel(ch, e, rng)[0]
        if shared:
            b = hf._sample_channel(ch, e, rng)[0]
        else:
            b = hf._sample_channel(ch, hf._rate_draw(rate, rng), rng)[0]
        hits += bool(a and b)
    return hits


def f4_cancel(tmp):
    """Production Engine/Outcomes: slip:b toggles B-01 ok->bad and B-02 bad->ok, so the pair cancels in the count."""
    _mod, eng, slots = fixture(tmp, "f1_cancel_solver", hf._CHANNEL_SOLVER, CANCEL_SURFACE)
    outs = hf.Outcomes(eng, slots)
    got_one = set(outs.of({("degrade", "slip:b"): {"B-01"}})[0])
    got_two = set(outs.of({("degrade", "slip:b"): {"B-01", "B-02"}})[0])
    want_one, want_two = {"SB1", "SB"}, {"SB1", "SB2"}
    passed = got_one == want_one and got_two == want_two and "SB" not in got_two
    reason = None
    if not passed:
        reason = (f"slip:b {{B-01}} -> {sorted(got_one)} (want {sorted(want_one)}); "
                  f"slip:b {{B-01,B-02}} -> {sorted(got_two)} (want {sorted(want_two)}); "
                  f"count slot SB in the cancelling set: {'SB' in got_two}")
    return {"id": "f4_cancel", "status": "PASS" if passed else "FAIL", "statistic": {"B-01": sorted(got_one),
            "B-01,B-02": sorted(got_two)}, "target": {"B-01": sorted(want_one), "B-01,B-02": sorted(want_two)},
            "n": 1, "z": None, "exact_p": None, "pass": passed, "tolerance": "exact failed sets",
            "reason": reason, "count_slot_passes": "SB" not in got_two}


def f5_joint(draws, seed, cf, gate):
    """2x2 joint table of S1/S2 through the simulate composition: one rate draw, one run-latent sample, Outcomes.of."""
    ch = cf["by"]["duo:link"]
    if ch["rate"].get("point") != 0.3:
        raise ValueError(f"duo:link rate is not the disclosed point 0.3: {ch['rate']}")
    outs, rng = hf.Outcomes(cf["eng"], cf["by_slots"]), random.Random(seed)
    counts = {(0, 0): 0, (0, 1): 0, (1, 0): 0, (1, 1): 0}
    for _ in range(draws):
        e = hf._rate_draw(ch["rate"], rng)
        hit, sl = hf._sample_channel(ch, e, rng)
        failing = {ch["element"]: set(hit)} if hit else {}
        failed = outs.of(failing, cache=False)[0] | set(sl)
        counts[(int("S1" in failed), int("S2" in failed))] += 1
    # tie the composition to the tool: simulate's own marginal for S1 must be the joint table's marginal (0.3)
    prod_slots = cf["by_slots"]
    prod = hf.simulate(cf["eng"], hf.Outcomes(cf["eng"], prod_slots),
                       hf.Gates(prod_slots, {"V2": {"cap": 0.75, "mode": None}}, "long-horizon", 550),
                       [], {}, {}, {}, draws=max(2000, draws // 4), seed=seed, dependence="independent",
                       extent="whole", channels=[ch])["slots"]["S1"]["P_fail"]
    marg = (counts[(1, 0)] + counts[(1, 1)]) / draws
    marginal_ok = abs(prod - marg) < 0.01 and abs(marg - 0.3) < 0.02
    cells = {"00": rec_cell(0.7, counts[(0, 0)], draws, gate), "11": rec_cell(0.3, counts[(1, 1)], draws, gate),
             "01": rec_cell(0.0, counts[(0, 1)], draws, gate), "10": rec_cell(0.0, counts[(1, 0)], draws, gate)}
    passed = all(c["pass"] for c in cells.values())   # the marginal cross-check is report-only, not a gate
    return {"id": "f5_joint", "status": "PASS" if passed else "FAIL", "statistic": cells["00"]["statistic"],
            "target": 0.7, "n": draws, "z": cells["00"]["z"], "exact_p": None, "pass": passed,
            "cells": cells, "counts": {f"{a}{b}": counts[(a, b)] for a, b in counts},
            "independent": {"00": 0.49, "11": 0.09, "01": 0.21, "10": 0.21},
            "marginal_cross_check": {"simulate_S1": prod, "joint_table_S1": round(marg, 6), "pass": marginal_ok,
                                     "rule": "simulate()'s own marginal for S1 equals the joint table's (tie the "
                                             "composition to the tool)"},
            "rule": "P00/P11 normal z; P01/P10 exact binomial (n*p0 = 0 < 5)",
            "marginal_note": ("the marginal cross-check agrees with simulate()" if marginal_ok else
                              "WARNING: the composition's marginal disagrees with simulate()"),
            "reason": None if passed else "; ".join(f"{k}: {v['statistic']} vs {v['target']}"
                                                    for k, v in cells.items() if not v["pass"])}


def simulate_view(cf, channels, *, draws, seed):
    return hf.simulate(cf["eng"], cf["outs"], cf["gates"], [], {}, {}, {}, draws=draws, seed=seed,
                       dependence="independent", extent="whole", channels=channels)


def f7_e2e(draws, seed, cf):
    ch = {"id": "one", "rate": {"point": 0.25, "mean": 0.25}, "element": None, "latent": "run", "members": [],
          "slots": ["S"], "batches": None, "family": "test", "kind": "test"}
    return simulate_view(cf, [ch], draws=draws, seed=seed)["views"]["V2"]["E_average"]


def f7_sd(draws, seed, cf):
    ch = {"id": "sd", "rate": {"point": 0.25, "mean": 0.25}, "element": None, "latent": "run", "members": [],
          "slots": ["S"], "batches": None, "family": "test", "kind": "test"}
    out = simulate_view(cf, [ch], draws=draws, seed=seed)
    return out["views"]["V2"]["P_gate"]["per_rollout_sd"], out["views"]["V2"]["P_gate"]


def f7_shared(draws, seed, cf):
    """q ~ Beta(1,1) once per baseline, six runs: E[average] = 0.75 through simulate (the tool, not a coin loop)."""
    ch = {"id": "q", "rate": {"alpha": 1.0, "beta": 1.0, "mean": 0.5}, "element": None, "latent": "run",
          "members": [], "slots": ["S"], "batches": None, "family": "test", "kind": "test"}
    return simulate_view(cf, [ch], draws=draws, seed=seed)["views"]["V2"]["E_average"]


def f8_geometry(tmp):
    """dm.geometry on dm._SCALE_SOLVER: the declared channel is the only route to U; blanking it blocks."""
    caps = dm.caps_for("v3", {"difficulty_mode": "hard"})
    got = {}
    for name, text in (("declared", dm._SCALE_SOLVER), ("blanked", dm._SCALE_SOLVER.replace("CHANNELS = {",
                                                                                            "_UNUSED = {"))):
        mod = _solver(tmp, f"f1_scale_{name}", text)
        eng = dm.Engine(mod, "")
        slots = dm.Slots(SCALE_SURFACE["slots"], SCALE_SURFACE)
        g = dm.geometry(eng, slots, SCALE_SURFACE, caps)
        got[name] = {"u_exact": g["U_exact"], "verdict": g["views"]["V3"]["U"]["verdict"],
                     "mechanisms": [dm._label(e) for e in eng.mechanisms()],
                     "flippable": g["flippable_slots"]}
    passed = (got["declared"]["u_exact"] == "2/3" and got["declared"]["verdict"] == "PASS"
              and "degrade:slip:class" not in got["declared"]["mechanisms"]
              and got["blanked"]["u_exact"] == "0/1" and got["blanked"]["verdict"] == "BLOCK")
    reason = None if passed else (f"declared {got['declared']} / blanked {got['blanked']} "
                                  f"(want 2/3 PASS without the channel as a mechanism, and 0/1 BLOCK)")
    return {"id": "f8_geometry", "status": "PASS" if passed else "FAIL", "statistic": got,
            "target": {"declared": "2/3 PASS", "blanked": "0/1 BLOCK"}, "n": 1, "z": None, "exact_p": None,
            "pass": passed, "tolerance": "exact", "reason": reason}


def f9_mechanisms(draws, seed, tmp, gate):
    """late/quiet on dm._SOLVER with flat priors: P(both land in one run) is 0.25 independent, 1/3 correlated."""
    mod, eng, slots = fixture(tmp, "f1_dm_solver", dm._SOLVER, dm._surface(), dm._SQL)
    outs, gates = hf.Outcomes(eng, slots), gates_for(slots)
    mechs = [("rule", "late"), ("rule", "quiet")]
    fam = {m: hf.family_of(mod, m, [], {}) for m in mechs}
    src = {m: hf.source_of(mod, m, []) for m in mechs}
    priors = {f: {"alpha": 1.0, "beta": 1.0, "mean": 0.5} for f in fam.values()}
    out = {"independent": hf.simulate(eng, outs, gates, mechs, priors, fam, src, draws=draws, seed=seed,
                                      dependence="independent", extent="whole"),
           "correlated": hf.simulate(eng, outs, gates, mechs, priors, fam, src, draws=draws, seed=seed,
                                     dependence="correlated", extent="whole")}
    pairs = {}
    for dep, rep in out.items():
        lp = rep.get("landing_pairs")
        if lp is None:
            return {"id": "f9_mechanisms", "status": "STUB", "statistic": None, "target": None, "n": 0, "z": None,
                    "exact_p": None, "pass": False,
                    "reason": "hardness_forecast.simulate() does not emit 'landing_pairs' yet (G3 additive field); "
                              "no value is inferred", "sources": {dm._label(m): src[m] for m in mechs}}
        key = next((k for k in (f"{dm._label(mechs[0])}|{dm._label(mechs[1])}",
                                f"{dm._label(mechs[1])}|{dm._label(mechs[0])}",
                                f"{mechs[0][1]}|{mechs[1][1]}", f"{mechs[1][1]}|{mechs[0][1]}") if k in lp), None)
        if key is None or "both" not in (lp.get(key) or {}):
            return {"id": "f9_mechanisms", "status": "STUB", "statistic": None, "target": None, "n": 0, "z": None,
                    "exact_p": None, "pass": False,
                    "reason": f"landing_pairs has no 'both' entry for late|quiet: {sorted(lp)}",
                    "sources": {dm._label(m): src[m] for m in mechs}}
        raw = (rep.get("landing_pair_counts") or {}).get(key) or {}
        pairs[dep] = {"both": float(lp[key]["both"]), "either": lp[key].get("either"), "n": lp[key].get("n"),
                      "runs": raw.get("runs") or lp[key].get("runs") or draws * RUNS, "hits": raw.get("both")}
    cells = {}
    for dep, target in (("independent", 0.25), ("correlated", 1 / 3)):
        n = int(pairs[dep]["runs"])
        hits = pairs[dep].get("hits")
        if not isinstance(hits, int):
            hits = round(pairs[dep]["both"] * n)          # fallback only: the raw counter is preferred
        share = hits / n
        var = VAR_PER_BASELINE[f"f9_{dep}"]
        se = math.sqrt(var / draws) if draws else None
        z = (share - target) / se if se else None
        cells[dep] = {"statistic": round(share, 6), "target": target, "n": n, "hits": hits, "z":
                      round(z, 4) if z is not None else None, "se": round(se, 6) if se else None,
                      "se_rule": "analytic variance of the per-baseline statistic (six correlated runs share the rate)",
                      "var_per_baseline": var, "baselines": draws, "either": pairs[dep]["either"],
                      "exact_p": None, "pass": z is not None and abs(z) <= gate["z_crit"]}
    same_source = len(set(src.values())) < len(mechs)
    passed = all(c["pass"] for c in cells.values()) and not same_source
    return {"id": "f9_mechanisms", "status": "PASS" if passed else "FAIL", "statistic": pairs["independent"]["both"],
            "target": 0.25, "n": int(pairs["independent"]["runs"]), "z": cells["independent"]["z"],
            "exact_p": None, "pass": passed, "cells": cells, "n_unit": "one run of six per baseline",
            "sources": {dm._label(m): src[m] for m in mechs},
            "independent_expected": {"both": 0.25, "either": 0.75},
            "correlated_expected": {"both": 1 / 3, "either": 2 / 3},
            "reason": None if passed else ("late and quiet share a source_of" if same_source else
                                           "; ".join(f"{k}: {v['statistic']} vs {v['target']}" for k, v in cells.items()
                                                     if not v["pass"]))}


def _raises(fn, want=ValueError):
    try:
        fn()
    except want:
        return True
    except Exception:                                      # noqa: BLE001 - any other exception is not a clean refusal
        return False
    return False


SPECS_F10 = ("x=-1", "x=-1,2", "x=nan", "x=nan,1", "x=1,nan", "x=inf", "x=inf,1", "x=1,inf",
              "x=1e400", "x=1e400,1", "x=1,1e400", "x=1e400,1e400", "x=1e308,1", "x=1,1e308",
              "x=1000000001,1", "x=0,0", "x=0,1", "x=1,0", "x=abc", "x=")
F10_CHECKS = frozenset([f"parse_rate({s!r}) raises ValueError" for s in SPECS_F10]
                       + ["undeclared-rate 'ghost' is UNPARAMETERIZED, never zero", "all simulated outputs finite"])


def f10_fail_closed(draws, seed, cf, missing):
    checks = {f"parse_rate({s!r}) raises ValueError": _raises(lambda s=s: hf.parse_rate(s)) for s in SPECS_F10}
    ghost = missing.get("ghost")
    checks["undeclared-rate 'ghost' is UNPARAMETERIZED, never zero"] = (
        ghost is not None and (ghost.get("rate") or {}).get("alpha") is None and "ghost" not in cf["by"])
    chans = [cf["by"][k] for k in ("scale:a", "linked:a", "deleg:a", "pair:b", "duo:ind", "duo:link", "surface:deck")]
    rep = simulate_view(cf, chans, draws=max(32, min(draws, 64)), seed=seed)
    numbers = [rep["views"]["V2"]["E_average"], rep["views"]["V2"]["P_all"], *rep["views"]["V2"]["band_10_90"],
               *rep["views"]["V2"]["P_gate"].values()]
    checks["all simulated outputs finite"] = all(isinstance(x, (int, float)) and math.isfinite(x) for x in numbers)
    passed = all(checks.values())
    bad = [k for k, v in checks.items() if not v]
    reason = None
    if not passed:
        reason = "failed: " + "; ".join(bad)
        if any("1e400" in b for b in bad):
            reason += " (pending G3: parse_rate will reject inf/nan/1e400 Beta parameters)"
    return {"id": "f10_fail_closed", "status": "PASS" if passed else "FAIL", "statistic": sum(checks.values()),
            "target": len(checks), "n": 1, "z": None, "exact_p": None, "pass": passed, "tolerance": "exact",
            "checks": checks, "missing_rate": "UNPARAMETERIZED (channel_specs reports it; never zero)",
            "reason": reason}


def f6_chain():
    return {"id": "f6_chain", "status": "ABSENT", "statistic": None, "target": 0.488, "n": 0, "z": None,
            "exact_p": None, "pass": False,
            "reason": "no chain channel ships in any solver (oracle_kit supports the kind; the rev14 wrapper declares "
                      "only scale:groups and tool_surface:register)"}


# ------------------------------------------------------------------ production-path tests

def production_path(tmp, cf):
    """Always run: one rate draw per baseline per channel, and a sampled member subset reaches the solver as its degrade."""
    out = {}

    # (i) one channel-rate draw per six-run baseline: calls == draws * len(channels), not draws * RUNS * len(channels)
    chans = [{"id": "p1", "rate": {"point": 0.1, "mean": 0.1}, "element": None, "latent": "run", "members": [],
              "slots": ["S"], "batches": None, "family": "test", "kind": "test"},
             {"id": "p2", "rate": {"point": 0.1, "mean": 0.1}, "element": None, "latent": "run", "members": [],
              "slots": ["C"], "batches": None, "family": "test", "kind": "test"}]
    draws = 7
    calls, original = {"n": 0}, hf._rate_draw

    def counted(rate, rng):
        calls["n"] += 1
        return original(rate, rng)

    hf._rate_draw = counted
    try:
        simulate_view(cf, chans, draws=draws, seed=1)
    finally:
        hf._rate_draw = original
    want = draws * len(chans)
    out["rate_draw_once_per_baseline"] = {
        "pass": calls["n"] == want and calls["n"] != draws * RUNS * len(chans),
        "calls": calls["n"], "want": want, "wrong_if_per_run": draws * RUNS * len(chans), "draws": draws,
        "channels": len(chans),
        "rule": "simulate() draws rates once per baseline, outside the six-run loop"}

    # (ii) a sampled member subset reaches the solver as the channel's degrade
    _mod, eng, slots = fixture(tmp, "f1_member_solver", hf._CHANNEL_SOLVER, A_SURFACE)
    outs = hf.Outcomes(eng, slots)
    one = set(outs.of({("degrade", "slip:a"): {"A-01"}})[0])
    both = set(outs.of({("degrade", "slip:a"): {"A-01", "A-02"}})[0])
    out["sampled_members_reach_solver"] = {
        "pass": one == {"S1"} and both == {"S1", "S2"}, "one_member": sorted(one), "full_set": sorted(both),
        "want_one_member": ["S1"], "want_full_set": ["S1", "S2"],
        "rule": "Outcomes.of({('degrade','slip:a'): subset}) fails exactly the slots the sampled members move"}
    # (iii) a sampled subset passes through simulate() into Outcomes.of unchanged for BOTH latents, and the slot report
    # separates P(fail) from P(fails all six): a swapped report or a run-latent expansion is caught deterministically
    _m3, eng3, slots3 = fixture(tmp, "f1_member_solver3", hf._CHANNEL_SOLVER, A_SURFACE)
    outs3, gates3 = hf.Outcomes(eng3, slots3), gates_for(slots3)
    orig_sample, orig_of = hf._sample_channel, hf.Outcomes.of

    def _run(latent, stub, draws=1):
        cap = []

        def _of_rec(self, failing, cache=True):
            cap.append({k: (set(v) if v is not None else None) for k, v in failing.items()})
            return orig_of(self, failing, cache=cache)
        ch = {"id": "p3", "rate": {"point": 1.0, "mean": 1.0}, "element": ("degrade", "slip:a"), "latent": latent,
              "members": ["A-01", "A-02"], "slots": [], "batches": None, "family": "test", "kind": "test"}
        try:
            hf._sample_channel, hf.Outcomes.of = stub, _of_rec
            rep = hf.simulate(eng3, outs3, gates3, [], {}, {}, {}, draws=draws, seed=1,
                              dependence="independent", extent="whole", channels=[ch])
        finally:
            hf._sample_channel, hf.Outcomes.of = orig_sample, orig_of
        return cap, rep

    cap_m, rep_m = _run("member", lambda c, e, rng: ({"A-01"}, set()))
    cap_r, rep_r = _run("run", lambda c, e, rng: ({"A-01"}, set()))
    counter = {"n": 0}

    def _one_in_six(c, e, rng):
        counter["n"] += 1
        return ({"A-01"}, set()) if counter["n"] % RUNS == 1 else (set(), set())
    _cap_s, rep_s = _run("member", _one_in_six)
    got_m = cap_m[0].get(("degrade", "slip:a")) if cap_m else None
    got_r = cap_r[0].get(("degrade", "slip:a")) if cap_r else None
    out["sampled_subset_reaches_solver_through_simulate"] = {
        "pass": got_m == {"A-01"} and got_r == {"A-01"}
        and rep_m["slots"]["S1"]["P_fail"] == 1.0 and rep_m["slots"]["S2"]["P_fail"] == 0.0
        and rep_r["slots"]["S1"]["P_fail"] == 1.0 and rep_r["slots"]["S2"]["P_fail"] == 0.0
        and abs(rep_s["slots"]["S1"]["P_fail"] - 1 / RUNS) < 5e-5   # the report rounds to 4 decimals
        and rep_s["slots"]["S1"]["P_fails_all_six"] == 0.0,
        "subset_member_latent": sorted(got_m or []), "subset_run_latent": sorted(got_r or []),
        "member": {"S1": rep_m["slots"]["S1"], "S2": rep_m["slots"]["S2"]},
        "run": {"S1": rep_r["slots"]["S1"], "S2": rep_r["slots"]["S2"]},
        "one_in_six": rep_s["slots"]["S1"],
        "rule": "the sampled singleton arrives unchanged for both latents (a run-latent expansion fails S2), and the "
                "slot report's P(fail) and P(fails all six) are distinct"}
    return out


# ------------------------------------------------------------------ per-seed run

def run_seed(seed: int, draws: int, tmp, gate) -> dict:
    cf = channel_fixture(tmp)
    cf["by_slots"] = dm.Slots(A_SURFACE["slots"], A_SURFACE)    # f5's joint table reads S1/S2
    res = {"protocol": "F1 acceptance protocol, fourth revision (2026-10-28)", "seed": seed, "draws": draws,
           "runs_per_baseline": RUNS, "model": MODEL,
           "gate": {k: gate[k] for k in ("m", "alpha", "z_crit", "rule")}, "assertions": {}}
    A = res["assertions"]

    A["f1_independent"] = rec_z("f1_independent", f1("scale:a", draws, seed, cf["by"]), 0.5542995960043573, draws,
                                gate, {"unit": "baseline"})
    A["f1_linked"] = rec_z("f1_linked", f1("linked:a", draws, seed, cf["by"]), 0.02, draws, gate,
                           {"unit": "baseline"})
    A["f2_beta_n2"] = rec_z("f2_beta_n2", f2(draws, seed), 2 / 3, draws, gate,
                            {"unit": "baseline", "plug_in": 0.75, "linked": 0.5})
    A["f3_scope"] = rec_z("f3_scope", f3(draws, seed, True), 1 / 3, draws, gate,
                          {"unit": "baseline", "per_run_control": f3(draws, seed, False), "per_run_target": 0.25})
    A["f4_cancel"] = f4_cancel(tmp)
    A["f5_joint"] = f5_joint(draws, seed, cf, gate)
    A["f6_chain"] = f6_chain()
    e2e = f7_e2e(draws, seed, cf)
    A["f7_e2e"] = rec_z("f7_e2e", round(e2e * draws), 0.875, draws, gate, {"unit": "baseline"},
                        var=VAR_PER_BASELINE["f7_e2e"], baselines=draws)
    sd, pgate = f7_sd(draws, seed, cf)
    A["f7_sd"] = rec_z("f7_sd", round(sd * draws), 0.8218, draws, gate,
                       {"unit": "baseline", "exact_target": 1 - 0.75 ** 6 - 0.25 ** 6, "P_gate": pgate})
    A["f7_shared"] = rec_z("f7_shared", round(f7_shared(draws, seed, cf) * draws), 0.75, draws, gate,
                           {"unit": "baseline",
                            "power_note": "the E[average] mean is the same whether q is drawn once per baseline or per "
                                          "run (both 0.75), so this mean does NOT test the per-run defect; no gated "
                                          "spread statistic exists for this shared-uniform construction (f7_sd tests "
                                          "the SD gate under a POINT rate and does not cover q-per-run)"},
                           var=VAR_PER_BASELINE["f7_shared"], baselines=draws)
    A["f8_geometry"] = f8_geometry(tmp)
    A["f9_mechanisms"] = f9_mechanisms(draws, seed, tmp, gate)
    A["f10_fail_closed"] = f10_fail_closed(draws, seed, cf, cf["missing"])
    # every manifest id exactly once, in manifest order
    res["assertions"] = {aid: A[aid] for aid in gate["ids"]}
    assert len(res["assertions"]) == 13, res["assertions"].keys()
    res["production_path"] = production_path(tmp, cf)
    res["provenance"] = fal.report(LEDGER)
    res["status_counts"] = counts(res["assertions"])
    return res


def counts(assertions: dict) -> dict:
    out = {s: 0 for s in STATUSES}
    for r in assertions.values():
        out[r["status"]] += 1
    return out


def print_table(res: dict) -> None:
    print(f"F1 protocol seed {res['seed']} · draws {res['draws']} · m={res['gate']['m']} "
          f"alpha={res['gate']['alpha']} z_crit={res['gate']['z_crit']:.4f}")
    print("  id                  status  statistic      target         n      z/exact_p  pass")
    for aid, r in res["assertions"].items():
        stat = r.get("statistic")
        stat = f"{stat:.6f}" if isinstance(stat, float) else (str(stat) if stat is not None else "-")
        stat = stat if len(stat) <= 13 else stat[:13]
        tgt = r.get("target")
        tgt = f"{tgt:.6f}" if isinstance(tgt, float) else (str(tgt) if tgt is not None else "-")
        tgt = tgt if len(tgt) <= 13 else tgt[:13]
        test = f"p={r['exact_p']:.3g}" if r.get("exact_p") is not None else (
            f"{r['z']:.3f}" if r.get("z") is not None else "-")
        print(f"  {aid:19} {r['status']:6} {stat:13} {tgt:13} {str(r.get('n') or '-'):6} {test:9} {r['pass']}")
        if r["status"] in ("STUB", "ABSENT"):
            print(f"      reason: {r['reason']}")
    print(f"  statuses: {res['status_counts']}")
    for name, p in res["production_path"].items():
        print(f"  production-path {name}: {'PASS' if p['pass'] else 'FAIL'} ({p})")


# ------------------------------------------------------------------ summary and reproducibility

TARGETS = {"f1_independent": 0.5542995960043573, "f1_linked": 0.02, "f2_beta_n2": 2 / 3, "f3_scope": 1 / 3,
           "f7_e2e": 0.875, "f7_sd": 0.8218, "f7_shared": 0.75}
F5_TARGETS = {"00": 0.7, "11": 0.3, "01": 0.0, "10": 0.0}
F9_TARGETS = {"independent": 0.25, "correlated": 1 / 3}
F4_EXPECTED = {"B-01": ["SB", "SB1"], "B-01,B-02": ["SB1", "SB2"]}
F8_EXPECTED = {"declared": ("2/3", "PASS"), "blanked": ("0/1", "BLOCK")}


def _cell_ok(hits, target, n, baselines, var, gate) -> bool:
    """Recompute one comparison from its sufficient statistics, canonical target and analytic variance."""
    if not isinstance(hits, (int, float)) or n is None or n <= 0:
        return False
    phat = hits / n
    if var is not None:
        if not baselines:
            return False
        se = math.sqrt(var / baselines)
    elif target * n < 5:
        return exact_binom_two_sided(int(hits), int(n), target) >= gate["alpha"] / gate["m"]
    else:
        se = math.sqrt(target * (1 - target) / n)
    return se > 0 and abs(phat - target) / se <= gate["z_crit"]


def _number(x) -> bool:
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def _cell_rebuild(hits, target, n, baselines, var, gate) -> tuple:
    """(ok, rebuilt_cell) from sufficient statistics: count valid, SE from the analytic variance, z from the gate."""
    if not _number(hits) or hits < 0 or int(hits) != hits or not isinstance(n, int) or n <= 0 or hits > n:
        return False, {"rebuilt": False, "reason": "invalid count"}
    phat = hits / n
    if var is not None:
        if not isinstance(baselines, int) or baselines <= 0:
            return False, {"rebuilt": False, "reason": "missing baseline count"}
        se = math.sqrt(var / baselines)
        z = (phat - target) / se if se else None
        ok = z is not None and abs(z) <= gate["z_crit"]
        return ok, {"statistic": round(phat, 6), "target": target, "n": n, "baselines": baselines, "hits": hits,
                    "se": round(se, 6), "z": round(z, 4) if z is not None else None, "pass": ok}
    if target * n < 5:
        p = exact_binom_two_sided(int(hits), int(n), target)
        ok = p >= gate["alpha"] / gate["m"]
        return ok, {"statistic": round(phat, 6), "target": target, "n": n, "hits": hits, "exact_p": p, "pass": ok}
    se = math.sqrt(target * (1 - target) / n)
    z = (phat - target) / se if se else None
    ok = z is not None and abs(z) <= gate["z_crit"]
    return ok, {"statistic": round(phat, 6), "target": target, "n": n, "hits": hits, "se": round(se, 6),
                "z": round(z, 4) if z is not None else None, "pass": ok}


def revalidate(row: dict, aid: str, draws: int, gate: dict) -> dict:
    """Rebuild one assertion from sufficient statistics under the CURRENT manifest: canonical targets, analytic
    variances, full cell sets, sample budgets and every non-statistical predicate. A cached status, pass, z, SE,
    target, baseline count or check set is never trusted."""
    if row.get("status") in ("STUB", "ABSENT"):
        return dict(row)
    ok, rebuilt = False, {}
    if aid in TARGETS:
        var = VAR_PER_BASELINE.get(aid)
        base = row.get("n") if var is None else row.get("baselines")
        if row.get("n") != draws or (var is not None and base != draws):
            ok, rebuilt = False, {"rebuilt": False, "reason": "sample/baseline budget != the preregistered draws"}
        else:
            ok, rebuilt = _cell_rebuild(row.get("hits"), TARGETS[aid], row.get("n"), base, var, gate)
    elif aid == "f5_joint":
        cells = row.get("cells") or {}
        ok = set(cells) == set(F5_TARGETS)
        counts = {}
        out = {}
        for k, target in F5_TARGETS.items():
            c = cells.get(k) or {}
            cell_ok, cell = _cell_rebuild(c.get("hits"), target, c.get("n"), c.get("n"), None, gate)
            ok = ok and cell_ok and c.get("n") == draws
            counts[k] = c.get("hits")
            out[k] = cell
        if not all(_number(v) and v >= 0 and int(v) == v for v in counts.values()) or \
                sum(v for v in counts.values() if _number(v)) != draws:
            ok = False                                  # the four counts are a histogram over the baselines
        rebuilt = {"cells": out, "counts": {k: counts[k] for k in counts}}
    elif aid == "f9_mechanisms":
        cells = row.get("cells") or {}
        ok = set(cells) == set(F9_TARGETS)
        out = {}
        for k, target in F9_TARGETS.items():
            c = cells.get(k) or {}
            cell_ok, cell = _cell_rebuild(c.get("hits"), target, c.get("n"), c.get("baselines"),
                                          VAR_PER_BASELINE[f"f9_{k}"], gate)
            ok = ok and cell_ok and c.get("n") == draws * RUNS and c.get("baselines") == draws
            out[k] = cell
        src = row.get("sources") or {}
        ok = ok and set(src) == {"rule:late", "rule:quiet"} and src["rule:late"] != src["rule:quiet"]
        rebuilt = {"cells": out, "sources": row.get("sources")}
    elif aid == "f4_cancel":
        ok = (row.get("statistic") == F4_EXPECTED and row.get("count_slot_passes") is True and row.get("n") == 1)
        rebuilt = {"statistic": row.get("statistic"), "count_slot_passes": row.get("count_slot_passes"), "n": 1}
    elif aid == "f8_geometry":
        st = row.get("statistic") or {}
        ok = all((st.get(k) or {}).get("u_exact") == u and (st.get(k) or {}).get("verdict") == v
                 for k, (u, v) in F8_EXPECTED.items())
        mechs = (st.get("declared") or {}).get("mechanisms")
        ok = ok and isinstance(mechs, list) and "degrade:slip:class" not in mechs
        rebuilt = {"statistic": st}
    elif aid == "f10_fail_closed":
        checks = row.get("checks") or {}
        ok = set(checks) == F10_CHECKS and all(v is True for v in checks.values())
        rebuilt = {"checks": checks, "statistic": len(checks), "target": len(F10_CHECKS)}
    out = dict(row, status="PASS" if ok else "FAIL",
               revalidated="rebuilt from sufficient statistics, canonical targets/variances and the full check set")
    if aid in TARGETS:
        out.pop("cells", None)                          # a scalar assertion carries no cells payload
    out.update(rebuilt)
    out["pass"] = ok
    if "target" not in rebuilt and aid in TARGETS:
        out["target"] = TARGETS[aid]
    return out


def summarize(dirs, acceptance=ACCEPT, gate=None, manifest_path=MANIFEST) -> int:
    man = json.loads(Path(manifest_path).read_text())
    gate = gate or gate_params(man)
    runs = [json.loads((Path(d) / "result.json").read_text()) for d in dirs]
    seeds = [r["seed"] for r in runs]
    if len(set(seeds)) != len(seeds) or sorted(seeds) != sorted(gate["seeds"]):
        print(f"need exactly the pre-registered seeds {gate['seeds']}, got {seeds}", file=sys.stderr)
        return 2
    runs.sort(key=lambda r: r["seed"])
    acceptance = Path(acceptance)
    pooled, per_seed = {}, {}
    for r in runs:
        per_seed[r["seed"]] = {aid: revalidate(a, aid, r["draws"], gate) for aid, a in r["assertions"].items()}
        (acceptance / f"seed{r['seed']}").mkdir(parents=True, exist_ok=True)
        shutil.copyfile(Path(dirs[seeds.index(r["seed"])]) / "result.json",
                        acceptance / f"seed{r['seed']}" / "result.json")
    for aid in gate["ids"]:
        rows = [per_seed[s][aid] for s in sorted(per_seed)]
        statuses = [r["status"] for r in rows]
        kind = pooled_verdict(rows, aid)
        if kind == "FAIL":
            pooled[aid] = {"id": aid, "status": "FAIL", "pass": False, "reason": next(
                (r.get("reason") or "FAIL") for r in rows if r["status"] == "FAIL") if "FAIL" in statuses else
                "unexpected ABSENT in a seed", "per_seed": statuses}
        elif kind == "STUB":
            pooled[aid] = {"id": aid, "status": "STUB", "pass": False, "reason": next(
                r["reason"] for r in rows if r["status"] == "STUB"), "per_seed": statuses}
        elif kind == "ABSENT":
            pooled[aid] = {"id": aid, "status": "ABSENT", "pass": False, "reason": next(
                r["reason"] for r in rows if r["status"] == "ABSENT"), "per_seed": statuses}
        elif aid in ("f5_joint", "f9_mechanisms") and rows[0].get("cells"):
            # multi-cell assertion (f5, f9): pool every cell over the seeds and require all pooled cells
            cells = {}
            for name, cell in rows[0]["cells"].items():
                hits = sum(r["cells"][name]["hits"] for r in rows)
                n = sum(r["cells"][name]["n"] for r in rows)
                if cell["target"] * n < 5:
                    p = exact_binom_two_sided(int(hits), int(n), cell["target"])
                    cells[name] = {"statistic": round(hits / n, 6), "target": cell["target"], "n": n, "hits": hits,
                                   "z": None, "exact_p": p, "pass": p >= gate["alpha"] / gate["m"]}
                elif cell.get("var_per_baseline") or (aid == "f9_mechanisms" and f"f9_{name}" in VAR_PER_BASELINE):
                    bl = sum(r["cells"][name]["baselines"] for r in rows)
                    var = cell.get("var_per_baseline") or VAR_PER_BASELINE[f"f9_{name}"]
                    se = math.sqrt(var / bl)
                    z = (hits / n - cell["target"]) / se
                    cells[name] = {"statistic": round(hits / n, 6), "target": cell["target"], "n": n, "hits": hits,
                                   "z": round(z, 4), "se": round(se, 6), "exact_p": None,
                                   "se_rule": cell.get("se_rule", "analytic per-baseline variance"), "var_per_baseline": var,
                                   "baselines": bl, "pass": abs(z) <= gate["z_crit"]}
                else:
                    z = zstat(hits / n, cell["target"], n)
                    cells[name] = {"statistic": round(hits / n, 6), "target": cell["target"], "n": n, "hits": hits,
                                   "z": round(z, 4), "exact_p": None, "pass": abs(z) <= gate["z_crit"]}
            first = cells[next(iter(cells))]
            pooled[aid] = {"id": aid, "status": "PASS" if all(c["pass"] for c in cells.values()) else "FAIL",
                           "statistic": first["statistic"], "target": first["target"], "n": first["n"],
                           "z": first["z"], "exact_p": first["exact_p"], "cells": cells,
                           "pass": all(c["pass"] for c in cells.values()), "per_seed": [r["status"] for r in rows]}
        elif all(r.get("z") is not None for r in rows) and rows[0].get("hits") is not None:
            hits = sum(r["hits"] for r in rows)
            n = sum(r["n"] for r in rows)
            tgt = rows[0]["target"]
            phat = hits / n
            if aid in VAR_PER_BASELINE:                    # canonical per-baseline variance, never the row's cached var
                se = math.sqrt(VAR_PER_BASELINE[aid] / sum(r["baselines"] for r in rows))
            else:
                se = math.sqrt(TARGETS.get(aid, tgt) * (1 - TARGETS.get(aid, tgt)) / n) if n else None
            z = (phat - tgt) / se if se else None
            pooled[aid] = {"id": aid, "status": "PASS" if z is not None and abs(z) <= gate["z_crit"] else "FAIL",
                           "statistic": round(phat, 6), "hits": hits, "target": tgt, "n": n,
                           "z": round(z, 4) if z is not None else None, "se": round(se, 6) if se else None,
                           "exact_p": None, "pass": z is not None and abs(z) <= gate["z_crit"],
                           "per_seed": [r["status"] for r in rows],
                           "note": "pooled across seeds for report; the gate is the 39 seed-level tests"}
        else:
            passed = all(r["pass"] for r in rows)
            pooled[aid] = {"id": aid, "status": "PASS" if passed else "FAIL", "pass": passed,
                           "per_seed": [r["status"] for r in rows],
                           "statistic": [r.get("statistic") for r in rows]}
    all_seed_tests = [r["pass"] for rows in per_seed.values() for aid, r in rows.items()
                      if not (aid in ABSENT_BY_DESIGN and r["status"] == "ABSENT")]
    all_status = [r["status"] for rows in per_seed.values() for aid, r in rows.items()
                  if not (aid in ABSENT_BY_DESIGN and r["status"] == "ABSENT")]
    # a production-path failure must fail acceptance: the checks exist in every seed and every check passes
    prod_all = [r.get("production_path") or {} for r in runs]
    prod_ok = all(production_ok(r) for r in runs)
    prod_checks = sorted({k for p in prod_all for k in p})
    summary = {
        "protocol": "F1 acceptance protocol, fourth revision (2026-10-28)",
        "manifest": {"path": str(manifest_path), "sha256": hashlib.sha256(Path(manifest_path).read_bytes()).hexdigest(),
                     "ids": gate["ids"], "seeds": gate["seeds"], "draws_per_seed": gate["draws"],
                     "familywise_alpha": gate["alpha"], "multiplicity": man.get("multiplicity")},
        "gate": {k: gate[k] for k in ("m", "alpha", "z_crit", "rule", "draws")},
        "seeds": {str(s): {"statuses": counts(per_seed[s]), "assertions": per_seed[s]} for s in sorted(per_seed)},
        "pooled": pooled,
        "statuses": {
            "seed_level": {s: {k: sum(1 for r in per_seed[s].values() if r["status"] == k) for k in STATUSES}
                           for s in sorted(per_seed)},
            "pooled": {k: sum(1 for r in pooled.values() if r["status"] == k) for k in STATUSES}},
        "overall": {"pass": all(all_seed_tests) and all_status.count("PASS") == len(all_status) and prod_ok
                    and all(r["draws"] == gate["draws"] for r in runs),
                    "seed_tests": len(all_seed_tests), "seed_tests_passed": sum(all_seed_tests),
                    "draws_ok": all(r["draws"] == gate["draws"] for r in runs),
                    "absent_by_design": sorted(aid for aid, r in pooled.items()
                                               if r["status"] == "ABSENT" and aid in ABSENT_BY_DESIGN),
                    "acceptance_complete": all(all_seed_tests) and prod_ok
                    and all(r["draws"] == gate["draws"] for r in runs)
                    and all(aid in ABSENT_BY_DESIGN and r["status"] == "ABSENT"
                            for rows in per_seed.values() for aid, r in rows.items() if r["status"] != "PASS"),
                    "production_path_ok": prod_ok, "production_path_checks": prod_checks,
                    "non_pass": sorted({aid for aid, r in pooled.items() if r["status"] != "PASS"}),
                    "note": "the gate is the 39 SEED-LEVEL tests (13 ids x 3 seeds) plus the mandatory production "
                            "checks and the pre-registered draws; the pooled comparisons are report-only and do not "
                            "enter acceptance; a STUB or ABSENT id never counts as a pass; f6_chain is ABSENT by "
                            "design (no chain channel ships)"},
        "production_path": runs[0].get("production_path"),
        "provenance": runs[0].get("provenance"),
        "run": {"python": sys.version, "platform": platform.platform(),
                "logs": [str(Path(d)) for d in dirs]},
    }
    acceptance.mkdir(parents=True, exist_ok=True)
    (acceptance / "summary.json").write_text(json.dumps(summary, indent=1, default=str) + "\n")
    print_summary(summary)
    return 0 if summary["overall"]["acceptance_complete"] else 1


def print_summary(summary: dict) -> None:
    print(f"F1 acceptance summary · m={summary['gate']['m']} alpha={summary['gate']['alpha']} "
          f"z_crit={summary['gate']['z_crit']:.4f} · seeds {summary['manifest']['seeds']} · "
          f"draws {summary['manifest']['draws_per_seed']}")
    print("  id                  status  statistic      target         n       z/exact_p  pass  per-seed")
    for aid, r in summary["pooled"].items():
        stat = r.get("statistic")
        stat = f"{stat:.6f}" if isinstance(stat, float) else (str(stat) if stat is not None else "-")
        stat = stat if len(stat) <= 13 else stat[:13]
        tgt = r.get("target")
        tgt = f"{tgt:.6f}" if isinstance(tgt, float) else (str(tgt) if tgt is not None else "-")
        tgt = tgt if len(tgt) <= 13 else tgt[:13]
        test = f"p={r['exact_p']:.3g}" if r.get("exact_p") is not None else (
            f"{r['z']:.3f}" if r.get("z") is not None else "-")
        print(f"  {aid:19} {r['status']:6} {stat:13} {tgt:13} {str(r.get('n') or '-'):7} {test:9} "
              f"{str(r['pass']):5} {r.get('per_seed')}")
        if r["status"] in ("STUB", "ABSENT"):
            print(f"      reason: {r['reason']}")
    o = summary["overall"]
    print(f"  gate: {o['seed_tests_passed']}/{o['seed_tests']} seed-level tests pass; statuses {summary['statuses']}")
    print(f"  non-pass ids: {o['non_pass']}; draws_ok={o['draws_ok']}; "
          f"production_path_ok={o.get('production_path_ok')}; acceptance_complete={o['acceptance_complete']}")


SUMS_PATHS = ("support/fix_session_2026-10-25/scripts/f1_protocol.py",
              "support/fix_session_2026-10-25/scripts/f1_acceptance.py",
              "support/fix_session_2026-10-25/scripts/f1_audited_ledger.py",
              "support/fix_session_2026-10-25/f1_acceptance/F1_PROTOCOL_MANIFEST.json",
              "support/fix_session_2026-10-25/f1_acceptance/F1_PROVENANCE_AUDIT.txt",
              "support/fix_session_2026-10-25/f1_acceptance/F1_AUDITED_LEDGER.jsonl",
              "support/fix_session_2026-10-25/f1_acceptance/F1_SNAPSHOT.json",
              "support/fix_session_2026-10-25/f1_acceptance/F1_STATUS.md",
              "support/fix_session_2026-10-25/f1_acceptance/seed1/result.json",
              "support/fix_session_2026-10-25/f1_acceptance/seed2/result.json",
              "support/fix_session_2026-10-25/f1_acceptance/seed3/result.json",
              "support/fix_session_2026-10-25/f1_acceptance/summary.json",
              "support/fix_session_2026-10-25/logs/f1/protocol4/seed1/result.json",
              "support/fix_session_2026-10-25/logs/f1/protocol4/seed2/result.json",
              "support/fix_session_2026-10-25/logs/f1/protocol4/seed3/result.json",
              "support/hardness_ledger/ledger.jsonl")


def write_sums(acceptance=ACCEPT) -> int:
    """Regenerate F1_REPRODUCIBILITY_SHA256SUMS: tools/*.py plus every F1 artifact this harness pins.

    Run after the tools settle (build re-runs it) and after the final protocol run:
      python3 -B .../scripts/f1_protocol.py --write-sums
    """
    root = acceptance.parents[2]                        # Task_Authoring
    lines = []
    for path in sorted((root / "tools").glob("*.py")):
        lines.append((hashlib.sha256(path.read_bytes()).hexdigest(), str(path.relative_to(root))))
    for rel in SUMS_PATHS:
        p = root / rel
        if not p.exists():
            print(f"missing {rel}; list it after it is written", file=sys.stderr)
            return 2
        lines.append((hashlib.sha256(p.read_bytes()).hexdigest(), rel))
    (acceptance / "F1_REPRODUCIBILITY_SHA256SUMS").write_text("\n".join(f"{h}  {p}" for h, p in lines) + "\n")
    print(f"wrote {acceptance / 'F1_REPRODUCIBILITY_SHA256SUMS'} ({len(lines)} entries)")
    return 0


def production_ok(res) -> bool:
    """Every mandatory production-path check must exist and its EVIDENCE must re-derive the check; a cached flag, a
    missing payload or a contradictory payload is never a pass."""
    p = res.get("production_path") or {}
    rate = p.get("rate_draw_once_per_baseline") or {}
    if not (rate.get("draws") == 7 and rate.get("channels") == 2
            and rate.get("calls") == 14                                            # the fixture: 7 baselines x 2 channels
            and rate.get("calls") != 7 * RUNS * 2):
        return False
    sub = p.get("sampled_members_reach_solver") or {}
    if not (sub.get("one_member") == ["S1"] and sub.get("full_set") == ["S1", "S2"]):
        return False
    one = p.get("sampled_subset_reaches_solver_through_simulate") or {}
    m, r, s = one.get("member") or {}, one.get("run") or {}, one.get("one_in_six") or {}
    return (one.get("subset_member_latent") == ["A-01"] and one.get("subset_run_latent") == ["A-01"]
            and (m.get("S1") or {}).get("P_fail") == 1.0 and (m.get("S2") or {}).get("P_fail") == 0.0
            and (r.get("S1") or {}).get("P_fail") == 1.0 and (r.get("S2") or {}).get("P_fail") == 0.0
            and abs((s.get("P_fail") or 0) - 1 / RUNS) < 5e-5 and s.get("P_fails_all_six") == 0.0)


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="f1_protocol.py")
    ap.add_argument("out", nargs="*", type=Path)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--draws", type=int, default=None)
    ap.add_argument("--summarize", action="store_true")
    ap.add_argument("--acceptance-dir", type=Path, default=ACCEPT)
    ap.add_argument("--write-sums", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return protocol_self_test()
    man = manifest()
    gate = gate_params(man)
    if a.write_sums:
        return write_sums(a.acceptance_dir)
    if a.summarize:
        return summarize(a.out, a.acceptance_dir, gate)
    if len(a.out) != 1:
        ap.error("one OUT_DIR per run")
    if a.seed not in gate["seeds"]:
        ap.error(f"seed {a.seed} is not pre-registered (seeds {gate['seeds']})")
    draws = gate["draws"] if a.draws is None else a.draws
    if draws != gate["draws"]:
        print(f"NOT AN ACCEPTANCE RUN: draws {draws} != the pre-registered {gate['draws']}", file=sys.stderr)
        return 2
    out = a.out[0]
    out.mkdir(parents=True, exist_ok=True)
    if not Path(LEDGER).exists():
        print(json.dumps(fal.build(LEDGER, AUDIT), indent=1))
    with sx.scratch_tmp("f1_protocol4_") as tmp:
        res = run_seed(a.seed, draws, tmp, gate)
    res["draws_preregistered"] = gate["draws"]
    (out / "result.json").write_text(json.dumps(res, indent=1, default=str) + "\n")
    print_table(res)
    fal.print_report(res["provenance"])
    counts = res["status_counts"]
    absent_ok = {a["id"] for a in res["assertions"].values()
                 if a["status"] == "ABSENT" and a["id"] == "f6_chain"}    # the one pre-agreed ABSENT
    absent_bad = {k for k, a in res["assertions"].items() if a["status"] == "ABSENT"} - absent_ok
    prod_ok = production_ok(res)
    return 0 if counts["FAIL"] == 0 and counts["STUB"] == 0 and not absent_bad and prod_ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
