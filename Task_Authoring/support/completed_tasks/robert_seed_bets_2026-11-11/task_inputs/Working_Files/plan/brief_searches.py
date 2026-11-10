#!/usr/bin/env python3
"""Brief §5a. Run each discovery fact's natural query as Robert through tools/persona_view.py search (base data), count
the seeded rows Robert can see that carry the query (the SQL overlay persona_view search does not read), and record the
first visible hit. Then run check-sql on the load-bearing ids, can-see on the records the brief names as out of reach,
and entity.py for every name in §10.

Writes plan/brief_searches.json, plan/brief_searches.txt (verbatim outputs) and plan/brief_entity.txt.
Run from anywhere: ~/.local/bin/python3.12 -B plan/brief_searches.py
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402

TASK = "Task_Authoring/task_inputsS2"
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=TASK, PYTHONDONTWRITEBYTECODE="1")
PY = [sys.executable, "-B"]
ROB = "robert@harmonygames.co"
# Two #winddown messages hold a pasted secret. No output carrying either ts may reach a file: the run stops instead.
EXCLUDED_TS = ("1770858495.115779", "1770858501.263569")
A = "robert@harmonygames.co/"
ADM = "C04UEQVDVB7/"
ARTHUR_MAIL = A + "<CAOOpSqA2MTKGlKETvkoKqFfq1MaIktcGcH9cj21BJMAMN4Ok00@mail.gmail.com>"
LEO_REPLY = A + "<CAPBs_a5xhlLhxf4uFEerJEygHD5CJ2ob3qegV9nV-erG4foiIU@mail.gmail.com>"

# (fid, service, natural query, id the row must reach, how the query is formed)
Q = [
    ("F1", "slack", "angel calls", "C0ADGSZKR3R/1770945821.640039", "from the prompt's own words"),
    ("F2", "slack", "Payee history", "C0ADGSZKR3R/1770945859.212469", "named in the prompt"),
    ("F3", "gdocs", "how to count the money", "f_6feda53b2382c63bf47b25", "title quoted by F1"),
    ("F4", "gsheets", "Angel note working", "f_3304033843904a426f3c00", "title quoted by F2"),
    ("F5", "gslides", "angels", "f_a4b3c4287a4314d8e532e1", "F2 says the draft deck; one word of its subject"),
    ("F6", "linear", "Payee history", "0742c172-85de-47ed-a111-316e5c8cb187", "named in the prompt"),
    ("F7", "linear", "SVB notices", "ENG-2438", "the project description's words"),
    ("F8", "linear", "Singular Labs", "ENG-2443", "an issue title; its notes are read per issue, comments are not searched"),
    ("F9", "trello", "Angel note", "698e55f9af74d68d679de7b3", "F3 says the plan is on the board"),
    ("F10", "gcal", "Angel calls", "evt_f21476dc404329f67fd60d", "F1's words"),
    ("F11", "gmail", "Payment Processed", A + "1776227799449805411", "named by F3"),
    ("F12", "gmail", "BANCO DE AMERICA", A + "1795282860741136988", "the title of ENG-2442"),
    ("F13", "slack", "MotMot", ADM + "1712331372.614469", "the payee in the ENG-2442 note; the hit sits inside the exchange"),
    ("F14", "slack", "wrong account", ADM + "1712901800.684259", "two account endings on ENG-2442 prompt the words"),
    ("F15", "gmail", "BANCO DE AMERICA", A + "1795509850966005840", "same search as F12"),
    ("F16", "slack", "Lucas", ADM + "1719603220.131689", "the name in the ENG-2447 note; the hit sits inside the exchange"),
    ("F17", "gmail", "Western Union", A + "1800873055214061794", "the service named in Slack; 2 of 5 receipts inside the limit"),
    ("F18", "gmail", "ready for pickup", A + "1808201559428745555", "the subject line F17 shows; lists all 5"),
    ("F19", "slack", "Leapblock", "C05URGU759U/1770971846.479179", "the title of ENG-2439"),
    ("F20", "gmail", "Leapblock LTD", A + "1776934359028762037", "the title of ENG-2439"),
    ("F21", "slack", "Leapblock payment", ADM + "1694616951.239909", "the payee plus the plain word"),
    ("F22", "gmail", "JPMorgan", ARTHUR_MAIL, "the title of ENG-2450"),
    ("F23", "gmail", "JPMorgan", LEO_REPLY, "same search; it quotes F22"),
    ("F24", "gmail", "JPMorgan", A + "1807851044809802572", "the title of ENG-2450"),
    ("F25", "slack", "Chase account", ADM + "1761954952.006759", "F22's own words"),
    ("F26", "slack", "closed the account", ADM + "1735854841.070019", "the ENG-2444 note's own words"),
    ("F27", "gmail", "PERSON_4419_NAME", A + "1815095592611804295", "the title of ENG-2444"),
    ("F28", "contacts", "Brooks", "564155d70112411151e512a6", "the title of ENG-2455"),
    ("F29", "gdocs", "Lauren Brooks", "f_20a0df3860bb5731d22f07", "the name F28 gives"),
    ("F30", "gmail", "***3801", A + "1847427662807006290", "the account ending on ENG-2454"),
    ("F31", "linear", "Walsh", "ENG-2454", "the title of ENG-2454; its notes are read per issue"),
    ("F32", "snowflake", "REVENUE_DAILY", "ANALYTICS.MONETIZATION.REVENUE_DAILY", "F3 names the table by role"),
    ("F33", "gsheets", "P&L", "f_605121f4a36752645e0ac3", "plain word"),
    ("F34", "slack", "cash in bank", ADM + "1754445622.992119", "plain words; the next post is the other half"),
    ("F35", "gdocs", "Saga Map", "f_322bbfdb37d253aa8624b9", "the ENG-2439 note's words"),
    ("F36", "linear", "Private Entrepreneur", "ENG-2459", "the title of ENG-2459; its notes are read per issue"),
    ("F37", "gmail", "Payoneer", A + "1798239548116390324", "the F36 note's own word"),
    ("F38", "slack", "Telegram distribution", "C05KNDCHAAG/1760125440.959149", "the words of F29's Exhibit A"),
    ("F39", "linear", "Brooks", "ENG-2455", "the title of ENG-2455; its notes are read per issue"),
]
NAMES = ["Robert", "Leonard", "Leonard Hayes", "Arthur", "Blake", "Arthur Blake", "Lucas", "Martin", "Martin Walsh", "Marcus",
         "Victor", "Lauren Brooks", "Brooks", "Nathan Price", "Graham Porter", "Oleg", "Ozhan", "Frederick", "Samuel Turner", "Brian",
         "Oliver Brooks", "Calvin Price", "Martin Lewis", "Marcus Bennett", "Marcus Lee", "Deel", "Singular", "Dixelar"]
OUT_OF_REACH = [("gmail", "leonard.hayes@harmonygames.co/1798427314394417287")]
REACH = [("gdrive", "d_9f7ba94f7526d54d8482ba"), ("slack", "C0ADGSZKR3R/1770934638.035469"), ("slack", "C06MXPL9536/1715113013.494939"), ("slack", "C04UEQVDVB7/1761844454.096829")]
# Off-bank routes checked in Robert's own mail, and the phrase that proves the search works outside it.
CENSUS = ["Dixelar", "Payoneer", "Thanks for your payment", "Your Payment Was Approved", "Upwork", "PayPal", "Remitly", "MoneyGram", "Zelle", "Venmo", "Fiverr", "payment receipt"]


def guard(txt, what):
    """Stop before writing anything if an output carries an excluded ts. Prints the query only, never the output."""
    if any(t in txt for t in EXCLUDED_TS):
        sys.exit(f"STOP: {what} returned an excluded #winddown record; change the query. Nothing written.")
    return txt


def run(args, timeout=900):
    p = subprocess.run(PY + args, cwd=WS, env=ENV, capture_output=True, text=True, timeout=timeout)
    return (p.stdout + p.stderr).strip()


def overlay():
    """Seeded rows Robert can read, per service, as (id, searchable text)."""
    rows = {}
    for x in parse_sql(open(os.path.join(TI, "01_Universe_Inject.sql")).read()):
        if x["op"] != "insert":
            continue
        r, t = x["row"], x["table"]
        add = lambda svc, i, *txt: rows.setdefault(svc, []).append((i, " ".join(str(v) for v in txt if v)))
        if t == "gmail.gmail_messages" and r.get("user_email") == ROB:
            add("gmail", r.get("id") or r.get("message_id"), r.get("subject"), r.get("body_text"))
        elif t == "slack.slack_messages":
            add("slack", f"{r['channel_id']}/{r['ts']}", r.get("text"))
        elif t == "gdocs.docs_documents":
            add("gdocs", r["document_id"], r.get("title"), r.get("body_text"))
        elif t == "gsheets.sheets_spreadsheets":
            add("gsheets", r["spreadsheet_id"], r.get("title"))
        elif t == "gslides.slides_presentations":
            add("gslides", r["presentation_id"], r.get("title"))
        elif t == "gcal.gcal_events" and r.get("calendar_id") == ROB:
            add("gcal", r["event_id"], r.get("summary"))
        elif t == "trello.trello_cards":
            add("trello", r["id"], r.get("name"), r.get("desc"))
        elif t == "contacts.contacts":
            add("contacts", r["contact_id"], r.get("first_name"), r.get("last_name"), r.get("job"))
        elif t == "linear.linear_projects":
            add("linear", r["id"], r.get("name"), r.get("description"))
        elif t == "linear.linear_issues":
            add("linear", r["identifier"], r.get("title"), r.get("description"))
        elif t == "linear.linear_comments":
            add("linear", r["id"], r.get("body"))
    return rows


def hit_ids(txt):
    """Ids from the hit lines. Matched by regex: not every hit line parses as JSON, and a parse skip reads as a miss."""
    ids = []
    for line in txt.splitlines():
        m = re.match(r'\s*\{"id": "([^"]+)"', line)
        if m:
            ids.append(m.group(1))
            continue
        m = re.match(r'\s*\{"file": ', line)
        if m:
            mp = re.search(r'"pointer": "([^"]+)"', line)
            ids.append(mp.group(1) if mp else "?")
    return ids


def hg_json(args, stdin=None):
    p = subprocess.run(PY + ["Task_Authoring/tools/hg.py", "search"] + args, cwd=WS, env=ENV, input=stdin, capture_output=True, text=True, timeout=600)
    return json.loads(p.stdout)


def robert_threads(phrase):
    """{thread id: service file} for Robert's threads carrying the phrase: ids from persona_view, files from hg.py."""
    p = subprocess.run(PY + ["Task_Authoring/tools/persona_view.py", "search", "robert", "gmail", phrase, "--limit", "400", "--no-hidden", "--json"],
                       cwd=WS, env=ENV, capture_output=True, text=True, timeout=600)
    want = {h["id"] for h in json.loads(p.stdout)["visible"]}
    d = hg_json(["search", "gmail", phrase, "--limit", "5000", "--compact"])
    if not d.get("scan_complete"):
        sys.exit(f"STOP: incomplete scan for {phrase!r}")
    files = {m["service_file"]: 1 for m in d["matches"]}
    out = {}
    names = sorted(files)
    for i in range(0, len(names), 50):
        req = {"items": [{"id": f, "service": "gmail", "file": f, "pointer": "/id", "max_chars": 200} for f in names[i:i + 50]]}
        items = hg_json(["get-many", "--request", "-"], json.dumps(req)).get("items", {})
        for f, r in items.items():
            tid = str(r.get("text", "")).strip().strip('"')
            if tid in want:
                out[tid] = f
    return out, want


def bodies(files):
    """Full message list per thread file, every page, held in memory only."""
    res, names = {}, sorted(files)
    for i in range(0, len(names), 25):
        items = {f: "" for f in names[i:i + 25]}
        offs = {f: 0 for f in items}
        while offs:
            req = {"items": [{"id": f, "service": "gmail", "file": f, "pointer": "/messages", "offset": o, "max_chars": 20000} for f, o in offs.items()]}
            got = hg_json(["get-many", "--request", "-"], json.dumps(req))["items"]
            nxt = {}
            for f, r in got.items():
                items[f] += r.get("text", "")
                if r.get("truncated"):
                    nxt[f] = r["next_offset"]
            offs = nxt
        for f, t in items.items():
            res[f] = json.loads(t)
    return res


def verify_notices():
    """Re-derive every payee's notice sum and each bet's by-date sum from Robert's own mail. Aggregates only, no excerpts."""
    import datetime as dt
    from decimal import Decimal as D
    tids, want = robert_threads("Payment Processed")
    msgs = bodies(tids.values())
    rx = re.compile(r"\*\*\*(\d{4})\s*Amount:\s*([\d,]+\.\d{2})\s*([A-Z]{3}).*?Transaction Date:\s*([A-Z][a-z]{2} \d{2} \d{4})", re.S)
    by_end, by_bet, cnt, cur, n = {}, {"Domino Delights": D(0), "ZM": D(0), "Combo Fighter": D(0)}, {}, {}, 0
    lb_year = {}
    for f, ms in msgs.items():
        for m in ms:
            if "Payment Processed" not in str(m.get("subject")):
                continue
            for end, amt, c, date in rx.findall(str(m.get("body"))):
                n += 1
                a = D(amt.replace(",", ""))
                cur[c] = cur.get(c, 0) + 1
                cnt[end] = cnt.get(end, 0) + 1
                if c != "USD":
                    by_end.setdefault(end + " " + c, D(0))
                    by_end[end + " " + c] += a
                    continue
                by_end[end] = by_end.get(end, D(0)) + a
                if end == "1359":
                    lb_year[date[-4:]] = lb_year.get(date[-4:], D(0)) + a
                d = dt.datetime.strptime(date, "%b %d %Y").date()
                k = "Domino Delights" if d <= dt.date(2025, 1, 8) else "ZM" if d <= dt.date(2025, 11, 23) else "Combo Fighter"
                by_bet[k] += a
    lines = [f"VERIFY notices: {len(tids)} of {len(want)} Robert threads read through hg.py; {n} Processed payments; currencies {cur}"]
    lines += [f"VERIFY by-date USD sum {k}: {v:,.2f}" for k, v in by_bet.items()]
    lines += [f"VERIFY ending {k}: {v:,.2f} over {cnt.get(k.split()[0])} notices" for k, v in sorted(by_end.items())]
    lines.append("VERIFY Leapblock ***1359 by year: " + ", ".join(f"{y} {v:,.2f}" for y, v in sorted(lb_year.items())))
    rt, _ = robert_threads("ready for pickup")
    sent = {}          # one transfer per tracking number: thread 1802092844284446043 also holds a Fwd of its own receipt
    copies = 0
    for f, ms in bodies(rt.values()).items():
        for m in ms:
            b = str(m.get("body"))
            x = re.search(r"Transfer Amount[^\d$]*\$?\s*([\d,]+\.\d{2})", b)
            t = re.search(r"(?:MTCN|Tracking Number)[^\d]{0,20}(\d{4,})", b)
            if not (x and t and "[PERSON_NAME_36400]" in b):
                sys.exit(f"STOP: receipt in {f} lacks amount, tracking number or the receiver token")
            copies += t.group(1) in sent
            sent[t.group(1)] = D(x.group(1).replace(",", ""))
    lines.append(f"VERIFY Western Union: {len(sent)} transfers by tracking number, {copies} forwarded copy, each naming [PERSON_NAME_36400]; "
                 f"sent {sorted(str(a) for a in sent.values())}; total {sum(sent.values()):,.2f}")
    return lines


def verify_census():
    """The absence behind ENG-2459's zero: what Robert's mail holds per route, with a positive control. Counts and subjects only."""
    lines = []
    for q in CENSUS:
        p = subprocess.run(PY + ["Task_Authoring/tools/persona_view.py", "search", "robert", "gmail", q, "--limit", "300", "--no-hidden", "--json"],
                           cwd=WS, env=ENV, capture_output=True, text=True, timeout=600)
        v = json.loads(guard(p.stdout, f"census {q!r}"))
        subjects = sorted({re.sub(r"\[[A-Z_0-9]+\]", "[T]", str(h.get("subject")))[:44] for h in v["visible"]})
        lines.append(f"VERIFY census as Robert, {q!r}: {v['visible_total']} threads; subjects {subjects[:4]}")
    d = hg_json(["search", "gmail", "Thanks for your payment", "--limit", "400", "--compact"])
    leo = sum("leonard@" in m["service_file"] for m in d["matches"])
    lines.append(f"VERIFY census control, all mailboxes, 'Thanks for your payment': {len(d['matches'])} hits, {leo} in Leonard's mailbox files, scan_complete {d.get('scan_complete')}")
    return lines


def main():
    seeded = overlay()
    res, raw = [], []
    for fid, svc, q, want, how in Q:
        args = ["Task_Authoring/tools/persona_view.py", "search", "robert", svc, q, "--limit", "10"]
        if svc == "gmail":
            args.append("--no-hidden")
        txt = guard(run(args), f"{fid} {svc} {q!r}")
        raw.append(txt)
        m = re.search(r"visible hits=(\d+) \(showing (\d+)\)\s+hidden by ACL=(\S+)", txt)
        vis, hidden = (int(m.group(1)), m.group(3)) if m else (0, "?")
        if svc == "gmail":
            hidden = "n/a (--no-hidden)"
        ids = hit_ids(txt)
        match = sorted({i for i, t in seeded.get(svc, []) if q.lower() in t.lower()})
        if any(want in i for i in ids) or want in txt:
            first, found = want, "YES (base hit)"
        elif want in match:
            first, found = want, "YES (seeded: base search cannot show it; check-sql YES)" if svc in ("slack", "gmail", "gdocs", "gsheets", "gslides", "gcal", "gdrive") else "YES (seeded: base search cannot show it; unscoped, in the SQL overlay)"
        else:
            first, found = (ids[0] if ids else None), "NO"
        res.append(dict(fid=fid, service=svc, query=q, want=want, how=how, base=vis, seeded=len(match), hidden=hidden, first=first, found=found))
        print(fid, svc, repr(q), "base", vis, "seeded", len(match), found, flush=True)

    lb = os.path.join(TASK, "Working_Files/plan/load_bearing_ids.txt")
    cs = guard(run(["Task_Authoring/tools/persona_view.py", "check-sql", "robert", f"{TASK}/01_Universe_Inject.sql", "--load-bearing", lb]), "check-sql")
    need = {w for _, _, _, w, _ in Q}
    keep = [ln for ln in cs.splitlines() if ln.startswith("CHECK-SQL") or ln.startswith("verdict:") or (ln.startswith("[") and any(w in ln for w in need))]
    can = [guard(run(["Task_Authoring/tools/persona_view.py", "can-see", "robert", s, i]), f"can-see {i}") for s, i in OUT_OF_REACH + REACH]
    ver = verify_notices() + verify_census()
    print("\n".join(ver), flush=True)

    json.dump(res, open(os.path.join(HERE, "brief_searches.json"), "w"), indent=1)
    with open(os.path.join(HERE, "brief_searches.txt"), "w") as f:
        f.write("\n\n".join(raw) + "\n\n" + "\n".join(keep) + "\n\n" + "\n".join(can) + "\n\n" + "\n".join(ver) + "\n")
    ent = [guard(run(["Task_Authoring/tools/entity.py", "collisions"]), "collisions")]
    ent += [guard(run(["Task_Authoring/tools/entity.py", "resolve", n]), f"resolve {n}") for n in NAMES]
    open(os.path.join(HERE, "brief_entity.txt"), "w").write("\n\n".join(ent) + "\n")
    nos = [r["fid"] for r in res if r["found"] == "NO"]
    print("rows", len(res), "NO:", nos or "none", "| check-sql:", next((l for l in cs.splitlines() if l.startswith("verdict:")), "?"))


if __name__ == "__main__":
    main()
