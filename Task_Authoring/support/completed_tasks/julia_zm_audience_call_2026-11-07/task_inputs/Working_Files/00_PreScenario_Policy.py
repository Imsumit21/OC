#!/usr/bin/env python3
"""Pre-scenario policy scoring, rev3 (UNCALIBRATED). Reads the provisional probe surface; prints whole-policy and
single-miss scores, a six-run Monte Carlo, and the chance one run lands blocks that need reversal.
Rate rows: author prior; measured carrier rates; independent reviewer's judgement. None measures this design.
PAD adds always-pass weight, because a real rubric holds more passing rows than this probe (illustrative)."""
import json, math, random, statistics as st, sys

S = json.load(open(sys.argv[1], encoding='utf-8'))['slots']
TOT0 = sum(s['weight'] for s in S)
BLOCKS = ['K1', 'K3', 'K4', 'K5']
ALL = BLOCKS + ['K2', 'F', 'S', 'D', 'E', 'C']


def chans(s):
    return set(s.get('channels') or ([s['channel']] if s.get('channel') else []))


def score(missed, extra=frozenset(), pad=0):
    return (sum(s['weight'] for s in S if not (chans(s) & missed) and s['id'] not in extra) + pad) / (TOT0 + pad)


print('total weight', TOT0, '| rows', len(S), '| w5', sum(s['weight'] == 5 for s in S),
      '| flippable %.1f%%' % (100 * sum(s['weight'] for s in S if chans(s)) / TOT0))
for c in ALL:
    print('  unit %-3s can flip %.1f%%' % (c, 100 * sum(s['weight'] for s in S if c in chans(s)) / TOT0))
P = {'log, tickets, notes, warehouse only': set(ALL) - {'E', 'C'},
     'plus every mail': {'K3', 'K4', 'K5', 'K2', 'F', 'S'},
     'plus thread replies': {'K3', 'K4', 'K5'},
     'plus inline PR comments': {'K4', 'K5'},
     'plus Brian DM': {'K5'},
     'perfect': set()}
print('Whole policies:')
for k, v in P.items():
    print('  %-42s %.1f%%' % (k, 100 * score(v)))
print('Single misses:', {c: round(100 * score({c}), 1) for c in ALL})


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


def run(rates, rho, pad=0, base=.05, T=12000, seed=7):
    rnd = random.Random(seed)
    o = []
    sd_ = pa = al = a70 = b1 = b2 = 0
    for _ in range(T):
        sc = []
        fs = []
        for r in range(6):
            z = rnd.gauss(0, 1)
            m = set()
            for c, p in rates.items():
                if rnd.random() < 1 / (1 + math.exp(-(math.log(p / (1 - p)) - rho * z))):
                    m.add(c)
            if r == 0:
                nb = sum(c in m for c in BLOCKS)
                b1 += nb >= 1
                b2 += nb >= 2
            ex = {s['id'] for s in S if not chans(s) and rnd.random() < base}
            sc.append(score(m, frozenset(ex), pad))
            fs.append(frozenset(s['id'] for s in S if (chans(s) & m) or s['id'] in ex))
        av = st.mean(sc)
        sd = st.pstdev(sc)
        n, k, big = patterns(fs)
        full = sum(1 for f in fs if not f)
        o.append(av)
        g = .1 <= sd <= .3
        h = n > 0 and k >= 2 and big <= n / 2
        sd_ += g
        pa += h
        a70 += av < .70
        al += g and h and av < .85 and full < 5
    return st.mean(o), a70 / T, sd_ / T, pa / T, al / T, b1 / T, b2 / T


R = {'rev5 find odds': dict(K1=.60, K3=.55, K4=.55, K5=.60, K2=.20, F=.30, S=.20, D=.10, E=.05, C=.10),
     'rev5 discounted x0.7': dict(K1=.42, K3=.385, K4=.385, K5=.42, K2=.14, F=.21, S=.14, D=.07, E=.04, C=.07),
     'rev5 strong Opus x0.4': dict(K1=.24, K3=.22, K4=.22, K5=.24, K2=.08, F=.12, S=.08, D=.04, E=.02, C=.04),
     'rev4 prior': dict(K1=.50, K3=.65, K4=.30, K5=.35, K2=.20, F=.30, S=.20, D=.10, E=.05, C=.10),
     'rev4 K3 not a wall': dict(K1=.50, K3=.30, K4=.30, K5=.35, K2=.20, F=.30, S=.20, D=.10, E=.05, C=.10),
     'rev4 strong Opus': dict(K1=.25, K3=.35, K4=.15, K5=.15, K2=.10, F=.15, S=.10, D=.05, E=.03, C=.05),
     'author prior': dict(K1=.50, K3=.45, K4=.35, K5=.40, K2=.25, F=.30, S=.25, D=.10, E=.05, C=.10),
     'measured carriers': dict(K1=.57, K3=.70, K4=.17, K5=.44, K2=.22, F=.17, S=.22, D=.05, E=.02, C=.10),
     'reviewer judgement': dict(K1=.40, K3=.30, K4=.25, K5=.30, K2=.20, F=.25, S=.20, D=.05, E=.05, C=.10),
     'strong Opus': dict(K1=.20, K3=.15, K4=.12, K5=.15, K2=.10, F=.12, S=.10, D=.03, E=.03, C=.05)}
print('Six-run Monte Carlo, rho .6 (UNCALIBRATED; b1/b2 = one run lands at least 1 / 2 reversal blocks):')
print('%-20s %4s %6s %5s %6s %6s %6s %5s %5s' % ('rates', 'pad', 'E[avg]', 'P<70', 'P(SD)', 'P(pat)', 'P(all)', 'b1', 'b2'))
for k, v in R.items():
    for pad in (0, 40):
        r = run(v, .6, pad)
        print('%-20s %4d %5.1f%% %4.0f%% %5.0f%% %5.0f%% %5.0f%% %4.0f%% %4.0f%%' % (k, pad, r[0] * 100, r[1] * 100, r[2] * 100, r[3] * 100, r[4] * 100, r[5] * 100, r[6] * 100))
