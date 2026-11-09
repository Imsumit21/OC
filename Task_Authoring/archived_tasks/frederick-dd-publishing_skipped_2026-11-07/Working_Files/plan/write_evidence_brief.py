#!/usr/bin/env python3
"""Write the prompt-writing outcome review into Working_Files/00_V3_Authoring_Evidence.json, bound to the brief's artifact hash."""
import json, os, subprocess, sys
sys.dont_write_bytecode = True
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(WF, "solver"))
import solver as SV
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))
TR = json.load(open(os.path.join(WF, "solver", "truth.json")))
AGG = SV.aggregates(TR); T = AGG["totals"]
h = subprocess.run(["python3", "-B", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", "Task_Authoring/task_inputs/Working_Files/04_Prompt_Writing_Brief.md"], cwd=WS, capture_output=True, text=True).stdout.strip()
p = os.path.join(WF, "00_V3_Authoring_Evidence.json")
d = json.load(open(p))
d["spec_version"] = "V3"; d["context_hash"] = CTX["context_hash"]
live = sorted((v for v in TR.values() if v["Status"] == "Live"), key=lambda v: -v["12-month value"])
acc = [
 "D1: one native Google Sheet named DD publishing model whose final parent is d_6fc54be60d1377e340a5b5 (created there or moved there), tabs Publishers and Summary with the rule doc's columns",
 "D1 rows: exactly these 26 publishers: " + ", ".join(k for k, v in TR.items() if v["Status"]) + "; record spelling or obvious short forms; Homa, NCsoft, Tilting Point, Tamatem and the Sep 24 lead stay out",
 "D1 Live figures: " + "; ".join(f"{v['Publisher']} advance {v['Advance']}, installs {v['Monthly installs']}, value {v['12-month value']}, Q4 {v['Q4 cash']}" for v in live) + "; figures blank on other rows",
 "D1 statuses: " + "; ".join(f"{s}: {n}" for s, n in AGG["classes"].items()),
 f"D1 Summary: Keep value {T['keep_value']} (to the dollar accepted), First pick {T['first_pick']}, Banked so far 0",
 "D2: six checklists on the DD publishing card, one per status, 26 items, wording carrying the publisher's name",
 f"D3: {T['cards_new']} new cards named F/up with plus the publisher's name on BD Follow Up; a status comment on F/up with Marek and F/up with Lena",
 f"D4: {T['nudges']} unsent Gmail drafts, one per No reply publisher, as a new draft or a draft reply; Summit's to partnerships@summitmobile.io",
 "D5: three unsent Gmail drafts to Paola, Diego and Sofia carrying $0.50 D30 ARPI, as a new draft or a draft reply",
 f"D6: {T['contacts_added']} contacts with the company in the job field; Anika Rao and Lena Fischer skipped",
 "D7: seven events on Frederick's calendar, one per Live offer on its response date, named for the publisher; time of day is free",
 "D8: reply or reply-all on the hub thread with Copperleaf Games, $67,200, $32,000 and $0 banked; extra lines allowed",
]
alt = [
 "Oakline Q4 cash $20,000 (resend not counted): rejected; Arthur's reply says it'll land in October and the rule doc counts what lands in Q4",
 "Term-sheet numbers for Tallwater and Sunfold because changes came by phone: rejected; 'Use the latest terms we have from them, wherever they are, calls included'",
 "Kitebridge left out as the Sep 24 lead: rejected; the hub says he never made it onto the sheet",
 "Five organic notes, adding Orchard Lane and Summit: rejected; the standing line needs an offer in",
 "No organic notes because the calls already happened: rejected; the line says before we go any further",
 "Three reminders, one per date: rejected; the rule doc says one for each Live offer",
 "Notes in a Doc or Slack: rejected; the standing line says Gmail drafts",
 "No notes, reading the doc line as a limit on content: rejected in rev2; the rule doc says the notes aren't done and to do them as part of this",
 "A Q4 total across offers in the reply: rejected; rights go to one publisher and the hub asks what 'it' brings in",
 "Draft reply on the old thread versus a new draft: both accepted; no record says which",
]
d.setdefault("outcome_reviews", {})["prompt-writing"] = {
 "artifact": "04_Prompt_Writing_Brief.md", "artifact_hash": h,
 "reviewer": "Claude (Opus 5.5), self-review plus three blind passes by fresh agents that saw no design, solver or manifest (plan/sweep/); no independent human reviewer (REDTEAM_* unset)",
 "rationale": "Brief §4b gives one value or a closed accepted set for every graded field of rev2. The first blind solve matched the solver on every value; its five forks were settled in records, the second pass found none, and the one fork rev1 /prompt raised (whether the notes are owed) is settled in the rule doc's last line. The one open choice is the drafts' thread form, accepted both ways.",
 "accepted_outcomes": acc, "alternatives_considered": alt}
json.dump(d, open(p, "w"), indent=1, ensure_ascii=False)
print("outcome review bound to", h)
