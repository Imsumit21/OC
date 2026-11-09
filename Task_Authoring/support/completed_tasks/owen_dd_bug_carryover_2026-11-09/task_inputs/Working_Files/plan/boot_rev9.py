#!/usr/bin/env python3
"""rev9 placement model. Fixes boot_rev8's flaw: every Brian-authored carrier (DM lines, the Dec 1 shop reply, the Dec 8 music line) is caught together by one
behaviour, a from:Brian sweep or a read of Brian's DM past early December (D). 9 measured runs (7 stored + the rev7 and rev8 pre-checks, both D=1).
N = a record no run has opened (Vincent's email, Marcus's DM, Arthur's inline reviews: 0 of 9). L = Linear comment on the child (read by every run)."""
import random, statistics, itertools
RUNS = {"pre5": (0, 0), "r1": (1, 1), "r2": (0, 1), "r3": (1, 1), "r4": (1, 0), "r5": (0, 1), "r6": (0, 1), "pre7": (1, 1), "pre8": (1, 1)}   # (D, Q)
W = dict(A1=5, A3=3, V2=5, B1=5, B2=3, B3=5, B4=3, E2=5, I1=5, I2=5, I3=3, I4=3, H1=5, H2=5, V1=5, V3=5, V4=5, V5=3, R1=5)
SHARE = dict(A=.14, T=.10, P=.12, H=.07, S=.06, M=.05)   # /hardness's own weighted shares, knock-ons included (rev7/rev8 reports)
def one(d, rng, apply=.9):
    D, Q = RUNS[rng.choice(list(RUNS))]
    def got(where):
        return {"N": rng.random() < .03, "D": D and rng.random() < apply, "L": rng.random() < .97}[where]
    ok = {t: got(w) for t, w in d.items()}
    ok["S"] = (D or Q) and rng.random() < apply
    ok["M"] = (D and rng.random() < apply) or rng.random() < .5
    S = {"A1": ok["A"], "A3": ok["A"], "V2": ok["A"], "B1": ok["T"], "B2": ok["T"], "B3": ok["S"], "B4": ok["S"], "E2": ok["M"],
         "I1": ok["P"], "I2": ok["P"], "I3": ok["P"], "I4": ok["P"], "H1": ok["H"], "H2": ok["H"]}
    S["V1"] = ok["S"] and ok["T"] and ok["A"] and ok["M"]; S["V3"] = (ok["S"] + ok["T"] - (not ok["M"])) == 2 or (ok["S"] and ok["T"] and ok["M"])
    S["V4"] = ok["P"] and ok["H"]; S["V5"] = ok["S"] and ok["T"] and ok["M"]; S["R1"] = ok["A"]
    miss = [t for t in "ATPHSM" if not ok[t]]
    return S, len(miss) >= 2 or sum(SHARE[t] for t in miss) >= .15
def sim(d, label, total=130, n=5000, seed=7):
    rng = random.Random(seed); res = []; hard = []
    for _ in range(n):
        Ss = [one(d, rng) for _ in range(6)]
        sc = [1 - sum(W[k] for k, o in S.items() if not o) / total for S, _ in Ss]
        fail = [S for (S, _), s in zip(Ss, sc) if s < 1]; groups = []
        for i, S in enumerate(fail):
            hit = [g for g in groups if any(sum(S[k] != fail[j][k] for k in W) <= 1 for j in g)]
            groups = [g for g in groups if g not in hit] + [[i] + [j for g in hit for j in g]]
        lg = max((len(g) for g in groups), default=6) / max(len(fail), 1)
        res.append((statistics.mean(sc), statistics.pstdev(sc), len(groups) >= 2 and lg <= .5, sum(s == 1 for s in sc) < 5))
        hard.append(one(d, rng)[1])
    ph = sum(hard) / n; pa = sum(r[0] < .8 and .1 <= r[1] <= .3 and r[2] and r[3] for r in res) / n
    print(f"{label:52s} avg {statistics.mean(r[0] for r in res):.3f} | SD med {statistics.median(r[1] for r in res):.3f} P(SD) {sum(.1 <= r[1] <= .3 for r in res)/n:.2f} | P(patt) {sum(r[2] for r in res)/n:.2f} | P(base) {pa:.2f} | P(hard>=3) {ph:.2f} | joint {pa*ph:.2f}")
if __name__ == "__main__":
    for total in (130, 115):
        print(f"--- lean rubric total {total}")
        sim(dict(A="D", T="D", P="D", H="L"), "rev7: Apple, Tavern, popups in Brian's DM", total)
        sim(dict(A="N", T="D", P="D", H="L"), "rev8: Tavern, popups in Brian's DM", total)
        sim(dict(A="N", T="N", P="N", H="L"), "rev5: no second copies", total)
        sim(dict(A="N", T="N", P="D", H="L"), "rev9a: drop Tavern line (popups stay)", total)
        sim(dict(A="N", T="D", P="N", H="L"), "rev9b: drop popups line (Tavern stays)", total)
        sim(dict(A="N", T="N", P="D", H="D"), "rev9c: drop Tavern line; hold notes -> Brian's DM", total)
        sim(dict(A="N", T="D", P="N", H="D"), "rev9d: drop popups line; hold notes -> Brian's DM", total)
