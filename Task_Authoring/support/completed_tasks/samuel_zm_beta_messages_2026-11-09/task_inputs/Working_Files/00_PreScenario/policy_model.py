#!/usr/bin/env python3
"""Pre-scenario policy model (UNCALIBRATED). Storyline B sketch surface (Zombie Match 3D beta player messages).
Scores whole policies, single misses and a six-run Monte Carlo estimate of the Medium gates
(corrected avg < 85 %, < 5 full passes, population SD 0.10-0.30, >= 2 failure patterns with the largest <= 50 %).
Design aid only: landing rates are design priors, not measured Opus 5.5 rates (learnings §9)."""
import itertools, json, random, statistics, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
SURF = json.load(open(os.path.join(HERE, "sketch_surface.json")))["slots"]
SLOTS = [(s["id"], s["weight"], s["mechanisms"]) for s in SURF]
TOTAL = sum(w for _, w, _ in SLOTS)
MECHS = ["DONE", "CORR", "DATE", "EXC", "ALIAS", "FILT", "FOLLOW"]
# P(mechanism LANDS = the run misses the deciding record). Placement-informed design priors, deliberately spread so runs
# fail different subsets. Measured anchors (stored Opus 5.5 runs): inline PR comments opened in 1 of 6 Douglas runs and
# only 1-9 PRs in Julia runs; reply under an unrelated root caught ~20-30 %; older mail only by name search; a judgment
# on records every run reads rarely lands (Julia: 0 across 28+ runs), so DATE is set low.
P = {"DONE": 0.60, "CORR": 0.55, "DATE": 0.25, "EXC": 0.45, "ALIAS": 0.35, "FILT": 0.50, "FOLLOW": 0.50}
CAP = 0.85
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
        "Sheet flags taken at face value (no tickets, no reviews, no asks)": {"DONE", "CORR", "DATE", "EXC", "ALIAS", "FILT", "FOLLOW"},
        "Trusts Ready plus merged PR, otherwise thorough": {"DONE", "DATE"},
        "Reads everything, applies flags literally (no dependency, no older rule)": {"DATE", "EXC"},
        "Thorough except PR inline comments": {"DONE"},
        "Thorough except Slack thread replies": {"CORR"},
        "Thorough except anything outside the sheet's own names": {"ALIAS", "FILT"},
        "Thorough except mail older than the beta window": {"EXC"},
        "Right calls, misses the ticket-note rule": {"FOLLOW"},
    }
    for k, v in pol.items():
        print(f"  {score(v):6.1%}  {k}  [lands: {', '.join(sorted(v)) or '-'}]")
    print("\nSingle misses (one mechanism lands, all else right)")
    for m in MECHS:
        print(f"  {m:6} {score({m}):6.1%}")
    print("\nPairs that stay at or above the 85 % cap:", [f"{a}+{b}" for a, b in itertools.combinations(MECHS, 2) if score({a, b}) >= CAP] or "none")
    pf = 1.0
    for m in MECHS:
        pf *= 1 - P[m]
    print(f"\nP(one run catches every trap) ~ {pf:.3f} (independence) -> E[full passes of 6] ~ {6 * pf:.2f}")
    print(f"\nExpected traps landed per run at design rates: {sum(P.values()):.2f}; stored Opus runs miss about 1 per run, i.e. scale ~ {1/sum(P.values()):.2f}")
    print("\nSix-run Monte Carlo (landing scale x rho)")
    print("  scale  rho   E[avg]  P(cap)  P(SD)  P(<5 full)  P(patterns)  P(all gates)")
    for scale, rho in [(1.0, 0.3), (1.0, 0.6), (0.8, 0.35), (0.7, 0.35), (0.6, 0.35), (0.6, 0.6), (0.5, 0.35), (0.4, 0.35), (0.35, 0.35), (0.3, 0.35)]:
        r = sim(scale, rho)
        print(f"  {scale:4.2f}  {rho:4.2f}  {r['E_avg']:6.1%}  {r['cap']:6.2f}  {r['sd']:5.2f}  {r['full']:10.2f}  {r['pat']:11.2f}  {r['all']:12.2f}")


if __name__ == "__main__":
    main()
