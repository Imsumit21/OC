#!/usr/bin/env python3
"""Pre-scenario policy model (UNCALIBRATED). Storyline A sketch surface (Queue Manager roll-out stock-take).
Scores whole policies, single misses and a six-run Monte Carlo of the Hard gates: corrected average < 70 %, < 5 full
passes, population SD 0.10-0.30, >= 2 failure patterns with the largest <= 50 %, >= 100 counted calls. Engine reused from
the Owen pre-scenario model; the surface, policies and rates are this task's. Design aid only: landing rates are
placement judgements from stored runs of other tasks, not measured rates for this one."""
import itertools, json, random, statistics, os
from statistics import NormalDist
HERE = os.path.dirname(os.path.abspath(__file__))
SURF = json.load(open(os.path.join(HERE, "sketch_surface.json")))["slots"]
SLOTS = [(s["id"], s["weight"], s["mechanisms"]) for s in SURF]
TOTAL = sum(w for _, w, _ in SLOTS)
MECHS = ["BRANCH", "REOPEN", "INLINE", "FILT", "MAIL", "ALIAS", "ELSE", "DATE"]
# P = chance one run MISSES the deciding record (the trap lands). Tiers on purpose (rule 5):
#  near-certain: inline review comments 0/12 reads (Owen), 0/6 (Douglas); mail 0/8 (Owen), most runs (Vincent)
#                a 1:1 chat the run has no reason to open, in Spanish (Owen: Marcus DM 0/12; Vincent: Turkish DMs mostly missed)
#  lottery:      branch-vs-main build check; a reply under an unrelated root (bridge 3/6, 6/8; Owen 1/6); calendar read 3/7 (q4)
#  usually caught: an unlinked Linear ticket with the feature word in its title; an alias a search resolves
P = {"INLINE": 0.85, "MAIL": 0.80, "BRANCH": 0.50, "REOPEN": 0.55, "ELSE": 0.70, "DATE": 0.40, "ALIAS": 0.35, "FILT": 0.25}
LEDGER = {"INLINE": 0.50, "BRANCH": 0.50, "REOPEN": 0.17, "ELSE": 0.20, "DATE": 0.67, "ALIAS": 0.20, "FILT": 0.33, "MAIL": 0.33}
# Bimodal view: stored batches show carriers are mostly read by all runs or by none. Each lottery carrier resolves per
# batch to 0.9 or 0.1 with the design rate as the mixing weight.
READS = [87, 95, 72, 88, 54, 78, 115, 95, 119, 95, 61, 112, 71, 76, 77, 69, 69, 81]
CAP, FLOOR, BASE_SLIP = 0.70, 100, 0.03
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
    """Counted calls in one run: per-entry writes with no batch form (sub-issues, moves under the epic, notes, doc,
    reply) plus a resampled stored read count. A run that misses a report writes less."""
    w = 9 + rnd.randint(-1, 2) + 14 + 12 + 4 - sum(1 for m in ("MAIL", "REOPEN", "INLINE") if m in landed)
    return w + rnd.choice(READS) - rnd.randint(0, 3)
def sim(rates, scale=1.0, rho=0.35, n=6000, seed=11, extra=0, bimodal=False):
    N, rnd = NormalDist(), random.Random(seed)
    r = {"avg": [], "cap": 0, "sd": 0, "full": 0, "pat": 0, "all": 0, "min": [], "floor": 0, "sds": []}
    for _ in range(n):
        rr = {m: min(1, rates[m] * scale) for m in MECHS}
        if bimodal:
            rr = {m: (p if p >= 0.75 else (0.9 if rnd.random() < p else 0.1)) for m, p in rr.items()}
        runs, fs, cc = [], [], []
        for _ in range(6):
            z = rnd.gauss(0, 1)
            landed = {m for m in MECHS if N.cdf((rho ** .5) * z + ((1 - rho) ** .5) * rnd.gauss(0, 1)) < rr[m]}
            slips = {sid for sid, w, mm in SLOTS if not mm and rnd.random() < BASE_SLIP}
            runs.append(score(landed, slips, extra)); fs.append(failed(landed, slips)); cc.append(calls(landed, rnd))
        a, sd = statistics.mean(runs), statistics.pstdev(runs)
        full = sum(1 for x in runs if x >= .9999); npat, big = patterns(fs)
        golden = [c for x, c in zip(runs, cc) if x >= .9999]
        horizon = (min(golden) if golden else statistics.mean(cc)) >= FLOOR
        g = [a < CAP, .10 <= sd <= .30, full < 5, npat >= 2 and big <= .5, horizon]
        r["avg"].append(a); r["min"].append(min(cc)); r["sds"].append(sd)
        for k, ok in zip(["cap", "sd", "full", "pat", "floor"], g): r[k] += ok
        r["all"] += all(g)
    return {"E": statistics.mean(r["avg"]), "M": statistics.mean(r["min"]), "S": statistics.median(r["sds"]), **{k: r[k] / n for k in ["cap", "sd", "full", "pat", "floor", "all"]}}
def main():
    fl = sum(w for _, w, m in SLOTS if m)
    print(f"UNCALIBRATED · surface: {len(SLOTS)} slots, total weight {TOTAL}, mechanism-flippable {fl} ({fl / TOTAL:.1%})")
    share = {m: sum(w for _, w, mm in SLOTS if m in mm) / TOTAL for m in MECHS}
    print("Share of weight each channel can flip:", ", ".join(f"{m} {share[m]:.1%}" for m in MECHS), "· largest", f"{max(share.values()):.1%}")
    print("\nWhole policies")
    pol = {"Perfect": set(),
     "Takes every 'done' and 'ok' at face value, stays in the QA chat and the epic": set(MECHS),
     "Reads everything it is pointed at, never checks which build QA looked at": {"BRANCH"},
     "Checks builds, never reads inline review comments or mail": {"INLINE", "MAIL"},
     "Thorough in Slack and Linear, never opens mail, inline comments or threads under other posts": {"INLINE", "MAIL", "REOPEN"},
     "Never opens mail, inline comments or the Spanish chat, otherwise perfect": {"INLINE", "MAIL", "ELSE"},
     "English keyword searches only (misses the Spanish chat), no calendar": {"ELSE", "DATE"},
     "Finds every record, files a new sub-issue per item (no reuse)": {"ALIAS"}}
    for k, v in pol.items(): print(f"  {score(v):6.1%}  {k}  [lands: {', '.join(sorted(v)) or '-'}]")
    print("\nSingle misses")
    for m in MECHS: print(f"  {m:6} {score({m}):6.1%}")
    print("\nPairs at or above the 70 % line:", len([1 for a, b in itertools.combinations(MECHS, 2) if score({a, b}) >= CAP]), "of 28;",
          "triples at or above it:", len([1 for c in itertools.combinations(MECHS, 3) if score(set(c)) >= CAP]), "of 56")
    print("Near-certain trio alone (INLINE+MAIL+ELSE):", f"{score({'INLINE','MAIL','ELSE'}):.1%}")
    pf = 1.0
    for m in MECHS: pf *= 1 - P[m]
    print(f"P(one run catches every trap) ~ {pf:.4f} (independence); expected landings per run {sum(P.values()):.2f}")
    print("\nOne pre-check run: P(two or more causes, or one cause losing 30 % or more), independence")
    for sc in (1.0, .7, .5):
        ok = 0.0
        for k in range(len(MECHS) + 1):
            for c in itertools.combinations(MECHS, k):
                pr = 1.0
                for m in MECHS: pr *= (P[m] * sc) if m in c else 1 - P[m] * sc
                if k >= 2 or (k == 1 and 1 - score(set(c)) >= .30): ok += pr
        print(f"  scale {sc:4.2f}: {ok:.2f}")
    H = "  view                 scale  rho   E[avg]  P(<70)  P(SD)  med-SD  P(<5 full)  P(pat)  P(>=100)  P(all)"
    row = lambda name, sc, rho, r: f"  {name:20} {sc:4.2f}  {rho:4.2f}  {r['E']:6.1%}  {r['cap']:6.2f}  {r['sd']:5.2f}  {r['S']:6.3f}  {r['full']:9.2f}  {r['pat']:6.2f}  {r['floor']:8.2f}  {r['all']:6.2f}"
    print("\nSix-run Monte Carlo\n" + H)
    for sc, rho in [(1, .2), (1, .35), (1, .6), (.8, .35), (.7, .35), (.6, .35), (.5, .35)]:
        print(row("placement rates", sc, rho, sim(P, sc, rho)))
    for sc in (1, .7):
        print(row("bimodal carriers", sc, .35, sim(P, sc, .35, bimodal=True)))
    for sc in (1, .7):
        print(row("ledger family means", sc, .35, sim(LEDGER, sc, .35)))
    print("\nRubric inflation: always-pass weight /rubric may add (placement rates, rho .35)")
    for ex in (20, 40, 70):
        for sc in (1, .7):
            print(f"  +{ex:3} weight " + row("", sc, .35, sim(P, sc, .35, extra=ex)))
if __name__ == "__main__": main()
