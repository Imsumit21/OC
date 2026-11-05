import json, sys
sys.path.insert(0, "/home/sumit/Desktop/OC/Task_Authoring/task_inputs/Working_Files/plan/rubric")
import grade_baselines as g
OUT = {}
for run in sorted(p.name for p in g.BASE.glob("run-*")):
    d = g.load(run)
    w = d["w"]
    logev = [x["event"] for x in w if x["tool"] in ("gsheets_values_append", "gsheets_values_update")]
    def row(co):
        r = d["log"].get(co)
        return None if r is None else {"Decision": r[3], "Answered by": r[4], "told": r[5][:110], "Next": r[6]}
    missing = sorted(k for k in g.COS if k not in d["log"])
    ans = {k: [(x["event"], (x.get("body") or "")[:150].replace("\n", " ")) for x in v] for k, v in d["answered"].items()}
    hub = d["hub"][0] if d["hub"] else None
    keep, sign = g.reply_sections(hub["body"]) if hub else (set(), set())
    e = dict(
        log_events=logev, rows=len(d["rows"]), missing=missing,
        Framewell=row("Framewell"), Lanternfly=row("Lanternfly Publishing"), Spotlight=row("Spotlight Fest"),
        answered_n=len(d["answered"]), extra=sorted(set(d["answered"]) - {k for k, v in g.TRUTH.items() if "written_answer" in v["groups"]}),
        unanswered=sorted({k for k, v in g.TRUTH.items() if "written_answer" in v["groups"]} - set(d["answered"])),
        fw_answer=ans.get("Framewell"), lf_answer=[a[0] for a in ans.get("Lanternfly Publishing", [])], sp_answer=[a[0] for a in ans.get("Spotlight Fest", [])],
        cards=[(x["event"], x["input"]["name"]) for x in d["cards"]],
        contacts_n=len(d["contacts"]), contacts_last=max([x["event"] for x in w if x["tool"] == "contacts_add_new_contact"] or [0]),
        contacts_missing=sorted({k for k, v in g.TRUTH.items() if "contact_add" in v["groups"]} - {k for k in g.COS for c in d["contacts"] if any(a in (c.get("job") or "").lower() for a in g.keys(k))}),
        jan5=[(ev, sorted(g.names_in(s))) for _, s, ev in d["jan5"]],
        hub_event=hub["event"] if hub else None, sign_list=sorted(sign), keep_list=sorted(keep),
    )
    OUT[run] = e
json.dump(OUT, open("/tmp/claude-1000/-home-sumit-Desktop-OC/0eb6fcc3-ed7e-43b1-ab5b-04d624fcaa67/scratchpad/af_writes.json", "w"), indent=1, default=str)
for run, e in OUT.items():
    print("==", run)
    for k, v in e.items():
        print("  ", k, ":", str(v)[:400])
