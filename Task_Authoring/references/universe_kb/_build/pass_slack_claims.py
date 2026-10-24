"""Targeted Slack pass for superseded-claim traps: (a) thread parents that state a resolution
('fixed', 'resolved', 'live', 'deployed', 'works now') answered by a reply from someone else saying it
is still broken / not fixed; (b) messages with ~strikethrough~ (an in-place retraction)."""
import os, re, json, collections
from common import *

CLAIM = re.compile(r"\b(fixed|resolved|is live|went live|deployed|works now|working now|should be good|all good|done|merged|shipped|released|restored|back up)\b", re.I)
OVERTURN = re.compile(r"\b(still (not|broken|happening|failing|crashing|seeing|there|an issue)|not fixed|isn'?t fixed|broken again|happening again|doesn'?t work|not working|reopen|re-open|came back|regress|same issue|still the same|it'?s not)\b", re.I)
STRIKE = re.compile(r"(^|\s)~[^~\n]{3,}~(\s|$|[.,!?])")


def main():
    chans = {c["id"]: c for c in jload(SLACK + "/channels.json")}
    parents = {}
    over = []
    strikes = []
    for cid in sorted(os.listdir(SLACK + "/messages")):
        for fn in sorted(os.listdir(SLACK + "/messages/" + cid)):
            for x in jload(SLACK + "/messages/" + cid + "/" + fn):
                t = x.get("text") or ""
                ts = x.get("ts")
                tts = x.get("thread_ts")
                if x.get("subtype") or x.get("bot_id"):
                    continue
                if STRIKE.search(t):
                    strikes.append([cid, ts, x.get("user"), t[:200]])
                if tts and tts == ts and CLAIM.search(t):
                    parents[(cid, ts)] = (x.get("user"), t[:220], CLAIM.search(t).group(0).lower())
                elif tts and tts != ts and OVERTURN.search(t):
                    over.append([cid, tts, ts, x.get("user"), t[:220], OVERTURN.search(t).group(0).lower()])
    pairs = []
    for cid, tts, ts, u, t, m in over:
        p = parents.get((cid, tts))
        if p and p[0] != u:
            pairs.append({"channel": cid, "channel_name": chans.get(cid, {}).get("name"), "thread_ts": tts, "reply_ts": ts, "parent_user": p[0], "parent_claim": p[2],
                          "parent": p[1], "reply_user": u, "overturn_marker": m, "reply": t, "date": ts_to_dt(float(ts)).strftime("%Y-%m-%d")})
    pairs.sort(key=lambda x: x["reply_ts"])
    out = {"parent_claim_overturned_by_other": pairs, "strikethrough_messages": {"count": len(strikes), "examples": strikes[:40],
           "by_year": dict(collections.Counter(ts_to_dt(float(s[1])).strftime("%Y") for s in strikes))}}
    jdump(out, CACHE + "/kb_slack_claims.json")
    print("claims", len(pairs), "strikes", len(strikes))


if __name__ == "__main__":
    main()
