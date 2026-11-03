#!/usr/bin/env python3
"""Assemble 01_Scenario_Design.md from design_body.md and the pasted tool outputs (verbatim)."""
import json
from pathlib import Path
P = Path(__file__).resolve().parent; WF = P.parent
m = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())
budget = "\n".join(f"| {b['phase']} | {b['service']} | {b['calls']} | {b['reason']} |" for b in m["call_budget"])
ent = (P / "entity_collisions.txt").read_text().rstrip() + "\n\n" + (P / "entity_resolve.txt").read_text().rstrip()
body = (P / "design_body.md").read_text()
for k, v in {"{{REACH}}": (P / "reach.txt").read_text().rstrip(), "{{ENTITY}}": ent,
             "{{POLICY}}": (P / "policy_scores_output.txt").read_text().rstrip(), "{{BUDGET}}": budget,
             "{{HGATE}}": (P / "hardness_gate_design.txt").read_text().rstrip(),
             "{{V2}}": (P / "v2_check.txt").read_text().rstrip(), "{{LIVE}}": (P / "liveness.txt").read_text().rstrip()}.items():
    assert k in body, k
    body = body.replace(k, v)
(WF / "01_Scenario_Design.md").write_text(body)
print("01_Scenario_Design.md", len(body), "chars")
