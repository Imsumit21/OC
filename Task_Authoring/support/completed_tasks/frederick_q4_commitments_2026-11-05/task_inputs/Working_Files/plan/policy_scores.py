#!/usr/bin/env python3
"""UNCALIBRATED policy / Monte Carlo scores on the real 01_Gradable_Surface.json (design aid, never a gate).
Gates scored: requester avg < 80 %, Easy cap < 90 %, population SD 0.10-0.30, < 5 full passes, >= 2 patterns (largest <= 50 %)."""
import itertools, json, os, random, statistics
from statistics import NormalDist
HERE = os.path.dirname(os.path.abspath(__file__))
S = json.load(open(os.path.join(os.path.dirname(HERE), "01_Gradable_Surface.json")))["slots"]
SL = [(s["id"], s["weight"], s.get("mechanisms") or []) for s in S]
T = sum(w for _, w, _ in SL)
# rev4 landing rates (UNCALIBRATED): rev3 pre-check (run_forensics/rev3/precheck) caught EXC/DATE/FILT/SIGN/AMEND by name or on the
# delegation path and missed DONE; the de-named CORR/COMPL/NOTE moves and the WIN filter move use the bridge analogs (reply under an
# unrelated root caught 20-30%; DM thread 1/6-6/15; Nintendo-style out-of-filter member missed by rev3)
P = {"DONE": 0.60, "CORR": 0.70, "COMPL": 0.65, "EXC": 0.05, "DATE": 0.10, "FILT": 0.10, "SIGN": 0.05, "AMEND": 0.05, "NOTE": 0.60, "WIN": 0.55}
M = list(P); SLIP = 0.03
def score(l, sl=()): return 1 - sum(w for i, w, m in SL if set(m) & l or i in sl) / T
def failed(l, sl=()): return frozenset(i for i, w, m in SL if set(m) & l or i in sl)
def pats(fs):
    fs = [f for f in fs if f]
    if not fs: return 0, 0
    par = list(range(len(fs)))
    def f(i):
        while par[i] != i: par[i] = par[par[i]]; i = par[i]
        return i
    for a, b in itertools.combinations(range(len(fs)), 2):
        if len(fs[a] ^ fs[b]) <= 1: par[f(a)] = f(b)
    g = {}
    for i in range(len(fs)): g.setdefault(f(i), []).append(i)
    return len(g), max(map(len, g.values())) / len(fs)
def sim(scale=1.0, rho=0.35, n=12000, seed=5):
    N = NormalDist(); r = random.Random(seed); acc = dict(avg=[], u80=0, cap=0, sd=0, full=0, pat=0, all80=0, sds=[])
    for _ in range(n):
        runs, fs = [], []
        for _ in range(6):
            z = r.gauss(0, 1); l = set()
            for m in M:
                if N.cdf(rho ** .5 * z + (1 - rho) ** .5 * r.gauss(0, 1)) < P[m] * scale: l.add(m)
            sl = {i for i, w, mm in SL if not mm and r.random() < SLIP}
            runs.append(score(l, sl)); fs.append(failed(l, sl))
        a, sd = statistics.mean(runs), statistics.pstdev(runs); full = sum(x > .9999 for x in runs); np_, lg = pats(fs)
        g = dict(u80=a < .80, cap=a < .90, sd=.10 <= sd <= .30, full=full < 5, pat=np_ >= 2 and lg <= .5)
        acc["avg"].append(a); acc["sds"].append(sd)
        for k, v in g.items(): acc[k] += v
        acc["all80"] += all(g.values())
    return {k: (statistics.mean(v) if isinstance(v, list) else v / n) for k, v in acc.items()}
print(f"UNCALIBRATED · {len(SL)} slots · weight {T} · flippable {sum(w for _, w, m in SL if m)}")
print("Whole policies:")
for name, l in [("perfect", set()), ("reads mail, papers, hub-path rules; no Slack search, no Linear, no checklist join", {"CORR", "COMPL", "DONE", "EXC"}),
                ("trusts each company's own thread and paper", {"CORR", "COMPL", "DATE", "DONE"}),
                ("thorough but September-window searches only", {"FILT"}), ("thorough except DMs", {"COMPL"}),
                ("thorough except Linear comments", {"DONE"}), ("literal cash test (no exemption join)", {"EXC"}),
                ("rev3 pre-check behaviour (name searches, Aug 15+ inbox, folder papers, no Linear)", {"DONE", "CORR", "COMPL", "NOTE", "WIN"}),
                ("rev3 behaviour plus DM threads and contact-name searches", {"DONE", "NOTE", "WIN"})]:
    print(f"  {score(l):6.1%}  {name}")
print("Single misses:", ", ".join(f"{m} {score({m}):.1%}" for m in M))
_pairs = [f"{a}+{b}" for a, b in itertools.combinations([m for m in M if P[m] >= .5], 2) if score({a, b}) >= .80]
print("Pairs at or above 80 %:", ", ".join(_pairs) if _pairs else "none")
print("scale rho  E[avg]  P(<80%) P(<90%) P(SD) E[SD]  P(<5 full) P(patterns) P(all, <80%)")
for sc, rho in [(1.0, .35), (1.0, .6), (.8, .35), (.6, .35), (.5, .35), (.4, .35), (1.4, .35)]:
    x = sim(sc, rho)
    print(f" {sc:4.2f} {rho:4.2f}  {x['avg']:6.1%}  {x['u80']:6.2f}  {x['cap']:6.2f} {x['sd']:5.2f} {x['sds']:5.3f}  {x['full']:9.2f}  {x['pat']:10.2f}  {x['all80']:10.2f}")
