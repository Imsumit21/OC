#!/usr/bin/env python3
"""rev8 placement bootstrap: 8 measured Opus runs (7 stored + the rev7 pre-check). Blocks: D = Brian's Dec messages (DM history or a from:Brian window sweep),
K = the UI wrap deck, Q = sub-250 Brian replies, N = never reached (Gmail mail, Marcus DM, PR inline reviews: 0 of 8). Scores the six-run baseline gates
and a /hardness proxy for one pre-check run (independent causes missed; >= 2 needed for score 3+)."""
import random, statistics
RUNS = {"pre5": (0, 1, 0), "r1": (1, 0, 1), "r2": (0, 1, 1), "r3": (1, 0, 1), "r4": (1, 0, 0), "r5": (0, 1, 1), "r6": (0, 1, 1), "pre7": (1, 1, 1)}
W = dict(V1=5, V5=3, V2=5, V3=5, V4=5, I1=5, I2=5, I3=3, I4=3, B1=5, B2=3, B3=5, B4=3, E2=5, A1=5, A3=3)
def one(assign, rng, apply, nev):
    D, K, Q = RUNS[rng.choice(list(RUNS))]; blk = {"D": D, "K": K, "Q": Q, "N": 0, "DK": D or K}
    ok = {t: (blk[b] and rng.random() < apply) or rng.random() < nev for t, b in assign.items()}; ok["M"] = rng.random() < .9
    S = {"A1": ok["A"], "A3": ok["A"], "B1": ok["T"], "B2": ok["T"], "B3": ok["S"], "B4": ok["S"], "E2": ok["M"], "I2": ok["X"], "I4": ok["X"], "I1": ok["Z"], "I3": ok["Z"]}
    S["V1"] = 5 + ok["S"] + ok["T"] + (not ok["A"]) + (not ok["M"]) == 7; S["V5"] = 58 + (not ok["S"]) + (not ok["T"]) - (not ok["M"]) == 58
    S["V2"] = ok["A"]; S["V3"] = 9 - (not ok["S"]) - (not ok["T"]) + (not ok["M"]) == 9; S["V4"] = ok["X"] and ok["Z"]
    causes = len({assign[t] + (t if assign[t] == "N" else "") for t in "ATXZS" if not ok[t]} | ({"M"} if not ok["M"] else set()))
    if not ok["X"] and not ok["Z"] and assign["X"] == assign["Z"] == "N":
        causes -= 1   # both popups sit in Arthur's PR reviews: one cause
    return S, causes
def sim(assign, label, total=140, apply=.85, nev=.03, n=6000, seed=11):
    rng = random.Random(seed); res = []; hard = []
    for _ in range(n):
        Ss = [one(assign, rng, apply, nev) for _ in range(6)]
        sc = [1 - sum(W[k] for k, o in S.items() if not o) / total for S, _ in Ss]
        fail = [S for (S, _), s in zip(Ss, sc) if s < 1]; groups = []
        for i, S in enumerate(fail):
            hit = [g for g in groups if any(sum(S[k] != fail[j][k] for k in W) <= 1 for j in g)]
            groups = [g for g in groups if g not in hit] + [[i] + [j for g in hit for j in g]]
        lg = max((len(g) for g in groups), default=6) / max(len(fail), 1)
        res.append((statistics.mean(sc), statistics.pstdev(sc), len(groups) >= 2 and lg <= .5, sum(s == 1 for s in sc) < 5))
        _, c = one(assign, rng, apply, nev); hard.append(c >= 2)
    ph = sum(hard) / n; pa = sum(r[0] < .8 and .1 <= r[1] <= .3 and r[2] and r[3] for r in res) / n
    print(f"{label:44s} avg {statistics.mean(r[0] for r in res):.3f} P(avg<.80) {sum(r[0] < .8 for r in res)/n:.2f} | SD med {statistics.median(r[1] for r in res):.3f} P(SD ok) {sum(.1 <= r[1] <= .3 for r in res)/n:.2f} | P(patt) {sum(r[2] for r in res)/n:.2f} | P(base all) {pa:.2f} | P(hard>=3) {ph:.2f} | joint {pa*ph:.2f}")
for total in (140, 120):
    print(f"--- rubric total {total} (lean)")
    sim(dict(A="D", T="D", X="D", Z="D", S="Q"), "rev7 as uploaded (all four in Brian's DM)", total)
    sim(dict(A="N", T="N", X="N", Z="N", S="Q"), "rev5 + tooltip (no second carriers)", total)
    sim(dict(A="N", T="N", X="K", Z="K", S="Q"), "popups in deck; Tavern, Apple original only", total)
    sim(dict(A="N", T="D", X="K", Z="K", S="Q"), "popups deck; Tavern Brian DM; Apple orig", total)
    sim(dict(A="N", T="K", X="K", Z="K", S="Q"), "popups + Tavern in deck; Apple orig", total)
    sim(dict(A="N", T="N", X="D", Z="D", S="Q"), "popups in Brian's DM only", total)
    sim(dict(A="D", T="N", X="K", Z="K", S="Q"), "popups deck; Apple Brian DM; Tavern orig", total)
