import sys, json, re, collections, base64
sys.path.insert(0, ".")
import traj_lib as T
K = {"UNITY":"CANf1Nx47805f8aa3d388495515d37fa274ef9","CHANGES":"CANf1Nxe0e348c2afd3a05d686bccff4582ec3","PLAN":"CANf1Nx8adc8e5aab6af2f77119eca82ab3cde"}
print("=== search/list result membership")
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        if c["name"] in ("gmail_search_messages","gmail_list_messages"):
            t = T.text(c["out"])
            print(r, c["seq"], c["input"].get("query"), {k:(v in t) for k,v in K.items()})
print("=== reads")
seen = {}
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        if c["name"] in ("gmail_get_thread","gmail_get_message","gmail_get_messages_batch"):
            d = T.unwrap(c["out"])
            msgs = []
            if isinstance(d, dict):
                msgs = d.get("messages") if "messages" in d else [d]
            elif isinstance(d, list): msgs = d
            subs = []
            for m in msgs or []:
                if not isinstance(m, dict): continue
                p = m.get("payload") or {}
                h = {x["name"]: x["value"] for x in p.get("headers", [])}
                subs.append((h.get("Subject"), h.get("Date")))
                seen[m.get("id")] = m
            print(r, c["seq"], c["name"], json.dumps({k:(v if not isinstance(v,list) else f"[{len(v)} ids]") for k,v in c["input"].items()})[:120], "->", subs[:8], "keys", (list(d.keys()) if isinstance(d,dict) else type(d).__name__))
print("=== bodies")
for i, m in seen.items():
    if not any(v in i for v in K.values()) : continue
    p = m.get("payload") or {}
    h = {x["name"]: x["value"] for x in p.get("headers", [])}
    b = (p.get("body") or {}).get("data")
    print("-----", i); print({k:h.get(k) for k in ("Date","Subject","From","To")}); print("internalDate", m.get("internalDate"), "labelIds", m.get("labelIds"))
    if b: print(base64.urlsafe_b64decode(b + "=" * (-len(b) % 4)).decode("utf8"))
ev, calls = T.load("B3")
c = calls[20]; print("\n=== B3#20 get_message"); print(json.dumps(c["input"])); print(T.text(c["out"])[:1600])
c = calls[16]; print("\n=== B3#16 batch input"); print(json.dumps(c["input"])[:900]); print(T.text(c["out"])[:500])
