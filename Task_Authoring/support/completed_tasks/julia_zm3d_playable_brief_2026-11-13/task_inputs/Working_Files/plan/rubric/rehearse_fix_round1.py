#!/usr/bin/env python3
"""Rubric rehearsal on the repaired rubric (/rubric round 1 fixes; advisory, not a verifier): grade the six rev2
baseline runs against the 153 rows of 09_Rubrics.json and run the V3 difficulty gates (tools/difficulty_stats.compute).

Same method as rehearse_rows.py (surface_grader's slot results where a row covers a slot, keyword proxies on the
decoded writes otherwise), keyed through plan/rubric/fix_round1_map.json. What differs from the first rehearsal:
split comment rows are graded per part (the owed text, the holder's name); the 49-move volume row is a count only; the
Bow row no longer asks for Dynamite to be gone; the four added rows are graded from the sheet cells and the write order.
Writes plan/rubric/rehearsal_input_round1.json and prints the gates."""
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

plan = {r["P"].replace("P", "R"): r for r in json.loads((HERE / "rows.json").read_text())}
meta = [m for m in json.loads((HERE / "fix_round1_map.json").read_text()) if m["new"]]
crit = json.loads((TASK / "09_Rubrics.json").read_text())
assert [m["new"] for m in meta] == [f"R{i}" for i in range(1, len(crit) + 1)]
grades = json.loads((BASE / "surface_grades.json").read_text())["runs"]
BY_T = {l["ticket"]: l for l in O.BY.values()}
PACK_T = set(BY_T)
HOLDER = {"Brian": "brian", "Claire": "claire", "Calvin": "calvin", "Martin": "martin"}
OWED_KW = {"A1": r"ascii|binary|text (?:kind|format|file)|re-?export|export(?:ed)? again|\.glb|\.blend",
           "A2": r"\bUVs?\b|unwrap|redo|redone",
           "C4": r"re-?upload|re-?zip|put (?:them |it )?back|back in(?:to)? the outgoing|outgoing folder|send .{0,20}again",
           "C2": r"own version|own (?:rocket|explosion)|replacement|made here", "VIS": r"."}
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
    table, brief = [], ""
    sheet_ids, doc_ids = set(), set()
    doc_ev, sheet_ev, posts = [], [], []
    for x in ok:
        ev = int(x["event"])
        if x["tool"] in ("gsheets_values_update", "gsheets_values_append"):
            table += [list(map(str, r)) for r in val(x.get("values")) or []]
            sheet_ev.append(ev)
        if x["tool"] == "gdocs_create_document":
            inp = val(x.get("input")) or {}
            brief += "\n" + (inp.get("bodyText") or "")
            doc_ev.append(ev)
            doc_ids.add(str(x.get("file_id") or ""))
        if x["tool"] == "gdocs_batch_update":
            inp = val(x.get("input")) or {}
            for rq in inp.get("requests", []):
                brief += "\n" + ((rq.get("insertText") or {}).get("text") or "")
            doc_ev.append(ev)
        if x["tool"] == "gsheets_create_spreadsheet":
            sheet_ids.add(x.get("spreadsheet_id"))
        if x["tool"] == "slack_send_message" and x.get("channel") == O.VENDOR_CH:
            posts.append((ev, x.get("text") or ""))
    header = [h.strip().casefold() for h in table[0]] if table else []
    data = {r[0].strip().casefold(): r for r in table[1:] if r}
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
                doc=bool(doc_ev), sheet=bool(sheet_ids), sheet_ids=sheet_ids, doc_ev=doc_ev, sheet_ev=sheet_ev, posts=posts)


def has(text, rx):
    return re.search(rx, text, re.I | re.S) is not None


def cell(v, line, col):
    row = v["data"].get(line.casefold())
    cols = [c.replace("what is owed", "what's owed") for c in v["header"]]
    if not row or col not in cols:
        return None
    i = cols.index(col)
    return row[i].strip() if i < len(row) else ""


def grade_plan(r, v, slots):
    """A reviewed row that kept its meaning (rehearse_rows.grade, with the three changed checks)."""
    tag, b = r["tag"], v["brief"]
    if tag == "move_volume":                       # now a count only: exactly 49 pack tickets in Todo
        return len(v["moved"] & PACK_T) == 49
    if tag == "b_eight_Bow":                       # now the Bow among the eight, whatever happens to Dynamite
        return has(b, r"\bbow\b")
    if r["slot"] and SLOT_TAGS.match(tag):
        return bool(slots.get(r["slot"][0]))
    if tag == "brief_doc":
        return v["doc"]
    if tag == "sheet_doc":
        return v["sheet"]
    if tag in ("b_scenario", "b_purpose", "b_lose", "b_tray", "b_music", "b_start"):
        return bool(slots.get(r["slot"][0]))
    if tag.startswith("b_eight_"):
        return has(b, re.escape(tag[len("b_eight_"):]))
    if tag == "b_extras":
        return has(b, r"swap|extras?\b")
    if tag.startswith("b_zombie_"):
        return has(b, re.escape(tag[len("b_zombie_"):]))
    if tag == "b_anim":
        return has(b, r"\bwalk")
    if tag == "b_win":
        return has(b, r"(eliminat|kill|clear|defeat|destroy)\w*.{0,60}zombie|zombie.{0,60}(eliminat|kill|clear|defeat|destroy)")
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
    if tag.startswith("move_"):
        return re.search(r"DES-\d+", r["title"]).group() in v["moved"]
    if tag.startswith("comment_"):                 # a comment row the report kept whole (the line's own note)
        t = tag[len("comment_"):]
        body = " ".join(v["comments"].get(t, []))
        return bool(body) and has(body, HOLDER[BY_T[t]["who"]])
    if tag.startswith("share_"):
        _, which, who = tag.split("_", 2)
        email = next((e for e in v["shares"] if e and e.split("@")[0].startswith(who.split("@")[0])), None)
        ids = v["shares"].get(email, set())
        return bool(ids - v["sheet_ids"]) if which == "brief" else bool(ids & v["sheet_ids"])
    raise KeyError(tag)


def grade(m, v, slots):
    if m["change"] == "added":
        part = m["part"]
        if part == "state_delivered":
            return (cell(v, "Plushie Chick", "state") or "").casefold() == "delivered"
        if part == "board_empty":
            return cell(v, "Cannon", "board set") == ""
        files, key = (v["doc_ev"], "/document/") if part == "order_brief" else (v["sheet_ev"], "/spreadsheets/")
        linked = [ev for ev, text in v["posts"] if key in text]
        return bool(files) and bool(linked) and max(files) < min(linked)
    r = plan[m["from"]]
    if m["change"] == "split":
        t = r["tag"][len("comment_"):]
        l = BY_T[t]
        body = " ".join(v["comments"].get(t, []))
        if m["part"] == "holder":
            return bool(body) and has(body, HOLDER[l["who"]])
        return bool(body) and has(body, OWED_KW[l["cls"]])
    return grade_plan(r, v, slots)


rollouts = []
for n in range(1, 7):
    g = grades[f"run-{n}"]
    v = run_view(n)
    res = {m["new"]: bool(grade(m, v, g["results"])) for m in meta}
    rollouts.append({"id": f"run-{n}", "status": "completed", "tool_calls": int(g["counted_calls"]), "models": val(g["models"]),
                     "model_source": g.get("model_source") or f"trajectory:run-{n}", "model_check": val(g.get("model_check")),
                     "results": res})
data = {"spec_version": "V3", "difficulty_mode": "hard", "task_type": "long-horizon",
        "rubrics": [{"id": f"R{i}", "weight": c["weight"], "valid": True} for i, c in enumerate(crit, 1)],
        "rollouts": rollouts}
(HERE / "rehearsal_input_round1.json").write_text(json.dumps(data, indent=1) + "\n")
out = stats.compute(data)
tot = sum(c["weight"] for c in crit)
for ro in rollouts:
    passed = sum(c["weight"] for i, c in enumerate(crit, 1) if ro["results"][f"R{i}"])
    failed = [k for k, x in ro["results"].items() if not x]
    print(f"{ro['id']}: {passed}/{tot} = {passed / tot:.1%} · {len(failed)} rows failed · calls {ro['tool_calls']}")
ids = [f"R{i}" for i in range(1, len(crit) + 1)]
always = [k for k in ids if all(ro["results"][k] for ro in rollouts)]
never = [k for k in ids if not any(ro["results"][k] for ro in rollouts)]
print(f"rows passed by all six: {len(always)} (weight {sum(crit[int(k[1:]) - 1]['weight'] for k in always)}) · "
      f"rows failed by all six: {len(never)}: {' '.join(never)}")
view = out["views"]["platform"] if "views" in out else out
print(json.dumps({k: x.get("verdict") + " · " + str(x.get("value")) for k, x in view["gates"].items()
                  if isinstance(x, dict) and "verdict" in x}, indent=1, ensure_ascii=False))
