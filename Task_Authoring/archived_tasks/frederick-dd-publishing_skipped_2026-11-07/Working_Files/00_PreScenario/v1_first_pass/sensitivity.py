#!/usr/bin/env python3
"""Sensitivities on the sketch surface (UNCALIBRATED). Reuses policy_model; changes one assumption at a time."""
import policy_model as pm, random, statistics
base_total = pm.TOTAL
def run(label, scale=1.0, rho=0.35, P=None, extra=0):
    pm.TOTAL = base_total + extra
    r = pm.sim(scale, rho, n=6000, P_=P)
    pm.TOTAL = base_total
    print(f"  {label:58} E[avg] {r['E_avg']:6.1%}  E[SD] {r['E_sd']:.3f}  P(cap) {r['cap']:.2f}  P(SD) {r['sd']:.2f}  P(pat) {r['pat']:.2f}  P(all) {r['all']:.2f}")
print("Row-growth dilution: always-pass weight added by /rubric per-target rows")
for extra in (0, 40, 80):
    run(f"+{extra} always-pass weight, design rates", extra=extra)
    run(f"+{extra} always-pass weight, 0.7x rates", scale=0.7, extra=extra)
print("\nNear-certain miss: FILT2 landing rate")
for v in (0.8, 0.6, 0.4):
    P = dict(pm.P); P["FILT2"] = v
    run(f"FILT2 at {v}", P=P)
print("\nCorrelation: thorough searchers catch the Slack-side traps together")
for rho in (0.2, 0.35, 0.6, 0.8):
    run(f"rho {rho}", rho=rho)
print("\nPre-check (one run): P(at most one trap lands), P(two or more land)")
for scale in (1.0, 0.7, 0.5):
    rnd = random.Random(5); n = 40000; le1 = 0
    from statistics import NormalDist
    N = NormalDist()
    for _ in range(n):
        z = rnd.gauss(0, 1); c = 0
        for m in pm.MECHS:
            x = (0.35 ** 0.5) * z + (0.65 ** 0.5) * rnd.gauss(0, 1)
            c += N.cdf(x) < min(pm.P[m] * scale, .97)
        le1 += c <= 1
    print(f"  scale {scale}: P(<=1) {le1/n:.2f}  P(>=2) {1-le1/n:.2f}")
