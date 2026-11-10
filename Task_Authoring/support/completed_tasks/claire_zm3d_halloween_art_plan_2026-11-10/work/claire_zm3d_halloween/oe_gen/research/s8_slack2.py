import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
SL = {"slack_read_channel","slack_read_thread","slack_conversations_replies","slack_search_public_and_private","slack_conversations_search_messages"}
idmap = collections.defaultdict(collections.Counter)
mentions = collections.Counter()
allmsgs = {}
for r in T.RUNS:
    ev, calls = T.load(r)
    for c in calls:
        if c["name"] not in SL: continue
        t = T.text(c["out"])
        for m in re.findall(r"<@([A-Z0-9_a-z]+)(?:\|[^>]*)?>", t): mentions[m] += 1
        d = T.unwrap(c["out"])
        if isinstance(d, dict):
            for k in ("messages","matches"):
                for m in d.get(k, []) or []:
                    if isinstance(m, dict):
                        up = m.get("user_profile") or {}
                        idmap[str(m.get("user"))][str(up.get("real_name"))+" / "+str(up.get("email"))] += 1
                        if m.get("ts"): allmsgs[(m.get("channel"), m.get("ts"))] = m
print("user->profile"); 
for k, v in sorted(idmap.items()): print(" ", k, dict(v))
print("mentions", mentions.most_common(40))
print("unique msgs", len(allmsgs))
ev, calls = T.load("B3")
c = calls[18]; print("### concise search B3#18", c["input"]); print(T.text(c["out"])[:900])
d = T.unwrap(c["out"]); print(type(d), list(d.keys()) if isinstance(d, dict) else "")
ev, calls = T.load("B1")
c = calls[13]; print("### full search B1#13", c["input"]); print(T.text(c["out"])[:1100])
d = T.unwrap(c["out"]); print(type(d), list(d.keys()) if isinstance(d, dict) else "")
print({k: (d[k] if not isinstance(d[k], list) else len(d[k])) for k in d})
c = calls[91]; print("### concise read_channel B1#91", c["input"]); print(T.text(c["out"])[:900])
