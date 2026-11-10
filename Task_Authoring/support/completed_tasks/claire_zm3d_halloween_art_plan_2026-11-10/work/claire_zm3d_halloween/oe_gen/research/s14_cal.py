import sys, json
sys.path.insert(0, ".")
import traj_lib as T
ev, calls = T.load("B1")
c = calls[7]; print("=== gcal_search_events B1#7", json.dumps(c["input"]))
d = T.unwrap(c["out"]); print(type(d), list(d.keys()) if isinstance(d, dict) else len(d))
print(T.text(c["out"])[:900])
items = d.get("items") or d.get("events") or []
print("n items", len(items), {k:v for k,v in d.items() if k not in ("items","events")})
for e in items: print("  ", e.get("id"), "|", e.get("summary"), "|", (e.get("start") or {}), "|", len(e.get("attendees") or []))
tgt = [e for e in items if "alloween" in (e.get("summary") or "") or "review" in (e.get("summary") or "").lower()]
print(json.dumps(tgt[:1], ensure_ascii=False, indent=1)[:2500])
ev, calls = T.load("B3")
for s in (8, 9, 10, 11):
    c = calls[s]; print(f"=== B3#{s}", c["name"], json.dumps(c["input"], ensure_ascii=False)[:500]); print(T.text(c["out"])[:2300])
