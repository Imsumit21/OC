#!/usr/bin/env python3
"""Per-run counted-call model for storyline A (UNCALIBRATED design aid). Ranges come from measured Opus 5.5 habits on Robert's
Feb 14 tasks (wind-down: list_comments 23-28 of 28, Gmail searches 10-25 plus 4-7 batches, Slack reads and searches 5-20;
LLC: 149-162 counted calls on 38 issues). gmail_get_messages_batch takes up to 100 ids, so the 132 notices buy few calls.
No padding: every call answers a distinct question about a source-defined payee or performs a write a record asks for."""
import random, statistics
N_ISSUES = (22, 24)
def run(r, close_writes=True):
    n = r.randint(*N_ISSUES)
    comments_read = round(n * r.uniform(.85, 1.0))
    closes = round(n * r.uniform(.7, 1.0)) if close_writes else 0
    exception_comments = r.randint(1, 6)
    linear_meta = r.randint(2, 4)
    slack = r.randint(14, 26)          # ask thread, #winddown pages, founder channels, #leapblock, name searches
    gmail_notices = r.randint(5, 12)   # search pages plus batches over 132 notices and their siblings
    gmail_payee = r.randint(10, 28)    # per-payee lookups: invoices, receipts, Western Union, Node Media, Chase
    docs_drive = r.randint(6, 14)      # method doc, MSA and consulting agreements, Drive listing
    sheets_read = r.randint(2, 6)      # P&L costs tab
    warehouse = r.randint(3, 8)
    other = r.randint(1, 6)            # contacts, calendar, Trello
    write = r.randint(5, 9)            # create, move, two shares, value updates, read-back, reply
    return comments_read + closes + exception_comments + linear_meta + slack + gmail_notices + gmail_payee + docs_drive + sheets_read + warehouse + other + write
for label, cw in [("with the issue closes", True), ("without them", False)]:
    r = random.Random(7)
    x = sorted(run(r, cw) for _ in range(20000))
    six = [min(run(r, cw) for _ in range(6)) for _ in range(5000)]
    print(f"UNCALIBRATED {label}: mean {statistics.mean(x):.0f}, p5 {x[1000]}, p50 {x[10000]}, p95 {x[19000]}; P(run < 100) {sum(v < 100 for v in x) / len(x):.3f}; P(run <= 130) {sum(v <= 130 for v in x) / len(x):.3f}; median six-run minimum {sorted(six)[2500]}")
