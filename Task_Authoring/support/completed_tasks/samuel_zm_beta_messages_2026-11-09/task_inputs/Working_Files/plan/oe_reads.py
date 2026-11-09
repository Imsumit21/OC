#!/usr/bin/env python3
"""Base reads for the OE ledger. Every universe read goes through tools/hg.py (oe_hg.py); persona searches go through
tools/persona_view.py. Writes plan/oe_base.json. Nothing here reads the universe folders directly."""
import json, os, re, subprocess, sys, time
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from oe_hg import hg, get, find, many, WS, ENV
O = {}
def jl(x):
    try: return json.loads(x)
    except Exception: return None
# ---- Slack base records
def slack(cid, ts):
    f = f"messages/{cid}/{time.strftime('%Y-%m', time.gmtime(float(ts)))}.json"
    ms = [m for m in find("slack", ts, f, 6).get("matches", []) if m["pointer"].endswith("/ts")]
    if not ms: return {"error": "not found", "file": f}
    return {"file": f, "pointer": ms[0]["parent_pointer"], "rec": jl(get("slack", f, ms[0]["parent_pointer"], 6000)["text"])}
O["slack"] = {k: slack(*v) for k, v in dict(
    versions=("C0880U9751A", "1758643365.607149"), axe=("C05KNDCHAAG", "1758558164.541689"), scope=("C05KNDCHAAG", "1757704290.799329"),
    shove=("D06KPMDV2JZ", "1752162738.497679"), variantc=("C08R27X0EAH", "1755084279.518809"), beginning=("C08R27X0EAH", "1758291802.756889"),
    martin=("C08R8CHB0QL", "1759159849.386619"), android=("D06UFE81RF0", "1759163970.141449"), ios_release=("C0880U9751A", "1759182908.627389")).items()}
# ---- Confluence
O["liveops"] = jl(get("confluence", "confluence_working.json", "/pages/27", 30000)["text"])
# ---- GitHub
pr = find("github", "harmonygames-Games/match3d#248", "data.json", 3)
O["pr"] = jl(get("github", "data.json", "/pull_requests/2128", 8000)["text"])
O["hunk"] = jl(get("github", "data.json", "/review_comments/599", 60000)["text"])
O["client_file"] = hg("files", "github", "match3d/Assets/Scripts/Notifications/NotificationManager.cs").get("matches", [])
# ---- Sheets
O["pn_grid"] = jl(get("gsheets", "data.json", "/sheets_spreadsheets/220/sheets/1/grid", 60000)["text"])
O["pn_meta"] = {k: jl(get("gsheets", "data.json", "/sheets_spreadsheets/220/" + k, 200)["text"]) for k in ("title", "modified_time")}
O["pn_tabs"] = [jl(get("gsheets", "data.json", f"/sheets_spreadsheets/220/sheets/{i}/title", 200)["text"]) for i in range(3)]
# ---- Linear
O["zom"] = {z: jl(get("linear", "data.json", p, 6000)["text"]) for z, p in (("ZOM-542", "/issues/3617"), ("ZOM-483", "/issues/3554"), ("ZOM-556", "/issues/3632"), ("ZOM-563", "/issues/3640"), ("ZOM-397", "/issues/3461"))}
O["linear_comments_base"] = get("linear", "data.json", "/comments", 300).get("text")
# ---- Contacts and Linear users
O["contacts"] = {}
for a in ("brian.foster", "calvin.price", "douglas", "julia.lawson", "martin.walsh", "oliver.brooks", "owen.baker", "robert", "vincent.parker", "leonard.hayes"):
    r = find("contacts", a + "@harmonygames.co", "contacts.json", 4)
    ms = [m for m in r.get("matches", []) if m["pointer"].endswith("/email")]
    O["contacts"][a] = {"pointer": ms[0]["pointer"] if ms else None, "email": ms[0]["text"] if ms else None}
# ---- Drive folder
r = find("gdrive", "d_caafeec2804b3a67ce46aa", "data.json", 4)
ms = [m for m in r.get("matches", []) if m["pointer"].endswith("/id") or m["pointer"].endswith("/file_id")]
O["folder_ptr"] = ms[0]["parent_pointer"] if ms else None
O["folder"] = jl(get("gdrive", "data.json", O["folder_ptr"], 2500)["text"]) if ms else None
# ---- act-vs-defer searches as the persona
def pv(svc, q):
    p = subprocess.run(["python3", "-B", "Task_Authoring/tools/persona_view.py", "search", "samuel_turner", svc, q, "--limit", "50", "--json"], cwd=WS, capture_output=True, text=True, env=ENV, timeout=280)
    try: d = json.loads(p.stdout)
    except Exception: return {"error": p.stderr[:200] or p.stdout[:200]}
    return {"visible": len(d.get("visible", [])), "hits": [str(h.get("id")) + " | " + str(h.get("text") or h.get("snippet") or "")[:140] for h in d.get("visible", [])[:12]], "keys": list(d.keys())[:8]}
O["defer"] = {}
for svc in ("gmail", "slack"):
    for q in ("hold off", "don't send", "not yet", "don't move", "leave the tickets", "wait on"):
        O["defer"][f"{svc}:{q}"] = pv(svc, q)
for svc in ("linear", "trello"):
    for q in ("hold off", "don't send", "don't move"):
        r = find(svc, q, "data.json", 50)
        O["defer"][f"{svc}:{q}"] = {"visible": len(r.get("matches", [])), "complete": r.get("scan_complete"), "hits": [m["pointer"] + " | " + str(m["text"])[:120] for m in r.get("matches", [])[:6]]}
json.dump(O, open(os.path.join(HERE, "oe_base.json"), "w"), indent=0)
print("wrote oe_base.json", {k: (len(v) if hasattr(v, "__len__") else v) for k, v in O.items()})
