#!/usr/bin/env python3
"""Advisory, UNCALIBRATED: odds that a fresh six-run batch clears the platform gates, from observed miss rates.

Assumes each decision is missed independently in each run at the given rate and that a miss flips the rubric rows
listed in FOOT (09_Rubrics.json 923f89f3ac9c, total weight 165). The Domino Delights build total on the sheet (R25)
and in the reply (R58) fail whenever any Domino Delights build figure is wrong. Pattern grouping is the calculator's
single-linkage rule (same pattern unless two runs differ on two or more rows).
"""
import itertools
import random
import statistics

TOTAL = 165
FOOT = {"OFF": [("R8", 5), ("R33", 5), ("R69", 1)], "RET": [("R7", 5), ("R32", 5), ("R68", 1)],
        "CORR": [("R9", 5), ("R10", 5), ("R34", 5), ("R70", 1)], "ALIAS": [("R12", 5)]}
SHARED = ("OFF", "RET", "CORR")


def simulate(rates, foot=FOOT, n=200000, seed=7):
    rng = random.Random(seed)
    ok = dict(pattern=0, sd=0, avg=0, full=0, platform=0)
    for _ in range(n):
        runs = []
        for _run in range(6):
            miss = {m for m in rates if rng.random() < rates[m]}
            rows = {}
            for m in miss:
                rows.update(dict(foot[m]))
            if miss & set(SHARED):
                rows.update({"R25": 5, "R58": 5})
            runs.append(rows)
        scores = [1 - sum(r.values()) / TOTAL for r in runs]
        failing = [frozenset(r) for r in runs if r]
        parent = list(range(len(failing)))
        def find(x):
            while parent[x] != x:
                x = parent[x]
            return x
        for i, j in itertools.combinations(range(len(failing)), 2):
            if len(failing[i] ^ failing[j]) <= 1:
                parent[find(i)] = find(j)
        groups = {}
        for i in range(len(failing)):
            groups.setdefault(find(i), []).append(i)
        pattern = len(groups) >= 2 and max(map(len, groups.values())) <= 0.5 * len(failing)
        avg, sd, full = statistics.mean(scores), statistics.pstdev(scores), 6 - len(failing)
        ok["pattern"] += pattern
        ok["sd"] += 0.1 <= sd <= 0.3
        ok["avg"] += avg < 0.9
        ok["full"] += full < 5
        ok["platform"] += pattern and avg < 0.9 and full < 5
    return {k: round(v / n, 3) for k, v in ok.items()}


if __name__ == "__main__":
    observed = {"OFF": 10 / 13, "RET": 3 / 13, "CORR": 1 / 13, "ALIAS": 4 / 13}
    two_rows = dict(FOOT, ALIAS=[("R12", 5), ("Rnew", 3)])
    cases = [("observed rates (13 rev7 runs), rubric as is", observed, FOOT),
             ("observed rates, Node Media line graded on two cells", observed, two_rows),
             ("CORR missed 40%, others observed", dict(observed, CORR=0.4), FOOT),
             ("CORR missed 40% and Node Media on two cells", dict(observed, CORR=0.4), two_rows),
             ("OFF missed 50%, others observed", dict(observed, OFF=0.5), FOOT),
             ("RET missed 50%, others observed", dict(observed, RET=0.5), FOOT)]
    for label, rates, foot in cases:
        print(f"{label:55s} {simulate(rates, foot)}")
