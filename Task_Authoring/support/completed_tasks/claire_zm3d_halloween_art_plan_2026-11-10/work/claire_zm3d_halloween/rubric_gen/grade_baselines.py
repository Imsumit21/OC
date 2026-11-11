#!/usr/bin/env python3
"""Local projection only: grade the decoded writes of the rev3 runs against rows.json with regex rules. It is not the
platform verifier; it gives the likely weighted pass rate, spread and the rows every run misses. Never used to pick a
row or a weight."""
import json, re, sys, statistics as st
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
sys.path.insert(0, str(WF / "oe_gen"))
import model as M
rows = json.load(open(HERE / "rows.json"))
B = json.load(open(HERE / "baseline_writes.json"))
RUNS = ["run-1", "run-2", "run-3", "run-4", "run-5", "run-6"]
EXTRA = ["precheck-rev3"]
CALLS = "halloween version|refresh first|reuse|skip"
NAME2K = {M.name(k).lower(): k for k in M.ADS}

def call_of(t):
    if not t: return None
    m = re.search(r"call[^a-z]{0,12}(?:is\s+)?\W*(" + CALLS + ")", t, re.I) or re.search("(" + CALLS + ")", t, re.I)
    return m.group(1).lower() if m else None

def final_day(t):
    days = [int(a or b) for a, b in re.findall(r"Oct(?:ober)?\.?\s*(\d{1,2})|2025-10-(\d{2})", t or "")]
    days = [d for d in days if d <= 17]
    return max(days) if days else None

def tracker(run):
    out, store = {}, {}
    for s in B[run]["sheets"]:
        for tab, grid in s["tabs"].items():
            hdr = None
            for r in grid:
                cells = [str(c) for c in r]
                low = [c.lower() for c in cells]
                if hdr is None:
                    if any("call" in c for c in low) and len(cells) > 3:
                        hdr = low
                    continue
                joined = " | ".join(cells)
                def col(rx):
                    for i, h in enumerate(hdr):
                        if re.search(rx, h) and i < len(cells):
                            return cells[i]
                    return ""
                rec = {"call": call_of(col("call")), "owner": col("maker|owner|made by"), "due": col("due")}
                m = re.search(r"ART-(\d{3})", joined)
                k = None
                if m and f"ART-{m.group(1)}" in M.ADS and not re.search("new|ART-85[5-9]", low[0] if low else ""):
                    k = f"ART-{m.group(1)}"
                if not k:
                    for c in low:
                        if c.strip() in NAME2K:
                            k = NAME2K[c.strip()]
                if k:
                    out[k] = rec
                elif re.search(r"icon|iphone|ipad|google play", joined, re.I):
                    key = "icon" if re.search("icon", low[0] + " " + (low[1] if len(low) > 1 else "")) else "ipad" if re.search("ipad", joined, re.I) and not re.search("iphone", low[0] + (low[1] if len(low) > 1 else "")) else "iphone" if re.search("iphone", joined, re.I) else "play"
                    store.setdefault(key, rec)
    return out, store

def grade(run):
    r = B[run]
    C = {k: " ".join(x["body"] for x in v if x.get("success")) for k, v in r["comments"].items()}
    A = {k: [u.get("assignee_email") for u in v if u.get("assignee_email")] for k, v in r["updates"].items()}
    T, Sto = tracker(run)
    doc = " ".join(d.get("body", "") for d in r["doc"])
    res = {}
    for x in rows:
        t = x["tag"]; ok = False
        if t.startswith("cmt_call_"):
            k = t[9:]; ok = call_of(C.get(k)) == M.call(k).lower()
        elif t.startswith("cmt_due_"):
            k = t[8:]; d = final_day(C.get(k)); ok = d is not None and ((d <= 10) if M.due(k) == "Fri Oct 10" else (11 <= d <= 15))
        elif t.startswith("cmt_due_count_"):
            ok = any(final_day(C[k]) for k in C) and not any(final_day(C[k]) and (k in M.ARCHIVE or M.call(k) == "Skip") and re.search(r"(?i)\bdue\b[^.]{0,30}oct", C[k]) for k in C)
        elif t == "cmt_count":
            ok = len(C) == 58
        elif t == "assign_count_48":
            ok = sum(1 for k, v in A.items() if v and k in M.ISS) == 48
        elif t.startswith("assign_"):
            k = t[7:]; e = "julia" if M.maker(k) == "Julia Lawson" else "marcus.bennett"
            ok = bool(A.get(k)) and e in A[k][-1]
        elif t.startswith("share_scope_"):
            kind = "doc" if "w_doc" in t else "sheet"
            ok = len({x["email"] for x in r["shares"] if x["file_kind"] == kind and x["success"]}) == 6
        elif t.startswith("share_"):
            kind = "doc" if "w_doc" in t else "sheet"; who = t.split("_")[-1]
            ok = any(s["file_kind"] == kind and s["email"].startswith(who + "@") and s["role"] in ("commenter", "writer") and s["success"] for s in r["shares"])
        elif t.startswith("reply_"):
            ok = r["summary"]["thread_reply_both_links"]
        elif t == "tk_icon":
            ok = any(re.search("icon", n["title"], re.I) for n in r["new_tickets"])
        elif t == "tk_ipad":
            ok = any(re.search("ipad", n["title"], re.I) for n in r["new_tickets"])
        elif t == "tk_scope":
            ok = len({w for n in r["new_tickets"] for w in ("icon", "ipad", "iphone", "google play") if w in n["title"].lower()}) == 2
        elif t in ("doc_create",):
            ok = bool(r["doc"])
        elif t == "trk_create":
            ok = bool(r["sheets"])
        elif t == "trk_rows":
            ok = len(T) == 58
        elif t.startswith("trk_count_"):
            w = {"halloween": ("halloween version", 14), "refresh": ("refresh first", 36), "reuse": ("reuse", 2), "skip": ("skip", 10)}[t.split("_")[-1]]
            n = sum(1 for v in list(T.values()) + list(Sto.values()) if v["call"] == w[0]); ok = n == w[1]
        elif t.startswith("trk_call_"):
            k = t[9:]; ok = k in T and T[k]["call"] == M.call(k).lower()
        elif t.startswith("trk_due_count_"):
            n = int(t.split("_")[-1]); lo, hi = (0, 10) if n == 30 else (11, 15)
            ok = sum(1 for v in T.values() if (d := final_day(v["due"])) is not None and lo <= d <= hi) == n
        elif t.startswith("trk_due_"):
            k = t[8:]; d = final_day(T.get(k, {}).get("due")); ok = d is not None and ((d <= 10) if M.due(k) == "Fri Oct 10" else (11 <= d <= 15))
        elif t.startswith("trk_owner_count_"):
            n = int(t.split("_")[-1]); e = "julia" if n == 6 else "marcus"
            ok = sum(1 for k, v in T.items() if M.call(k) != "Skip" and e in v["owner"].lower()) == n
        elif t.startswith("trk_owner_ART"):
            k = t[10:]; ok = M.maker(k).split()[0].lower() in T.get(k, {}).get("owner", "").lower()
        elif re.match(r"trk_(icon|ipad|iphone|play)_call", t):
            key = t.split("_")[1]; ok = Sto.get(key, {}).get("call") == {"icon": "halloween version", "ipad": "halloween version", "iphone": "reuse", "play": "reuse"}[key]
        elif re.match(r"trk_(icon|ipad)_due", t):
            key = t.split("_")[1]; d = final_day(Sto.get(key, {}).get("due")); ok = d is not None and d <= 16
        elif re.match(r"trk_(icon|ipad)_owner", t):
            ok = "martin" in Sto.get(t.split("_")[1], {}).get("owner", "").lower()
        elif re.match(r"doc_(icon|ipad|iphone|play)_call", t):
            key = t.split("_")[1]; ok = Sto.get(key, {}).get("call") == {"icon": "halloween version", "ipad": "halloween version", "iphone": "reuse", "play": "reuse"}[key]
        elif t.startswith("doc_count_"):
            w = {"refresh": ("refresh first", 36), "halloween": ("halloween version", 12), "skip": ("skip", 10)}[t.split("_")[-1]]
            ok = sum(1 for v in T.values() if v["call"] == w[0]) == w[1]
        elif t == "doc_due10":
            ok = bool(re.search(r"android us phone[^\n]{0,80}oct(?:ober)? 10", doc, re.I))
        elif t == "doc_due15":
            ok = "Oct 15" in doc
        elif re.match(r"doc_(icon|ipad)_due", t):
            ok = "Oct 16" in doc
        elif t == "doc_julia":
            ok = bool(re.search(r"julia[^\n]{0,60}static|static[^\n]{0,60}julia", doc, re.I)) and not re.search(r"martin[^\n]{0,40}static", doc, re.I)
        elif t in ("doc_marcus_video", "doc_marcus_endcards", "doc_martin_icon", "doc_martin_ipad"):
            ok = t.split("_")[1] in doc.lower()
        elif t == "doc_icon_build":
            ok = bool(re.search(r"icon[^\n]{0,120}oct(?:ober)? 17|oct(?:ober)? 17[^\n]{0,120}icon", doc, re.I))
        elif t == "doc_iphone_ship":
            ok = bool(re.search(r"iphone[^\n]{0,160}oct(?:ober)? 1[67]", doc, re.I))
        elif t == "doc_play_route":
            ok = bool(re.search(r"(google play|\bplay\b|\bgp\b)[^\n]{0,200}(any day|1 day|one day|upload)", doc, re.I))
        else:
            raise SystemExit("ungraded " + t)
        res[t] = bool(ok)
    return res

G = {r: grade(r) for r in RUNS + EXTRA}
tw = sum(x["w"] for x in rows)
pct = {r: 100 * sum(x["w"] for x in rows if G[r][x["tag"]]) / tw for r in G}
print("total weight", tw)
for r in G:
    print(r, "rows passed", sum(G[r].values()), "of", len(rows), "weighted", round(pct[r], 1))
six = [pct[r] for r in RUNS]
print("avg six", round(st.mean(six), 1), "pop SD", round(st.pstdev(six) / 100, 3), "range", round(min(six), 1), round(max(six), 1))
allfail = [x for x in rows if not any(G[r][x["tag"]] for r in RUNS)]
allpass = [x for x in rows if all(G[r][x["tag"]] for r in RUNS)]
print("rows failing all six", len(allfail), "weight", sum(x["w"] for x in allfail), "| rows passing all six", len(allpass), "weight", sum(x["w"] for x in allpass))
import collections
fam = collections.Counter()
for x in allfail: fam[re.sub(r"_ART-\d+|_\d+$", "", x["tag"])] += 1
print(fam)
mix = [x for x in rows if x not in allfail and x not in allpass]
print("rows that vary", len(mix), "weight", sum(x["w"] for x in mix))
print([ (x["tag"], sum(G[r][x["tag"]] for r in RUNS)) for x in mix][:60])
json.dump({"pct": pct, "rows": {x["tag"]: {r: G[r][x["tag"]] for r in G} for x in rows}}, open(HERE / "baseline_grade.json", "w"), indent=0)
