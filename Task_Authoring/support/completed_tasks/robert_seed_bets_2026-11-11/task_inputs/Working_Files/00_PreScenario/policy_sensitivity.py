#!/usr/bin/env python3
"""Sensitivity (UNCALIBRATED): the platform has asked for one row per write (learnings; rubric-platform-vs-local-rules memory).
Re-scores the sketch with every payee issue close as its own weight-1 row instead of 5 samples plus a volume row, and with an
optional comment on every issue as its own weight-1 row."""
import importlib.util, os
H = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("pm", os.path.join(H, "policy_model.py")); pm = importlib.util.module_from_spec(spec); spec.loader.exec_module(pm)
base = list(pm.SLOTS)
def apply(extra):
    pm.SLOTS = base + [(f"E{i}", 1, []) for i in range(extra)]
    pm.TOTAL = sum(w for _, w, _ in pm.SLOTS)
for label, extra in [("sketch: closes sampled (5 + volume)", 0), ("one row per close (22 rows)", 16), ("one row per close and per comment (44 rows)", 38)]:
    apply(extra)
    print(f"\n{label}: total weight {pm.TOTAL}, flippable {sum(w for _, w, m in pm.SLOTS if m) / pm.TOTAL:.1%}")
    print("  scale  rho   E[avg]  P(<90)  P(SD)  P(all gates)")
    for sc, rho in [(1.0, .35), (.7, .35), (.5, .35), (.4, .35), (.3, .35)]:
        r = pm.sim(sc, rho, n=8000)
        print(f"  {sc:4.2f}  {rho:4.2f}  {r['E']:6.1%}  {r['cap']:6.2f}  {r['sd']:5.2f}  {r['all']:6.2f}")
