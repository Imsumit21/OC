#!/usr/bin/env python3
"""Whole-policy and single-miss scores on the rubric skeleton (the rows the portal's rules force), then a six-run
simulation at the budget's find-rate ranges. UNCALIBRATED: the find rates are ranges from archived tasks, not
measurements of this task. A row fails when any budget unit that lists it was missed."""
import json, random, statistics, itertools
from pathlib import Path
WF = Path(__file__).resolve().parents[1]
rows = json.loads((WF / "01_Rubric_Skeleton.json").read_text())["rows"]
budget = json.loads((WF / "01_Difficulty_Budget.json").read_text())
units = [u for u in budget["units"] if u["role"] != "realism"]
flips = {u["id"]: {r["id"] for r in u["rows"]} for u in units}
shared = {r["id"]: set() for r in rows}
mech_unit = {u["mechanism"]: u["id"] for u in units}
for r in rows:                                        # a row with several mechanisms fails when any of their units is missed
    for m in r.get("mechanisms") or []:
        if m in mech_unit: shared[r["id"]].add(mech_unit[m])
for uid, rs in flips.items():
    for rid in rs: shared[rid].add(uid)
weight = {r["id"]: r["weight"] for r in rows}; total = sum(weight.values())
def failed(missed): return frozenset(rid for rid, us in shared.items() if us & missed)
def score(missed): return 1 - sum(weight[r] for r in failed(missed)) / total
ids = [u["id"] for u in units]; name = {u["id"]: u["mechanism"] for u in units}
print(f"Rubric skeleton: {len(rows)} rows, total weight {total}; budget basis {budget['weight_basis']}  (UNCALIBRATED)")
print("\nWhole policies:")
for label, missed in (("reads everything", set()),
                      ("the ask, the notes, the pack list, the channel and every line's own ticket; nothing else", set(ids)),
                      ("that, plus pull requests and #zombie-art since the zip", set(ids) - {"C1"}),
                      ("that, plus every thread Robert posted in and the pack ticket's own comments", set(ids) - {"C1", "C3", "C4"}),
                      ("everything except the two anchor records", {"A1", "A2"}),
                      ("both anchors found, every coin-flip record missed", set(ids) - {"A1", "A2"})):
    print(f"  {score(missed)*100:5.1f} %  {label}")
print("\nSingle misses (everything else found):")
for u in units: print(f"  {score({u['id']})*100:5.1f} %  miss {u['id']} ({u['mechanism']}, {u['carrier']})")
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
rng = random.Random(20261111); LOSS = budget["undesigned_loss"]; TR = 20000
print("\nSix-run simulation, 20,000 trials per setting:")
print("  setting    E[avg]   P(avg<70)  P(<5 full)  P(SD band)  P(patterns)  P(ALL GATES)  mean SD")
for label, end in (("low find", 0), ("midpoint", 1), ("high find", 2)):
    rates = {u["id"]: (u["find_rate"][0], sum(u["find_rate"]) / 2, u["find_rate"][1])[end] for u in units}
    loss = (LOSS[1], sum(LOSS) / 2, LOSS[0])[end]; c = dict(a=0, f=0, s=0, p=0, all=0); es = sds = 0.0
    cache = {}
    for _ in range(TR):
        sc, fl = [], []
        for _r in range(6):
            missed = frozenset(uid for uid in ids if rng.random() >= rates[uid])
            if missed not in cache: cache[missed] = failed(missed)
            f = cache[missed]; fl.append(f); sc.append(1 - sum(weight[r] for r in f) / total - loss)
        avg = sum(sc) / 6; sd = statistics.pstdev(sc)
        ga, gf, gs, gp = avg < 0.70, True, 0.10 <= sd <= 0.30, patterns_ok(fl)
        c["a"] += ga; c["f"] += gf; c["s"] += gs; c["p"] += gp; c["all"] += (ga and gf and gs and gp); es += avg; sds += sd
    print(f"  {label:9}  {es/TR*100:5.1f} %   {c['a']/TR:.3f}      {c['f']/TR:.3f}       {c['s']/TR:.3f}       {c['p']/TR:.3f}        {c['all']/TR:.3f}       {sds/TR:.3f}")
print("\nTargets: E[avg] <= 62 %, P(all gates) >= 0.5.")
