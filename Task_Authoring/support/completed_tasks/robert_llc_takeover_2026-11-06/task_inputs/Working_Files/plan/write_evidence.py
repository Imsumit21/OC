#!/usr/bin/env python3
"""Write/refresh Working_Files/00_V3_Authoring_Evidence.json: the scenario role review bound to the current
01_Scenario_Design.md digest (stage_gate.digest_text: gate lines ignored). Keeps any other stage's entries."""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))
h = subprocess.run(["python3", "Task_Authoring/tools/stage_gate.py", "--artifact-hash",
                    "Task_Authoring/task_inputs/Working_Files/01_Scenario_Design.md"], cwd=WS, capture_output=True, text=True,
                   env=dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")).stdout.strip().splitlines()[-1]
path = os.path.join(WF, "00_V3_Authoring_Evidence.json")
data = json.load(open(path)) if os.path.exists(path) else {}
data.update({"spec_version": "V3", "context_hash": CTX["context_hash"]})
data.setdefault("role_reviews", {})["scenario"] = {
    "artifact": "01_Scenario_Design.md", "artifact_hash": h,
    "reviewer": "Claude (Opus 5.5), self-review plus one independent fresh-agent design review (REDTEAM_* unset; see design §13)",
    "persona_role": CTX["persona_role"],
    "rationale": ("Robert is a co-founder (roster: Co-Founder & Creative Director) and one of the three founders running the wind-down in #winddown "
                  "(C0ADGSZKR3R members; his Feb 11 Soundly cancellation C0ADGSZKR3R/1770839322.836779 and Figma note C0ADGSZKR3R/1770859313.592649). "
                  "Combo Fighter is his game: he wants it self-sustaining (C07C2866011/1770084297.911029) and says the missing piece is a budget "
                  "(D07H86MV4DN/1770873696.684969). Leonard proposed buying HG's assets under an LLC the founders own (C07C2866011/1770612982.268919) and "
                  "that the LLC can buy what Sunset's sale leaves (C07C2866011/1770850800.723979). Deciding which items the founders' LLC takes over, "
                  "the three-month budget and each founder's share is ordinary co-founder executive work inside Finance (budget, forecast, founder "
                  "funding) at the Feb 14, 2026 freeze, with the wind-down acknowledged. His Drive root d_9f7ba94f7526d54d8482ba is owned and "
                  "writable; Linear, Sheets, Drive and Slack writes are proven as Robert by the stored wind-down baselines."),
    "source_ids": ["C0ADGSZKR3R/1770839322.836779", "C0ADGSZKR3R/1770859313.592649", "C07C2866011/1770084297.911029",
                   "D07H86MV4DN/1770873696.684969", "C07C2866011/1770612982.268919", "C07C2866011/1770850800.723979",
                   "d_9f7ba94f7526d54d8482ba", "D04UP2L3E3S"],
}
json.dump(data, open(path, "w"), indent=1)
open(path, "a").write("\n")
print("wrote", path, "artifact_hash", h)
