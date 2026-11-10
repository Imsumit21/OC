import sys, json, re
sys.path.insert(0, ".")
import traj_lib as T
ev, calls = T.load("B1")
print("### channel search B1#0"); print(T.text(calls[0]["out"])[:700])
ev3, c3 = T.load("B3")
print("### B3#0"); print(c3[0]["input"], T.text(c3[0]["out"]))
print("### B3#3 channels_list input", c3[3]["input"]); print(T.text(c3[3]["out"])[:500])
ev4, c4 = T.load("B4")
print("### B4#0 zombie no types"); print(T.text(c4[0]["out"])[:500])
print("### B4#3"); print(c4[3]["input"]); print(T.text(c4[3]["out"])[:715])
print("### profile"); print(calls[1]["input"]); print(T.text(calls[1]["out"]))
print("### get_time"); print(T.text(calls[2]["out"]))
print("### read_channel B1#3 first 1200"); t = T.text(calls[3]["out"]); print(t[:1200])
d = T.unwrap(calls[3]["out"])
print("keys", list(d.keys()) if isinstance(d, dict) else type(d))
ms = d.get("messages") if isinstance(d, dict) else None
print("n msgs", len(ms) if ms else None)
if ms:
    print("msg keys", sorted({k for m in ms for k in m.keys()}))
    for m in ms:
        if m.get("ts") == "1759269913.882683":
            print("LEONARD", json.dumps(m, ensure_ascii=False, indent=1))
    print({k: d[k] for k in d if k != "messages"})
print("### read_thread B1#4"); print(T.text(calls[4]["out"]))
