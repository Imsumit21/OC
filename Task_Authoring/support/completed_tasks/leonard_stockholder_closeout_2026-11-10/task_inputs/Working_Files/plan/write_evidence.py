#!/usr/bin/env python3
"""Writes 00_V3_Authoring_Evidence.json with the scenario role review, bound to the current design digest."""
import json, os, subprocess
H = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(H); TASK = os.path.dirname(WF); ROOT = os.path.abspath(os.path.join(TASK, "..", ".."))
PY = os.path.expanduser("~/.local/bin/python3.12")
ctx = json.load(open(os.path.join(WF, "00_Task_Context.json")))
art = "Task_Authoring/task_inputs/Working_Files/01_Scenario_Design.md"
r = subprocess.run([PY, "-B", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", art], cwd=ROOT, capture_output=True, text=True)
h = r.stdout.strip().split()[-1] if r.stdout.strip() else ""
p = os.path.join(WF, "00_V3_Authoring_Evidence.json")
e = json.load(open(p)) if os.path.exists(p) else {"spec_version": "V3", "role_reviews": {}, "outcome_reviews": {}, "rubric_hash": "", "prompt_hash": "", "rubric_rows": []}
e["context_hash"] = ctx["context_hash"]
e["role_reviews"]["scenario"] = {
 "artifact": "01_Scenario_Design.md", "artifact_hash": h,
 "reviewer": "Claude (Opus 5.5), self-review plus four cold independent fresh-agent reviews (fork, coherence, run simulation, delta); REDTEAM_* unset, see design section 13",
 "persona_role": ctx["persona_role"],
 "rationale": ("Leonard Hayes is a co-founder (roster: Co-founder & Creative Director) and the company's primary operator: he owns the financial model and runway narrative per Persona_Briefs, signs the financing and Sunset documents, "
               "and runs the holder relationships himself. The work is his by his own words: he promised to personally reach out to every angel investor (D04UC0UEN2V/1770665186.368229), drafted the investor email (C0ADGSZKR3R/1770664700.848759), "
               "listed the outreach as his next task (C0ADGSZKR3R/1770934638.035469), ran the Carta terminations (C0ADGSZKR3R/1770935621.095649) and answered KPMG for Griffin in prior years (leonard.hayes@harmonygames.co/1817557789846606177). "
               "A founder closing out his stockholders, with the cap table and audit confirmation that requires, is plausible for this role at the freeze. Finance competency: cap table and investor reporting; competency need not match the title."),
 "source_ids": ["D04UC0UEN2V/1770665186.368229", "C0ADGSZKR3R/1770664700.848759", "C0ADGSZKR3R/1770934638.035469", "C0ADGSZKR3R/1770935621.095649", "leonard.hayes@harmonygames.co/1817557789846606177", "f_31115ddb6ed866f2b10d60"],
}
json.dump(e, open(p, "w"), indent=1, ensure_ascii=False)
print("evidence written", h)
