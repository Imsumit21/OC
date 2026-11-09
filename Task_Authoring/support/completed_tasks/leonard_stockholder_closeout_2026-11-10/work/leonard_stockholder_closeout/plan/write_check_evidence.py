#!/usr/bin/env python3
"""Record the prompt-check role review and outcome review in 00_V3_Authoring_Evidence.json, bound to 04_Prompt.txt's digest."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
PY = os.path.expanduser("~/.local/bin/python3.12")
h = subprocess.run([PY, "-B", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", "Task_Authoring/task_inputs/04_Prompt.txt"],
                   cwd=WS, capture_output=True, text=True, env=dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")).stdout.strip().splitlines()[-1].split()[-1]
ctx = json.load(open(os.path.join(WF, "00_Task_Context.json")))
p = os.path.join(WF, "00_V3_Authoring_Evidence.json"); d = json.load(open(p))
brief = d["outcome_reviews"]["prompt-writing"]
d.setdefault("role_reviews", {})["prompt-check"] = {
    "artifact": "04_Prompt.txt", "artifact_hash": h,
    "reviewer": "Claude (Opus 5.5), with cold rev2 reviews (Working_Files/research/rev2/) and local blind /prompt rounds (main Eval 1 reviewer and deep-recheck passes P1-P4 by fresh agents; Working_Files/research/prompt_review_rev1/, prompt_review_rev2/)",
    "persona_role": ctx["persona_role"],
    "rationale": ("Leonard Hayes is a co-founder of the company and runs its holder relationships himself: he promised to personally reach out to every angel investor "
                  "(D04UC0UEN2V/1770665186.368229), listed that outreach as his next task after the shutdown (C0ADGSZKR3R/1770934638.035469), ran the Carta terminations "
                  "(C0ADGSZKR3R/1770935621.095649) and has answered KPMG's yearly confirmation for Griffin (leonard.hayes@harmonygames.co/1817557789846606177). A founder asking an "
                  "assistant to close out the company's stockholders, the auditor's confirmation and the investor letter is inside his remit at the freeze."),
    "source_ids": ["D04UC0UEN2V/1770665186.368229", "C0ADGSZKR3R/1770934638.035469", "C0ADGSZKR3R/1770935621.095649", "leonard.hayes@harmonygames.co/1817557789846606177",
                   "C0ADGSZKR3R/1770664700.848759"],
}
d.setdefault("outcome_reviews", {})["prompt-check"] = {
    "artifact": "04_Prompt.txt", "artifact_hash": h,
    "reviewer": brief["reviewer"] + "; prompt checked in Working_Files/04_Prompt_Check.md",
    "rationale": brief["rationale"] + " The prompt adds no rule: it names the holder project, the close-out notes doc, the close-out folder, the investor email draft, KPMG's request and the drafts-only constraint for the holder messages.",
    "accepted_outcomes": brief["accepted_outcomes"],
    "alternatives_considered": brief["alternatives_considered"],
}
json.dump(d, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
print("prompt-check reviews bound to", h)
