#!/usr/bin/env python3
"""Pre-scenario policy model (UNCALIBRATED). Storyline A sketch surface (Domino Delights bug carry-over into Linear).
Scores whole policies, single misses and a six-run Monte Carlo of the Medium gates (corrected avg < 85 %, < 5 full passes,
population SD 0.10-0.30, >= 2 failure patterns with the largest <= 50 %). Adapted from Samuel's model; the engine is
unchanged, the surface, policies and rates are this task's. Design aid only: landing rates are not measured rates."""
import itertools, json, random, statistics, os
from statistics import NormalDist
HERE = os.path.dirname(os.path.abspath(__file__))
SURF = json.load(open(os.path.join(HERE, "sketch_surface.json")))["slots"]
SLOTS = [(s["id"], s["weight"], s["mechanisms"]) for s in SURF]
TOTAL = sum(w for _, w, _ in SLOTS)
MECHS = ["GONE", "LINE", "BACK", "ELSE", "ALIAS", "FILT", "FOLLOW", "TREE"]
P = {"GONE": 0.50, "LINE": 0.45, "BACK": 0.40, "ELSE": 0.35, "ALIAS": 0.30, "FILT": 0.35, "FOLLOW": 0.40, "TREE": 0.30}
# Ledger view: Opus 5.5 family means where a family has records (done_gap .50, superseding .17, completion_elsewhere .20,
# exact_predicate .33, scope_alias .20); house_rule has no records, so it keeps the design rate.
LEDGER = {"GONE": 0.50, "LINE": 0.50, "BACK": 0.17, "ELSE": 0.20, "ALIAS": 0.20, "FILT": 0.33, "FOLLOW": 0.40, "TREE": 0.50}
CAP, BASE_SLIP = 0.85, 0.03
score = lambda landed, slips=frozenset(): 1 - sum(w for sid, w, m in SLOTS if any(x in landed for x in m) or sid in slips) / TOTAL
failed = lambda landed, slips=frozenset(): frozenset(sid for sid, w, m in SLOTS if any(x in landed for x in m) or sid in slips)
def patterns(fsets):
    fs = [f for f in fsets if f]
    if not fs: return 0, 0.0
    parent = list(range(len(fs)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]; i = parent[i]
        return i
    for i, j in itertools.combinations(range(len(fs)), 2):
        if len(fs[i] ^ fs[j]) <= 1: parent[find(i)] = find(j)
    g = {}
    for i in range(len(fs)): g.setdefault(find(i), []).append(i)
    return len(g), max(len(x) for x in g.values()) / len(fs)
def sim(rates, scale=1.0, rho=0.35, n=20000, seed=11):
    N, rnd = NormalDist(), random.Random(seed)
    r = {"avg": [], "cap": 0, "sd": 0, "full": 0, "pat": 0, "all": 0}
    for _ in range(n):
        runs, fs = [], []
        for _ in range(6):
            z = rnd.gauss(0, 1)
            landed = {m for m in MECHS if N.cdf((rho ** .5) * z + ((1 - rho) ** .5) * rnd.gauss(0, 1)) < rates[m] * scale}
            slips = {sid for sid, w, mm in SLOTS if not mm and rnd.random() < BASE_SLIP}
            runs.append(score(landed, slips)); fs.append(failed(landed, slips))
        a, sd = statistics.mean(runs), statistics.pstdev(runs)
        full = sum(1 for x in runs if x >= .9999); npat, big = patterns(fs)
        g = [a < CAP, .10 <= sd <= .30, full < 5, npat >= 2 and big <= .5]
        r["avg"].append(a)
        for k, ok in zip(["cap", "sd", "full", "pat"], g): r[k] += ok
        r["all"] += all(g)
    return {"E": statistics.mean(r["avg"]), **{k: r[k] / n for k in ["cap", "sd", "full", "pat", "all"]}}
def main():
    fl = sum(w for _, w, m in SLOTS if m)
    print(f"UNCALIBRATED · surface: {len(SLOTS)} slots, total weight {TOTAL}, mechanism-flippable {fl} ({fl / TOTAL:.1%})")
    print("\nWhole policies")
    pol = {"Perfect": set(),
     "Canvas ticks at face value, nothing else": set(MECHS),
     "Stays inside the canvas, otherwise thorough": {"FILT", "BACK"},
     "Trusts merged, states and fix claims, otherwise thorough": {"LINE", "TREE", "ELSE"},
     "Reads everything, never asks what the live build contains": {"GONE", "LINE"},
     "Never opens comments on tickets outside the tree": {"ALIAS", "FOLLOW"},
     "Never reads #builds": {"ELSE"},
     "Never reads 1:1 DMs beyond Arthur's": {"BACK"},
     "Right calls, misses the note rule": {"FOLLOW"}}
    for k, v in pol.items(): print(f"  {score(v):6.1%}  {k}  [lands: {', '.join(sorted(v)) or '-'}]")
    print("\nSingle misses")
    for m in MECHS: print(f"  {m:6} {score({m}):6.1%}")
    print("\nPairs at or above the 85 % cap:", [f"{a}+{b}" for a, b in itertools.combinations(MECHS, 2) if score({a, b}) >= CAP] or "none")
    pf = 1.0
    for m in MECHS: pf *= 1 - P[m]
    print(f"\nP(one run catches every trap) ~ {pf:.3f} (independence); expected landings per run at design rates {sum(P.values()):.2f}")
    print("\nOne pre-check run under the narrow-miss rule (one cause under 15 % caps /hardness at 2), independence")
    for sc in (1.0, .7, .5):
        ok = 0.0
        for k in range(len(MECHS) + 1):
            for c in itertools.combinations(MECHS, k):
                pr = 1.0
                for m in MECHS: pr *= (P[m] * sc) if m in c else 1 - P[m] * sc
                if k >= 2 or (k == 1 and 1 - score(set(c)) >= .15): ok += pr
        print(f"  scale {sc:4.2f}: P(two or more causes, or one cause losing 15 % or more) = {ok:.2f}")
    print("\nSix-run Monte Carlo, design rates (scale x rho)\n  scale  rho   mean-land  E[avg]  P(cap)  P(SD)  P(<5 full)  P(pat)  P(all)")
    for sc, rho in [(1, .3), (1, .6), (.8, .35), (.7, .35), (.6, .35), (.6, .6), (.5, .35), (.4, .35), (.3, .35)]:
        r = sim(P, sc, rho)
        print(f"  {sc:4.2f}  {rho:4.2f}  {sum(P.values()) / 8 * sc:8.2f}  {r['E']:6.1%}  {r['cap']:6.2f}  {r['sd']:5.2f}  {r['full']:9.2f}  {r['pat']:6.2f}  {r['all']:6.2f}")
    print("\nSix-run Monte Carlo, ledger view (scale x rho)")
    for sc, rho in [(1, .35), (.7, .35), (.5, .35)]:
        r = sim(LEDGER, sc, rho)
        print(f"  {sc:4.2f}  {rho:4.2f}  {sum(LEDGER.values()) / 8 * sc:8.2f}  {r['E']:6.1%}  {r['cap']:6.2f}  {r['sd']:5.2f}  {r['full']:9.2f}  {r['pat']:6.2f}  {r['all']:6.2f}")
if __name__ == "__main__": main()
