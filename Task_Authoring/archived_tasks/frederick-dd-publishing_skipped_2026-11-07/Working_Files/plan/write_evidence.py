#!/usr/bin/env python3
"""Write Working_Files/00_V3_Authoring_Evidence.json (scenario role review), bound to the design's artifact hash."""
import json, os, subprocess, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))
h = subprocess.run(["python3", "-B", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", "Task_Authoring/task_inputs/Working_Files/01_Scenario_Design.md"], cwd=WS, capture_output=True, text=True).stdout.strip().split()[-1]
p = os.path.join(WF, "00_V3_Authoring_Evidence.json")
d = json.load(open(p)) if os.path.exists(p) else {"spec_version": "V3", "role_reviews": {}, "outcome_reviews": {}, "rubric_rows": []}
d["spec_version"] = "V3"; d["context_hash"] = CTX["context_hash"]
d.setdefault("role_reviews", {})["scenario"] = {
 "artifact": "01_Scenario_Design.md", "artifact_hash": h,
 "reviewer": "Claude (Opus 5.5), self-review, with one fresh-context agent review recorded in design section 13; dual red team unavailable (REDTEAM_* unset)",
 "persona_role": "Co-founder",
 "rationale": "Frederick Stone is a co-founder (roster) and Commercial Lead (Contacts). Leonard put the Domino Delights publishing-rights question to the founders by name on Aug 25 (C07C2866011/1756140953.197759) and at the Aug 28 sync (f_26e1f9a86761e35049192a). Frederick ran the Appodeal publishing talks (frederick.stone@harmonygames.co/1830012626042968381), was handed the Rayking mail (frederick.stone@harmonygames.co/1842348778705877030) and opened publishing outreach on Sep 24 (D05S58U4SAK/1758736827.548589, f_10dfa1b4236a7c35dcb632). Modelling what each offer brings in, and recommending one to the founders, is ordinary work for a commercial co-founder at a startup with no finance lead: a forecast for a strategic decision, inside Finance.",
 "source_ids": ["C07C2866011/1756140953.197759", "f_26e1f9a86761e35049192a", "frederick.stone@harmonygames.co/1830012626042968381", "D05S58U4SAK/1758736827.548589", "f_10dfa1b4236a7c35dcb632"],
}
json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)
print("evidence bound to", h)
