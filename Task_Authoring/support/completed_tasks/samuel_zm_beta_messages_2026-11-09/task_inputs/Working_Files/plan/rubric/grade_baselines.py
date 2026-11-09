#!/usr/bin/env python3
"""Advisory local grade of the six rev6 baselines (and the pre-check) against rows.json. The verifier is the grading of record.
Reads raw write payloads through run_forensics/rev6/baseline/fair_regrade/facts.py; each row is judged on its own target."""
import collections
import json
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
sys.argv = ["x", str(WF / "run_forensics/rev6/baseline/fair_regrade")]
sys.path.insert(0, sys.argv[1])
sys.path.insert(0, str(WF.parents[1] / "tools"))
from facts import facts, FILES, FOLDER  # noqa: E402
import difficulty_stats as ds  # noqa: E402

ROWS = json.loads((HERE / "rows.json").read_text())
TRUTH = {k: v for k, v in json.loads((WF / "solver/truth.json").read_text()).items() if isinstance(v, dict) and v.get("Call")}
RUNS = [f"run-{i}" for i in range(1, 7)]
FA = {l: facts(FILES[l]) for l in FILES}
HEADER = ["Message", "Ticket", "Call", "What's missing", "Audience", "Final headline", "String change"]
WRITES = {"gsheets_values_update", "gsheets_create_spreadsheet", "gdocs_create_document", "gdocs_batch_update", "linear_create_comment", "linear_update_issue",
          "linear_create_issue", "trello_create_checklist", "trello_create_check_item", "gmail_send_message", "gdrive_move_file", "gdrive_create_file"}
DMT = ("slack_send_message", "slack_conversations_add_message")


def tag(name):
    return name.lower().replace("&", "and").replace("'", "").replace(" ", "_")


BYTAG = {tag(k): k for k in TRUTH}
EXIST = {v["Ticket"] for v in TRUTH.values() if v["Ticket"]}
WHY = {"Lives recharged": r"test ?6|tick|0\.3\.49|both", "Plague Race": r"test ?6|5-minute|timer|never showed|both|ios",
       "Weekly Leaderboard reset": r"test ?5|wrong day|last session|reset day", "Finish first mission": r"test ?4|reach|below level 20|our own|permission ask"}
SEC = re.compile(r"(?is)(already (?:scheduled|schedules?)[^\n]*(?:hold|still)|still (?:a )?hold|built but held|schedules? (?:but|and) (?:is )?(?:still|held)|built.*(?:hold|held))")


def rowv(F, name):
    return F["rows"].get(TRUTH[name]["Ticket"] or "", {})


def first_call(F, k):
    for b in F["comments"].get(k, []):
        m = re.search(r"\b(Go|Hold|Drop)\b", b)
        if m:
            return m.group(1)
    return None


def hold_section(F):
    n = F["note"]
    m = SEC.search(n)
    return n[m.start():] if m else ""


def holds_listed(F):
    h = re.split(r"(?i)\n\s*(?:\d[.)]\s*)?(?:totals?|counts?|calls)\b", hold_section(F))[0]
    return [k for k in ("Lives recharged", "Plague Race", "Weekly Leaderboard", "Finish first mission") if re.search(k.split()[0] + r"\b.*", h, re.I) and k.split()[0].lower() in h.lower()], h


def mail_body(F, addr):
    return "\n".join(str(m.get("body")) for m in F["mails"] if addr in " ".join(m.get("to") or []))


def mail_says(F, addr, name):
    k = TRUTH[name]["Ticket"]
    c = TRUTH[name]["Call"]
    word = r"\bHold\b|\bheld\b|\bhold\b" if c == "Hold" else r"\bDrop\b|\bdropped\b|\bcancel"
    toks = [re.escape(k)] if k else []
    toks.append(re.escape(name.split(" (")[0]))
    toks.append(re.escape(" ".join(name.split()[:2])))
    for line in re.split(r"\n", mail_body(F, addr)):
        if any(re.search(t, line, re.I) for t in toks) and re.search(word, line, re.I):
            return True
    return False


def judge(F, r):
    t = r["tag"]
    if t == "sheet_folder":
        return F["parents"].get(F["sheet"]) == FOLDER
    if t == "sheet_header":
        for c in F["calls"]:
            if c["tool"] == "gsheets_values_update" and isinstance(c["input"].get("values"), list) and c["input"]["values"]:
                return [str(x).strip().lower() for x in c["input"]["values"][0]][:7] == [h.lower() for h in HEADER]
        return False
    if t == "sheet_rows":
        return len(F["rows"]) == 36
    if t == "msg_lapsed_1_day":
        return bool(re.search(r"(?i)lapsed 1|24 hours", F["rows"].get("DES-316", {}).get("Message", "")))
    if t == "tally_go":
        return sum(1 for v in F["rows"].values() if v["Call"].strip().lower() == "go") == 2
    if t.startswith("un_"):
        u = F["upd"].get("DES-" + t[6:])
        return bool(u) and u.get("assignee") is None
    if t.startswith("call_"):
        n = BYTAG[t[5:]]
        return rowv(F, n).get("Call", "").strip().lower() == TRUTH[n]["Call"].lower()
    if t.startswith("miss_"):
        n = BYTAG[t[5:]]
        m = rowv(F, n).get("Miss", "")
        if n in WHY:
            return bool(re.search(WHY[n], m, re.I))
        if n == "Lapsed 14 days":
            return bool(re.search(r"lapsed 7|DES-317|weekly", m, re.I))
        return bool(re.search({"needs a server send": r"test ?2|server", "not scheduled in the client": r"test ?3|schedul"}[TRUTH[n]["What's missing"]], m, re.I)) and bool(m)
    if t.startswith("aud_"):
        n = BYTAG[t[4:]]
        return bool(TRUTH[n]["Ticket"]) and re.sub(r"\W", "", TRUTH[n]["Audience"].lower()) in re.sub(r"\W", "", rowv(F, n).get("Aud", "").lower())
    if t.startswith("ticket_"):
        n = {"wc": "Win & Collect start"}.get(t[7:]) or BYTAG[t[7:]]
        return bool(TRUTH[n]["Ticket"]) and bool(rowv(F, n))
    if t == "head_l7":
        return "your squad is waiting" in F["rows"].get("DES-317", {}).get("Head", "").lower()
    if t == "head_l1":
        return "horde is growing" in F["rows"].get("DES-316", {}).get("Head", "").lower()
    if t == "str_l7":
        return bool(re.match(r"(?i)\s*(yes|DES-\d)", F["rows"].get("DES-317", {}).get("Str", "")))
    if t == "str_l1":
        return re.match(r"(?i)\s*(no|none|unchanged)\b", F["rows"].get("DES-316", {}).get("Str", "")) is not None
    if t in ("head_count", "str_count"):
        col = "Head" if t == "head_count" else "Str"
        filled = [v for v in F["rows"].values() if v[col].strip() and v[col].strip().lower() not in ("n/a", "na", "-", "—", "–")]
        return bool(filled) and all(v["Call"].strip().lower() == "go" for v in filled)
    if t == "note_folder":
        return len([p for p in F["parents"].values() if p == FOLDER]) >= 2
    if t == "note_page":
        return 0 < len(F["note"].split()) <= 750
    if t == "note_first":
        a = re.search(r"\bD1\b", F["note"])
        b = re.search(r"(?i)day 1\b|lapsed reminders", F["note"])
        c = SEC.search(F["note"])
        return bool(a and b and c and a.start() < b.start() < c.start())
    m = re.match(r"note_(ios|android)_(d1|d7)$", t)
    if m:
        v = {("ios", "d1"): r"31\.(65|7|6)\b", ("ios", "d7"): r"9\.(28|3)\b", ("android", "d1"): r"37\.(86|9)\b", ("android", "d7"): r"10\.(68|7)\b"}[(m.group(1), m.group(2))]
        return bool(re.search(v, F["note"]))
    if t == "note_ladder":
        return all(re.search(rf"(?<![\d.]){d}(?![\d.])", F["note"]) for d in (1, 7, 14, 21, 28)) and bool(re.search(r"(?i)\bday", F["note"]))
    if t.startswith("nhn_"):
        n = BYTAG[t[4:]]
        names, h = holds_listed(F)
        return n.split()[0].lower() in h.lower() and rowv(F, n).get("Call", "").strip().lower() == "hold"
    if t.startswith("nh_"):
        n = BYTAG[t[3:]]
        names, h = holds_listed(F)
        key = n.split()[0]
        seg = [l for l in h.split("\n") if key.lower() in l.lower()]
        return bool(seg) and any(re.search(WHY[n], l, re.I) for l in seg) and TRUTH[n]["Call"] == "Hold" and rowv(F, n).get("Call", "").strip().lower() == "hold"
    if t == "note_count":
        names, h = holds_listed(F)
        return len(names) == 4
    if t.startswith("cm_"):
        if t == "cm_count":
            return sum(1 for k in EXIST if first_call(F, k)) == 32 and not [k for k in F["comments"] if k not in EXIST and not k.startswith("DES-3") and first_call(F, k)]
        n = BYTAG[t[3:]]
        k = TRUTH[n]["Ticket"]
        return bool(k) and first_call(F, k) == TRUTH[n]["Call"]
    if t.startswith("mv_"):
        if t == "mv_backlog":
            return sum(1 for k, u in F["upd"].items() if k in EXIST and str(u.get("state")).lower() == "backlog") == 24
        if t == "mv_cancel":
            return sum(1 for k, u in F["upd"].items() if k in EXIST and str(u.get("state")).lower() == "canceled") == 6
        if t == "mv_unassign":
            return sum(1 for k, u in F["upd"].items() if k in EXIST and u.get("assignee") is None) == 24
        if t == "mv_total":
            new = {m.group(0) for c in F["calls"] if c["tool"] == "linear_create_issue" for m in re.finditer(r"DES-\d+", str(c["result"]))}
            return sum(1 for k in F["upd"] if k in EXIST or k not in new) == 30
        n = BYTAG[t[3:]]
        u = F["upd"].get(TRUTH[n]["Ticket"])
        want = "canceled" if TRUTH[n]["Call"] == "Drop" else "backlog"
        return bool(u) and str(u.get("state")).lower() == want
    if t == "new_string":
        return any("Your Squad Is Waiting" in (i.get("title", "") + " " + i.get("description", "")) and i.get("parentId") == "DES-314" for i in F["new"])
    if t == "new_count":
        return len(F["new"]) == 5
    if t.startswith(("newb_", "newu_")):
        return False
    if t.startswith("new_"):
        return False if BYTAG[t[4:]] else False
    if t.startswith("chk_"):
        if t == "chk_count":
            return len(F["checks"]) == 2
        n = BYTAG[t[4:]]
        return any(n.lower() in c.lower() or TRUTH[n]["Ticket"] in c for c in F["checks"])
    if t.startswith("em_"):
        if t == "em_count":
            return len({a for m in F["mails"] for a in (m.get("to") or [])}) == 8
        p, rest = t[3:].split("_", 1)
        addr = {"brian": "brian.foster@", "calvin": "calvin.price@", "douglas": "douglas@", "julia": "julia.lawson@", "martin": "martin.walsh@", "oliver": "oliver.brooks@", "owen": "owen.baker@", "robert": "robert@"}[p]
        n = BYTAG[rest]
        return bool(TRUTH[n]["Ticket"]) and mail_says(F, addr, n)
    if t.startswith("dm_"):
        c = t[3:].capitalize()
        n = {"Go": 2, "Hold": 28, "Drop": 6}[c]
        return bool(re.search(rf"\b{c}:? {n}\b|\b{n} {c}\b", F["dm"].replace("*", ""), re.I))
    if t == "order_dm":
        idx = [i for i, c in enumerate(F["calls"]) if c["tool"] in DMT]
        wr = [i for i, c in enumerate(F["calls"]) if c["tool"] in WRITES]
        return bool(idx) and max(wr) < max(idx)
    raise KeyError(t)


def grade(labs):
    return {l: {r["tag"]: bool(judge(FA[l], r)) for r in ROWS} for l in labs}


def score(res):
    W = sum(r["w"] for r in ROWS)
    return sum(r["w"] for r in ROWS if res[r["tag"]]) / W


if __name__ == "__main__":
    G = grade(RUNS)
    sc = [score(G[l]) for l in RUNS]
    W = sum(r["w"] for r in ROWS)
    print("rows", len(ROWS), "weight", W)
    print("scores", [round(x * 100, 1) for x in sc], "mean", round(statistics.mean(sc) * 100, 1), "popSD", round(statistics.pstdev(sc), 3), "pass rows", [sum(G[l].values()) for l in RUNS])
    P = grade(["precheck"])
    print("precheck", round(score(P["precheck"]) * 100, 1))
    allfail = [r for r in ROWS if not any(G[l][r["tag"]] for l in RUNS)]
    print("all-fail rows", len(allfail), "weight", sum(r["w"] for r in allfail), [r["tag"] for r in allfail])
    pat = collections.Counter(tuple(sorted(t for t, v in G[l].items() if not v)) for l in RUNS)
    print("patterns", len(pat), "largest", max(pat.values()) / len(RUNS))
    vary = [(r["tag"], r["w"], "".join("P" if G[l][r["tag"]] else "." for l in RUNS)) for r in ROWS if 0 < sum(G[l][r["tag"]] for l in RUNS) < 6]
    print("varying rows", len(vary))
    for x in vary:
        print("  ", x)
    data = dict(spec_version="V3", difficulty_mode="medium", task_type="long-horizon", rubrics=[dict(id=r["tag"], weight=r["w"], valid=True) for r in ROWS],
                rollouts=[dict(id=l, status="completed", tool_calls=len(FA[l]["calls"]), models=["claude-opus-5-5"], model_source="trajectory", results=G[l]) for l in RUNS])
    json.dump({"grades": G, "scores": sc}, open(HERE / "local_grade.json", "w"), indent=0)
    d = ds.compute(data)
    print(json.dumps(d)[:1200])
