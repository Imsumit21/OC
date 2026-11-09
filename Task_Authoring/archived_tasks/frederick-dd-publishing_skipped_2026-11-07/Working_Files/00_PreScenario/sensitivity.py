#!/usr/bin/env python3
"""Sensitivities on the v2 lean surface (UNCALIBRATED), against the requester cap of 80 %."""
import random
from statistics import NormalDist
import policy_model as pm
base_total = pm.TOTAL
def run(label, scale=1.0, rho=0.35, P=None, extra=0):
    pm.TOTAL = base_total + extra
    r = pm.sim(scale, rho, n=6000, P_=P)
    pm.TOTAL = base_total
    fl = sum(w for _, w, m in pm.SLOTS if m) / (base_total + extra)
    print(f"  {label:52} flippable {fl:5.1%}  E[avg] {r['E_avg']:6.1%}  E[SD] {r['E_sd']:.3f}  P(cap) {r['cap']:.2f}  P(SD) {r['sd']:.2f}  P(pat) {r['pat']:.2f}  P(all) {r['all']:.2f}")
print("Row growth: always-pass weight /rubric may add (Q4 went 57 -> 102 rows, Robert 73 -> 130)")
for extra in (0, 40, 80, 120):
    run(f"+{extra} always-pass weight, design rates", extra=extra)
    run(f"+{extra} always-pass weight, 0.7x rates", scale=0.7, extra=extra)
print("\nLedger view (family priors where they exist; 0.30 where none)")
L = {"DONE": .50, "CORR": .17, "INPUT": .17, "FILT1": .33, "FILT2": .33, "ALIAS": .30, "EXC": .30, "FOLLOW": .30}
run("ledger priors", P=L)
run("ledger priors, +40 always-pass weight", P=L, extra=40)
print("\nCorrelation")
for rho in (0.2, 0.35, 0.6, 0.8):
    run(f"rho {rho}", rho=rho)
print("\nPre-check (one run, rho 0.35)")
N = NormalDist()
central = ("DONE", "CORR", "EXC", "INPUT", "FILT2")
for scale in (1.0, 0.7, 0.5):
    rnd = random.Random(5); n = 40000; ge2 = cen = none = 0
    for _ in range(n):
        z = rnd.gauss(0, 1); hit = set()
        for m in pm.MECHS:
            x = (0.35 ** 0.5) * z + (0.65 ** 0.5) * rnd.gauss(0, 1)
            if N.cdf(x) < min(pm.P[m] * scale, .97):
                hit.add(m)
        ge2 += len(hit) >= 2; cen += bool(hit & set(central)); none += not hit
    print(f"  scale {scale}: P(no trap lands) {none/n:.3f}  P(two or more land) {ge2/n:.2f}  P(first pick, second pick or Q4 total wrong) {cen/n:.2f}")
