#!/usr/bin/env python3
"""Replaces the pasted design-tool blocks in 01_Scenario_Design.md's Self-review with the current outputs in
research/tool_out/ (hardness_gate.txt, surface.txt, v2.txt, liveness.txt). Run after re-running those tools."""
import re
from pathlib import Path

WF = Path(__file__).resolve().parents[1]
OUT = WF / "research" / "tool_out"
p = WF / "01_Scenario_Design.md"
t = p.read_text()
for name, head in [("hardness_gate.txt", "HARDNESS GATE (extreme (design))"), ("surface.txt", "GRADABLE SURFACE ("),
                   ("v2.txt", "ADVISORY · Hardness v2"), ("liveness.txt", "TRAP LIVENESS")]:
    new = (OUT / name).read_text().rstrip("\n")
    rx = re.compile(r"```\n" + re.escape(head) + r".*?\n```", re.S)
    assert rx.search(t), name
    t = rx.sub(lambda m: "```\n" + new + "\n```", t, count=1)
p.write_text(t)
print("design pastes refreshed")
