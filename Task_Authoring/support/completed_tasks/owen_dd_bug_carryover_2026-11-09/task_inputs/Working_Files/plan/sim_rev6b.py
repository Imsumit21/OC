#!/usr/bin/env python3
"""Container-level simulation: a run sees a container with its measured rate; a seen correction is applied with prob a."""
import random, statistics
def sim(cfg, total, n=5000, apply=0.85, seed=3):
    rng = random.Random(seed); out = []
    for _ in range(n):
        runs = []
        for _ in range(6):
            seen = {c: rng.random() < p for c, p in cfg["containers"].items()}
            ok = {t: (seen[c] and rng.random() < apply) if c else (rng.random() < pr) for t, (c, pr) in cfg["traps"].items()}
            S = {}
            for t, rows in cfg["rows"].items(): 
                for r, w in rows: S[r] = (S.get(r, (True, w))[0] and ok[t], w)
            S["V3"] = ((9 - (not ok["S"]) - (not ok["T"]) + (not ok["M"])) == 9, 5)
            S["V4"] = (ok["X"] and ok["Z"], 5); S["V2"] = (ok["A"], 5)
            S["V1"] = ((5 + ok["S"] + ok["T"] + (not ok["A"]) + (not ok["M"])) == 7, 5)
            S["V5"] = ((58 + (not ok["S"]) + (not ok["T"]) - (not ok["M"])) == 58, 3)
            loss = sum(w for r, (o, w) in S.items() if not o); runs.append((1 - loss / total, {r: o for r, (o, w) in S.items()}))
        sc = [r[0] for r in runs]; fail = [r for r in runs if r[0] < 1]
        groups = []
        for i, r in enumerate(fail):
            hit = [g for g in groups if any(sum(r[1][k] != fail[j][1][k] for k in r[1]) <= 1 for j in g)]
            groups = [g for g in groups if g not in hit] + [[i] + [j for g in hit for j in g]]
        lg = max((len(g) for g in groups), default=6) / max(len(fail), 1)
        out.append((statistics.mean(sc), statistics.pstdev(sc), len(groups) >= 2 and lg <= .5, sum(s == 1 for s in sc) < 5))
    allok = sum(a < .8 and .1 <= s <= .3 and p and f for a, s, p, f in out) / n
    print(f"{cfg['name']:52s} total {total:3d} | avg {statistics.mean(o[0] for o in out):.3f} P(<.80) {sum(o[0] < .8 for o in out)/n:.2f} | SD med {statistics.median(o[1] for o in out):.3f} P(>=.1) {sum(o[1] >= .1 for o in out)/n:.2f} | P(pattern) {sum(o[2] for o in out)/n:.2f} | P(all) {allok:.2f}")
ROWS = {"A": [("A1", 5), ("A3", 3)], "T": [("B1", 5), ("B2", 3)], "S": [("B3", 5), ("B4", 3)], "M": [("E2", 5)], "X": [("I2", 5), ("I4", 3)], "Z": [("I1", 5), ("I3", 3)]}
base = dict(name="", containers=dict(D=.43, K=.57, Q=.71), rows=ROWS)
for total in (151, 120):
    sim(dict(base, name="rev5 as is", traps=dict(A=(None, 0), T=(None, 0), S=("Q", 1), M=(None, .9), X=(None, 0), Z=(None, 0))), total)
    sim(dict(base, name="T->Brian DM, X->deck; A,Z stay hidden", traps=dict(A=(None, 0), T=("D", 1), S=("Q", 1), M=(None, .9), X=("K", 1), Z=(None, 0))), total)
    sim(dict(base, name="T->DM, X+Z->deck (one heavy trap); A hidden", traps=dict(A=(None, 0), T=("D", 1), S=("Q", 1), M=(None, .9), X=("K", 1), Z=("K", 1))), total)
    sim(dict(base, name="T->DM, X->deck, Z->sub-250 thread; A hidden", traps=dict(A=(None, 0), T=("D", 1), S=("Q", 1), M=(None, .9), X=("K", 1), Z=("Q", 1))), total)
print("--- heavier blocks")
for total in (151, 130, 120):
    sim(dict(base, name="A+T->Brian DM, X+Z->deck, S sub-250", traps=dict(A=("D", 1), T=("D", 1), S=("Q", 1), M=(None, .9), X=("K", 1), Z=("K", 1))), total)
    sim(dict(base, name="A+T->DM(.5), X+Z->deck(.5), S(.6)", containers=dict(D=.5, K=.5, Q=.6), traps=dict(A=("D", 1), T=("D", 1), S=("Q", 1), M=(None, .9), X=("K", 1), Z=("K", 1))), total)
    sim(dict(base, name="A->sub-250, T->DM, X+Z->deck", traps=dict(A=("Q", 1), T=("D", 1), S=("Q", 1), M=(None, .9), X=("K", 1), Z=("K", 1))), total)
