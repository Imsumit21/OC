#!/usr/bin/env python3
"""Policy scores on the real gradable surface (UNCALIBRATED), against the requester cap of 80 %.
Whole policies, single misses, six-run gates, row-growth stress and pre-check odds. FILT splits into its two members here,
because a run can catch one and miss the other. Design aid only: rates are placement priors (learnings §9)."""
import itertools, json, os, random, statistics
from statistics import NormalDist
HERE = os.path.dirname(os.path.abspath(__file__))
SURF = json.load(open(os.path.join(HERE, "..", "01_Gradable_Surface.json")))["slots"]
AGG = {"S_total", "T_chk_live", "T_cards", "C_vol", "M_vol"}
ONLY1 = {"R_top", "K_r_top", "K_r_value", "K_r_q4"}     # the first pick moves with Copperleaf, not Redwood
def chans(s):
    out = set()
    for m in s["mechanisms"]:
        if m != "FILT":
            out.add(m)
        elif s["id"] in AGG:
            out |= {"FILT1", "FILT2"}
        elif s["id"] in ONLY1 or "PH" in s["id"] or "Copperleaf" in s["id"]:
            out.add("FILT1")
        else:
            out.add("FILT2")
    return out
SLOTS = [(s["id"], s["weight"], chans(s), s["class"]) for s in SURF]
TOTAL = sum(w for _, w, _, _ in SLOTS)
MECHS = ["DONE", "CORR", "ALIAS", "FILT1", "FILT2", "EXC", "INPUT", "DATE", "FOLLOW"]
P = {"DONE": .50, "CORR": .55, "ALIAS": .55, "FILT1": .35, "FILT2": .55, "EXC": .30, "INPUT": .45, "DATE": .40, "FOLLOW": .50}
LEDGER = {"DONE": .50, "CORR": .17, "INPUT": .17, "FILT1": .33, "FILT2": .33, "ALIAS": .20, "EXC": .20, "DATE": .67, "FOLLOW": .20}
CAP, SLIP = .80, .03
def score(l, slips=frozenset(), total=None): return 1 - sum(w for i, w, m, _ in SLOTS if m & l or i in slips) / (total or TOTAL)
def failed(l, slips=frozenset()): return frozenset(i for i, _, m, _ in SLOTS if m & l or i in slips)
def patterns(fs):
    fs = [f for f in fs if f]
    if not fs: return 0, 0.0
    p = list(range(len(fs)))
    def find(i):
        while p[i] != i: p[i] = p[p[i]]; i = p[i]
        return i
    for i, j in itertools.combinations(range(len(fs)), 2):
        if len(fs[i] ^ fs[j]) <= 1: p[find(i)] = find(j)
    g = {}
    for i in range(len(fs)): g.setdefault(find(i), []).append(i)
    return len(g), max(len(v) for v in g.values()) / len(fs)
def sim(scale=1., rho=.35, n=8000, seed=11, Pm=None, extra=0):
    N, r, PP, tot = NormalDist(), random.Random(seed), Pm or P, TOTAL + extra
    out = dict(avg=[], sd=[], cap=0, band=0, full=0, pat=0, all=0); mix = {i: 0 for i, _, _, _ in SLOTS}; allf = dict(mix)
    for _ in range(n):
        runs, fs = [], []
        for _ in range(6):
            z = r.gauss(0, 1); l = set()
            for m in MECHS:
                if N.cdf(rho ** .5 * z + (1 - rho) ** .5 * r.gauss(0, 1)) < min(PP[m] * scale, .97): l.add(m)
            sl = {i for i, _, c, _ in SLOTS if not c and r.random() < SLIP}
            runs.append(score(l, sl, tot)); fs.append(failed(l, sl))
        a, sd = statistics.mean(runs), statistics.pstdev(runs)
        full = sum(x >= .9999 for x in runs); npat, big = patterns(fs)
        g = [a < CAP, .10 <= sd <= .30, full < 5, npat >= 2 and big <= .5]
        out["avg"].append(a); out["sd"].append(sd)
        for k, ok in zip(("cap", "band", "full", "pat"), g): out[k] += ok
        out["all"] += all(g)
        for i, _, _, _ in SLOTS:
            c = sum(i in f for f in fs)
            mix[i] += 0 < c < 6; allf[i] += c == 6
    res = dict(E=statistics.mean(out["avg"]), SD=statistics.mean(out["sd"]), **{k: out[k] / n for k in ("cap", "band", "full", "pat", "all")})
    res["mixed"] = sum(w * mix[i] / n for i, w, _, _ in SLOTS) / tot
    res["allfail"] = sum(w * allf[i] / n for i, w, _, _ in SLOTS) / tot
    return res
def main():
    fl = sum(w for _, w, m, _ in SLOTS if m)
    print(f"UNCALIBRATED · surface: {len(SLOTS)} slots, total weight {TOTAL}, mechanism-flippable {fl} ({fl/TOTAL:.1%}) · cap {CAP:.0%}")
    print("\nWhole policies")
    for k, v in {"Perfect": set(), "Inbox, outreach sheet and term sheets only": set(MECHS),
                 "Term sheets at face value, otherwise thorough": {"CORR", "INPUT", "DONE"},
                 "Thorough except the population": {"FILT1", "FILT2"},
                 "Thorough except anything not under the trading name": {"ALIAS", "FILT1", "FILT2"},
                 "Thorough except calendar and card comments": {"CORR", "INPUT"},
                 "Thorough except Slack beyond name searches": {"DONE", "FOLLOW", "FILT1"},
                 "Value alone, misses the rights position": {"EXC"},
                 "Finishes at the model, the board and the reply": {"FOLLOW"},
                 "Rule doc's Oct 31 date kept": {"DATE"}}.items():
        print(f"  {score(v):6.1%}  {k}  [{', '.join(sorted(v)) or '-'}]")
    print("\nSingle misses")
    for m in MECHS:
        print(f"  {m:7} {score({m}):6.1%}  slots {sum(m in c for _,_,c,_ in SLOTS)}  weight share {sum(w for _,w,c,_ in SLOTS if m in c)/TOTAL:.1%}")
    print("\nPairs at or above the cap:", [f"{a}+{b}" for a, b in itertools.combinations(MECHS, 2) if score({a, b}) >= CAP] or "none")
    pf = 1.
    for m in MECHS: pf *= 1 - P[m]
    print(f"P(one run catches every trap) ~ {pf:.4f}; expected landings {sum(P.values()):.2f}")
    print("\nSix-run Monte Carlo")
    print("  view                                    E[avg]  E[SD]  mixed  allfail P(<80) P(SD) P(pat) P(all)")
    rows = [("design rates, rho .35", dict()), ("design rates, rho .2", dict(rho=.2)), ("design rates, rho .6", dict(rho=.6)), ("0.8x", dict(scale=.8)), ("0.7x", dict(scale=.7)), ("0.6x", dict(scale=.6)), ("0.5x", dict(scale=.5)),
            ("+40 always-pass weight", dict(extra=40)), ("+80 always-pass weight", dict(extra=80)), ("0.7x, +40", dict(scale=.7, extra=40)), ("0.7x, +80", dict(scale=.7, extra=80)),
            ("ledger priors", dict(Pm=LEDGER)), ("ledger priors, +40", dict(Pm=LEDGER, extra=40))]
    for k, kw in rows:
        r = sim(**kw)
        print(f"  {k:38} {r['E']:6.1%} {r['SD']:6.3f} {r['mixed']:6.1%} {r['allfail']:6.1%} {r['cap']:5.2f} {r['band']:5.2f} {r['pat']:5.2f} {r['all']:5.2f}")
    print("\nPre-check (one run, rho .35)")
    N = NormalDist(); central = {"EXC", "INPUT", "FILT1", "DONE"}
    for sc in (1., .7, .5):
        r = random.Random(5); n = 40000; ge2 = cen = none = 0
        for _ in range(n):
            z = r.gauss(0, 1); l = {m for m in MECHS if N.cdf(.35 ** .5 * z + .65 ** .5 * r.gauss(0, 1)) < min(P[m] * sc, .97)}
            ge2 += len(l) >= 2; cen += bool(l & central); none += not l
        print(f"  scale {sc}: P(none) {none/n:.3f}  P(two or more) {ge2/n:.2f}  P(first pick or banked figure wrong) {cen/n:.2f}")
if __name__ == "__main__":
    main()
