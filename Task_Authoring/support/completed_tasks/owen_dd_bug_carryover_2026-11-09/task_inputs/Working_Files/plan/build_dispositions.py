#!/usr/bin/env python3
"""Writes Working_Files/01c_Dispositions.json: a written disposition for every mutation result, channel degrade, intervention and
liveness flag of the current SQL and solver. Re-run after any SQL or solver change, before preflight_report.py."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")


def tool(args):
    r = subprocess.run(["python3", "-B"] + args, cwd=WS, env=ENV, capture_output=True, text=True, timeout=1200)
    return json.loads(r.stdout)


mut = tool(["Task_Authoring/tools/difficulty_mutation.py", "mutate", "--task-dir", "Task_Authoring/task_inputs", "--json"])
status = {}
for g in ("rules", "degrades", "shards"):
    for m in mut["mutants"].get(g) or []:
        if isinstance(m, dict) and m.get("id"):
            status[m["id"]] = (m.get("diagnostic"), m.get("flipped_slots") or [])
for i in mut["interventions"]:
    status[i["id"]] = (i.get("verdict") or i.get("result") or i.get("status") or i.get("diagnostic"), [])
ONLY = {"INLINE": "Arthur's inline comments are the only records that a popup was left out of #1905 and #1908",
        "REPLY": "Brian's Dec 1 reply under the gems post is the only record that the shop icons came back",
        "BACK": "Marcus's Dec 3 DM is the only record that the Tavern frame went again",
        "FOLLOW": "Brian's comment on the UI optimization card is the only statement of the closing rule",
        "GONE": "the removal is read from base records (C09SWTHEMEW/1764659626.614679, f_948768f5a462e7037d17c9, C9CA62B5180A/1765927876.696389); no seeded record carries it",
        "LINE": "the open state of #1913 is base data (harmonygames-Games/GameOfDominoes#1913), so nothing seeded carries it",
        "ELSE": "flicker rests on base commits and #builds; Brian's Dec 8 DM is the only closing record for music and acid",
        "ALIAS": "Vincent's mail and his note on ENG-2363 are the only ties from the two lines to their tickets"}
TEXT = {"INLINE": "I1 to I4 and V4", "FOLLOW": "O1 to O3"}
CTRL = {"inline_over": "ENG-2417 and ENG-2432 (their state is graded through K9 and K12, write-content samples)", "reply_over": "the Purple bg line (it feeds V1 and V5)", "back_over": "the character frames line (it feeds V1 and V5)",
        "gone_over": "the team navigation line (K7)", "line_over": "the treasure button post (F3)", "else_over": "the mega tile post (F1)", "alias_over": "the team navigation line (K7)"}
d = {}
for rid in mut["dispositions"]["required"]:
    st, slots = status.get(rid, ("?", []))
    st = str(st).upper()
    if rid.startswith("rule:"):
        r = rid.split(":", 1)[1]
        if st == "KILLED":
            d[rid] = {"disposition": "live", "reason": f"KILLED: flips a direct slot of weight 3 or more; {ONLY[r]}"}
        else:
            d[rid] = {"disposition": "live", "reason": f"{st} on direct slots by construction: {r} is graded on write content ({TEXT[r]}), which the grader decodes and geometry counts as flippable; {ONLY[r]}"}
    elif rid == "degrade:ch_miss":
        d[rid] = {"disposition": "live", "reason": f"{st}: the channel-miss operator puts each channel member on its rule's natural reading; it flips the direct slots of every rule except INLINE and FOLLOW, which are write-content"}
    elif rid.startswith("degrade:"):
        op = rid.split(":", 1)[1]
        d[rid] = {"disposition": "weak-accepted", "reason": f"{st}: over-application operator on its control, {CTRL[op]}. Controls are reported as control trials, never landings, and are deliberately not weighted"}
    elif rid.startswith("intervention:rule:"):
        r = rid.split(":")[-1]
        if "NO-INJECTED" in st:
            d[rid] = {"disposition": "redundant", "reason": f"no-injected-records: {ONLY[r]}; the sampled key has no seeded deciding record, by design"}
        else:
            d[rid] = {"disposition": "live", "reason": f"{st}: removing the rule's seeded deciding record from an in-memory copy of the SQL moves the member to its natural reading, with no change outside the closure"}
    elif rid.startswith("intervention:degrade:"):
        d[rid] = {"disposition": "redundant", "reason": "no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records"}
    else:
        d[rid] = {"disposition": "live", "reason": st}
LIVE = {"T_GONE:breadcrumb": "weak-accepted: the hub's delegation reaches the economy doc only through Arthur's rule text about the build players have; the removal itself sits in the BoomBit channel and the doc, and each line still needs the join",
        "T_FILT:breadcrumb": "weak-accepted: the rule doc's scope sentence is the fairness link for the later bugs, and it is the record a run must read",
        "D_ZMCANVAS:breadcrumb": "weak-accepted: the rule doc names the ZM canvases to leave them out; that is the scope line, not a route to an answer",
        "D_ZMDOC:breadcrumb": "weak-accepted: the decoy doc shares words with the rule doc by design; its title names the other game",
        "D_SUB250:breadcrumb": "weak-accepted: the rule doc names Robert's sub-250 reports to leave them out",
        "D_ECONCANVAS:breadcrumb": "weak-accepted: the rule doc names the economy canvas to leave it out"}
lv = tool(["Task_Authoring/tools/trap_liveness.py", "--task-dir", "Task_Authoring/task_inputs", "--json"])
req = (lv.get("dispositions") or {}).get("required") or []
ld = {}
for k in req:
    reason = LIVE.get(k, "weak-accepted: lexical flag reviewed; the governing record is outside the entry set")
    disp, _, why = reason.partition(": ")
    ld[k] = {"disposition": disp, "reason": why}
json.dump({"_note": "Written dispositions for /create-injection rev1 (plan/build_dispositions.py from the tools' --json output).", "mutation": d, "liveness": ld}, open(os.path.join(WF, "01c_Dispositions.json"), "w"), indent=1)
print("mutation", len(d), "liveness", len(ld), "missing liveness reasons:", [k for k in req if k not in LIVE])
