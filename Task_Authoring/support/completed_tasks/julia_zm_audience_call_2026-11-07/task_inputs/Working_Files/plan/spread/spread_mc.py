#!/usr/bin/env python3
"""Six-run Monte Carlo on the frozen gradable surface with the /create-difficulty gate rules (UNCALIBRATED).

Gate rules mirrored from Task_Authoring/tools/difficulty_stats.py:
  weighted rate = passed weight / total weight (77); population SD (statistics.pstdev) in [0.10, 0.30];
  failing runs = runs with any failed slot; patterns = single-linkage over failed-slot sets whose symmetric
  difference is <= 1 slot; gate needs >= 2 patterns and largest share <= 50 % (requester margin: < 45 %);
  full passes < 5; average < 0.85 (mode medium).
Run model: each mechanism (R_K1, R_K3, R_K4, R_K5, R_F, R_D, R_E) is missed with its miss rate; a miss fails every
slot listing that mechanism; slots with no mechanism fail at a 5 % slip. Shared thoroughness: a Gaussian copula
within each run (latent correlation rho across all seven mechanisms), so the marginal rates are kept exactly.
Usage: python spread_mc.py [--trials N] [--grid] [--profile K1,K3,K4,K5] [--json out.json]
"""
import argparse, itertools, json, math, random, statistics, sys
from pathlib import Path
from statistics import NormalDist

HERE = Path(__file__).resolve().parent
SURF = HERE.parents[1] / "01_Gradable_Surface.json"
SLOTS = json.loads(SURF.read_text(encoding="utf-8"))["slots"]
TOTAL = sum(s["weight"] for s in SLOTS)
MECHS = ["R_K1", "R_K3", "R_K4", "R_K5", "R_F", "R_D", "R_E"]
UNMAPPED = [i for i, s in enumerate(SLOTS) if not s["mechanisms"]]
ND = NormalDist()

# Base miss rates for the non-block mechanisms (judgement; see 06_Spread_Plan.md section 2).
OTHER_MISS = {"R_F": 0.30, "R_D": 0.10, "R_E": 0.25}


def popcount(x):
    return bin(x).count("1")


def build_tables(spread_states=0):
    """Map (mechanism-miss bitmask, unmapped-slip bitmask) -> (failed-slot bitmask, score).
    spread_states=True models a rubric that grades the 43 Canceled as four per-block rows (the ST1 weight split
    across the blocks) instead of one co-flipping row; the surface itself is unchanged."""
    slot_mech = []
    for s in SLOTS:
        slot_mech.append({MECHS.index(m) for m in s["mechanisms"]})
    weights = [s["weight"] for s in SLOTS]
    table = {}
    for mm in range(1 << len(MECHS)):
        missed = {i for i in range(len(MECHS)) if mm >> i & 1}
        for um in range(1 << len(UNMAPPED)):
            fmask, lost = 0, 0.0
            for j, s in enumerate(SLOTS):
                fail = bool(slot_mech[j] & missed)
                if j in UNMAPPED:
                    fail = bool(um >> UNMAPPED.index(j) & 1)
                if (spread_states == 1 and s["id"] == "S-ST1") or (spread_states == 2 and s["id"] in ("S-ST1", "S-ST2")):
                    # four rubric rows, one per block, weight split evenly; each fails on its own block only
                    share = s["weight"] / 4
                    for b in range(4):
                        if b in missed:
                            fmask |= 1 << (len(SLOTS) + 4 * (s["id"] == "S-ST2") + b)
                            lost += share
                    continue
                if fail:
                    fmask |= 1 << j
                    lost += weights[j]
            table[(mm, um)] = (fmask, (TOTAL - lost) / TOTAL)
    return table


def patterns(fmasks):
    fs = [f for f in fmasks if f]
    n = len(fs)
    par = list(range(n))

    def fd(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for i in range(n):
        for j in range(i + 1, n):
            if popcount(fs[i] ^ fs[j]) <= 1:
                par[fd(i)] = fd(j)
    c = {}
    for i in range(n):
        r = fd(i)
        c[r] = c.get(r, 0) + 1
    return n, len(c), (max(c.values()) if c else 0)


def simulate(find, rho, trials, seed=7, table=None, other=None, slip=0.05, rate_jitter=0.0):
    """find: dict block -> find rate (R_K1..R_K5). Returns gate probabilities and score summaries."""
    table = table or TABLE
    other = other or OTHER_MISS
    rnd = random.Random(seed)
    base_miss = [1 - find["R_K1"], 1 - find["R_K3"], 1 - find["R_K4"], 1 - find["R_K5"],
                 other["R_F"], other["R_D"], other["R_E"]]
    sr = math.sqrt(rho)
    se = math.sqrt(1 - rho)
    acc = dict(sd_low=0, sd_high=0, sd=0, pat45=0, pat50=0, full=0, avg=0, all45=0, all50=0)
    avgs, sds, fulls, npat, big = [], [], [], [], []
    for _ in range(trials):
        miss = base_miss
        if rate_jitter:
            miss = [min(.95, max(.05, m + rnd.uniform(-rate_jitter, rate_jitter))) if k < 4 else m
                    for k, m in enumerate(base_miss)]
        cut = [ND.inv_cdf(m) for m in miss]
        fm, sc = [], []
        for _r in range(6):
            z = rnd.gauss(0, 1)
            mm = 0
            for k in range(7):
                if sr * z + se * rnd.gauss(0, 1) < cut[k]:
                    mm |= 1 << k
            um = 0
            for u in range(len(UNMAPPED)):
                if rnd.random() < slip:
                    um |= 1 << u
            f, s = table[(mm, um)]
            fm.append(f)
            sc.append(s)
        a = sum(sc) / 6
        d = statistics.pstdev(sc)
        nfail, k, b = patterns(fm)
        full = 6 - nfail
        g_sd = 0.10 - 1e-9 <= d <= 0.30 + 1e-9
        g45 = nfail > 0 and k >= 2 and b / nfail < 0.45
        g50 = nfail > 0 and k >= 2 and b / nfail <= 0.50 + 1e-9
        g_full = full < 5
        g_avg = a < 0.85
        acc["sd"] += g_sd
        acc["sd_low"] += d < 0.10 - 1e-9
        acc["sd_high"] += d > 0.30 + 1e-9
        acc["pat45"] += g45
        acc["pat50"] += g50
        acc["full"] += g_full
        acc["avg"] += g_avg
        acc["all45"] += g_sd and g45 and g_full and g_avg
        acc["all50"] += g_sd and g50 and g_full and g_avg
        avgs.append(a)
        sds.append(d)
        fulls.append(full)
        npat.append(k)
        big.append(b / nfail if nfail else 1.0)
    out = {k: v / trials for k, v in acc.items()}
    avgs.sort()
    sds.sort()
    out["E_avg"] = sum(avgs) / trials
    out["avg_p10_p90"] = [avgs[int(.1 * trials)], avgs[int(.9 * trials)]]
    out["median_sd"] = sds[trials // 2]
    out["E_full_passes"] = sum(fulls) / trials
    out["E_patterns"] = sum(npat) / trials
    out["median_largest_share"] = sorted(big)[trials // 2]
    return out


def ladder(table):
    rows = []
    for nm in range(5):
        mm = (1 << nm) - 1
        rows.append((nm, table[(mm, 0)][1]))
    return rows


TABLE = build_tables(0)

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--trials", type=int, default=6000)
    ap.add_argument("--grid", action="store_true")
    ap.add_argument("--profile", action="append", default=[])
    ap.add_argument("--spread-states", type=int, default=0, help="0 surface as is; 1 ST1 per block; 2 ST1+ST2 per block")
    ap.add_argument("--jitter", type=float, default=0.0)
    ap.add_argument("--other", default="")
    ap.add_argument("--json")
    a = ap.parse_args()
    table = build_tables(a.spread_states)
    other = dict(OTHER_MISS)
    if a.other:
        f, d, e = (float(x) for x in a.other.split(","))
        other = {"R_F": f, "R_D": d, "R_E": e}
    print("total weight", TOTAL, "ladder (blocks missed -> score, F/D/E found, no slip):",
          ", ".join(f"{n}:{s:.3f}" for n, s in ladder(table)), file=sys.stderr)
    results = []
    profiles = []
    if a.grid:
        levels = [0.35, 0.40, 0.45, 0.50, 0.55, 0.60, 0.65]
        profiles = list(itertools.combinations_with_replacement(levels, 4))
    for p in a.profile:
        profiles.append(tuple(float(x) for x in p.split(",")))
    for prof in profiles:
        find = dict(zip(["R_K1", "R_K3", "R_K4", "R_K5"], prof))
        row = {"find": prof}
        for rho in (0.0, 0.6):
            row[f"rho{rho}"] = simulate(find, rho, a.trials, table=table, other=other, rate_jitter=a.jitter)
        results.append(row)
        r0, r6 = row["rho0.0"], row["rho0.6"]
        print("find %-24s | rho0 E%.3f sd%.2f p45 %.2f full %.2f all45 %.2f | rho.6 E%.3f sd%.2f p45 %.2f full %.2f all45 %.2f" % (
            ",".join(f"{x:.2f}" for x in prof), r0["E_avg"], r0["sd"], r0["pat45"], r0["full"], r0["all45"],
            r6["E_avg"], r6["sd"], r6["pat45"], r6["full"], r6["all45"]))
    if a.json:
        Path(a.json).write_text(json.dumps(results, indent=1), encoding="utf-8")
