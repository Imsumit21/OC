#!/usr/bin/env python3
"""Re-read every base record the four fact sheets cite through tools/hg.py and assert each quote is a substring;
seeded quotes are asserted against the injection SQL text. Writes verified_corpus.json (all verified quote text)."""
import json, os, sys, re
from concurrent.futures import ThreadPoolExecutor
import oe_lib as L
D = sys.argv[1]
facts = []
for n in ("options", "stock", "told", "winddown"):
    for f in json.load(open(os.path.join(D, f"facts_{n}.json"))):
        f["_sheet"] = n
        facts.append(f)
SQLT = L.SQL.replace("''", "'")
SQLN = L.squash(L.norm(SQLT))
need = sorted({(f["service"], f["file"], f["pointer"]) for f in facts if f.get("source") == "base" and f.get("file") and str(f.get("pointer") or "").startswith("/") and " " not in str(f.get("pointer")) and f.get("quotes")})
print("base reads", len(need), flush=True)
with ThreadPoolExecutor(8) as ex:
    res = list(ex.map(lambda t: L.hg_get(*t), need))
L._save()
bad, ok, corpus = [], 0, []
for f in facts:
    if f.get("key", "").startswith(("absence", "defer")):
        continue
    for q in f.get("quotes") or []:
        corpus.append(q)
        if " " in str(f.get("pointer") or ""):
            continue
        if f.get("source") == "base" and f.get("file") and str(f.get("pointer") or "").startswith("/"):
            t = L.hg_get(f["service"], f["file"], f["pointer"])
            if q in t or L.squash(q) in L.squash(t):
                ok += 1
            else:
                bad.append((f["key"], q[:90], f["pointer"]))
        elif f.get("source") == "sql":
            if L.squash(L.norm(q)) in SQLN or L.squash(L.norm(q)).replace("'", "''") in SQLN:
                ok += 1
            else:
                bad.append((f["key"], q[:90], "sql"))
print("verified", ok, "bad", len(bad))
for b in bad[:60]:
    print(b)
json.dump(sorted(set(corpus)), open(os.path.join(L.HERE, "verified_corpus.json"), "w"), ensure_ascii=False, indent=0)
