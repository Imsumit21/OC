import sys, json, re, collections, os
sys.path.insert(0, ".")
import traj_lib as T
ev, calls = T.load("B1")
print("=== search_channels with types", [ (c["id"], c["name"], c["is_private"]) for c in T.unwrap(calls[0]["out"])["channels"]], T.unwrap(calls[0]["out"]).get("total_count"))
ev, c4 = T.load("B4")
print("=== search_channels no types", [ (c["id"], c["name"], c["is_private"]) for c in T.unwrap(c4[0]["out"])["channels"]], T.unwrap(c4[0]["out"]).get("total_count"))
print("=== Robert thread parent in channel reads")
P = "1759167065.499092"
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        if c["name"] in ("slack_read_channel",) and c["input"].get("channel_id") == "C08R8CHB0QL":
            d = T.unwrap(c["out"]); ms = d["messages"]
            hit = [m for m in ms if m.get("ts") == P or m.get("thread_ts") == P]
            print(r, c["seq"], c["input"], "n", len(ms), "has_more", d.get("has_more"), "oldest", ms[-1]["ts"], "hit", json.dumps(hit, ensure_ascii=False)[:600])
print("=== B4#96"); print(T.text(c4[96]["out"]))
ev, c5 = T.load("B5")
print("=== B5#90", c5[90]["input"]); print(T.text(c5[90]["out"]))
print("=== search default limit B4#94", c4[94]["input"]); d = T.unwrap(c4[94]["out"]); print(len(d["messages"]), {k:v for k,v in d.items() if k!="messages"})
print("=== Martin store thread B1#14"); ev, c1 = T.load("B1"); print(T.text(c1[14]["out"])[:1900])
print("=== B1#14 concise form B4#95"); print(T.text(c4[95]["out"]))
print("=== PC#26", ); evp, cp = T.load("PC"); print(cp[26]["input"], cp[26]["raw"], len(cp[26]["out"]))
print("=== B5#85", c5[85]["raw"], c5[85]["input"], len(c5[85]["out"]))
print("=== channel messages newer than thread? read_channel C06DJBJL798 limit 30: newest ts/thread fields")
d = T.unwrap(c1[3]["out"]); print([ (m["ts"], m.get("reply_count")) for m in d["messages"][:4]])
print("=== who posted in read of 1755114007.441789 (B1#86) first 900"); print(T.text(c1[86]["out"])[:900]); d = T.unwrap(c1[86]["out"]); print("n", len(d["messages"]), {k:v for k,v in d.items() if k!="messages"})
