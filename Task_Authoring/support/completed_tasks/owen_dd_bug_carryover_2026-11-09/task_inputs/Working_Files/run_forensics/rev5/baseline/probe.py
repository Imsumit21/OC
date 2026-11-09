import json, sys, re, collections, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from behaviour import calls
for a in sys.argv[1:]:
    lab, p = a.split("=", 1); cs = calls(p)
    q = lambda pre: [(n, i) for _, n, i, r in cs if n.startswith(pre)]
    slack_search = [i.get("query") or i.get("search_query") or i.get("filter_in_channel") for _, n, i, r in cs if "search" in n and n.startswith("slack")]
    hist = collections.Counter(i.get("channel_id") for _, n, i, r in cs if n in ("slack_read_channel", "slack_conversations_history"))
    threads = [(i.get("channel_id"), i.get("message_ts") or i.get("thread_ts")) for _, n, i, r in cs if n in ("slack_read_thread", "slack_conversations_replies")]
    gm = [(n, json.dumps(i)[:80]) for n, i in q("gmail")]
    gh = [(n, json.dumps(i)[:90]) for n, i in q("github")]
    lc = [i.get("issueId") or i.get("issue_id") or i.get("id") for _, n, i, r in cs if n == "linear_list_comments"]
    seen = lambda rx: any(re.search(rx, r) for _, n, i, r in cs)
    print(f"=== {lab}: {len(cs)} calls")
    print("  slack searches:", slack_search)
    print("  histories:", dict(hist))
    print("  threads:", collections.Counter(c for c, t in threads))
    print("  gmail:", gm)
    print("  github:", collections.Counter(n for n, _ in gh), [x[1] for x in gh if 'pull' in x[0] or 'review' in x[0] or 'comment' in x[0]][:6])
    print("  linear list_comments on non-tree:", [x for x in lc if x and not re.match(r"ENG-24(0[1-9]|[1-3]\d)$", str(x))])
    print("  saw: ENG-2073 mail", seen(r"Apple sync line"), "| Marcus tavern", seen(r"lost their frame again"), "| shop reply", seen(r"don.t trust that tick"),
          "| music DM", seen(r"music plays normally"), "| 1905 inline", seen(r"how-to-play popup still points"), "| 1908 inline", seen(r"info popup keeps the old frame"))
