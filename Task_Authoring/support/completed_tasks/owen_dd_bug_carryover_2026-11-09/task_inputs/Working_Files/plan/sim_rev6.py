#!/usr/bin/env python3
"""Monte Carlo of six-run batches on the gradable-surface weights for candidate catch rates (design aid, UNCALIBRATED)."""
import random, statistics, sys, itertools
W = dict(V1=5, V5=3, V2=5, V3=5, V4=5, I1=5, I2=5, I3=3, I4=3, B1=5, B2=3, B3=5, B4=3, E2=5, A1=5, A3=3)
TOTAL = 151
def run(p, rng, skill):
    c = {k: rng.random() < min(1, max(0, v + skill)) for k, v in p.items()}   # skill: shared per-run diligence
    S = {}
    S["A1"] = S["A3"] = c["A"]; S["B1"] = S["B2"] = c["T"]; S["B3"] = S["B4"] = c["S"]; S["E2"] = c["M"]
    S["I2"] = S["I4"] = c["X"]; S["I1"] = S["I3"] = c["Z"]
    broken = 5 + c["S"] + c["T"] + (not c["A"]) + (not c["M"]); S["V1"] = broken == 7
    fixed = 58 + (not c["S"]) + (not c["T"]) - (not c["M"]); S["V5"] = fixed == 58
    S["V2"] = c["A"]; S["V3"] = (9 - (not c["S"]) - (not c["T"]) + (not c["M"])) == 9; S["V4"] = c["X"] and c["Z"]
    loss = sum(W[k] for k, ok in S.items() if not ok)
    return 1 - loss / TOTAL, S
def batch(p, rng, sd_skill):
    rs = [run(p, rng, rng.gauss(0, sd_skill)) for _ in range(6)]
    sc = [r[0] for r in rs]
    fail = [r for r in rs if r[0] < 1]
    groups = []
    for i, r in enumerate(fail):
        hit = [g for g in groups if any(sum(r[1][k] != fail[j][1][k] for k in W) <= 1 for j in g)]
        groups = [g for g in groups if g not in hit] + [[i] + [j for g in hit for j in g]]
    largest = max(len(g) for g in groups) / len(fail) if fail else 1
    return statistics.mean(sc), statistics.pstdev(sc), len(groups), largest, sum(1 for s in sc if s == 1)
def report(name, p, sd_skill=0.1, n=4000):
    rng = random.Random(7); R = [batch(p, rng, sd_skill) for _ in range(n)]
    ok = [r for r in R if r[0] < 0.80 and 0.1 <= r[1] <= 0.3 and r[2] >= 2 and r[3] <= 0.5 and r[4] < 5]
    print(f"{name:34s} avg {statistics.mean(r[0] for r in R):.3f} | SD med {statistics.median(r[1] for r in R):.3f} P(SD>=.1) {sum(r[1] >= .1 for r in R)/n:.2f} | P(patterns ok) {sum(r[2] >= 2 and r[3] <= .5 for r in R)/n:.2f} | P(avg<.80) {sum(r[0] < .8 for r in R)/n:.2f} | P(all gates) {len(ok)/n:.2f}")
report("rev5 now", dict(A=0, T=0, S=.75, M=.83, X=0, Z=0))
report("A,T,X at .5; Z 0", dict(A=.5, T=.5, S=.75, M=.83, X=.5, Z=0))
report("A,T,X,Z at .5", dict(A=.5, T=.5, S=.75, M=.83, X=.5, Z=.5))
report("A,T at .5; X,Z .4", dict(A=.5, T=.5, S=.75, M=.83, X=.4, Z=.4))
report("A .5 T .4 X .5 Z .3 S .6", dict(A=.5, T=.4, S=.6, M=.83, X=.5, Z=.3))
report("all .5 incl S,M", dict(A=.5, T=.5, S=.5, M=.5, X=.5, Z=.5))
report("A .7 T .5 X .5 Z .5", dict(A=.7, T=.5, S=.75, M=.83, X=.5, Z=.5))
report("A 1 T .5 X .5 Z .5", dict(A=1, T=.5, S=.75, M=.83, X=.5, Z=.5))
report("A .3 T .3 X .3 Z .3", dict(A=.3, T=.3, S=.75, M=.83, X=.3, Z=.3))
