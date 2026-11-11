#!/usr/bin/env python3
"""UNCALIBRATED sensitivity: the platform has asked for a row per write. Adds the 22 issue closes as weight-1 rows that pass."""
import importlib.util, os
H = os.path.dirname(os.path.abspath(__file__))
sp = importlib.util.spec_from_file_location("pm", os.path.join(H, "policy_scores.py")); pm = importlib.util.module_from_spec(sp); sp.loader.exec_module(pm)
base = list(pm.SLOTS)
for label, extra in [("surface as written", 0), ("plus a row per issue close (22)", 22), ("plus a row per close and 18 more payee cell rows", 40)]:
    pm.SLOTS = base + [(f"E{i}", 1, []) for i in range(extra)]; pm.TOTAL = sum(w for _, w, _ in pm.SLOTS)
    print(f"\n{label}: total weight {pm.TOTAL}, flippable {sum(w for _, w, m in pm.SLOTS if m) / pm.TOTAL:.1%}")
    print("  scale  rho   E[avg]  P(<90)  P(SD)  P(all gates)")
    for sc, rho in [(1.0, .35), (.7, .35), (.7, .10), (.5, .35), (.5, .10), (.3, .35)]:
        r = pm.sim(sc, rho, n=6000)
        print(f"  {sc:4.2f}  {rho:4.2f}  {r['E']:6.1%}  {r['cap']:6.2f}  {r['sd']:5.2f}  {r['all']:6.2f}")
