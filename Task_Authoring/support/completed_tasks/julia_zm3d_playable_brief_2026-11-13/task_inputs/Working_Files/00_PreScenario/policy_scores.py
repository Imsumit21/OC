#!/usr/bin/env python3
"""Pre-scenario policy scoring on the SKETCH surface (storyline A). UNCALIBRATED.

Scores whole retrieval policies and single misses on sketch_surface.json, then simulates six runs with each unit's
find-rate range from sketch_budget.json and reports E[average] and the joint chance that every baseline gate passes
(average strictly under 0.70, fewer than five full passes, population SD inside 0.10-0.30, two or more failure
patterns with the largest at most half of the failing runs; two runs share a pattern unless they differ on two or
more rows, grouped by single linkage as difficulty_stats does). A row fails when any unit that can flip it was missed.
The numbers describe this sketch, not Opus 5.5: the find rates are ranges taken from carrier_find_rates.json.
/create-scenario S5c repeats this on the real surface before any SQL.
"""
import json, random, statistics, itertools
from pathlib import Path
HERE = Path(__file__).resolve().parent
surface = json.loads((HERE / "sketch_surface.json").read_text())["slots"]
budget = json.loads((HERE / "sketch_budget.json").read_text())
units = [u for u in budget["units"] if u["role"] != "realism"]
mech_unit = {u["mechanism"]: u["id"] for u in units}
total = sum(s["weight"] for s in surface)
CAP, RUNS, TRIALS = 0.70, 6, 20000
FMT_FIND = (0.10, 0.35, 0.60)          # realism unit R1 (old base vendor rules): assumed range, not in the budget
LOSS = budget.get("undesigned_loss", [0.0, 0.0])

def failed_rows(missed, fmt_missed):
    out = []
    for s in surface:
        ms = s["mechanisms"]
        if any(mech_unit.get(m) in missed for m in ms) or (fmt_missed and "FMT" in ms):
            out.append(s["id"])
    return out
weight = {s["id"]: s["weight"] for s in surface}
def score(missed, fmt_missed=False):
    return 1 - sum(weight[r] for r in failed_rows(missed, fmt_missed)) / total

ids = [u["id"] for u in units]
print(f"SKETCH surface: {len(surface)} rows, total weight {total}  (UNCALIBRATED)")
print("\nWhole policies (rows failed = rows of every unit the policy never opens):")
policies = [
    ("P0 reads everything", set(), False),
    ("P1 hub, shortlist and item tickets only (no comments on other tickets, no DMs, no PR reviews, no other channels)", set(ids), True),
    ("P2 P1 + pull-request reviews and vendor-channel search", set(ids) - {"C1", "C2"}, True),
    ("P3 P1 + every thread and channel the ask's people post in (no DMs, no off-set tickets)", {"A1", "A2", "C1"}, False),
    ("P4 everything except the two anchor records", {"A1", "A2"}, False),
    ("P5 both anchors found, every coin-flip record missed", set(ids) - {"A1", "A2"}, False),
]
for name, missed, fmt in policies:
    print(f"  {score(missed, fmt)*100:5.1f} %  {name}")
print("\nSingle misses (everything else found):")
for u in units:
    print(f"  {score({u['id']})*100:5.1f} %  miss {u['id']} ({u['mechanism']}, {u['carrier']})")
print(f"  {score(set(), True)*100:5.1f} %  miss R1 (FMT, realism: old base vendor rules)")

def patterns_ok(fails):
    failing = [f for f in fails if f]
    if not failing: return False
    parent = list(range(len(failing)))
    def find(x):
        while parent[x] != x: parent[x] = parent[parent[x]]; x = parent[x]
        return x
    for a, b in itertools.combinations(range(len(failing)), 2):
        if len(failing[a] ^ failing[b]) <= 1: parent[find(a)] = find(b)
    sizes = {}
    for i in range(len(failing)): sizes[find(i)] = sizes.get(find(i), 0) + 1
    return len(sizes) >= 2 and max(sizes.values()) <= len(failing) / 2

rng = random.Random(20261111)
print("\nSix-run simulation, 20,000 trials per setting:")
print("  setting   E[avg]   P(avg<70)  P(<5 full)  P(SD band)  P(patterns)  P(ALL GATES)   mean SD")
for label, end in (("low find", 0), ("midpoint", 1), ("high find", 2)):
    rates = {u["id"]: (u["find_rate"][0], sum(u["find_rate"]) / 2, u["find_rate"][1])[end] for u in units}
    loss = (LOSS[1], sum(LOSS) / 2, LOSS[0])[end]
    c = dict(avg=0, full=0, sd=0, pat=0, all=0); esum = 0.0; sdsum = 0.0
    for _ in range(TRIALS):
        scores, fails = [], []
        for _r in range(RUNS):
            missed = {uid for uid in ids if rng.random() >= rates[uid]}
            fmt = rng.random() >= FMT_FIND[end]
            rows = frozenset(failed_rows(missed, fmt))
            fails.append(rows)
            scores.append(1 - sum(weight[r] for r in rows) / total - loss)
        avg = sum(scores) / RUNS; sd = statistics.pstdev(scores)
        full = sum(1 for f in fails if not f) if loss == 0 else 0
        g_avg, g_full, g_sd, g_pat = avg < CAP, full < 5, 0.10 <= sd <= 0.30, patterns_ok(fails)
        c["avg"] += g_avg; c["full"] += g_full; c["sd"] += g_sd; c["pat"] += g_pat; c["all"] += (g_avg and g_full and g_sd and g_pat)
        esum += avg; sdsum += sd
    print(f"  {label:9} {esum/TRIALS*100:5.1f} %   {c['avg']/TRIALS:.3f}      {c['full']/TRIALS:.3f}       {c['sd']/TRIALS:.3f}       {c['pat']/TRIALS:.3f}        {c['all']/TRIALS:.3f}        {sdsum/TRIALS:.3f}")
print("\nTargets (goal rule 5): E[avg] <= 62 %, P(all gates) >= 0.5.")
