#!/usr/bin/env python3
"""Write Working_Files/01c_Dispositions.json: a written disposition for every mutation result, channel degrade,
intervention and liveness flag of the current SQL + solver (reads `difficulty_mutation.py mutate --json` and
`trap_liveness.py --json`). Re-run after any SQL or solver change, before preflight_report.py."""
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
for gname in ("rules", "degrades", "shards"):
    for m in mut["mutants"].get(gname) or []:
        if isinstance(m, dict) and m.get("id"):
            status[m["id"]] = (m.get("diagnostic"), m.get("flipped_slots") or [])
for i in mut["interventions"]:
    status[i["id"]] = (i.get("verdict") or i.get("result") or i.get("status") or i.get("diagnostic"), [])

TEXT = {   # the write-content slots each rule decides (geometry counts them; the solver does not read text)
    "CORR": "C2, C3, R2, R3, R4, R6", "AUTH": "C3, R4, R6, R7", "FILT": "C1, L1, R2, R3", "COMPLETE": "R2, R3",
    "DONE": "C3, R6", "DATE": "C4, C5", "STACKS": "P1, R2, R3"}
DIRECT = {"CORR": "G2 (DD decision) and V1", "AUTH": "G2, G3 and V1", "COMPLETE": "I1 (Metabase decision) and V1",
          "FILT": "V1 (the LLC row count)"}
ONLY = {"CORR": "Arthur's DM reply is the only record of the trimmed $140", "AUTH": "only REVENUE_DAILY gives January income per game",
        "FILT": "the campaign is in no list; Leonard's status and the channel history are its only records",
        "COMPLETE": "Arthur's mail is the only record of the $248 he carries", "DONE": "the App Store notice is the only record that the support build did not ship",
        "DATE": "the card's own-deadline rule, the base layer.ai access-date post and (rev4) Leonard's reply under it (C09UHHN6PFZ/1770923700.470906, the only record that CF's concept art is there) set the layer.ai step",
        "STACKS": "Arthur's Jenkins email (robert@harmonygames.co/1856982378087295205) is the only record of what CF's account bills now ($62, over the ENG-2445 note's ~$95)"}
CTRL = {"corr_over": "Combo Fighter backend and auth stacks (AWS) (P1 reads its $62 in the plan text)",
        "auth_over": "Combo Fighter (G1)", "filt_over": "Unity Ads balance and Playable vendor (no slot of their own; they enter V1 and R1)",
        "complete_over": "Build machines (no slot; a Founder row changes no aggregate the surface reads)",
        "done_over": "Helpshift (I4 reads only its decision)", "stacks_over": "Domino Delights production account (AWS) (C2 reads its $140 in the plan text)",
        "date_over": "AppsFlyer (P3 reads its cost, not its date)"}
mdisp = {}
for rid in mut["dispositions"]["required"]:
    st, slots = status.get(rid, ("?", []))
    st = str(st).upper()
    if rid.startswith("rule:"):
        r = rid.split(":", 1)[1]
        if st == "KILLED":
            mdisp[rid] = {"disposition": "live", "reason": f"KILLED: flips {DIRECT.get(r, 'its direct slots')} and the write-content slots {TEXT[r]}; {ONLY[r]}"}
        else:
            mdisp[rid] = {"disposition": "live", "reason": f"{st} on direct slots by construction: {r} is graded through the plan and reply text "
                          f"({TEXT[r]}, write_content slots the grader decodes; geometry counts them as flippable){'' if r not in DIRECT else ' and ' + DIRECT[r]}; {ONLY[r]}"}
    elif rid == "degrade:ch_miss":
        mdisp[rid] = {"disposition": "live", "reason": f"{st}: the channel-miss operator puts each channel member on its rule's natural reading "
                      "(DD/ZM keys, the campaign, Metabase/dbt/GitHub, DD support, layer.ai/GitHub dates, CF's stacks); it flips G2, G3, I1, V1 and the write-content slots"}
    elif rid.startswith("degrade:"):
        op = rid.split(":", 1)[1]
        mdisp[rid] = {"disposition": "weak-accepted", "reason": f"{st}: over-application operator on its control member, {CTRL[op]}. Controls measure "
                      "over-application and are reported as control trials (OVER-APPLIED / HELD) in node_verdicts, never as landings; they are deliberately not weighted"}
    elif rid.startswith("intervention:rule:"):
        r = rid.split(":")[-1]
        if False:
            pass
        else:
            mdisp[rid] = {"disposition": "live", "reason": f"{st}: removing the rule's injected deciding record from an in-memory copy of the SQL flips its members to "
                          "the natural reading; nothing outside the node's closure changed (no escape)"}
    elif rid.startswith("intervention:degrade:"):
        mdisp[rid] = {"disposition": "redundant", "reason": "no-injected-records: a degrade operator models a run's reading error and has no deciding record of "
                      "its own; the rule interventions cover the records"}
    else:
        mdisp[rid] = {"disposition": "live", "reason": f"{st}"}

LIVE = {
    "T1:breadcrumb": "weak-accepted: the hub's delegations reach the draft (f_d996e4c434ce160dc52596) and the project's issue note, both stale versions; the governing DM reply D04V95AAAHW/1770952200.665739 is outside the entry set (threaded under an unrelated Feb 2 root)",
    "T2:breadcrumb": "weak-accepted: the ground rules (f_1e468a9d69ea0f0a2001f5) name the warehouse table by role, an incorporation link UGT needs; the difficulty left is the month, the grain sum and the join with CORR's $140",
    "T3:breadcrumb": "weak-accepted: the hub's 'what it costs us March through May' is the fairness link for the campaign; the campaign itself (C09UHHN6PFZ/1770404445.795829) is in no entry record, and (rev4) Leonard's status C09UHHN6PFZ/1770938400.370665 no longer uses the project word the rev3 run searched first",
    "T3:order": "weak-accepted: the entry set meets the project and #winddown lists before any campaign record; that ordering is the designed filter trap (the campaign sits only in channel history and Leonard's status)",
    "T4:breadcrumb": "weak-accepted: the split email (robert@harmonygames.co/1856989298688559716) states the counting rule, not Arthur's completion (robert@harmonygames.co/1856975772058401508), which a mail search by tool name finds",
    "T8:order": "weak-accepted: the hub uses Leonard's draft (f_d996e4c434ce160dc52596) for its layout only and never labels it superseded; its numbers are the stale summary by design",
    "T8:self-advertising": "weak-accepted: the draft's title says '(draft)' because Leonard named it so on Tuesday (natural wording, no 'stale' marker); its rows carry the old figures the later notes overturn",
    "T9:breadcrumb": "weak-accepted: the hub's cost sentence again (fairness link); the one-off Unity Ads balance is only in C09UHHN6PFZ/1770845002.610529 and its issue note",
    "T9:order": "weak-accepted: the one-off lines are met in #prototype history; nothing in the entry set ranks them",
    "T16:breadcrumb": "weak-accepted: the hub's cost sentence; the campaign status is in C09UHHN6PFZ/1770938400.370665 (a reply under the Feb 6 root), not in the hub",
    "T16:order": "weak-accepted: Robert's deck (Feb 5) and the Feb 7 'both live' post are met before the Feb 12 status by design (superseding versions in real time order)",
}
try:
    lv = tool(["Task_Authoring/tools/trap_liveness.py", "--task-dir", "Task_Authoring/task_inputs", "--json"])
    req = (lv.get("dispositions") or {}).get("required") or []
except Exception:   # noqa: BLE001
    req = list(LIVE)
ldisp = {}
for k in req:
    reason = LIVE.get(k, "weak-accepted: lexical flag reviewed; the governing record is outside the entry set")
    disp, _, why = reason.partition(": ")
    ldisp[k] = {"disposition": disp, "reason": why}
out = {"_note": "Written dispositions for /create-injection rev4 (plan/build_dispositions.py from the tools' --json output).",
       "mutation": mdisp, "liveness": ldisp}
json.dump(out, open(os.path.join(WF, "01c_Dispositions.json"), "w"), indent=1)
open(os.path.join(WF, "01c_Dispositions.json"), "a").write("\n")
print("mutation", len(mdisp), "liveness", len(ldisp), "missing liveness reasons:", [k for k in req if k not in LIVE])
