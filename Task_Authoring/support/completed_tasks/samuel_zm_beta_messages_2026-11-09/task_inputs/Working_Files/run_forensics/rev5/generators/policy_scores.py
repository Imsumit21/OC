#!/usr/bin/env python3
"""Whole-policy and single-miss scores on the real gradable surface (UNCALIBRATED design aid, learnings §42).
Gates: requester bar (corrected avg < 80 %) and the assigned Medium cap (< 85 %), < 5 full passes, population SD 0.10-0.30,
>= 2 failure patterns with the largest <= 50 %. Landing rates are design priors, not measured Opus 5.5 rates."""
import itertools, json, os, random, statistics
from statistics import NormalDist
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
SL = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))["slots"]
IDS = json.load(open(os.path.join(HERE, "ids.json")))
P = IDS["rates"]
MECHS = list(P)
SLOTS = [(s["id"], s["weight"], s.get("mechanisms") or [], s["class"]) for s in SL]
TOTAL = sum(w for _, w, _, _ in SLOTS)
SLIP = 0.03
# latent groups: mechanisms found by a shared behaviour are correlated beyond the run-level latent
SHARED = {"DONE": "code", "BUILT": "code", "CORR": "thread", "QA": "thread"}


def score(l, slips=frozenset()):
    return 1 - sum(w for i, w, m, _ in SLOTS if set(m) & l or i in slips) / TOTAL


def failed(l, slips=frozenset()):
    return frozenset(i for i, w, m, _ in SLOTS if set(m) & l or i in slips)


def patterns(fs):
    fs = [f for f in fs if f]
    if not fs:
        return 0, 0.0
    par = list(range(len(fs)))

    def find(i):
        while par[i] != i:
            par[i] = par[par[i]]
            i = par[i]
        return i
    for i, j in itertools.combinations(range(len(fs)), 2):
        if len(fs[i] ^ fs[j]) <= 1:
            par[find(i)] = find(j)
    g = {}
    for i in range(len(fs)):
        g.setdefault(find(i), []).append(i)
    return len(g), max(len(x) for x in g.values()) / len(fs)


def sim(scale=1.0, rho=0.35, shared=0.25, n=12000, seed=7):
    N = NormalDist()
    r = random.Random(seed)
    out = {"avg": [], "bar": 0, "cap": 0, "sd": 0, "full": 0, "pat": 0, "all": 0, "allcap": 0}
    for _ in range(n):
        runs, fs = [], []
        for _ in range(6):
            z = r.gauss(0, 1)
            lat = {"code": r.gauss(0, 1), "thread": r.gauss(0, 1)}
            land = set()
            for m in MECHS:
                g = SHARED.get(m)
                a, b = rho, (shared if g else 0.0)
                x = (a ** .5) * z + (b ** .5) * (lat[g] if g else 0) + ((1 - a - b) ** .5) * r.gauss(0, 1)
                if N.cdf(x) < P[m] * scale:
                    land.add(m)
            sl = {i for i, w, mm, c in SLOTS if not mm and r.random() < SLIP}
            runs.append(score(land, sl))
            fs.append(failed(land, sl))
        a, sd = statistics.mean(runs), statistics.pstdev(runs)
        fullp = sum(1 for x in runs if x >= .9999)
        npat, big = patterns(fs)
        g = [a < .80, .10 <= sd <= .30, fullp < 5, npat >= 2 and big <= .5]
        out["avg"].append(a)
        out["bar"] += g[0]; out["cap"] += a < .85; out["sd"] += g[1]; out["full"] += g[2]; out["pat"] += g[3]
        out["all"] += all(g); out["allcap"] += all([a < .85] + g[1:])
    return {"E": statistics.mean(out["avg"]), **{k: out[k] / n for k in ("bar", "cap", "sd", "full", "pat", "all", "allcap")}}


def main():
    flip = sum(w for _, w, m, _ in SLOTS if m)
    print(f"UNCALIBRATED · surface {len(SLOTS)} slots, weight {TOTAL}, mechanism-flippable {flip} ({flip / TOTAL:.1%}), always-pass {TOTAL - flip} ({(TOTAL - flip) / TOTAL:.1%})")
    print("\nWhole policies")
    pol = {
        "Perfect": set(),
        "Sheet flags and the parent's children only": set(MECHS),
        "Thorough on tickets, never opens GitHub": {"DONE", "BUILT"},
        "Thorough on tickets and GitHub, never opens Slack threads": {"CORR", "QA"},
        "Reads everything, takes each flag literally (no join)": {"DEP"},
        "Trusts Done tickets, otherwise thorough": {"DONE", "DEP", "QA"},
        "Stays inside the sheet's names and the parent": {"ALIAS", "FILT"},
        "Right calls, misses the freeze comment": {"FOLLOW"},
    }
    for k, v in pol.items():
        print(f"  {score(v):6.1%}  {k}  [lands: {', '.join(sorted(v)) or '-'}]")
    print("\nSingle misses")
    for m in MECHS:
        print(f"  {m:7} {score({m}):6.1%}")
    print("\nPairs at or above the 80 % bar:", [f"{a}+{b}" for a, b in itertools.combinations(MECHS, 2) if score({a, b}) >= .80] or "none")
    tot = sum(P.values())
    print(f"\nDesign landing rates {P}; sum {tot:.2f}, mean {tot / len(P):.2f}")
    pf = 1.0
    for m in MECHS:
        pf *= 1 - P[m]
    print(f"P(one run catches every trap) ~ {pf:.3f} under independence -> E[full passes of 6] ~ {6 * pf:.2f}")
    print("\nSix-run Monte Carlo (run latent rho, plus shared latents for code-read and thread-open behaviour)")
    print("  scale mean-rate rho   E[avg]  P(<80)  P(<85)  P(SD)  P(<5 full)  P(patterns)  P(all, 80 bar)  P(all, 85 cap)")
    for sc, rho in [(1.0, .30), (1.0, .50), (.8, .35), (.7, .35), (.6, .35), (.6, .5), (.5, .35), (.4, .35), (.3, .35)]:
        x = sim(sc, rho)
        print(f"  {sc:4.2f}  {tot / len(P) * sc:6.2f}   {rho:4.2f} {x['E']:6.1%}  {x['bar']:6.2f}  {x['cap']:6.2f}  {x['sd']:5.2f}  {x['full']:9.2f}  {x['pat']:10.2f}  {x['all']:13.2f}  {x['allcap']:13.2f}")


if __name__ == "__main__":
    main()
