import sys, json, re, collections
sys.path.insert(0, ".")
import traj_lib as T
pats = ["manual review","Unity rep","re-recorded","rerecorded","#1935","#1896","#1966","C09ATAJ220H","C05KNDCHAAG","C0880U9751A","zm-animations","vacation","ad statics","the July capture","Sep 16 one","old zombies","68768a1501ae552dbee94b8a","Marcus/[PERSON"]
WRITE = {"linear_create_comment","linear_update_issue","linear_create_issue","gdocs_create_document","gsheets_values_update","slack_send_message","Bash","gdocs_batch_update","gsheets_batch_update"}
for r in T.RUNS:
    ev, calls = T.load(r)
    print("=====", r)
    for p in pats:
        reads = []; writes = 0
        for c in calls:
            t = T.text(c["out"])
            if p.lower() in t.lower():
                if c["name"] in WRITE: writes += 1
                else: reads.append(f'#{c["seq"]} {c["name"]}')
        print(f"  {p!r}: reads={reads[:6]} (n={len(reads)}) writes/bash={writes}")
    ch = collections.Counter()
    for c in calls:
        if c["name"] in ("slack_read_channel","slack_read_thread","slack_conversations_replies"):
            ch[c["input"].get("channel_id")] += 1
    print("  channels read:", dict(ch))
