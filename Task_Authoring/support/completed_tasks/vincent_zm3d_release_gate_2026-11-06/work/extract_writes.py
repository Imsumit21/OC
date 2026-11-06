import json, sys, re, collections

WRITE_HINTS = ("create", "update", "send", "append", "batch_update", "add_", "delete", "move", "post", "reply", "comment", "share", "clear")
READ_ONLY = ("search", "list", "get", "read", "lookup", "submit_search", "job_")

def is_write(name):
    n = name.split("__")[-1]
    if any(n.startswith(p) or ("_" + p) in n for p in ("search", "list_", "get_", "read_")):
        if not any(h in n for h in ("create", "update", "send", "append", "add", "delete", "move", "post", "comment", "share", "clear")):
            return False
    return any(h in n for h in WRITE_HINTS)

def main(path):
    d = json.load(open(path))
    out = []
    for i, ev in enumerate(d):
        if ev.get("type") != "assistant":
            continue
        msg = ev.get("message", {})
        for c in msg.get("content", []) or []:
            if c.get("type") == "tool_use" and c.get("name", "").startswith("mcp__hg__"):
                name = c["name"].replace("mcp__hg__", "")
                if is_write(name):
                    out.append({"event": i, "tool": name, "input": c.get("input")})
    final = d[-1].get("result") if isinstance(d[-1], dict) else None
    return out, final

if __name__ == "__main__":
    res = {}
    for p in sys.argv[1:]:
        w, f = main(p)
        res[p] = {"writes": w, "final": f}
    json.dump(res, open("/tmp/rubricwork/writes_all.json", "w"), ensure_ascii=False, indent=1)
    for p, v in res.items():
        print("==", p, len(v["writes"]))
        for w in v["writes"]:
            print("  ", w["event"], w["tool"])
