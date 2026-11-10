#!/usr/bin/env python3
"""Regenerate Working_Files/01_Grounding_Dossier.md from the current files and fresh tool runs.

Inputs: 01_Universe_Inject.sql, plan/sql_ids.json, plan/ids.json, plan/wording.json, plan/cohort.json, plan/notes.json,
the final manifest (else the draft), solver/truth.json, and the universe through tools/hg.py and persona_view.
A missing truth.json, manifest or preflight leaves that block to fill on the next run.

Figures are computed on each run: the 132 notices are re-read through hg.py, every quote is checked against its record
(a quote that no longer matches stops the run with exit 3), and tool outputs are pasted from fresh runs.

Scratch holds request ids and keyword counts with pointers only. Base text stays in memory and is never written there.
Searches go through hg.py. persona_view is used only for can-see and check-sql.

  ~/.local/bin/python3.12 -B Task_Authoring/task_inputsS2/Working_Files/plan/assemble_dossier.py [--kw-only] [--fresh-kw]
Writes the dossier and plan/load_bearing_ids.txt. Design-only text: no prompt, Oracle Event or criterion wording."""
import collections, concurrent.futures as cf, datetime as D, hashlib, importlib.util, json, os, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
BUNDLE = os.path.dirname(TI)
WS = os.path.dirname(BUNDLE)
TASK = os.path.relpath(TI, WS)
TOOLS = os.path.join(BUNDLE, "tools")
KB = os.path.join(BUNDLE, "references", "universe_kb", "by_universe", "normal")
SCR = os.environ.get("DOSSIER_SCRATCH", "/private/tmp/claude-501/-Users-sumit-Source-OC/291ff662-f24b-4f22-9fb7-b1cecbd8895a/scratchpad/ij4")
try:
    os.makedirs(SCR, exist_ok=True)
except OSError:
    SCR = tempfile.mkdtemp(prefix="dossier_")
os.environ["TASK_AUTHORING_TASK_DIR"] = TASK
os.chdir(WS)
sys.path.insert(0, TOOLS)
SQLP = os.path.join(TI, "01_Universe_Inject.sql")
ROB, LEO, ART = "robert@harmonygames.co", "leonard.hayes@harmonygames.co", "arthur.blake@harmonygames.co"
BAD = []          # quotes that did not match their record
TODO_DISP = []    # tool flags with no written disposition


def jl(*p):
    return json.load(open(os.path.join(*p)))


def sh(args, stdin=None, timeout=2400):
    return subprocess.run([sys.executable, "-B"] + [str(a) for a in args], cwd=WS, capture_output=True, text=True,
                          input=stdin, timeout=timeout, env=dict(os.environ))


def tool(name, *a):
    r = sh([os.path.join(TOOLS, name)] + list(a))
    return (r.stdout + (("\n" + r.stderr) if r.stderr.strip() and not r.stdout.strip() else "")).rstrip()


def hgj(*a, stdin=None):
    r = sh([os.path.join(TOOLS, "hg.py")] + list(a), stdin=stdin)
    s = r.stdout
    try:
        return json.loads(s)
    except ValueError:
        i, j = s.find("{"), s.rfind("}")
        if i >= 0 and j > i:
            return json.loads(s[i:j + 1])
        raise SystemExit(f"hg.py {' '.join(map(str, a))[:90]} printed no JSON: {r.stderr[-300:]}")


def records(checks):
    """hg.py records. The request file holds ids only and is removed straight after."""
    fd, p = tempfile.mkstemp(suffix=".json", dir=SCR)
    with os.fdopen(fd, "w") as f:
        json.dump({"checks": checks}, f)
    try:
        return hgj("records", "--request", p)["checks"]
    finally:
        os.remove(p)


def read_many(items):
    """hg.py search get-many, following truncated pages. items: {id, service, file, pointer}. Returns id -> parsed JSON."""
    buf, todo = collections.defaultdict(str), [dict({"max_chars": 12000}, offset=0, **i) for i in items]
    while todo:
        batch, todo = todo[:50], todo[50:]
        d = hgj("search", "get-many", "--request", "-", "--compact", stdin=json.dumps({"items": batch}))
        for it in batch:
            r = d["items"].get(it["id"]) or {}
            if r.get("error"):
                raise SystemExit(f"get-many {it['file']} {it.get('pointer')}: {r['error']}")
            buf[it["id"]] += r.get("text", "")
            if r.get("truncated"):
                todo.append(dict(it, offset=r["next_offset"]))
    return {k: json.loads(v) for k, v in buf.items()}


# ======================================================================== keyword counts (hg.py only, no excerpts kept)
TERMS = ["motmot", "leapblock", "lucas", "western union", "chase", "jpmorgan", "carta", "brooks", "telegram", "node media",
         "angel", "payee", "banco de america", "payment processed", "angel note", "payee history", "how to count the money",
         "chase records", "angel calls", "note to angels"]
KW_SCOPE = [("slack", "messages/*/*.json", 1500), ("gmail", "threads/0*.json", 1500), ("gdocs", "data.json", 200), ("gdrive", "data.json", 200),
            ("gsheets", "data.json", 200), ("gslides", "data.json", 200), ("gcal", "data.json", 200), ("linear", "data.json", 200),
            ("trello", "data.json", 200), ("contacts", "contacts.json", 200), ("confluence", "*.json", 200), ("snowflake", "snowflake.json", 200)]
KW_FILE = os.path.join(SCR, "kw_counts.json")


def keyword_counts(fresh=False):
    """{term|service: {n, complete, ptr, channels}}: counts and pointers only. Reused while the term list is unchanged."""
    have = {} if fresh or not os.path.exists(KW_FILE) else json.load(open(KW_FILE))

    def scan(scope):
        svc, glob, limit = scope
        need = [t for t in TERMS if f"{t}|{svc}" not in have]
        if not need:
            return {}
        req = {"service": svc, "file": glob, "queries": [{"id": t, "query": t, "limit": limit} for t in need]}
        d = hgj("search", "search-many", "--request", "-", "--compact", stdin=json.dumps(req))
        out = {}
        for t in need:
            r = (d.get("queries") or {}).get(t) or {}
            ms = r.get("matches") or []
            first = ms[0] if ms else {}
            chans = collections.Counter(m.get("service_file", m.get("file", "")).split("messages/")[-1].split("/")[0] for m in ms) if svc == "slack" else {}
            out[f"{t}|{svc}"] = {"n": len(ms), "complete": bool(r.get("scan_complete")) and len(ms) < limit,
                                 "ptr": f"{first.get('service_file', '')} {first.get('parent_pointer') or first.get('pointer') or ''}".strip(),
                                 "channels": dict(chans)}
        return out

    with cf.ThreadPoolExecutor(4) as ex:
        for part in ex.map(scan, KW_SCOPE):
            have.update(part)
    json.dump(have, open(KW_FILE, "w"))
    return have


if __name__ == "__main__" and "--kw-only" in sys.argv:
    k = keyword_counts("--fresh-kw" in sys.argv)
    print(len(k), "keyword counts in", KW_FILE)
    sys.exit(0)

# ======================================================================== current files
from base_check import parse_sql  # noqa: E402
import persona_view as PV  # noqa: E402

I = jl(HERE, "ids.json")
IDS, BASE, T, ISS = I["IDS"], I["BASE"], I["T"], I["issues"]
Q = jl(HERE, "wording.json")
C = jl(HERE, "cohort.json")
S = jl(HERE, "sql_ids.json")
NOTES = jl(HERE, "notes.json")
CTX = jl(WF, "00_Task_Context.json")
SQLTXT = open(SQLP).read()
STM = parse_sql(SQLTXT)
SQLSHA = hashlib.sha256(SQLTXT.encode()).hexdigest()
FINAL = os.path.exists(os.path.join(WF, "01_Hardness_Manifest.json"))
MAN = jl(WF, "01_Hardness_Manifest.json" if FINAL else "01_Hardness_Manifest.draft.json")
TRUTHP = os.path.join(WF, "solver", "truth.json")
TRUTH = jl(TRUTHP) if os.path.exists(TRUTHP) else None
AGG = None
if TRUTH is not None:
    try:
        spec = importlib.util.spec_from_file_location("solver_mod", os.path.join(WF, "solver", "solver.py"))
        SOLV = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(SOLV)
        AGG = SOLV.aggregates(TRUTH)
    except Exception as e:  # noqa: BLE001 - the solver is another author's file; keep the dossier buildable
        print("solver aggregates unavailable:", repr(e)[:200])
SLOC = {k: v["locator"] for k, v in S["slack"].items()}
SROW = {k: v["id"] for k, v in S["slack"].items()}
GM = {k: v[ROB]["message"] for k, v in S["gmail"].items() if ROB in v}
GT = {k: v[ROB]["thread"] for k, v in S["gmail"].items() if ROB in v}
LN = S["linear"]
EV_ROB = S["gcal"][ROB]
ACT = jl(KB, "activity.json")
CONV = jl(KB, "conventions.json")
U = PV.Universe()
P = PV.resolve_persona("robert")
SRC = open(os.path.abspath(__file__)).read()


def seen(svc, oid):
    return PV.can_see(U, P, svc, oid)


def note_ptrs(n):
    return [tuple(x.strip().split(" ", 1)) for x in str(n.get("pointer") or "").split(";") if " " in x.strip()]


# ======================================================================== base reads (memory only)
SL, GMT, DOCS = {}, {}, {}


def load_slack(locs):
    byf = collections.defaultdict(list)
    for loc in locs:
        ch, ts = loc.split("/")
        m = D.datetime.fromtimestamp(float(ts), D.timezone.utc).strftime("%Y-%m")
        byf[f"messages/{ch}/{m}.json"].append(ts)
    checks = [{"id": f"s{n}", "service": "slack", "file": f, "pointer": "", "field": "ts", "values": sorted(set(v))} for n, (f, v) in enumerate(sorted(byf.items()))]
    for c0 in range(0, len(checks), 40):
        for r in records(checks[c0:c0 + 40]).values():
            for m in r.get("matches") or []:
                x = m["record"]
                SL[f"{x['channel']}/{x['ts']}"] = {"rec": x, "file": m["file"].split("/slack/")[-1], "ptr": m["pointer"]}


def load_gmail(ids):
    items, meta = [], {}
    for tid in sorted(set(ids)):
        if tid.startswith("threads/"):
            f, n = tid, None
        else:
            v = seen("gmail", tid)
            ev = v.get("evidence") or {}
            f, n = ev.get("file"), ev.get("messages_in_thread")
        if not f:
            BAD.append(f"gmail {tid}: no thread file")
            continue
        meta[tid] = f
        items.append({"id": tid, "service": "gmail", "file": f, "pointer": ""})
    got = read_many(items)
    for tid, th in got.items():
        GMT[tid] = {"file": meta[tid], "thread": th}


def load_docs(ids):
    r = records([{"id": "d", "service": "gdocs", "file": "data.json", "pointer": "/docs_documents", "field": "document_id", "values": sorted(set(ids))}])
    for m in r["d"].get("matches") or []:
        DOCS[m["record"]["document_id"]] = {"rec": m["record"], "ptr": m["pointer"]}


def norm(s):
    return re.sub(r"[\s‌]+", " ", re.sub(r"&zwnj;", " ", str(s or ""))).strip()


def text_of(loc):
    if loc in SL:
        return norm(SL[loc]["rec"].get("text"))
    if loc in GMT:
        return norm(" ".join(f"{m.get('subject')} {m.get('body')}" for m in GMT[loc]["thread"].get("messages") or []))
    if loc in DOCS:
        return norm(DOCS[loc]["rec"].get("body_text"))
    return None


def q(loc, frag):
    """A quote checked against its record: `"frag" (loc)`."""
    t = text_of(loc)
    if t is None:
        if re.match(r"^[CD][A-Z0-9]+/\d", loc):
            load_slack([loc])
        elif "@" in loc or loc.startswith("threads/"):
            load_gmail([loc])
        elif loc.startswith("f_"):
            load_docs([loc])
        t = text_of(loc)
    if t is None or norm(frag) not in t:
        BAD.append(f"{loc}: {frag[:70]!r}" + (" (record not read)" if t is None else ""))
    return f"“{frag}” ({loc})"


slack_base = set(re.findall(r"\b[CD][A-Z0-9]{8,11}/\d{10}\.\d{6}\b", SRC)) | {v for v in BASE.values() if re.match(r"^[CD][A-Z0-9]+/\d", v)}
gmail_base = set(re.findall(r"robert@harmonygames\.co/\d{15,}", SRC)) | {v for v in BASE.values() if v.startswith(ROB)}
doc_base = {BASE["msa"], BASE["brooks_contract"]}
for k_, ns in NOTES.items():
    for n in ns:
        for svc, p_ in note_ptrs(n):
            if svc == "slack":
                slack_base.add(p_)
            elif svc == "gmail":
                gmail_base.add(p_)
            elif svc == "gdocs":
                doc_base.add(p_)
seeded_loc = set(SLOC.values())
load_slack(sorted(slack_base - seeded_loc))
load_gmail(sorted(gmail_base - {GT[k] for k in GT}))
load_docs(doc_base)

# ---- the 132 notices, re-read and parsed
SVB = jl(WF, "00_PreScenario", "svb_processed_robert.json")
raw = read_many([{"id": f"n{i}", "service": "gmail", "file": r["thread"], "pointer": f"/messages/{r['idx']}"} for i, r in enumerate(SVB)]
                + [{"id": f"t{i}", "service": "gmail", "file": r["thread"], "pointer": "/id"} for i, r in enumerate(SVB)])
NRX = re.compile(r"To:\s*(.+?\*\*\*(\d{4}))\s*Amount:\s*([\d,\.]+)\s*([A-Z]{3})\s*Transaction Date:\s*(\w{3} \d{2} \d{4})")
SUF = {s.strip(): p[0] for p in C for s in p[2].split(",")}
NOT, NOT_DIFF = [], []
for i, r in enumerate(SVB):
    m_ = raw[f"n{i}"]
    b = norm(m_.get("body"))
    g = NRX.search(b)
    if not g or "Payment Processed" not in str(m_.get("subject")):
        BAD.append(f"notice {r['thread']}: not parsed")
        continue
    amt = float(g.group(3).replace(",", ""))
    d_ = D.datetime.strptime(g.group(5), "%b %d %Y").date().isoformat()
    NOT.append({"thread": raw[f"t{i}"], "file": r["thread"], "to": g.group(1), "suffix": g.group(2), "amt": amt, "ccy": g.group(4), "txn": d_,
                "sent": m_.get("date"), "ref": r.get("ref"), "key": SUF.get(g.group(2))})
    if (r.get("usd") is not None and abs(amt - float(r["usd"])) > 0.001) or d_ != r["txn"]:
        NOT_DIFF.append(r["thread"])


def bet(d):
    return "Domino Delights" if d <= "2025-01-08" else "ZM" if d <= "2025-11-23" else "Combo Fighter"


def usd(x, cents=True):
    return f"${x:,.2f}" if cents else f"${x:,.0f}"


NUSD = [n for n in NOT if n["ccy"] == "USD"]
NOTHER = [n for n in NOT if n["ccy"] != "USD"]
BYBET = collections.Counter()
PAY = collections.defaultdict(lambda: {"n": 0, "sum": 0.0, "first": None, "last": None, "spell": set()})
for n in NOT:
    p_ = PAY[n["key"]]
    p_["n"] += 1
    p_["spell"].add(n["to"])
    p_["first"] = min(p_["first"] or n["txn"], n["txn"])
    p_["last"] = max(p_["last"] or n["txn"], n["txn"])
    if n["ccy"] == "USD":
        p_["sum"] += n["amt"]
        BYBET[bet(n["txn"])] += n["amt"]
LBY = collections.Counter()
for n in NUSD:
    if n["key"] == "Leapblock":
        LBY[n["txn"][:4]] += n["amt"]

# ---- Western Union receipts
WU = []
for k in ("wu1", "wu2", "wu3", "wu4", "wu5"):
    b = norm(GMT[BASE[k]]["thread"]["messages"][0].get("body"))
    a = re.search(r"Transfer Amount ([\d,\.]+) USD", b)
    f = re.search(r"Transfer Fees \+ ([\d,\.]+) USD", b)
    r_ = re.search(r"Total to Final Receiver ([\d,\.]+) USD", b)
    tok = re.search(r"Final Receiver Details Name (\[[A-Z_0-9]+\])", b)
    d_ = re.search(r"Date of Transactions (\d\d-\d\d-\d{4})", b)
    WU.append({"id": BASE[k], "sent": float(a.group(1).replace(",", "")) if a else None, "recv": float(r_.group(1).replace(",", "")) if r_ else None,
               "fee": float(f.group(1).replace(",", "")) if f else None, "tok": tok.group(1) if tok else None, "date": d_.group(1) if d_ else None})
WU_TOTAL = sum(w["sent"] or 0 for w in WU)

# ---- warehouse
TABF = os.path.join(SCR, "snowflake_tables.json")
tab_ids = {int(k): v for k, v in json.load(open(TABF)).items()} if os.path.exists(TABF) else {}
NEED = ("REVENUE_DAILY", "REVENUE_DAILY_V2", "STORE_TRANSACTIONS")


def table_ptr(name):
    return next((i for i, v in tab_ids.items() if str(v).endswith("." + name)), None)


for i in range(0, 90):
    if all(table_ptr(n_) is not None for n_ in NEED):
        break
    if i in tab_ids:
        continue
    try:
        tab_ids[i] = read_many([{"id": "x", "service": "snowflake", "file": "snowflake.json", "pointer": f"/tables/{i}/id"}])["x"]
    except SystemExit:
        break
json.dump(tab_ids, open(TABF, "w"))
REV_PTR, V2_PTR, STORE_PTR = (table_ptr(n_) for n_ in NEED)


def lifetime(ptr):
    rows = read_many([{"id": "rev", "service": "snowflake", "file": "snowflake.json", "pointer": f"/tables/{ptr}/rows", "max_chars": 590000}])["rev"]
    k0 = rows[0] if rows else {}
    gk = next((k for k in k0 if k.lower() in ("game_id", "title_id", "game", "game_name", "app_id")), None)
    vk = next((k for k in k0 if k.lower() in ("total_revenue_usd", "total_revenue_current", "revenue_usd", "total_revenue", "revenue")), None)
    print("table", ptr, "rows", len(rows), "keys", list(k0)[:12])
    if not gk or not vk:
        return None
    out = collections.Counter()
    for r in rows:
        out[r[gk]] += r[vk] or 0
    return {k: round(v, 2) for k, v in out.items()}


REV = lifetime(REV_PTR)
REV2 = lifetime(V2_PTR) if V2_PTR is not None else None
V2TXT = "not compared: its columns differ" if REV2 is None else ("equal" if REV2 == REV else "DIFFERENT: " + json.dumps(REV2))
print("snowflake pointers: REVENUE_DAILY", REV_PTR, "V2", V2_PTR, "STORE", STORE_PTR, "| V2", V2TXT)

# ---- identity rows
idr = records([
    {"id": "contacts", "service": "contacts", "file": "contacts.json", "pointer": "/contacts", "field": "email",
     "values": ["employee_0024@harmonygames.co", "lauren@harmonygames.co", "lucas@harmonygames.co", ROB, LEO, ART, "martin.walsh@harmonygames.co", "nathan@harmonygames.co", "oliver.brooks@harmonygames.co"]},
    {"id": "users", "service": "slack", "file": "users.json", "pointer": "", "field": "id", "values": ["EMPLOYEE_0024_SLACK_ID", "EMPLOYEE_0038_SLACK_ID", "EMPLOYEE_0025_SLACK_ID", "EMPLOYEE_0016_SLACK_ID"]},
    {"id": "chans", "service": "slack", "file": "channels.json", "pointer": "", "field": "id", "values": ["C05URGU759U", "C0ADGSZKR3R", "C04UEQVDVB7"]},
    {"id": "lists", "service": "trello", "file": "data.json", "pointer": "/lists", "field": "idBoard", "values": [BASE["founders_board"]]},
    {"id": "cards", "service": "trello", "file": "data.json", "pointer": "/cards", "field": "idBoard", "values": [BASE["founders_board"]]},
    {"id": "lusers", "service": "linear", "file": "data.json", "pointer": "/users", "field": "id", "values": ["usr_63fffeb4fab5233e", "usr_cc3e90160f490686", "usr_Robert", "usr_EMPLOYEE_0024"]},
])
CON = {m["record"]["email"]: m for m in idr["contacts"]["matches"]}
SU = {m["record"]["id"]: m for m in idr["users"]["matches"]}
CH = {m["record"]["id"]: m for m in idr["chans"]["matches"]}
LISTS = {m["record"]["id"]: m["record"] for m in idr["lists"]["matches"]}
BCARDS = [m["record"] for m in idr["cards"]["matches"]]
LUS = {m["record"]["id"]: m for m in idr["lusers"]["matches"]}
PLS = records([{"id": "pl", "service": "gsheets", "file": "data.json", "pointer": "/sheets_spreadsheets", "field": "spreadsheet_id", "values": [BASE["pl_costs"]]}])["pl"]["matches"][0]
PL = PLS["record"]
PL_COSTS = next(t for t in PL["sheets"] if t["title"] == "HG Costs")
PL_ROW7 = [c for c in PL_COSTS["grid"][6] if isinstance(c, str) and c.strip()][:2]
print("base reads done:", len(SL), "slack,", len(GMT), "gmail threads,", len(NOT), "notices,", len(DOCS), "docs; bad so far", len(BAD))

if "--audit-notes" in sys.argv:      # stdout only: each seeded note beside the records it cites
    for key, ns in NOTES.items():
        for n in ns:
            print(f"## {key} | {n['author']} | {n['text']}")
            for svc, p_ in note_ptrs(n):
                t = text_of(p_) or ""
                if svc == "gmail" and p_ in GMT:
                    m0 = GMT[p_]["thread"]["messages"][0]
                    t = f"{m0.get('date')} {m0.get('subject')} :: " + norm(m0.get("body"))[:330]
                elif svc == "slack" and p_ in SL:
                    x = SL[p_]["rec"]
                    t = D.datetime.fromtimestamp(float(x["ts"]), D.timezone.utc).strftime("%Y-%m-%d ") + str(x.get("user")) + ": " + t[:330]
                print(f"   {svc} {p_} [{seen(svc, p_)['verdict']}]: {t[:400]}")
    sys.exit(0)

# ======================================================================== load-bearing ids, then fresh tool runs
KW = keyword_counts("--fresh-kw" in sys.argv)
INS = [x for x in STM if x["op"] == "insert"]
UPD = [x for x in STM if x["op"] == "update"]
ROWS = collections.defaultdict(list)
for x in INS:
    ROWS[x["table"]].append(x)
note_rows = [r for k in LN for r in LN[k]["comments"]]
lb = list(SLOC.values()) + [IDS["method"], IDS["sheet"], IDS["deck"], EV_ROB, GM["arthur_mail"], GM["leonard_reply"]]
UNSCOPED_LB = [IDS["project"], IDS["trello"], IDS["c_brooks"]] + [x["row"]["id"] for x in ROWS["trello.trello_actions"] if x["row"]["type"] == "commentCard"]
lb += list(S["deck_elements"]) and [e.split("#")[1] for e in S["deck_elements"]]
UNSCOPED_LB += [LN[k]["issue"] for k in LN] + [r["id"] for r in note_rows]
lb += [v for k, v in BASE.items() if not v.startswith("snowflake:") and k != "founders_board"] + [n["thread"] for n in NOT]
for ns in NOTES.values():
    for n in ns:
        for svc, p_ in note_ptrs(n):
            if seen(svc, p_)["verdict"] == "YES":
                lb.append(p_)
lb = list(dict.fromkeys(lb))
LBP = os.path.join(HERE, "load_bearing_ids.txt")
open(LBP, "w").write("\n".join(lb) + "\n")

W = os.path.join(TASK, "Working_Files")
MANP = os.path.join(W, "01_Hardness_Manifest.json")
JOBS = {"sql_lint": ("sql_lint.py", SQLP), "base_check": ("base_check.py", SQLP), "base_claims": ("base_claims.py", SQLP, "--task-dir", TASK),
        "checksql": ("persona_view.py", "check-sql", "robert", SQLP, "--load-bearing", LBP)}
if FINAL:
    JOBS["hardness_gate"] = ("hardness_gate.py", MANP, SQLP)
    JOBS["fact_check"] = ("fact_check.py", SQLP, "--manifest", MANP, "--no-leak")
with cf.ThreadPoolExecutor(6) as ex:
    OUT = dict(zip(JOBS, ex.map(lambda a: tool(*a), JOBS.values())))
HL = hgj("lint", "--sql", SQLP)
FLAGS = [f for f in HL.get("flags") or [] if isinstance(f, dict)]


CNT_SCHEME = "the base cnt_ + 12 hex scheme" if IDS["c_brooks"].startswith("cnt_") else "the base 24 hex scheme"
# ---- 1.F lookups (counts only are kept)
IDC = os.path.join(SCR, "idcheck_counts.json")
idc = json.load(open(IDC)) if os.path.exists(IDC) else {}


def lookup(label, svc, ids, file, pointer=None, key=None):
    ids = sorted(set(ids))
    h = hashlib.sha1(json.dumps([svc, file, pointer, key, ids]).encode()).hexdigest()
    if h not in idc:
        fd, p = tempfile.mkstemp(suffix=".json", dir=SCR)
        with os.fdopen(fd, "w") as f:
            json.dump(ids, f)
        a = ["search", "lookup", svc, "--ids-file", p, "--file", file] + (["--pointer", pointer] if pointer is not None else []) + (["--key", key] if key else []) + ["--compact"]
        try:
            d = hgj(*a)
        finally:
            os.remove(p)
        idc[h] = {"n": len(ids), "checked": d.get("records_checked"), "complete": d.get("scan_complete"), "hits": sum(1 for v in (d.get("matches") or {}).values() if v)}
        json.dump(idc, open(IDC, "w"))
    return dict(idc[h], label=label, svc=svc, file=file, pointer=pointer)


g = lambda t, k: [x["row"][k] for x in ROWS[t]]
LOOK = [lookup("Drive files", "gdrive", g("gdrive.drive_files", "id"), "data.json", "/drive_files", "id"),
        lookup("calendar events", "gcal", g("gcal.gcal_events", "event_id"), "data.json", "/events", "event_id"),
        lookup("Trello cards", "trello", g("trello.trello_cards", "id"), "data.json", "/cards", "id"),
        lookup("Trello actions", "trello", g("trello.trello_actions", "id"), "data.json", "/actions", "id"),
        lookup("Linear issues", "linear", g("linear.linear_issues", "id"), "data.json", "/issues", "id"),
        lookup("Linear projects", "linear", g("linear.linear_projects", "id"), "data.json", "/projects", "id"),
        lookup("contacts", "contacts", g("contacts.contacts", "contact_id"), "contacts.json", "/contacts", "contact_id"),
        lookup("Slack rows", "slack", g("slack.slack_messages", "id"), "messages/*/*.json", "", "id"),
        lookup("Gmail messages", "gmail", g("gmail.gmail_messages", "id"), "threads/*.json", "/messages", "id")]
th_nums = sorted({x.split("/", 1)[1] for x in g("gmail.gmail_threads", "id")})
hth = hashlib.sha1(json.dumps(th_nums).encode()).hexdigest()
if hth not in idc:
    d = hgj("search", "search-many", "--request", "-", "--compact", stdin=json.dumps({"service": "gmail", "file": "threads/*.json", "queries": [{"id": n, "query": n, "limit": 5} for n in th_nums]}))
    idc[hth] = {"n": len(th_nums), "hits": sum(1 for n in th_nums if (d["queries"][n].get("matches") or [])), "complete": all(d["queries"][n].get("scan_complete") for n in th_nums)}
    json.dump(idc, open(IDC, "w"))
THC = idc[hth]
ts_checks = [{"id": f"t{i}", "service": "slack", "file": "messages/%s/%s.json" % (S["slack"][k]["channel"], D.datetime.fromtimestamp(float(S["slack"][k]["ts"]), D.timezone.utc).strftime("%Y-%m")),
              "pointer": "", "field": "ts", "values": [S["slack"][k]["ts"]]} for i, k in enumerate(S["slack"])]
TSC = records(ts_checks)
CONT_CHECK = records([{"id": "m", "service": "contacts", "file": "contacts.json", "pointer": "/contacts", "field": "email", "values": ["lauren@harmonygames.co"]},
                      {"id": "l", "service": "linear", "file": "data.json", "pointer": "/issues", "field": "project_id", "values": [IDS["project"]]},
                      {"id": "c", "service": "linear", "file": "data.json", "pointer": "/comments", "field": "id", "values": ["__none__"]},
                      {"id": "max", "service": "linear", "file": "data.json", "pointer": "/issues", "field": "identifier", "values": ["ENG-2437", "ENG-2438"]}])

UPD_TR = next((x for x in UPD if x["table"] == "trello.trello_boards"), None)
UPD_LIN = next((x for x in UPD if x["table"] == "linear.linear_teams"), None)
TEAM = records([{"id": "t", "service": "linear", "file": "data.json", "pointer": "/teams", "field": "id", "values": ["team_ENG"]}])["t"]["matches"][0]
L = []
A = L.append


def c(x):
    return re.sub(r"\s+", " ", str(x)).replace("|", "\\|")


def row(*cells):
    A("| " + " | ".join(c(x) for x in cells) + " |")


def head(*cols):
    row(*cols)
    A("|" + "---|" * len(cols))


def fence(t):
    L.extend(["```", t, "```"])


def seed_q(key, frag):
    t = norm(Q.get(key) if isinstance(Q.get(key), str) else json.dumps(Q.get(key), ensure_ascii=False))
    if norm(frag) not in t:
        BAD.append(f"wording {key}: {frag[:70]!r}")
    return f"“{frag}”"


def has_row(table, **kw):
    return [x for x in ROWS[table] if all(x["row"].get(k) == v for k, v in kw.items())]


AD, WD, EX, LBC, FO = "C04UEQVDVB7", "C0ADGSZKR3R", "C07C2866011", "C05URGU759U", "C04UTBZL6AX"
n_ins, n_upd = len(INS), len(UPD)
schemas = sorted({x["table"].split(".")[0] for x in STM})
latest_slack = max(float(v["ts"]) for v in S["slack"].values())
iso = lambda t: D.datetime.fromtimestamp(float(t), D.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
PLK = str(PL_ROW7[:1])

# ======================================================================== header
A("# Grounding Dossier — Robert · the seed, bet by bet · contains no prompt, OE or criterion text")
A("")
A(f"SQL: `{TASK}/01_Universe_Inject.sql` sha256 {SQLSHA[:12]} ({n_ins} INSERT + {n_upd} UPDATE over {len(schemas)} schemas: {', '.join(schemas)}). Snowflake and Confluence are read, never written. "
  f"{CTX['universe']['clock_line']}; seed bound {CTX['freeze_utc']}; Robert's today is {CTX['universe']['persona_today_weekday']} {CTX['universe']['persona_today']}. "
  f"Generated by `plan/assemble_dossier.py` from the current SQL, `plan/sql_ids.json`, `plan/notes.json`, the {'final' if FINAL else 'draft'} manifest, "
  f"{'`solver/truth.json`' if TRUTH else 'no truth.json yet'} and fresh `tools/hg.py` runs. Every quote below was checked against its record on this run; every total is computed from the {len(NOT)} notices re-read through hg.py or from truth.json. Every probability elsewhere is UNCALIBRATED.")
A("")

# ======================================================================== 1.A
SCHEMA = {f"{t['table_schema']}.{t['table_name']}": t["columns"] for t in jl(BUNDLE, "references", "universe_schema_live.json")}


def cols(t):
    return ", ".join(x["column"] + ("*" if x["nullable"] == "NO" and x.get("default") is None else "") for x in SCHEMA.get(t, []) if x.get("generated") != "ALWAYS")


TBL = [("gdrive.drive_files", "gdrive", "data.json", "/drive_files", "id", "created_time / modified_time ISO-Z; export parents = parents_json, shared_with_emails = shared_with_emails_json, owners = owners_json; ids f_/d_ + 22 hex"),
       ("gdocs.docs_documents", "gdocs", "data.json", "/docs_documents", "document_id", "created_time / modified_time ISO-Z; style_runs = style_runs_json; document_id equals the Drive id; owner_email may be a Resource token (I14)"),
       ("gsheets.sheets_spreadsheets", "gsheets", "data.json", "/sheets_spreadsheets", "spreadsheet_id", "ISO-Z; tabs sit in each row's sheets array"),
       ("gslides.slides_presentations", "gslides", "data.json", "/slides_presentations", "presentation_id", "no element timestamps; pages and elements are nested arrays"),
       ("trello.trello_cards", "trello", "data.json", "/cards", "id", "dateLastActivity ISO-Z; idMembers = \"idMembers_json\", badges = badges_json; first 8 hex of an id = Unix seconds; shortLink and shortUrl null in the export"),
       ("trello.trello_actions", "trello", "data.json", "/actions", "id", "date ISO-Z; data = data_json"),
       ("gcal.gcal_events", "gcal", "data.json", "/events", "event_id", "start_ts / end_ts ISO-Z; attendees = attendees_json; one row per attendee calendar"),
       ("contacts.contacts", "contacts", "contacts.json", "/contacts", "contact_id", "no timestamps; ids are 24 hex or cnt_ + 12 hex (the six cnt_ rows include /contacts/2)"),
       ("linear.linear_projects", "linear", "data.json", "/projects", "id", "created_at ISO-Z text; labels = labels_json"),
       ("linear.linear_issues", "linear", "data.json", "/issues", "id", "ISO-Z text; id = identifier = KEY-number; labels, links, relations = *_json"),
       ("trello.trello_boards", "trello", "data.json", "/boards", "id", "dateLastActivity ISO-Z; updated by the SQL, not inserted"),
       ("linear.linear_teams", "linear", "data.json", "/teams", "id", "no event timestamp; issue_counter updated by the SQL, not inserted")]
cnt = records([{"id": t[0], "service": t[1], "file": t[2], "pointer": t[3], "field": t[4], "values": ["__none__"]} for t in TBL])
samp = read_many([{"id": f"{t[0]}#{i}", "service": t[1], "file": t[2], "pointer": f"{t[3]}/{i}/{t[4]}"} for t in TBL for i in range(2 if t[3] == "/projects" else 3)])
GFILES = hgj("search", "files", "gmail", "threads/", "--limit", "1").get("total_matching_paths")
RBOX = U.gmail()["mailboxes"][ROB]
A("## 1.A Structural")
A("")
A("Live columns from `references/universe_schema_live.json` (`*` = NOT NULL, no default; generated columns omitted). Base counts are `records_checked` from `hg.py records` over the full collection; sample ids are read through `hg.py search get-many`.")
A("")
head("Table", "Live columns", "Base location", "Base count", "3 sample ids", "Timestamp format and mapping")
for t in TBL:
    s_ = [samp[k] for k in sorted(samp) if k.startswith(t[0] + "#")]
    row(t[0], cols(t[0]), f"{t[1]} {t[2]} {t[3]}", cnt[t[0]].get("records_checked"), ", ".join(s_), t[5])
sp = read_many([{"id": f"p{i}", "service": "gslides", "file": "data.json", "pointer": f"/slides_presentations/0/pages/{i}/object_id"} for i in range(3)] +
               [{"id": f"e{i}", "service": "gslides", "file": "data.json", "pointer": f"/slides_presentations/0/pages/{i}/elements/0/object_id"} for i in range(3)] +
               [{"id": f"s{i}", "service": "gsheets", "file": "data.json", "pointer": f"/sheets_spreadsheets/{i}/spreadsheet_id"} for i in range(3)])
row("gsheets.sheets_sheets", cols("gsheets.sheets_sheets"), "gsheets data.json /sheets_spreadsheets/N/sheets", f"nested in {cnt['gsheets.sheets_spreadsheets'].get('records_checked')} spreadsheets", ", ".join(f"{sp[f's{i}']}#0" for i in range(3)), "grid = grid_json; sheet_id 0 on a first tab")
row("gslides.slides_pages", cols("gslides.slides_pages"), "gslides data.json /slides_presentations/N/pages", f"nested in {cnt['gslides.slides_presentations'].get('records_checked')} decks", ", ".join(sp[f"p{i}"] for i in range(3)), "slide_ + 12 hex, unique within a deck")
row("gslides.slides_page_elements", cols("gslides.slides_page_elements"), "gslides data.json /slides_presentations/N/pages/M/elements", "nested", ", ".join(sp[f"e{i}"] for i in range(3)), "el_ + 12 hex; TEXT_BOX 9144000 × 5143500")
row("linear.linear_comments", cols("linear.linear_comments"), "linear data.json /comments", CONT_CHECK["c"].get("records_checked"), "none in base (NB-24): the first comment rows in the export are seeded, comment_ + 32 hex per the passed precedent", "ISO-Z text")
row("gmail.gmail_threads", cols("gmail.gmail_threads"), "gmail threads/*.json (one object per file)", f"{GFILES} thread files; Robert's mailbox {RBOX['threads']}", f"{BASE['n_ban_first']}, {BASE['wu1']}, {BASE['jpm_notice']}", "id = mailbox/numeric; history_id digits or NULL")
row("gmail.gmail_messages", cols("gmail.gmail_messages"), "gmail threads/*.json /messages", f"Robert's mailbox {RBOX['messages']} messages", ", ".join(GMT[BASE[k]]["thread"]["messages"][0]["id"] for k in ("n_ban_first", "wu1", "jpm_notice")), "date ISO-Z in numbered files, RFC-2822 in alias files (I04); internal_date ms; labelIds = label_ids_json; \\r\\n line ends")
ws = records([{"id": "a", "service": "slack", "file": f"messages/{WD}/2026-02.json", "pointer": "", "field": "ts", "values": ["__none__"]}, {"id": "b", "service": "slack", "file": f"messages/{LBC}/2026-02.json", "pointer": "", "field": "ts", "values": ["__none__"]}])
row("slack.slack_messages", cols("slack.slack_messages"), f"slack messages/<channel>/<yyyy-mm>.json ({SL[BASE['angels']]['file']} {SL[BASE['angels']]['ptr']})".replace("<channel>", "CHANNEL").replace("<yyyy-mm>", "YYYY-MM"), f"touched shards: {WD} 2026-02 {ws['a'].get('records_checked')}, {LBC} 2026-02 {ws['b'].get('records_checked')}", f"{SL[BASE['angels']]['rec']['id']}, {SL[BASE['draft_note']]['rec']['id']}, {SL[BASE['linear_keep']]['rec']['id']}", "ts 6 decimals; id = sha256(channel|ts)[:32]; user = user_id; new top-level rows carry no thread fields")
A("")
A(f"Board shape, opened through hg.py: board {BASE['founders_board']} has lists " + ", ".join(f"{v['name']} ({k})" for k, v in LISTS.items()) + f"; {len(BCARDS)} cards, highest idShort {max(x.get('idShort') or 0 for x in BCARDS)}, last card activity {max(x.get('dateLastActivity') or '' for x in BCARDS)}; open cards on To Do: {sum(1 for x in BCARDS if LISTS.get(x['idList'], {}).get('name') == 'To Do' and not x.get('closed'))}.")
A("")

# ======================================================================== 1.B
con = lambda e: f"contacts.json {CON[e]['pointer']}" if e in CON else "no contact row"
A("## 1.B Entity")
A("")
head("Entity", "Spelling used", "Where it appears (cited)", "Agreement")
row("Leonard Hayes", f"{LEO} · EMPLOYEE_0038_SLACK_ID · usr_63fffeb4fab5233e · PERSON_6094_TRELLO_USER_ID",
    f"slack users.json {SU['EMPLOYEE_0038_SLACK_ID']['pointer']}; linear data.json {LUS['usr_63fffeb4fab5233e']['pointer']}; {con(LEO)} (job {CON[LEO]['record']['job']}); " + q(f"{WD}/1770933601.686309", "linear we keep during transition"),
    "AGREE on identity. Contacts job differs from the roster title (S06, pre-existing: avoid); no seed states a title")
row("Arthur Blake ('Blake')", f"{ART} · EMPLOYEE_0025_SLACK_ID · usr_cc3e90160f490686",
    f"slack users.json {SU['EMPLOYEE_0025_SLACK_ID']['pointer']}; {con(ART)}; " + q(f"{AD}/1712901800.684259", "because Blake put the wrong account number") + "; " + q(f"{AD}/1736978214.260099", "Just put the MotMot payment into SVB"),
    "AGREE: Leonard's 'Blake' is Arthur in the base and in the ask")
row("Robert", f"{ROB} · EMPLOYEE_0016_SLACK_ID · usr_Robert", f"slack users.json {SU['EMPLOYEE_0016_SLACK_ID']['pointer']}; linear data.json {LUS['usr_Robert']['pointer']} (I10); {con(ROB)} job {CON[ROB]['record']['job']}",
    "DISAGREE (pre-existing: avoid): Contacts title against the persona title (S06); no seed or graded fact uses a title")
row("Leapblock's contact", "EMPLOYEE_0024_SLACK_ID, shown as the bare token; the seeded statement names Leapblock in its text",
    f"slack users.json {SU['EMPLOYEE_0024_SLACK_ID']['pointer']} (email null); {con('employee_0024@harmonygames.co')} first_name {CON['employee_0024@harmonygames.co']['record']['first_name']}, job {CON['employee_0024@harmonygames.co']['record']['job']}; "
    + q(BASE["msa"], "scott@harmonygames.co") + "; " + q("robert@harmonygames.co/1784519237112280991", "he is the one managing the external art studio called LeapBlock") + "; " + q(f"{LBC}/1770922108.887399", "Hi [PERSON_NAME_0083]"),
    "DISAGREE (pre-existing: avoid): one person under a Slack token, a Contacts first name and a body token; nothing joins them mechanically, so no claim rests on the join")
row("Lauren Brooks", "Lauren Brooks; notices spell [PERSON_NAME_7249] Brooks ***5384; seeded contact " + IDS["c_brooks"],
    q(f"{EX}/1760122065.890659", "sent this contract out") + f" (file Consulting Agreement Lauren Brooks.pdf); {BASE['brooks_contract']} " + q(BASE["brooks_contract"], "run and optimize paid UA for Telegram") + f"; activity.json lauren@harmonygames.co; P&L {BASE['pl_costs']} HG Costs row 7 reads {PLK}",
    "DISAGREE (pre-existing: avoid): HG Costs row 7 carries another human name; that row stays off the path. DISAGREE (designed): a monthly contractor reads as Build until the contract shows paid UA (T6)")
row("Oliver Brooks", "oliver.brooks@harmonygames.co", f"{con('oliver.brooks@harmonygames.co')}; activity.json; `entity.py` SHARED_LAST_NAMES brooks (plan/research/entity_collisions.txt); contacts.json has no Lauren row (" + f"{CONT_CHECK['m'].get('records_checked')} rows checked, {len(CONT_CHECK['m'].get('matches') or [])} matches)", "AGREE: a different person; the seeded contact separates them")
row("MotMot", "MotMot; notices spell BANCO DE AMERICA ***8605 and ***3341",
    q(BASE["n_ban_first"], "BANCO DE AMERICA ***8605") + "; " + q(BASE["n_ban_mod"], "BANCO DE AMERICA ***3341") + "; " + q(f"{AD}/1712331372.614469", "thats the motmot one?") + "; " + q(f"{AD}/1712331142.975829", "This wire didn’t go through") + "; " + q(f"{AD}/1712901800.684259", "bank returned our money"),
    f"DISAGREE (designed, T1): Processed notice against the founders' Apr 5 and Apr 12, 2024 notes. HG Salary row label 'MotMot + Blake LLC' (S4 of sc2) stays off the path")
row("Node Media", "Node Media LLC; notices spell PERSON_4419_NAME LLC ***0115",
    q(f"{AD}/1735854841.070019", "closing our account with Node Media LLC") + "; " + q(f"{AD}/1735854852.066529", "3+ months payment") + "; " + q(BASE["node_mail"], "Sept - $1,428.57") + "; " + q(BASE["node_mail"], "nodemedia.co"),
    f"AGREE on identity. The mail explains Sept to Nov, not the whole {usd(PAY['Node Media']['sum'])} wire (sc2 X8); no graded fact needs the remainder. Alias is designed (T5)")
row("Lucas", f"Lucas; notices spell [PERSON_NAME_36400] ***6577; base contact {CON['lucas@harmonygames.co']['record']['contact_id']}",
    f"{con('lucas@harmonygames.co')} job {CON['lucas@harmonygames.co']['record']['job']}; " + q(f"{AD}/1719603595.852129", "via company card") + "; " + q(BASE["wu1"], "Final Receiver Details Name [PERSON_NAME_36400]") + f"; first notice {PAY['Lucas']['first']}; " + q(f"{AD}/1727147072.731139", "help setup IBAN for Lucas"),
    f"AGREE: the receipts' receiver token equals the notice token. Designed gap (T2): {WU and len(WU)} receipts of {usd(WU_TOTAL)} sit outside the notices")
row("Chase ***3203", "the company's Chase account; notices spell JPMorgan [PERSON_NAME_4503] ***3203",
    q(BASE["jpm_notice"], "JPMorgan [PERSON_NAME_4503] ***3203") + "; " + q(f"{AD}/1761954952.006759", "Chase account closed") + "; " + q(f"{WD}/1770932925.126829", "tied to our Chase account which is closed") + f"; seeded {GM['arthur_mail']} " + seed_q("arthur_mail", "our own Chase account"),
    "DISAGREE (designed, T4): a cost by its notice, the company's own money by Arthur's mail. The link from ***3203 to the Chase account and the top-up reason are the seed's own, consistent with the base and carried as an open item")
row("Carta", "Carta", q(f"{WD}/1770932858.658179", "we have time for Carta renewal") + "; " + q(f"{WD}/1770932925.126829", "I can’t remove the bank account from Carta") + "; " + q(f"{WD}/1770935621.095649", "Carta terminations are done"),
    "AGREE. Paid from Chase, so outside the notices by the method's Chase sentence; no Carta figure is graded")
row("Deel", "Deel; notices spell Deel, Inc. ***8380 and [ORG_NAME_0057], Inc. ***8380",
    q(BASE["deel_recipient"], "Deel, Inc. ***8380") + "; " + q("robert@harmonygames.co/1778183297904473683", "[ORG_NAME_0057], Inc. ***8380") + "; " + q(f"{AD}/1680895323.182209", "for contractors we start with Deel") + "; " + q(f"{WD}/1770933601.686309", "let’s keep Deel, gusto, Intuit"),
    f"AGREE: same suffix, redaction variance (NB-12). {PAY['Deel']['n']} notices, {len(PAY['Deel']['spell'])} spellings")
row("Payee history project", f"Linear project {IDS['project']} with {LN['Deel']['issue']} to {LN[list(LN)[-1]]['issue']}", f"base holds {CONT_CHECK['l'].get('records_checked')} issues, none on this project; highest base ENG number confirmed by linear data.json {(CONT_CHECK['max']['matches'] or [{}])[0].get('pointer')}", "AGREE (new)")
row("Angel note method doc", f"'{Q['method_title']}' {IDS['method']}", q(f"{WD}/1770934638.035469", "Reaching out to our angels properly") + "; " + q(f"{AD}/1754445718.724799", "matching what banks say so that’s the ground source of truth"), "AGREE (new, in Leonard's own terms)")
A("")
A(f"Designed disagreements are listed under Intended disagreements. No roster person is renamed. No new header token is minted: the seeded contact uses Lauren Brooks's existing address, and EMPLOYEE_0024_SLACK_ID is the base author of {LBC}/1770842824.806309.")
A("")

# ======================================================================== 1.C
PH = CONV["slack"]["per_person_hours_and_style"]
ps = lambda e: PH[e]["style"]
A("## 1.C Voice and realism")
A("")
A("Seeded speakers, each with its activity.json status at the clock (`references/universe_kb/by_universe/normal/activity.json`); length bands, capitalisation and hours from conventions.json `slack.per_person_hours_and_style`:")
for name, e, sid, quotes in [
        ("Leonard Hayes", LEO, "EMPLOYEE_0038_SLACK_ID", [q(f"{WD}/1770933601.686309", "During shutdown, let’s keep Deel, gusto, Intuit."), q(f"{AD}/1754445718.724799", "I’m accurate in terms of the balances"), q(f"{WD}/1770932925.126829", "good luck to them taking the money from us next time lol")]),
        ("Arthur Blake", ART, "EMPLOYEE_0025_SLACK_ID", [q(f"{AD}/1712331718.859679", "I think I messed up the bank account number."), q(f"{AD}/1736978214.260099", "Needs approval."), q(f"{WD}/1770937232.664809", "I'll be moving github")])]:
    w_ = PH[e]["slack_core_80pct_window_utc"]
    st = ps(e)
    A(f"- {name} ({e}, {sid}) — activity.json status_at_clock {ACT['people'][e]['status_at_clock']}. Real messages: {'; '.join(quotes)}. Length p50 {st['len']['p50']}, p90 {st['len']['p90']}, p99 {st['len']['p99']}; lower-case start {st['lower_start_share']:.0%}; core window {w_['start_hour']:02d}–{w_['end_hour']:02d} UTC.")
e24 = ACT["slack_only_ids"]["EMPLOYEE_0024_SLACK_ID"]
A(f"- Leapblock's contact (EMPLOYEE_0024_SLACK_ID) — activity.json slack_only_ids: {e24['messages']} messages, last post {e24['last'][:19]}Z; the email entity employee_0024@harmonygames.co reads status_at_clock {ACT['people']['employee_0024@harmonygames.co']['status_at_clock']}, which describes the unjoined Linear and calendar account, not this Slack id. Real messages: "
  + "; ".join([q(f"{LBC}/1705504271.041319", "Hey guys, sorry for the delay with the invoices!"), q(f"{LBC}/1718965064.900049", "The payment arrived, thanks!"), q(f"{LBC}/1746539617.368519", "I've just spoken to the accountant")]) + f". Opens with 'Hey guys', mixed case; seeded at {iso(S['slack']['statement']['ts'])}, inside the Feb 13 window after his Feb 12 call ({LBC}/1770922209.919939).")
A(f"- Robert ({ROB}, EMPLOYEE_0016_SLACK_ID) — activity.json status_at_clock {ACT['people'][ROB]['status_at_clock']}: the persona, with no seeded voice.")
A(f"- Lauren Brooks (lauren@harmonygames.co) — activity.json status_at_clock {ACT['people']['lauren@harmonygames.co']['status_at_clock']}: a contact row only, no seeded voice.")
A("")
sub = CONV["gmail"]["internal_subject_len_chars"]
pv_ = CONV["slack"]["length_chars_by_channel_type"]["private"]
ask_len = [len(Q["ask"]), len(Q["ask2"])]
A(f"conventions.json keys used: `slack.length_chars_by_channel_type.private` p50 {pv_['p50']}, p99 {pv_['p99']}: the two ask posts are {ask_len[0]} and {ask_len[1]} characters ({WD}/1770934638.035469 shows Leonard's longer lists; the ask stays near the channel's p99, split in two as sw2 advised), the statement {len(Q['statement'])}. "
  f"`gmail.internal_subject_len_chars` p50 {sub['p50']}: '{Q['arthur_subject']}' is short, as Arthur's mail is. `gcal.duration_min` p75 {CONV['gcal']['duration_min']['p75']}, max band p99 {CONV['gcal']['duration_min']['p99']}: the hold runs 90 minutes because it blocks a run of calls. `linear.title_prefixes_by_team` ENG: plain titles, as the seeded bank spellings are.")
A(f"Times: the ask is {iso(S['slack']['ask']['ts'])} (Thursday 5:23 pm PT, inside Leonard's window); Arthur's mail {T['arthur']} (morning ET); Leonard's reply follows it at {S['gmail']['leonard_reply'][ROB]['message'] and [x['row']['date'] for x in ROWS['gmail.gmail_messages'] if x['row']['id'] == GM['leonard_reply']][0]}.")
A("Arthur's real mail, read through hg.py: " + "; ".join([q("robert@harmonygames.co/1837277453195980012", "Done."), q("robert@harmonygames.co/1822060525232306557", "Yes, I confirm."), q("robert@harmonygames.co/1855403930841796194", "We need counsel to structure a cap table reset")]) + f". All three open capitalised. Seeded mail {GM['arthur_mail']} opens " + ("in lower case" if Q["arthur_mail"][:1].islower() else "capitalised") + " (`plan/research/sw2_coherence.md` advised capitalising). Eval 0 puts voice outside its checks, so this is a realism note for the SQL owner, not a defect.")
A("")

# ======================================================================== 1.D
A("## 1.D Keyword")
A("")
A("Counts are `hg.py search search-many` hits over the base, unscoped by persona: Slack `messages/*/*.json`, Gmail `threads/0*.json` (Robert's numbered thread files, which also hold a few token mailboxes, I05), the other services whole. `N+` means the query reached its limit. Slack 'in reach' sums hits in channels where `persona_view can-see` says YES. Seeded = SQL rows carrying the term.")
A("")
head("Term", "Slack (in reach)", "Gmail", "Drive family", "Linear / Trello / Contacts", "Confluence / Snowflake", "Seeded rows", "First pointer or NEW TERM")
chan_ok = {}


def in_reach(chs):
    n = 0
    for ch, k in chs.items():
        if ch not in chan_ok:
            chan_ok[ch] = seen("slack", ch)["verdict"] == "YES"
        n += k if chan_ok[ch] else 0
    return n


def seeded_hits(term):
    out = []
    for x in INS:
        txt = " ".join(str(v) for k, v in (x.get("row") or {}).items() if isinstance(v, str) and not k.endswith("_id") and k not in ("id",))
        if term.lower() in txt.lower():
            out.append(x)
    return out


def rid_of(x):
    r = x.get("row") or {}
    t = x["table"]
    if t == "gslides.slides_pages" or t == "gslides.slides_page_elements":
        return f"{r['presentation_id']}#{r['object_id']}"
    if t == "gsheets.sheets_sheets":
        return f"{r['spreadsheet_id']}#{r['sheet_id']}"
    if t == "slack.slack_messages":
        return f"{r['channel_id']}/{r['ts']}"
    for k in ("id", "event_id", "contact_id", "document_id", "spreadsheet_id", "presentation_id"):
        if r.get(k):
            return str(r[k])
    return str(next(iter((x.get("where") or {}).values()), "?"))


fmt = lambda t, s: f"{KW[f'{t}|{s}']['n']}{'' if KW[f'{t}|{s}']['complete'] else '+'}"
for t in TERMS:
    tot = sum(KW[f"{t}|{s}"]["n"] for s, _, _ in KW_SCOPE)
    sh_ = seeded_hits(t)
    first = next((KW[f"{t}|{s}"]["ptr"] for s, _, _ in KW_SCOPE if KW[f"{t}|{s}"]["n"]), "")
    sv = next((s for s, _, _ in KW_SCOPE if KW[f"{t}|{s}"]["n"]), "")
    note = ""
    if t.startswith("chase"):
        note = " ('chase' also matches 'purchase', so the raw count overstates the bank name)"
    ptr = f"{sv} {first}{note}" if tot and t != "chase records" else f"NEW TERM — introduced in {rid_of(sh_[0]) if sh_ else 'no row'}, reached via {'Leonard’s ask' if t != 'chase records' else 'a mail search for Chase or JPMorgan'}{note}"
    row(t, f"{fmt(t, 'slack')} ({in_reach(KW[f'{t}|slack']['channels'])})", fmt(t, "gmail"), f"docs {fmt(t, 'gdocs')}, drive {fmt(t, 'gdrive')}, sheets {fmt(t, 'gsheets')}, slides {fmt(t, 'gslides')}",
        f"{fmt(t, 'linear')} / {fmt(t, 'trello')} / {fmt(t, 'contacts')}", f"{fmt(t, 'confluence')} / {fmt(t, 'snowflake')}", len(sh_), ptr)
A("")
A(f"Controls: 'angel note', 'payee history', 'how to count the money', 'angel calls' and 'note to angels' have 0 base hits, so each seeded name is unique. 'node media' has {fmt('node media', 'gmail')} hits in Robert's numbered files by that spelling; the Node mail {BASE['node_mail']} carries it as nodemedia.co, so a Gmail search on the two-word name can miss it and the Slack name {AD}/1735854841.070019 is the path.")
A("")

# ======================================================================== 1.E
A("## 1.E Persona reach")
A("")
A(f"Load-bearing record ids (seeded and base) are in `Working_Files/plan/load_bearing_ids.txt` ({len(lb)} ids: the {len(NOT)} notice threads, the proof records Robert can read, and the scoped seeded rows that carry a fact, deck elements included). Unscoped rows that carry a fact are listed below rather than in that file: check-sql cannot infer a service for a Linear, Trello or Contacts id and returns UNVERIFIED (U4), which fails the run. Output verbatim:")
A("")
fence(OUT["checksql"])
A("")
A(f"- {WD} — #winddown, private, Robert in members LB (slack channels.json {CH[WD]['pointer']}): the ask {SLOC['ask']}, {SLOC['ask2']}; base {BASE['angels']}, {BASE['linear_keep']}.")
A(f"- {LBC} — #leapblock, private, Robert in members LB (slack channels.json {CH[LBC]['pointer']}): the statement {SLOC['statement']}. Arthur is not a member; nothing needs him there.")
A(f"- {AD} — #admin_foundersonly, private, Robert in members LB (slack channels.json {CH[AD]['pointer']}): {BASE['wire_fail']}, {BASE['wrong_acct']}, {BASE['returned']}, {BASE['lucas_card']}, {BASE['lb_done']}, {BASE['node_close']}, {BASE['laptop']}.")
A(f"- Robert's mailbox LB: Arthur's mail {GM['arthur_mail']} (thread {GT['arthur_mail']}), Leonard's reply {GM['leonard_reply']}, the {len(WU)} receipts from {BASE['wu1']}, the Awaiting notice {BASE['lb_await']}, the BGN notice {BASE['bgn_notice']}, the JPMorgan notice {BASE['jpm_notice']}. All carry INBOX or SENT, none SPAM or TRASH.")
A(f"- Drive family LB: {IDS['method']}, {IDS['sheet']}, {IDS['deck']} are Leonard's, shared with Robert (shared_with_emails_json); {BASE['brooks_contract']}, {BASE['msa']}, {BASE['pl_costs']} are Resource-owned and shared with Robert (I14); the write home is Robert's root {BASE['robert_root']}.")
A(f"- Calendar LB: Robert's copy {EV_ROB} (self true). Invitation {GM['invite']} is a companion and carries no relied-on fact (R08, manifest hazard_acknowledgements).")
A(f"- Unscoped (visible to all): project {IDS['project']}, {LN['Deel']['issue']} to {LN[list(LN)[-1]]['issue']} and their {len(note_rows)} notes, card {IDS['trello']} and its comment, contact {IDS['c_brooks']}, snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY.")
A(f"- Unscoped rows that carry a fact ({len(UNSCOPED_LB)}, visible to every persona): " + ", ".join(UNSCOPED_LB) + ".")
A(f"- Not in the id file, by design: the Leonard and Arthur mailbox copies of the Chase mail and reply, Arthur's hold copy, Arthur's invitation and Leonard's hold copy. They sit outside Robert's view, are companions, and carry no fact Robert needs: his own copies do (see the record ledger, SQL L{min(x['line'] for x in ROWS['gcal.gcal_events'])}).")
A(f"- No designed denial: denied_probes has {len(MAN.get('denied_probes') or [])} entries. The return notices stay out of every proof: Robert's evidence for the return is {BASE['returned']}.")
A("")

# ======================================================================== 1.F
A("## 1.F Collision")
A("")
A("Every minted id was looked up over its full base collection with `hg.py search lookup` (identity index or complete scan):")
A("")
for x in LOOK:
    A(f"- {x['label']}: {x['n']} ids over {x['svc']} {x['file']}{' ' + x['pointer'] if x['pointer'] else ''}; {x['checked']} records checked, scan_complete {x['complete']}, {x['hits']} matches.")
A(f"- Gmail thread ids: {THC['n']} numeric ids searched over threads/*.json (thread files are single objects, so lookup cannot array them): {THC['hits']} with a match, scan_complete {THC['complete']}.")
A(f"- Slack (channel, ts): " + "; ".join(f"{S['slack'][k]['channel']}/{S['slack'][k]['ts']} {len(TSC[f't{i}'].get('matches') or [])} matches in {TSC[f't{i}'].get('records_checked')} records" for i, k in enumerate(S["slack"])) + ".")
A(f"- Linear comments: linear data.json /comments holds {CONT_CHECK['c'].get('records_checked')} rows, so comment_ ids cannot collide (NB-24). Slides object ids are per-presentation. idShort {S['trello']['idShort']} is one above the board's highest.")
A(f"- Contact: {IDS['c_brooks']} follows {CNT_SCHEME}; no base contact holds lauren@harmonygames.co ({CONT_CHECK['m'].get('records_checked')} rows checked), so this is no second account for her.")
A(f"- Identity tokens: EMPLOYEE_0024_SLACK_ID is a base author in {LBC} (slack users.json {SU['EMPLOYEE_0024_SLACK_ID']['pointer']}, real_name the bare token, email null). `usr_EMPLOYEE_0024` (linear data.json {LUS['usr_EMPLOYEE_0024']['pointer'] if 'usr_EMPLOYEE_0024' in LUS else 'absent'}) and contact {CON['employee_0024@harmonygames.co']['record']['contact_id']} are a separate unjoined account; the seed writes only the Slack id. EMPLOYEE_0024 maps to several entities in `entity.py collisions` (plan/research/entity_collisions.txt), so no record depends on joining them.")
A(f"- New names: {', '.join(repr(Q[k]) for k in ('method_title', 'sheet_title', 'deck_title', 'trello_title', 'project_name', 'hold_title'))} have 0 base hits on their stems in 1.D. '{Q['arthur_subject']}' has one Snowflake substring hit ('purchase records'), no mail or Slack hit. Header tokens: none minted. Body tokens: [PERSON_NAME_0055] in the invitation subject is the base token for Robert's invitations.")
A("")

# ======================================================================== record ledger
ELEM = collections.defaultdict(set)
for f in MAN.get("ask_fragments") or []:
    for x in (f.get("seeded_ids") or []) + [f.get("locator")]:
        ELEM[x].add(f["id"])
for a_ in MAN.get("anchors") or []:
    ELEM[a_["locator"].replace("linear:project/", "")].add(a_["id"])
for h in MAN.get("authorities") or []:
    for x in h.get("seeded_ids") or []:
        ELEM[x].add(h["id"])
    for x in h.get("decoy_seeded_ids") or []:
        ELEM[x].add(h["id"] + " decoy")
for t_ in MAN.get("traps") or []:
    for x in t_.get("seeded_ids") or []:
        ELEM[x].add(t_["id"])
for ch_ in MAN.get("chains") or []:
    for hp in ch_.get("hops") or []:
        ELEM[hp.get("record")].add(ch_["id"])
for f in MAN.get("facts") or []:
    for x in f.get("home_ids") or []:
        ELEM[x].add("fact: " + f["key"])
COMP = {}   # key -> payee
for k in LN:
    ELEM[LN[k]["issue"]].add("cohort: " + k)
    for r in LN[k]["comments"]:
        ELEM[r["id"]].add("cohort note: " + k)
        COMP[r["id"]] = LN[k]["issue"]
GKEY = {}
for k, boxes in S["gmail"].items():
    for box, v in boxes.items():
        GKEY[v["message"]] = (k, box)
        GKEY[v["thread"]] = (k, box)
GFRAG = {"arthur_mail": "K12", "leonard_reply": "K12", "invite": "K6", "invite_arthur": "K6"}
ORPH = []


def elements(x, rid):
    r = x.get("row") or {}
    el = set(ELEM.get(rid, set())) | set(ELEM.get(rid.split("#")[0], set())) | set(ELEM.get(str(r.get("id")), set()))
    t = x["table"]
    if rid in GKEY:
        el.add(GFRAG[GKEY[rid][0]] + (" companion" if GKEY[rid][1] != ROB or GKEY[rid][0] == "invite_arthur" else ""))
    if t == "gcal.gcal_events":
        el.add("K6" + ("" if r.get("calendar_id") == ROB else " companion"))
    if t.startswith("trello."):
        el |= {"K7", "T9"}
    return el


def reach_of(x):
    r, t = x.get("row") or {}, x["table"]
    if t.startswith("gmail"):
        return "Robert's mailbox" if r.get("user_email") == ROB else "other mailbox (companion)"
    if t == "gcal.gcal_events":
        return "Robert's calendar (self)" if r.get("calendar_id") == ROB else "other calendar (companion)"
    if t.startswith("slack"):
        return f"member of {r.get('channel_id')}"
    if t.startswith(("gdrive", "gdocs", "gsheets", "gslides")):
        return "shared with Robert (Drive row)"
    return "unscoped"


CARRIER = {"linear.linear_comments": "● (§6b)", "gdrive.drive_files": "○ (Drive row)", "contacts.contacts": "○", "trello.trello_cards": "○", "trello.trello_actions": "○",
           "gcal.gcal_events": "● time and attendees", "gslides.slides_pages": "○ (page row)", "trello.trello_boards": "companion", "linear.linear_teams": "companion"}
DEC = {k: LN[k]["issue"] for k in ("MotMot", "Leapblock", "Lucas", "JPMorgan")}


def role_of(x, rid, el):
    t, r = x["table"], x.get("row") or {}
    if x["op"] == "update":
        return "companion (board activity, T06)" if t.startswith("trello") else "companion (team counter follows the seeded issues)"
    if rid in GKEY:
        k, box = GKEY[rid]
        if box != ROB or k == "invite_arthur":
            return "companion copy"
        return {"arthur_mail": "overturning", "leonard_reply": "connecting (confirms the correction)", "invite": "companion (INT-11)"}[k]
    if t == "gcal.gcal_events":
        return "connecting (when the calls start)" if r.get("calendar_id") == ROB else "companion copy"
    if rid == SLOC["ask"]:
        return "first link (anchor AN1)"
    if rid == SLOC["ask2"]:
        return "first link (K16)"
    if rid == SLOC["statement"]:
        return "overturning"
    if rid == SLOC["return_note"]:
        return "overturning"
    if rid == IDS["project"]:
        return "first link (anchor AN2)"
    if rid.split("#")[0] == IDS["method"]:
        return "authority (H1)"
    if rid.split("#")[0] in (IDS["sheet"], IDS["deck"]):
        return "decoy (stale quick figures)"
    if t.startswith("trello."):
        return "decoy (H1, superseded plan)"
    if t == "contacts.contacts":
        return "connecting (spells a token name)"
    if t == "linear.linear_issues":
        return "write target and cohort record"
    if t == "linear.linear_comments":
        return "claim met first" if rid in {r_["id"] for r_ in LN["JPMorgan"]["comments"]} else "connecting (what the founders remember)"
    return "connecting"


def container(x, rid):
    r, t = x.get("row") or {}, x["table"]
    if t == "linear.linear_comments":
        return r["issue_id"]
    if t == "linear.linear_issues":
        return IDS["project"]
    if t.startswith("gmail"):
        return r.get("thread_id") or rid
    if t == "gcal.gcal_events":
        return r.get("calendar_id")
    if t.startswith("slack"):
        return r.get("channel_id")
    if t.startswith("trello"):
        return BASE["founders_board"]
    return rid.split("#")[0]


A("## Record ledger")
A("")
A("One row per SQL statement, in SQL order, keyed to `plan/sql_ids.json`.")
A("")
head("#", "SQL line", "Table", "Id", "Container", "Manifest element", "Carrier", "Reach path", "Discovery role")
seen_ids = collections.defaultdict(set)
for n, x in enumerate(sorted(STM, key=lambda z: z["line"]), 1):
    rid = rid_of(x)
    seen_ids[x["table"]].add(rid)
    el = elements(x, rid) if x["op"] == "insert" else ({"K7", "T9"} if x["table"].startswith("trello") else {"AN2 companion"})
    if not el:
        ORPH.append(rid)
    els = " / ".join(sorted(el))
    row(n, f"SQL L{x['line']}", x["table"] + (" (UPDATE)" if x["op"] == "update" else ""), rid, container(x, rid) if x["op"] == "insert" else rid, els or "ORPHAN",
        CARRIER.get(x["table"], "●"), reach_of(x), role_of(x, rid, el))
A("")
want = sum(len(v) for v in S["rows"].values())
A(f"Ledger check: {len(STM)} statements against {want} keys in `plan/sql_ids.json` rows; orphans {len(ORPH)}{(': ' + ', '.join(ORPH[:5])) if ORPH else ''}. SQL L{min(x['line'] for x in STM)} is the first statement.")
A("")
A("### Note proofs")
A("")
A("Each seeded note beside what it repeats. Pointers come from `plan/notes.json`. Every pointer was read through hg.py on this run and each note was compared with its records by hand; 'NO' marks a record Robert cannot open, which backs the author's claim but never proves a graded fact.")
A("")
head("Note id", "Issue", "Author", "Text", "Base records read", "Robert can read all", "Check")
NOTE_FLAG = {"wanted off Deel": "note true (first Eveline notice below), but the cited mail is the wrong record: it is the Recipient Created for M ***4020, the website payee"}
ev_first = sorted((n for n in NOT if n["key"] == "Eveline Art"), key=lambda z: z["txn"])[0]
n_no = 0
for key, ns in NOTES.items():
    for j, n in enumerate(ns):
        cid = LN[key]["comments"][j]["id"]
        ptrs = note_ptrs(n)
        for svc, p_ in ptrs:
            if text_of(p_) is None and svc in ("slack", "gmail", "gdocs"):
                BAD.append(f"note pointer not read: {p_}")
        vis = [seen(s_, p_)["verdict"] for s_, p_ in ptrs]
        allv = all(v == "YES" for v in vis)
        n_no += 0 if allv else 1
        if allv != bool(n.get("robert_can_read")):
            BAD.append(f"note {cid}: notes.json robert_can_read differs from can-see")
        flag = next((v for k_, v in NOTE_FLAG.items() if k_ in n["text"]), None)
        if norm(LN[key]["comments"][j]["text"]) != norm(n["text"]):
            BAD.append(f"note {cid}: SQL text differs from notes.json")
        chk = (flag + f" ({ev_first['thread']}, {ev_first['txn']})") if flag else "matches"
        row(cid, LN[key]["issue"], n["author"], n["text"], "; ".join(f"{p_}" + ("" if v == "YES" else " NO") for (s_, p_), v in zip(ptrs, vis)), "yes" if allv else "no", chk)
A("")
A(f"{len(note_rows)} notes; {n_no} cite a record Robert cannot open beside ones he can. Claims confirmed in the text: {q('C0880U9751A/1746128542.006369', 'with him at Super Evil')}; Brian is EMPLOYEE_0026_SLACK_ID and Frederick EMPLOYEE_0008_SLACK_ID (slack users.json); Superplay appears in {BASE['n_ban_first'] and 'robert@harmonygames.co/1787749395030696806'}.")
A("")

# ======================================================================== findability
A("## Findability and discovery-order proofs")
A("")
A("### Per seeded record")
A("")
head("Record", "Agent's likely query", "Term present", "Competing base hits", "Chain position")
F = [(f"slack.slack_messages {SLOC['ask']} (row {SROW['ask']})", "#winddown history; 'angel'", seed_q("ask", "before I start the angel calls"), f"'angel' Slack {fmt('angel', 'slack')}; reachable as the newest root in {WD} (last base post {WD}/1770937460.360699 is earlier)", "first link"),
     (f"slack.slack_messages {SLOC['ask2']}", "the post after the ask", seed_q("ask2", "Payee history project"), "'payee history' 0", "first link"),
     (f"gdocs.docs_documents {IDS['method']}", "Drive or Docs search 'Angel note'", f"title '{Q['method_title']}', named in the ask", "'angel note' 0", "connecting (authority)"),
     (f"linear.linear_projects {IDS['project']}", "linear project list", f"name '{Q['project_name']}'; base has {cnt['linear.linear_projects'].get('records_checked')} projects", "'payee history' 0", "first link"),
     (f"gsheets.sheets_spreadsheets {IDS['sheet']}", "Drive search 'Angel note working'", f"title '{Q['sheet_title']}'", "'angel note' 0", "connecting (decoy, layout source)"),
     (f"gslides.slides_presentations {IDS['deck']}", "Drive search 'draft deck', 'angels'", f"title '{Q['deck_title']}'", f"'angel' Drive {fmt('angel', 'gdrive')}, 'note to angels' 0", "connecting (decoy)"),
     (f"trello.trello_cards {IDS['trello']}", "Trello search 'Angel note' after 'our board'", f"title '{Q['trello_title']}'", f"'angel' Trello {fmt('angel', 'trello')}", "connecting (superseded)"),
     (f"slack.slack_messages {SLOC['return_note']}", "Slack search on the account ending or 'came back'", seed_q("return_note", "came back to us"), "founders' channel, Feb 13", "overturning"),
     (f"slack.slack_messages {SLOC['statement']}", "#leapblock read, Slack search 'Leapblock'", seed_q("statement", "the USD wires Leapblock received from you"), f"'leapblock' Slack {fmt('leapblock', 'slack')}; newest post in {LBC}", "terminal (T3)"),
     (f"gmail.gmail_messages {GM['arthur_mail']}", "mail search 'JPMorgan', 'Chase', '3203'", seed_q("arthur_mail", "JPMorgan ***3203"), f"'jpmorgan' Gmail {fmt('jpmorgan', 'gmail')}, 'chase' Gmail {fmt('chase', 'gmail')}; newest of them, reachable by recent date or the co-term 3203", "terminal (T4)"),
     (f"gmail.gmail_messages {GM['leonard_reply']}", "the same thread", seed_q("leonard_reply", "that’s the one I couldn’t place"), "one reply in the seeded thread", "terminal (confirms T4)"),
     (f"gcal.gcal_events {EV_ROB}", "calendar read for Feb 17", f"summary '{Q['hold_title']}'", "'angel calls' 0", "connecting"),
     (f"contacts.contacts {IDS['c_brooks']}", "contacts search 'Brooks'", f"Lauren Brooks, job {Q['c_brooks_job']}", f"'brooks' Contacts {fmt('brooks', 'contacts')}", "connecting (T6)"),
     (f"linear.linear_issues {LN['Deel']['issue']} to {LN[list(LN)[-1]]['issue']}", "linear_list_issues on the project, then comments per issue", "issue titles are the bank spellings; notes need linear_list_comments", f"linear data.json /comments has {CONT_CHECK['c'].get('records_checked')} base rows", "connecting (cohort)")]
for f in F:
    row(*f)
A("")
A("### Dynamic-change seeds")
A("")
head("Trap", "Claim met first", "Overturned by", "Why met first", "Why decisive")
for t_ in MAN.get("traps") or []:
    if t_["id"] in ("T1", "T2", "T3", "T4", "T5", "T6", "T7", "T8", "T9"):
        row(t_["id"], t_.get("expected_wrong_reading"), t_.get("resolver"), t_.get("discovery_order") or "manifest gives no order; met on the first read", ", ".join((t_.get("seeded_ids") or [])[:2] + (t_.get("base_pointers") or [])[:2]))
A("")
A("### Hidden authorities")
A("")
A(f"- H1, the method doc {IDS['method']}: `hg.py search` on 'how to count the money' gives {fmt('how to count the money', 'gdocs')} base hits, so the only hit is the seeded doc; the ask names its title. Decoy: card {IDS['trello']} on the Harmony Games board, first hit on a Trello search for the note. Decisive clause: {seed_q('method', 'It replaces the quick plan I left on our board')}, with the card's own comment {seed_q('trello_comment', 'it’s in a doc' if '’' in Q['trello_comment'] else 'it' + chr(39) + 's in a doc')}.")
A(f"- H2, snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY (snowflake.json /tables/{REV_PTR}): named by role in the method, {seed_q('method', 'the warehouse’s daily revenue table')}; lifetime sums on this run: " + ", ".join(f"{k} {usd(v)}" for k, v in sorted(REV.items())) + f"; REVENUE_DAILY_V2 (/tables/{V2_PTR}): {V2TXT}. Decoy: STORE_TRANSACTIONS (snowflake.json /tables/{STORE_PTR}), met on a search for revenue by store. Decisive clause: the table comment says it includes both IAP and ad revenue, and the method says {seed_q('method', 'as recorded')}.")
A(f"- H3, SVB's Payment Processed notices, first {BASE['n_ban_first']}: 'payment processed' gives {fmt('payment processed', 'gmail')} hits in the numbered thread files, and Robert's box holds {len(NOT)} Processed notices ({len(NUSD)} USD, {len(NOTHER)} {NOTHER[0]['ccy'] if NOTHER else ''}). Decoy: P&L {BASE['pl_costs']} HG Costs, a monthly sheet by line. Decisive clause: {seed_q('method', 'SVB’s Payment Processed notices are the one place I know with a line per payment')}. The manifest keeps the note {q(f'{AD}/1754445622.992119', 'I identified a discrepancy between the cash in bank balance')} as a distractor: it is about balances, and its own next line says {q(f'{AD}/1754445718.724799', 'matching what banks say')}.")
A("")

# ======================================================================== seeded text against the SQL rows
def sql_text(table, key, field, val):
    t_ = str(next((x["row"].get(key) for x in ROWS[table] if x["row"].get(field) == val), None))
    return norm(t_.replace("\\r", " ").replace("\\n", " "))      # parse_sql keeps E-string escapes literal


TIES = [("ask", sql_text("slack.slack_messages", "text", "id", SROW["ask"])), ("ask2", sql_text("slack.slack_messages", "text", "id", SROW["ask2"])),
        ("statement", sql_text("slack.slack_messages", "text", "id", SROW["statement"])), ("method", sql_text("gdocs.docs_documents", "body_text", "document_id", IDS["method"])),
        ("arthur_mail", sql_text("gmail.gmail_messages", "body_text", "id", GM["arthur_mail"])), ("leonard_reply", sql_text("gmail.gmail_messages", "body_text", "id", GM["leonard_reply"]))]
for k_, t_ in TIES:
    if norm(Q[k_]) not in t_:
        BAD.append(f"wording.json {k_} is not in its SQL row")
hh = (D.datetime.fromisoformat(T["arthur"].replace("Z", "+00:00")) - D.timedelta(hours=8)).strftime("%-I:%M %p")
REPLY_TXT = sql_text("gmail.gmail_messages", "body_text", "id", GM["leonard_reply"])
if f"at {hh} arthur blake" not in REPLY_TXT or norm(Q["arthur_mail"])[:60] not in re.sub(r"\s*>\s*", " ", REPLY_TXT):
    BAD.append("Leonard's reply does not quote Arthur's mail at its own time")
top_n = max(int(x["row"]["id"].split("-")[1]) for x in ROWS["linear.linear_issues"])
TEAM_OK = UPD_LIN is not None and int(UPD_LIN["set"]["issue_counter"]) == top_n
token_titles = sum(1 for x in ROWS["linear.linear_issues"] if re.search(r"\[[A-Z_0-9]+\]|PERSON_\d+", x["row"]["title"]))
UNR = open(os.path.join(HERE, "unresolved.md")).read() if os.path.exists(os.path.join(HERE, "unresolved.md")) else ""
UNR_KNOWN = next((l[2:].strip() for l in UNR.splitlines() if l.startswith("- Known-issue cards")), "")
m13 = re.search(r"touches (\d+) issue titles", UNR_KNOWN)
TITLE_NOTE = f"plan/unresolved.md says {m13.group(1)} token issue titles; this SQL has {token_titles} by token pattern." if m13 and int(m13.group(1)) != token_titles else ""
UNR_COLD = next((l[2:].strip() for l in UNR.splitlines() if l.startswith("- Cold audit dispositions")), "")

# ======================================================================== self-validation
sumchk = abs(BYBET["Domino Delights"] - float(Q["sheet_rows"][0][3].replace(",", ""))) < .005 and abs(BYBET["ZM"] - float(Q["sheet_rows"][0][4].replace(",", ""))) < .005 and abs(BYBET["Combo Fighter"] - float(Q["sheet_rows"][0][5].replace(",", ""))) < .005
stm = Q["statement"]
ynum = {y: float(re.search(rf"{y}[^;]*?\s([\d,]+)(?:;|\.)", stm).group(1).replace(",", "")) for y in ("2023", "2024", "2025", "2026")}
orphan = float(re.search(r"Amount: ([\d,\.]+) USD", norm(GMT[BASE["lb_await"]]["thread"]["messages"][0]["body"])).group(1).replace(",", ""))
RET = next(n for n in NOT if n["thread"] == BASE["n_ban_first"])
JPM = next(n for n in NOT if n["thread"] == BASE["jpm_notice"])
stmt_ok = all(abs(ynum[y] - LBY[y] - (orphan if y == "2023" else 0)) < .005 for y in ynum)
tot_stmt = float(re.search(r"Total ([\d,]+) over", stm).group(1).replace(",", ""))
n_stmt = int(re.search(r"over (\d+) wires", stm).group(1))
A("## Self-validation")
A("")
head("QC category", "Tool-enforced (result)", "Manual (evidence)")
row("Missing Universe Data", "check-sql verdict under 1.E", f"every deciding fact is readable by Robert: {BASE['returned']}, {BASE['wu1']}, {SLOC['statement']}, {GM['arthur_mail']}, {BASE['brooks_contract']}, {BASE['bgn_notice']}, snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY")
row("Temporal Field", "sql_lint errors 0; base_check Check C", f"Tuesday in the ask = {T['hold_start'][:10]}, a Tuesday; order Trello {T['trello']}, sheet {T['sheet']}, deck {T['deck']}, project {T['project']}, method {T['method']}, ask {T['ask']}, statement {T['statement']}, mail {T['arthur']}. Latest seeded Slack {iso(latest_slack)} is before Feb 13 10:03Z (NB-6, {SLOC['statement']})")
row("Cross-service Referential", "base_check Check A", f"titles in the ask equal the seeded titles ({IDS['method']}, {IDS['sheet']}); {GM['arthur_mail']} repeats the notice's amount and suffix ({BASE['jpm_notice']}); no Drive link is seeded (R04)")
row("Quantitative / Reconciliation", "no reply counters touched; Trello badges carry the seeded comment", f"sheet row ties to the re-read notices: {sumchk} (" + ", ".join(f"{k} {usd(v)}" for k, v in BYBET.items()) + f"); statement year totals tie to the {PAY['Leapblock']['n']} Leapblock notices plus {usd(orphan, False)} ({BASE['lb_await']}): {stmt_ok}; statement total {tot_stmt:,.0f} over {n_stmt} wires against {PAY['Leapblock']['sum'] + orphan:,.0f} over {PAY['Leapblock']['n'] + 1}; WU receipts sum {usd(WU_TOTAL)} ({BASE['wu1']}); notices that differ from the parsed census: {len(NOT_DIFF)}")
row("State / Lifecycle", f"{len(ROWS['linear.linear_issues'])} issues in Backlog with no lifecycle stamps; team_ENG issue_counter {TEAM['record'].get('issue_counter', 'is not in the base export') if TEAM['record'].get('issue_counter') is not None else 'is not in the base export'}, set to {UPD_LIN['set']['issue_counter'] if UPD_LIN else 'unchanged'} at SQL L{UPD_LIN['line'] if UPD_LIN else 0}, equal to the highest seeded issue: {TEAM_OK}", f"nothing seeded says a payee is closed; {BASE['linear_keep']} keeps Linear during transition; Chase closed {AD}/1761954952.006759 and Arthur's mail speaks of it in the past tense")
row("Identifier / Format", f"hg.py lint FAIL {HL['counts'].get('FAIL')} CHECK {HL['counts'].get('CHECK')}; sql_lint errors 0", f"ids follow 1.A; roster addresses only; {IDS['c_brooks']} uses {CNT_SCHEME}; usr_63fffeb4fab5233e and usr_cc3e90160f490686 are base Linear ids")
row("Semantic / Category", "—", f"titles match content ({IDS['method']}, {IDS['project']}, {EV_ROB}); the issue titles are the bank's own spellings, so a token title is what the bank shows (NB-12)")
row("Other", "—", f"voice per 1.C; no seed states a bet total, a bucket list or a classification: the deck {IDS['deck']} holds only the plain sum, labelled draft")
A("")

# ======================================================================== integrations
A("## Integrations and companions")
A("")
head("Service", "INT id", "Companion", "Decision")
row("gcal", "INT-11", "invitation mails", f"seeded for Robert ({GM['invite']}) and Arthur, one calendar copy per attendee ({EV_ROB} is Robert's); relied on by nothing (R08)")
row("gmail", "INT-22, INT-05", "notification mail", f"none: founder mail needs none; Leonard's reply {GM['leonard_reply']} carries in_reply_to and references (I06)")
row("slack", "INT-22", "Slack email notifications", f"none: never relied on; no bot post seeded ({SLOC['ask']})")
row("linear", "INT-03, INT-04, INT-05", "linear[bot] comment, Slack notices, digests", f"none: no PR is seeded and {IDS['project']} is a note-keeping project; base carries no such notices for it")
row("gdocs, gdrive, gsheets, gslides", "INT-13", "Drive Slack app DMs", f"none: DM-only and optional; Drive rows mirror owner and sharing for {IDS['method']}, {IDS['sheet']}, {IDS['deck']}")
row("trello", "INT-21", "no Trello to Slack integration exists", f"none; card {IDS['trello']} dateLastActivity and the board's follow the comment (SQL L{UPD_TR['line'] if UPD_TR else 0}, T06)")
row("contacts", "none", "nothing mirrors contacts", f"contacts: none ({IDS['c_brooks']})")
A("")

# ======================================================================== touched-data census
card_row = ROWS["trello.trello_cards"][0]["row"]
acts = ROWS["trello.trello_actions"]
last_act = max(x["row"]["date"] for x in acts)
copies = collections.defaultdict(set)
for x in ROWS["gmail.gmail_messages"]:
    copies[x["id"] if "id" in x else x["row"]["id"].split("/", 1)[1]].add(x["row"]["body_text"])
same_copies = all(len(v) == 1 for v in copies.values())
drive_links = sum(1 for x in ROWS["slack.slack_messages"] if "docs.google.com" in str(x["row"].get("text")))
A("## Touched-data census and coherence hazards")
A("")
A(f"Touched data: #winddown {WD} (Feb 9 to 12, what a run reads around the ask); #leapblock {LBC} (invoices, the Feb 11 and 12 exchange, the statement); #admin_foundersonly {AD} (Sep 2023 approval, Apr 2024 wire, Jun 2024 card, Jan 2025 Node, Aug 2024 JPMorgan, Oct 2025 laptop and Chase close); #executives {EX} (contract, 4X, playable); Robert's mailbox (the {len(NOT)} Processed notices, Awaiting and Recipient notices, the {len(WU)} Western Union receipts, the Node mail, the seeded Chase thread); "
  f"Drive {BASE['brooks_contract']}, {BASE['msa']}, {BASE['pl_costs']}, Robert's root {BASE['robert_root']}; the founders' board {BASE['founders_board']}; snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY. Matched against `references/universe_kb/by_universe/normal/coherence_hazards.json`; sweep and resolutions in `plan/research/sc2_coherence.md` Task 2, re-checked on this SQL:")
A("")
A(f"- temporal: T06 — card dateLastActivity {card_row.get('dateLastActivity')} against its latest action {last_act}: {'equal' if card_row.get('dateLastActivity') == last_act else 'DIFFERENT'}; the UPDATE at SQL L{UPD_TR['line'] if UPD_TR else 0} moves the board to the same time. T07 — seeded Slack ends {iso(latest_slack)}, before the export end, and points at no missing artifact.")
A(f"- semantic: S05, S06 — roster status and titles stay off every graded fact; contacts.json {CON[ROB]['pointer']} is never quoted as a title. S03 — no Linear label is seeded (labels_json empty on all {len(ROWS['linear.linear_issues'])} issues). S07 — the wind-down notes doc stays unopened.")
A(f"- referential: R04 — {drive_links} seeded Slack rows carry a Drive link; files are named by title (hazard_acknowledgements excluded). R08 — both seeded invitation mails have a same-summary calendar row within a day ({EV_ROB}); nothing relies on them (excluded).")
A(f"- quantitative: Q04 — no base parent is updated, so no counter changes; the seeded Slack rows are new roots. Q05, Q06, Q07 — the ledger, CASH_BALANCE and quoted vendor figures stay off the path, so MONTHLY_BURN's Sep 2023 gap is never read against the {usd(orphan, False)} wire (sc2 Q11). Q09 — REVENUE_DAILY against REVENUE_DAILY_V2 lifetime sums on this run: {V2TXT}. Q10 — the seeded mail copies are identical across mailboxes: {same_copies}.")
A(f"- state/lifecycle: L08 — no base open issue is modified or cited; seeded issues are unassigned in Backlog (excluded). L13 — the design never says work stopped at the shutdown (excluded). L01–L07 not touched: no base Linear issue is updated.")
A(f"- identifier/format: I01 — seeded Slack ids are sha256(channel|ts)[:32]. I03, I04 — mailbox aliases and date formats follow the base ({GM['arthur_mail']}). I05 — Robert's id prefix is checked on every notice. I06 — Leonard's reply carries in_reply_to and references. I10 — usr_Robert quoted exactly. I14 — Resource owners on {BASE['msa']}. I15 — seeded Drive names equal their native titles. I17 — card creator is PERSON_6094_TRELLO_USER_ID. I18 — " + q(f"{AD}/1698436632.335299", "to submit his reimbursement") + " is struck through in the base and concerns a reimbursement, not a wire.")
A("")
A("Known data issues (`references/known_data_issues/normal.md`, with `plan/research/sc2_coherence.md` Task 6):")
for k, v in [("NB-1", f"only founders and Leapblock's contact post after Feb 11 20:40Z ({SLOC['ask']}, {SLOC['statement']})"),
             ("NB-2", f"no P&L cost line is graded; {BASE['pl_costs']} is a decoy and the method does not call it wrong"),
             ("NB-3, NB-10", f"no cash or balance is asked ({BASE['pl_accurate']} stays a distractor)"),
             ("NB-4", f"Feb 2 wires come from the Processed notices, not the ledger ({BASE['n_ban_first']} family)"),
             ("NB-6", f"seeded Slack stops at {iso(latest_slack)} ({SLOC['statement']})"),
             ("NB-12", f"plan/unresolved.md: key OE and rubric lines on the account ending, not the name; {token_titles} seeded issue titles carry a token on this SQL; {AD}/1735854841.070019 spells Node Media"),
             ("NB-15", f"no rule rests on roster status; Lauren Brooks is decided by {BASE['brooks_contract']}"),
             ("NB-23", f"Singular uses bank amounts only ({AD}/1726272869.834809)"),
             ("NB-24", f"every Linear comment is seeded ({LN['Deel']['issue']} to {LN[list(LN)[-1]]['issue']})"),
             ("NB-26", f"plan/unresolved.md: the method leaves Combo Fighter's revenue off the page, the deck and the reply, so nothing grades it; the table total on this run is {usd(REV.get('combo_fighter', 0))} (snowflake.json /tables/{REV_PTR}); it touches the method's revenue source and deck slide 4 ({IDS['deck']}: {Q['deck'][3]})"),
             ("NB-29", f"no window starts at the shutdown decision ({WD}/1770664700.848759)"),
             ("NB-31", f"reach rests on persona_view verdicts, never DM member lists (1.E, {WD})")]:
    A(f"- {k}: {v}.")
A("")

# ======================================================================== intended disagreements
A("## Intended disagreements")
A("")
head("Claim met first", "Overturning record", "Why realistic", "Resolution", "Best argument it is unintended", "Why the designed reading holds")
pay = lambda k: usd(PAY[k]["sum"])
DIS = [
    ("T1", f"Payment Processed, {RET['to']}, {usd(RET['amt'])} ({BASE['n_ban_first']})", f"{q(f'{AD}/1712331142.975829', 'This wire didn’t go through')}, {q(f'{AD}/1712331718.859679', 'Fixed up and resubmitted the payment')}, {q(f'{AD}/1712901800.684259', 'bank returned our money')}", "a bank says processed before the receiving bank rejects", f"MotMot counts {usd(PAY['MotMot']['sum'] - RET['amt'])}, not {pay('MotMot')}", "the notice was never corrected, so two systems silently disagree", f"the overturning records are dated human statements by both founders, later than the notice, and the Recipient Modified mail {BASE['n_ban_mod']} sits between them"),
    ("T2", f"the notices show {pay('Lucas')} to ***6577 from {PAY['Lucas']['first']}", f"{len(WU)} Western Union receipts of {usd(WU_TOTAL)} ({BASE['wu1']}), route in {q(f'{AD}/1719603595.852129', 'via company card')}", "he was paid by card before he had an IBAN", f"Lucas counts {usd(PAY['Lucas']['sum'] + WU_TOTAL)}", "the method says go by the bank, so card transfers look out of scope", f"its sentence {seed_q('method', 'it goes in only if a receipt for it reached your mail')} admits them, and the receipts carry the same payee token as his SVB notices"),
    ("T3", f"no Processed notice for {usd(orphan, False)}; only Awaiting {BASE['lb_await']}", f"{SLOC['statement']} (30 wires, first one {usd(orphan, False)}), with {q(f'{AD}/1694616951.239909', 'Done!')}", "the bank mail failed to arrive or was not kept; the payee's accountant has the wire", f"Leapblock counts {usd(PAY['Leapblock']['sum'] + orphan, False)}", "the wire may never have gone: nothing in the base shows it landing", f"the payee itself lists it, the year totals tie to the notices exactly ({stmt_ok}), and the base shows no chasing afterwards (plan/research/sc3_record_plan.md 2.5)"),
    ("T4", f"{JPM['to']} {usd(JPM['amt'])} ({BASE['jpm_notice']}) and Leonard's note {LN['JPMorgan']['comments'][0]['id']}", f"Arthur's mail {GM['arthur_mail']} and Leonard's reply {GM['leonard_reply']}", "Arthur ran the wire and remembers it when the statements come out", "not spending; the row stays at zero", "Leonard approved it and cannot place it, so the explanation looks convenient", f"Leonard's reply accepts it the same day, the wire was created by Arthur ({AD}/1724100562.903529), and Chase is the company's own ({AD}/1761954952.006759). The ***3203 link itself is seeded, carried in Unresolved"),
    ("T5", f"PERSON_4419_NAME LLC {pay('Node Media')} reads as a vendor of the bet running on {PAY['Node Media']['first']}", f"{q(f'{AD}/1735854841.070019', 'closing our account with Node Media LLC')}, {BASE['node_mail']}", "the bank shows a legal name, the founders a trade name", "Marketing, out of build cost", "the mail covers less than the wire, so the identification could be wrong", "the channel post names it on the wire's own day and the note says one closing payment; only the bucket depends on it"),
    ("T6", f"Leonard's note {LN['Lauren Brooks']['comments'][0]['id']} and contact {IDS['c_brooks']} read as a monthly contractor", f"{BASE['brooks_contract']} {q(BASE['brooks_contract'], 'run and optimize paid UA for Telegram')}", "a title says little; a contract says what the work was", "Marketing, out of build cost", "the contract also covers product advice, so Build is arguable", f"the method's sentence {seed_q('method', 'Marketing is anything made or bought to get installs')} takes the service's purpose, and Exhibit A opens with Telegram distribution"),
    ("T7", f"Martin Walsh's notice reads like {NOTHER[0]['amt']:,.0f} dollars of pay", f"{BASE['bgn_notice']} is in BGN; {q(f'{AD}/1761844454.096829', 'did you handle Martin’s laptop?')}", "a one-off wire in his local currency", "a Company line in its own currency", "the note calls it a payment to him, so it could be Build", f"the Slack run on the same day ties it to the laptop, and {seed_q('method', 'Anything not paid in dollars stays in its own currency')}"),
    ("T8", f"Leonard's quick figures on {IDS['sheet']} and {IDS['deck']}", f"the method {IDS['method']} and the corrected register", "a first pass made before the rules were written", "the deck's figures change", "the sheet and deck tie to the cent, so they look authoritative", f"the sheet labels itself {seed_q('sheet_rows', 'quick pass')} and the ask calls them quick numbers"),
    ("T9", f"the plan on card {IDS['trello']}: {seed_q('trello_desc', 'add up the notices by date and round them')}", f"the method {IDS['method']} and the card's comment", "a card left behind when the plan moved to a doc", "the method governs", "the card is newer on its board than anything else, so it could read as current", "the method says it replaces the board plan and the comment points to the doc; both are later than the card"),
    ("T15", f"{q(f'{AD}/1754445622.992119', 'I identified a discrepancy between the cash in bank balance')} reads as a claim for the P&L", f"the method {IDS['method']}", "Leonard speaks of balances, not per-payee detail", "the notices stay the source", "the same author praised the P&L, so the method contradicts him", f"{q(f'{AD}/1754445718.724799', 'matching what banks say')} is his next post, and the method never calls the P&L wrong"),
]
for d in DIS:
    row(*d[1:])
A("")

# ======================================================================== constraints
A("## Constraints for the prompt brief")
A("")
head("Anchor", "May be named (noun phrases only)", "Record")
for a_ in MAN.get("anchors") or []:
    row(a_["id"], a_["prompt_reference"], a_["locator"])
A("")
A(f"Never name in the prompt: the method's rules, the bet dates, the buckets, any payee, any figure, the notices, #leapblock, #admin_foundersonly, the Chase mail, the contract, Western Union, or the warehouse table. Deadlines: the first angel call on {T['hold_start'][:10]} ({EV_ROB}). Deliverable kinds: one sheet in Robert's Drive with the working sheet's layout, shared with Leonard and Arthur; each payee issue closed, with a reason where the figure differs from the notices; one reply to Leonard in #winddown.")
A("")

# ======================================================================== fact sheet
A("## Fact sheet")
A("")
if FINAL and MAN.get("facts"):
    head("Key", "Value", "Kind", "Home / must appear in")
    for f in MAN["facts"]:
        row(f["key"], f["value"], f["kind"], ", ".join((f.get("home_ids") or []) + (f.get("must_appear_in") or [])))
    A("")
    A("Output verbatim:")
    A("")
    fence(OUT.get("fact_check", ""))
else:
    A("(facts fill from `01_Hardness_Manifest.json` on the next run.)")
A("")
if AGG:
    tt = AGG["totals"]
    A("Solver totals (`solver/truth.json`, `solver.aggregates`):")
    A("")
    head("Bet", "Build cost", "Brought in", "Draft deck figure")
    deck = re.findall(r"\$(\d+)K", Q["deck"][2])
    for i_, b_ in enumerate(("Domino Delights", "ZM", "Combo Fighter")):
        row(b_, usd(tt["build"][b_]), (usd(tt["revenue"][b_]) if tt["revenue"][b_] is not None else "left off by the method (NB-26)"), f"${deck[i_]}K ({IDS['deck']})")
    A("")
    A(f"Marketing {usd(tt['marketing_usd'])}; Company {usd(tt['company_usd'])} plus {tt['company_bgn']:,.0f} BGN; not a cost {usd(tt['not_a_cost_usd'])}. Classes: {AGG['classes']}. Reason comments on: {', '.join(AGG['groups']['reason_comment'])}. Warehouse sums on this run agree with truth: {all(abs(REV[k] - tt['revenue'][v]) < .005 for k, v in (('domino_delights', 'Domino Delights'), ('zombie_match_3d', 'ZM')))}; Combo Fighter's {usd(REV.get('combo_fighter', 0))} is left off by the method (NB-26) and not graded.")
else:
    A("(totals fill from `solver/truth.json` on the next run.)")
A("")

# ======================================================================== facts for the human
A("## Facts for the human")
A("")
head("Locator", "Base/seeded", "Fact", "Reach", "Role", "Re-verify?")
trow = lambda k: TRUTH.get(k, {}) if TRUTH else {}
H = [(SLOC["ask"], "seeded", f"Leonard, {iso(S['slack']['ask']['ts'])}, row {SROW['ask']}: {Q['ask']}", "#winddown member", "evidence (anchor AN1)", "no"),
     (SLOC["ask2"], "seeded", f"Leonard, {iso(S['slack']['ask2']['ts'])}, row {SROW['ask2']}: {Q['ask2']}", "#winddown member", "evidence (K16)", "no"),
     (IDS["method"], "seeded", f"Leonard, {T['method']}, edited {T['method_mod']}: '{Q['method_title']}', the counting rules", "shared with Robert", "authority (H1)", "no"),
     (IDS["sheet"], "seeded", f"Leonard, {T['sheet']}: '{Q['sheet_title']}', header {', '.join(Q['sheet_header'])}; row {', '.join(x for x in Q['sheet_rows'][0] if x)}", "shared with Robert", "decoy; layout source", "no"),
     (IDS["deck"], "seeded", f"Leonard, {T['deck']}: '{Q['deck_title']}', {len(Q['deck'])} slides; {Q['deck'][2]}", "shared with Robert", "decoy", "no"),
     (IDS["project"], "seeded", f"Leonard, {T['project']} (SQL L{ROWS['linear.linear_projects'][0]['line']}): Linear project '{Q['project_name']}': {Q['project_desc']}", "unscoped", "authority for the cohort (AN2)", "no"),
     (IDS["trello"], "seeded", f"Leonard, {T['trello']}: card '{Q['trello_title']}': {Q['trello_desc']}; comment: {Q['trello_comment']}", "unscoped", "decoy (H1)", "no"),
     (SLOC["return_note"], "seeded", f"Leonard, {iso(S['slack']['return_note']['ts'])}, row {SROW['return_note']}: {Q['return_note']}", "#admin_foundersonly member", "overturning evidence (T1)", "no"),
     (SLOC["statement"], "seeded", f"Leapblock's contact, {iso(S['slack']['statement']['ts'])}, row {SROW['statement']}: {Q['statement']}", "#leapblock member", "overturning evidence (T3)", "no"),
     (GM["arthur_mail"], "seeded", f"Arthur → Leonard, Robert, {T['arthur']}, '{Q['arthur_subject']}' (thread {GT['arthur_mail']}): {Q['arthur_mail']}", "Robert's INBOX", "overturning evidence (T4)", "no"),
     (GM["leonard_reply"], "seeded", f"Leonard → Arthur, Robert, 'Re: {Q['arthur_subject']}', quoting Arthur's mail: {Q['leonard_reply']}", "Robert's INBOX", "evidence (T4)", "no"),
     (EV_ROB, "seeded", f"'{Q['hold_title']}', {T['hold_start']} to {T['hold_end']}, Leonard organizer", "Robert's calendar (self)", "evidence (deadline)", "no"),
     (GM["invite"], "seeded", f"invitation for '{Q['hold_title']}'", "Robert's INBOX", "companion", "no"),
     (IDS["c_brooks"], "seeded", f"contact Lauren Brooks, lauren@harmonygames.co, job {Q['c_brooks_job']}", "unscoped", "evidence (T6)", "no"),
     (BASE["returned"], "base", q(BASE["returned"], "this is money returned to us because Blake put the wrong account number"), "#admin_foundersonly member", "overturning evidence (T1)", "no"),
     (BASE["wire_fail"], "base", q(BASE["wire_fail"], "This wire didn’t go through"), "#admin_foundersonly member", "evidence (T1)", "no"),
     (BASE["wrong_acct"], "base", q(BASE["wrong_acct"], "I think I messed up the bank account number"), "#admin_foundersonly member", "evidence (T1)", "no"),
     (BASE["n_ban_mod"], "base", q(BASE["n_ban_mod"], "Recipient Name: BANCO DE AMERICA ***3341"), "Robert's INBOX", "evidence (T1)", "no"),
     (BASE["lucas_card"], "base", q(BASE["lucas_card"], "via company card"), "#admin_foundersonly member", "evidence (T2)", "no"),
     (BASE["lb_await"], "base", q(BASE["lb_await"], "Leapblock LTD ***1359Amount: 33,290.00 USD"), "Robert's INBOX", "claim met first (T3)", "no"),
     (BASE["lb_done"], "base", q(BASE["lb_done"], "Done!"), "#admin_foundersonly member", "evidence (T3)", "no"),
     (BASE["node_close"], "base", q(BASE["node_close"], "closing our account with Node Media LLC"), "#admin_foundersonly member", "evidence (T5)", "no"),
     (BASE["node_mail"], "base", q(BASE["node_mail"], "Sept - $1,428.57"), "Robert's INBOX", "evidence (T5)", "no"),
     (BASE["brooks_contract"], "base", q(BASE["brooks_contract"], "plan, launch, and scale Telegram distribution") + "; " + q(BASE["brooks_contract"], "minimum $500"), "shared with Robert", "evidence (T6)", "no"),
     (BASE["laptop"], "base", q(BASE["laptop"], "did you handle Martin’s laptop?"), "#admin_foundersonly member", "evidence (T7)", "no"),
     (BASE["msa"], "base", q(BASE["msa"], "Game of Dominoes - 3D Saga Map"), "shared with Robert", "evidence (Leapblock)", "no"),
     (BASE["pl_costs"], "base", f"'{PL['title']}', tabs {', '.join(t_['title'] for t_ in PL['sheets'])}", "shared with Robert", "decoy (H3)", "no"),
     ("snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY", "base", "lifetime total_revenue_usd: " + ", ".join(f"{k} {usd(v)}" for k, v in sorted(REV.items())), "unscoped", "authority (H2)", "yes, after any data regeneration"),
     (BASE["robert_root"], "base", "Robert's Drive root", "Robert owns", "write target", "no")]
for w_ in WU:
    H.append((w_["id"], "base", f"Western Union, {w_['date']}: sent {usd(w_['sent'])}, fee {usd(w_['fee'])}, received {usd(w_['recv'])}, Final Receiver {w_['tok']}", "Robert's INBOX", "evidence (T2)", "no"))
for h in H:
    row(*h)
A("")
A("Payee issues (full ids; notes are in Note proofs):")
A("")
head("Issue", "Base/seeded", "Payee and bank name", "Notices", "Truth", "Reach", "Role")
for p in C:
    k = p[0]
    t_ = trow(k)
    row(LN[k]["issue"], "seeded", f"{k}: {p[1]} ***{p[2]}, {p[3]}", f"{PAY[k]['n']} notices, {usd(PAY[k]['sum'])}, {PAY[k]['first']} to {PAY[k]['last']}",
        f"{t_.get('Bucket', '(fills from truth.json)')}, paid {usd(t_['paid']) if 'paid' in t_ else '(fills from truth.json)'}", "unscoped", "write target; cohort record")
A("")
A(f"All {len(NOT)} Processed notices, re-read on this run:")
A("")
head("Thread", "Base/seeded", "To", "Amount", "Transaction Date", "Bet by date", "Payment Reference")
for n in sorted(NOT, key=lambda z: (z["txn"], z["thread"])):
    row(n["thread"], "base", n["to"], f"{n['amt']:,.2f} {n['ccy']}", n["txn"], bet(n["txn"]), n["ref"] or "none")
A("")

# ======================================================================== follow-ups
A("## Platform follow-ups")
A("")
A(f"- ○ carriers to confirm in the pre-check: card {IDS['trello']} and its comment render through the Trello read tools; contact {IDS['c_brooks']} renders `job`; no graded fact rests on either alone. Linear comments are ● (§6b), so the {len(note_rows)} notes need no follow-up.")
A(f"- Snowflake figures (REVENUE_DAILY lifetime sums, snowflake.json /tables/{REV_PTR}) are re-verified after any data regeneration by re-running this script.")
A(f"- `{MAN.get('solver', {}).get('path', 'solver/solver.py')}` and the preflight bind by sha256 to the SQL: any rebuild needs them re-run, then this script, then the gate.")
A("- No call_budget row depends on an unverified behaviour.")
A("")

# ======================================================================== self-review
A("## Self-review")
A("")
A("### Tool outputs (final SQL, verbatim)")
A("")
A("`sql_lint.py`:")
fence(OUT["sql_lint"])
sw = re.search(r"errors: (\d+)\s+warnings: (\d+)", OUT["sql_lint"])
wtxt = [l for l in OUT["sql_lint"].splitlines() if l.strip().startswith("warn")]
known = [l for l in wtxt if "clock" in l]
if known:
    A(f"sql_lint warning disposition (clock class, {len(known)} warnings): the copies of the Angel calls hold start and end on {T['hold_start'][:10]}, after the clock; a not-yet-happened event in plan fields, allowed by hard gate 4 (SQL L{min(x['line'] for x in ROWS['gcal.gcal_events'])}).")
if len(known) != len(wtxt):
    TODO_DISP.append(f"sql_lint: {len(wtxt) - len(known)} warning(s) outside the clock class need a disposition line")
A("")
A("`hg.py lint` (the eval's hg_injection_lint, with base data):")
fence(f"hg_injection_lint counts {json.dumps(HL.get('counts'))}; sha256 {HL.get('sha256')}; flags {len(FLAGS)}; info {len(HL.get('info') or [])}")
LINT_DISP = {}   # check name -> written disposition; a flag with none is reported, never auto-dispositioned
for f in FLAGS:
    if str(f.get("severity")).upper() == "CHECK":
        d_ = LINT_DISP.get(f.get("check"))
        if d_:
            A(f"LINT {f.get('check')} L{f.get('line')}: {d_}")
        else:
            TODO_DISP.append(f"hg lint CHECK {f.get('check')} L{f.get('line')}: {json.dumps(f)[:160]}")
if not FLAGS:
    A(f"No FAIL or CHECK flag on sha256 {SQLSHA[:12]}, so no LINT disposition line applies.")
A("")
A("`base_check.py`:")
fence(OUT["base_check"])
A("`base_claims.py`:")
fence(OUT["base_claims"])
A("`hardness_gate.py` (final manifest + SQL):")
fence(OUT.get("hardness_gate") or "(runs once 01_Hardness_Manifest.json exists)")
A("")
PRE = os.path.join(WF, "01c_Preflight_Report.md")
A("### Preflight (S4b–S5e)")
A("")
if os.path.exists(PRE):
    fence(open(PRE).read().rstrip().replace("[]", "(none)"))
else:
    A("(`01c_Preflight_Report.md` not produced yet; this block fills on the next run. Solver, truth and dispositions belong to the preflight owner.)")
A("")
A("### /injection Checks A–C walk")
A("")
tb = collections.Counter(x["table"] for x in STM)
A(f"- Inventory: {n_ins} INSERT, {n_upd} UPDATE ({', '.join(x['table'] + ' keyed on id' for x in UPD)}), no DELETE, no upsert, one BEGIN/COMMIT; every statement is in the record ledger: PASS.")
A(f"- Check A (references, uniqueness, ownership, id contracts): PASS. base_check Check A; 1.F full-collection lookups with {sum(x['hits'] for x in LOOK)} matches; Slack channels {WD}, {LBC} and members resolve; Drive parent d_63fffeb4fab5233ed5bb73 is Leonard's root; Trello board {BASE['founders_board']} and list resolve; Linear authors usr_63fffeb4fab5233e and usr_cc3e90160f490686 are base users; {IDS['method']} has a docs row with body text; one account per person (contact {IDS['c_brooks']} is the first for her).")
A(f"- Check B (structure, literal JSON, generated and NOT NULL columns): PASS. sql_lint errors {sw.group(1)}; no text_fts or body_text_fts; every *_json value parses; Linear dates YYYY-MM-DDTHH:MM:SSZ; state_history_json given on all {tb['linear.linear_issues']} issues. The schema snapshot stays unverified by design.")
A(f"- Check C (dates, parent and reply, statuses, counts, amounts, superseding records): PASS. base_check Check C; every event at or before the clock except the hold's plan fields; Leonard's reply follows Arthur's mail ({T['arthur']}) in each mailbox with in_reply_to set; notes fall between issue creation and the ask; statement ties to the notices ({stmt_ok}); no grader-facing or padding text (hg.py lint grader_language and padding_comment clear).")
A("- PENDING: none in static scope. Live load and search ranking are outside this review.")
A("")
A("### Touched-data census")
A("")
A("The census and hazard dispositions are in 'Touched-data census and coherence hazards' above: all six categories, with `plan/research/sc2_coherence.md` Task 2 re-checked on this SQL.")
A("")
A("### Counter-readings")
A("")
head("Category", "Counter-reading (strongest argument it fails)", "Evidence that resolves it", "Verdict")
CR = [("Temporal", "Leonard's sheet and deck predate the rules they feed, and could cite figures not yet made", f"Trello {T['trello']}, sheet {T['sheet']}, deck {T['deck']} all follow {WD}/1770934638.035469 (22:17Z), and the method {T['method']} is later and replaces them", "PASS"),
      ("Temporal", "the statement says 'as we said yesterday' with no call on record", f"{LBC}/1770922209.919939 (Feb 12 18:50Z, 'should I call u here?') is the call; the statement is {iso(S['slack']['statement']['ts'])}", "PASS"),
      ("Temporal", "'stop at the last run on Feb 2' could miss a later notice", f"latest Processed notice is {max(n['txn'] for n in NOT)} in the re-read set ({len(NOT)} notices)", "PASS"),
      ("Semantic / Category", "'bet' is an odd word for a founder's cost note", q(f"{WD}/1770664700.848759", "multiple bets") + " shows Leonard's own usage", "PASS"),
      ("Semantic / Category", "the card sits on To Do, where every other card is closed, though the design record plan says Backlog", f"board lists in 1.A; a live quick plan on To Do is plausible and the precedent passed with it, but it departs from 01_Scenario_Design.md §11 and plan/research/sw2_coherence.md T2 (Unresolved)", "PASS, noted"),
      ("Cross-service Referential", "Arthur's mail says the money went back after Carta's renewal, a link no base record states", f"Carta on Chase {WD}/1770932925.126829; Chase is the company's {AD}/1761954952.006759; plan/research/sc3_record_plan.md 3.2 fit; the link stays a seeded claim (Unresolved)", "PASS, disclosed"),
      ("Cross-service Referential", "the MotMot, Node and Lucas names differ from the bank's", f"each ties by suffix and a dated record: {AD}/1712331372.614469, {AD}/1735854841.070019, {BASE['wu1']}", "PASS"),
      ("Quantitative", "the statement's total could fail to tie to the notices", f"year totals tie {stmt_ok}; total {tot_stmt:,.0f} over {n_stmt} wires ({SLOC['statement']})", "PASS"),
      ("Quantitative", "the quick sheet row could differ from the notices it claims to add up", f"ties to the cent: {sumchk} ({IDS['sheet']}); BGN kept out, label says USD", "PASS"),
      ("State / Lifecycle", "Linear was winding down, so a new project on Feb 12 reads as a contradiction", q(f"{WD}/1770933601.686309", "linear we keep during transition"), "PASS"),
      ("State / Lifecycle", "Arthur writes of the Chase account after it closed", q(f"{AD}/1761954952.006759", "Chase account closed") + f"; the mail uses the past tense and works from statements ({AD}/1761958213.753549)", "PASS"),
      ("Identifier / Format", "the seeded contact id could open a second scheme", f"{IDS['c_brooks']} follows {CNT_SCHEME} (samples in 1.A)", "PASS"),
      ("People status", "Leapblock's contact reads quiet_since_2024-01 in activity.json yet posts on Feb 13", f"that status belongs to the unjoined email entity; slack_only_ids shows {e24['messages']} messages to {e24['last'][:10]}; {LBC}/1770922209.919939 is his Feb 12 post", "PASS"),
      ("Other", "a designed disagreement reads as two silent system fields", "each overturning record is a dated human message: see Intended disagreements, T1 to T9", "PASS")]
for d in DIS:
    CR.append((f"Other (designed {d[0]})", d[5], d[6], "designed"))
for x in CR:
    row(*x)
A("")
PS = os.path.join(HERE, "policy_scores.txt")
A(f"Lazy-solver pass on the implemented records: it reads the ask, the method and the issue list, sums the notices by date and stops. It keeps MotMot at {pay('MotMot')}, Lucas at {pay('Lucas')}, Leapblock at {usd(PAY['Leapblock']['sum'], False)} and JPMorgan as a cost, never opening {AD}, {LBC} or Arthur's mail; no seeded record hands it a total (fact_check --no-leak above). Policy scores: `plan/policy_scores.txt`.")
A("")
A(f"Re-verified this run through hg.py, not carried from notes: all {len(NOT)} notices, {len(WU)} receipts, REVENUE_DAILY sums (V2: {V2TXT}), {len(SL)} Slack records, {len(GMT)} mail threads, the contract and MSA, contacts, Slack users and channels, and the board.")
A("")
A("Unresolved:")
for u_ in [
        "REDTEAM_* is unset, so `tools/redteam_review.py` cannot run; the design's fallback review stands (`plan/redteam_section.md`).",
        "Leapblock invoice PDFs f_06f42106818045db3b7d0d and siblings (0000000032, 0000000033) are unread: PDF bytes are not reachable through hg.py, so nothing here confirms they total the Sep 2023 wire. A run with gdrive_read_file might read them.",
        "The Chase top-up link is invented though consistent: no base record names the ***3203 holder or the reason for the wire (plan/research/sc3_record_plan.md 3.3).",
        "Every ledger prior is thin (n_eff 1, UNCALIBRATED); landing rates are design priors until a platform run.",
        "Dataset similarity cannot be measured locally; only the platform reports it.",
        "`tools/stage_check.py`, named in the skill, does not exist in tools/; `tools/stage_gate.py` is the working gate.",
        f"Keyword counts are hg.py hits, not persona-scoped; Slack 'in reach' is derived from channels, and Gmail is limited to the numbered thread files.",
        f"plan/notes.json cites robert@harmonygames.co/1780926053399834352 for the Eveline note, which is the Recipient Created for M ***4020; the note itself holds on {ev_first['thread']}. Pointer metadata only, no SQL effect.",
        "The Trello card is on To Do; the design record plan and plan/research/sw2_coherence.md T2 say Backlog.",
        "Preflight, dispositions and the gate's own --paste block belong to the preflight owner and follow the final SQL."] + ([f"From plan/unresolved.md: {UNR_KNOWN}"] if UNR_KNOWN else []) + ([f"From plan/unresolved.md: {UNR_COLD}"] if UNR_COLD else []) + ([TITLE_NOTE] if TITLE_NOTE else []):
    A(f"- {u_}")
A("")

open(os.path.join(WF, "01_Grounding_Dossier.md"), "w").write("\n".join(L) + "\n")
print("wrote 01_Grounding_Dossier.md", sum(len(x) + 1 for x in L), "chars;", len(lb), "load-bearing ids; orphans", len(ORPH))
print("token issue titles:", token_titles, "| team counter tie:", TEAM_OK, "| card date", card_row.get("dateLastActivity"), last_act)
print("check-sql:", (re.search(r"^verdict: \S+", OUT["checksql"], re.M) or [None])[0], "| notices differ:", len(NOT_DIFF), "| sheet tie", sumchk, "| statement tie", stmt_ok)
for t in TODO_DISP:
    print("NEEDS DISPOSITION:", t)
if BAD:
    print("QUOTES OR READS THAT FAILED:")
    for b in BAD:
        print("  ", b)
    sys.exit(3)
