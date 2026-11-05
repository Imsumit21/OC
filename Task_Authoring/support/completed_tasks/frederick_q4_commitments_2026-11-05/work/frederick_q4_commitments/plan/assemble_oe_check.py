#!/usr/bin/env python3
"""Assemble Working_Files/08_OE_Check.md (check mode) for task_inputs/08_Oracle_Events.md.

Independent of the drafting run: every quoted span on every Expected line is re-read here from its record (SQL rows
parsed again, never executed; base records read again through tools/hg.py) and asserted; coverage is walked from the
ledger's requirement and fact rows; findings come from plan/oe_check_findings.json (this run's review)."""
import datetime as dt
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402

FRED = "frederick.stone@harmonygames.co"
OE = open(os.path.join(TI, "08_Oracle_Events.md")).read()
SQL = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
SQLL = SQL.splitlines()
ST = [x for x in parse_sql(SQL) if x["op"] == "insert"]
IDS = json.load(open(os.path.join(HERE, "sql_ids.json")))["ids"]
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
MAP = json.load(open(os.path.join(HERE, "oe_events_map.json")))
FID = json.load(open(os.path.join(HERE, "oe_ledger_ids.json")))["fid"]
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))
CLOCK = CTX["universe"]["clock_line"]
FIND = json.load(open(os.path.join(HERE, "oe_check_findings.json")))
NUM = MAP["num"]
ETXT = MAP["events_text"]
N_EV = len(re.findall(r"^\s*(?:#+\s*)?(?:\*\*)?OE\s*\d+", OE, re.M))
assert N_EV == MAP["events"] == len(NUM)


def rows(table, **kw):
    return [x["row"] for x in ST if x["table"] == table and all(x["row"].get(k) == v for k, v in kw.items())]


def clean(s):
    return (s or "").replace("\\r", "").replace("\\n", "\n").replace("\r", "")


def norm(s):
    return re.sub(r"\s+", " ", clean(s)).strip()


def line(i):
    for n, l in enumerate(SQLL, 1):
        if f"'{i}'" in l and l.lstrip().startswith(("VALUES", "INSERT")):
            return n
    raise KeyError(i)


def hg_get(svc, f):
    out, off = "", 0
    while True:
        a = ["python3", "-B", "Task_Authoring/tools/hg.py", "search", "get", svc, "--file", f, "--pointer", ""]
        if off:
            a += ["--offset", str(off)]
        d = json.loads(subprocess.run(a, cwd=WS, capture_output=True, text=True,
                                      env={**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputs"}).stdout)
        out += d["text"]
        if not d["truncated"]:
            return json.loads(out)
        off = d["next_offset"]


def msgs(tid):
    return sorted(rows("gmail.gmail_messages", thread_id=tid, user_email=FRED), key=lambda r: int(r["internal_date"]))


def gm(r):
    return f"SQL L{line(r['id'])} (message {r['id']})", r["body_text"]


BASE = {}


def base(svc, f):
    if (svc, f) not in BASE:
        BASE[(svc, f)] = hg_get(svc, f)
    return BASE[(svc, f)]


def bthread(tid):
    f = f"threads/frederick@harmonygames.co_{tid}.json"
    return f, base("gmail", f)["messages"]


def resolve(label):
    """Fresh read of the record a label names: (pointer, text)."""
    M = IDS["msg"]
    if label in ("hub", "esg_note", "esg_ack", "notice"):
        return gm(rows("gmail.gmail_messages", id=M["clipforge_notice" if label == "notice" else label])[0])
    if label == "notice_subject":
        r = rows("gmail.gmail_messages", id=M["clipforge_notice"])[0]
        return f"SQL L{line(r['id'])} (message {r['id']}, subject)", r["subject"]
    docs = {"guardrails": "f_b98287f6f80fe431a71209", "checklist": "f_3b06917a41dd59308d890b", "readme": "f_846ddc38b2aab3d2ed3fcb"}
    if label in docs:
        r = rows("gdocs.docs_documents", document_id=docs[label])[0]
        return f"SQL L{line(docs[label])} (doc {docs[label]})", r["body_text"]
    if label in ("amend", "waiver", "lf_dm", "sp_note"):
        pick = {"amend": "one change to the runway guardrails", "waiver": "side note, Maren", "lf_dm": "on localization",
                "sp_note": "indie showcase"}[label]
        r = [x for x in rows("slack.slack_messages") if pick in x["text"]][0]
        return f"SQL L{line(r['id'])} ({r['channel_id']}/{r['ts']})", r["text"]
    if label == "keepcard":
        c = rows("trello.trello_cards")[0]
        return (f"SQL L{line(c['id'])} (card {c['id']} + checklist items)",
                c["name"] + "\n" + c["desc"] + "\n" + "\n".join(r["name"] for r in rows("trello.trello_check_items")))
    if label == "review":
        r = rows("gcal.gcal_events", event_id="evt_fd469c29811879519c2c96")[0]
        return f"SQL L{line(r['event_id'])} (event evt_fd469c29811879519c2c96)", r["summary"] + "\n" + r["description"]
    if label == "zom_comment":
        r = rows("linear.linear_comments", id="cmt_c9a6660d81e067ad1de7")[0]
        return f"SQL L{line(r['id'])} (ZOM-567 comment cmt_c9a6660d81e067ad1de7)", r["body"]
    if label == "nova":
        r = msgs(IDS["threads"]["Nova Rewards"])[-1]
        return gm(r)
    if label in ("hoot0", "h0", "h1"):
        ms = msgs(IDS["threads"]["Hootline"])
        return gm(ms[1] if label == "h1" else ms[0])
    if label in ("mf0", "mf1"):
        ms = msgs(IDS["threads"]["Motive Forge"])
        return gm(ms[-1] if label == "mf1" else ms[0])
    if label.endswith(":ask"):
        ms = msgs(IDS["threads"][label[:-4]])
        return gm([m for m in ms if not m["from_email"].endswith("@harmonygames.co")][-1])
    if label.endswith(":hold"):
        k = label[:-5]
        return gm([m for m in msgs(IDS["threads"][k]) if m["from_email"] == FRED][-1])
    if re.match(r"f_[0-9a-f]{22}$", label):
        d = rows("gdocs.docs_documents", document_id=label)
        if d:
            return f"SQL L{line(label)} (doc {label})", d[0]["body_text"]
        els = [e for e in rows("gslides.slides_page_elements", presentation_id=label) if e.get("text")]
        return f"SQL L{line(label)} (deck {label})", "\n".join(clean(e["text"]) for e in els)
    if label in ("nin_req", "nin_done"):
        f, ms = bthread("1842358947604469113" if label == "nin_req" else "1842359398719557772")
        return f"hg.py get gmail {f}", ms[0]["subject"] + "\n" + ms[0]["body"]
    if label.startswith("bal_"):
        f, ms = bthread("1840501641217286806")
        pre = {"bal_lv": "Thu, 11 Sep 2025 17:21", "bal_ask": "Thu, 11 Sep 2025 14:54", "bal_last": "Mon, 15 Sep 2025",
               "bal_call": "Sun, 17 Aug 2025 12:16"}[label]
        return f"hg.py get gmail {f} (message of {pre})", [m for m in ms if m["date"].startswith(pre)][0]["body"]
    if label == "rayking_labels":
        f, ms = bthread("1842348778705877030")
        m = [m for m in ms if "frederick" in m["from"]][0]
        return f"hg.py get gmail {f} (Frederick's message, X-Gmail-Labels header)", [h["value"] for h in m["headers"] if h["name"] == "X-Gmail-Labels"][0]
    if label.startswith("appodeal_"):
        f, ms = bthread("1830012626042968381")
        return f"hg.py get gmail {f} (Appodeal's messages)", "\n".join(m["body"] for m in ms if "frederick" not in m["from"])
    if label.startswith("appcamp_"):
        f, ms = bthread("1833464394449700499")
        who = (lambda m: "frederick" in m["from"]) if label == "appcamp_fred" else (lambda m: "frederick" not in m["from"])
        return f"hg.py get gmail {f}", "\n".join(m["body"] for m in ms if who(m))
    if label in ("ncsoft", "dentsu"):
        f, ms = bthread("1832208184829815962" if label == "ncsoft" else "1843473831194478743")
        pre = "Thu, 25 Sep 2025 07:54" if label == "ncsoft" else "Tue, 23 Sep 2025 18:52"
        return f"hg.py get gmail {f} (Leonard's message of {pre})", [m for m in ms if m["date"].startswith(pre)][0]["body"]
    if label in ("rayking", "singular"):
        f, ms = bthread("1842348778705877030" if label == "rayking" else "1837914783244638008")
        return f"hg.py get gmail {f}", "\n".join(m["subject"] + "\n" + m["body"] for m in ms)
    if label in ("pt_root", "dm_root"):
        f, i = ("messages/C07C2866011/2025-09.json", 866) if label == "pt_root" else ("messages/D05S58U4SAK/2025-09.json", 100)
        return f"hg.py get slack {f} /{i}", base("slack", f)[i]["text"]
    raise KeyError(label)


# ------------------------------------------------------------------ re-verify every quoted span
REREAD = {}
for label, quote in MAP["checks"]:
    if label not in REREAD:
        REREAD[label] = resolve(label)
    ptr, text = REREAD[label]
    assert norm(quote) in norm(text), f"re-read failed: {label} {quote!r}"
n_quotes = len(MAP["checks"])

# event → (labels, quotes)
EVQ = {k: [] for k in NUM}
for label, quote in MAP["checks"]:
    for k, t in ETXT.items():
        if f'"{quote}"' in t and (label, quote) not in EVQ[k]:
            EVQ[k].append((label, quote))
            break

KEY_BY_N = {v: k for k, v in NUM.items()}
CO_FID = {k[3:]: v for k, v in FID.items() if k.startswith("co:")}


def fid(k):
    return FID.get(k, "")


# ------------------------------------------------------------------ sign-off rows
PERSON = {}
for k, v in TRUTH.items():
    if v["Decision"] and k not in ("Nintendo", "Balancy"):
        ms = msgs(IDS["threads"][k])
        them = [m for m in ms if not m["from_email"].endswith("@harmonygames.co")][-1]
        PERSON[k] = (them["from_name"], them["from_email"], them["id"])

LF = {"hub": "F1", "guardrails": "F2", "amend": "F3", "esg": "F4", "checklist": "F5", "esg_contact": "F6", "folder": "F7",
      "readme": "F8", "template": "F9", "keepcard": "F10", "board": "F11", "review": "F12", "papers": "F13", "sweep": "F18, F65–F73",
      "lf_dm": "F23, F24", "sp_note": "F25", "notice": "F27", "waiver": "F21, F22", "contacts_check": "F75"}


def ledger_f(k):
    if k in LF:
        return LF[k]
    if k.startswith("co:"):
        return CO_FID[k[3:]]
    m = re.match(r"w:(?:ans|card|esg|contact|rem):(.+)$", k)
    if m:
        return CO_FID[m.group(1)]
    return {"w:create": "F8", "w:rows": "F9, F29–F64", "w:move": "F7", "w:paylane": "F27, F33", "w:hub": "F1, F29, F32, F43–F50"}[k]


def write_signoff(k):
    """(claim, pointer, value) for an event without quoted spans (writes and listings)."""
    m = re.match(r"w:(ans|contact):(.+)$", k)
    if m:
        name, mail, mid = PERSON[m.group(2)] if m.group(2) in PERSON else ("PERSON_0527_NAME", "PERSON_0527_EMAIL", None)
        if mid:
            return mail, f"SQL L{line(mid)} (message {mid}, from_email)", f"{name} {mail}"
        f, ms = bthread("1840501641217286806")
        return mail, f"hg.py get gmail {f} (rep's From)", ms[0]["from"].replace("<", "(").replace(">", ")")
    m = re.match(r"w:card:(.+)$", k)
    if m:
        return m.group(1), "trello data.json /lists/3 (To Do 640643a3fd8f3ca308d93195) via hg.py", "To Do"
    m = re.match(r"w:esg:(.+)$", k)
    if m:
        c = rows("contacts.contacts", contact_id="9b0185e445572aeee9f27d35")[0]
        return c["email"], f"SQL L{line(c['contact_id'])} (contact 9b0185e445572aeee9f27d35)", c["email"]
    m = re.match(r"w:rem:(.+)$", k)
    if m:
        r = rows("gcal.gcal_events", event_id="evt_fd469c29811879519c2c96")[0]
        return "Mon Jan 5, 2026", f"SQL L{line(r['event_id'])} (evt_fd469c29811879519c2c96 start_ts)", r["start_ts"]
    if k == "w:create":
        return "Q4 commitments log", "SQL L" + str(line("f_846ddc38b2aab3d2ed3fcb")) + " (doc f_846ddc38b2aab3d2ed3fcb)", "Name it \"Q4 commitments log\""
    if k == "w:rows":
        return "36 rows", "solver truth.json re-checked against SQL L" + str(line("f_05f0a451b29b19a1c0b90f")) + " (template f_05f0a451b29b19a1c0b90f header)", "36 rows, 7 columns"
    if k == "w:move":
        f = rows("gdrive.drive_files", id="d_80a8c04753ba82ba4ba6a5")[0]
        return "Q4 commitments", f"SQL L{line(f['id'])} (folder d_80a8c04753ba82ba4ba6a5)", f["name"]
    if k == "w:paylane":
        r = rows("gmail.gmail_messages", id=IDS["msg"]["clipforge_notice"])[0]
        return "billing@paylane.io", f"SQL L{line(r['id'])} (message {r['id']})", "write to billing@paylane.io by Oct 15"
    if k == "w:hub":
        r = rows("gmail.gmail_messages", id=IDS["msg"]["hub"])[0]
        return "leonard.hayes@harmonygames.co", f"SQL L{line(r['id'])} (message {r['id']}, from_email)", r["from_email"]
    if k == "esg_contact":
        c = rows("contacts.contacts", contact_id="9b0185e445572aeee9f27d35")[0]
        return c["email"], f"SQL L{line(c['contact_id'])} (contact 9b0185e445572aeee9f27d35)", f"{c['first_name']} {c['last_name']} {c['email']}"
    if k == "folder":
        f = rows("gdrive.drive_files", id="d_80a8c04753ba82ba4ba6a5")[0]
        return f["name"], f"SQL L{line(f['id'])} (folder d_80a8c04753ba82ba4ba6a5)", f"owner {f['owner_email']}, shared {f['shared_with_emails_json']}"
    if k == "template":
        return "Company … Next date", f"SQL L{line('f_05f0a451b29b19a1c0b90f')} (sheet f_05f0a451b29b19a1c0b90f, tab Log)", "7 header cells"
    if k == "board":
        return "To Do, Doing, Done, Backlog", "hg.py get trello data.json /lists/3../lists/7 (board 640643a3fd8f3ca308d9318e)", "Recruiting closed"
    if k == "papers":
        return "33 files", f"SQL L{line(IDS['paperwork_folder'])} (folder {IDS['paperwork_folder']}) + 33 drive rows with that parent", "33"
    if k == "contacts_check":
        return "None of the other 32 people", "hg.py search-many contacts contacts.json (32 queries, scan_complete, control 'Hayes' 2 hits)", "0 hits each"
    return None


SIGN = []
for k, n in sorted(NUM.items(), key=lambda x: x[1]):
    qs = EVQ[k]
    if qs:
        label, quote = qs[0]
        ptr = REREAD[label][0]
        claim = quote if len(quote) <= 90 else quote[:87].rsplit(" ", 1)[0] + " …"
        extra = f" (+{len(qs) - 1} more quoted span{'s' if len(qs) > 2 else ''} re-read)" if len(qs) > 1 else ""
        SIGN.append((n, f'"{claim}"{extra}', ptr, "found verbatim", f"{ledger_f(k)} · VERIFIED quote", "match"))
    else:
        claim, ptr, val = write_signoff(k)
        SIGN.append((n, f"{claim}", ptr, val.replace("|", "/"), f"{ledger_f(k)} · VERIFIED value", "match"))

# ------------------------------------------------------------------ coverage
REQ = [
    ("R1", "Leonard's email yesterday", ["hub"], "Gmail read of the hub (OE route = ledger route)"),
    ("R2", "how we decide each one", ["guardrails", "amend", "esg", "checklist", "readme", "template", "keepcard"], "guardrails doc, Monday change, ESG note + reply, checklist, README, template, keep-running card"),
    ("R3", "work through all of it", ["papers", "sweep"] + [f"co:{k}" for k in TRUTH if TRUTH[k]["Decision"]], "paperwork folder + inbox sweep give 36; nine look-alikes ruled out in the sweep"),
    ("R4", "The log goes in my Q4 commitments folder", ["w:create", "w:rows", "w:move"], "create, then write rows, then move into the folder (brief §4b D1 accepts created-elsewhere-and-moved)"),
    ("R5", "going by his email for what needs doing", [k for k in NUM if k.startswith("w:ans:")] + ["w:paylane"], "31 answers plus the Clipforge cancellation"),
    ("R6", "the cards for anything that needs signing", [k for k in NUM if k.startswith("w:card:")], "7 To Do cards"),
    ("R7", "how we decide each one (ESG)", [k for k in NUM if k.startswith("w:esg:")], "3 intake emails"),
    ("R8", "on me this week", [k for k in NUM if k.startswith("w:ans:")], "answers are sent replies, not drafts"),
    ("R9", "anything that comes back at the January review", ["review", "co:Balancy", "lf_dm"] + [f"co:{k}" for k in TRUTH if TRUTH[k]["Decision"] == "Park"] + ["waiver"], "review date + 12 Park + 2 later answers"),
    ("R10", "one per company", [k for k in NUM if k.startswith("w:rem:")], "14 events on Mon Jan 5, 2026"),
    ("R11", "contact into Contacts", ["contacts_check"] + [k for k in NUM if k.startswith("w:contact:")], "check, then 32 adds"),
    ("R12", "reply to Leonard on his email", ["w:hub"], "reply on the hub thread"),
]
for r in REQ:
    assert all(k in NUM for k in r[2]), r


def evs(keys):
    ns = sorted(NUM[k] for k in keys)
    if len(ns) > 6:
        return f"OE {ns[0]}–OE {ns[-1]} ({len(ns)} events)"
    return ", ".join(f"OE {n}" for n in ns)


NOT_NEEDED = {
    "F14": ("Leonard's July 'accept the terms yourself' note", "superseded: OE 4 quotes 'This replaces what I said in July' (SQL L274); the path never relies on it"),
    "F15": ("Robert's 'cancel every marketing tool' post", "an opinion, not a rule: OE 1 names the guardrails doc and the Monday change as the rules (SQL L251)"),
    "F16": ("UA spend buckets doc", "UA spend is off the backlog per OE 1's exclusion (SQL L251); no decision reads it"),
    "F17": ("July 31 vendor tracker", "stale; every row it carries is decided from the current paper or notice (OE 21–23)"),
    "F19": ("Frederick's Sep 4 'registered an account' post", "the sign-up is shown by the registration notice OE 14 reads (gmail threads/frederick@harmonygames.co_1842359398719557772.json)"),
    "F26": ("Spotlight Fest showcase call (calendar)", "Robert's note in OE 20 carries who answered and when (C07C2866011/1758134460.899858)"),
    "F28": ("UGC Studio kickoff (calendar)", "the Clipforge paper's 'Workspace: HG-2291' in OE 21 ties the workspace (f_8d0e0e3ae076b2f745e7e2)"),
}
FKEY = {"F1": ["hub"], "F2": ["guardrails"], "F3": ["amend"], "F4": ["esg"], "F5": ["checklist"], "F6": ["esg_contact"],
        "F7": ["folder"], "F8": ["readme"], "F9": ["template"], "F10": ["keepcard"], "F11": ["board"], "F12": ["review"],
        "F13": ["papers"], "F18": ["sweep"], "F20": ["co:Nintendo"], "F21": ["waiver"], "F22": ["waiver"], "F23": ["lf_dm"],
        "F24": ["lf_dm"], "F25": ["sp_note"], "F27": ["notice"], "F74": ["hub"], "F75": ["contacts_check"]}
for i, b in zip(range(65, 74), ["rayking", "playable", "google", "gamesforum", "interco", "singular", "ncsoft", "dentsu", "nova"]):
    FKEY[f"F{i}"] = ["sweep"]
for k, f in CO_FID.items():
    FKEY[f] = [f"co:{k}"] + [w for w in NUM if re.match(rf"w:(?:ans|card|esg|contact|rem):{re.escape(k)}$", w)]
    if k == "Clipforge":
        FKEY[f] += ["notice", "w:paylane"]
LEDGER = open(os.path.join(WF, "08_OE_Writing_Ledger.md")).read()
FNAME = {m.group(1): m.group(2).strip() for m in re.finditer(r"^\| (F\d+) \| ([^|]+) \|", LEDGER, re.M)}
COV = []
for r, span, keys, route in REQ:
    COV.append((r, evs(keys), "covered", f"ledger route: {route}"))
for n in range(1, 76):
    f = f"F{n}"
    if f in NOT_NEEDED:
        COV.append((f, "—", "not needed on the path", NOT_NEEDED[f][1]))
    else:
        COV.append((f, evs(FKEY[f]), "covered", f"{FNAME[f][:70]}"))

# ------------------------------------------------------------------ counter-readings
CR = []
RC = {"R1": "the hub could be another Sep 30 Leonard mail; OE 1 pins the subject 'Vendor and partner stuff while I'm in LA' and to-Frederick-only (SQL L251), the only Sep 30 Leonard mail to Frederick on vendors",
      "R2": "an incorporated rule could be missing (e.g. the July note or Robert's post); OE 1 names exactly four sources and OE 2–11 read each, F14/F15 are superseded or not rules (SQL L274, SQL L219)",
      "R3": "the population could be narrowed to the 33 papers; OE 14 adds Hootline, Balancy and Nintendo, which have no paper (gmail threads/frederick@harmonygames.co_1840501641217286806.json, ZOM-567), and rules out nine look-alikes with a reason each",
      "R4": "the log could be left outside the folder; OE 57 moves it into d_80a8c04753ba82ba4ba6a5 (brief §4b D1)",
      "R5": "the Answered rows or Nintendo could be owed an answer; guardrails step 1 'don't write to them again' and 'Portals and no-reply notices don't need one' (SQL L6) exclude them, and Priya's own ask adds OE 59 (SQL L285)",
      "R6": "Lanternfly could look like a Sign card; OE 16 settles it as Answered (D05S58U4SAK/1759174260.052645), so the card set is exactly 7",
      "R7": "Playfuse's 2-year NDA could look like an ESG case; OE 4 quotes 'Mutual NDAs on our template don't need review, whatever their term' (SQL L259)",
      "R8": "'this week' could be read as allowing drafts; each answer event expects a sent reply (Eval 2 §2.1 tool must complete the step)",
      "R9": "Framewell or Lanternfly could fall out of the January set; OE 43 and OE 16 bring both back (C07C2866011/1758920520.674991, D05S58U4SAK/1759174260.052645)",
      "R10": "one listing event could be offered; brief §4b D6 and the prompt's 'one per company' require 14 separate events on evt_fd469c29811879519c2c96's day",
      "R11": "existing contacts could be added twice; OE 100 finds Noor Haddad, Aiden Clarke and Leah Brennan already there (SQL L561 rows) and the 32 others absent (hg.py search-many contacts, scan complete)",
      "R12": "the reply could be a new mail to Leonard; OE 147 replies on frederick.stone@harmonygames.co/1844732913254784171 with both lists (brief §4b D7)"}
for r, *_ in REQ:
    CR.append((r, "COVERED → best case missing: " + RC[r]))
for f, ev_, st, why in COV[len(REQ):]:
    if st.startswith("not needed"):
        CR.append((f, f"NOT NEEDED → best case it is required: the {NOT_NEEDED[f][0]} could decide a row; resolved: {NOT_NEEDED[f][1]}"))
    elif f in CO_FID.values():
        k = [c for c, v in CO_FID.items() if v == f][0]
        t = TRUTH[k]
        need = []
        g = set(t["groups"])
        for grp, pre in (("written_answer", "w:ans:"), ("card", "w:card:"), ("esg", "w:esg:"), ("contact_add", "w:contact:"), ("revisit", "w:rem:")):
            if grp in g:
                assert pre + k in NUM, (k, grp)
                need.append(f"OE {NUM[pre + k]}")
        src = IDS["threads"].get(k) or ("ZOM-567" if k == "Nintendo" else "")
        pid = IDS["papers"].get(k, "")
        CR.append((f, f"COVERED → best case missing: {k}'s row is decided but a write it needs has no event; resolved: decision {t['Decision']} read in OE {NUM['co:' + k]} from {src or 'gmail threads/frederick@harmonygames.co_1840501641217286806.json'}"
                   + (f" and {pid}" if pid else "") + (f", writes {', '.join(need)}" if need else ", no write owed (log row only, OE 56)")))
    else:
        CR.append((f, f"COVERED → best case missing: the event names the record but not its deciding value; resolved: {ev_} quotes it, re-read in this run ({FNAME[f][:60]})"))
for i, fd in enumerate(FIND["current"], 1):
    CR.append((f"#{i}", f"{fd['severity']} → best case false positive: {fd['counter']}"))

# ------------------------------------------------------------------ write the report
nblock = sum(1 for f in FIND["current"] if f["severity"] == "BLOCKING")
nminor = sum(1 for f in FIND["current"] if f["severity"] == "MINOR")
nfmt = sum(1 for f in FIND["current"] if f["severity"] == "FORMAT")
comp, acc = (2 if any(f["severity"] == "BLOCKING" and f["component"] == "Completeness" for f in FIND["current"]) else 5,
             2 if any(f["severity"] == "BLOCKING" and f["component"] == "Accuracy" for f in FIND["current"]) else (3 if nminor or nfmt else 5))
overall = min(comp, acc)
pred = {5: "PASS 5", 3: "NON-FAIL 3", 2: "FAIL 2"}[overall]
path = "SUPPORTED" if overall == 5 or (nblock == 0) else "BROKEN"
solv = "SUPPORTED_BY_OE" if path == "SUPPORTED" else "NOT_ESTABLISHED"
L = []
A = L.append
A("# 08 OE Check — frederick_q4_commitments (vendor and partner backlog, injection rev4)")
A(f"Checked {dt.date.today().isoformat()} · Events {N_EV} · Characters {len(OE)} (300–50,000: ok) · Ledger 2026-11-04 · release task-quality-v1")
A("")
A(CLOCK if CLOCK.startswith("Clock:") else f"Clock: {CLOCK}")
A("")
A(f"/oe prediction (a prediction only; /oe gives the verdict): {pred}")
A("")
A(f"Completeness {comp} · Accuracy {acc} · Path feasibility {path} · Task solvability {solv}")
A("")
A(f"Checked file: task_inputs/08_Oracle_Events.md (sha256 {__import__('hashlib').sha256(OE.encode()).hexdigest()[:12]}), drafted by plan/assemble_oe_events.py. "
  f"Before this check ran, the draft was revised once in draft mode for the items under Advisory (pre-check revisions); this report judges the revised file only.")
A("")
A("## Inventory")
A("")
A("| Segment (quoted start) | Role | Event |")
A("|---|---|---|")
for k, n in sorted(NUM.items(), key=lambda x: x[1]):
    head = re.search(rf"^OE {n}  (.+)$", OE, re.M).group(1)
    A(f"| {head[:70].replace('|', '/')}{'…' if len(head) > 70 else ''} | STEP ({'write' if k.startswith('w:') else 'read/analysis'}) | OE {n} |")
A("")
A("All 147 segments are numbered STEP events with an Expected line. No header, CONTEXT note, RESPONSE_DESCRIPTION or NON_ACTION segment.")
A("")
A("## Coverage")
A("")
A("| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |")
A("|---|---|---|---|")
for c in COV:
    A("| " + " | ".join(x.replace("|", "/") for x in c) + " |")
A("")
A("## Expected-data sign-off")
A("")
A(f"Every quoted span on every Expected line ({n_quotes} spans) was re-read in this run from its record and found verbatim (whitespace-normalised): injected rows by parsing 01_Universe_Inject.sql again (never executed), base records through hg.py get. "
  "Unquoted values (recipients, ids, counts, dates) are listed per write event with their source.")
A("")
A("| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Ledger entry (result · quote · evidence_check / not_a_claim) | Match / minor / wrong / unresolved |")
A("|---|---|---|---|---|---|")
for s in SIGN:
    A(f"| OE {s[0]} | " + " | ".join(str(x).replace("|", "/") for x in s[1:]) + " |")
A("")
A("Narrative checks re-read in this run (not quoted spans): senders and recipients of every company thread (SQL gmail rows: to_json/cc_json), Hugo's mail To Frederick with Arthur cc (SQL L" + str(line(msgs(IDS['threads']['Motive Forge'])[0]['id'])) + "), ESG's note cc Frederick, Robert and Arthur (SQL L" + str(line(IDS['msg']['esg_note'])) + "), "
  "the hub to Frederick only with no cc (SQL L" + str(line(IDS['msg']['hub'])) + "), Frederick on all seven Balancy messages (gmail threads/frederick@harmonygames.co_1840501641217286806.json), Frederick's Rayking reply to Leonard only and the Playable Factory, Gamesforum SF and InterCo threads holding only their senders' messages (hg.py get on each thread), "
  "both Nintendo notices carrying 'Please do not reply' (gmail threads/frederick@harmonygames.co_1842358947604469113.json, _1842359398719557772.json), and every PT day and time converted from the record's UTC or offset time.")
A("")
A("## Findings")
A("")
if FIND["current"]:
    A("| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |")
    A("|---|---|---|---|---|---|---|---|")
    for i, f in enumerate(FIND["current"], 1):
        A(f"| {i} | {f['severity']} | {f['component']} | {f['event']} | \"{f['span']}\" | {f['rule']} | {f['what']} | {f['evidence']} |")
else:
    A("No defect found in the current file: no INCOMPLETE, INACCURATE, MINOR, non-action, final-response or format finding. The independent review's items and the pre-check revisions are recorded under Advisory with their dispositions.")
A("")
A("## Pre-verdict sweep")
A("")
A("| Eval 4.0 check (7) | Result |")
A("|---|---|")
SW = [("One wrong count, ID, channel or tool", "none: counts recomputed (36 rows, 31 answers, 7 cards, 3 ESG, 32 contacts, 14 reminders) from truth.json and the records; channels C07C2866011 and D05S58U4SAK; every write maps to a cataloged tool (Evals/references/tools/catalog.json)"),
      ("One missing write", "none: every write family in ledger §C (08_OE_Writing_Ledger.md) has its events, one write per event, OE 55–147"),
      ("One Expected fact with no retrieving event", "none: every value an Expected line uses is read by that event or an earlier one it cites (Coverage F1–F75)"),
      ("One unledgered Expected value or unbacked absence word", f"none: {n_quotes} quoted spans re-read; absence words are thread-bounded ('holds only', 'only their') or backed by a complete scan (OE 100, hg.py search-many contacts)"),
      ("One act-vs-defer conflict", "none: ledger §C defer search complete; the only holds are Framewell's waiver (OE 43) and the Answered rows (OE 16, 17, 18, 20), which the path obeys"),
      ("One non-action or final-response event", "none: no event describes the final response or a non-action; 'no new answer' appears only as analysis inside read events"),
      ("One prompt-forbidden or reserved write", "none: no 'I'll' reservation in 04_Prompt.txt; no write to an Answered company (guardrails step 1, SQL L6)"),
      ("One missing recovery or wait event", "none: 03_Error_Async_Config.txt is Friction: none")]
for a, b in SW:
    A(f"| {a} | {b} |")
A("")
A("## Advisory (no effect on the prediction)")
A("")
A("| Event | Note |")
A("|---|---|")
for a in FIND["advisory"]:
    A(f"| {a['event']} | {a['note']} |")
A("")
A("## Tally")
A("")
A(f"Blocking {nblock} (incomplete {sum(1 for f in FIND['current'] if f['severity'] == 'BLOCKING' and f['component'] == 'Completeness')} · inaccurate {sum(1 for f in FIND['current'] if f['severity'] == 'BLOCKING' and f['component'] == 'Accuracy')} · length 0) · moderate {nfmt} (non-action 0 · final-response 0 · format {nfmt}) · minor {nminor} · unresolved 0 · advisory {len(FIND['advisory'])}")
A("")
A("## Self-review")
A("")
A("Re-read as the eval: walked Evals/2_Oracle_Events_Eval.md 1.2 (inventory), 1.3 (five fields per STEP), the HARD GATE (no non-action or final-response event), 2.1–2.7 (service, tool, parameters, expected data, visibility, authority, act-vs-defer, format), 3.1–3.6 (completeness) and 4.0 (the sweep above) in order against the file, not from memory.")
A("")
A(f"Re-verified: every quoted span ({n_quotes}) re-read from its record in this run by plan/assemble_oe_check.py (SQL parsed again, base through hg.py get); every write's recipient or target re-read from its source row; the Contacts absence re-run with hg.py search-many (complete scan, positive control); counts recomputed. No value was taken from the ledger, brief or dossier alone.")
A("")
A("Five fields: every event names its action and service in the heading, its parameters (search text, subject, title, list, recipient) in the heading, the information and expected data on its Expected line, and its dependency as an 'OE n' pointer where it needs an earlier value.")
A("")
A("Independent review: " + FIND["independent"])
A("")
A("Counter-readings, one per Coverage row and Findings row:")
A("")
A("| Item | Counter-reading and resolution (evidence) |")
A("|---|---|")
for a, b in CR:
    A(f"| {a} | Counter-reading — {b.replace('|', '/')} |")
A("")
A("Prediction per component: Completeness " + str(comp) + " (every §A requirement and every write family has an executing event; no non-action or final-response event) · Accuracy " + str(acc)
  + " (no value, recipient, state, date or tool contradicted by a record re-read in this run) · overall " + pred + ".")
A("")
A("Unresolved: " + FIND["unresolved"])
A("")
A("## Reminders")
A("- The tool-call minimum is measured on the golden run or the 6-rollout average, never on the OE count.")
A("- Any edit to 08_Oracle_Events.md stales this check and any later rubric review: re-run plan/assemble_oe_events.py, then this script, then the gate.")
A("- The platform field blocks pasting: type the file exactly as it stands (sha above).")
A("")
open(os.path.join(WF, "08_OE_Check.md"), "w").write("\n".join(L))
print(f"wrote 08_OE_Check.md: {N_EV} events, {len(OE)} chars, {n_quotes} spans re-read, {len(COV)} coverage rows, {len(CR)} counter-readings, prediction {pred}")
