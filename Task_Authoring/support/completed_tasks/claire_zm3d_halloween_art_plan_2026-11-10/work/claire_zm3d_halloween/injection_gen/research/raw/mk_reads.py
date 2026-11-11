import json, os, glob

R = os.path.dirname(os.path.abspath(__file__))
SERV = {
    "slack": ("slack", "messages/*.json"),
    "gmail_claire": ("gmail", "threads/claire*"),
    "gdrive": ("gdrive", "data.json"),
    "gdocs": ("gdocs", "data.json"),
    "gsheets": ("gsheets", "data.json"),
    "gslides": ("gslides", "data.json"),
    "linear": ("linear", "data.json"),
    "trello": ("trello", "data.json"),
    "confluence": ("confluence", "confluence_working.json"),
    "github": ("github", "data.json"),
}

items = []
seen = set()
for tag, (svc, f) in SERV.items():
    p = os.path.join(R, "out_%s.json" % tag)
    if not os.path.exists(p):
        continue
    d = json.load(open(p))
    for qid, q in (d.get("queries") or {}).items():
        ms = q.get("matches") or []
        for m in ms[:3]:
            ptr = m.get("parent_pointer")
            key = (svc, f, ptr)
            if key in seen:
                continue
            seen.add(key)
            items.append({
                "id": "%s__%s__%d" % (tag, qid, len(items)),
                "service": svc,
                "file": f,
                "pointer": ptr,
                "max_chars": 900,
            })
with open(os.path.join(R, "reads.json"), "w") as fh:
    json.dump({"items": items}, fh, indent=1)
print("items", len(items))
