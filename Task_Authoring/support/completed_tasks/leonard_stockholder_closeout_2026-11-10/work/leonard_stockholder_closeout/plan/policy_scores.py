#!/usr/bin/env python3
"""Whole-policy, single-miss and six-run scores on the real gradable surface (UNCALIBRATED).
Miss rates come from research census C5 (unpointed carriers, other personas, n = 6 per trap) and judgement. A landed trap fails each of its rows at Q,
because real misses are partial. Rows with no rule slip at SLIP (C5: added rows pass 88-96 %). Design aid only (learnings §9)."""
import itertools, json, os, random, statistics
from statistics import NormalDist
H = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(H)
SL = [(s["id"], s["weight"], s["mechanisms"]) for s in json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))["slots"]]
T = sum(w for _, w, _ in SL)
P = {"ADV": .50, "LETTER": .15, "TOLD": .15, "ASOF": .10, "FAM": .15, "BOARD": .10, "ASK": .10, "BOUNCE": .50, "EXT": .55, "ALIAS": .20}   # rev2b: Husnu Akin and the ES-8/ES-10 digest make ALIAS and ADV easier
# rev2: the platform pre-check (01a_Hardening_Report.md) caught LETTER, TOLD, ASOF, FAM, BOARD and ASK and missed ADV with the split un-stated;
# new rules at the cold census rates (research/rev2/census_a_bounce.md 0.50, census_b_carta.md 0.55-0.60, census_c_alias.md 0.30); ADV after un-pointing
# with the "go by the ledger" bridge (census_d_adv.md: solved 35-50 %)
M = list(P); SLIP, Q = .05, .80
def score(landed):
    return 1 - sum(w for s, w, m in SL if any(x in landed for x in m)) / T
def patterns(fs):
    fs = [f for f in fs if f]
    if not fs: return 0, 0.0
    par = list(range(len(fs)))
    def find(i):
        while par[i] != i: par[i] = par[par[i]]; i = par[i]
        return i
    for i, j in itertools.combinations(range(len(fs)), 2):
        if len(fs[i] ^ fs[j]) <= 1: par[find(i)] = find(j)
    g = {}
    for i in range(len(fs)): g.setdefault(find(i), []).append(i)
    return len(g), max(len(v) for v in g.values()) / len(fs)
def sim(scale=1.0, rho=.15, n=5000, seed=11):
    N = NormalDist(); r = random.Random(seed); A = []; c = dict(h=0, s=0, p=0, sd=0, pat=0, ap=0, ah=0)
    SDs = []
    for _ in range(n):
        runs, fsets = [], []
        for _ in range(6):
            z = r.gauss(0, 1); landed = set()
            for m in M:
                if N.cdf((rho ** .5) * z + ((1 - rho) ** .5) * r.gauss(0, 1)) < min(P[m] * scale, .97): landed.add(m)
            f = frozenset(s for s, w, m in SL if (r.random() < SLIP if not m else (any(x in landed for x in m) and r.random() < Q)))
            runs.append(1 - sum(w for s, w, m in SL if s in f) / T); fsets.append(f)
        a, sd = statistics.mean(runs), statistics.pstdev(runs); npat, big = patterns(fsets); full = sum(x >= .9999 for x in runs)
        ok = .10 <= sd <= .30 and full < 5 and npat >= 2 and big <= .5
        A.append(a); SDs.append(sd); c["h"] += a < .70; c["s"] += a <= .62; c["p"] += a < .85; c["sd"] += .10 <= sd <= .30; c["pat"] += npat >= 2 and big <= .5; c["ap"] += ok and a < .85; c["ah"] += ok and a < .70
    return statistics.mean(A), statistics.mean(SDs), {k: v / n for k, v in c.items()}
fl = sum(w for _, w, m in SL if m)
print(f"UNCALIBRATED · {len(SL)} slots, weight {T}, tagged to a rule {fl} ({fl / T:.1%}), weight-5 rows {sum(1 for _, w, _ in SL if w == 5)}")
for m in M:
    w = sum(x for _, x, mm in SL if m in mm); print(f"  {m:7} weight {w:3d} {w / T:5.1%}  design miss {P[m]:.2f}")
need = sum(sum(x for _, x, mm in SL if m in mm) / T * P[m] for m in M) * Q
print(f"expected miss weight (share x miss x Q) ~ {need:.3f}; the requester aims under 70 %")
print("\nWhole policies")
for k, v in {"Perfect": set(), "Owner list and the Carta search only": {"ADV", "LETTER", "TOLD", "ASOF", "FAM", "BOARD", "ASK", "BOUNCE", "EXT", "ALIAS"},
             "Thorough, trusts the founders' 'done' lines": {"LETTER"}, "Thorough, trusts the owner list's share column": {"ADV"},
             "Thorough, answers KPMG with today's holdings": {"ASOF"}, "Thorough except mail older than 2025": {"FAM"},
             "The pre-check's path (bulk pulls, letters by id, Carta-sender mail only, no alias lookup)": {"ADV", "BOUNCE", "EXT", "ALIAS"},
             "Thorough, reads letters by message id": {"BOUNCE"}, "Thorough, reads Carta's own notices only": {"EXT"}, "Thorough, never asks who Akin is": {"ALIAS"},
             "Thorough except DMs and recent mail": {"TOLD", "ASK"}, "Thorough, keeps the board list in the documents": {"BOARD"}}.items():
    print(f"  {score(v):6.1%}  {k}")
print("\nSingle misses (every row of the trap)\n  " + "  ".join(f"{m} {score({m}):.1%}" for m in M))
pf = 1.0
for m in M: pf *= 1 - P[m]
print(f"\nP(one run catches every trap) ~ {pf:.3f}; traps landing per run at design rates {sum(P.values()):.2f}")
print("\nSix-run Monte Carlo  (scale multiplies every miss rate)\n  scale  rho   E[avg]  mean SD  P(<70)  P(<=62)  P(<85)  P(SD)  P(patterns)  P(all, platform)  P(all, hard bar)")
for sc, rho in [(1.0, .15), (1.0, .35), (.85, .15), (.85, .35), (.7, .15), (.7, .35), (.5, .15)]:
    e, sd, c = sim(sc, rho)
    print(f"  {sc:4.2f}  {rho:4.2f}  {e:6.1%}  {sd:7.3f}  {c['h']:6.2f}  {c['s']:7.2f}  {c['p']:6.2f}  {c['sd']:5.2f}  {c['pat']:11.2f}  {c['ap']:16.2f}  {c['ah']:16.2f}")
