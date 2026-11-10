#!/usr/bin/env python3
"""Write Working_Files/01c_Dispositions.json: a written disposition for every mutation result, channel degrade,
intervention and liveness flag of the current SQL + solver (reads `difficulty_mutation.py mutate --json` and
`trap_liveness.py --json`, and re-solves each rule for what it really moves). Re-run after any SQL or solver change,
before preflight_report.py.

Labels follow the measured result: a KILLED rule or degrade is `live`; anything WEAK, SURVIVED or EQUIVALENT is never `live`
and its reason says what it moved. A rule that is not KILLED is printed. An intervention is `live` only where the solver
reads the amount or the account from the seeded row; a load-bearing result that rests on a note-presence gate stays
weak-accepted, because the deciding fact is a base record. A liveness flag with no reviewed reason below is left out, so
`trap_liveness.py --require-dispositions` stops on it.
"""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
TASK = "Task_Authoring/task_inputsS2"
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=TASK)
sys.path.insert(0, os.path.join(WS, "Task_Authoring", "tools"))
import oracle_kit as ok  # noqa: E402


def tool(args):
    r = subprocess.run([sys.executable, "-B"] + args, cwd=WS, env=ENV, capture_output=True, text=True, timeout=1200)
    return json.loads(r.stdout)


mut = tool(["Task_Authoring/tools/difficulty_mutation.py", "mutate", "--task-dir", TASK, "--json"])
status = {}
for gname in ("rules", "degrades"):
    for m in mut["mutants"].get(gname) or []:
        status[m["id"]] = m
inter = {i["id"]: i for i in mut["interventions"]}

surface = json.load(open(os.path.join(WF, "01_Gradable_Surface.json")))
mod = ok.load_solver(os.path.join(WF, "solver", "solver.py"))
state = mod.load_state(open(os.path.join(TI, "01_Universe_Inject.sql")).read())
truth = mod.solve(state)
tot0 = mod.aggregates(truth)["totals"]
AGG = {"B1": lambda t: t["build"][mod.DD], "B2": lambda t: t["build"][mod.ZM], "B3": lambda t: t["build"][mod.CF], "B4": lambda t: t["company_usd"]}
PRESENCE_GATED = {"RET": "the Apr 2024 Slack notes", "OFF": "the five Western Union receipts", "ALIAS": "Node's invoice mail",
             "CLASS": "her contract", "CURR": "the BGN notice and the laptop note"}


def money(v):
    return f"{v:,.2f}"


def effect(rule):
    """What the rule's natural reading really moves, and which declared aggregate slots it leaves alone."""
    rows = mod.solve(state, disable=frozenset({rule}))
    tot = mod.aggregates(rows)["totals"]
    k = next(iter(mod.touched(state, rule)))
    a, b = truth[k], rows[k]
    bits = [f"{k} paid {money(a['paid'])} -> {money(b['paid'])}" if a["paid"] != b["paid"] else f"{k} paid unchanged at {money(a['paid'])}"]
    if a["Bucket"] != b["Bucket"]:
        bits.append(f"bucket {a['Bucket']} -> {b['Bucket']}")
    moved = [s for s, f in AGG.items() if f(tot) != f(tot0)]
    bits += [f"{s} {money(AGG[s](tot0))} -> {money(AGG[s](tot))}" for s in moved]
    declared = [s["id"] for s in surface["slots"] if rule in (s.get("mechanisms") or [])]
    idle = [s for s in declared if s in AGG and s not in moved]
    return "; ".join(bits), declared, idle


mdisp = {}
not_killed = []
for rid in mut["dispositions"]["required"]:
    if rid.startswith("rule:"):
        r = rid.split(":", 1)[1]
        m = status[rid]
        moves, declared, idle = effect(r)
        flipped = m.get("flipped_slots") or []
        text = [s for s in declared if s not in flipped]
        reason = (f"{m['diagnostic']}: flips {', '.join(flipped) or 'no slot'}. Its natural reading moves: {moves}."
                  + (f" Its declared text slots ({', '.join(text)}) are graded from the writes and out of this measure." if text else ""))
        if idle:
            reason += f" Declared {', '.join(idle)} does not move under this fallback, so geometry counts it by declaration only."
        if m["diagnostic"] != "KILLED":
            not_killed.append(f"{r}: {m['diagnostic']}")
        mdisp[rid] = {"disposition": "live" if m["diagnostic"] == "KILLED" else "weak-accepted" if m["diagnostic"] == "WEAK" else "redesign", "reason": reason}
    elif rid == "degrade:ch_miss":
        m = status[rid]
        members = sorted({x for c in mod.CHANNELS.values() for x in c["members"]})
        mdisp[rid] = {"disposition": "live" if m["diagnostic"] == "KILLED" else "weak-accepted", "reason": f"{m['diagnostic']}: flips "
                      f"{', '.join(m.get('flipped_slots') or []) or 'no slot'}, putting each channel member ({', '.join(members)}) on its rule's natural reading"}
    elif rid.startswith("degrade:"):
        op = rid.split(":", 1)[1]
        m = status[rid]
        ctl = next((v["controls"] for v in mod.RULES.values() if v["over_application"] == op), [])
        mdisp[rid] = {"disposition": "weak-accepted", "reason": f"{m['diagnostic']}: flips {', '.join(m.get('flipped_slots') or []) or 'no slot'}. Over-application operator on "
                      f"{', '.join(ctl)} ({mod.DEGRADES[op]}). Controls measure over-application and are reported as control trials, never as landings, so it is deliberately not a designed loss"}
    elif rid.startswith("intervention:rule:"):
        r = rid.split(":")[-1]
        i = inter[rid]
        changed = ", ".join(i.get("changed_records") or []) or "nothing"
        flipped = ", ".join(i.get("flipped_slots") or []) or "no slot"
        if i.get("status") != "load-bearing":
            mdisp[rid] = {"disposition": "redesign", "reason": f"{i.get('status')}: {i.get('finding') or i.get('why')}; removed {len(i.get('removed_records') or [])} record(s), changed {changed}"}
        elif r in PRESENCE_GATED:
            mdisp[rid] = {"disposition": "weak-accepted", "reason": f"load-bearing through the solver's presence gate only: removing the {len(i['removed_records'])} "
                          f"note(s) on the issue changes {changed} and flips {flipped}, inside the closure. The fact that decides the row is base ({PRESENCE_GATED[r]}), fixed in the "
                          "solver, which an in-memory SQL edit can't remove; a run could still reach it by name without the note"}
        else:
            mdisp[rid] = {"disposition": "live", "reason": f"load-bearing: the solver reads the amount or the account from this seeded row's text; removing it changes "
                          f"{changed} and flips {flipped}, inside the closure, and no base record restores it"}
    elif rid.startswith("intervention:degrade:"):
        mdisp[rid] = {"disposition": "redundant", "reason": "no-injected-records: a degrade models a run's reading error and has no deciding record of its own; "
                      "the rule interventions cover the records"}

LIVE = {
    "T6:breadcrumb": ("weak-accepted", "the hub names the method by title, the fairness link for the bucket sentence. The method gives the rule only; what she did is in her "
                      "contract f_20a0df3860bb5731d22f07, reached through ENG-2455 and the contact row, and neither is in the entry set"),
    "T8:self-advertising": ("weak-accepted", "the deck is titled 'Note to angels (draft)' and Leonard's ask calls it the draft deck, so the word is natural. It marks the deck unfinished, "
                            "not its figures wrong, and the working sheet carries the same quick figures without it"),
    "T9:breadcrumb": ("weak-accepted", "this trap is neutralised by the entry set: the hub sends every run to the method, whose third sentence says it replaces the plan on the board. "
                      "The sentence stays because unique ground truth needs it. T9 carries no rule and no slot, so nothing is lost"),
}
lv = tool(["Task_Authoring/tools/trap_liveness.py", "--task-dir", TASK, "--json"])
req = (lv.get("dispositions") or {}).get("required") or []
ldisp = {k: {"disposition": LIVE[k][0], "reason": LIVE[k][1]} for k in req if k in LIVE}
out = {"_note": "Written dispositions for /create-injection rev1 (plan/build_dispositions.py from the tools' --json output).",
       "mutation": mdisp, "liveness": ldisp}
with open(os.path.join(WF, "01c_Dispositions.json"), "w") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)
    f.write("\n")
print("mutation", len(mdisp), "of", len(mut["dispositions"]["required"]), "liveness", len(ldisp), "rules not KILLED:", not_killed or "none",
      "unreviewed liveness flags:", [k for k in req if k not in LIVE] or "none")
