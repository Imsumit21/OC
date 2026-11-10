import sys, json
sys.path.insert(0, ".")
import traj_lib as T
print("=== all gdrive_search / list_folder")
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        if c["name"] in ("gdrive_search","gdrive_list_folder"):
            d = T.unwrap(c["out"])
            fs = d.get("files", []) if isinstance(d, dict) else []
            print(r, c["seq"], c["name"], json.dumps(c["input"]), "n", len(fs), "total", d.get("totalCount") if isinstance(d,dict) else None, "next", d.get("nextPageToken") if isinstance(d,dict) else None, "|", [f.get("name") for f in fs][:4])
ev, calls = T.load("B3")
c = calls[24]; print("\n=== B3#24", c["input"]); print(T.text(c["out"])[:1600])
ev, calls = T.load("B1")
c = calls[21]; print("\n=== B1#21 fullText seasonal", c["input"])
d = T.unwrap(c["out"]); print([ (f["id"], f["name"], f["mimeType"].split(".")[-1]) for f in d["files"]])
c = calls[88]; print("\n=== B1#88 list_folder"); d = T.unwrap(c["out"]); print(T.text(c["out"])[:700]); print([(f["id"], f["name"]) for f in d["files"]])
ev, calls = T.load("PC")
c = calls[30]; print("\n=== PC#30"); print(T.text(c["out"])[:400])
for s in (31, 32):
    c = calls[s]; d = T.unwrap(c["out"]); print(f"\n=== PC#{s}", c["input"], {k:v for k,v in d.items() if k!='files'}); print([(f["id"], f["name"]) for f in d["files"]][:60])
c = calls[25]; print("\n=== PC#25 gslides_get_presentation (rest)"); print(T.text(c["out"]))
ev, calls = T.load("B4")
for s in (87, 91):
    c = calls[s]; print(f"\n=== B4#{s} metadata"); print(T.text(c["out"])[:1500])
