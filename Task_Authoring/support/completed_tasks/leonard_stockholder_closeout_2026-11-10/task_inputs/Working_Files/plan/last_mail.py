#!/usr/bin/env python3
"""For each holder issue's email, find the latest message in Leonard's mailbox before 2026-02-01 (Pacific) that carries the address in
from/to/cc/bcc. Writes plan/last_mail.json {issue: {address, date_pt, file, pointer}}. Reads only through tools/hg.py search."""
import datetime as D, json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__)); WS = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
PY = os.path.expanduser("~/.local/bin/python3.12")
sys.path.insert(0, HERE)
import importlib.util
spec = importlib.util.spec_from_file_location("bs", os.path.join(HERE, "build_sql.py"))
src = open(os.path.join(HERE, "build_sql.py"), encoding="utf-8").read()
EMAIL = eval(re.search(r"EMAIL = (\{.*?\})\n", src, re.S).group(1))
PT = D.timezone(D.timedelta(hours=-8))
CUT = D.datetime(2026, 2, 1, tzinfo=PT)


def hg(*a):
    r = subprocess.run([PY, "-B", "Task_Authoring/tools/hg.py", "search"] + list(a), cwd=WS, capture_output=True, text=True, timeout=1500)
    try:
        return json.loads(r.stdout)
    except ValueError:
        return {}


def one(item):
    k, addr = item
    d = hg("search", "gmail", addr, "--file", "threads/leonard@harmonygames.co_*.json", "--limit", "50000")
    hits = [m for m in d.get("matches") or [] if "leonard@harmonygames.co_" in str(m.get("file"))]
    msgs = {}
    for m in hits:
        mm = re.match(r"(/messages/\d+)/(from|to|cc|bcc)$", str(m.get("pointer")))
        if mm:
            msgs[(m["file"].split("/gmail/")[-1], mm.group(1))] = 1
    best = None
    for (f, ptr) in msgs:
        g = hg("get", "gmail", "--file", f, "--pointer", ptr + "/date_parsed")
        t = str(g.get("text") or "").strip('"')
        try:
            when = D.datetime.fromisoformat(t)
        except ValueError:
            continue
        if when.tzinfo is None:
            when = when.replace(tzinfo=D.timezone.utc)
        if when < CUT and (best is None or when > best[0]):
            best = (when, f, ptr)
    if not best:
        return k, {"address": addr, "date_pt": None, "headers_hits": len(msgs), "complete": d.get("scan_complete")}
    return k, {"address": addr, "date_pt": best[0].astimezone(PT).date().isoformat(), "file": best[1], "pointer": best[2],
               "headers_hits": len(msgs), "complete": d.get("scan_complete")}


ONLY = set(filter(None, os.environ.get("ONLY", "").split(",")))
old = json.load(open(os.path.join(HERE, "last_mail.json"))) if ONLY and os.path.exists(os.path.join(HERE, "last_mail.json")) else {}
with ThreadPoolExecutor(8) as ex:
    out = dict(old)
    out.update(dict(ex.map(one, sorted((k, v) for k, v in EMAIL.items() if not ONLY or k in ONLY))))
json.dump(out, open(os.path.join(HERE, "last_mail.json"), "w"), indent=1)
for k, v in out.items():
    print(k, v["address"][:24], v["date_pt"], v.get("headers_hits"), v.get("complete"), v.get("file", "")[-40:], v.get("pointer", ""))
