import json, re, statistics, collections
rows = json.load(open("/Users/sumitkumar/Source/Outlier/OC/Task_Authoring/task_inputs/Working_Files/rubric/rows.json"))
res = json.load(open("/tmp/rubricwork/writes_all.json"))
KEYRX = re.compile(r"\b(?:ZOM|ART|DES)-\d+\b")


def grade(v):
    tabs, reg, z570, creates, slack = [], [], "", [], []
    for w in v["writes"]:
        t, i = w["tool"], w["input"] or {}
        if t == "gsheets_batch_update":
            tabs += [r["addSheet"]["properties"]["title"] for r in i.get("requests", []) if "addSheet" in r]
        elif t in ("gsheets_values_update", "gsheets_values_append"):
            reg += i.get("values") or []
        elif t == "linear_update_issue" and i.get("id") == "ZOM-570":
            z570 += " ".join(p.get("text", "") for p in i.get("patch", [])) + (i.get("description") or "")
        elif t == "linear_create_issue":
            creates.append(i)
        elif t == "slack_send_message":
            slack.append(i)
    data = {str(r[0]).strip(): r for r in reg if r and KEYRX.fullmatch(str(r[0]).strip())}
    newkey = "ZOM-581"
    out = {}
    blockers_listed = set(KEYRX.findall(z570))
    for r in rows:
        tag = r["tag"]
        ok = None
        if tag == "tab":
            ok = len(tabs) == 1
        elif tag == "regonly":
            ok = True
        elif tag == "z_only":
            ok = bool(z570)
        elif tag == "s_time":
            ok = bool(slack)
        elif tag == "tabname":
            ok = bool(tabs) and "135" in tabs[0] and "50" in tabs[0]
        elif tag == "count133":
            ok = len(data) == 133 and not ({"ZOM-570","ZOM-359","ZOM-475"} & set(data))
        elif tag.startswith(("reg_", "fix_", "smp_")):
            key = r["vals"].split("`")[1] if tag != "reg_new" else newkey
            call = "BLOCKER" if tag.startswith("reg_") else r["vals"].split("`")[3]
            ok = key in data and str(data[key][4]).strip().upper() == call
        elif tag.startswith("bs_"):
            key, val = r["vals"].split("`")[1], r["vals"].split("`")[3]
            ok = key in data and str(data[key][2]).strip().lower() == val
        elif tag == "title_546":
            ok = "ZOM-546" in data and "refill algorithm spawns fewer items" in str(data["ZOM-546"][1]).lower()
        elif tag == "qa_449":
            ok = "ZOM-449" in data and re.search(r"repro|froze|fail|still", str(data["ZOM-449"][3]), re.I) is not None
        elif tag == "qa_559":
            ok = "ZOM-559" in data and "victory" in str(data["ZOM-559"][3]).lower()
        elif tag == "ev_435":
            ok = "ZOM-435" in data and re.search(r"68dc63484a5b2d0a869e758f|68d1eb90bef538c7c5c5599d|pTbZYXdb", str(data["ZOM-435"][5])) is not None
        elif tag == "ev_562":
            ok = "ZOM-562" in data and re.search(r"1844730396672762606|CAMqj9qx|mail\.google", str(data["ZOM-562"][5])) is not None
        elif tag == "z_keep":
            ok = bool(z570)  # all runs appended (patch append / insert_before)
        elif tag == "z_count":
            ok = len(blockers_listed - {"ZOM-570"}) == 19
        elif tag == "z_new":
            ok = newkey in blockers_listed
        elif tag.startswith("z_"):
            key = r["vals"].strip("`")
            ok = key in blockers_listed
        elif tag == "new_issue":
            ok = len(creates) >= 1 and "N-1" in json.dumps(creates[0]) and "level 1" in json.dumps(creates[0])
        elif tag == "new_device":
            ok = len(creates) >= 1 and "iPhone 13" in json.dumps(creates[0])
        elif tag == "new_os":
            ok = len(creates) >= 1 and "iOS 18.6" in json.dumps(creates[0])
        elif tag == "new_repro":
            ok = len(creates) >= 1 and "level 200" in json.dumps(creates[0]) and re.search(r"[Ll]aunch", json.dumps(creates[0])) is not None
        elif tag == "new_one":
            ok = len(creates) == 1
        elif tag == "s_thread":
            ok = bool(slack) and all(s.get("thread_ts") == "1759263900.484190" for s in slack)
        elif tag == "s_call":
            ok = any(re.search(r"no-go|not ready", s.get("message", "") or s.get("text", ""), re.I) for s in slack)
        out[tag] = ok
    return out


tw = sum(r["w"] for r in rows)
scores, fails = {}, collections.Counter()
for p, v in res.items():
    g = grade(v)
    s = sum(r["w"] for r in rows if g[r["tag"]]) / tw
    scores[p] = s
    for t, ok in g.items():
        if not ok:
            fails[t] += 1
    print(f"{s:.3f}", p, [t for t, ok in g.items() if not ok])
vals = [scores[p] for p in scores if "PreCheck" not in p]
print("mean", round(statistics.mean(vals), 3), "pstdev", round(statistics.pstdev(vals), 3), "n", len(vals))
print("fail counts:", dict(fails))
