#!/usr/bin/env python3
"""Per-run counted-call estimate (UNCALIBRATED). Reads anchored on stored Opus 5.5 runs: Q4 commitments 152-212 total calls,
bridge 109-150, LLC 152-163 (exposure_stored_runs_output.txt). Writes are the planned single-object writes."""
import random, statistics
W = {"sheet create, values, move": 5, "contact per publisher that answered": 19, "BD Follow Up card, checklist, items": 25,
     "mail drafts": 8, "calendar reminders": 5, "reply": 1, "read-backs": 3}
wr = sum(W.values())
print("Planned single-object writes", wr, W)
rnd = random.Random(3); mins = []; allruns = []
for _ in range(40000):
    runs = [rnd.triangular(60, 150, 90) + rnd.gauss(wr, 3) for _ in range(6)]
    mins.append(min(runs)); allruns += runs
mins.sort(); allruns.sort()
q = lambda a, p: a[int(p * len(a))]
print(f"per run: mean {statistics.mean(allruns):.0f}, p5 {q(allruns,.05):.0f}, p95 {q(allruns,.95):.0f}")
print(f"six-run minimum: median {q(mins,.5):.0f}, p5 {q(mins,.05):.0f}")
print(f"P(six-run minimum > 100) {sum(m>100 for m in mins)/len(mins):.3f}   P(> 130) {sum(m>130 for m in mins)/len(mins):.3f}")
