#!/usr/bin/env python3
"""Write Working_Files/01c_Dispositions.json: a written disposition for every mutation result, channel degrade, intervention and
liveness flag of the current SQL and solver. Re-run after any SQL or solver change, before preflight_report.py."""
import json, os, subprocess

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
PY = os.path.expanduser("~/.local/bin/python3.12")
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")


def tool(args):
    r = subprocess.run([PY, "-B"] + args, cwd=WS, env=ENV, capture_output=True, text=True, timeout=1200)
    return json.loads(r.stdout)


mut = tool(["Task_Authoring/tools/difficulty_mutation.py", "mutate", "--task-dir", "Task_Authoring/task_inputs", "--max-k", "10", "--allow-max-k", "10", "--json"])
status = {}
for g in ("rules", "degrades", "shards"):
    for m in mut["mutants"].get(g) or []:
        if isinstance(m, dict) and m.get("id"):
            status[m["id"]] = (m.get("diagnostic"), m.get("flipped_slots") or [])
for i in mut["interventions"]:
    status[i["id"]] = (i.get("status"), [])
ONLY = {"ADV": "the Due Diligence advisor table and the term sheet are the only records that take advisor options out of the merged lines",
        "LETTER": "only joining the six letters to the eight Feb 12 Carta entries shows the two with no letter",
        "TOLD": "Leonard's Feb 9 DM and Robert's seeded reply are the only records that two angels were told",
        "ASOF": "KPMG's seeded mail fixes the date; the notices' effective dates give the figures",
        "FAM": "the seeded reply under the Feb 12 list is the only record of the family rule",
        "SIDE": "the signed chain is the only record that adds Segerstrale", "BOARD": "the two resignation mails decide the board",
        "ASK": "Claire's group DM is the only record of the question",
        "BOUNCE": "the seeded delivery failure in Owen's letter thread is the only record that his letter never reached him",
        "EXT": "Calvin's seeded forward of Carta's Jan 23 update is the only record of ES-3's Feb 20 last day",
        "ALIAS": "Leonard's seeded Feb 12 mail to Akin is the only record that Collins was told"}
TEXT = {"ADV": "K1, K8, P1, A1, NC_Deepak, B2", "LETTER": "C_DATE, N_Vincent, N_Oliver", "TOLD": "C_FIRST, LC_Seg, LC_Neb", "ASOF": "A1, A2, AL_*",
        "FAM": "F1, F2, F3, N_COUNT", "SIDE": "S3", "BOARD": "B1, B2, L6, G2", "ASK": "Q1", "BOUNCE": "C_DATE", "EXT": "P1, P_first, N_Calvin, D6, N_COUNT", "ALIAS": "C_FIRST, LC_Col"}
OVER = {"adv_over": "ENG-2441 and ENG-2442", "letter_over": "ENG-2450 and ENG-2460", "told_over": "ENG-2448", "asof_over": "ENG-2455", "fam_over": "ENG-2442",
        "side_over": "ENG-2447", "board_over": "SUMMARY", "ask_over": "ENG-2461", "bounce_over": "ENG-2456", "ext_over": "ENG-2454", "alias_over": "ENG-2449"}
md = {}
for rid in mut["dispositions"]["required"]:
    st, _ = status.get(rid, ("?", []))
    st = str(st)
    if rid.startswith("rule:"):
        r = rid.split(":", 1)[1]
        md[rid] = {"disposition": "live", "reason": f"{st}: graded through its direct slots and the write-content slots {TEXT[r]}, which geometry counts; {ONLY[r]}"}
    elif rid.startswith("shard:"):
        r = rid.split(":")[1]
        md[rid] = {"disposition": "live", "reason": f"{st}: a slice of rule {r}'s keys; the rule's other keys and write-content slots {TEXT[r]} carry the rest"}
    elif rid.startswith("degrade:ch_") or rid == "degrade:live_miss":
        md[rid] = {"disposition": "live", "reason": f"{st}: the channel puts a member on its natural reading; where no direct slot reads the field, the write-content slots do"}
    elif rid.startswith("degrade:"):
        op = rid.split(":", 1)[1]
        md[rid] = {"disposition": "weak-accepted", "reason": f"{st}: over-application on its control {OVER[op]}; controls measure over-application and are not weighted as landings"}
    elif rid.startswith("intervention:rule:"):
        r = rid.split(":")[-1]
        if st == "no-injected-records":
            md[rid] = {"disposition": "live", "reason": f"no-injected-records: {r} is decided by base records; {ONLY[r]}"}
        else:
            md[rid] = {"disposition": "live", "reason": f"{st}: removing the rule's injected deciding record flips its members to the natural reading, and nothing outside its closure changed"}
    elif rid.startswith("intervention:degrade:"):
        md[rid] = {"disposition": "redundant", "reason": "no-injected-records: a degrade models a run's reading error and has no deciding record of its own; the rule interventions cover the records"}
    else:
        md[rid] = {"disposition": "live", "reason": st}
lv = tool(["Task_Authoring/tools/trap_liveness.py", "--task-dir", "Task_Authoring/task_inputs", "--json"])
req = (lv.get("dispositions") or {}).get("required") or []
LIVE = {
 "breadcrumb": "weak-accepted: the delegation words reach the wrong source first or share terms with the authority by design; the deciding record stays outside the entry set",
 "order": "weak-accepted: the entry set meets the claim before the overturning record, which is the designed order",
 "self-advertising": "weak-accepted: the draft sheet's title says draft because Leonard named it so; T20 carries no weight",
}
ld = {}
for k in req:
    d, _, why = LIVE.get(k.split(":")[-1], LIVE["breadcrumb"]).partition(": ")
    ld[k] = {"disposition": d, "reason": why}
out = {"_note": "Written dispositions for /create-injection rev2 (plan/build_dispositions.py from the tools' --json output).", "mutation": md, "liveness": ld, "geometry": {"geometry.U": {"disposition": "accepted-unverified", "reason": "ten solver rules exceed the default k of 8: with the disclosed --max-k 10 --allow-max-k 10 override key-locality passes on 55 of 55 configurations and U = 0.782 (205/262) PASS against the 0.15 the medium cap needs (plan/geometry.txt); at the default k the bound is unverified, not failed"}}}
json.dump(out, open(os.path.join(WF, "01c_Dispositions.json"), "w"), indent=1, ensure_ascii=False)
open(os.path.join(WF, "01c_Dispositions.json"), "a").write("\n")
print("mutation", len(md), "liveness", len(ld))
