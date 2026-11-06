"""Extract per-run facts for the all-fail rows R5 / R40 / R41 (ZOM-293 call, ZOM-570 blocker list)."""
import json, re, sys
from pathlib import Path

D = Path(sys.argv[1])
KEY = re.compile(r"\b(?:ZOM|ART|DES)-\d+\b")


def blocks(ev):
    m = ev.get("message") or {}
    c = m.get("content")
    return c if isinstance(c, list) else []


for n in range(1, 7):
    ev = json.load(open(D / f"trajectory-run-{n}.json"))
    print(f"===== run-{n} ({len(ev)} events)")
    uses = {}
    for i, e in enumerate(ev):
        for b in blocks(e):
            if b.get("type") == "tool_use":
                uses[b.get("id")] = (i, b.get("name"), b.get("input"))
    # 1. reads of ZOM-293 / its comments
    for i, e in enumerate(ev):
        for b in blocks(e):
            if b.get("type") == "tool_use":
                s = json.dumps(b.get("input"))
                if "ZOM-293" in s or "3347" in s:
                    print(f"  read/use ev{i} {b.get('name')} {s[:160]}")
            if b.get("type") == "tool_result":
                s = json.dumps(b.get("content"))
                if "both gone, 600 coins worth" in s or "what goes wrong here" in s:
                    u = uses.get(b.get("tool_use_id"), (None, None, None))
                    print(f"  RESULT-with-cmt_zom293_1 ev{i} from tool ev{u[0]} {u[1]} {json.dumps(u[2])[:120]}")
    # 2. sheet writes holding ZOM-293
    for i, e in enumerate(ev):
        for b in blocks(e):
            if b.get("type") == "tool_use" and re.search(r"sheet|gdrive", b.get("name") or "", re.I):
                s = json.dumps(b.get("input"), ensure_ascii=False)
                m = re.search(r'\[[^\[\]]*"ZOM-293"[^\[\]]*\]', s)
                if m:
                    print(f"  SHEET ev{i} {b.get('name')}: {m.group(0)[:400]}")
    # 3. ZOM-570 description updates
    for i, e in enumerate(ev):
        for b in blocks(e):
            if b.get("type") == "tool_use" and "update_issue" in (b.get("name") or ""):
                inp = b.get("input") or {}
                s = json.dumps(inp, ensure_ascii=False)
                if "ZOM-570" in s or "570" in s:
                    desc = inp.get("description") or ""
                    tail = desc.split("Other push notes go in the comments here.", 1)[-1]
                    keys = sorted(set(KEY.findall(tail)), key=lambda k: (k.split('-')[0], int(k.split('-')[1])))
                    print(f"  ZOM-570 UPDATE ev{i} {b.get('name')} keys_after_arthur={keys} (n={len(keys)}) ZOM-293_in_tail={'ZOM-293' in tail}")
                    print("     tail:", tail[:700].replace("\n", " | "))
    # 4. final result
    for i, e in enumerate(ev):
        if e.get("type") == "result":
            r = e.get("result") or ""
            j = r.find("ZOM-293")
            print(f"  RESULT ev{i} subtype={e.get('subtype')} is_error={e.get('is_error')} ZOM-293 mention: {r[max(0,j-200):j+200].replace(chr(10),' ') if j>=0 else 'none'}")
