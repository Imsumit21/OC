#!/usr/bin/env python3
"""Pre-scenario policy model v2 (UNCALIBRATED). Storyline A sketch surface (whole-canvas carry-over into Linear).
Scores whole policies, single misses and a six-run Monte Carlo of the requester gates (avg < 80 %, every run > 130 counted
calls) and the other gates (< 5 full passes, population SD 0.10-0.30, >= 2 failure patterns with the largest <= 50 %). Adapted from Samuel's model; the engine is
unchanged, the surface, policies and rates are this task's. Design aid only: landing rates are not measured rates."""
import itertools, json, random, statistics, os
from statistics import NormalDist
HERE = os.path.dirname(os.path.abspath(__file__))
SURF = json.load(open(os.path.join(HERE, "sketch_surface.json")))["slots"]
SLOTS = [(s["id"], s["weight"], s["mechanisms"]) for s in SURF]
TOTAL = sum(w for _, w, _ in SLOTS)
MECHS = ["INLINE", "REPLY", "BACK", "FOLLOW", "GONE", "LINE", "FILT", "ALIAS"]
# Rates come from carriers measured on the completed tasks: inline PR comments read 1-4 of 20 (Douglas); a reply under an
# unrelated root caught 2 of 8 then 3 of 6 (bridge); a 1:1 DM about 3 of 6 (bridge); a rule off the named card, about half;
# a done claim against a stated rule is usually caught (bridge Paul); judgement joins rarely land (Julia).
P = {"INLINE": 0.85, "REPLY": 0.60, "BACK": 0.50, "FOLLOW": 0.50, "GONE": 0.35, "LINE": 0.30, "FILT": 0.30, "ALIAS": 0.20}
# Ledger view: Opus 5.5 family means where a family has records (done_gap .50, superseding .17, exact_predicate .33,
# scope_alias .20); house_rule has no records, so it keeps the design rate.
LEDGER = {"INLINE": 0.50, "REPLY": 0.17, "BACK": 0.17, "FOLLOW": 0.50, "GONE": 0.35, "LINE": 0.50, "FILT": 0.33, "ALIAS": 0.20}
# Stored reads per run on ticket and list tasks (bridge, q4, llc); the call model resamples them.
READS = [87, 95, 72, 88, 54, 78, 115, 95, 119, 95, 61, 112, 71, 76, 77, 69, 69, 81]
EXTRA = 0  # always-pass weight added by /rubric per-target rows (see the inflation view)
CAP, FLOOR, BASE_SLIP = 0.80, 130, 0.03
score = lambda landed, slips=frozenset(), extra=0: 1 - sum(w for sid, w, m in SLOTS if any(x in landed for x in m) or sid in slips) / (TOTAL + extra)
failed = lambda landed, slips=frozenset(): frozenset(sid for sid, w, m in SLOTS if any(x in landed for x in m) or sid in slips)
def patterns(fsets):
    fs = [f for f in fsets if f]
    if not fs: return 0, 0.0
    parent = list(range(len(fs)))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]; i = parent[i]
        return i
    for i, j in itertools.combinations(range(len(fs)), 2):
        if len(fs[i] ^ fs[j]) <= 1: parent[find(i)] = find(j)
    g = {}
    for i in range(len(fs)): g.setdefault(find(i), []).append(i)
    return len(g), max(len(x) for x in g.values()) / len(fs)
def calls(landed, rnd):
    """Counted calls in one run: per-entry writes with no batch form, plus a resampled stored read count."""
    w = 63 + (0 if "FILT" in landed else 7) + rnd.randint(12, 16) + 28 + 5
    return w + rnd.choice(READS) - rnd.randint(0, 3)
def sim(rates, scale=1.0, rho=0.35, n=20000, seed=11, extra=0, cap_scale=None):
    N, rnd = NormalDist(), random.Random(seed)
    r = {"avg": [], "cap": 0, "sd": 0, "full": 0, "pat": 0, "all": 0, "min": [], "floor": 0}
    for _ in range(n):
        runs, fs, cc = [], [], []
        for _ in range(6):
            z = rnd.gauss(0, 1)
            landed = {m for m in MECHS if N.cdf((rho ** .5) * z + ((1 - rho) ** .5) * rnd.gauss(0, 1)) < rates[m] * scale}
            slips = {sid for sid, w, mm in SLOTS if not mm and rnd.random() < BASE_SLIP}
            runs.append(score(landed, slips, extra)); fs.append(failed(landed, slips)); cc.append(calls(landed, rnd))
        a, sd = statistics.mean(runs), statistics.pstdev(runs)
        full = sum(1 for x in runs if x >= .9999); npat, big = patterns(fs)
        g = [a < CAP, .10 <= sd <= .30, full < 5, npat >= 2 and big <= .5, min(cc) > FLOOR]
        r["avg"].append(a); r["min"].append(min(cc))
        for k, ok in zip(["cap", "sd", "full", "pat", "floor"], g): r[k] += ok
        r["all"] += all(g)
    return {"E": statistics.mean(r["avg"]), "M": statistics.mean(r["min"]), **{k: r[k] / n for k in ["cap", "sd", "full", "pat", "floor", "all"]}}
def main():
    fl = sum(w for _, w, m in SLOTS if m)
    print(f"UNCALIBRATED · surface: {len(SLOTS)} slots, total weight {TOTAL}, mechanism-flippable {fl} ({fl / TOTAL:.1%})")
    print("\nWhole policies")
    pol = {"Perfect": set(),
     "Canvas ticks at face value, nothing else": set(MECHS),
     "Reads PR reviews but never inline comments, otherwise perfect": {"INLINE"},
     "Thorough, never opens threads under unrelated posts or other DMs": {"INLINE", "REPLY", "BACK"},
     "Stays inside the canvas, otherwise thorough": {"FILT", "REPLY", "BACK"},
     "Reads everything, never asks what the live build contains": {"GONE", "LINE"},
     "Right calls, misses the note rule": {"FOLLOW"}}
    for k, v in pol.items(): print(f"  {score(v):6.1%}  {k}  [lands: {', '.join(sorted(v)) or '-'}]")
    print("\nSingle misses")
    for m in MECHS: print(f"  {m:6} {score({m}):6.1%}")
    print("\nPairs at or above the 80 % line:", [f"{a}+{b}" for a, b in itertools.combinations(MECHS, 2) if score({a, b}) >= CAP] or "none")
    pf = 1.0
    for m in MECHS: pf *= 1 - P[m]
    print(f"\nP(one run catches every trap) ~ {pf:.3f} (independence); expected landings per run at design rates {sum(P.values()):.2f}")
    print("Triples at or above the 80 % line:", [f"{a}+{b}+{c}" for a, b, c in itertools.combinations(MECHS, 3) if score({a, b, c}) >= CAP] or "none")
    print("\nOne pre-check run under the narrow-miss rule (one cause under 15 % caps /hardness at 2), independence")
    for sc in (1.0, .7, .5):
        ok = 0.0
        for k in range(len(MECHS) + 1):
            for c in itertools.combinations(MECHS, k):
                pr = 1.0
                for m in MECHS: pr *= (P[m] * sc) if m in c else 1 - P[m] * sc
                if k >= 2 or (k == 1 and 1 - score(set(c)) >= .15): ok += pr
        print(f"  scale {sc:4.2f}: P(two or more causes, or one cause losing 15 % or more) = {ok:.2f}")
    H = "  scale  rho   mean-land  E[avg]  P(<80)  P(SD)  P(<5 full)  P(pat)  P(>130 all six)  mean-min-calls  P(all)"
    row = lambda sc, rho, rates, r: f"  {sc:4.2f}  {rho:4.2f}  {sum(rates.values()) / 8 * sc:8.2f}  {r['E']:6.1%}  {r['cap']:6.2f}  {r['sd']:5.2f}  {r['full']:9.2f}  {r['pat']:6.2f}  {r['floor']:14.2f}  {r['M']:13.0f}  {r['all']:6.2f}"
    print("\nSix-run Monte Carlo, carrier rates (scale x rho)\n" + H)
    for sc, rho in [(1, .3), (1, .6), (.8, .35), (.7, .35), (.6, .35), (.6, .6), (.5, .35), (.4, .35)]:
        print(row(sc, rho, P, sim(P, sc, rho)))
    print("\nLedger view (scale x rho)")
    for sc, rho in [(1, .35), (.7, .35)]:
        print(row(sc, rho, LEDGER, sim(LEDGER, sc, rho)))
    print("\nRubric inflation view: /rubric adds always-pass per-target rows (carrier rates, rho .35)")
    for ex in (30, 60, 100):
        for sc in (1, .7):
            print(f"  +{ex:3} weight" + row(sc, .35, P, sim(P, sc, .35, extra=ex)))
if __name__ == "__main__": main()
