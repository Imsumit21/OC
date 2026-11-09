#!/usr/bin/env python3
"""Per-run counted-call model for the stockholder close-out (UNCALIBRATED design aid). Ranges follow census_C5 (about 45 discovery
calls plus unbatchable per-target calls; no Leonard run exists, so habits are by analogy from Robert and Frederick). Gmail reads can
batch at 100 ids, so the Carta notices buy few calls. No padding: each issue is one real holder and each read answers that holder's
own question; each write is asked for by a record."""
import random, statistics
def run(r, issues=26, closes=True, notices=True, comment_targets=26):
    comments_read = round(issues * r.uniform(.85, 1.0))
    comment_write = round(comment_targets * r.uniform(.85, 1.0))
    move = round(issues * r.uniform(.7, 1.0)) if closes else 0
    notes = r.randint(7, 9)
    opt_notices = r.randint(8, 12) if notices else 0
    calls = r.randint(0, 8)
    linear_meta = r.randint(2, 4)
    slack = r.randint(12, 24)
    gmail = r.randint(14, 34)
    docs = r.randint(8, 16)
    sheets_snow = r.randint(3, 8)
    other = r.randint(1, 5)
    write = r.randint(6, 10)
    return comments_read + comment_write + move + notes + opt_notices + calls + linear_meta + slack + gmail + docs + sheets_snow + other + write
for label, kw in [("as sketched", {}), ("without state moves", {"closes": False}), ("without option notices", {"notices": False}), ("without either", {"closes": False, "notices": False}), ("variant H: state moves, no option notices, 14 exception comments", {"notices": False, "comment_targets": 14})]:
    r = random.Random(7)
    x = sorted(run(r, **kw) for _ in range(20000))
    six = [min(run(r, **kw) for _ in range(6)) for _ in range(5000)]
    print(f"UNCALIBRATED {label}: mean {statistics.mean(x):.0f}, p5 {x[1000]}, p50 {x[10000]}, p95 {x[19000]}; P(run < 100) {sum(v < 100 for v in x) / len(x):.3f}; P(run < 130) {sum(v < 130 for v in x) / len(x):.3f}; median six-run minimum {statistics.median(six):.0f}")
