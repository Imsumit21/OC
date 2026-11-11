#!/usr/bin/env python3
"""Prompt check (04) for task_inputsS2: lookups, then the report.

  ~/.local/bin/python3.12 -B Working_Files/plan/assemble_check.py lookups   # every lookup, raw outputs to plan/check_r1/
  ~/.local/bin/python3.12 -B Working_Files/plan/assemble_check.py           # writes Working_Files/04_Prompt_Check.md

The lookups read the universe only through Task_Authoring/tools/hg.py, persona_view.py, entity.py and check-sql on the
SQL; they never execute SQL and never write outside plan/check_r1/. Two #winddown messages hold a pasted secret: every
output is guarded, and a run that meets either ts stops before anything is written. The queries never search for those
ts. The assemble step checks every quoted span against 04_Prompt.txt byte for byte and stops on a miss.
"""
import datetime as dt
import hashlib
import json
import os
import re
import subprocess
import sys
from decimal import Decimal as D

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
OUT = os.path.join(HERE, "check_r1")
TASK = "Task_Authoring/task_inputsS2"
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=TASK, PYTHONDONTWRITEBYTECODE="1")
PY = [sys.executable, "-B"]
EXCLUDED_TS = ("1770858495.115779", "1770858501.263569")
ROB = "robert@harmonygames.co"
A = ROB + "/"
PROMPT_PATH = os.path.join(TI, "04_Prompt.txt")
SQL_PATH = os.path.join(TI, "01_Universe_Inject.sql")


def guard(txt, what):
    if any(t in txt for t in EXCLUDED_TS):
        sys.exit(f"STOP: {what} returned an excluded #winddown record; change the query. Nothing more written.")
    return txt


def run(args, timeout=900):
    p = subprocess.run(PY + args, cwd=WS, env=ENV, capture_output=True, text=True, timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def save(name, text):
    os.makedirs(OUT, exist_ok=True)
    guard(text, name)
    with open(os.path.join(OUT, name), "w") as f:
        f.write(text if text.endswith("\n") else text + "\n")


def hg(args, stdin=None, timeout=900):
    p = subprocess.run(PY + ["Task_Authoring/tools/hg.py", "search"] + args, cwd=WS, env=ENV, input=stdin,
                       capture_output=True, text=True, timeout=timeout)
    guard(p.stdout, "hg.py " + " ".join(args[:3]))
    return json.loads(p.stdout)


def get_all(service, file, pointer):
    txt, off = "", 0
    while True:
        d = hg(["get", service, "--file", file, "--pointer", pointer, "--offset", str(off), "--max-chars", "400000"])
        txt += d["text"]
        if not d.get("truncated"):
            return txt
        off = d["next_offset"]


# ------------------------------------------------------------------ lookups


def l_context():
    rc, out, err = run(["Task_Authoring/tools/task_context.py", "--task-dir", TASK, "--require-source"])
    ctx = json.loads(out)
    with open(os.path.join(WF, "00_Task_Context.json")) as f:
        same = json.load(f) == ctx
    keep = {k: ctx[k] for k in ("persona_name", "persona_role", "email", "business_function", "competency", "task_skill",
                                 "task_type", "horizon", "difficulty_mode", "universe_date_raw", "freeze_utc", "context_hash")}
    keep["universe"] = {k: ctx["universe"][k] for k in ("key", "clock_line", "persona_today", "persona_today_weekday",
                                                        "shutdown_rules_apply")}
    keep["source_status"] = ctx["source"]["status"]
    keep["kb_status"] = ctx["source"]["kb_status"]
    keep["identical_to_Working_Files/00_Task_Context.json"] = same
    rc2, out2, _ = run(["Task_Authoring/tools/hg.py", "universe", "show"])
    save("01_context.txt", f"$ task_context.py --task-dir {TASK} --require-source   (no --write; rc {rc})\n"
         + json.dumps(keep, indent=1) + f"\n\n$ hg.py universe show (rc {rc2})\n" + out2)


def l_slack_ids():
    req = {"service": "slack", "file": "users.json", "queries": [
        {"id": "leonard", "query": "leonard.hayes@harmonygames.co", "limit": 5},
        {"id": "robert", "query": "robert@harmonygames.co", "limit": 5},
        {"id": "arthur", "query": "arthur.blake@harmonygames.co", "limit": 5},
        {"id": "blake_name", "query": "Blake", "limit": 20}]}
    users = hg(["search-many", "--request", "-", "--compact"], json.dumps(req))
    ch = hg(["search", "slack", "winddown", "--file", "channels.json", "--limit", "20", "--compact"])
    reads = {"items": []}
    seen = set()
    for q in users["queries"].values():
        for m in q["matches"]:
            if m["parent_pointer"] not in seen:
                seen.add(m["parent_pointer"])
                reads["items"].append({"id": "users" + m["parent_pointer"].replace("/", "_"), "service": "slack",
                                       "file": "users.json", "pointer": m["parent_pointer"], "max_chars": 1500})
    for m in ch["matches"]:
        if m["parent_pointer"] not in seen and m["text"] == "winddown":
            seen.add(m["parent_pointer"])
            reads["items"].append({"id": "channel" + m["parent_pointer"].replace("/", "_"), "service": "slack",
                                   "file": "channels.json", "pointer": m["parent_pointer"], "max_chars": 4000})
    got = hg(["get-many", "--request", "-", "--compact"], json.dumps(reads))
    save("02_slack_people_channel.json", json.dumps({"search_users": users, "search_channel": ch, "reads": got}, indent=1))


def l_entity():
    out = []
    for name in ("Leonard", "Leonard Hayes", "Blake", "Arthur Blake", "Robert"):
        rc, o, e = run(["Task_Authoring/tools/entity.py", "resolve", name])
        out.append(f"$ entity.py resolve {name!r} (rc {rc})\n{o}{e}")
    save("03_entity.txt", "\n".join(out))


LB_IDS = [
    # prompt premises (seeded)
    "C0ADGSZKR3R/1770945821.640039", "C0ADGSZKR3R/1770945859.212469", "f_6feda53b2382c63bf47b25",
    "f_3304033843904a426f3c00", "f_a4b3c4287a4314d8e532e1", "evt_f21476dc404329f67fd60d",
    # fair-reading settlers (seeded)
    "C05URGU759U/1770971846.479179",
    A + "<CAOOpSqA2MTKGlKETvkoKqFfq1MaIktcGcH9cj21BJMAMN4Ok00@mail.gmail.com>",
    A + "<CAPBs_a5xhlLhxf4uFEerJEygHD5CJ2ob3qegV9nV-erG4foiIU@mail.gmail.com>",
    # Robert's Drive and the base settlers (judged against the base)
    "d_9f7ba94f7526d54d8482ba", "C0ADGSZKR3R/1770934638.035469",
    "C04UEQVDVB7/1712331142.975829", "C04UEQVDVB7/1712331372.614469", "C04UEQVDVB7/1712901800.684259",
    "C04UEQVDVB7/1712901837.860709", "C04UEQVDVB7/1719603590.685019", "C04UEQVDVB7/1719603595.852129",
    "C04UEQVDVB7/1761954952.006759", "C04UEQVDVB7/1761844454.096829", "C04UEQVDVB7/1761844624.408899",
    "C05KNDCHAAG/1760125440.959149", "f_20a0df3860bb5731d22f07",
    A + "1795282860741136988", A + "1776934359028762037", A + "1807851044809802572", A + "1847427662807006290",
    A + "1800873055214061794", A + "1802092844284446043", A + "1803223458475671884", A + "1805405368810910191",
    A + "1808201559428745555", A + "1798239548116390324", A + "1811158112675912556", A + "1776227799449805411",
]


def l_checksql():
    ids = os.path.join(OUT, "04_load_bearing_ids.txt")
    save("04_load_bearing_ids.txt", "\n".join(LB_IDS))
    rc, o, e = run(["Task_Authoring/tools/persona_view.py", "check-sql", "robert", SQL_PATH, "--load-bearing", ids])
    save("05_check_sql.txt", f"$ persona_view.py check-sql robert 01_Universe_Inject.sql --load-bearing check_r1/04_load_bearing_ids.txt (rc {rc})\n{o}{e}")
    cs = []
    for svc, rid in (("gdrive", "d_9f7ba94f7526d54d8482ba"), ("slack", "C0ADGSZKR3R/1770934638.035469"),
                     ("slack", "C04UEQVDVB7/1712901837.860709"), ("slack", "C04UEQVDVB7/1719603595.852129"),
                     ("slack", "C04UEQVDVB7/1761954952.006759"), ("slack", "C04UEQVDVB7/1761844624.408899"),
                     ("slack", "C05KNDCHAAG/1760125440.959149"), ("gdocs", "f_20a0df3860bb5731d22f07"),
                     ("gmail", A + "1798239548116390324"), ("gmail", A + "1811158112675912556"),
                     ("gmail", A + "1776934359028762037"), ("gmail", A + "1807851044809802572")):
        rc, o, e = run(["Task_Authoring/tools/persona_view.py", "can-see", "robert", svc, rid])
        cs.append(f"$ persona_view.py can-see robert {svc} {rid} (rc {rc})\n{o}{e}")
    save("06_can_see.txt", "\n".join(cs))


def l_persona_search():
    out = []
    for svc, q in (("slack", "angel calls"), ("slack", "Payee history"), ("gdocs", "how to count the money"),
                   ("gsheets", "Angel note working"), ("gslides", "Note to angels"), ("linear", "Payee history"),
                   ("gcal", "Angel calls")):
        args = ["Task_Authoring/tools/persona_view.py", "search", "robert", svc, q, "--limit", "10"]
        rc, o, e = run(args)
        out.append(f"$ persona_view.py search robert {svc} {q!r} --limit 10 (rc {rc})\n{o}{e}")
    save("07_persona_search.txt", "\n".join(out))


def l_linear():
    req = {"service": "linear", "file": "data.json", "queries": [
        {"id": "payee_projects", "query": "Payee", "pointer": "/projects", "limit": 50},
        {"id": "payee_history_any", "query": "Payee history", "limit": 50},
        {"id": "control_zombie_match", "query": "Zombie Match", "pointer": "/projects", "limit": 5},
        {"id": "done_state", "query": "Done", "pointer": "/issues", "key": "state_id", "limit": 3}]}
    d = hg(["search-many", "--request", "-", "--compact"], json.dumps(req))
    eng = hg(["get", "linear", "--file", "data.json", "--pointer", "/issues/844", "--max-chars", "1500"])
    save("08_linear_base.json", json.dumps({"search_many": d, "team_ENG_Done_example": eng}, indent=1))


def l_revenue():
    lines = []
    for t, gk, tk, dk in ((12, "game_id", "total_revenue_usd", "date"), (13, "title_id", "total_revenue_current", "report_date")):
        name = hg(["get", "snowflake", "--file", "snowflake.json", "--pointer", f"/tables/{t}/id"])["text"]
        rows = json.loads(get_all("snowflake", "snowflake.json", f"/tables/{t}/rows"))
        agg = {}
        for r in rows:
            a = agg.setdefault(r[gk], {"rows": 0, "total": D(0), "iap": D(0), "ad": D(0), "first": "9999", "last": "0000"})
            a["rows"] += 1
            a["total"] += D(str(r[tk]))
            a["iap"] += D(str(r.get("iap_revenue_usd", r.get("iap_revenue_current", 0))))
            a["ad"] += D(str(r.get("ad_revenue_usd", r.get("ad_revenue_current", 0))))
            a["first"], a["last"] = min(a["first"], r[dk]), max(a["last"], r[dk])
        lines.append(f"VERIFY {name}: {len(rows)} rows via hg.py get /tables/{t}/rows (paged to the end)")
        for g, a in sorted(agg.items()):
            lines.append(f"VERIFY {name} {g}: total {a['total']:,.2f} (iap {a['iap']:,.2f}, ad {a['ad']:,.2f}) over {a['rows']} rows, "
                         f"{a['first']} to {a['last']}")
    save("09_revenue.txt", "\n".join(lines))


def robert_threads(phrase):
    rc, o, e = run(["Task_Authoring/tools/persona_view.py", "search", "robert", "gmail", phrase, "--limit", "400",
                    "--no-hidden", "--json"])
    want = {h["id"] for h in json.loads(guard(o, phrase))["visible"]}
    d = hg(["search", "gmail", phrase, "--limit", "5000", "--compact"])
    if not d.get("scan_complete"):
        sys.exit(f"STOP: incomplete scan for {phrase!r}")
    names = sorted({m["service_file"] for m in d["matches"]})
    out = {}
    for i in range(0, len(names), 50):
        req = {"items": [{"id": f, "service": "gmail", "file": f, "pointer": "/id", "max_chars": 200} for f in names[i:i + 50]]}
        for f, r in hg(["get-many", "--request", "-"], json.dumps(req)).get("items", {}).items():
            tid = str(r.get("text", "")).strip().strip('"')
            if tid in want:
                out[tid] = f
    return out, want


def bodies(files):
    res, names = {}, sorted(files)
    for i in range(0, len(names), 25):
        items = {f: "" for f in names[i:i + 25]}
        offs = {f: 0 for f in items}
        while offs:
            req = {"items": [{"id": f, "service": "gmail", "file": f, "pointer": "/messages", "offset": o, "max_chars": 20000}
                             for f, o in offs.items()]}
            got = hg(["get-many", "--request", "-"], json.dumps(req))["items"]
            nxt = {}
            for f, r in got.items():
                items[f] += r.get("text", "")
                if r.get("truncated"):
                    nxt[f] = r["next_offset"]
            offs = nxt
        for f, t in items.items():
            res[f] = json.loads(t)
    return res


def l_notices():
    """Robert's own SVB notices, re-derived: aggregates only, no message text written."""
    tids, want = robert_threads("Payment Processed")
    msgs = bodies(tids.values())
    rx = re.compile(r"\*\*\*(\d{4})\s*Amount:\s*([\d,]+\.\d{2})\s*([A-Z]{3}).*?Transaction Date:\s*([A-Z][a-z]{2} \d{2} \d{4})", re.S)
    by_end, by_end_bet, by_bet, cnt, cur, n = {}, {}, {"Domino Delights": D(0), "ZM": D(0), "Combo Fighter": D(0)}, {}, {}, 0
    first, last, dates = None, None, {}
    for f, ms in msgs.items():
        for m in ms:
            if "Payment Processed" not in str(m.get("subject")):
                continue
            for end, amt, c, date in rx.findall(str(m.get("body"))):
                n += 1
                a = D(amt.replace(",", ""))
                cur[c] = cur.get(c, 0) + 1
                cnt[end] = cnt.get(end, 0) + 1
                d = dt.datetime.strptime(date, "%b %d %Y").date()
                first, last = min(first or d, d), max(last or d, d)
                if end in ("9368", "3203", "8605", "3341", "3801", "1359"):
                    dates.setdefault(end, []).append(f"{d} {a:,.2f} {c}")
                if c != "USD":
                    by_end[end + " " + c] = by_end.get(end + " " + c, D(0)) + a
                    continue
                by_end[end] = by_end.get(end, D(0)) + a
                k = "Domino Delights" if d <= dt.date(2025, 1, 8) else "ZM" if d <= dt.date(2025, 11, 23) else "Combo Fighter"
                by_bet[k] += a
                by_end_bet.setdefault(end, {}).setdefault(k, D(0))
                by_end_bet[end][k] += a
    lines = [f"VERIFY notices: {len(tids)} of {len(want)} Robert threads read through hg.py get-many; {n} Processed payments; "
             f"currencies {cur}; transaction dates {first} to {last}"]
    lines += [f"VERIFY by-date USD sum {k}: {v:,.2f}" for k, v in by_bet.items()]
    for k, v in sorted(by_end.items()):
        split = ", ".join(f"{b} {x:,.2f}" for b, x in by_end_bet.get(k, {}).items())
        lines.append(f"VERIFY ending {k}: {v:,.2f} over {cnt.get(k.split()[0])} notices" + (f" ({split})" if split else ""))
    for k in ("9368", "3203", "8605", "3341", "3801"):
        lines.append(f"VERIFY dated notices ***{k}: {sorted(dates.get(k, []))}")
    lb = dates.get("1359", [])
    lines.append(f"VERIFY ***1359 first notice {min(lb) if lb else None}; by year " + ", ".join(
        f"{y} {sum(D(x.split()[1].replace(',', '')) for x in lb if x.startswith(y)):,.2f}" for y in ("2023", "2024", "2025", "2026")))
    # Western Union receipts: one transfer per tracking number
    rt, _ = robert_threads("ready for pickup")
    sent, copies = {}, 0
    for f, ms in bodies(rt.values()).items():
        for m in ms:
            b = str(m.get("body"))
            x = re.search(r"Transfer Amount[^\d$]*\$?\s*([\d,]+\.\d{2})", b)
            t = re.search(r"(?:MTCN|Tracking Number)[^\d]{0,20}(\d{4,})", b)
            if not (x and t):
                continue
            copies += t.group(1) in sent
            sent[t.group(1)] = (D(x.group(1).replace(",", "")), "[PERSON_NAME_36400]" in b)
    lines.append(f"VERIFY Western Union in Robert's mail: {len(sent)} transfers by tracking number, {copies} forwarded copy; "
                 f"amounts {sorted(str(a) for a, _ in sent.values())}; all name [PERSON_NAME_36400]: {all(k for _, k in sent.values())}; "
                 f"total {sum(a for a, _ in sent.values()):,.2f}")
    # the Awaiting notice that no Processed notice follows
    at, _ = robert_threads("Leapblock LTD")
    aw = []
    for f, ms in bodies(at.values()).items():
        for m in ms:
            s = str(m.get("subject"))
            if "Processed" in s:
                continue
            b = str(m.get("body"))
            for end, amt, date in re.findall(r"\*\*\*(\d{4})\s*Amount:\s*([\d,]+\.\d{2})\s*USD.*?Transaction Date:\s*([A-Z][a-z]{2} \d{2} \d{4})", b, re.S):
                if end == "1359":
                    kind = "Awaiting" if "Awaiting" in s else "Scheduled" if "Schedul" in s else s[:30]
                    aw.append((str(dt.datetime.strptime(date, "%b %d %Y").date()), kind, amt))
    pdates = {x.split()[0] for x in dates.get("1359", [])}
    unmatched = sorted({(d, a) for d, k, a in aw if d not in pdates})
    lines.append(f"VERIFY ***1359 Awaiting/Scheduled notices in Robert's mail: {len(aw)}; dated with no Processed ***1359 notice "
                 f"the same day: {unmatched}")
    save("10_notices.txt", "\n".join(lines))


def l_census():
    lines = []
    for q in ("Dixelar", "Payoneer", "Thanks for your payment", "Upwork"):
        rc, o, e = run(["Task_Authoring/tools/persona_view.py", "search", "robert", "gmail", q, "--limit", "300", "--no-hidden", "--json"])
        v = json.loads(guard(o, q))
        subjects = sorted({re.sub(r"\[[A-Z_0-9]+\]", "[T]", str(h.get("subject")))[:50] for h in v["visible"]})
        ids = sorted(h["id"] for h in v["visible"])[:6]
        lines.append(f"VERIFY Robert's mail {q!r}: {v['visible_total']} threads; ids {ids}; subjects {subjects[:5]}")
    d = hg(["search", "gmail", "Thanks for your payment", "--limit", "400", "--compact"])
    leo = sum("leonard" in m["service_file"] for m in d["matches"])
    lines.append(f"VERIFY control, all mailboxes, 'Thanks for your payment': {len(d['matches'])} hits, {leo} in Leonard's "
                 f"mailbox files, scan_complete {d.get('scan_complete')}")
    save("11_census.txt", "\n".join(lines))


def l_base_settlers():
    """The base posts that settle the fair-reading forks, read by search hit in their own month file (never #winddown)."""
    req = [
        ("motmot_returned", "C04UEQVDVB7", "2024-04", "returned"),
        ("motmot_wire", "C04UEQVDVB7", "2024-04", "didn"),
        ("lucas_card", "C04UEQVDVB7", "2024-06", "Lucas"),
        ("chase_closed", "C04UEQVDVB7", "2025-10", "Chase account closed"),
        ("chase_closed_nov", "C04UEQVDVB7", "2025-11", "Chase account closed"),
        ("laptop", "C04UEQVDVB7", "2025-10", "laptop"),
        ("direct_wire", "C04UEQVDVB7", "2025-10", "direct wire"),
        ("telegram_lead", "C05KNDCHAAG", "2025-10", "Telegram distribution"),
        ("oleg_may", "C06MXPL9536", "2024-05", "payoneer"),
        ("lauren_exec", "C07C2866011", "2025-10", "non mobile app store distribution"),
        ("lauren_gmt", "C09KU8U4DPF", "2025-10", "GMT / Marketing plan"),
    ]
    res = {}
    for qid, ch, month, q in req:
        f = f"messages/{ch}/{month}.json"
        d = hg(["search", "slack", q, "--file", f, "--limit", "20", "--compact"])
        res[qid] = {"file": f, "query": q, "scan_complete": d.get("scan_complete"),
                    "hits": [{"pointer": m["parent_pointer"], "text": m["text"][:300]} for m in d["matches"]
                             if m["pointer"].endswith("/text")]}
        for h in res[qid]["hits"]:
            h.update(fields(f, h["pointer"]))
    # the company-card exchange right after the Lucas hit, read by pointer in the same file
    res["lucas_card_next"] = {"file": "messages/C04UEQVDVB7/2024-06.json", "query": "pointers after the Lucas hit",
                              "hits": [dict(pointer=f"/{i}", **fields("messages/C04UEQVDVB7/2024-06.json", f"/{i}", True))
                                       for i in range(112, 116)]}
    for qid in ("lauren_exec", "lauren_gmt"):
        for h in res[qid]["hits"]:
            ch = res[qid]["file"].split("/")[1]
            rc, o, e = run(["Task_Authoring/tools/persona_view.py", "can-see", "robert", "slack", f"{ch}/{h['ts']}"])
            h["can_see"] = guard(o, "can-see").splitlines()[0] if o else e[:200]
    save("12_base_settlers.json", json.dumps(res, indent=1))


def fields(f, pointer, text=False):
    keys = ["ts", "user"] + (["text"] if text else [])
    req = {"items": [{"id": k, "service": "slack", "file": f, "pointer": f"{pointer}/{k}", "max_chars": 400} for k in keys]}
    got = hg(["get-many", "--request", "-", "--compact"], json.dumps(req))["items"]
    return {k: str(got.get(k, {}).get("text", "")).strip('"') for k in keys}


def l_winddown_context():
    """Shutdown state at the clock, read by search in #winddown with the guard on (the excluded ts never reach a file)."""
    d = hg(["search", "slack", "angel", "--file", "messages/C0ADGSZKR3R/2026-02.json", "--limit", "20", "--compact"])
    hits = [{"pointer": m["parent_pointer"], "text": m["text"][:400]} for m in d["matches"] if m["pointer"].endswith("/text")]
    for h in hits:
        h.update(fields("messages/C0ADGSZKR3R/2026-02.json", h["pointer"]))
    d2 = hg(["search", "slack", "Sunset the products", "--file", "messages/C0ADGSZKR3R/2026-02.json", "--limit", "5", "--compact"])
    hits2 = [{"pointer": m["parent_pointer"], "text": m["text"][:300]} for m in d2["matches"] if m["pointer"].endswith("/text")]
    for h in hits2:
        h.update(fields("messages/C0ADGSZKR3R/2026-02.json", h["pointer"]))
    save("13_shutdown_context.json", json.dumps({"winddown_angel": {"scan_complete": d.get("scan_complete"), "hits": hits},
                                                 "winddown_announcement": {"scan_complete": d2.get("scan_complete"),
                                                                           "hits": hits2}}, indent=1))


def l_tools():
    rc, o, e = run(["Task_Authoring/tools/hardness_v2_check.py", "--task-dir", TASK])
    save("14_hardness_v2_check.txt", f"$ hardness_v2_check.py --task-dir {TASK} (rc {rc})\n{o}{e}")
    rc, o, e = run(["Task_Authoring/tools/gradable_surface.py", "gradeable-report", "--task-dir", TASK])
    save("15_gradeable_report.txt", f"$ gradable_surface.py gradeable-report --task-dir {TASK} (rc {rc})\n{o}{e}")


def l_prompt_scan():
    raw = open(PROMPT_PATH, "rb").read()
    text = raw.decode()
    cat = json.load(open(os.path.join(WS, "Evals/references/tools/catalog.json")))
    names = sorted(t["name"] for t in cat)
    params = sorted({p for t in cat for p in (t.get("parameters") or {})})
    words = re.findall(r"[A-Za-z_]+", text)
    tool_hits = [n for n in names if n in text]
    param_hits = sorted({w for w in words if w in params and ("_" in w or re.search(r"[a-z][A-Z]", w))})
    never = ["SVB", "notice", "Leapblock", "Chase", "JPMorgan", "Western Union", "Payoneer", "Deel", "Singular", "contract",
             "warehouse", "Snowflake", "REVENUE", "bucket", "Build", "Marketing", "Company", "returned", "came back",
             "admin_foundersonly", "leapblock", "ENG-", "f_", "d_", "evt_", "C0", "Trello", "board", "P&L", "payee by payee",
             "Lucas", "Oleg", "MotMot", "Dixelar", "receipt", "Can you take care of what he asked for", "Angel note",
             "how to count the money", "working sheet", "Note to angels", "Jan 8", "Nov 23", "first", "then", "finally",
             "I'll", "I’ll", "I need to", "I want to", "I'm going to", "if ", "If ", "but not", "tool", "MCP", "server",
             "make sure", "clean up", "today", "yesterday", "this morning", "#", "*", "\n- ", "1.", "2."]
    hits = {w: text.count(w) for w in never if w in text}
    cw = re.compile(r"[A-Z][a-z]+")
    caps = sorted(set(cw.findall(text)))
    lines = [f"04_Prompt.txt: {len(raw)} bytes, {len(text.split())} whitespace words, sha256 {hashlib.sha256(raw).hexdigest()[:12]}, "
             f"trailing newline {text.endswith(chr(10))}, non-ASCII {sorted({c for c in text if ord(c) > 127})}",
             f"sentences: {len(re.findall(r'[.?!](?:\s|$)', text))}",
             f"catalog: {len(names)} tool names, {len(params)} parameter names; tool names in the prompt: {tool_hits}; "
             f"code-like parameter names in the prompt: {param_hits}",
             f"must-not-appear / register scan (brief §9 and C14-C16 words; counts): {hits}",
             f"capitalised words: {caps}"]
    save("16_prompt_scan.txt", "\n".join(lines))


def l_buckets():
    """Bucket settlers outside Slack: the contract's scope line, the agency mail's subject, the contact row."""
    res = {}
    d = hg(["search", "gdocs", "Telegram distribution", "--limit", "10", "--compact"])
    res["contract_scope"] = {"scan_complete": d.get("scan_complete"),
                             "hits": [{"file": m["service_file"], "pointer": m["parent_pointer"],
                                       "text": re.sub(r"\s+", " ", m["text"])[:160]} for m in d["matches"]
                                      if "f_20a0df3860bb5731d22f07" in json.dumps(m) or "Telegram distribution" in m["text"]][:5]}
    rc, o, e = run(["Task_Authoring/tools/persona_view.py", "search", "robert", "gdocs", "Lauren Brooks", "--limit", "5"])
    res["contract_as_robert"] = guard(o, "gdocs Lauren Brooks")
    rc, o, e = run(["Task_Authoring/tools/persona_view.py", "search", "robert", "gmail", "PERSON_4419_NAME", "--limit", "5", "--no-hidden"])
    res["agency_mail_as_robert"] = guard(o, "gmail PERSON_4419_NAME")
    c = hg(["search", "contacts", "Telegram", "--limit", "10", "--compact"])
    res["contact"] = [{"file": m["service_file"], "pointer": m["parent_pointer"], "text": m["text"][:120]} for m in c["matches"]]
    rows = []
    for m in c["matches"][:3]:
        rows.append(hg(["get", "contacts", "--file", m["service_file"], "--pointer", m["parent_pointer"],
                        "--max-chars", "800"])["text"])
    res["contact_rows"] = rows
    save("17_buckets.json", json.dumps(res, indent=1))


def l_rev6():
    """What rev6 changed, read from the SQL as text (never executed), plus the base records each change rests on."""
    sys.path.insert(0, os.path.join(WS, "Task_Authoring", "tools"))
    from base_check import parse_sql
    raw = open(SQL_PATH, "rb").read()
    rows = parse_sql(raw.decode())
    lines = [f"SQL 01_Universe_Inject.sql sha256 {hashlib.sha256(raw).hexdigest()[:12]}, {len(raw)} bytes; "
             f"INSERT {sum(1 for x in rows if x['op'] == 'insert')}, UPDATE {sum(1 for x in rows if x['op'] != 'insert')}"]
    text = raw.decode().split("\n")
    iss = {}
    for x in rows:
        r = x.get("row") or {}
        if x["table"] == "linear.linear_issues":
            iss[r["id"]] = r["identifier"]
        if x["table"] == "gdocs.docs_documents":
            body = r["body_text"].replace("\\n", "\n")
            hold = [l for l in body.split("\n") if "Combo Fighter" in l and "revenue" in l]
            ln = next(i + 1 for i, l in enumerate(text) if "INSERT INTO gdocs.docs_documents" in l) + 1
            lines.append(f"VERIFY method f_6feda53b2382c63bf47b25 (SQL L{ln}), modified {r['modified_time']}: {hold}")
        if x["table"] == "slack.slack_messages" and r["channel_id"] == "C0ADGSZKR3R":
            lines.append(f"VERIFY ask {r['channel_id']}/{r['ts']} created {r['created_at']}")
    for x in rows:
        r = x.get("row") or {}
        if x["table"] == "linear.linear_comments" and iss.get(r["issue_id"]) in ("ENG-2454", "ENG-2455", "ENG-2459"):
            ln = next(i + 1 for i, l in enumerate(text) if r["id"] in l)
            lines.append(f"VERIFY note {iss[r['issue_id']]} {r['id']} (SQL L{ln}) by {r['author_id']} at {r['created_at']}: {r['body']!r}")
    req = {"service": "linear", "file": "data.json", "queries": [
        {"id": "leonard", "query": "usr_63fffeb4fab5233e", "pointer": "/users", "limit": 3},
        {"id": "arthur", "query": "usr_cc3e90160f490686", "pointer": "/users", "limit": 3}]}
    d = hg(["search-many", "--request", "-", "--compact"], json.dumps(req))
    for k, q in d["queries"].items():
        for m in q["matches"][:1]:
            u = hg(["get", "linear", "--file", "data.json", "--pointer", m["parent_pointer"], "--max-chars", "600"])["text"]
            lines.append(f"VERIFY linear user {k}: {m['parent_pointer']} {u[:200]}")
    # the contract's own scope line behind Leonard's ENG-2455 note
    c = hg(["search", "gdocs", "run and optimize paid UA for Telegram", "--limit", "3", "--compact"])
    lines.append(f"VERIFY contract scope 'run and optimize paid UA for Telegram': hits {[(m['service_file'], m['parent_pointer']) for m in c['matches']]}, "
                 f"scan_complete {c.get('scan_complete')}")
    did = hg(["get", "gdocs", "--file", "data.json", "--pointer", c["matches"][0]["parent_pointer"] + "/document_id"])["text"] if c["matches"] else ""
    lines.append(f"VERIFY that hit is document {did}")
    save("18_rev6.txt", "\n".join(lines))


def l_nb26():
    """NB-26, the platform's Cross-Service Coherence finding: Combo Fighter sales in Slack against the warehouse."""
    out = {}
    for qid, f, q in (("robert_dm", "messages/D07H86MV4DN/2026-02.json", "rotation pack"),
                      ("leonard_purchase", "messages/C07C2866011/2026-02.json", "I can see my purchase")):
        d = hg(["search", "slack", q, "--file", f, "--limit", "5", "--compact"])
        hits = [{"pointer": m["parent_pointer"], "text": m["text"][:200]} for m in d["matches"] if m["pointer"].endswith("/text")]
        for h in hits:
            h.update(fields(f, h["pointer"]))
            rc, o, e = run(["Task_Authoring/tools/persona_view.py", "can-see", "robert", "slack", f"{f.split('/')[1]}/{h['ts']}"])
            h["can_see"] = guard(o, "can-see").splitlines()[0] if o else e[:200]
        out[qid] = {"file": f, "query": q, "scan_complete": d.get("scan_complete"), "hits": hits}
    name = hg(["get", "snowflake", "--file", "snowflake.json", "--pointer", "/tables/4/id"])["text"]
    comment = hg(["get", "snowflake", "--file", "snowflake.json", "--pointer", "/tables/4/comment"])["text"]
    rows = json.loads(get_all("snowflake", "snowflake.json", "/tables/4/rows"))
    gk = next(k for k in ("game_id", "title_id", "game") if rows and k in rows[0])
    per = {}
    for r in rows:
        per[r[gk]] = per.get(r[gk], 0) + 1
    out["iap_transactions"] = {"table": name, "comment": comment[:400], "rows": len(rows), "rows_by_game": per}
    rev = [l for l in open(os.path.join(OUT, "09_revenue.txt")) if "REVENUE_DAILY\" combo" in l]
    out["revenue_daily_combo_fighter_iap"] = [re.sub(r"total [\d,.]+ \(iap ([\d,.]+), ad [\d,.]+\)", r"iap \1", l.strip())
                                             for l in rev]
    save("19_nb26.json", json.dumps(out, indent=1))


def l_payouts():
    """The blind read's ad-payout note: AppLovin's Tipalti payments in Robert's mail against the warehouse's DD ad revenue."""
    tids, want = robert_threads("Tipalti payment processed")
    pay = []
    for f, ms in sorted(bodies(tids.values()).items()):
        for m in ms:
            a = re.findall(r"(?:USD|\$)\s?([\d,]+\.\d{2})", str(m.get("body")))
            if a:
                pay.append((str(m.get("date"))[:10], a[0]))
    rows = json.loads(get_all("snowflake", "snowflake.json", "/tables/12/rows"))
    mon = {}
    for r in rows:
        if r["game_id"] == "domino_delights":
            mon[r["date"][:7]] = mon.get(r["date"][:7], D(0)) + D(str(r["ad_revenue_usd"]))
    tot = sum(D(x.replace(",", "")) for _, x in pay)
    lines = [f"VERIFY Tipalti (AppLovin) payments in Robert's mail: {len(pay)} of {len(want)} threads; {sorted(pay)}; total {tot:,.2f}",
             "VERIFY REVENUE_DAILY domino_delights ad revenue by month from 2025-01: "
             + ", ".join(f"{k} {v:,.2f}" for k, v in sorted(mon.items()) if k >= "2025-01"),
             f"VERIFY REVENUE_DAILY domino_delights ad revenue 2025-01 onwards: {sum(v for k, v in mon.items() if k >= '2025-01'):,.2f}"]
    save("20_payouts.txt", "\n".join(lines))


LOOKUPS = [l_context, l_slack_ids, l_entity, l_checksql, l_persona_search, l_linear, l_revenue, l_notices, l_census,
           l_base_settlers, l_winddown_context, l_buckets, l_rev6, l_nb26, l_payouts, l_tools, l_prompt_scan]


def lookups(only=None):
    for fn in LOOKUPS:
        if only and fn.__name__ not in only:
            continue
        print(f"... {fn.__name__}", flush=True)
        fn()
    print("lookups done:", sorted(os.listdir(OUT)))


# ------------------------------------------------------------------ report

PROMPT = open(PROMPT_PATH, encoding="utf-8").read()
SPANS = []


def Q(s):
    """A prompt span, quoted. Stops the build if it is not an exact substring of 04_Prompt.txt."""
    if s not in PROMPT:
        sys.exit(f"STOP: span not in 04_Prompt.txt: {s!r}")
    SPANS.append(s)
    return f'"{s}"'


def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in rows:
        if len(r) != len(head):
            sys.exit(f"STOP: row has {len(r)} cells, header {len(head)}: {r[:2]}")
        out.append("| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in r) + " |")
    return "\n".join(out)


def verify_lines(name, prefix="VERIFY"):
    with open(os.path.join(OUT, name)) as f:
        return [l.rstrip() for l in f if l.startswith(prefix)]


BLIND_LINE = ("A blind subagent read of this exact text on the rev6 SQL predicted the same: Unique Ground Truth 5, Clarity 5, "
              "Cross-Service Coherence 5 and Business Function 5, with 'no open fork'. It reproduced the build costs "
              "959,342.64 / 544,433.44 / 72,685.61, Company 49,625.00 plus BGN 1,999 and Marketing 73,965.63, and brought in "
              "12,331.25 / 11.99 with Combo Fighter's left off (Self-review).")
BLIND_ROWS = [
    ["Unique Ground Truth 5. All 22 payees settled by a record Robert can read, including Lauren Brooks as Marketing on "
     "comment_990674712ad0127e26f780eadb5418ea and Martin's laptop as Company. Build 959,342.64 / 544,433.44 / 72,685.61; "
     "five reason comments (ENG-2439, ENG-2442, ENG-2447, ENG-2450, ENG-2459)",
     "Agrees with the fair-readings table and the verification log's arithmetic, figure for figure"],
    ["Clarity 5; '3 at worst' on two readings it judged settled: Combo Fighter's revenue in the reply (the prompt's general "
     "words against the doc's specific carve-out, which 'should govern'), and thread against top-level",
     "Agrees with C7: the method's hold governs the one figure and the writes do not change; placement is the same write "
     "(finding 1 is for the rubric)"],
    ["Cross-Service Coherence 5. NB-26 'avoided by design': D07H86MV4DN/1770782454.127069 against the warehouse's Combo Fighter "
     "IAP of 0, with the task leaving Combo Fighter's revenue off. NB-1 and NB-6 not triggered; NB-24 uses only injected "
     "comments. Watch NB-12 and NB-23",
     "Agrees with C22 (check_r1/19_nb26.json). NB-12 (key on account endings, never payee names) is already in brief §4b. "
     "NB-23 is a rubric-stage note: grade Singular's two paid wires (31,250.00), never the invoice total"],
    ["Business Function 5; '3 at worst' if a reviewer reads the payee reconciliation as Finance / Ops",
     "Agrees with C4 and the platform's measured 5"],
    ["Residual risk it judged settled: an agent might put Lucas's Western Union payments on a separate line, so ENG-2447 "
     "would need no reason", "Settled: 'Every payee keeps its line, even at zero' gives one line per payee, and ENG-2447's "
     "13,975.00 differs from its notices' 6,450.00 (check_r1/10_notices.txt), so its reason stands (f_6feda53b2382c63bf47b25)"],
    ["Low-impact, not graded: AppLovin payouts exceed Domino Delights' warehouse ad revenue in some months, and the payouts "
     "are not split by game", "Checked this run (check_r1/20_payouts.txt). Robert's mail holds 8 Tipalti payments, May 2025 "
     "to Jan 2026, totalling 5,184.00. None states the game or month it pays for. Their shape follows the warehouse's "
     "Domino Delights ad revenue a month later, and their total stays below the warehouse's 7,337.72 for 2025 onward. No "
     "per-game or per-month contradiction can be shown, the brought-in figure is the table total the method names, and the "
     "platform did not raise it: not a C22 finding"],
    ["It wrote no files; the harness kept one large search output in its own tool-results folder", "Outside this check's "
     "folders; nothing it read was saved into check_r1/"],
]


def build():
    raw = open(PROMPT_PATH, "rb").read()
    wc, sha = len(raw.decode().split()), hashlib.sha256(raw).hexdigest()[:12]
    if (wc, sha) != (109, "d0cb08476d23"):
        sys.exit(f"STOP: 04_Prompt.txt is {wc} words / {sha}; this report was written for 109 / d0cb08476d23")
    sql_sha = hashlib.sha256(open(SQL_PATH, "rb").read()).hexdigest()[:12]
    if sql_sha != "ad50f039b5c2":
        sys.exit(f"STOP: 01_Universe_Inject.sql is {sql_sha}; this report was written for rev6 ad50f039b5c2")
    if not BLIND_ROWS:
        sys.exit("STOP: the rev6 blind read has not been folded in")
    clock = json.load(open(os.path.join(WF, "00_Task_Context.json")))["universe"]["clock_line"]
    rev = verify_lines("09_revenue.txt")
    notices = verify_lines("10_notices.txt")
    census = verify_lines("11_census.txt")
    L = []
    P = L.append

    P("# Prompt Check — robert_seed_bets")
    P(f"> Prompt: 04_Prompt.txt · {wc} words · sha256 {sha} · {clock} · checked 2026-11-08 against 04_Prompt_Writing_Brief.md "
      "(2026-11-08, rev6, SQL ad50f039b5c2) · release task-quality-v1")
    P("> Suggested wording is allowed under the repository exception. Check clean ordinary writing, role plausibility, no "
      "hints/riddles and every fair outcome.")
    P("")
    P(clock)
    P("")
    P("Robert (robert@harmonygames.co) · Co-founder & Creative Director · Executive · Finance · Analysis and synthesis · "
      "long-horizon (Long Horizon) · Easy (V3 cap below 90 %) · normal universe, Robert's today Saturday Feb 14, 2026. "
      "Upstream: injection rev6 (01_Universe_Inject.sql sha256 ad50f039b5c2, 123 INSERT + 2 UPDATE; injection gate PASS pasted "
      "in 01_Grounding_Dossier.md, hg.py lint FAIL 0 CHECK 0), 03_Error_Async_Config.txt (Friction: none, gate PASS "
      "b51534f72800), no reference files, brief gate PASS (04_Prompt_Writing_Brief.md#90722254898a).")
    P("")
    P("Platform history. The Portal reviewed this exact prompt text with the rev4 records "
      "(plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md, attempt 6aeed82596dcfe103f9f74d9; its stored SQL copy hashes "
      "872bbb30…, 74,429 bytes, on which /injection passed). /prompt failed at 2: Unique Ground Truth 2 and Clarity 1 on Lauren "
      "Brooks's bucket (its I1, I2), and Cross-Service Coherence 1 on Combo Fighter's revenue against NB-26 (its I3). Every "
      "other dimension scored 5, Business Function included, and its dataset-similarity gate passed (nearest 0.676, distinct). "
      "Rev6 changes records only (run_forensics/rev4 against rev6, check_r1/18_rev6.txt): a third Leonard note on ENG-2455, "
      "the method's hold on Combo Fighter's revenue, and ENG-2454's note naming the laptop; the later notes on ENG-2456 to "
      "ENG-2459 move by about 1.5 minutes and all stay before the ask. This check re-runs C1–C24 on rev6 and tests the "
      "platform's three findings directly in C6, C7 and C22.")
    P("")
    P("04_Prompt.txt was read byte for byte: 535 bytes, ASCII only, no trailing newline, six sentences, 109 whitespace words, "
      "sha256 d0cb08476d23 before and after this run (check_r1/16_prompt_scan.txt). Every lookup ran in this run, on rev6, "
      "through Task_Authoring/tools/hg.py, persona_view.py (can-see, search, check-sql on the SQL) and entity.py; the raw "
      "outputs are in Working_Files/plan/check_r1/ (written by plan/assemble_check.py lookups). Earlier leads were "
      "re-verified, not reused.")
    P("")

    # ---------------------------------------------------------- summary
    P("## Summary")
    P("")
    P("- Fail 0 · Non-fail 0 · Advisory 2 (C6: two gradable-surface slots are narrower than the accepted outcomes, a "
      "rubric-stage risk; C20: relative day names) · UNVERIFIED none.")
    P("- The platform's three findings, re-tested on rev6: Lauren Brooks's bucket (I1, I2) is settled by Leonard's own note on "
      "ENG-2455 (C6, C7); Combo Fighter's revenue (I3) is held by the method on the page, the deck and the reply, and graded "
      "nowhere (C7, C22); the prompt's 'what each bet cost to build and brought in' does not conflict with that hold, because "
      "the prompt hands the counting to the method that carries it (C7, C18).")
    P("- Checks clean: C1, C2, C3, C4, C5, C7, C8, C9, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C21, C22, C23, C24.")
    P("- Calibration self-test (prompt_qc_cases.json, 15 cases): no FAIL case matched; every PASS control or case that applies "
      "is matched (table below).")
    P("- Predicted /prompt band: PASS (no Fail, no Non-fail, no UNVERIFIED hard gate among C4, C6, C17, C18, C19). " + BLIND_LINE)
    P("- Status: READY FOR /prompt (after /injection on rev6, since the SQL changed).")
    P("")

    # ---------------------------------------------------------- findings
    P("## Findings")
    P("")
    P(table(["#", "Check", "Dimension · severity", "Quoted span", "Rule (source)", "Defect"], [
        ["1", "C6", "Unique Ground Truth · Advisory (rubric stage)", Q("reply to him in #winddown"),
         "Eval 1 §2.1 (accept every fair reading); playbook 04 C6; brief §12",
         "Not a prompt defect. The prompt fixes the channel and recipient, and §4b and the sidecar accept a thread under "
         "C0ADGSZKR3R/1770945859.212469, a thread under C0ADGSZKR3R/1770945821.640039, or a top-level post. The rev6 surface "
         "(29 slots, weight 91) still has D4 read only the thread of 1770945821.640039, and D1 only the root "
         "d_9f7ba94f7526d54d8482ba where §4b accepts any folder Robert owns (01_Gradable_Surface.json). The rubric must accept "
         "all three reply placements and any Robert-owned folder, or it rejects a fair run. The platform agrees the placement "
         "is not a fork ('A thread reply and a top-level #winddown reply reach the same recipient in the same channel')."],
        ["2", "C20", "Alignment with Today's Date · Advisory", Q("On Thursday") + " … " + Q("on Tuesday"),
         "Prompt Writing §4.2 prefers absolute dates; Eval 1 §2.8 allows relative wording that resolves to one window",
         "Relative day names. Each resolves to one record: Leonard's ask C0ADGSZKR3R/1770945821.640039 is 2026-02-13T01:23:41Z = "
         "Thu Feb 12, 5:23 PM PST, and the angel calls evt_f21476dc404329f67fd60d are Tue Feb 17, 9:00–10:30 AM PST "
         "(17:00–18:30Z), a future meeting. The platform scored Today's Date 5 on this text. No change suggested."],
    ]))
    P("")
    P("Suggested wording: none. Both findings are Advisory; finding 1 is for the rubric stage.")
    P("")

    # ---------------------------------------------------------- fair readings
    P("## Fair readings (accepted outcomes)")
    P("")
    P("Reading A is the best-supported reading and Reading B the strongest alternative; where the platform raised a fork, its "
      "own Reading B is the one tested. Each material difference is settled by the prompt, a source the prompt incorporates "
      "(Leonard's two #winddown posts, and through them the method f_6feda53b2382c63bf47b25 and the working sheet "
      "f_3304033843904a426f3c00), a newer source, source identity or scope, or it is accepted as a second fair outcome with "
      "the same material result (Eval 1 §2.1). Every settling record is readable by Robert (check_r1/05_check_sql.txt, "
      "06_can_see.txt; Linear is unscoped). The sidecar outcome_reviews.prompt-check is rewritten in this run and bound to the "
      "04_Prompt.txt digest (plan/write_check_evidence.py).")
    P("")
    P(table(["Deliverable", "Reading A", "Reading B (strongest alternative)", "Resolution and evidence"], [
        ["Sheet: owner and place", "A new Google Sheet Robert owns in his Drive (root d_9f7ba94f7526d54d8482ba, or a folder he "
         "owns), any title", "Fill in Leonard's own working sheet f_3304033843904a426f3c00, which Robert can edit",
         "Settled by the prompt (" + Q("Build that page as a sheet in my Drive") + ") and by source identity: "
         "C0ADGSZKR3R/1770945859.212469 'keep yours in your drive'; the working sheet sits in Leonard's folder "
         "d_63fffeb4fab5233ed5bb73 (SQL L10). Folder and title are representational (§4b)."],
        ["Sheet: form", "A spreadsheet", "A one-page doc (" + Q("one straight page") + ")",
         "Settled by the prompt: " + Q("Build that page as a sheet") + ". A doc beside the sheet changes no graded write."],
        ["Sheet: layout and rows", "The working sheet's eight columns (Payee, Name on the bank, Bucket, Domino Delights, ZM, "
         "Combo Fighter, Company, Note; SQL L20), one row per payee, 22 rows ENG-2438 to ENG-2459, zero rows kept",
         "A free layout, or only the payees that carry money",
         "Settled by the incorporated records: 'use the layout of my Angel note working sheet' (C0ADGSZKR3R/1770945859.212469) "
         "and 'Every payee keeps its line, even at zero' (f_6feda53b2382c63bf47b25). Column order and extra columns are free."],
        ["Sheet: build cost per bet", "Domino Delights 959,342.64 · ZM 544,433.44 · Combo Fighter 72,685.61",
         "The notices by date, as on the working sheet and the deck: 984,888.21 / 608,820.50 / 73,685.61 ($985K / $609K / $74K)",
         "Settled by authority: the method says 'A notice is where you start, not the last word', keeps Marketing 'out of build "
         "cost', puts Company in 'the Company column', and 'replaces the quick plan I left on our board' (Trello "
         "698e55f9af74d68d679de7b3 'add up the notices by date and round them'). Re-derived this run from Robert's own mail "
         "(check_r1/10_notices.txt): the by-date sums are exactly B. B less the Marketing lines (16,428.57; 46,201.50; 6,085.56; "
         "3,750.00; 1,500.00; 125.00) and Company lines (31,250.00; 7,500.00; 7,175.00; 3,200.00; 500.00), the returned ***8605 "
         "wire (4,032.00) and ENG-2450's 4,000.00, plus Leapblock's unnotified first wire (33,290.00) and Lucas's receipts "
         "(7,525.00), gives A to the cent."],
        ["Sheet: ENG-2455 Lauren Brooks (platform I1)", "Marketing: 500.00 under ZM and 1,000.00 under Combo Fighter by date, "
         "outside both build totals",
         "The platform's B: Build, as a monthly contractor on the team (contact 564155d70112411151e512a6 'Telegram Contractor', "
         "SQL L95; 'the contract I sent out in Oct, $500 a month'), which makes ZM 544,933.44 and Combo Fighter 73,685.61. Its "
         "C, Company, it excluded itself",
         "Settled on rev6 by source identity and authority. Leonard, who wrote the method, adds on her own issue 'her contract "
         "had her running our paid UA on telegram, so she’s marketing, not build' (ENG-2455 "
         "comment_990674712ad0127e26f780eadb5418ea, SQL L234, by usr_63fffeb4fab5233e = leonard.hayes@harmonygames.co, "
         "2026-02-13T00:45:13Z, before the ask). Her contract bears it out: 'user acquisition: run and optimize paid UA for "
         "Telegram, manage budgets, creatives, and funnels' (f_20a0df3860bb5731d22f07, check_r1/18_rev6.txt), and the method's "
         "'Marketing is anything made or bought to get installs' takes it. C05KNDCHAAG/1760125440.959149, "
         "C07C2866011/1760309256.938589 and her own C09KU8U4DPF/1760369975.840689 ('build a GMT / Marketing plan') agree. The "
         "platform's missing record ('Leonard's own comment on ENG-2455 … would do it') now exists."],
        ["Sheet: ENG-2454 Martin ***3801", "1,999.00 BGN on the Company line, outside every dollar total",
         "Build, ZM by date, kept in BGN: the platform's reading on rev4 ('paid him direct for this one, not through "
         "Leapblock'); or converted to USD",
         "Settled on rev6 by the note itself: 'paid him direct for his laptop, not through Leapblock' (ENG-2454 "
         "comment_e89f05a3984064bdb00bc2b1fe6ffee2, SQL L224, by usr_cc3e90160f490686 = arthur.blake@harmonygames.co), with "
         "the laptop exchange C04UEQVDVB7/1761844454.096829 'did you handle Martin’s laptop?' and C04UEQVDVB7/1761844624.408899 "
         "'we are doing that as direct wire'. The method puts 'equipment' in Company and says 'Anything not paid in dollars "
         "stays in its own currency next to the line'. Cell or Note both accepted (§4b)."],
        ["Sheet: ENG-2439 Leapblock", "407,944.00 (Domino Delights 337,594.00, ZM 59,250.00, Combo Fighter 11,100.00)",
         "374,654.00, the 29 Processed notices ('what the banks say is our ground source of truth')",
         "Settled by authority and a newer source: 'If someone we paid closes out their file with us and tells us what they "
         "received, that beats the notices for them' and Leapblock's closing post C05URGU759U/1770971846.479179 (Feb 13, 2026: "
         "30 wires, 407,944, the first 33,290 on 13 Sep 2023). The notices tie to it by year once the 2023-09-13 33,290.00 "
         "Awaiting wire, which no Processed notice follows (the first Processed ***1359 notice is 2023-10-02), is added "
         "(check_r1/10_notices.txt). Case K49-newer-source; the platform's F3 agrees."],
        ["Sheet: ENG-2442 MotMot", "37,056.00 (***3341, ***8605)", "41,088.00: the ***8605 notice of 2024-04-02 says Processed",
         "Settled by authority: 'Take a notice as paid unless one of us has said the money came back' with "
         "C04UEQVDVB7/1712331142.975829 'This wire didn’t go through', C04UEQVDVB7/1712331718.859679 'Fixed up and resubmitted "
         "the payment' and C04UEQVDVB7/1712901800.684259 'bank returned our money' (check_r1/12_base_settlers.json); "
         "platform F2."],
        ["Sheet: ENG-2447 Lucas", "13,975.00", "6,450.00 from the notices only; 8,600.00 counting the forwarded receipt twice; "
         "or the transfers with fees",
         "Settled by authority: 'If we paid a contractor some other way, it goes in only if a receipt for it reached your mail, "
         "at the amount sent, not the fee'. Robert's mail holds five Western Union transfers by tracking number, 7,525.00, plus "
         "one forwarded copy (check_r1/10_notices.txt); he paid 'via company card' (C04UEQVDVB7/1719603595.852129); "
         "platform F6."],
        ["Sheet: ENG-2450 JPMorgan ***3203", "Zero, no cost bucket (any no-cost label)", "4,000.00 as Company, or Build by date",
         "Settled by a newer source under the method: Arthur's mail in Robert's INBOX "
         "robert@harmonygames.co/<CAOOpSqA2MTKGlKETvkoKqFfq1MaIktcGcH9cj21BJMAMN4Ok00@mail.gmail.com> (Feb 13, 2026) 'That was "
         "our own Chase account … So it never left the company', with 'Money we moved between our own accounts isn’t spending, "
         "no bucket for that'. Chase was the company's (C04UEQVDVB7/1761954952.006759 'Chase account closed'); platform F4."],
        ["Sheet: ENG-2459 Oleg ***9368", "Zero, Marketing, a reason first", "125.00 from the notice, or the Payoneer re-send "
         "counted from the Dixelar mails",
         "Settled by authority: Leonard's note 'that wire came back the same day, I’d already re-sent it through payoneer' "
         "(comment_3906b5b40dfcdabdc83381f0060bac82, SQL L262, 2026-02-13T00:58:46Z) meets the came-back test, and the re-send "
         "needs a receipt in Robert's mail. His mail holds two 'Dixelar sent you a payment request' threads "
         "(robert@harmonygames.co/1798239548116390324, robert@harmonygames.co/1811158112675912556) and no 'Thanks for your "
         "payment' receipt: 0 in his mail, 6 in Leonard's, scan complete (check_r1/11_census.txt). A request is not a receipt, "
         "and Leonard's receipts are outside Robert's view; platform F5 and DR2 agree. The line is Marketing, so no build total "
         "moves."],
        ["Sheet: ENG-2443 Singular", "Company", "Marketing (attribution serves ads), or Build by date",
         "Settled by authority: ENG-2443's note 'attribution tool, not one game' meets 'Company is legal, tools … anything "
         "else that wasn’t for one of the three games'; platform F8."],
        ["Sheet: Marketing and Company placement", "Marketing dollars in the bet columns by date and outside each build total; "
         "Company 49,625.00 in the Company column", "Marketing in its own column or only in the Note; Company also in a bet cell",
         "Both accepted: same build totals and the same Company figure. The method says 'list it under its bet by date like the "
         "rest, but keep it out of build cost' and 'that goes in the Company column' (§4b, material figure / representational "
         "cell)."],
        ["Sheet: brought in (platform I3)", "Domino Delights 12,331.25 and ZM 11.99 from ANALYTICS.MONETIZATION.REVENUE_DAILY, "
         "anywhere on the sheet; Combo Fighter's left off (blank, or marked held)",
         "Combo Fighter's warehouse figure on the sheet as well, because the page is " + Q("what each bet cost us to build and what it brought in")
         + "; or the figures only in the reply; or REVENUE_DAILY_V2",
         "The first is settled by authority and scope: the method, which the prompt incorporates (" + Q("He laid out how he wants it counted and how it should look")
         + "), says 'Leave Combo Fighter’s revenue off for now, on the page, on the deck and when you tell me, until we’ve "
         "checked its first sales' (f_6feda53b2382c63bf47b25, SQL L15). It governs exactly that one figure and leaves Domino "
         "Delights and ZM standing. Reply-only is settled by " + Q("Build that page as a sheet") + ". V2 is accepted: equal "
         "sums (check_r1/09_revenue.txt). No surface slot grades a Combo Fighter figure (01_Gradable_Surface.json: V1, V2 only)."],
        ["Sheet: sharing", "leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co, any role",
         "'Blake' read as someone other than Arthur Blake",
         "Settled: entity.py resolve 'Blake' gives one candidate, arthur.blake@harmonygames.co (check_r1/03_entity.txt), and "
         "C0ADGSZKR3R/1770945859.212469 says 'share it with Blake and me'."],
        ["Linear: Payee history issues", "All 22 (ENG-2438 to ENG-2459) to Done, with a reason comment first on ENG-2439, "
         "ENG-2442, ENG-2447, ENG-2450 and ENG-2459", "Move only the five that differ; or leave the states and only comment; "
         "or comment on ENG-2454 or ENG-2455 as well",
         "The first two are settled by authority, the method's last paragraph: 'move each payee’s issue to Done once its line is "
         "right. If your figure isn’t what the notices add up to, say why on the issue first.' The third is accepted: an extra "
         "comment is not penalised (§4b). ENG-2455's figure (1,500.00) equals its notices, so it needs no reason. Done is a "
         "team_ENG state (ENG-100, check_r1/08_linear_base.json)."],
        ["Reply: placement", "A thread under C0ADGSZKR3R/1770945859.212469, the post that says 'tell me here'",
         "A thread under C0ADGSZKR3R/1770945821.640039, or a top-level post in C0ADGSZKR3R",
         "All three accepted: same channel, recipient, contents and write, slack_send_message with or without thread_ts "
         "(Eval 1 §2.1 check 5; platform F21). The prompt says only " + Q("reply to him in #winddown") + ". Finding 1 records "
         "that surface D4 is narrower."],
        ["Reply: what each bet brought in", "Domino Delights 12,331.25 and ZM 11.99, with Combo Fighter's left out or said to "
         "be held until its first sales are checked",
         "Combo Fighter's warehouse figure given too, because the prompt asks for " + Q("what each bet cost to build and brought in"),
         "Settled by authority, scope and source identity: the hold names the reply ('and when you tell me'), the prompt hands "
         "the counting to Leonard's method, and both the ask and the hold are Leonard's. The posts (01:23Z) are later than the "
         "doc's last edit (00:41Z) but do not override it: the first sends the counting to the doc ('how I want it counted is in "
         "the doc I just wrote') and the second restates the ask. A Combo Fighter figure is outside §4b's acceptance, and no "
         "slot grades it."],
        ["Reply: the deck", "Say what changes: the three cost figures move from $985K / $609K / $74K to the new ones, and the "
         "brought-in slide ('What each brought in: to fill in') gets Domino Delights and ZM, Combo Fighter's still off",
         "Edit the deck f_a4b3c4287a4314d8e532e1; or fill all three revenue figures on the slide",
         "Settled by source identity: Leonard's 'what changes on the deck, I’ll update it myself' (C0ADGSZKR3R/1770945859.212469), "
         "and the prompt asks for " + Q("what changes on the draft deck") + " in the reply; the hold covers the deck too ('on "
         "the deck'). An edit is not penalised (§4b)."],
        ["Reply: build figures", "Each bet's build cost, exact or rounded", "Each bet's total spend, Marketing and Company "
         "included", "Settled by the prompt (" + Q("what each bet cost to build") + ") and the method ('keep it out of build "
         "cost')."],
    ]))
    P("")
    P("BOTH_FAIR_FIGURE: none. Every figure fork above is settled by a newer source or the incorporated method, so no reported "
      "figure is left to a choice between sources (cases K49-newer-source and K50-both-fair-figure).")
    P("")

    # ---------------------------------------------------------- calibration
    P("## Calibration self-test (prompt_qc_cases.json, 15 calibration_cases)")
    P("")
    P(table(["Case", "Rule", "Expected", "This prompt"], [
        ["K11-staged-errors", "staged_errors", "FAIL", "not matched: spelling, capitals and punctuation are clean"],
        ["K11-control-spelled-correctly", "staged_errors", "PASS", "matched"],
        ["K31-trap-hint", "trap_hint_or_riddle", "FAIL", "not matched: no line voices a doubt about any payee or figure; "
         "'He laid out how he wants it counted' points at a record"],
        ["control-symptom", "trap_hint_or_riddle", "PASS", "matched in kind: it names Leonard's ask, not a cause"],
        ["K42-hidden-destination", "hidden_destination", "FAIL", "not matched: Drive, the Payee history project and #winddown "
         "are named"],
        ["K47-hidden-destination", "hidden_destination", "FAIL", "not matched: #winddown is named, not described"],
        ["K44-hidden-destination", "hidden_destination", "FAIL", "not matched: the reply's place is named"],
        ["control-named-destination", "hidden_destination", "PASS", "matched: 'reply to him in #winddown' has the shape of "
         "'post the summary in #winddown'"],
        ["K1-audit-form", "audit_form", "FAIL", "not matched: no reconcile / classify / complete-the-record verbs"],
        ["K43-audit-form", "audit_form", "FAIL", "not matched"],
        ["K44-if-chain", "if_chain", "FAIL", "not matched: no 'if' in the prompt (check_r1/16_prompt_scan.txt)"],
        ["control-plain-request", "audit_form", "PASS", "matched: one plain ask, the rules in the records"],
        ["K43-departed-person-premise", "false_state_premise", "FAIL", "not matched: only Leonard, Robert and Blake act, all "
         "active at the clock (entity.py last activity 2026-02-13; Arthur's mail Feb 13)"],
        ["K50-both-fair-figure", "ugt_both_fair_figure", "PASS", "not applicable: no figure is left open between sources"],
        ["K49-newer-source", "ugt_both_fair_figure", "PASS", "matched in kind: Leapblock's statement and Arthur's Chase mail are "
         "newer sources that settle their figures"],
    ]))
    P("")

    # ---------------------------------------------------------- C1-C24
    P("## Check results (C1–C24)")
    P("")
    P(table(["#", "Result", "Evidence"], [
        ["C1", "clean", "109 whitespace words, inside 20–4,000 (check_r1/16_prompt_scan.txt)"],
        ["C2", "clean", "task_context.py --require-source (no --write; output identical to Working_Files/00_Task_Context.json): all "
         "eight V3 fields; persona robert resolves in roster.json ('Co-Founder & Creative Director', case only); source ready, "
         "KB bound, freeze 2026-02-14T00:00:00Z (check_r1/01_context.txt)"],
        ["C3", "clean", "A co-founder in the wind-down: Leonard @-mentions Robert in #winddown and asks him to own the page, 'you "
         "know what each of these people did better than I do, can you own it?' (C0ADGSZKR3R/1770945821.640039). Robert sent "
         "contractor pay 'via company card' (C04UEQVDVB7/1719603595.852129) and weighed in on booking the returned wire "
         "(C04UEQVDVB7/1712901837.860709). Voice judged against the role only (A-27). The platform scored Persona 5"],
        ["C4", "clean", "Finance: an account of fundraising money spent, as a spreadsheet, with deck corrections (taxonomy screen "
         "9). Analysis and synthesis: reconcile notices, notes, Slack, receipts and the warehouse under the method, and compute "
         "the totals. Executive maps to Founders / Exec / Strategy: a founder deliverable for the angel calls "
         "(evt_f21476dc404329f67fd60d). The platform scored this exact text Business Function 5, Competency 5 and Task Skill 5; "
         "rev6 changes no part of the function. The rev4 check's Non-fail on Business Function rested on a blind local read "
         "and is withdrawn on the platform's measured 5. The sheet is the authored artifact"],
        ["C5", "clean", "Ambiguity, dynamic change and multi-source are load-bearing (brief §8; platform Complexity 5). The prompt "
         "restates no rule, column or figure; hardness_v2_check 'CLEAN RULE_IN_PROMPT no run of 8 resolver words in the prompt' "
         "on rev6 (check_r1/14_hardness_v2_check.txt)"],
        ["C6", "Advisory (finding 1)", "Fair readings table. The platform's fork I1 (Lauren Brooks, its Readings A, B and C) is "
         "settled on rev6 by Leonard's own note on ENG-2455 (comment_990674712ad0127e26f780eadb5418ea), which her contract bears "
         "out. Its rev4 reading of Martin as Build is settled by ENG-2454's laptop note. Combo Fighter's revenue is held by the "
         "method. Every other material field is settled as the platform's own F2–F21 found; the open fields are representational "
         "and accepted. Sidecar outcome review rewritten this run. Surface slots D4 and D1 are narrower than §4b (finding 1)"],
        ["C7", "clean", "Platform I2 (Clarity 1) was the same Lauren fork, and with it settled the contents no longer diverge. "
         "Writes under every reading: create a sheet, write its values, share it twice, move 22 issues, add 5 reason comments, "
         "send one Slack message. Prompt against the hold: " + Q("what each bet cost to build and brought in")
         + " meets 'Leave Combo Fighter’s revenue off for now, on the page, on the deck and when you tell me'. The writes are the "
         "same under both readings; only one figure in the contents differs, and the incorporated method governs it (fair "
         "readings), so this is not an Action Decision Ambiguity or two incompatible instructions: the reply gives what each bet "
         "cost and what Domino Delights and ZM brought in, and says Combo Fighter's is held. The channel, recipient, time and "
         "form are fixed; thread or top-level is the same write. No 'I'll [verb]' in the prompt; Leonard's own 'I’ll update it "
         "myself' keeps the deck his"],
        ["C8", "clean", "(a) Both posts, the method and the working sheet are Robert-visible (check-sql PASS on rev6); (b) the "
         "first post names the method by title and the second names the layout sheet, and persona_view search finds no "
         "competing base record (check_r1/07_persona_search.txt); (c) the posts and the method state what is attributed to "
         "them, the hold included; (d) the method states tests, the bet calendar and the hold, no payee figure or total"],
        ["C9", "clean", "No root cause, finding entity, figure or count in the prompt; brief §9 scan finds none of the never-name "
         "items (check_r1/16_prompt_scan.txt: only 'Build' as a verb and the '#' of #winddown hit)"],
        ["C10", "clean", "Only AN1 (Leonard's ask in #winddown) and AN2 (the Payee history project) are named. 'the draft deck' "
         "is Leonard's own description in the second post, not the deck's title, and the deck is a stale summary"],
        ["C11", "clean", "Every write depends on the investigation: the rows and totals, which five issues take a reason, and the "
         "reply's figures"],
        ["C12", "clean", "Gmail (notice sums, receipts, Arthur's mail), Snowflake (brought in), Slack (the ask, #admin_foundersonly, "
         "#leapblock), Linear (notes, the ENG-2455 bucket, writes), Docs, Sheets, Slides, Drive, Contacts, Calendar and Trello "
         "carry weight; the platform scored Tool Use 5 with each service changing a graded fact. Tier: the gate re-runs "
         "hardness_gate --profile extreme on the current manifest and SQL (tier.hardness)"],
        ["C13", "clean", "One purpose: Leonard's page before the angel calls (platform Coherence 5)"],
        ["C14", "clean", "No catalog tool or parameter name, no MCP server and no 'tool' (check_r1/16_prompt_scan.txt)"],
        ["C15", "clean", "No first / then / finally and no read order; one dependency phrase orders the reply after the work"],
        ["C16", "clean", "No spec-sheet layout, answer-key clause, staged error, riddle, hedge, hidden destination, audit wording or "
         "if-chain (platform Contrived 5)"],
        ["C17", "clean", "Verification log below: every person, channel, doc, project, date, relationship and state premise was "
         "looked up in this run on rev6 (platform Truthfulness 5 on the same text)"],
        ["C18", "clean", "Catalog writes exist: gsheets_create_spreadsheet, gsheets_values_update, gdrive_share_file, "
         "linear_update_issue (state), linear_create_comment, slack_send_message (thread_ts optional). No conflicting "
         "instructions: the hold narrows one figure inside the counting the prompt delegates (C7). Exact values survive: "
         "REVENUE_DAILY total_revenue_usd is NUMBER(38,2) and sums to the cent through hg.py (check_r1/09_revenue.txt); the "
         "notices carry two decimals (check_r1/10_notices.txt). The sheet link: an Opus 5.5 run on the same catalog created a "
         "sheet with gsheets_create_spreadsheet and posted a docs.google.com/spreadsheets link with slack_send_message "
         "(completed_tasks/robert_llc_takeover_2026-11-06 run_forensics/rev3/precheck/writes.json). gradable_surface.py "
         "gradeable-report on rev6: 'SURFACE.GRADEABLE PASS · 29 slot(s)' (check_r1/15_gradeable_report.txt). The platform "
         "scored Feasibility 5"],
        ["C19", "clean", "Lens 1: check-sql on rev6, verdict PASS with 0 load-bearing rows hidden over 34 ids "
         "(check_r1/05_check_sql.txt); can-see YES on Robert's root and the base settlers (check_r1/06_can_see.txt, "
         "12_base_settlers.json); the NO rows are Arthur's and Leonard's copies of the same mails. Lens 2: no ask reads someone "
         "else's scoped data (platform Persona ACL 5)"],
        ["C20", "Advisory (finding 2)", "Thursday = Thu Feb 12, 5:23 PM PT (past); Tuesday = Tue Feb 17, 9:00 AM PT (a future "
         "meeting). No 'today', 'yesterday' or exact timestamp"],
        ["C21", "clean", "03_Error_Async_Config.txt 'Friction:          none'; no failure or wait is mentioned"],
        ["C22", "clean", "Platform I3 tested directly. The base conflict is real and stays: Robert's DM D07H86MV4DN/1770782454.127069 "
         "'I mean I was sort of shocked that 2 people bought rotation pack..' and Leonard's C07C2866011/1770353490.801449 'I can "
         "see my purchase' stand against IAP_TRANSACTIONS, which has no Combo Fighter row ('absence here means no sales'), and "
         "REVENUE_DAILY's Combo Fighter IAP of 0.00 (check_r1/19_nb26.json). Rev6 takes it out of the task: the method holds "
         "Combo Fighter's revenue 'on the page, on the deck and when you tell me, until we’ve checked its first sales', which is "
         "the platform's own fix 2 ('have him say the Combo Fighter number stays off the page'). The surface grades no Combo "
         "Fighter figure, and the hold's 'first sales' agrees with the Slack side. Other points met in C17–C18 are consistent: "
         "Leonard's ENG-2455 note matches the contract's paid-UA line; ENG-2454's laptop note matches the founders' laptop "
         "exchange; every note precedes the ask (latest 00:58:46Z, check_r1/18_rev6.txt); the ***9368 notice and the Payoneer "
         "re-send are both 2024-05-07 (C06MXPL9536/1715113013.494939); Chase closed Oct 31, 2025 (C04UEQVDVB7/1761954952.006759); "
         "Leapblock's statement ties out. The local injection gate passes on SQL ad50f039b5c2 (hg.py lint FAIL 0 CHECK 0, "
         "01_Grounding_Dossier.md); no Portal /injection has run on rev6 yet"],
        ["C23", "clean", "No supplied sample (Eval 1 §2.9 N/A). The platform's dataset-similarity gate passed for this exact "
         "text: nearest 0.676, 'distinct', none sharing the scenario"],
        ["C24", "clean", "Four write kinds over Sheets, Drive, Linear and Slack"],
    ]))
    P("")

    # ---------------------------------------------------------- verification log
    P("## Verification log")
    P("")
    P("Every row was looked up in this run on rev6: base records through Task_Authoring/tools/hg.py and persona_view.py, seeded "
      "records in 01_Universe_Inject.sql (rev6, sha256 ad50f039b5c2; read as text, never executed) with check-sql for Robert's "
      "view. Raw outputs: Working_Files/plan/check_r1/.")
    P("")
    P(table(["Span", "Type", "Universe record (locator)", "Result"], [
        [Q("On Thursday"), "date", "C0ADGSZKR3R/1770945821.640039 created_at 2026-02-13T01:23:41Z (SQL L46) = Thu Feb 12, 2026, "
         "5:23 PM PST; the second post C0ADGSZKR3R/1770945859.212469 at 01:24:19Z, 5:24 PM PST (check_r1/18_rev6.txt)",
         "match (Pacific day)"],
        [Q("#winddown"), "channel", "hg.py channels.json /154: C0ADGSZKR3R name 'winddown', private, created 1770663237 "
         "(Feb 9, 2026), 7 members incl. EMPLOYEE_0016_SLACK_ID and EMPLOYEE_0038_SLACK_ID (check_r1/02_slack_people_channel.json)",
         "match; Robert a member (can-see YES)"],
        [Q("Leonard"), "person", "hg.py users.json /23: EMPLOYEE_0038_SLACK_ID 'Leonard Hayes' leonard.hayes@harmonygames.co; "
         "entity.py resolve 'Leonard' gives one candidate (check_r1/03_entity.txt)", "match; unique Leonard"],
        [Q("Leonard asked me"), "relationship / event", "C0ADGSZKR3R/1770945821.640039 opens '<@EMPLOYEE_0016_SLACK_ID>' "
         "(users.json /9 = Robert, robert@harmonygames.co) and asks 'can you own it?'", "match"],
        [Q("one straight page on what each bet cost us to build and what it brought in"), "event",
         "C0ADGSZKR3R/1770945821.640039: 'I want one straight page on what each bet cost us to build and what it brought in'",
         "match (Leonard's words)"],
        [Q("each bet"), "entity set", "f_6feda53b2382c63bf47b25 'Domino Delights up to Jan 8, 2025, ZM from Jan 9, 2025 to Nov "
         "23, 2025, Combo Fighter from Nov 24, 2025'; deck slide el_15b213cdfaa1 'What we built: Domino Delights, ZM, Combo "
         "Fighter'", "match; three bets defined by the method"],
        [Q("ahead of his angel calls on Tuesday"), "event / date / relationship", "C0ADGSZKR3R/1770945821.640039 'before I start "
         "the angel calls on tuesday'; evt_f21476dc404329f67fd60d 'Angel calls' on robert@harmonygames.co, 2026-02-17T17:00–18:30Z "
         "(Tue Feb 17, 9:00–10:30 AM PST), organizer leonard.hayes@harmonygames.co (SQL L90; check-sql YES)",
         "match; Leonard's calls, a future meeting"],
        [Q("He laid out how he wants it counted"), "relationship / doc", "C0ADGSZKR3R/1770945821.640039 'how I want it counted is "
         "in the doc I just wrote, Angel note: how to count the money'; f_6feda53b2382c63bf47b25, owner "
         "leonard.hayes@harmonygames.co, created 2026-02-12T23:52:18Z, modified 2026-02-13T00:41:06Z, shared with Robert, now "
         "carrying the Combo Fighter hold (SQL L8, L15; check-sql YES; check_r1/18_rev6.txt)", "match"],
        [Q("and how it should look"), "relationship / doc", "C0ADGSZKR3R/1770945859.212469 'use the layout of my Angel note "
         "working sheet'; f_3304033843904a426f3c00 'Angel note working', owner Leonard, eight columns (SQL L10, L20; check-sql YES)",
         "match"],
        [Q("my Drive"), "destination", "d_9f7ba94f7526d54d8482ba, folder owned by robert@harmonygames.co (persona_view can-see "
         "YES, 'persona owns the file'; check_r1/06_can_see.txt)", "match"],
        [Q("Blake"), "person", "entity.py resolve 'Blake': no exact match, one candidate arthur.blake@harmonygames.co; users.json "
         "/13 EMPLOYEE_0025_SLACK_ID 'Arthur Blake'; last activity gmail 2026-02-13 (check_r1/03_entity.txt)",
         "match; active at the clock"],
        [Q("share it with him and Blake"), "recipients", "C0ADGSZKR3R/1770945859.212469 'share it with Blake and me' = "
         "leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co", "match"],
        [Q("the Payee history project in Linear"), "project", "0742c172-85de-47ed-a111-316e5c8cb187 'Payee history', team_ENG, "
         "started 2026-02-12 (SQL L98), with ENG-2438 to ENG-2459; base linear data.json: 'Payee' in /projects 0 matches and "
         "'Payee history' anywhere 0 matches, scan complete; control 'Zombie Match' in /projects -> /projects/1 "
         "(check_r1/08_linear_base.json)", "match; the only such project"],
        [Q("the way he wants"), "relationship", "f_6feda53b2382c63bf47b25 last paragraph 'On the Linear project: move each "
         "payee’s issue to Done once its line is right. If your figure isn’t what the notices add up to, say why on the issue "
         "first.'", "match; an instruction, not an answer"],
        [Q("reply to him in #winddown"), "channel", "C0ADGSZKR3R/1770945859.212469 'when you’re done tell me here'; Robert is "
         "a member of C0ADGSZKR3R (check-sql YES)", "match"],
        [Q("the draft deck"), "doc", "f_a4b3c4287a4314d8e532e1 'Note to angels (draft)', owner Leonard, created "
         "2026-02-12T22:52:37Z, shared with Robert (SQL L12, L23; check-sql YES); C0ADGSZKR3R/1770945859.212469 'my quick numbers "
         "are on that sheet and on the draft deck'", "match (Leonard's term)"],
        [Q("what changes on the draft deck"), "requested output", "deck slides el_0e414d770865 'What each bet cost to build: "
         "Domino Delights $985K, ZM $609K, Combo Fighter $74K' and el_30f4d02c73c5 'What each brought in: to fill in' (SQL L35, "
         "L39)", "new output, not a premise; changes exist"],
        [Q("what it brought in"), "requested figure", "ANALYTICS.MONETIZATION.REVENUE_DAILY summed through hg.py get "
         "/tables/12/rows, 2,284 rows: domino_delights 12,331.25, zombie_match_3d 11.99 (REVENUE_DAILY_V2 equal; "
         "check_r1/09_revenue.txt); Combo Fighter's held by the method's 'Leave Combo Fighter’s revenue off for now' "
         "(f_6feda53b2382c63bf47b25, SQL L15)", "new output; two values exist to the cent, the third is held"],
        [Q("Build that page as a sheet"), "requested output", "catalog.json gsheets_create_spreadsheet (title, driveFileId); "
         "Robert's root d_9f7ba94f7526d54d8482ba", "new output, not a premise"],
        [Q("with the link to the sheet"), "requested output", "catalog.json slack_send_message (text); hg.py shows no premise",
         "new output, not a premise"],
        [Q("me") + " / " + Q("my"), "persona", "robert@harmonygames.co, roster.json persona_key robert (check_r1/01_context.txt)",
         "match"],
        ["(state) the wind-down", "state premise", "C0ADGSZKR3R created Feb 9, 2026; Leonard's plan there "
         "C0ADGSZKR3R/1770664700.848759 ('close out vendor commitments, and Sunset the products in a controlled way'); "
         "C0ADGSZKR3R/1770934638.035469 (Leonard, Feb 12): 'Reaching out to our angels properly and let them know about the "
         "situation' (check_r1/13_shutdown_context.json); deck slide el_2f133c6a4173 'What happens next: an orderly wind-down'",
         "the angel calls belong to the wind-down; no business-as-usual premise"],
        ["(state) who acts", "state premise", "entity.py last activity: leonard.hayes@harmonygames.co slack 2026-02-13; "
         "robert@harmonygames.co slack 2026-02-13; arthur.blake@harmonygames.co gmail 2026-02-13 (check_r1/03_entity.txt). "
         "No departed person acts", "match"],
    ]))
    P("")
    P("Re-derived values behind the fair readings (aggregates only; full lines in check_r1/09_revenue.txt, 10_notices.txt, "
      "11_census.txt, 18_rev6.txt, 19_nb26.json). Combo Fighter's revenue rows are held by the method and are not listed:")
    P("")
    keep = [l for l in notices if l.startswith(("VERIFY notices", "VERIFY by-date", "VERIFY ending 1359", "VERIFY ending 3341",
                                                "VERIFY ending 5384", "VERIFY ending 6577", "VERIFY ending 8605",
                                                "VERIFY ending 3203", "VERIFY ending 9368", "VERIFY ending 3801",
                                                "VERIFY ***1359 first", "VERIFY Western Union"))]
    keep += [l for l in rev if ("REVENUE_DAILY\" " in l or "REVENUE_DAILY_V2\" " in l) and "combo_fighter" not in l]
    keep += [l for l in census if "Thanks for your payment" in l or "'Dixelar'" in l]
    for l in keep:
        if "11.75" in l:
            sys.exit("STOP: a held Combo Fighter revenue value reached the report")
        P("- hg.py: " + l.replace("VERIFY ", "", 1).replace("[", "(").replace("]", ")").replace('"', ""))
    P("")
    P("Arithmetic from every ending in check_r1/10_notices.txt, bucketed by the method and the notes (Lauren Brooks's ***5384 "
      "as Marketing per ENG-2455): Domino Delights 984,888.21 − 16,428.57 − 25,000.00 − 3,200.00 − 6,075.00 − 7,500.00 − "
      "4,000.00 − 125.00 − 4,032.00 + 33,290.00 + 7,525.00 = 959,342.64; ZM 608,820.50 − 46,201.50 − 6,085.56 − 3,750.00 − "
      "500.00 − 6,250.00 − 1,100.00 − 500.00 = 544,433.44; Combo Fighter 73,685.61 − 1,000.00 = 72,685.61; Company 31,250.00 + "
      "7,500.00 + 7,175.00 + 3,200.00 + 500.00 = 49,625.00, plus 1,999.00 BGN. Brought in: Domino Delights 12,331.25 and ZM "
      "11.99; Combo Fighter's held.")
    P("")

    # ---------------------------------------------------------- brief coverage
    P("## Brief coverage")
    P("")
    P(table(["Brief item (§4 deliverables, §6 triggers)", "Present in the prompt (quoted span, or absent)"], [
        ["AN1 anchor: Leonard's ask in #winddown", Q("On Thursday in #winddown Leonard asked me")],
        ["deadline: the angel calls", Q("ahead of his angel calls on Tuesday")],
        ["§6 count by the method", Q("He laid out how he wants it counted")],
        ["§6 sheet layout (a pointer, no layout clause)", Q("and how it should look")],
        ["§4 the sheet in Robert's Drive", Q("Build that page as a sheet in my Drive")],
        ["§4 / §6 the sheet shared with Leonard and Arthur", Q("share it with him and Blake")],
        ["AN2 anchor and §4 the payee issues to Done, reason first", Q("Work through the Payee history project in Linear the way he wants")],
        ["§6 brought-in figures on the page", Q("what each bet cost us to build and what it brought in")],
        ["§4 the reply in #winddown", Q("reply to him in #winddown")],
        ["§4 reply contents: figures and deck changes", Q("with what each bet cost to build and brought in and what changes on the draft deck")],
        ["§6 the link (the prompt's own trigger)", Q("with the link to the sheet")],
        ["§4b Combo Fighter's revenue held on the page, the deck and the reply", "absent (record trigger: the method's hold sentence, f_6feda53b2382c63bf47b25)"],
        ["§6 the five figures that differ", "absent (record triggers: the method's came-back, closing-file, receipt and own-account sentences)"],
        ["§6 buckets and the bet calendar, Lauren's and Martin's included", "absent (record triggers: the method's Buckets and Which bet paragraphs, the ENG-2455 and ENG-2454 notes)"],
        ["§9 must-not-appear list", "absent: none of its items appears (check_r1/16_prompt_scan.txt)"],
    ]))
    P("")
    L.extend(SELF_REVIEW())
    P("")
    P("## Route")
    P("")
    P("No Fail. The SQL changed (rev6, sha256 ad50f039b5c2), so the GEN_EXECUTION §3 re-run matrix applies: /injection on rev6 "
      "first, then /prompt with 04_Prompt.txt exactly as saved (unchanged, sha256 d0cb08476d23), then a new Opus pre-check and "
      "/hardness. Use the GEN_EXECUTION §7 paste list: the task date, the prompt, all eight assignment fields, the SQL; there "
      "is no error/async configuration to supply (Friction: none) and no reference file. When /prompt and /injection ask the "
      "task date, answer \"February 14, 2026\". A /prompt FAIL is fatal: fix the cause and re-run. Finding 1 goes to the "
      "rubric stage (accept every reply placement and any Robert-owned folder; grade no Combo Fighter revenue figure); "
      "finding 2 needs no edit. After the pair: /create-humantime.")
    text = "\n".join(L) + "\n"
    bad = [s for s in SPANS if s not in PROMPT]
    if bad:
        sys.exit(f"STOP: spans not in the prompt: {bad}")
    for q in re.findall(r'"([^"\n]+)"', text.split("## Findings")[1].split("## Fair readings")[0]):
        if q not in PROMPT:
            sys.exit(f"STOP: a Findings quote is not in the prompt: {q!r}")
    if "11.75" in text:
        sys.exit("STOP: the held Combo Fighter revenue figure appears in the report")
    guard(text, "04_Prompt_Check.md")
    with open(os.path.join(WF, "04_Prompt_Check.md"), "w") as f:
        f.write(text)
    after = hashlib.sha256(open(PROMPT_PATH, "rb").read()).hexdigest()[:12]
    print(f"wrote Working_Files/04_Prompt_Check.md: {len(text)} chars; {len(SPANS)} prompt spans verified as exact substrings; "
          f"04_Prompt.txt sha256 {sha} before, {after} after; SQL {sql_sha}")


def SELF_REVIEW():
    rows = [
        ["C1", "Another tokenizer could put the text outside the field.", "109 whitespace words (check_r1/16_prompt_scan.txt); "
         "the field takes 20–4,000 (GEN_EXECUTION §3).", "none stands"],
        ["C2", "The roster spells the role 'Co-Founder', so the persona might not bind; or the task might be Normal Horizon.",
         "roster.json persona_key robert, role 'Co-Founder & Creative Director' (case only); check_r1/01_context.txt: long-horizon, "
         "Long Horizon, easy, freeze 2026-02-14T00:00:00Z, source ready, identical to 00_Task_Context.json.", "none stands"],
        ["C3", "A Creative Director costing the seed money reads as a CFO's job, and Leonard, who wrote the method, is the natural "
         "owner.", "Leonard hands it to Robert by name (C0ADGSZKR3R/1770945821.640039); Robert sent contractor pay 'via company "
         "card' (C04UEQVDVB7/1719603595.852129); the platform scored Persona 5 (plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md); "
         "a better-fitting colleague is Non-fail at most (Eval 1 §1.1).", "none stands"],
        ["C4", "Business Function could read 3: reconciling 22 payees against bank notices is 'Financial reconciliation', the "
         "Finance / Legal / HR / Ops row, and a blind local read of rev4 scored it 3.", "The platform scored this exact text "
         "Business Function 5 ('a founder deliverable for the angel calls'; plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md), "
         "and task_categories.md says to classify by business purpose. Rev6 changes records only. The measured score outranks "
         "the local read, so the rev4 check's Non-fail is withdrawn.", "none stands"],
        ["C5", "'He laid out how he wants it counted and how it should look' could carry the recipe.", "It names no rule, column "
         "or figure; RULE_IN_PROMPT CLEAN on rev6 (check_r1/14_hardness_v2_check.txt); platform Data Seeding 5.", "none stands"],
        ["C6", "The platform's I1 could still stand: Lauren Brooks as Build on her 'Telegram Contractor' contact and monthly "
         "contract; or Martin as Build, as the platform read rev4; or Leapblock at 374,654, ENG-2459 at 125.00; and a narrow "
         "rubric could reject a fair run.", "Leonard's note on ENG-2455 (comment_990674712ad0127e26f780eadb5418ea, SQL L234) "
         "names her bucket in his own words, before the ask, and her contract f_20a0df3860bb5731d22f07 says 'run and optimize "
         "paid UA for Telegram' (check_r1/18_rev6.txt); ENG-2454's note now names the laptop (SQL L224); Leapblock and ENG-2459 "
         "were already settled on the platform's own F3 and F5. The narrow D4 and D1 slots are finding 1.", "Advisory kept"],
        ["C7", "The prompt's 'what each bet cost to build and brought in' asks for every bet's revenue, while the method says to "
         "leave Combo Fighter's off 'when you tell me': two instructions disagree, and the platform's Clarity 1 was a contents "
         "fork too.", "Same writes either way (one sheet, one slack_send_message; catalog.json); the incorporated method "
         "governs the one figure (Eval 1 §2.1 authority and scope), names the reply itself, and comes from the same requester; "
         "the platform's Clarity 1 rested only on the Lauren fork, now settled (comment_990674712ad0127e26f780eadb5418ea). "
         "Eval 1 §2.6 fails divergent writes, not a governed figure. " + "The blind rev6 read's Clarity result is in the table "
         "below.", "none stands"],
        ["C8", "'He laid out how he wants it counted' could lead to the Trello quick plan instead of the doc, or the doc could "
         "hand over the answer.", "The first post names the doc by title (C0ADGSZKR3R/1770945821.640039); the doc says 'It "
         "replaces the quick plan I left on our board' and states tests and a hold, not payee figures "
         "(f_6feda53b2382c63bf47b25).", "none stands"],
        ["C9", "'each bet' presupposes three bets and 'what changes on the draft deck' presupposes a change.", "Both are Leonard's "
         "words (C0ADGSZKR3R/1770945821.640039, C0ADGSZKR3R/1770945859.212469); neither names a payee, figure, cause or count "
         "(Eval 1 §1.3.3; platform Pre-Solving PASS).", "none stands"],
        ["C10", "'the draft deck' names brief §5 F5, which is marked No.", "It is not the deck's title ('Note to angels (draft)', "
         "f_a4b3c4287a4314d8e532e1) but Leonard's description in C0ADGSZKR3R/1770945859.212469, which the agent reads anyway.",
         "none stands"],
        ["C11", "The issue moves might not depend on what is found.", "The reason comments fall on the five issues whose figure "
         "differs (ENG-2439, ENG-2442, ENG-2447, ENG-2450, ENG-2459), which only the corrections reveal "
         "(check_r1/10_notices.txt).", "none stands"],
        ["C12", "The second service could be trivial.", "Gmail sets every notice sum (check_r1/10_notices.txt), Snowflake the "
         "brought-in figures (check_r1/09_revenue.txt), Linear's ENG-2455 note sets a bucket, and "
         "C05URGU759U/1770971846.479179 moves ENG-2439; the gate re-runs hardness_gate --profile extreme.", "none stands"],
        ["C13", "The Linear sentence could be a bolt-on to the page.", "Leonard put the payees there for this page "
         "(C0ADGSZKR3R/1770945859.212469) and the method ties each issue's Done to its line (f_6feda53b2382c63bf47b25); platform "
         "Coherence 5.", "none stands"],
        ["C14", "'#winddown', 'in Linear' or 'my Drive' could read as tool names.", "No catalog tool or parameter name "
         "(check_r1/16_prompt_scan.txt); natural product names pass (prompt_qc_examples.md row 103).", "none stands"],
        ["C15", "'Build … Work through … When you're done, reply' could be a command list.", "No source or read order is "
         "scripted (Eval 1 §1.3.1); the platform: '\"When you're done\" is one ordering phrase, not a step list' "
         "(plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md).", "none stands"],
        ["C16", "'how it should look' hides the layout like a hidden destination, or 'He laid out how he wants it counted' hints "
         "that the notices are wrong.", "Destinations are named and the clause points at a named record (control-named-destination, "
         "unlike K42-hidden-destination); it voices no doubt (K31-trap-hint not matched); platform Contrived 5.", "none stands"],
        ["C17", "'On Thursday' is false in UTC (Feb 13); 'Blake' could be someone else; a sheet for Tuesday's calls could assume "
         "business as usual after the shutdown.", "2026-02-13T01:23:41Z is Thu Feb 12, 5:23 PM PST (GEN_EXECUTION §0a); "
         "entity.py gives one 'Blake' (check_r1/03_entity.txt); the calls tell the angels 'about the situation' "
         "(C0ADGSZKR3R/1770934638.035469); platform Truthfulness 5 on this text.", "none stands"],
        ["C18", "The prompt asks for every bet's revenue while the method withholds one, which is the 'conflicting instructions' "
         "row of Eval 1 §2.2; or the sheet's link might not be producible.", "The prompt delegates the counting to the method "
         "('He laid out how he wants it counted'), which narrows one figure without contradicting any write (C7); the link is "
         "shown by an Opus 5.5 run on the same catalog (robert_llc_takeover run_forensics/rev3/precheck/writes.json); platform "
         "Feasibility 5.", "none stands"],
        ["C19", "Robert might not see a record that settles a fork, now ENG-2455's note included.", "Linear is unscoped "
         "(Evals/references/persona/acl.md); check-sql on rev6 PASS with 0 load-bearing rows hidden (check_r1/05_check_sql.txt); "
         "can-see YES on the base settlers (check_r1/06_can_see.txt, 12_base_settlers.json).", "none stands"],
        ["C20", "Finding 2 is a false positive, since /prompt allows relative wording.", "Eval 1 §2.8 local override; the "
         "platform scored Today's Date 5; the Advisory rests only on Prompt Writing §4.2 and changes no band.", "Advisory kept"],
        ["C21", "Friction might be configured or implied.", "03_Error_Async_Config.txt 'Friction: none'; the prompt mentions no "
         "failure or wait.", "none stands"],
        ["C22", "Cross-Service Coherence fails on the presence of an inconsistency in data the task touches, and the agent still "
         "reads REVENUE_DAILY, whose Combo Fighter rows the Slack sales contradict (NB-26, platform I3).", "The platform scored "
         "it because 'the prompt asks what each bet brought in' and recommended the hold rev6 adds; with the hold no graded "
         "output depends on Combo Fighter's rows (01_Gradable_Surface.json: V1, V2 only), the agent's reads of the table serve "
         "Domino Delights and ZM, and 'until we’ve checked its first sales' agrees with D07H86MV4DN/1770782454.127069 "
         "(check_r1/19_nb26.json).", "none stands"],
        ["C23", "The prompt shares the persona and frame of two shipped Robert prompts, which a dataset check could flag.",
         "The platform's similarity gate passed this exact text at 0.676, distinct "
         "(plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md); Eval 1 §2.9 is N/A without supplied samples.", "none stands"],
        ["C24", "The task could reduce to one Slack post.", "Sheets, Drive, Linear and Slack writes (catalog.json).",
         "none stands"],
    ]
    out = ["## Self-review", "",
           "Phase walk: Evals/1_Prompt_Eval.md Phases 1–3 were read again for this run and walked in order against this report, "
           "with the platform's rev4 report beside it: Phase 1 → C2–C5, C9, C14–C16, C24; Phase 2 → C6–C8, C10–C13, C17–C20, C23; "
           "Phase 3 → C18, C21, C22. Every C-check has a result with evidence; none is UNVERIFIED. The 15 calibration cases are "
           "self-tested above.",
           "",
           table(["Check", "Counter-reading (strongest case that /prompt fails it, or that a finding is a false positive)",
                  "Evidence that resolves it", "Verdict"], rows),
           "",
           "Blind read on rev6 (one Opus subagent, run in this session on the exact 04_Prompt.txt and the rev6 SQL, told not to "
           "open Working_Files, plateform_reports, the later slots or support/, to write no file, and to drop the two excluded "
           "#winddown ts unread; it was not told what the platform found or what rev6 changed). Its report and how each point "
           "was handled:",
           "",
           table(["Its result", "Disposition in this check"], BLIND_ROWS),
           "",
           "Re-verified, not carried: every value in this report was re-read through hg.py, persona_view.py, entity.py or the "
           "rev6 SQL in this run (check_r1/). The brief, the dossier, the platform report and the session's leads were used only "
           "to choose what to look up.",
           "",
           "Mechanics: every quoted span in Findings, Fair readings, Check results, Verification log and Brief coverage was "
           "checked as an exact substring of 04_Prompt.txt by plan/assemble_check.py, which stops on a miss, on a held Combo "
           "Fighter revenue value or on a SQL other than ad50f039b5c2; severities follow the C-table and no Fail is raised; the "
           "04_Prompt.txt hash d0cb08476d23 is the same before and after this run. No output in check_r1/ carries either "
           "excluded #winddown ts (every write is guarded).",
           "",
           "Unresolved: none. UNVERIFIED: none. Carried as findings, not open items: the rubric must widen surface slots D4 and D1 "
           "(finding 1); relative day names (finding 2). Outside this stage: /injection has not yet run on rev6.",
           ""]
    return out


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "lookups":
        lookups(set(sys.argv[2:]) or None)
    else:
        build()
