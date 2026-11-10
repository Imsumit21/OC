import json, os

TERMS = [
    ("halloween", "halloween"),
    ("halloween_push", "Halloween push"),
    ("live_creatives", "live creatives"),
    ("release_calendar", "release calendar"),
    ("seasonal_ad", "seasonal art direction"),
    ("oct_ua_plan", "October UA plan"),
    ("halloween_bits", "Halloween Bits"),
    ("kaykit", "KayKit"),
    ("ua_masters", "UA masters"),
    ("store_screens", "store screens"),
    ("cheer_fastcouch", "cheer fastcouch"),
    ("boris", "boris"),
    ("portrait_endcard", "portrait UA end card"),
    ("recapture", "re-capture"),
    ("recaptured", "re-captured"),
    ("merge_cut", "merge cut"),
    ("android_tablet", "Android US tablet"),
    ("ios_uk", "iOS UK"),
    ("halloween_review", "Halloween review"),
    ("ua_creative_lib", "UA creative library"),
    ("zombie_swap", "zombie swap"),
    ("android_1452", "Android #1452"),
    ("ios_1232", "iOS 1232"),
    ("halloween_pack", "Halloween pack"),
    ("zm_roadmap", "ZM ROADMAP"),
    ("capture_requests", "Video Capture Requests for UA"),
    ("release_checklist", "release checklist"),
]

LIMIT = 400

targets = {
    "slack": {"service": "slack", "file": "messages/*.json"},
    "gmail_claire": {"service": "gmail", "file": "threads/claire*"},
    "gdrive": {"service": "gdrive", "file": "data.json"},
    "gdocs": {"service": "gdocs", "file": "data.json"},
    "gsheets": {"service": "gsheets", "file": "data.json"},
    "gslides": {"service": "gslides", "file": "data.json"},
    "linear": {"service": "linear", "file": "data.json"},
    "trello": {"service": "trello", "file": "data.json"},
    "confluence": {"service": "confluence", "file": "confluence_working.json"},
    "github": {"service": "github", "file": "data.json"},
}

out = os.path.dirname(os.path.abspath(__file__))
for name, t in targets.items():
    req = dict(t)
    req["queries"] = [{"id": k, "query": q, "limit": LIMIT} for k, q in TERMS]
    with open(os.path.join(out, "req_%s.json" % name), "w") as f:
        json.dump(req, f, indent=1)
print("wrote", len(targets), "request files")
