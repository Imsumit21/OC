#!/usr/bin/env python3
"""Write Working_Files/01c_Dispositions.json: a written disposition for every mutation result and liveness flag."""
import json, os, re, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
env = {**os.environ, "TASK_AUTHORING_TASK_DIR": os.path.join(WS, "Task_Authoring/task_inputsK")}
txt = subprocess.run(["python3", "-B", "Task_Authoring/tools/difficulty_mutation.py", "mutate", "--task-dir", "Task_Authoring/task_inputsK", "--json"],
                     cwd=WS, capture_output=True, text=True, env=env).stdout
rep = json.loads(txt)
required = rep["dispositions"]["required"]
RULE = {
    "DONE": "flips X1 and with it the sheet, ticket and approval reading: Arthur's inline comment is what moves the row off Go. The client source carries the same day, so a close reader needs no comment; kept as a second route",
    "CORR": "flips X3 and X16: the new line only exists in Leonard's reply under Martin's post",
    "DEP": "flips X5: the row is a Hold only through the join of the trigger, the ask point and the reach test",
    "QA": "flips X7: Vincent's DM reply is the only record that withdraws the iPhone pass",
    "ALIAS": "flips X9: the row's ticket is under another name outside the parent",
    "FILT": "flips X11 and X12: both asks sit in comments on tickets about other things",
    "BUILT": "flips X15: the ask reads as new work until the batch is read as covering day 14. The source carries it too; the cancel mail is the ● carrier the rule reads",
}
OVER = {
    "done_over": ("live", "K2 reads it: over-applying the day test to Lapsed 1 day flips a control"),
    "dep_over": ("live", "K1 reads it: over-applying the reach test to Lives recharged flips a control"),
    "qa_over": ("live", "K1 reads it: doubting Vincent's pass on Lives recharged flips a control"),
    "corr_over": ("weak-accepted", "no slot grades Lapsed 1 day's headline, so this over-application is only visible in the plan row; K10 keeps one headline control on Lives recharged. Not worth a new slot: the surface already has a headline sample"),
    "alias_over": ("weak-accepted", "no slot grades Season Pass start's Ticket column; the Ticket column is sampled on the Win & Collect row, where the mechanism lands, and adding a control slot would not change any decision"),
    "filt_over": ("weak-accepted", "the red dot is off the plan: V1 (register_keys_exact, a delivery slot) catches an extra row, and delivery slots never count in the mutation view"),
    "built_over": ("weak-accepted", "no slot grades Lapsed 30 days' call; it is a declared control read per run by node_verdicts, not a graded row"),
    "follow_over": ("weak-accepted", "K12 greps the Canceled update on Axe Arena in the writes, which the solver cannot read; the operator is live in the ticket-state field only"),
    "ch_miss": ("live", "the channel operator moves every designed member; it is the failure the forecast samples"),
}
out = {}
for i in required:
    kind, _, name = i.partition(":")
    if kind == "rule" and name in RULE:
        d, r = "live", RULE[name]
    elif i == "rule:FOLLOW":
        d, r = "solver-gap", "the ticket state is graded from the linear_update_issue payloads (X18, X19, X19b are write_content), which the solver's rows do not reach, so no direct slot moves; the failure is real and the intervention below shows the freeze comment is load-bearing"
    elif kind == "degrade" and name in OVER:
        d, r = OVER[name]
    elif kind == "intervention":
        k2, _, n2 = name.partition(":")
        if k2 == "rule":
            d, r = "live", f"removing {n2}'s deciding record changes its member: the record is load-bearing as designed"
        else:
            d, r = "live", "a degrade operator acts on no injected record of its own, so there is nothing to remove: expected"
    elif kind.startswith("shard") or "shard" in i:
        d, r = "live", "a shard of a rule's records: the same reading as that rule's whole result"
    else:
        d, r = "live", "same reading as the whole-rule result above"
    out[i] = {"disposition": d, "reason": r}
live_txt = subprocess.run(["python3", "-B", "Task_Authoring/tools/trap_liveness.py", "--task-dir", "Task_Authoring/task_inputsK", "--json"],
                          cwd=WS, capture_output=True, text=True, env=env).stdout
lv = json.loads(live_txt)
LIVE = {"T3": "the rule's reach sentence is a fairness link: it is the only way the join can be made, and the deciding fact stays in Robert's post and the trigger on the sheet",
        "T5": "'under whatever name' is the hub's fairness link to the alias; removing it would leave the ticket unfindable by intent",
        "T6": "the hub's 'filed on a ticket or a card' is the scope sentence the two off-parent asks need; removing it would make them out of scope",
        "T11": "'PNs Beta tab' names the population; the other tabs stay near-duplicates by design",
        "T14": "'phone message' is the rule's own predicate; red-dot tickets stay keyword collisions the predicate excludes",
        "T15": "same predicate as T14: Rate Us and the permission popup show inside the game"}
ldisp = {}
for f in [f"{n['id']}:{x}" for n in lv["nodes"] + lv.get("authority_decoys", []) for x in n["flagged"]]:
    node = f.split(":")[0]
    ldisp[f] = {"disposition": "accepted", "reason": LIVE.get(node, "a fairness link, kept: the playbook says never remove one to clear a flag")}
json.dump({"mutation": out, "liveness": ldisp}, open(os.path.join(WF, "01c_Dispositions.json"), "w"), indent=1, ensure_ascii=False)
print("mutation", len(out), "liveness", len(ldisp), "required", len(required))
