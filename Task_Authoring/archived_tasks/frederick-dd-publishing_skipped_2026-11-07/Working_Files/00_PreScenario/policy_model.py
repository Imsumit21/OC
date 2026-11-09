#!/usr/bin/env python3
"""Pre-scenario policy model (UNCALIBRATED). Storyline A sketch surface (Domino Delights publishing-rights model).
Scores whole policies, single misses and a six-run Monte Carlo estimate of the Medium gates
(corrected avg < 85 %, < 5 full passes, population SD 0.10-0.30, >= 2 failure patterns with the largest <= 50 %).
Design aid only: landing rates are placement priors, not measured Opus 5.5 rates for this task (learnings §9).
Structure adapted from Samuel's model (format and code only; no fact carried over)."""
import itertools, json, random, statistics, os
from statistics import NormalDist
HERE = os.path.dirname(os.path.abspath(__file__))
SURF = json.load(open(os.path.join(HERE, "sketch_surface.json")))["slots"]
SLOTS = [(s["id"], s["weight"], s["mechanisms"]) for s in SURF]
TOTAL = sum(w for _, w, _ in SLOTS)
MECHS = ["DONE", "CORR", "ALIAS", "FILT1", "FILT2", "EXC", "INPUT", "FOLLOW"]
# P(mechanism LANDS = the run misses the deciding record). Anchors from stored Opus 5.5 runs (memory and exposure output):
#  CORR   calendar note found by a name search 3 of 7 -> 0.55
#  FILT2  Linear-only fact, 0 of 6 caught on the Frederick Q4 task; one pointer added so it is not near-certain -> 0.60
#  FILT1  a reply under an unrelated #executives post, caught 20-30 %, but reachable by a generic search too -> 0.45
#  DONE   done_gap ledger prior 0.50 (n_eff 4) -> 0.50
#  ALIAS  no prior; contact search 1-9 calls per run, deep Slack name sweep 1 of 6 baselines -> 0.50
#  INPUT  card comment; trello_get_comments ran 6/6 only where the prompt named the card -> 0.45
#  FOLLOW reply under a root about another topic, caught 20-30 %; set lower because it is a rule, not an item -> 0.50
#  EXC    judgment after retrieval, which rarely lands -> 0.30
P = {"DONE": 0.50, "CORR": 0.55, "ALIAS": 0.50, "FILT1": 0.45, "FILT2": 0.60, "EXC": 0.30, "INPUT": 0.45, "FOLLOW": 0.50}
CAP, BASE_SLIP = 0.80, 0.03   # requester cap: under 80 % (the assigned Medium cap is 85 %)

def score(landed, slips=frozenset()):
    return 1 - sum(w for sid, w, m in SLOTS if any(x in landed for x in m) or sid in slips) / TOTAL
def failed(landed, slips=frozenset()):
    return frozenset(sid for sid, w, m in SLOTS if any(x in landed for x in m) or sid in slips)
def patterns(fsets):
    fs = [f for f in fsets if f]
    if not fs:
        return 0, 0.0
    parent = list(range(len(fs)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]; i = parent[i]
        return i
    for i, j in itertools.combinations(range(len(fs)), 2):
        if len(fs[i] ^ fs[j]) <= 1:   # single-linkage: differ on <= 1 rubric
            parent[find(i)] = find(j)
    g = {}
    for i in range(len(fs)):
        g.setdefault(find(i), []).append(i)
    return len(g), max(len(v) for v in g.values()) / len(fs)

def sim(scale=1.0, rho=0.35, n=12000, seed=11, P_=None, fixed=None):
    N, rnd, PP = NormalDist(), random.Random(seed), (P_ or P)
    res = {"avg": [], "cap": 0, "sd": 0, "full": 0, "pat": 0, "all": 0, "sdv": []}
    for _ in range(n):
        runs, fsets = [], []
        for _ in range(6):
            z = rnd.gauss(0, 1)   # run-level thoroughness latent (Gaussian copula keeps marginals)
            landed = set()
            for m in MECHS:
                x = (rho ** 0.5) * z + ((1 - rho) ** 0.5) * rnd.gauss(0, 1)
                if N.cdf(x) < min(PP[m] * scale, 0.97):
                    landed.add(m)
            slips = {sid for sid, w, mm in SLOTS if not mm and rnd.random() < BASE_SLIP}
            runs.append(score(landed, slips)); fsets.append(failed(landed, slips))
        a, sd = statistics.mean(runs), statistics.pstdev(runs)
        full = sum(1 for r in runs if r >= 0.9999)
        npat, largest = patterns(fsets)
        g = [a < CAP, 0.10 <= sd <= 0.30, full < 5, npat >= 2 and largest <= 0.5]
        res["avg"].append(a); res["sdv"].append(sd)
        for k, ok in zip(["cap", "sd", "full", "pat"], g):
            res[k] += ok
        res["all"] += all(g)
    return {"E_avg": statistics.mean(res["avg"]), "E_sd": statistics.mean(res["sdv"]), **{k: res[k] / n for k in ["cap", "sd", "full", "pat", "all"]}}

def main():
    fl = sum(w for _, w, m in SLOTS if m)
    print(f"UNCALIBRATED · surface: {len(SLOTS)} slots, total weight {TOTAL}, mechanism-flippable {fl} ({fl/TOTAL:.1%})")
    print("\nWhole policies")
    pol = {
        "Perfect": set(),
        "Inbox and outreach tab only, nothing else opened": set(MECHS),
        "Term mails at face value, otherwise thorough": {"DONE", "CORR", "INPUT"},
        "Thorough on deals, finishes at the model and the reply": {"FOLLOW"},
        "Thorough except the population (tab plus own inbox)": {"FILT1", "FILT2"},
        "Thorough except anything not under the trading name": {"ALIAS", "FILT1", "FILT2"},
        "Picks on value alone, misses the rights position": {"EXC"},
        "Thorough except calendar and card comments": {"CORR", "INPUT"},
        "Thorough except Slack beyond name searches": {"DONE", "FOLLOW"},
    }
    for k, v in pol.items():
        print(f"  {score(v):6.1%}  {k}  [lands: {', '.join(sorted(v)) or '-'}]")
    print("\nSingle misses (one mechanism lands, all else right)")
    for m in MECHS:
        print(f"  {m:7} {score({m}):6.1%}   slots {sum(1 for _,_,x in SLOTS if m in x)}  weight share {sum(w for _,w,x in SLOTS if m in x)/TOTAL:.1%}")
    print("\nPairs that stay at or above the 80 % cap:", [f"{a}+{b}" for a, b in itertools.combinations(MECHS, 2) if score({a, b}) >= CAP] or "none")
    pf = 1.0
    for m in MECHS:
        pf *= 1 - P[m]
    print(f"\nP(one run catches every trap) ~ {pf:.4f} (independence) -> E[full passes of 6] ~ {6*pf:.3f}")
    print(f"Expected traps landed per run at design rates: {sum(P.values()):.2f}")
    print("\nSix-run Monte Carlo (landing scale x rho)")
    print("  scale  rho   mean_rate  E[avg]  E[SD]  P(cap)  P(SD)  P(<5 full)  P(patterns)  P(all gates)")
    for scale, rho in [(1.0, 0.2), (1.0, 0.35), (1.0, 0.6), (0.8, 0.35), (0.7, 0.35), (0.6, 0.35), (0.5, 0.35), (0.4, 0.35)]:
        r = sim(scale, rho)
        mr = sum(min(P[m]*scale, .97) for m in MECHS) / len(MECHS)
        print(f"  {scale:4.2f}  {rho:4.2f}  {mr:8.2f}  {r['E_avg']:6.1%}  {r['E_sd']:5.3f}  {r['cap']:6.2f}  {r['sd']:5.2f}  {r['full']:10.2f}  {r['pat']:11.2f}  {r['all']:12.2f}")

if __name__ == "__main__":
    main()
