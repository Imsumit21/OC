#!/usr/bin/env python3
"""Fresh base reads for the OE ledger, all through Task_Authoring/tools/hg.py (search lookup / get-many / search).
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
IDS = json.load(open(os.path.join(HERE, "ids.json")))
B = IDS["BASE"]


def hg(*args, timeout=900):
    p = subprocess.run(["python3", "Task_Authoring/tools/hg.py", "search", *args], cwd=WS, env=ENV, capture_output=True, text=True, timeout=timeout)
    if p.returncode:
        sys.stderr.write(p.stderr[-2000:])
    return json.loads(p.stdout)


def lookup(service, ids, file, key, pointer=None):
    f = os.path.join(TMP, f"ids_{service}_{abs(hash(file)) % 10**8}.json")
    json.dump(ids, open(f, "w"))
    args = ["lookup", service, "--ids-file", f, "--file", file, "--key", key, "--compact"]
    if pointer:
        args += ["--pointer", pointer]
    d = hg(*args)
    assert d.get("scan_complete"), (service, file, d.get("errors"))
    return d["matches"]


def get_many(items, max_chars=6000):
    if len(items) > 50:
        out = {}
        for i in range(0, len(items), 50):
            out.update(get_many(items[i:i + 50], max_chars))
        return out
    f = os.path.join(TMP, f"gm_{abs(hash(json.dumps(items))) % 10**8}.json")
    json.dump({"items": [{**it, "max_chars": it.get("max_chars", max_chars)} for it in items]}, open(f, "w"))
    d = hg("get-many", "--request", f)
    out = {}
    for k, r in (d.get("items") or {}).items():
        assert not r.get("truncated"), (k, r.get("pointer"))
        out[k] = {"value": r.get("text"), "truncated": r.get("truncated")}
    return out


SLACK = {k: v for k, v in B.items() if "/" in v and v.split("/")[0][:1] in "CD" and "." in v.split("/")[1]}
need = ["dd_aws_1k", "dd_aws_300", "dd_less_1k", "helpshift_feb28", "figma_sep11", "appsflyer", "checklist", "keep_list", "action_items", "arthur_kub",
        "lifestyle", "auction", "buy_back", "keep_live", "vo_root", "vo_budget", "layer_mar3", "unity_100", "archive_feb15", "boombit_retention",
        "calm_owned", "calm_sub", "repos_llc", "dd_boombit", "dm_ra_root"]
by_chan = {}
for k in need:
    ch, ts = SLACK[k].split("/")
    by_chan.setdefault(ch, []).append((k, ts))
ptr = {}
for ch, lst in by_chan.items():
    m = lookup("slack", [ts for _, ts in lst], f"messages/{ch}/*.json", "ts")
    for k, ts in lst:
        hit = m.get(ts) or []
        assert len(hit) == 1, (k, ts, hit)
        sf = hit[0]["file"].split("/slack/", 1)[1]
        ptr[k] = (sf, hit[0]["pointer"].rsplit("/", 1)[0])
slack = get_many([{"id": k, "service": "slack", "file": f, "pointer": p} for k, (f, p) in ptr.items()])
OUT = {"slack": {}, "ptr": ptr}
for k, r in slack.items():
    v = r.get("value") or r.get("data") or r.get("text")
    if isinstance(v, str):
        try:
            v = json.loads(v)
        except Exception:
            pass
    OUT["slack"][k] = {"file": ptr[k][0], "pointer": ptr[k][1], "rec": v, "truncated": r.get("truncated")}

# Snowflake REVENUE_DAILY (table 12) January 2026 rows, by position (rows 2044..2229 from the complete date search)
sf_items = [{"id": f"r{n}", "service": "snowflake", "file": "snowflake.json", "pointer": f"/tables/12/rows/{n}", "max_chars": 800} for n in range(2040, 2234)]
sf = get_many(sf_items)
rows = {}
for k, r in sf.items():
    v = r.get("value") or r.get("data") or r.get("text")
    if isinstance(v, str):
        v = json.loads(v)
    rows[int(k[1:])] = v
OUT["revenue_rows"] = rows
tname = get_many([{"id": "t12", "service": "snowflake", "file": "snowflake.json", "pointer": "/tables/12/name", "max_chars": 200},
                  {"id": "t12s", "service": "snowflake", "file": "snowflake.json", "pointer": "/tables/12/schema", "max_chars": 200},
                  {"id": "t12d", "service": "snowflake", "file": "snowflake.json", "pointer": "/tables/12/database", "max_chars": 200}])
OUT["revenue_table"] = {k: (v.get("value") or v.get("data") or v.get("text")) for k, v in tname.items()}

# Drive root, contacts, Linear users, Confluence page
g = lookup("gdrive", ["d_9f7ba94f7526d54d8482ba"], "data.json", "id", "/drive_files")
gp = g["d_9f7ba94f7526d54d8482ba"][0]["pointer"].rsplit("/", 1)[0]
lu = lookup("linear", ["usr_63fffeb4fab5233e", "usr_cc3e90160f490686"], "data.json", "id", "/users")
rob = hg("search", "linear", "robert@harmonygames.co", "--limit", "5")
rob_ptr = [m["parent_pointer"] for m in rob["matches"] if m["pointer"].startswith("/users/")]
items = [{"id": "root", "service": "gdrive", "file": "data.json", "pointer": gp, "max_chars": 2000},
         {"id": "c_leonard", "service": "contacts", "file": "contacts.json", "pointer": "/contacts/169", "max_chars": 2000},
         {"id": "c_arthur", "service": "contacts", "file": "contacts.json", "pointer": "/contacts/168", "max_chars": 2000},
         {"id": "u_leonard", "service": "linear", "file": "data.json", "pointer": lu["usr_63fffeb4fab5233e"][0]["pointer"].rsplit("/", 1)[0], "max_chars": 1500},
         {"id": "u_arthur", "service": "linear", "file": "data.json", "pointer": lu["usr_cc3e90160f490686"][0]["pointer"].rsplit("/", 1)[0], "max_chars": 1500},
         {"id": "aws_page", "service": "confluence", "file": "confluence_working.json", "pointer": "/pages/2", "max_chars": 12000}]
if rob_ptr:
    items.append({"id": "u_robert", "service": "linear", "file": "data.json", "pointer": rob_ptr[0], "max_chars": 1500})
misc = get_many(items)
OUT["misc"] = {}
for k, r in misc.items():
    v = r.get("value") or r.get("data") or r.get("text")
    if isinstance(v, str):
        try:
            v = json.loads(v)
        except Exception:
            pass
    OUT["misc"][k] = {"pointer": next(i["pointer"] for i in items if i["id"] == k), "rec": v, "truncated": r.get("truncated")}

# Linear workflow states of team ENG
st = hg("search", "linear", "team_ENG", "--limit", "60")
OUT["linear_state_hits"] = [m for m in st["matches"] if "state" in m["pointer"]][:40]
json.dump(OUT, open(os.path.join(HERE, "oe_base.json"), "w"), indent=1, default=str)
print("slack", len(OUT["slack"]), "revenue rows", len(rows), "misc", sorted(OUT["misc"]), "state hits", len(OUT["linear_state_hits"]))
