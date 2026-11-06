#!/usr/bin/env python3
"""Per-run counted-call model for storyline A v3 (UNCALIBRATED design aid). Requester target 2026-11-05: more than
130 counted calls in EVERY run. Ranges come from measured Opus 5.5 habits on Robert's Feb 14 wind-down task
(exposure_robert_runs.txt: per-issue linear_list_comments 23-28 of 28, one linear_create_comment per issue, Gmail
searches 10-25, Slack reads/searches 5-20) and the bridge task's one-write-per-entry pattern. No padding: every call
answers a distinct question about a source-defined item or performs a write a record asks for."""
import random, statistics
N_ISSUES = (36, 40)          # candidate issues Leonard seeds in the LLC project (cohort, source-defined)
def run(rnd):
    n = rnd.randint(*N_ISSUES)
    read_comments = round(n * rnd.uniform(0.82, 1.0))      # 23-28 of 28 measured
    comment_writes = n                                      # one decision comment per issue (6/6 measured)
    state_writes = round(n * rnd.uniform(0.55, 1.0))        # every issue gets a state; some runs skip unchanged ones
    new_issues = rnd.choice([0, 1, 1, 2])                   # the campaign issue (FILT) and any other missing item
    discovery = rnd.randint(14, 24)                         # DM, ground rules, #winddown pages, threads, channels
    warehouse = rnd.randint(2, 6)                           # list, describe, January query
    off_issue_checks = rnd.randint(10, 28)                  # name searches in Slack/Gmail, calendar, GitHub, Drive
    linear_meta = rnd.randint(2, 4)                         # teams, project, states
    sheet = rnd.randint(5, 8)                               # create, move, two shares, value updates, read-back
    reply = 1
    return read_comments + comment_writes + state_writes + new_issues + discovery + warehouse + off_issue_checks + linear_meta + sheet + reply
rnd = random.Random(7)
runs = [run(rnd) for _ in range(20000)]
six_min = [min(run(rnd) for _ in range(6)) for _ in range(5000)]
print("UNCALIBRATED per-run counted calls: mean %.0f, p5 %d, p50 %d, p95 %d, min %d" % (statistics.mean(runs), sorted(runs)[1000], sorted(runs)[10000], sorted(runs)[19000], min(runs)))
print("P(one run <= 130) = %.3f; P(all six runs > 130) = %.3f; median of the six-run minimum = %d" % (sum(r <= 130 for r in runs)/len(runs), sum(m > 130 for m in six_min)/len(six_min), sorted(six_min)[2500]))
