import sys, json
sys.path.insert(0, ".")
import traj_lib as T
ev, calls = T.load("B1")
for s in (5, 6, 8, 9, 10, 23):
    c = calls[s]; print(f"=== B1#{s}", c["name"], json.dumps(c["input"], ensure_ascii=False)); print(T.text(c["out"])[:1700 if s != 10 else 5400])
ev, calls = T.load("B3")
for s in (12, 13):
    c = calls[s]; print(f"=== B3#{s}", c["name"], json.dumps(c["input"], ensure_ascii=False)); print(T.text(c["out"])[:1100])
ev, calls = T.load("PC")
for s in (10, 17, 18, 19, 25):
    c = calls[s]; print(f"=== PC#{s}", c["name"], json.dumps(c["input"], ensure_ascii=False)); print(T.text(c["out"])[:900])
