#!/usr/bin/env python3
"""Rubric rehearsal (advisory, not a verifier): grade the six rev2 baseline runs against the drafted 09_Rubrics.json
rows and run the V3 difficulty gates (tools/difficulty_stats.compute) on the result.

Rows that cover a gradable-surface slot take the slot's result from run_forensics/rev2/baseline/surface_grades.json
(surface_grader decoded every write); the other rows are graded here from the decoded writes (run-n/writes.json):
the sheet's cells, the brief text, ticket moves and comments, Drive shares. Text checks are keyword proxies of what
a judge reads, so the per-row result is an estimate. Writes plan/rubric/rehearsal_input.json and prints the gates."""
import ast
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
TASK = WF.parent
WS = TASK.parents[1]
BASE = WF / "run_forensics" / "rev2" / "baseline"
sys.path.insert(0, str(WF / "oe_gen"))
sys.path.insert(0, str(WS / "Task_Authoring" / "tools"))
import model as O                 # noqa: E402
import difficulty_stats as stats  # noqa: E402

rows = json.loads((HERE / "rows.json").read_text())
crit = json.loads((TASK / "09_Rubrics.json").read_text())
grades = json.loads((BASE / "surface_grades.json").read_text())["runs"]
BY_T = {l["ticket"]: l for l in O.BY.values()}
OWED_T = {l["ticket"] for l in O.BY.values() if l["state"] == "Owed"}
HOLDER = {"Brian": "brian", "Claire": "claire", "Calvin": "calvin", "Martin": "martin"}
OWED_KW = {"A1": r"ascii|binary|text (?:kind|format|file)", "A2": r"\bUVs?\b|unwrap|redo|redone",
           "C4": r"zip|unpack|cut off|re-?upload|put (?:them |it )?back|outgoing folder", "C2": r"own version|librar|licen|Soundly",
           "VIS": r"."}
SLOT_TAGS = re.compile(r"^(x_|o_|h_|bs_|sheet_volume$|move_Refrigerator$|comment_DES-(349|367|380|402)$|dm_|post_|share_brief_intake$|share_list_brian)")


def val(x):
    if isinstance(x, str):
        try:
            return ast.literal_eval(x)
        except (ValueError, SyntaxError):
            return x
    return x


def run_view(n):
    w = json.loads((BASE / f"run-{n}" / "writes.json").read_text())
    ok = [x for x in w if x.get("ok") in (True, "True")]
    table = []
    for x in ok:
        if x["tool"] in ("gsheets_values_update", "gsheets_values_append"):
            table += [list(map(str, r)) for r in val(x.get("values")) or []]
    header = [h.casefold() for h in table[0]] if table else []
    data = {r[0].strip().casefold(): r for r in table[1:] if r}
    brief = ""
    doc_ids, sheet_ids = set(), set()
    for x in ok:
        if x["tool"] == "gdocs_create_document":
            inp = val(x.get("input")) or {}
            brief += "\n" + (inp.get("bodyText") or "")
        if x["tool"] == "gdocs_batch_update":
            inp = val(x.get("input")) or {}
            doc_ids.add(inp.get("documentId"))
            for rq in inp.get("requests", []):
                brief += "\n" + ((rq.get("insertText") or {}).get("text") or "")
        if x["tool"] == "gsheets_create_spreadsheet":
            sheet_ids.add(x.get("spreadsheet_id"))
    shares = {}
    for x in ok:
        if x["tool"] == "gdrive_share_file" and x.get("role") == "reader":
            shares.setdefault(x.get("email"), set()).add(x.get("file_id"))
    moved = {x["issue"] for x in ok if x["tool"] == "linear_update_issue" and str(x.get("state")).casefold() == "todo"}
    comments = {}
    for x in ok:
        if x["tool"] == "linear_create_comment":
            comments.setdefault(x["issue"], []).append(x.get("body") or "")
    return dict(header=header, data=data, brief=brief, shares=shares, moved=moved, comments=comments,
                doc=any(x["tool"] == "gdocs_create_document" for x in ok), sheet=bool(sheet_ids), sheet_ids=sheet_ids)


def has(text, rx):
    return re.search(rx, text, re.I | re.S) is not None


def grade(r, v, slots):
    tag = r["tag"]
    if r["slot"] and SLOT_TAGS.match(tag):
        return bool(slots.get(r["slot"][0]))
    b = v["brief"]
    if tag == "brief_doc":
        return v["doc"]
    if tag == "sheet_doc":
        return v["sheet"]
    if tag in ("b_scenario", "b_purpose", "b_lose", "b_tray", "b_music", "b_start", "b_held_Rocket sound"):
        return bool(slots.get(r["slot"][0]))
    if tag.startswith("b_eight_"):
        name = tag[len("b_eight_"):]
        if name == "Bow":
            return bool(slots.get("B1"))
        return has(b, re.escape(name))
    if tag == "b_extras":
        return has(b, r"swap|extras?\b")
    if tag.startswith("b_zombie_"):
        return has(b, re.escape(tag[len("b_zombie_"):]))
    if tag == "b_anim":
        return has(b, r"\bwalk")
    if tag == "b_win":
        return has(b, r"(eliminat|kill|clear|defeat|destroy)\w*.{0,60}zombie|zombie.{0,60}(eliminat|kill|clear|defeat|destroy)")
    if tag == "b_held_Explosion sound":
        return has(b, r"explosion.{0,160}(own version|not ours|librar|licen|hold|later|placeholder|replace)")
    if tag.startswith("b_use_"):
        return has(b, re.escape(tag[len("b_use_"):].split(" ")[0]))
    if tag == "sheet_header":
        want = ["line", "category", "board set", "state", "what's owed", "who has it", "ticket"]
        h = [x.replace("what is owed", "what's owed") for x in v["header"]]
        return all(w in h for w in want)
    if tag == "sheet_ticket":
        row = v["data"].get("cannon")
        return bool(row) and "DES-398" in " ".join(row)
    if tag == "sheet_category":
        row = v["data"].get("iron")
        return bool(row) and any(c.strip().casefold() == "bathroom" for c in row[1:3])
    if tag.startswith("move_") and tag != "move_volume":
        t = re.search(r"DES-\d+", r["title"]).group()
        return t in v["moved"]
    if tag == "move_volume":
        return v["moved"] == OWED_T
    if tag.startswith("comment_"):
        t = tag[len("comment_"):]
        l = BY_T[t]
        body = " ".join(v["comments"].get(t, []))
        return bool(body) and has(body, HOLDER[l["who"]]) and has(body, OWED_KW.get(l["cls"], "."))
    if tag.startswith("share_"):
        _, which, who = tag.split("_", 2)
        email = next(e for e in v["shares"] if e and e.split("@")[0].startswith(who.split("@")[0])) if any(
            e and e.split("@")[0].startswith(who.split("@")[0]) for e in v["shares"]) else None
        ids = v["shares"].get(email, set())
        return (bool(ids - v["sheet_ids"]) if which == "brief" else bool(ids & v["sheet_ids"]))
    raise KeyError(tag)


rollouts = []
for n in range(1, 7):
    g = grades[f"run-{n}"]
    v = run_view(n)
    res = {f"R{i}": grade(r, v, g["results"]) for i, r in enumerate(rows, 1)}
    rollouts.append({"id": f"run-{n}", "status": "completed", "tool_calls": int(g["counted_calls"]),
                     "models": val(g["models"]),
                     "model_source": g.get("model_source") or f"trajectory:run-{n}", "model_check": val(g.get("model_check")),
                     "results": res})
data = {"spec_version": "V3", "difficulty_mode": "hard", "task_type": "long-horizon",
        "rubrics": [{"id": f"R{i}", "weight": c["weight"], "valid": True} for i, c in enumerate(crit, 1)],
        "rollouts": rollouts}
(HERE / "rehearsal_input.json").write_text(json.dumps(data, indent=1) + "\n")
out = stats.compute(data)
tot = sum(c["weight"] for c in crit)
for ro in rollouts:
    passed = sum(c["weight"] for i, c in enumerate(crit, 1) if ro["results"][f"R{i}"])
    failed = [k for k, x in ro["results"].items() if not x]
    print(f"{ro['id']}: {passed}/{tot} = {passed / tot:.1%} · {len(failed)} rows failed · calls {ro['tool_calls']}")
always = [f"R{i}" for i in range(1, len(crit) + 1) if all(ro["results"][f"R{i}"] for ro in rollouts)]
never = [f"R{i}" for i in range(1, len(crit) + 1) if not any(ro["results"][f"R{i}"] for ro in rollouts)]
print(f"rows passed by all six: {len(always)} (weight {sum(crit[int(r[1:]) - 1]['weight'] for r in always)}) · rows failed by all six: {len(never)}: {' '.join(never)}")
view = out["views"]["platform"] if "views" in out else out
print(json.dumps({k: v.get("verdict") + " · " + str(v.get("value")) for k, v in view["gates"].items()
                  if isinstance(v, dict) and "verdict" in v}, indent=1, ensure_ascii=False))
