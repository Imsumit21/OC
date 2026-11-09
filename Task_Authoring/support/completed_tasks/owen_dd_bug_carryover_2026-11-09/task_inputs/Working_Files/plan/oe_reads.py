#!/usr/bin/env python3
"""Fresh base reads for the OE ledger (owen_dd_bug_carryover, rev9), all through Task_Authoring/tools/hg.py.
Writes plan/oe_base.json. Never reads the universe JSON directly."""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
ENV = {**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"}
TMP = os.path.join(HERE, "oe_tmp")
os.makedirs(TMP, exist_ok=True)


def hg(*args, timeout=900):
    p = subprocess.run(["python3", "Task_Authoring/tools/hg.py", "search", *args], cwd=WS, env=ENV, capture_output=True, text=True, timeout=timeout)
    if p.returncode:
        sys.stderr.write(p.stderr[-2000:])
    return json.loads(p.stdout)


def whole(service, file):
    """Read a whole JSON file by paging the root pointer."""
    out, off = [], 0
    while True:
        d = hg("get", service, "--file", file, "--pointer", "", "--offset", str(off), "--max-chars", "400000", "--compact")
        out.append(d["text"])
        if not d.get("truncated"):
            break
        off = d["next_offset"]
    return json.loads("".join(out))


def lookup(service, ids, file, key, pointer=None):
    f = os.path.join(TMP, f"ids_{service}_{abs(hash((file, pointer, key))) % 10**8}.json")
    json.dump(ids, open(f, "w"))
    args = ["lookup", service, "--ids-file", f, "--file", file, "--key", key, "--compact"]
    if pointer:
        args += ["--pointer", pointer]
    d = hg(*args)
    assert d.get("scan_complete"), (service, file, d.get("errors"))
    return d["matches"]


def get_many(items, max_chars=20000):
    if len(items) > 25:
        out = {}
        for i in range(0, len(items), 25):
            out.update(get_many(items[i:i + 25], max_chars))
        return out
    f = os.path.join(TMP, f"gm_{abs(hash(json.dumps(items))) % 10**8}.json")
    json.dump({"items": [{**it, "max_chars": it.get("max_chars", max_chars)} for it in items]}, open(f, "w"))
    d = hg("get-many", "--request", f)
    out = {}
    for k, r in (d.get("items") or {}).items():
        assert not r.get("truncated"), (k, r.get("pointer"))
        v = r.get("text")
        try:
            v = json.loads(v)
        except Exception:
            pass
        out[k] = v
    return out


def records(service, file, key, ids, pointer):
    m = lookup(service, ids, file, key, pointer)
    items = []
    for i in ids:
        hit = m.get(i) or []
        assert hit, (service, i)
        items.append({"id": i, "service": service, "file": file, "pointer": hit[0]["pointer"].rsplit("/", 1)[0]})
    got = get_many(items)
    return {i: {"file": file, "pointer": it["pointer"], "rec": got[i]} for i, it in zip(ids, items)}


OUT = {"slack_files": {}, "slack": {}, "linear": {}, "github": {}, "contacts": {}, "gdocs": {}}
# whole message files: the canvas comment channel and the bug channel from Nov 2025 on
for f in ["messages/CE156FDFB428/2025-11.json", "messages/C05V5FNLB9V/2025-11.json", "messages/C05V5FNLB9V/2025-12.json", "messages/C05V5FNLB9V/2026-02.json"]:
    OUT["slack_files"][f] = whole("slack", f)
    print(f, len(OUT["slack_files"][f]), file=sys.stderr)
# single base messages in other channels
SINGLE = {"C09SWTHEMEW": ["1764659626.614679", "1770926214.816149"], "C9CA62B5180A": ["1764721779.638599", "1765927350.212199", "1765927876.696389", "1765928003.630799", "1765933143.608699"], "D07E9PSQB6W": ["1763585860.227679"],
          "C09Q4S613CN": ["1764013026.858409", "1764042435.541279", "1764013100.931229"], "C05433XK267": ["1765310004.760809", "1765310444.095399", "1765397569.397939"], "C050WGU41HR": ["1764694580.083459"]}
for ch, tss in SINGLE.items():
    m = lookup("slack", tss, f"messages/{ch}/*.json", "ts")
    items = []
    for ts in tss:
        hit = m.get(ts) or []
        assert len(hit) == 1, (ch, ts, hit)
        sf = hit[0]["file"].split("/slack/", 1)[1]
        items.append({"id": f"{ch}/{ts}", "service": "slack", "file": sf, "pointer": hit[0]["pointer"].rsplit("/", 1)[0]})
    got = get_many(items)
    for it in items:
        OUT["slack"][it["id"]] = {"file": it["file"], "pointer": it["pointer"], "rec": got[it["id"]]}
# Linear issues: the master, its three groups, the 28 children and the two reused tickets
LIN = ["ENG-2401", "ENG-2403", "ENG-2404", "ENG-2405", "ENG-2073", "ENG-2363", "ENG-2406", "ENG-2181", "ENG-2351", "ENG-2280", "ENG-2281", "ENG-2398"] + [f"ENG-{n}" for n in range(2409, 2438) if n != 2436]
m = lookup("linear", LIN, "data.json", "id", "/issues")
FIELDS = ["id", "title", "state_id", "parent_id", "team_id", "labels", "assignee_id", "completed_at", "updated_at"]
items = []
for i in LIN:
    base = m[i][0]["pointer"].rsplit("/", 1)[0]
    items += [{"id": f"{i}|{f}", "service": "linear", "file": "data.json", "pointer": f"{base}/{f}", "max_chars": 2000} for f in FIELDS]
got = get_many(items)
for i in LIN:
    OUT["linear"][i] = {"file": "data.json", "pointer": m[i][0]["pointer"].rsplit("/", 1)[0], "rec": {f: got[f"{i}|{f}"] for f in FIELDS}}
# GitHub: the open window PR, the two reviewed PRs and the economy-line PR
GH = ["harmonygames-Games/GameOfDominoes#1913", "harmonygames-Games/GameOfDominoes#1905", "harmonygames-Games/GameOfDominoes#1908", "harmonygames-Games/GameOfDominoes#1916"]
OUT["github"] = records("github", "data.json", "id", GH, "/pull_requests")
OUT["commit_merge"] = get_many([{"id": "c", "service": "github", "file": "data.json", "pointer": "/commits/252"}])["c"]
# Contacts for the three people on the review
OUT["contacts"] = records("contacts", "contacts.json", "email", ["arthur.blake@harmonygames.co", "robert@harmonygames.co", "oliver.brooks@harmonygames.co"], "/contacts")
# the economy doc
OUT["gdocs"] = records("gdocs", "data.json", "document_id", ["f_948768f5a462e7037d17c9"], "/docs_documents")
json.dump(OUT, open(os.path.join(HERE, "oe_base.json"), "w"), indent=1, ensure_ascii=False)
print("ok", {k: len(v) for k, v in OUT.items() if isinstance(v, dict)})
