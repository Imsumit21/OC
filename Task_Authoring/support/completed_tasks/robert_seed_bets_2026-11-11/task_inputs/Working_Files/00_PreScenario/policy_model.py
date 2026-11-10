#!/usr/bin/env python3
"""Pre-scenario policy model (UNCALIBRATED). Recommended storyline A sketch surface (the seed, bet by bet).
Scores whole policies, single misses and a six-run Monte Carlo of the gates: corrected average < 90 % (Easy), < 5 full
passes, population SD 0.10-0.30, >= 2 failure patterns with the largest <= 50 %. Design aid only: landing rates are design
priors, not measured Opus 5.5 rates (learnings §9). Structure follows the LLC task's model."""
import itertools, json, os, random, statistics
from statistics import NormalDist
H = os.path.dirname(os.path.abspath(__file__))
SURF = json.load(open(os.path.join(H, "sketch_surface.json")))["slots"]
SLOTS = [(s["id"], s["weight"], s["mechanisms"]) for s in SURF]
TOTAL = sum(w for _, w, _ in SLOTS)
MECHS = ["RET", "OFF", "ORPH", "CORR", "ALIAS", "OVR", "CURR"]
# P(mechanism lands = the run misses the deciding record). Anchors: Robert wind-down baselines landed 2.67 of 5 traps per
# run (0.53 each); LLC baselines: VO 5/6, ENG-2462 3/6, DD 1/6, CF stacks 1/6, layer 5/6 (mean 0.50); Frederick bridge 0.50.
P = {"RET": 0.45, "OFF": 0.50, "ORPH": 0.40, "CORR": 0.45, "ALIAS": 0.40, "OVR": 0.45, "CURR": 0.25}
CAP, TARGET, SLIP = 0.90, 0.82, 0.03
def failed(landed, slips=frozenset()):
    return frozenset(s for s, w, m in SLOTS if any(x in landed for x in m) or s in slips)
def score(landed, slips=frozenset()):
    f = failed(landed, slips)
    return 1 - sum(w for s, w, m in SLOTS if s in f) / TOTAL
def patterns(fsets):
    fs = [f for f in fsets if f]
    if not fs:
        return 0, 0.0
    par = list(range(len(fs)))
    def find(i):
        while par[i] != i:
            par[i] = par[par[i]]; i = par[i]
        return i
    for i, j in itertools.combinations(range(len(fs)), 2):
        if len(fs[i] ^ fs[j]) <= 1:
            par[find(i)] = find(j)
    g = {}
    for i in range(len(fs)):
        g.setdefault(find(i), []).append(i)
    return len(g), max(len(v) for v in g.values()) / len(fs)
def sim(scale=1.0, rho=0.35, n=20000, seed=11, cap=CAP):
    N = NormalDist(); rnd = random.Random(seed)
    R = {"avg": [], "cap": 0, "sd": 0, "full": 0, "pat": 0, "all": 0}
    plain = [s for s, w, m in SLOTS if not m]
    for _ in range(n):
        runs, fsets = [], []
        for _ in range(6):
            z = rnd.gauss(0, 1); landed = set()
            for m in MECHS:
                x = (rho ** .5) * z + ((1 - rho) ** .5) * rnd.gauss(0, 1)
                if N.cdf(x) < P[m] * scale:
                    landed.add(m)
            slips = {s for s in plain if rnd.random() < SLIP}
            runs.append(score(landed, slips)); fsets.append(failed(landed, slips))
        a, sd = statistics.mean(runs), statistics.pstdev(runs)
        full = sum(1 for r in runs if r >= .9999); npat, big = patterns(fsets)
        g = [a < cap, .10 <= sd <= .30, full < 5, npat >= 2 and big <= .5]
        R["avg"].append(a)
        for k, ok in zip(["cap", "sd", "full", "pat"], g):
            R[k] += ok
        R["all"] += all(g)
    return {"E": statistics.mean(R["avg"]), **{k: R[k] / n for k in ["cap", "sd", "full", "pat", "all"]}}
def main():
    fl = sum(w for _, w, m in SLOTS if m)
    print(f"UNCALIBRATED · {len(SLOTS)} slots, total weight {TOTAL}, flippable {fl} ({fl / TOTAL:.1%}), weight-5 slots {sum(1 for _, w, _ in SLOTS if w == 5)}")
    print("\nUnit of discovery: weight each rule can flip (share of total; gate: none over half)")
    for m in MECHS:
        w = sum(x for _, x, mm in SLOTS if m in mm)
        print(f"  {m:6} {w:3d}  {w / TOTAL:5.1%}")
    print("\nWhole policies")
    pol = {
     "Perfect": set(),
     "Adds up the Processed notices by date, reads nothing else": set(MECHS),
     "Notices, the method and the payee project; no older Slack, no other mail": {"RET", "OFF", "ORPH", "CORR", "ALIAS", "OVR"},
     "Thorough except older founder-channel history": {"RET", "OVR"},
     "Thorough except mail beyond the notices": {"OFF", "CORR", "ALIAS"},
     "Thorough except #leapblock": {"ORPH"},
     "Thorough, lets the payment date decide every game": {"OVR"},
     "Thorough, takes the bank's notice as money gone for good": {"RET"},
     "Thorough, treats every wire as a cost": {"CORR"},
     "Thorough, treats the notice currency as USD": {"CURR"},
    }
    for k, v in pol.items():
        print(f"  {score(v):6.1%}  {k}  [lands: {', '.join(sorted(v)) or '-'}]")
    print("\nSingle misses"); 
    for m in MECHS:
        print(f"  {m:6} {score({m}):6.1%}")
    pairs = sorted((score({a, b}), a, b) for a, b in itertools.combinations(MECHS, 2))
    print("\nHighest pair:", f"{pairs[-1][1]}+{pairs[-1][2]} {pairs[-1][0]:.1%}", "· lowest pair:", f"{pairs[0][1]}+{pairs[0][2]} {pairs[0][0]:.1%}")
    print("Single misses that stay at or above the 90 % cap:", [m for m in MECHS if score({m}) >= CAP] or "none")
    pf = 1.0
    for m in MECHS:
        pf *= 1 - P[m]
    print(f"\nP(one run catches every trap) ~ {pf:.3f} (independence) -> E[full passes of 6] ~ {6 * pf:.2f}; traps landing per run at design rates {sum(P.values()):.2f}")
    print("\nSix-run Monte Carlo (landing scale x rho), Easy cap 90 %")
    print("  scale  rho   E[avg]  P(<90)  P(SD)  P(<5 full)  P(patterns)  P(all gates)")
    for sc, rho in [(1.0, .3), (1.0, .6), (.8, .35), (.7, .35), (.6, .35), (.6, .6), (.5, .35), (.4, .35), (.35, .35), (.3, .35), (.25, .35)]:
        r = sim(sc, rho)
        print(f"  {sc:4.2f}  {rho:4.2f}  {r['E']:6.1%}  {r['cap']:6.2f}  {r['sd']:5.2f}  {r['full']:10.2f}  {r['pat']:11.2f}  {r['all']:12.2f}")
if __name__ == "__main__":
    main()
