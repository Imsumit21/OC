#!/usr/bin/env python3
"""Pre-scenario policy model (UNCALIBRATED). Sketch surface for storyline A (bridge-round pipeline).
Scores whole policies, single misses, and a Monte-Carlo six-run gate estimate. Design aid only."""
import itertools, random, statistics, json, sys
NORM = statistics.NormalDist()

# slot: (id, weight, mechanisms that can flip it, note)
SLOTS = [
    ("S1_volume_firm_count", 3, ["FILT1", "FILT2"], "register firm count"),
    ("S2_status_sample_1", 3, [], "plain status from cc'd thread"),
    ("S3_status_sample_2", 3, [], ""),
    ("S4_status_sample_3", 3, [], ""),
    ("S5_status_sample_4", 3, [], ""),
    ("S6_status_sample_5", 3, [], ""),
    ("X1_corr_firm_passed", 5, ["CORR"], "verbal pass recorded off the email thread"),
    ("X2_alias_firm_passed", 5, ["ALIAS"], "pass mail under the fund's other name"),
    ("X3_outside_filter_firm1", 5, ["FILT1"], "pitched firm absent from the list"),
    ("X4_outside_filter_firm2", 5, ["FILT2"], "second pitched firm absent from the list"),
    ("X5_soft_circle_not_committed", 5, ["DONE1"], "verbal yes, SAFE unsigned"),
    ("X6_build_access_still_owed", 5, ["DONE2"], "email says invites sent; Android add never landed"),
    ("A1_committed_total", 5, ["DONE1", "INPUT"], "committed $ total"),
    ("W1_sheet_in_board_folder", 1, [], "delivery"),
    ("W2_reply_on_ask_thread", 1, [], "delivery"),
    ("W3_reply_passed_count", 3, ["CORR", "ALIAS"], "passed count"),
    ("W4_reply_committed_total", 5, ["DONE1", "INPUT"], "same fact as A1 (2 slots max)"),
    ("W5_followthrough_count", 3, ["FOLLOW", "CORR", "ALIAS"], "keep-warm checklist count"),
    ("W6_followthrough_sample", 3, ["FOLLOW"], "one named passed firm on checklist"),
]
TOTAL = sum(w for _, w, _, _ in SLOTS)
MECHS = ["DONE1", "DONE2", "CORR", "ALIAS", "FILT1", "FILT2", "INPUT", "FOLLOW"]
# per-run probability that the mechanism LANDS (agent misses the hard record); varied findability tiers
P = {"DONE1": 0.55, "DONE2": 0.50, "CORR": 0.50, "ALIAS": 0.35,
     "FILT1": 0.45, "FILT2": 0.30, "INPUT": 0.40, "FOLLOW": 0.55}
BASE_SLIP = 0.03  # per non-mechanism slot

def score(landed, slips=frozenset()):
    lost = 0
    for sid, w, m, _ in SLOTS:
        if any(x in landed for x in m) or sid in slips:
            lost += w
    return 1 - lost / TOTAL

def failed(landed, slips=frozenset()):
    return frozenset(sid for sid, w, m, _ in SLOTS if any(x in landed for x in m) or sid in slips)

def patterns(fsets):
    fs = [f for f in fsets if f]
    parent = list(range(len(fs)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]; i = parent[i]
        return i
    for i, j in itertools.combinations(range(len(fs)), 2):
        if len(fs[i] ^ fs[j]) <= 1:
            parent[find(i)] = find(j)
    groups = {}
    for i in range(len(fs)):
        groups.setdefault(find(i), []).append(i)
    return len(groups), (max(len(g) for g in groups.values()) / len(fs) if fs else 0)

def sim(n=20000, rho=0.35, seed=7):
    rnd = random.Random(seed)
    ok = avgs = 0; inband = 0; pat = 0; fp = 0; cap = 0; av = []
    for _ in range(n):
        runs = []; fsets = []
        for _ in range(6):
            z = rnd.gauss(0, 1)  # shared run-level latent (Gaussian copula: marginals stay exactly P)
            landed = set()
            for m in MECHS:
                x = (rho ** 0.5) * z + ((1 - rho) ** 0.5) * rnd.gauss(0, 1)
                if NORM.cdf(x) < P[m]:
                    landed.add(m)
            slips = {sid for sid, w, mm, _ in SLOTS if not mm and rnd.random() < BASE_SLIP}
            runs.append(score(landed, slips)); fsets.append(failed(landed, slips))
        a = statistics.mean(runs); sd = statistics.pstdev(runs)
        full = sum(1 for r in runs if r >= 0.9999)
        npat, largest = patterns(fsets)
        g_cap = a < 0.85; g_sd = 0.10 <= sd <= 0.30; g_full = full < 5
        g_pat = npat >= 2 and largest <= 0.5
        av.append(a); cap += g_cap; inband += g_sd; pat += g_pat; fp += g_full
        ok += g_cap and g_sd and g_full and g_pat
    return {"E_avg": round(statistics.mean(av), 3), "P_cap": cap / n, "P_sd_band": inband / n,
            "P_patterns": pat / n, "P_fullpass_ok": fp / n, "P_all_gates": ok / n}

if __name__ == "__main__":
    print(f"UNCALIBRATED policy model · total weight {TOTAL} · mechanism-flippable "
          f"{sum(w for _, w, m, _ in SLOTS if m)} ({sum(w for _, w, m, _ in SLOTS if m)/TOTAL:.0%})")
    print("\nWhole policies (score with the named mechanisms landed):")
    pol = {
        "perfect run": set(),
        "reads every cc'd thread, no off-thread checks (CORR,DONE1,DONE2,FOLLOW land)": {"CORR", "DONE1", "DONE2", "FOLLOW"},
        "list-bound (FILT1,FILT2,ALIAS land)": {"FILT1", "FILT2", "ALIAS"},
        "trusts 'done' sources (DONE1,DONE2,INPUT land)": {"DONE1", "DONE2", "INPUT"},
        "everything but follow-through (FOLLOW lands)": {"FOLLOW"},
        "lazy: every mechanism lands": set(MECHS),
    }
    for k, v in pol.items():
        print(f"  {score(v):6.1%}  {k}")
    print("\nSingle misses (one mechanism lands, all else right):")
    for m in MECHS:
        print(f"  {score({m}):6.1%}  {m}")
    base = dict(P)
    print(f"\nMonte Carlo six-run gates (Gaussian copula; landing P x scale; base slip {BASE_SLIP}); design P = {base}")
    for scale in (1.0, 0.75, 0.6, 0.5):
        for rho in (0.3, 0.6):
            P.update({k: v * scale for k, v in base.items()})
            print(f"  scale {scale:.2f} rho {rho}: ", json.dumps(sim(n=8000, rho=rho)))
    P.update(base)
