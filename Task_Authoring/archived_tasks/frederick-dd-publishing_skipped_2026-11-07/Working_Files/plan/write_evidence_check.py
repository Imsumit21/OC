#!/usr/bin/env python3
"""Write the prompt-check role and outcome reviews into Working_Files/00_V3_Authoring_Evidence.json, bound to 04_Prompt.txt."""
import json, os, subprocess, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))
h = subprocess.run(["python3", "-B", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", "Task_Authoring/task_inputs/04_Prompt.txt"], cwd=WS, capture_output=True, text=True).stdout.strip()
p = os.path.join(WF, "00_V3_Authoring_Evidence.json")
d = json.load(open(p))
d["context_hash"] = CTX["context_hash"]
pw = d["outcome_reviews"]["prompt-writing"]
d["role_reviews"]["prompt-check"] = {
 "artifact": "04_Prompt.txt", "artifact_hash": h, "reviewer": "Claude (Opus 5.5), prompt-check self-review; no independent human reviewer (REDTEAM_* unset)",
 "persona_role": "Co-founder",
 "rationale": "The prompt has Frederick Stone (Co-founder, roster frederick_stone, Executive) hand his assistant the publisher model Leonard's Sep 30 email asks him for. He ran the Appodeal publishing talks, was handed the Rayking mail and opened publisher outreach on Sep 24, and he owns the DD publishing folder. Modelling offers for a founders' decision is ordinary for a commercial co-founder at a startup with no finance lead; the taxonomy lists Co-founder for Finance.",
 "source_ids": ["frederick.stone@harmonygames.co/1844732284109533347", "d_6fc54be60d1377e340a5b5", "frederick.stone@harmonygames.co/1830012626042968381", "frederick.stone@harmonygames.co/1842348778705877030", "D05S58U4SAK/1758736827.548589", "C07C2866011/1756140953.197759"]}
d["outcome_reviews"]["prompt-check"] = {
 "artifact": "04_Prompt.txt", "artifact_hash": h, "reviewer": "Claude (Opus 5.5), prompt-check self-review over brief §4b and three blind passes (plan/sweep/); no independent human reviewer",
 "rationale": "Every deliverable reached from the prompt has one fair outcome or a closed set, settled by a prompt sentence or a persona-visible record: Leonard's email for the model, the card, Contacts and the reply; the rule doc for scope, status, value, Q4 cash and reminders; the card for checklists, follow-ups and nudges; the standing line for the organic notes. The drafts' thread form is accepted both ways.",
 "accepted_outcomes": pw["accepted_outcomes"], "alternatives_considered": pw["alternatives_considered"]}
json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)
print("prompt-check reviews bound to", h)
