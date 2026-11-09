#!/usr/bin/env python3
"""Pre-scenario policy model (UNCALIBRATED). Scores the sketch on three row shapes against the platform gates (medium, < 85 %)
and the requester's hard bar (< 70 %, design target E[avg] <= 62 %). Design aid only (learnings §9). Structure follows the sibling
task's model. Miss rates come from census_C5_run_habits.md (unpointed carriers, n = 6 per trap) plus judgement; they are not
measured on this task, and every rate there comes from other personas. Rows with no trap slip at SLIP (C5: added rows pass 88-96 %)."""
import itertools, json, os, random, statistics
from statistics import NormalDist
H = os.path.dirname(os.path.abspath(__file__))
MECHS = ["OPT", "ADV", "TOLD", "SIDE", "BOARD", "ASOF", "ALIAS", "CAP"]
ALLM = MECHS + ["FAM"]
# OPT is pointed (Leonard's Feb 12 list says "Carta terminations"), so it is a low-miss channel: C5 pointed traps land near 6/6 caught.
P = {"OPT": 0.20, "ADV": 0.40, "TOLD": 0.45, "SIDE": 0.50, "BOARD": 0.50, "ASOF": 0.45, "ALIAS": 0.25, "CAP": 0.80, "FAM": 0.50}
SLIP, Q = 0.05, 0.80   # Q: a landed trap fails each of its rows with this chance (misses are partial, not all-or-nothing)
def load(n):
    return [(s["id"], s["weight"], s["mechanisms"]) for s in json.load(open(os.path.join(H, n)))["slots"]]
def failed(SL, landed, slips=frozenset(), rnd=None):
    return frozenset(s for s, w, m in SL if s in slips or any(x in landed for x in m) and (rnd is None or rnd.random() < Q))
def score(SL, landed, slips=frozenset()):
    f = failed(SL, landed, slips)
    return 1 - sum(w for s, w, m in SL if s in f) / sum(w for _, w, _ in SL)
def score_f(SL, f):
    return 1 - sum(w for s, w, m in SL if s in f) / sum(w for _, w, _ in SL)
def patterns(fsets):
    fs = [f for f in fsets if f]
    if not fs: return 0, 0.0
    par = list(range(len(fs)))
    def find(i):
        while par[i] != i:
            par[i] = par[par[i]]; i = par[i]
        return i
    for i, j in itertools.combinations(range(len(fs)), 2):
        if len(fs[i] ^ fs[j]) <= 1: par[find(i)] = find(j)
    g = {}
    for i in range(len(fs)): g.setdefault(find(i), []).append(i)
    return len(g), max(len(v) for v in g.values()) / len(fs)
def sim(SL, scale=1.0, rho=0.15, n=6000, seed=11):
    N = NormalDist(); rnd = random.Random(seed); plain = [s for s, w, m in SL if not m]
    A = []; c = dict(hard=0, le62=0, plat=0, sd=0, full=0, pat=0, allplat=0, allhard=0)
    for _ in range(n):
        runs, fsets = [], []
        for _ in range(6):
            z = rnd.gauss(0, 1); landed = set()
            for m in ALLM:
                x = (rho ** .5) * z + ((1 - rho) ** .5) * rnd.gauss(0, 1)
                if N.cdf(x) < min(P[m] * scale, .97): landed.add(m)
            slips = {s for s in plain if rnd.random() < SLIP}
            f = failed(SL, landed, slips, rnd); runs.append(score_f(SL, f)); fsets.append(f)
        a, sd = statistics.mean(runs), statistics.pstdev(runs)
        full = sum(1 for r in runs if r >= .9999); npat, big = patterns(fsets)
        ok = .10 <= sd <= .30 and full < 5 and npat >= 2 and big <= .5
        A.append(a); c["hard"] += a < .70; c["le62"] += a <= .62; c["plat"] += a < .85; c["sd"] += .10 <= sd <= .30
        c["full"] += full < 5; c["pat"] += npat >= 2 and big <= .5; c["allplat"] += ok and a < .85; c["allhard"] += ok and a < .70
    return {"E": statistics.mean(A), **{k: v / n for k, v in c.items()}}
def main():
    SL = load("sketch_surface.json"); T = sum(w for _, w, _ in SL)
    fl = sum(w for _, w, m in SL if m)
    print(f"UNCALIBRATED · planning shape (row per write): {len(SL)} rows, weight {T}, flippable {fl} ({fl / T:.1%}), always-pass share {1 - fl / T:.1%}, weight-5 rows {sum(1 for _, w, _ in SL if w == 5)}")
    print("\nUnit of discovery: weight each trap can flip (share of total; gate: none over half; C5 wants heavy traps at 12-16 %)")
    for m in MECHS:
        w = sum(x for _, x, mm in SL if m in mm); r = sum(1 for _, x, mm in SL if m in mm)
        print(f"  {m:6} rows {r:3d}  weight {w:3d}  {w / T:5.1%}  design miss {P[m]:.2f}")
    print(f"(Whole policies and single misses below take every row of a landed trap; the Monte Carlo fails each row at Q = {Q}.)")
    print("\nWhole policies")
    pol = {"Perfect": set(), "Owner list and Carta search only, trusts the Feb 12 list": {"ADV", "TOLD", "SIDE", "BOARD", "ASOF", "CAP", "ALIAS"},
           "Thorough except mail older than 2025": {"SIDE", "ALIAS", "CAP"}, "Thorough except DMs": {"TOLD"},
           "Thorough, trusts the owner list's share column": {"ADV"}, "Thorough, never opens Carta": {"OPT", "ASOF"},
           "Thorough, answers KPMG with today's holdings": {"ASOF"}, "Reads nothing beyond the anchors": set(MECHS)}
    for k, v in pol.items(): print(f"  {score(SL, v):6.1%}  {k}  [{', '.join(sorted(v)) or '-'}]")
    print("\nSingle misses"); print("  " + "  ".join(f"{m} {score(SL, {m}):.1%}" for m in MECHS))
    pf = 1.0
    for m in MECHS: pf *= 1 - P[m]
    print(f"\nP(one run catches every trap) ~ {pf:.3f}; E[full passes of 6] ~ {6 * pf:.2f}; traps landing per run at design rates {sum(P.values()):.2f}")
    print("\nSix-run Monte Carlo, planning shape (scale multiplies every miss rate)")
    print("  scale  rho   E[avg]  P(<70)  P(<=62)  P(<85)  P(SD)  P(<5 full)  P(patterns)  P(all, platform)  P(all, hard bar)")
    for sc, rho in [(1.0, .15), (1.0, .35), (.85, .15), (.85, .35), (.7, .15), (.7, .35), (.5, .15), (.5, .35)]:
        r = sim(SL, sc, rho)
        print(f"  {sc:4.2f}  {rho:4.2f}  {r['E']:6.1%}  {r['hard']:6.2f}  {r['le62']:7.2f}  {r['plat']:6.2f}  {r['sd']:5.2f}  {r['full']:10.2f}  {r['pat']:11.2f}  {r['allplat']:16.2f}  {r['allhard']:16.2f}")
    print("\nRow shape (dilution), scale x rho .15")
    print("  shape         rows  weight  always-pass   scale 1.0: E / P(all,hard) / P(all,platform)   scale .7: E / P(all,hard) / P(all,platform)")
    for nm, f in [("sampled", "sketch_surface_sampled.json"), ("row per write", "sketch_surface.json"), ("heavy", "sketch_surface_heavy.json")]:
        X = load(f); t = sum(w for _, w, _ in X); ap = sum(w for _, w, m in X if not m) / t
        a, b = sim(X, 1.0), sim(X, .7)
        print(f"  {nm:13} {len(X):4d}  {t:6d}  {ap:10.1%}   {a['E']:6.1%} / {a['allhard']:.2f} / {a['allplat']:.2f}                  {b['E']:6.1%} / {b['allhard']:.2f} / {b['allplat']:.2f}")
def variant():
    X = load("sketch_surface_variantH.json"); t = sum(w for _, w, _ in X)
    print(f"\nVariant H (hard-leaning): {len(X)} rows, weight {t}, always-pass {sum(w for _, w, m in X if not m) / t:.1%}")
    for m in ALLM:
        w = sum(x for _, x, mm in X if m in mm)
        if w: print(f"  {m:6} weight {w:3d}  {w / t:5.1%}  design miss {P[m]:.2f}")
    print("  scale  rho   E[avg]  P(<70)  P(<=62)  P(<85)  P(SD)  P(patterns)  P(all, platform)  P(all, hard bar)")
    for sc, rho in [(1.0, .15), (1.0, .35), (.85, .15), (.85, .35), (.7, .15), (.7, .35)]:
        r = sim(X, sc, rho)
        print(f"  {sc:4.2f}  {rho:4.2f}  {r['E']:6.1%}  {r['hard']:6.2f}  {r['le62']:7.2f}  {r['plat']:6.2f}  {r['sd']:5.2f}  {r['pat']:11.2f}  {r['allplat']:16.2f}  {r['allhard']:16.2f}")
    need = sum(w * P[m] for m in ALLM for w in [sum(x for _, x, mm in X if m in mm) / t]) * Q
    print(f"  expected miss weight at design rates (sum of share x miss x Q) ~ {need:.3f}; 62 % needs about 0.38")
if __name__ == "__main__":
    main()
    variant()
