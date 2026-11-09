#!/usr/bin/env python3
"""Bootstrap six-run batches from the 7 stored runs' measured exposure (D = Brian's DM past early Dec, K = the deck, Q = sub-250 Brian replies)."""
import random, statistics
RUNS = {"pre": (0, 1, 0), "r1": (1, 0, 1), "r2": (0, 1, 1), "r3": (1, 0, 1), "r4": (1, 0, 0), "r5": (0, 1, 1), "r6": (0, 1, 1)}
W = dict(V1=5, V5=3, V2=5, V3=5, V4=5, I1=5, I2=5, I3=3, I4=3, B1=5, B2=3, B3=5, B4=3, E2=5, A1=5, A3=3)
def run(v, rng, apply):
    D, K, Q = v
    ok = dict(A=D and rng.random() < apply, T=D and rng.random() < apply, X=K and rng.random() < apply, Z=K and rng.random() < apply,
              S=Q and rng.random() < apply, M=rng.random() < .9)
    S = {"A1": ok["A"], "A3": ok["A"], "B1": ok["T"], "B2": ok["T"], "B3": ok["S"], "B4": ok["S"], "E2": ok["M"], "I2": ok["X"], "I4": ok["X"], "I1": ok["Z"], "I3": ok["Z"]}
    S["V1"] = 5 + ok["S"] + ok["T"] + (not ok["A"]) + (not ok["M"]) == 7; S["V5"] = 58 + (not ok["S"]) + (not ok["T"]) - (not ok["M"]) == 58
    S["V2"] = ok["A"]; S["V3"] = 9 - (not ok["S"]) - (not ok["T"]) + (not ok["M"]) == 9; S["V4"] = ok["X"] and ok["Z"]
    return S
def gates(total, apply, n=6000, seed=11):
    rng = random.Random(seed); keys = list(RUNS); res = []
    for _ in range(n):
        Ss = [run(RUNS[rng.choice(keys)], rng, apply) for _ in range(6)]
        sc = [1 - sum(W[k] for k, o in S.items() if not o) / total for S in Ss]
        fail = [S for S, s in zip(Ss, sc) if s < 1]; groups = []
        for i, S in enumerate(fail):
            hit = [g for g in groups if any(sum(S[k] != fail[j][k] for k in W) <= 1 for j in g)]
            groups = [g for g in groups if g not in hit] + [[i] + [j for g in hit for j in g]]
        lg = max((len(g) for g in groups), default=6) / max(len(fail), 1)
        res.append((statistics.mean(sc), statistics.pstdev(sc), len(groups) >= 2 and lg <= .5, sum(s == 1 for s in sc) < 5))
    print(f"total {total} apply {apply}: avg {statistics.mean(r[0] for r in res):.3f} P(<.80) {sum(r[0] < .8 for r in res)/n:.2f} | SD med {statistics.median(r[1] for r in res):.3f} P(SD>=.1) {sum(.1 <= r[1] <= .3 for r in res)/n:.2f} | P(patterns) {sum(r[2] for r in res)/n:.2f} | P(all) {sum(r[0] < .8 and .1 <= r[1] <= .3 and r[2] and r[3] for r in res)/n:.2f}")
for total in (151, 130, 120):
    for apply in (.75, .9):
        gates(total, apply)
print("--- alternatives (which block carries which correction)")
def gates2(assign, total, apply=.85, n=6000, seed=11, label=""):
    rng = random.Random(seed); keys = list(RUNS); res = []
    for _ in range(n):
        Ss = []
        for _ in range(6):
            D, K, Q = RUNS[rng.choice(keys)]; blk = {"D": D, "K": K, "Q": Q, "DK": D or K}
            ok = {t: blk[b] and rng.random() < apply for t, b in assign.items()}; ok["M"] = rng.random() < .9
            S = {"A1": ok["A"], "A3": ok["A"], "B1": ok["T"], "B2": ok["T"], "B3": ok["S"], "B4": ok["S"], "E2": ok["M"], "I2": ok["X"], "I4": ok["X"], "I1": ok["Z"], "I3": ok["Z"]}
            S["V1"] = 5 + ok["S"] + ok["T"] + (not ok["A"]) + (not ok["M"]) == 7; S["V5"] = 58 + (not ok["S"]) + (not ok["T"]) - (not ok["M"]) == 58
            S["V2"] = ok["A"]; S["V3"] = 9 - (not ok["S"]) - (not ok["T"]) + (not ok["M"]) == 9; S["V4"] = ok["X"] and ok["Z"]; Ss.append(S)
        sc = [1 - sum(W[k] for k, o in S.items() if not o) / total for S in Ss]
        fail = [S for S, s in zip(Ss, sc) if s < 1]; groups = []
        for i, S in enumerate(fail):
            hit = [g for g in groups if any(sum(S[k] != fail[j][k] for k in W) <= 1 for j in g)]
            groups = [g for g in groups if g not in hit] + [[i] + [j for g in hit for j in g]]
        lg = max((len(g) for g in groups), default=6) / max(len(fail), 1)
        res.append((statistics.mean(sc), statistics.pstdev(sc), len(groups) >= 2 and lg <= .5, sum(s == 1 for s in sc) < 5))
    print(f"{label:30s} total {total}: avg {statistics.mean(r[0] for r in res):.3f} | SD med {statistics.median(r[1] for r in res):.3f} P(SD ok) {sum(.1 <= r[1] <= .3 for r in res)/n:.2f} | P(patterns) {sum(r[2] for r in res)/n:.2f} | P(all) {sum(r[0] < .8 and .1 <= r[1] <= .3 and r[2] and r[3] for r in res)/n:.2f}")
for total in (151, 130):
    gates2(dict(A="D", T="D", X="K", Z="K", S="Q"), total, label="rev6 as built")
    gates2(dict(A="D", T="D", X="D", Z="D", S="Q"), total, label="all four in Brian's DM")
    gates2(dict(A="D", T="D", X="D", Z="K", S="Q"), total, label="A,T,X in DM; Z deck")
    gates2(dict(A="D", T="D", X="DK", Z="DK", S="Q"), total, label="X,Z in both DM and deck")
