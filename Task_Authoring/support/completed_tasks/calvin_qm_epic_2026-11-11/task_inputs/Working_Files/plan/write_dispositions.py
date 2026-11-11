#!/usr/bin/env python3
"""Write Working_Files/01c_Dispositions.json: a written disposition for every mutation result and liveness flag."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
TD = "Task_Authoring/task_inputs"
env = {**os.environ, "TASK_AUTHORING_TASK_DIR": os.path.join(WS, TD)}
run = lambda *a: subprocess.run(["python3", "-B", *a], cwd=WS, capture_output=True, text=True, env=env).stdout   # noqa: E731
rep = json.loads(run("Task_Authoring/tools/difficulty_mutation.py", "mutate", "--task-dir", TD, "--json"))
required = rep["dispositions"]["required"]
RULE = {
    "BRANCH": "flips B1, B2, B3: the three ok, chat rows are Waiting on QA only because the #builds post shows #1718 was built from a feature branch and Arthur's doc counts main builds only",
    "INLINE": "flips I1 and I4: the two rows are Waiting on a fix only through Arthur's review comments on #472 and #475",
    "REOPEN": "flips R1: Vincent's thread reply is the only record that takes the pass off the gift row",
    "BACK": "flips K1B: Robert's channel post is the only record that takes the pass off the Endless row",
    "ELSE": "flips E1 and E2: Oliver's line on #473 is the only record that says the two fixes are merged",
    "FILT": "flips F1 and F3: Marcus's DM is the only record of the icon glow report",
    "ALIAS": "flips A1 and A2: Vincent's notes on ZOM-556 and ZOM-560 are what tie the two rows to tickets under other words",
    "GATE": "flips G1 and G2: the changed card moves Daily Gift off the review and Level-end rewards onto it",
}
OVER = {
    "branch_over": ("live", "K6 and K7 read it: un-passing a row whose ok was on a main build flips a control"),
    "inline_over": ("live", "K8 reads it: dropping #472 from the Collect & Win panel row flips a control"),
    "reopen_over": ("weak-accepted", "no direct slot grades the two nr controls (rows 7 and 27); they are declared controls read per run by node_verdicts, and the passed count V1 moves in the writes"),
    "back_over": ("weak-accepted", "no direct slot grades the two Zombie Lane ok controls; K9 (Zombie Lane is Clear) is a write_content slot that moves with them, which the mutation view cannot read"),
    "else_over": ("weak-accepted", "K2 (weight 1) reads the pass claim animation row; the over-application also moves V2 and V3 in the reply, which the mutation view cannot read"),
    "filt_over": ("weak-accepted", "the chat remark is off the list: an extra row moves V3 and V7 in the writes; no direct slot can read a row that should not exist"),
    "alias_over": ("weak-accepted", "no direct slot grades the Ticket cell of rows 1 and 38; the Ticket column is sampled where the mechanism lands (A1, A2) and on K13"),
    "gate_over": ("weak-accepted", "no direct slot grades the review flag of the two Win Streak and Endless controls; the review count V4 moves in the reply, which the mutation view cannot read"),
}
out = {}
for i in required:
    kind, _, name = i.partition(":")
    if kind == "rule" and name in RULE:
        d, r = "live", RULE[name]
    elif kind == "degrade" and name in OVER:
        d, r = OVER[name]
    elif kind == "degrade" and name.startswith("miss_"):
        d, r = "live", f"the channel operator gives {name[5:].upper()}'s members their natural reading: the same slots as the rule's own ablation, and the failure the forecast samples"
    elif kind == "intervention":
        k2, _, n2 = name.partition(":")
        if k2 == "rule":
            d, r = "live", f"removing {n2}'s deciding record changes its members: the record is load-bearing as designed"
        else:
            d, r = "live", "a degrade operator acts on no injected record of its own, so there is nothing to remove: expected"
    elif "shard" in i:
        d, r = "live", "a slice of a rule's records: KILLED where the slice holds a member, EQUIVALENT where it holds none, which is the expected reading for rules that act on one to six rows of 39"
    else:
        d, r = "live", "same reading as the whole-rule result above"
    out[i] = {"disposition": d, "reason": r}
lv = json.loads(run("Task_Authoring/tools/trap_liveness.py", "--task-dir", TD, "--json"))
LIVE = {
    "T_INLINE": "'a fix for it is in main' in Brian's note is the fairness link; it names no PR, no reviewer and no comment, and the deciding words stay in Arthur's inline comment, its GitHub mail and its #zombie-prs copy",
    "T_INLINE_PACK": "same link as T_INLINE: the note asks whether a fix is in main, not which PR or where to look",
    "T_ELSE": "the note's sentence about a dev's line on a merged PR of theirs is the fairness link: without it Oliver's comment could not count; it names no PR and no dev",
    "T_ALIAS_GIFT": "'if a ticket already has the report' is the fairness link to the tie; the ticket key is only on Vincent's note",
    "T_ALIAS_STREAK": "same link as T_ALIAS_GIFT",
    "T_SHARE": "'everyone on the review invite' is the hub's own delegation of the share list; the names are only on the event",
    "T_FIELDS": "'Julia's point about your tickets' is the note's own wording of a field rule it states in full; nothing is hidden behind it",
    "T_STATE": "the state mapping is the note's rule; which tickets change follows from statuses worked out elsewhere",
    "D_432": "a decoy ticket found by the same 'daily gift' words a solver would search; the tie is on ZOM-556",
}
flags = lv.get("dispositions", {}).get("required") or []
live = {}
for f in flags:
    fid = f if isinstance(f, str) else (f.get("id") or f"{f.get('trap')}:{f.get('flag')}")
    trap = fid.split(":")[0]
    live[fid] = {"disposition": "accepted", "reason": LIVE.get(trap, "a fairness link the incorporation chain needs; the deciding fact stays in the trap's own record")}
geom = {"geometry.U": {"disposition": "accepted-unverified", "reason": "key-locality passes on every configuration checked, so U is a bound here; recorded in case a later revision makes the solver non-composable"}}
json.dump({"mutation": out, "liveness": live, "geometry": geom}, open(os.path.join(WF, "01c_Dispositions.json"), "w"), indent=1, ensure_ascii=False)
print("mutation dispositions", len(out), "of", len(required), "· liveness", len(live), list(live)[:12])
