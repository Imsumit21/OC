"""Rebuild plan/load_bearing.txt from the final manifest and the plan (learnings section 39). Run: python3 plan/gen_lb.py"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
m = json.loads((HERE.parent / "01_Hardness_Manifest.json").read_text(encoding="utf8"))
draft = json.loads((HERE.parent / "01_Hardness_Manifest.draft.json").read_text(encoding="utf8"))
denied = {d.get("record") for d in m.get("denied_probes", []) or []}
ids = []


def add(x):
    if x is None or (len(str(x)) == 24 and all(c in "0123456789abcdef" for c in str(x))):
        return   # no form mail for Brian; a 24-hex id is Trello, an unscoped service
    x = str(x)
    if not x or " " in x or x.startswith(("gdocs:", "gslides:", "gsheets:", "trello:", "gdrive:", "page_", "ZOM-")):
        return
    if x.startswith(("harmonygames-Games/", "cmt_")) or x in denied or x in ids:
        return
    ids.append(x)


for f in m["ask_fragments"]:
    for x in f.get("seeded_ids", []) + f.get("base_pointers", []):
        add(x)
for a in m["authorities"]:
    for x in a.get("seeded_ids", []) + a.get("base_pointers", []):
        add(x)
for t in m["traps"]:
    for x in t.get("seeded_ids", []) + t.get("base_pointers", []):
        add(x)
    for v in t.get("version_records") or []:
        add(v.get("id") or v.get("base_pointer"))
for c in m["chains"]:
    for h in c["hops"]:
        add(h["record"])
for s in m["cohort"]["evidence_surfaces"]:
    if s["service"] in ("gdocs", "gmail"):
        for x in s.get("seeded_ids", []):
            add(x)
pr = draft["planned_records"]
for s in pr["sessions"]:
    add(s["notes_doc"])
for f in pr["forms"]:
    add(f.get("msg"))
    add(f.get("thread"))
for k in ("ask", "R0_relay"):
    add(pr[k]["row"])
add(pr["workbook"])
add(pr["kpi_sheet"])
add("evt_da65644831bc088267263d")
add("D076RBM29JS/1758658884.207315")
(HERE / "load_bearing.txt").write_text("\n".join(ids) + "\n", encoding="utf8")
print(len(ids), "load-bearing ids")
