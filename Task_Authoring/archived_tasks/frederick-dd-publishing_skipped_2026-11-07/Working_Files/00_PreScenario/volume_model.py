#!/usr/bin/env python3
"""Per-run counted-call estimate (UNCALIBRATED) against the requester floor of more than 130 in EVERY run.
Reads are anchored on stored runs (stored_runs_counted_output.txt): bridge 54-95, Q4 61-119, LLC 69-81.
A run that misses traps also skips writes, so the plan's writes are discounted by the expected misses."""
import random, statistics
W = {"contact per publisher with a named person": 22, "group checklists": 4, "checklist item per publisher": 26,
     "follow-up cards": 16, "comment on an existing card": 1, "reminders": 8, "follow-through drafts": 3,
     "sheet create, values, move": 5, "reply": 1}
wr = sum(W.values())
print("Planned writes", wr, W)
q = lambda a, p: a[int(p * len(a))]
for label, shift in [("all writes made", 0), ("run skips 6 writes through misses", -6), ("run skips 10 writes", -10)]:
    rnd = random.Random(3); mins = []; allr = []
    for _ in range(40000):
        runs = [rnd.triangular(54, 125, 85) + rnd.gauss(wr + shift, 2) for _ in range(6)]
        mins.append(min(runs)); allr += runs
    mins.sort(); allr.sort()
    print(f"{label:36} per run mean {statistics.mean(allr):.0f}, p5 {q(allr,.05):.0f}; six-run minimum median {q(mins,.5):.0f}, p5 {q(mins,.05):.0f}; P(every run > 130) {sum(m>130 for m in mins)/len(mins):.3f}")
