#!/usr/bin/env python3
"""rev9 baselines: every write payload per run (format, shares, sheet, reply result) and which seeded records each run's tool results contain."""
import json, sys, re, os, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from behaviour import calls
PROBES = {"brian_popups": "never got back to the two popups", "brian_gift": "Daily Gift isn", "brian_music": None,
          "brian_shop_dec1": "trust that tick", "marcus_tavern": "lost their frame again", "vincent_mail": "sign in lines on my list",
          "vincent_apple_text": "same sync problem as ENG-2073", "tooltips_reply": "1 pixel gap is gone", "oliver_note": None}
def run(lab, p):
    cs = calls(p)
    blob = "\n".join(r for *_, r in cs).replace("\\n", " ").replace("\\u2019", "’").replace("\\'", "'")
    cr = [i for _, n, i, r in cs if n == "linear_create_issue"]
    keys = collections.Counter(tuple(sorted(k for k in i if i[k] not in (None, "", []))) for i in cr)
    nopre = [i.get("title", "")[:50] for i in cr if not i.get("title", "").startswith("[2231] ")]
    lab_ = collections.Counter(json.dumps(i.get("labels") or i.get("labelIds")) for i in cr)
    par = collections.Counter(i.get("parentId") or i.get("parent") for i in cr)
    com = [(i.get("issueId") or i.get("id"), i.get("body", "")) for _, n, i, r in cs if n == "linear_create_comment"]
    shares = [(json.dumps({k: v for k, v in i.items() if k != "fileId"})[:120], r[:80]) for _, n, i, r in cs if "share" in n or "permission" in n]
    drive = [(n, json.dumps(i)[:200], r[:150]) for _, n, i, r in cs if n.startswith(("gdrive_create", "gsheets_create", "gdrive_move", "gdrive_update"))]
    sheet = [(n, i) for _, n, i, r in cs if n.startswith("gsheets") and ("update" in n or "append" in n or "write" in n or "batch" in n)]
    rows = []
    for n, i in sheet:
        v = i.get("values") or (i.get("data") or [{}])[0].get("values") if isinstance(i.get("data"), list) else i.get("values")
        if v: rows += v
    rep = [(i.get("channel_id"), r[:160]) for _, n, i, r in cs if n == "slack_send_message"]
    tools = collections.Counter(n for _, n, i, r in cs)
    gh = sorted(n for n in tools if n.startswith("github"))
    exp = {k: (v in blob if v else None) for k, v in PROBES.items()}
    print(f"\n===== {lab}: {len(cs)} calls; creates {len(cr)}; create-key sets {dict(keys)}; labels {dict(lab_)}; parents {dict(par)}")
    print("  titles without '[2231] ':", nopre[:5])
    print("  comments:", len(com), "targets:", collections.Counter(re.sub(r'\d$', 'x', str(t)) for t, b in com), "ENG-2073" in [t for t, b in com], "ENG-2363" in [t for t, b in com])
    print("  shares:", shares)
    print("  drive:", drive)
    print("  sheet rows:", len(rows), "header:", rows[:1], "outcome counts:", collections.Counter((r[1] if len(r) > 1 else None) for r in rows[1:]))
    print("  reply:", rep)
    print("  github tools:", {n: tools[n] for n in gh}, " gmail:", {n: tools[n] for n in tools if n.startswith("gmail")})
    print("  exposure:", exp)
for a in sys.argv[1:]:
    l, p = a.split("=", 1); run(l, p)
