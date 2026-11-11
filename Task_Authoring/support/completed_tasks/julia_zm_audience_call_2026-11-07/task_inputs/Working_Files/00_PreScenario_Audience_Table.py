#!/usr/bin/env python3
"""Pre-scenario proof that the audience answer flips under every block-miss combination.
Provisional design numbers for seeded sessions, not base facts. No prompt, OE or criterion text.
Rule tested: lead = higher mean star rating over counted sessions, one audience label per session,
minimum 6 sessions per audience, gap under TIE means no clear lead."""
import itertools

TIE = 0.25
MIN_N = 6
# group: (casual ratings, RPG ratings). Stars in half steps; each list is one session per entry.
G = {
    'counted': ([4, 4, 3.5, 4, 3.5, 3.5, 4, 4, 4], [3.5, 3.5, 3, 3.5, 3.5, 3, 3.5, 3.5]),
    'K1 coached gathering': ([], [5, 4, 5, 4.5, 5, 4.5, 5, 4, 5, 4.5, 4.5, 5, 4.5]),
    'K3 Samsung group': ([2, 3, 2, 2, 2.5, 2, 2.5, 3.5, 2, 2.5, 2], []),
    'K4 industry batch': ([], [5, 5, 4, 5, 5, 4.5, 5, 5, 4.5]),
    'K5 store-build miss': ([2, 2.5, 3, 2.5, 2, 2, 2.5, 3.5, 2.5, 2], []),
}
B = [k for k in G if k != 'counted']


def read(keep):
    c = list(G['counted'][0])
    r = list(G['counted'][1])
    for k in keep:
        c += G[k][0]
        r += G[k][1]
    mc = sum(c) / len(c)
    mr = sum(r) / len(r)
    return len(c), mc, len(r), mr, (c + r)


n1, m1, n2, m2, a = read([])
print('Truth: casual n=%d mean %.3f | RPG n=%d mean %.3f | overall n=%d mean %.3f | casual leads by %.3f' % (n1, m1, n2, m2, len(a), sum(a) / len(a), m1 - m2))
assert n1 >= MIN_N and n2 >= MIN_N and m1 - m2 > TIE
print('Session count:', sum(len(v[0]) + len(v[1]) for v in G.values()), '| not counted:', sum(len(G[k][0]) + len(G[k][1]) for k in B))
worst = 9
rows = []
for r in range(1, 5):
    for keep in itertools.combinations(B, r):
        n1, m1, n2, m2, a = read(keep)
        gap = m2 - m1
        worst = min(worst, gap)
        rows.append((gap, keep, m1, m2, sum(a) / len(a)))
ok = sum(g > TIE for g, *_ in rows)
print('Miss combinations:', len(rows), '| RPG wrongly leads by more than tie band in', ok, '| smallest wrong gap %.3f' % worst)
for g, k, c, r_, o in sorted(rows)[:6]:
    print('  wrong gap %.3f casual %.3f RPG %.3f overall %.3f  kept: %s' % (g, c, r_, o, ', '.join(x.split()[0] for x in k)))
print('All 60 kept overall mean %.3f' % (sum(sum(v[0]) + sum(v[1]) for v in G.values()) / sum(len(v[0]) + len(v[1]) for v in G.values())))
