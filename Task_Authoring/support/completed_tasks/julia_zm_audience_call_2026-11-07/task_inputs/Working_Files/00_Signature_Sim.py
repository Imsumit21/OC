#!/usr/bin/env python3
"""Signature-share simulation on the real gradable surface (UNCALIBRATED).
Each run misses channels at the given rates; a missed rule fails every slot listing it; unmapped slots fail at a 5 %
slip rate. Patterns use the gate's rule: single-linkage over failed-slot sets differing by at most one slot.
Prints P(largest pattern share < 45 %) and P(<= 50 %, the platform gate), with at least 2 patterns, for six runs."""
import json, math, random, sys

SURF = 'Task_Authoring/task_inputs/Working_Files/01_Gradable_Surface.json'
slots = json.load(open(SURF, encoding='utf-8'))['slots']


def patterns(fs):
    fs = [f for f in fs if f]
    n = len(fs)
    par = list(range(n))

    def fd(x):
        while par[x] != x:
            par[x] = par[par[x]]
            x = par[x]
        return x
    for i in range(n):
        for j in range(i + 1, n):
            if len(fs[i] ^ fs[j]) <= 1:
                par[fd(i)] = fd(j)
    c = {}
    for i in range(n):
        c[fd(i)] = c.get(fd(i), 0) + 1
    return n, len(c), max(c.values()) if c else 0


def sim(rates, rho, slip=.05, T=30000, seed=11):
    rnd = random.Random(seed)
    lt45 = le50 = 0
    for _ in range(T):
        fs = []
        for r in range(6):
            z = rnd.gauss(0, 1)
            miss = {c for c, p in rates.items()
                    if rnd.random() < 1 / (1 + math.exp(-(math.log(p / (1 - p)) - rho * z)))}
            f = frozenset(s['id'] for s in slots
                          if (set(s['mechanisms']) & miss) or (not s['mechanisms'] and rnd.random() < slip))
            fs.append(f)
        n, k, big = patterns(fs)
        if n == 0:
            continue
        lt45 += k >= 2 and big / n < .45
        le50 += k >= 2 and big / n <= .5
    return lt45 / T, le50 / T


S = {
    'current, reviewer odds': dict(R_K1=.60, R_K3=.62, R_K4=.55, R_K5=.25, R_F=.30, R_D=.05, R_E=.05),
    'option B (K1,K4 found ~75%)': dict(R_K1=.25, R_K3=.62, R_K4=.25, R_K5=.25, R_F=.30, R_D=.05, R_E=.05),
    'balanced near 50%': dict(R_K1=.50, R_K3=.50, R_K4=.50, R_K5=.50, R_F=.30, R_D=.05, R_E=.05),
    'strong Opus': dict(R_K1=.25, R_K3=.25, R_K4=.20, R_K5=.15, R_F=.15, R_D=.03, R_E=.03),
}
print('%-30s %4s %10s %10s' % ('scenario (real surface)', 'rho', 'P(<45%)', 'P(<=50%)'))
for k, v in S.items():
    for rho in (0, .6):
        a, b = sim(v, rho)
        print('%-30s %4.1f %9.0f%% %9.0f%%' % (k, rho, 100 * a, 100 * b))
