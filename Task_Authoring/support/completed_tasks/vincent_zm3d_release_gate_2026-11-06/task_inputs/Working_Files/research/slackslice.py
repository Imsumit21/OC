#!/usr/bin/env python3
"""Dump a slack channel slice with resolved user names and human ts. Read-only."""
import json, os, sys, datetime as dt
ROOT = "/Users/sumitkumar/Source/Outlier/OC"
SD = os.path.join(ROOT, "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack")
users = {u["id"]: (u.get("real_name") or u.get("name") or u["id"]) for u in json.load(open(os.path.join(SD, "users.json")))}
chans = {c["id"]: c.get("name") for c in json.load(open(os.path.join(SD, "channels.json")))}

def ts(t):
    return dt.datetime.utcfromtimestamp(float(t)).strftime("%Y-%m-%d %H:%MZ")

def main():
    chan, file = sys.argv[1], sys.argv[2]
    lo = int(sys.argv[3]); hi = int(sys.argv[4])
    msgs = json.load(open(os.path.join(SD, "messages", chan, file)))
    print(f"# {chans.get(chan)} {chan} {file} total={len(msgs)}")
    for i in range(max(0, lo), min(len(msgs), hi + 1)):
        m = msgs[i]
        who = users.get(m.get("user"), m.get("user") or "?")
        txt = (m.get("text") or "")
        for a in m.get("attachments") or []:
            txt += "\n    [attach] " + (a.get("fallback") or a.get("text") or json.dumps(a)[:400])
        print(f"/{i} {ts(m['ts'])} {who}: {txt}")

if __name__ == "__main__":
    main()
