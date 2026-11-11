import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
print("=== formula writes + readbacks")
for r, seqs in (("B4",(118,119,120)),("B5",(102,103,104,105,106,107)),("PC",(104,105,106))):
    calls = T.load(r)[1]
    for s in seqs:
        c = calls[s]
        i = json.dumps(c["input"], ensure_ascii=False)
        f = re.findall(r'=[A-Z]+\([^"]{0,70}', i)[:2]
        print(r, s, c["name"], {k:v for k,v in c["input"].items() if k in ("range","ranges","valueInputOption")}, "formulas", f, "->", T.text(c["out"])[:210].replace("\n"," "))
print("=== B3 ART-813 / dup list_comments")
calls = T.load("B3")[1]
seen = collections.Counter(c["input"].get("issueId") for c in calls if c["name"]=="linear_list_comments")
print([k for k,v in seen.items() if v>1])
for c in calls:
    if c["name"]=="linear_list_comments" and c["input"].get("issueId") in [k for k,v in seen.items() if v>1]:
        print(c["seq"], c["input"], [ (x["id"], x["body"][:60]) for x in T.unwrap(c["out"])["comments"]])
print([ (c["seq"], c["name"]) for c in calls if c["seq"] in (181,182,183,184)])
print("B3#183 out", T.text(calls[183]["out"])[:130])
print("=== any later read of ART-813 in B3:", [ (c["seq"], c["name"]) for c in calls if c["seq"]>164 and "ART-813" in json.dumps(c["input"]) and c["name"].startswith("linear_")])
print("=== gcal list row")
for r, s in (("B3",10),("B6",10),("PC",9)):
    calls = T.load(r)[1]
    for k in (s, s+1):
        t = T.text(calls[k]["out"]) or ""
        for line in t.splitlines():
            if "Halloween" in line: print(r, k, calls[k]["name"], line[:200])
print("=== all slack search queries")
for r in T.RUNS:
    print(r, [ (c["name"].replace("slack_",""), c["input"]) for c in T.load(r)[1] if c["name"] in ("slack_search_public_and_private","slack_conversations_search_messages")])
print("=== mentions in final slack message, and thread reads per run")
TH = ["1759269913.882683","1755114007.441789","1759245641.309714","1758121809.236839","1758872409.023532","1759167065.499092"]
for r in T.RUNS:
    calls = T.load(r)[1]
    s = [c for c in calls if c["name"]=="slack_send_message"][0]
    m = re.findall(r"<@[A-Z0-9_]+>", s["input"]["message"])
    got = {t: [c["seq"] for c in calls if c["name"] in ("slack_read_thread","slack_conversations_replies") and (c["input"].get("message_ts")==t or c["input"].get("thread_ts")==t)] for t in TH}
    print(r, "mentions", m, {k[-6:]:v for k,v in got.items()})
print("=== Unity mail: body seen?")
print("B5#13 full -> yes; B1#20, B6#18 get_thread -> yes; B3#20, B4#15 get_message -> yes")
print("=== linear_list_comments limit form B4")
print([ (c["seq"], c["input"]) for c in T.load("B4")[1] if c["name"]=="linear_list_comments" and "limit" in c["input"]])
print("=== B4 readme read B4#9, B4#13 ranges", T.load("B4")[1][13]["input"])
