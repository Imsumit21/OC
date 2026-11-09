#!/usr/bin/env python3
"""Write Working_Files/00_V3_Authoring_Evidence.json (scenario role review), bound to the design's artifact hash."""
import json, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))
env = {**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputsK"}
p = subprocess.run(["python3", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", "Task_Authoring/task_inputsK/Working_Files/01_Scenario_Design.md"], cwd=WS, capture_output=True, text=True, env=env)
h = p.stdout.strip().split()[-1]
path = os.path.join(WF, "00_V3_Authoring_Evidence.json")
ev = json.load(open(path)) if os.path.exists(path) else {"spec_version": "V3", "context_hash": CTX["context_hash"], "role_reviews": {}, "outcome_reviews": {}}
ev["context_hash"] = CTX["context_hash"]
ev["role_reviews"]["scenario"] = {
    "artifact": "01_Scenario_Design.md", "artifact_hash": h,
    "reviewer": "Claude (Opus 5.5), self-review, with one fresh-context agent review recorded in design section 13; dual red team unavailable (REDTEAM_* unset)",
    "persona_role": "Game Designer",
    "rationale": ("Samuel Turner is a Game Designer (roster) who built the Zombie Match phone messages himself: Leonard sent him the sheet and said he would start there "
                  "(D06L58XCVKK/1750138057.452159), the roadmap card reads '[Feature] Push Notifications - Samuel + Leonard' (6851a769c65dc0017a227bb7), and he merged the client work in "
                  "harmonygames-Games/match3d#248. He also moved the permission ask with Robert (D06KPMDV2JZ/1752162738.497679) and owns the Rate Us popup (ZOM-397). Deciding what the game says to a "
                  "lapsed player, when, and what reaches them before the beta is ordinary design work in Marketing and GTM (retention and communications) at the Oct 1, 2025 freeze. "
                  "His Drive root d_caafeec2804b3a67ce46aa is owned and writable."),
    "source_ids": ["D06L58XCVKK/1750138057.452159", "6851a769c65dc0017a227bb7", "harmonygames-Games/match3d#248", "D06KPMDV2JZ/1752162738.497679", "ZOM-397", "d_caafeec2804b3a67ce46aa"],
}
json.dump(ev, open(path, "w"), indent=1, ensure_ascii=False)
print("evidence bound to", h)
