#!/usr/bin/env python3
"""UNCALIBRATED policy scores on the real 01_Gradable_Surface.json (FILT split into its two members)."""
import json, random, statistics, itertools
from pathlib import Path
S = json.loads((Path(__file__).resolve().parents[1] / "01_Gradable_Surface.json").read_text())["slots"]
TOT = sum(s["weight"] for s in S)
MEMBER = {"ST3": {"FILT_HOMA"}, "ST4": {"FILT_BRIGHT"}, "V1": {"FILT_HOMA", "FILT_BRIGHT"}}
def movers(s):
    m = set(s.get("mechanisms", [])) - {"FILT"}
    return m | MEMBER.get(s["id"], set())
# rev6 author estimates after the rev5 Opus pre-check (all seven LEAKED there): rules still on the read path are low
P = {"DONE1": .25, "INPUT": .50, "DONE2": .50, "CORR": .45, "ALIAS": .30, "FILT_HOMA": .10, "FILT_BRIGHT": .15, "FOLLOW": .10}
NORM = statistics.NormalDist()
def score(landed, slips=()):
    return 1 - sum(s["weight"] for s in S if movers(s) & landed or s["id"] in slips) / TOT
def failed(landed, slips=()):
    return frozenset(s["id"] for s in S if movers(s) & landed or s["id"] in slips)
def patterns(fs):
    fs = [f for f in fs if f]; par = list(range(len(fs)))
    def find(i):
        while par[i] != i: i = par[i]
        return i
    for i, j in itertools.combinations(range(len(fs)), 2):
        if len(fs[i] ^ fs[j]) <= 1: par[find(i)] = find(j)
    g = {}
    for i in range(len(fs)): g.setdefault(find(i), []).append(i)
    return len(g), (max(map(len, g.values())) / len(fs) if fs else 0)
def sim(scale, rho, n=6000, seed=3):
    r = random.Random(seed); out = dict(avg=[], cap80=0, cap85=0, sd=0, pat=0, full=0, allg=0)
    for _ in range(n):
        runs, fs = [], []
        for _ in range(6):
            z = r.gauss(0, 1)
            landed = {m for m, p in P.items() if NORM.cdf(rho**.5 * z + (1 - rho)**.5 * r.gauss(0, 1)) < p * scale}
            slips = {s["id"] for s in S if not movers(s) and r.random() < .03}
            runs.append(score(landed, slips)); fs.append(failed(landed, slips))
        a, sd = statistics.mean(runs), statistics.pstdev(runs); np_, lg = patterns(fs)
        g = [a < .85, .10 <= sd <= .30, np_ >= 2 and lg <= .5, sum(x > .9999 for x in runs) < 5]
        out["avg"].append(a); out["cap80"] += a < .80; out["cap85"] += g[0]; out["sd"] += g[1]; out["pat"] += g[2]
        out["full"] += g[3]; out["allg"] += all(g)
    return {"E_avg": round(statistics.mean(out["avg"]), 3), "P(avg<80%)": out["cap80"] / n, "P(avg<85%)": out["cap85"] / n,
            "P(SD band)": out["sd"] / n, "P(patterns)": out["pat"] / n, "P(all gates)": out["allg"] / n}
if __name__ == "__main__":
    print(f"UNCALIBRATED · surface weight {TOT}")
    for k, v in {"perfect": set(), "mail and channel history only, no DMs, thread replies or later posts (INPUT DONE2 CORR)": {"INPUT", "DONE2", "CORR"},
                 "list-bound (FILT both, ALIAS)": {"FILT_HOMA", "FILT_BRIGHT", "ALIAS"},
                 "trusts done sources (DONE1 DONE2 INPUT)": {"DONE1", "DONE2", "INPUT"},
                 "all but follow-through": {"FOLLOW"}, "lazy (all land)": set(P)}.items():
        print(f"  {score(v):6.1%}  {k}")
    print("single misses:", {m: f"{score({m}):.1%}" for m in P})
    print("two misses (lowest/highest):", sorted(f"{score(set(c)):.1%} {c}" for c in itertools.combinations(P, 2))[0],
          "...", sorted(f"{score(set(c)):.1%} {c}" for c in itertools.combinations(P, 2))[-1])
    for sc in (1.0, .75, .6, .5):
        for rho in (.3, .6):
            print(f"  scale {sc} rho {rho}: {sim(sc, rho)}")
