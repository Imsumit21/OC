#!/usr/bin/env python3
"""Pre-scenario policy model (UNCALIBRATED). Storyline A sketch surface (vendor and partner commitments close-out).
Scores whole policies, single misses and a six-run Monte Carlo estimate of the Easy gates
(corrected avg < 90 %, < 5 full passes, population SD 0.10-0.30, >= 2 failure patterns with the largest <= 50 %).
Design aid only: landing rates are design priors, not measured Opus 5.5 rates (learnings §9)."""
import itertools, json, random, statistics, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
SURF = json.load(open(os.path.join(HERE, "sketch_surface.json")))["slots"]
SLOTS = [(s["id"], s["weight"], s["mechanisms"]) for s in SURF]
TOTAL = sum(w for _, w, _ in SLOTS)
MECHS = ["DONE", "CORR", "COMPL", "FILT", "EXC", "DATE"]
# P(mechanism LANDS = the run misses the deciding record). Placement-informed priors (memory: thread reply under an
# unrelated #executives post ~20-30 % caught; a record on the run's own search path ~100 % caught; Gmail bulk-read by
# ~6/15 runs). Deliberately spread so runs fail different subsets.
P = {"DONE": 0.40, "CORR": 0.60, "COMPL": 0.55, "FILT": 0.45, "EXC": 0.35, "DATE": 0.30}
CAP = 0.90
BASE_SLIP = 0.03


def score(landed, slips=frozenset()):
    lost = sum(w for sid, w, m in SLOTS if any(x in landed for x in m) or sid in slips)
    return 1 - lost / TOTAL


def failed(landed, slips=frozenset()):
    return frozenset(sid for sid, w, m in SLOTS if any(x in landed for x in m) or sid in slips)


def patterns(fsets):
    fs = [f for f in fsets if f]
    if not fs:
        return 0, 0.0
    parent = list(range(len(fs)))

    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for i, j in itertools.combinations(range(len(fs)), 2):
        if len(fs[i] ^ fs[j]) <= 1:  # single-linkage: differ on <= 1 rubric
            parent[find(i)] = find(j)
    groups = {}
    for i in range(len(fs)):
        groups.setdefault(find(i), []).append(i)
    return len(groups), max(len(g) for g in groups.values()) / len(fs)


def sim(scale=1.0, rho=0.35, n=20000, seed=11):
    from statistics import NormalDist
    N = NormalDist()
    rnd = random.Random(seed)
    res = {"avg": [], "cap": 0, "sd": 0, "full": 0, "pat": 0, "all": 0}
    for _ in range(n):
        runs, fsets = [], []
        for _ in range(6):
            z = rnd.gauss(0, 1)  # run-level thoroughness latent (Gaussian copula keeps marginals)
            landed = set()
            for m in MECHS:
                x = (rho ** 0.5) * z + ((1 - rho) ** 0.5) * rnd.gauss(0, 1)
                if N.cdf(x) < P[m] * scale:
                    landed.add(m)
            slips = {sid for sid, w, mm in SLOTS if not mm and rnd.random() < BASE_SLIP}
            runs.append(score(landed, slips))
            fsets.append(failed(landed, slips))
        a, sd = statistics.mean(runs), statistics.pstdev(runs)
        full = sum(1 for r in runs if r >= 0.9999)
        npat, largest = patterns(fsets)
        g = [a < CAP, 0.10 <= sd <= 0.30, full < 5, npat >= 2 and largest <= 0.5]
        res["avg"].append(a)
        for k, ok in zip(["cap", "sd", "full", "pat"], g):
            res[k] += ok
        res["all"] += all(g)
    return {"E_avg": statistics.mean(res["avg"]), **{k: res[k] / n for k in ["cap", "sd", "full", "pat", "all"]}}


def main():
    print(f"UNCALIBRATED · surface: {len(SLOTS)} slots, total weight {TOTAL}, "
          f"mechanism-flippable {sum(w for _, w, m in SLOTS if m)} ({sum(w for _, w, m in SLOTS if m) / TOTAL:.1%})")
    print("\nWhole policies")
    pol = {
        "Perfect": set(),
        "Inbox-and-doc only (no Slack threads, no calendar)": {"CORR", "COMPL", "FILT", "EXC"},
        "Trusts 'done' sources (registration, unanswered follow-up, free trial)": {"DONE", "COMPL", "DATE"},
        "Reads everything, applies the cash test literally (no exemption, no trial terms)": {"EXC", "DATE"},
        "Thorough except Slack thread replies": {"CORR"},
        "Thorough except calendar": {"COMPL", "FILT"},
    }
    for k, v in pol.items():
        print(f"  {score(v):6.1%}  {k}  [lands: {', '.join(sorted(v)) or '-'}]")
    print("\nSingle misses (one mechanism lands, all else right)")
    for m in MECHS:
        print(f"  {m:6} {score({m}):6.1%}")
    print("\nPairs that stay above the 90 % cap:", [f"{a}+{b}" for a, b in itertools.combinations(MECHS, 2) if score({a, b}) >= CAP] or "none")
    pf = 1.0
    for m in MECHS:
        pf *= 1 - P[m]
    print(f"\nP(one run catches every trap) ~ {pf:.3f} (independence) -> E[full passes of 6] ~ {6 * pf:.2f}")
    print("\nSix-run Monte Carlo (landing scale x rho)")
    print("  scale  rho   E[avg]  P(cap)  P(SD)  P(<5 full)  P(patterns)  P(all gates)")
    for scale, rho in [(1.0, 0.3), (1.0, 0.6), (0.8, 0.35), (0.7, 0.35), (0.6, 0.35), (0.6, 0.6), (0.5, 0.35)]:
        r = sim(scale, rho)
        print(f"  {scale:4.2f}  {rho:4.2f}  {r['E_avg']:6.1%}  {r['cap']:6.2f}  {r['sd']:5.2f}  {r['full']:10.2f}  {r['pat']:11.2f}  {r['all']:12.2f}")


if __name__ == "__main__":
    main()
