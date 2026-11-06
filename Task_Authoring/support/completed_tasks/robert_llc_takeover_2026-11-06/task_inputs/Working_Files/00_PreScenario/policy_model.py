#!/usr/bin/env python3
"""Pre-scenario policy model (UNCALIBRATED). Storyline A sketch surface (founders LLC take-over plan for Combo Fighter, Mar-May 2026).
Scores whole policies, single misses and a six-run Monte Carlo estimate of the gates at the requester cap
(corrected avg < 85 % requester cap, < 5 full passes, population SD 0.10-0.30, >= 2 failure patterns with the largest <= 50 %).
Design aid only: landing rates are design priors, not measured Opus 5.5 rates (learnings §9)."""
import itertools, json, random, statistics, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))
SURF = json.load(open(os.path.join(HERE, "sketch_surface.json")))["slots"]
SLOTS = [(s["id"], s["weight"], s["mechanisms"]) for s in SURF]
TOTAL = sum(w for _, w, _ in SLOTS)
MECHS = ["CORR", "AUTH", "FILT", "COMPLETE", "DONE", "DATE", "EXC"]
# P(mechanism LANDS = the run misses the deciding record). Placement-informed design priors (UNCALIBRATED), spread so
# runs fail different subsets. Measured anchors: six stored Opus 5.5 baselines on Robert's Feb 14 wind-down task
# (exposure_robert_runs.txt) read #winddown in full 6/6, its key threads 6/6, #executives 1/6 (roots from Feb 11 only),
# #prototype history 1/6 (one named thread 3-4/6), DMs 0/6, Snowflake 1/6 (table list only), GitHub 1/6, Calendar 1/6,
# and ran per-account Slack name searches in most runs. Measured catches there: an #executives root 1/6, a GitHub PR
# bot comment 0/6, a #prototype reply found by name search 4/6, a judgment clash 3/6, a swept-channel clash 6/6. Frederick runs: Calendar search 3/7, gcal_search_events returns
# descriptions; a correction named by its item and placed off the swept path was caught about 40-60 %.
P = {"CORR": 0.40, "AUTH": 0.30, "FILT": 0.55, "COMPLETE": 0.40, "DONE": 0.50, "DATE": 0.35, "EXC": 0.40}
CAP = 0.85  # requester target 2026-11-05: average strictly under 85 % (stricter than the Easy 90 % cap)
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
        "Linear project and #winddown only (issue notes and #winddown figures as final)": {"CORR", "AUTH", "FILT", "COMPLETE", "DONE", "DATE", "EXC"},
        "Every Slack channel, DM and issue, nothing else": {"AUTH", "DONE", "COMPLETE"},
        "Thorough except DMs": {"CORR"},
        "Thorough except the warehouse": {"AUTH"},
        "Thorough except store notices in the mailbox": {"DONE"},
        "Thorough except Feb #prototype / #executives history": {"FILT", "DATE"},
        "Right calls, never searches mail or calendar by tool name": {"COMPLETE"},
        "Takes issue comments about Calm Play at face value": {"EXC"},
        "Thorough, dates steps loosely": {"DATE"},
    }
    for k, v in pol.items():
        print(f"  {score(v):6.1%}  {k}  [lands: {', '.join(sorted(v)) or '-'}]")
    print("\nSingle misses (one mechanism lands, all else right)")
    for m in MECHS:
        print(f"  {m:6} {score({m}):6.1%}")
    pairs = sorted((score({a, b}), a, b) for a, b in itertools.combinations(MECHS, 2))
    print("\nHighest-scoring pair of misses:", f"{pairs[-1][1]}+{pairs[-1][2]} {pairs[-1][0]:.1%}")
    print("\nPairs that stay at or above the 85 % cap:", [f"{a}+{b}" for a, b in itertools.combinations(MECHS, 2) if score({a, b}) >= CAP] or "none")
    pf = 1.0
    for m in MECHS:
        pf *= 1 - P[m]
    print(f"\nP(one run catches every trap) ~ {pf:.3f} (independence) -> E[full passes of 6] ~ {6 * pf:.2f}")
    print(f"\nExpected traps landed per run at design rates: {sum(P.values()):.2f}; Robert wind-down baselines landed ~2.67 of 5 traps per run (scale ~1.0 there); Frederick bridge runs ~1 per run (scale ~ {1/sum(P.values()):.2f})")
    print("\nSix-run Monte Carlo (landing scale x rho)")
    print("  scale  rho   E[avg]  P(cap)  P(SD)  P(<5 full)  P(patterns)  P(all gates)")
    for scale, rho in [(1.0, 0.3), (1.0, 0.6), (0.8, 0.35), (0.7, 0.35), (0.6, 0.35), (0.6, 0.6), (0.5, 0.35), (0.4, 0.35), (0.35, 0.35), (0.3, 0.35)]:
        r = sim(scale, rho)
        print(f"  {scale:4.2f}  {rho:4.2f}  {r['E_avg']:6.1%}  {r['cap']:6.2f}  {r['sd']:5.2f}  {r['full']:10.2f}  {r['pat']:11.2f}  {r['all']:12.2f}")


if __name__ == "__main__":
    main()
