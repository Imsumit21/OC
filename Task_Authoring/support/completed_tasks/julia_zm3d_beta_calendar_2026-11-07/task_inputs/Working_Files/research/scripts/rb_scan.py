import json, os, re, sys, datetime
RAW = "/Users/sumitkumar/Source/Outlier/OC/Task_Authoring/task_inputsS/Working_Files/research/raw"
names = json.load(open(os.path.join(RAW, "slack_names.json")))
def nm(u): return names.get(u, u)

CH = {"C08R27X0EAH":"#zombie-bugs","C0880U9751A":"#zombie-match3d","C090N54TG79":"#zombie-design",
      "C08R6BF4ENN":"#zombie-ops","C08R8CHB0QL":"#zombie-art","C05KNDCHAAG":"#company-internal",
      "C05433XK267":"#builds"}

def load(ch, mon):
    p = os.path.join(RAW, f"slack_{ch}_{mon}.json")
    return json.load(open(p)) if os.path.exists(p) else None

def flat(m):
    """all searchable text of a message"""
    parts = [m.get("text") or ""]
    for a in (m.get("attachments") or []):
        if isinstance(a, dict):
            for k in ("pretext","title","text","fallback","footer"):
                if a.get(k): parts.append(str(a[k]))
            for f in (a.get("fields") or []):
                parts.append(str(f.get("title",""))+" "+str(f.get("value","")))
    for b in (m.get("blocks") or []):
        parts.append(json.dumps(b))
    for f in (m.get("files") or []):
        parts.append(str(f.get("title") or "")+" "+str(f.get("name") or ""))
    return "\n".join(parts)

BEAT = {
 "plague": r"plague",
 "C&W": r"collect\s*(?:&|and|n)?\s*win|win\s*(?:&|and|n)?\s*collect|\bc\s*&\s*w\b|win&collect",
 "seasonpass": r"season\s*pass|\bseason\b",
 "endless": r"endless|monster\s*mode",
 "league/lb": r"leaderboard|league",
 "lane/trophy": r"zombie\s*lane|trophy\s*path|\btrophy\b",
 "quest": r"quest",
 "daily/login": r"daily|log\s*in|login|gift",
}
OOS = r"boss\s*arena|infinite\s*boss|axe\s*arena"

def beats_of(t):
    tl = (t or "").lower()
    return [k for k,p in BEAT.items() if re.search(p, tl)]

def ts2s(ts):
    return datetime.datetime.utcfromtimestamp(float(ts)).strftime("%Y-%m-%d %H:%M")

def roots(lo, hi):
    out = []
    for ch in CH:
        for mon in ("2025-08","2025-09"):
            msgs = load(ch, mon)
            if not msgs: continue
            for m in msgs:
                ts = m.get("ts","")
                if not (lo <= ts <= hi): continue
                if m.get("thread_ts") not in (None, ts): continue
                reps = sorted([x for x in msgs if x.get("thread_ts")==ts and x.get("ts")!=ts], key=lambda x: float(x["ts"]))
                out.append((ch, ts, m, reps))
    out.sort(key=lambda r: float(r[1]))
    return out

if __name__ == "__main__":
    lo, hi = sys.argv[1], sys.argv[2]
    minrc = int(sys.argv[3]) if len(sys.argv)>3 else 1
    for ch, ts, m, reps in roots(lo,hi):
        rc = m.get("reply_count") or 0
        alltxt = flat(m)
        bs = beats_of(alltxt)
        if rc < minrc: continue
        oos = bool(re.search(OOS, alltxt, re.I))
        print("="*110)
        print(f"{CH[ch]} {ts} {ts2s(ts)} | {nm(m.get('user'))} | rc={rc} loaded={len(reps)} files={len(m.get('files') or [])} att={len(m.get('attachments') or [])} | beats={bs} OOS={oos}")
        print("ROOT:", re.sub(r"\s+"," ", alltxt)[:500])
        if reps:
            last = reps[-1]
            print(f"LAST {ts2s(last['ts'])} {nm(last.get('user'))}:", re.sub(r"\s+"," ",flat(last))[:260], "| beatinlast=", beats_of(flat(last)))
