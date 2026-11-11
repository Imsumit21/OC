"""julia_zm_audience_read solver: the tools/oracle_kit.py contract (rev1 .. rev7).

Truth owner for the friend sessions (ZOM-568 onward, plus the late sessions a host reports inline in his form thread,
keys T1, T2, ...) and the two context values (panel, retention).
Parses the injection SQL as data through tools/base_check.parse_sql; never executes SQL. Every session field is read
from its seeded record (ticket header, ticket comment, notes Doc, or the host's form mail for late sessions) and every
rule reads its deciding record, so removing a record from the SQL text changes the truth. The one base input is the
warehouse table the retention rule names; it is read through tools/hg.py records (refresh with
`python3 solver.py --refresh-base`) and held in base_retention_rows.json so that repeated solves stay deterministic.

rev7 additions, all derived from the SQL (absent records leave the rev6 behaviour unchanged):
  R_K3  a real-device PASS row for a Samsung model in a QA matrix Sheet linked from Slack, under the gate Doc's
        "a pass covers a device only if it ran on that device ... covers all the Samsung sessions" clause, clears
        the Samsung group; Arthur's editor-only note keeps ZOM-567 / Vision Bot from being that pass.
        disable R_K3 = the matrix is not found -> Samsung excluded (device) with re-run notes.
  R_G   a player whose Contacts job says they work in games is not counted (Leonard's industry rule).
  R_T   sessions a host lists inline in a later reply in his form thread count (no doc, no ticket yet).
        disable R_T = the reply is not found -> verdict "absent".
  R_E   a later cohort cut-off on the retention figure (Linear comment) restricts the install-weighted D7.
        disable R_E = the cut-off is missed (when it exists), else the install-weighted rule is missed.
"""
import collections
import json
import pathlib
import re
import subprocess
import sys
import tempfile
from datetime import date, datetime, timedelta

KEY_REGEX = r"ZOM-(?:5(?:6[89]|[7-9]\d)|6[0-4]\d)|T\d+"
FIELDS = ["ticket", "observer", "session_date", "audience", "rating", "device", "build"]
CLASS_FIELD, GROUPS_FIELD = "verdict", "groups"
REVISIONS = ("rev1", "rev2", "rev7")
HERE = pathlib.Path(__file__).resolve().parent
BASE_ROWS = HERE / "base_retention_rows.json"


def _find_tools():
    for parent in HERE.parents:
        if (parent / "tools" / "base_check.py").is_file():
            return parent / "tools", parent.parent
        if (parent / "Task_Authoring" / "tools" / "base_check.py").is_file():
            return parent / "Task_Authoring" / "tools", parent
    fallback = pathlib.Path(r"C:\Users\shukl\Desktop\OC\Task_Authoring\tools")
    return fallback, fallback.parents[1]


TOOLS, ROOT = _find_tools()

JULIA = "julia.lawson@harmonygames.co"
GATE_DOC = "f_748d26e760e54651eaa0d8"
DECK = "f_a087f049d271e9aa9f567f"
KPI_SHEET = "f_4e21b203a62910bdae0353"
RC27 = "harmonygames-Games/match3d#476#rc_27"
ZOM567_LINE = "cmt_38b3cc50dceda37f40f5"
K1_MAIL = JULIA + "/<CA627c4f3eb036ebf28f00ed982586b0cba3e5@mail.gmail.com>"
PANEL_MAIL = JULIA + "/<CA9cfc392aa3b0ae856cc7f3b86c0d50e6f144@mail.gmail.com>"
K4_LINE = "246d6f4a90620e5dafbb06068f450e46"
R3_INDUSTRY = "e72083b249987542a134098010edd305"
K5_REPLY = "d7122186e361aa99778c65cb1502759d"
F_REPLY = "167dc58affb9902420038f71d0f5af28"
R4_PANEL = "7b38bd6429ce0f189456ac72af02f210"
R5_RETENTION = "2ca968ace3e14d1a34c535f8a5c0cd6e"
BUILDS_1943_TS = "1758575557.575349"
# rev7 deciding records (the solver still finds them from content; these ids name them for RULES / decoys)
QA_SHEET = "f_cadae9f611d82d56ac02c3"
QA_POST = "3dd0b6d6c52c21cd5bbfcd6d6f5345cd"
QA_REPLY = "3d8e451a198d5d59b39e60064b590305"
T_MAIL = JULIA + "/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com>"
E_CUTOFF = KPI_SHEET  # rev7: Vincent's Sep 30 note row on the KPI tab

RULES = {
    "R_K1": {"mechanism": "A13", "family": "A13", "requirement": "R1", "nodes": ["T-K1", "CH-K1"], "decides": ["verdict"],
             "natural_reading": "the form's no-coaching line stands, so the 13 sessions count",
             "source": "gmail:k1-host-mail", "signature": "Claire, Friday, before the group played",
             "authority": [K1_MAIL], "controls": ["ZOM-605", "ZOM-621", "ZOM-625"],
             "over_application": "over:K1_all_sessions_that_day"},
    "R_K3": {"mechanism": "A24", "family": "done_gap", "requirement": "R2", "nodes": ["T-K3", "CH-K3"], "decides": ["verdict", "rerun"],
             "natural_reading": "rev7: no on-device pass is found (ZOM-567 / Vision Bot is editor-only), so the Samsung "
                                "sessions are dropped with re-run notes; rev6: the Done ticket clears them",
             "source": "slack:zombie-bugs-matrix", "signature": "real device yes, SM-A546E, PASS, 2025-09-29",
             "authority": [GATE_DOC, QA_SHEET, QA_POST], "decoys": [ZOM567_LINE, RC27],
             "controls": ["ZOM-643", "ZOM-589", "ZOM-625"],
             "over_application": "over:K3_all_android"},
    "R_K4": {"mechanism": "A18", "family": "A18", "requirement": "R4", "nodes": ["T-K4", "CH-K4"], "decides": ["verdict"],
             "natural_reading": "Brian's clean label stands, so the 9 sessions count",
             "source": "slack:brian-dm", "signature": "the group works in games",
             "authority": [K4_LINE, R3_INDUSTRY], "controls": ["ZOM-626", "ZOM-627"],
             "over_application": "over:K4_any_group_nickname"},
    "R_K5": {"mechanism": "A17", "family": "A17", "requirement": "R3", "nodes": ["T-K5", "CH-K5"], "decides": ["verdict"],
             "natural_reading": "build id 1943 is treated as ordinary, so its sessions count",
             "source": "slack:k5-reply", "signature": "Android #1943 never went through a store",
             "authority": [K5_REPLY, GATE_DOC], "controls": ["ZOM-643", "ZOM-597", "ZOM-623"],
             "over_application": "over:K5_all_android"},
    "R_G": {"mechanism": "A13", "family": "A13", "requirement": "R4", "nodes": ["T-G"], "decides": ["verdict"],
            "natural_reading": "no doc or ticket names the player's work, so every non-Brian session counts",
            "source": "contacts:zm-playtest-players", "signature": "job: ... games studio / games publisher",
            "authority": [R3_INDUSTRY], "controls": ["ZOM-590", "ZOM-633"],
            "over_application": "over:G_any_tech_job"},
    "R_T": {"mechanism": "A17", "family": "A17", "requirement": "R1", "nodes": ["T-T"], "decides": ["verdict"],
            "natural_reading": "the read is the ticketed sessions only; the late inline sessions are missed",
            "source": "gmail:owen-late-reply", "signature": "Two more, sorry these are late ... Sun Sep 28",
            "authority": [T_MAIL]},
    "R_F": {"mechanism": "A14", "family": "A14", "requirement": "R8", "nodes": ["T-F"], "decides": ["rerun"],
            "natural_reading": "no re-run note, or a note on every not-counted ticket",
            "source": "slack:robert-dm", "signature": "technical drops get a re-run note",
            "authority": [F_REPLY], "controls": ["ZOM-568", "ZOM-569"],
            "over_application": "over:F_rerun_all_notcounted"},
    "R_D": {"mechanism": "A19", "family": "A19", "requirement": "R10", "nodes": ["T-PANEL"], "decides": ["panel_mean"],
            "natural_reading": "mean of all 10 ratings, 3.1",
            "source": "gmail:panel-forward", "signature": "void leaves sum and count", "authority": [PANEL_MAIL, R4_PANEL]},
    "R_E": {"mechanism": "A15", "family": "A15", "requirement": "R11", "nodes": ["T-RET"], "decides": ["retention_d7"],
            "natural_reading": "rev7: install-weighted over all mature cohorts (9.09), missing the 2025-07-24 cut-off; "
                               "rev6: simple cohort mean from the KPI tab",
            "source": "gsheets:kpi-snapshot-note", "signature": "cohort weeks starting on or after 2025-07-24",
            "authority": [R5_RETENTION, E_CUTOFF]},
}

DEGRADES = {
    "over:K1_all_sessions_that_day": "the coached reading spreads to every session dated the day of the gathering",
    "over:K3_all_android": "the device gate spreads from Samsung to every non-iPhone session",
    "over:K4_any_group_nickname": "the industry exclusion spreads to any one-observer batch that shares a relation",
    "over:K5_all_android": "the store-builds clause spreads from build 1943 to every Android build",
    "over:G_any_tech_job": "the industry exclusion spreads to any player with a QA / developer / producer style job",
    "over:F_rerun_all_notcounted": "a re-run note goes on all not-counted sessions, not only the technical drops",
    "slip:verdict": "a single row goes wrong while the verdicts are written",
}


def _session_keys():
    return [f"ZOM-{n}" for n in range(568, 648)] + ["T1", "T2"]


CHANNELS = {
    "scale:verdict": {"kind": "scale", "degrade": "slip:verdict", "members": _session_keys(), "latent": "member",
                      "family": "row association at scale (A2 slip)",
                      "description": "a single row goes wrong while 82 verdicts are written"},
    "tool_surface:state_writes": {"kind": "tool_surface", "degrade": None, "members": [], "slots": ["S-ST1", "S-ST2"],
                                  "latent": "run",
                                  "description": "a run stops partway through the state writes; the solver cannot express "
                                                 "a partial close-out, so surface slots carry it"},
    "delegation:handling": {"kind": "delegation", "degrade": None, "members": [], "slots": ["S-F1"], "latent": "run",
                            "description": "Robert's handling is lost when work is split or the owner is not followed"},
    "chain:decision": {"kind": "chain", "degrade": None, "members": [], "slots": ["S-DEC", "S-BRIAN"], "latent": "run",
                       "description": "the keep-or-hold mapping is misapplied after a right audience call"},
    "synthesis:context": {"kind": "synthesis", "degrade": None, "members": [], "slots": ["S-D1", "S-E1"], "latent": "run",
                          "description": "panel or retention context drops out of the memo"},
}

_ROUTES = {
    "ZOM-559": {"service": "linear", "file": "data.json", "pointer": "/issues", "field": "identifier"},
    BUILDS_1943_TS: {"service": "slack", "file": "messages/C05433XK267/2025-09.json", "pointer": "", "field": "ts"},
    "1758803475.436309": {"service": "slack", "file": "messages/C05433XK267/2025-09.json", "pointer": "", "field": "ts"},
    "1758517286.431379": {"service": "slack", "file": "messages/C090N54TG79/2025-09.json", "pointer": "", "field": "ts"},
    "f_89fadbc54660c9881d8cf9": {"service": "gdocs", "file": "data.json", "pointer": "/docs_documents", "field": "document_id"},
}


def base_route(record_id):
    return _ROUTES.get(str(record_id))


def _text(value):
    """SQL text as written: newlines stay as backslash escapes in the parsed row."""
    return str(value or "").replace("\\r\\n", "\n").replace("\\n", "\n")


def _base_retention():
    if BASE_ROWS.is_file():
        return json.loads(BASE_ROWS.read_text(encoding="utf8"))["rows"]
    return []


def refresh_base():
    """Read every Zombie Match 3D row of USER_COHORT_RETENTION through tools/hg.py records."""
    req = {"checks": [{"id": "ret", "service": "snowflake", "file": "snowflake.json", "pointer": "/tables/10/rows",
                       "field": "game_id", "values": ["zombie_match_3d"]}]}
    with tempfile.TemporaryDirectory() as tmp:
        path = pathlib.Path(tmp) / "req.json"
        path.write_text(json.dumps(req))
        run = subprocess.run([sys.executable, "-B", str(TOOLS / "hg.py"), "records", "--request", str(path)], cwd=ROOT,
                             capture_output=True, text=True, encoding="utf8")
    doc = json.loads(run.stdout)
    check = doc["checks"]["ret"]
    assert check.get("scan_complete") is True, "incomplete scan"
    rows = [m["record"] for m in check["matches"]]
    BASE_ROWS.write_text(json.dumps({"source": "snowflake.json /tables/10/rows (USER_COHORT_RETENTION), game_id zombie_match_3d",
                                     "read_through": "tools/hg.py records", "rows": rows}, indent=0) + "\n", encoding="utf8")
    return len(rows)


# ------------------------------------------------------------------ late inline sessions (R_T)

_LATE_LINE = re.compile(r"^(\d+)\. ([^,\n]+), (\d+), ([^.\n]+)\. Build ([^,\n]+), (casual|RPG), (\d(?:\.\d)?) stars?, "
                        r"played on an? ([^.\n]+)\.", re.M | re.I)


def _late_sessions(mail):
    """Sessions a host lists inline in a form-thread reply in Julia's mailbox: [(key, session, mail id)]."""
    out = []
    for mid in sorted(mail, key=lambda i: (mail[i].get("date") or "", i)):
        m = mail[mid]
        if m.get("user_email") != JULIA or "friend sessions form" not in str(m.get("subject", "")).lower():
            continue
        body = _text(m.get("body_text"))
        lines = _LATE_LINE.findall(body)
        head = re.search(r"Host: ([^.\n]+)\. Day: \w+ (\w{3}) (\d{1,2})\.", body)
        if not lines or not head:
            continue
        year = int(str(m["date"])[:4])
        day = datetime.strptime(f"{head.group(2)} {head.group(3)} {year}", "%b %d %Y").date().isoformat()
        coached = not re.search(r"\bno coaching\b", body, re.I)
        for n, player, age, relation, build, audience, stars, device in lines:
            out.append({"ticket": None, "observer": head.group(1).strip(), "session_date": day, "audience": audience,
                        "rating": _stars(stars), "device": device.strip(), "build": build.strip(), "age": int(age),
                        "relation": relation.strip(), "player": player.strip(), "doc": None, "comment": None,
                        "mail": mid, "late": True, "coached_form": coached})
    for i, s in enumerate(out, 1):
        s["key"] = f"T{i}"
    return out


def load_state(sql_text, revision=None):
    try:
        from base_check import parse_sql
    except ImportError:
        if str(TOOLS) not in sys.path:
            sys.path.insert(0, str(TOOLS))
        from base_check import parse_sql
    tables = collections.defaultdict(list)
    for x in parse_sql(sql_text):
        if x["op"] == "insert":
            tables[x["table"]].append(x["row"])
    issues = {r["id"]: r for r in tables["linear.linear_issues"] if str(r.get("title", "")).startswith("Friend session:")}
    comments = collections.defaultdict(list)
    for r in tables["linear.linear_comments"]:
        comments[r["issue_id"]].append(r)
    docs = {r["document_id"]: r for r in tables["gdocs.docs_documents"]}
    docs_by_title = {r["title"]: r for r in tables["gdocs.docs_documents"]}
    slack = {r["id"]: r for r in tables["slack.slack_messages"]}
    mail = {r["id"]: r for r in tables["gmail.gmail_messages"]}
    reviews = {r["id"]: r for r in tables["github.github_review_comments"]}
    contacts = {}
    for r in tables["contacts.contacts"]:
        name = f"{str(r.get('first_name') or '').strip()} {str(r.get('last_name') or '').strip()}".strip()
        contacts.setdefault(name, r)
    sessions = {}
    for key in sorted(issues):
        head = _text(issues[key]["description"])
        field = lambda name, text=head: (re.search(rf"^{name}: (.+)$", text, re.M) or [None, None])[1]
        title = field("Notes doc")
        doc = docs_by_title.get(title)
        body = _text(doc["body_text"]) if doc else ""
        dfield = lambda name, text=body: (re.search(rf"^{name}: (.+)$", text, re.M) or [None, None])[1]
        note = next(iter(comments.get(key) or []), None)
        sessions[key] = {
            "ticket": key, "observer": field("Observer"), "session_date": field("Session date"),
            "audience": dfield("Audience") or field("Audience"),
            "rating": _stars(dfield("Stars") or field("Stars")),
            "device": _device(note["body"]) if note else None, "build": dfield("Build"),
            "age": int(dfield("Age")) if dfield("Age") else None, "relation": dfield("Relation"),
            "player": (dfield("Player") or "").strip() or None,
            "doc": doc["document_id"] if doc else None, "comment": note["id"] if note else None}
    for s in _late_sessions(mail):
        sessions[s.pop("key")] = s
    sheets = {(r["spreadsheet_id"], r["title"]): json.loads(r["grid_json"]) for r in tables["gsheets.sheets_sheets"]}
    return {"revision": revision or REVISIONS[-1], "sessions": sessions, "docs": docs, "slack": slack, "mail": mail,
            "reviews": reviews, "sheets": sheets, "comments": {r["id"]: r for r in tables["linear.linear_comments"]},
            "contacts": contacts, "base_retention": _base_retention()}


def _stars(value):
    """A star value as the records write it: 5, 3.5."""
    number = float(value)
    return int(number) if number == int(number) else number


def _device(body):
    """The phone named in a ticket comment, whatever the lead-in ("on a", "played on an", "phone: ")."""
    text = str(body).strip()
    return re.sub(r"^(?:device for this one: |phone: |phone was an? |played on an? |on an? )", "", text)


def _on(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def _session_order(state):
    """Ticketed sessions first (sorted), then late inline sessions in mail order."""
    ss = state["sessions"]
    return sorted(k for k in ss if not ss[k].get("late")) + [k for k in ss if ss[k].get("late")]


# ------------------------------------------------------------------ rule readings from the deciding records

def _k1_scope(st):
    """(host, day) from Claire's later mail: the host is its sender, the day the Friday before it."""
    m = st["mail"].get(K1_MAIL)
    body = " ".join(_text(m["body_text"]).split()).lower() if m else ""
    if "before anyone touched their phone" not in body or "friday at my place" not in body:
        return None
    d = date.fromisoformat(m["date"][:10])
    while d.weekday() != 4:
        d -= timedelta(days=1)
    return m["from_name"], d.isoformat()


def _gate_text(st):
    doc = st["docs"].get(GATE_DOC)
    return " ".join(_text(doc["body_text"]).split()) if doc else ""


def _samsung(st, device):
    """The gate Doc's one device group, read from its own family and model-number lists."""
    if not device:
        return False
    text = _gate_text(st)
    i = text.find("Samsung is the one device group")
    if i < 0:
        return False
    sentence = re.split(r"(?:Every|Other) (?:other )?(?:group|phones)", text[i:i + 400])[0]
    prefixes = re.findall(r"\bSM-[A-Z]\b", sentence)
    fam = re.search(r"Galaxy ([A-Z](?:\s*(?:,|and)\s*(?:Galaxy\s+)?[A-Z])*)\b", sentence)
    if fam:
        prefixes += ["Galaxy " + x for x in re.findall(r"\b([A-Z])\b", fam.group(1))]
    return any(device.startswith(p) for p in prefixes)


def _pass_on_device(st):
    """Vision Bot (ZOM-567) as the pass: holds unless the job owner's note says it ran with no phone."""
    note = st["reviews"].get(RC27)
    return not (note and "no phone in the loop" in str(note["body"]))


def _device_pass(st):
    """A real-device clean run on a Samsung model, in a QA matrix Sheet a Slack post links, under the gate Doc's
    'pass covers a device only if it ran on that device' clause: (sheet id, [record ids]) or None."""
    text = _gate_text(st)
    if "A pass covers a device only if it ran on that device" not in text or "covers all the Samsung sessions" not in text:
        return None
    dev_builds = _k5_builds(st)
    for (sid, _title), grid in sorted(st["sheets"].items()):
        if not grid:
            continue
        head = [str(c).strip().lower() for c in grid[0]]
        col = lambda *names: next((i for i, h in enumerate(head) if any(n in h for n in names)), None)
        c_model, c_real, c_result, c_build = col("model"), col("real device"), col("result"), col("build")
        if None in (c_model, c_real, c_result):
            continue
        hit = False
        for row in grid[1:]:
            cell = lambda i: str(row[i]).strip() if i is not None and i < len(row) else ""
            build_id = (re.search(r"\((\d+)\)", cell(c_build)) or [None, None])[1]
            if (_samsung(st, cell(c_model)) and cell(c_real).lower().startswith("yes")
                    and cell(c_result).upper() == "PASS" and build_id not in dev_builds):
                hit = True
                break
        if not hit:
            continue
        links = sorted(mid for mid, m in st["slack"].items() if f"spreadsheets/d/{sid}" in str(m.get("text", "")))
        if not links:
            continue
        posts = set(links) | {st["slack"][m]["thread_parent_id"] for m in links if st["slack"][m].get("thread_parent_id")}
        return sid, [sid] + sorted(posts)
    return None


def _k3_excludes(st, key, disable):
    """True when the device gate drops this Samsung session."""
    found = _device_pass(st)
    if found:                                   # rev7: the matrix clears the group; missing it drops the group
        return _on(disable, "R_K3", key)
    return not _on(disable, "R_K3", key) and not _pass_on_device(st)


def _k4_groups(st):
    """Relation values the DM line says work in games, once the industry rule exists."""
    line, rule = st["slack"].get(K4_LINE), st["slack"].get(R3_INDUSTRY)
    if not line or not rule or "game-industry people don" not in str(rule["text"]):
        return set()
    text = str(line["text"])
    if "oyun sektör" not in text:
        return set()
    return {s["relation"] for s in st["sessions"].values() if s["relation"] and s["relation"] in text}


_GAMES_JOB = re.compile(r"\bgames?\b", re.I)


def _industry_contact(st, key):
    """The player's Contacts row when its job says they work in games and Leonard's industry rule exists."""
    rule = st["slack"].get(R3_INDUSTRY)
    if not rule or "game-industry people don" not in str(rule["text"]) or "works in games" not in str(rule["text"]):
        return None
    player = st["sessions"][key].get("player")
    contact = st["contacts"].get(player) if player else None
    if contact and _GAMES_JOB.search(str(contact.get("job") or "")):
        return contact
    return None


def _k5_builds(st):
    """Build ids the reply says never went through a store, once the gate Doc's store clause exists."""
    reply, doc = st["slack"].get(K5_REPLY), st["docs"].get(GATE_DOC)
    if not reply or not doc or "anything that never went through a store" not in _text(doc["body_text"]):
        return set()
    if "never went through a store" not in str(reply["text"]):
        return set()
    return set(re.findall(r"android (\d{4})", str(reply["text"])))


def _handling(st):
    """The reasons Robert's reply gives a re-run note."""
    reply = st["slack"].get(F_REPLY)
    return {"device", "build"} if reply and "technical reason, device or build" in str(reply["text"]) else set()


def _batch_shares_relation(st, key):
    s = st["sessions"][key]
    batch = [x for x in st["sessions"].values() if x["observer"] == s["observer"] and x["session_date"] == s["session_date"]]
    return len(batch) >= 2 and len({x["relation"] for x in batch}) == 1


def _reason(st, key, disable):
    """The exclusion the rules give a session, or None; (reason, rule)."""
    s = st["sessions"][key]
    k1 = _k1_scope(st)
    if not _on(disable, "R_K1", key) and k1 and (s["observer"], s["session_date"]) == k1:
        return "coached", "R_K1"
    if _samsung(st, s["device"]) and _k3_excludes(st, key, disable):
        return "device", "R_K3"
    if not _on(disable, "R_K4", key) and s["relation"] in _k4_groups(st):
        return "game_industry", "R_K4"
    if not _on(disable, "R_G", key) and _industry_contact(st, key):
        return "game_industry", "R_G"
    build_id = (re.search(r"\((\d+)\)", s["build"] or "") or [None, None])[1]
    if not _on(disable, "R_K5", key) and build_id in _k5_builds(st):
        return "build", "R_K5"
    return None, None


_TECH_JOB = re.compile(r"\b(?:qa|developer|engineer|producer|designer|tester)\b", re.I)


def _session_row(st, key, disable, degrade):
    s = st["sessions"][key]
    late = bool(s.get("late"))
    reason, rule = _reason(st, key, disable)
    truth_reason = _reason(st, key, frozenset())[0]
    # over-application reaches only the rule's controls: sessions the truth counts, whatever other mistakes a run makes
    if truth_reason is None:
        k1 = _k1_scope(st)
        android = not str(s["device"]).startswith("iPhone")
        contact = st["contacts"].get(s.get("player")) if s.get("player") else None
        if k1 and _on(degrade, "over:K1_all_sessions_that_day", key) and s["session_date"] == k1[1]:
            reason = "coached"
        elif _on(degrade, "over:K3_all_android", key) and android:
            reason = "device"
        elif _on(degrade, "over:K4_any_group_nickname", key) and _batch_shares_relation(st, key):
            reason = "game_industry"
        elif _on(degrade, "over:G_any_tech_job", key) and contact and _TECH_JOB.search(str(contact.get("job") or "")):
            reason = "game_industry"
        elif _on(degrade, "over:K5_all_android", key) and android:
            reason = "build"
    verdict = "notcounted" if reason else "counted"
    if _on(degrade, "slip:verdict", key):
        verdict = "counted" if reason else "notcounted"
        reason = None if reason else "slip"
    rerun = reason in _handling(st) and not (truth_reason in _handling(st) and _on(disable, "R_F", key))
    if _on(degrade, "over:F_rerun_all_notcounted", key) and truth_reason not in (None, *_handling(st)) and verdict == "notcounted":
        rerun = True
    if late and _on(disable, "R_T", key):          # the late reply is never found: no row, no ticket
        verdict, reason, rerun = "absent", None, False
    if rule:
        basis = list(RULES[rule]["authority"])
        if rule == "R_G":
            basis = [_industry_contact(st, key)["contact_id"], R3_INDUSTRY]
        elif rule == "R_K3":                       # dropped: the gate Doc plus the editor-only note on the decoy
            basis = [GATE_DOC, RC27] + ([ZOM567_LINE] if _device_pass(st) else [])
    elif _samsung(st, s["device"]) and _device_pass(st):
        basis = [GATE_DOC] + _device_pass(st)[1]
    else:
        basis = [s["mail"]] if late else [key]
    row = {"ticket": s["ticket"], "observer": s["observer"], "session_date": s["session_date"], "audience": s["audience"],
           "rating": s["rating"], "device": s["device"], "build": s["build"], "age": s["age"], "relation": s["relation"]}
    if s.get("player"):
        contact = st["contacts"].get(s["player"])
        row["player"] = s["player"]
        row["job"] = contact.get("job") if contact else None
    row.update({"verdict": verdict, "reason": reason, "rerun": rerun, "groups": [reason] if reason else []})
    if late:
        row["needs_ticket"] = verdict != "absent"
        row["evidence"] = {"ticket": s["mail"], "doc": s["mail"], "comment": s["mail"], "verdict": basis}
    else:
        row["evidence"] = {"ticket": key, "doc": s["doc"], "comment": s["comment"], "verdict": basis}
        if row.get("job") is not None:
            row["evidence"]["job"] = [st["contacts"][s["player"]]["contact_id"]]
    return row


def _panel_row(st, disable):
    m = st["mail"].get(PANEL_MAIL)
    ratings, void = {}, set()
    if m:
        text = _text(m["body_text"])
        ratings = {int(n): float(v) for n, v in re.findall(r"player (\d+) (\d(?:\.\d)?)", text)}
        void = {int(n) for n in re.findall(r"Player (\d+)'s rating is void", text)}
    rule = st["slack"].get(R4_PANEL)
    honours = bool(rule) and "comes out of both the sum and the count" in str(rule["text"]) and not _on(disable, "R_D", "panel")
    kept = [v for n, v in sorted(ratings.items()) if not (honours and n in void)]
    return {"item": "panel", "panel_mean": round(sum(kept) / len(kept), 2) if kept else None, "panel_n": len(kept),
            "panel_void": sorted(void), "groups": [], "evidence": {"panel_mean": [PANEL_MAIL, R4_PANEL]}}


def _retention_cutoff(st):
    """(cohort-week cut-off, record id) from Vincent's later note on the KPI tab that restricts quoted ZM retention, or None."""
    for r in st["sheets"].get((KPI_SHEET, "KPI")) or []:
        body = " ".join(_text(" ".join(str(c) for c in r)).split())
        m = re.search(r"cohort weeks starting on or after (\d{4}-\d{2}-\d{2})", body)
        if m and "ZM retention" in body:
            return m.group(1), KPI_SHEET
    return None


def _retention_row(st, disable):
    rule = st["slack"].get(R5_RETENTION)
    grid = st["sheets"].get((KPI_SHEET, "KPI")) or []
    kpi = next((float(r[-1]) for r in grid if r and r[0] == "D7 mean"), None)
    cut = _retention_cutoff(st)
    weighted = bool(rule) and "install-weighted D7" in str(rule["text"])
    if cut:                                         # rev7: disabling R_E misses the cut-off, not the weighting
        use_cut, use_weight = not _on(disable, "R_E", "retention"), weighted
    else:
        use_cut, use_weight = False, weighted and not _on(disable, "R_E", "retention")
    if use_weight:
        mature = [r for r in st["base_retention"] if r.get("d14_ret") is not None and r.get("d7_ret") is not None]
        if use_cut:
            mature = [r for r in mature if str(r["cohort_week"]) >= cut[0]]
        installs = sum(r["installs"] for r in mature)
        value = round(sum(r["d7_ret"] * r["installs"] for r in mature) / installs, 2) if installs else None
        row = {"item": "retention", "retention_d7": value, "retention_rows": len(mature), "retention_method": "install-weighted",
               "groups": [], "evidence": {"retention_d7": [R5_RETENTION] + ([cut[1]] if use_cut else [])}}
        if cut:
            row["retention_cutoff"] = cut[0] if use_cut else None
            row["retention_installs"] = installs
        return row
    return {"item": "retention", "retention_d7": kpi, "retention_rows": sum(1 for r in grid if r and re.match(r"\d{4}-\d{2}-\d{2}$", str(r[0]))),
            "retention_method": "kpi simple mean", "groups": [], "evidence": {"retention_d7": [KPI_SHEET]}}


def _late_placeholders(state):
    """Players in Julia's contacts with no ticketed or late session: the late sessions whose reply is missing from
    the record set (an intervention that drops Owen's mail). They stay keys, with verdict "absent"."""
    ss = state["sessions"]
    if any(s.get("late") for s in ss.values()) or not state.get("contacts"):
        return []
    players = {s.get("player") for s in ss.values()}
    extra = [n for n in state["contacts"] if n not in players]
    return [f"T{i}" for i in range(1, len(extra) + 1)]


def keys(state):
    return _session_order(state) + _late_placeholders(state) + ["panel", "retention"]


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    out = {}
    for k in (keys_ if keys_ is not None else keys(state)):
        if k == "panel":
            out[k] = _panel_row(state, disable)
        elif k == "retention":
            out[k] = _retention_row(state, disable)
        elif k not in state["sessions"] and re.fullmatch(r"T\d+", k):
            out[k] = {"ticket": None, "verdict": "absent", "reason": None, "rerun": False, "groups": [],
                      "evidence": {}}
        else:
            out[k] = _session_row(state, k, disable, degrade)
    return out


def aggregates(rows):
    """The totals every artifact reads: counted set, means, gap, the lead read and the keep-or-hold mapping."""
    sess = {k: v for k, v in rows.items() if re.fullmatch(KEY_REGEX, k)}
    counted = [v for v in sess.values() if v["verdict"] == "counted"]
    by = {a: [v["rating"] for v in counted if str(v["audience"]).lower() == a] for a in ("casual", "rpg")}
    means = {a: round(sum(x) / len(x), 3) if x else None for a, x in by.items()}
    lead, gap = "no clear lead", None
    if by["casual"] and by["rpg"]:
        raw = sum(by["casual"]) / len(by["casual"]) - sum(by["rpg"]) / len(by["rpg"])
        gap = round(abs(raw), 3)
        if min(len(by["casual"]), len(by["rpg"])) >= 6 and abs(raw) >= 0.25:
            lead = "casual" if raw > 0 else "rpg"
    groups = collections.defaultdict(list)
    for k, v in sess.items():
        for g in v.get("groups") or []:
            groups[g].append(k)
    return {"classes": dict(collections.Counter(v["verdict"] for v in sess.values())), "groups": dict(groups),
            "counts": {a: len(x) for a, x in by.items()}, "means": means, "gap": gap, "lead": lead,
            "decision": "hold" if lead == "casual" else "keep", "rerun": sorted(k for k, v in sess.items() if v["rerun"]),
            "new_tickets": sorted(k for k, v in sess.items() if v.get("needs_ticket"))}


def evidence(rows, key, field):
    ev = rows[key].get("evidence") or {}
    if field in ("ticket", "observer", "session_date"):
        return [ev["ticket"]]
    if field == "device":
        return [ev["comment"]] if ev.get("comment") else []
    if field == "build" and "1943" in str(rows[key].get("build")):
        return [ev["doc"], BUILDS_1943_TS]
    if field in ("audience", "rating", "build", "age", "relation", "player"):
        return [ev["doc"]] if ev.get("doc") else []
    return list(ev.get(field) or [])


def touched(state, rule):
    if rule == "R_D":
        return {"panel"}
    if rule == "R_E":
        return {"retention"}
    truth = solve(state)
    off = solve(state, disable=frozenset({rule}))
    return {k for k in truth if {f: v for f, v in truth[k].items() if f != "evidence"}
            != {f: v for f, v in off[k].items() if f != "evidence"}}


def _deciding_ids(state, rule, key):
    if rule == "R_K3":
        found = _device_pass(state)
        return [GATE_DOC] + found[1] if found else [RC27]
    if rule == "R_G":
        c = _industry_contact(state, key) if key in state["sessions"] else None
        return [c["contact_id"], R3_INDUSTRY] if c else [R3_INDUSTRY]
    if rule == "R_T":
        s = state["sessions"].get(key) or {}
        return [s["mail"]] if s.get("mail") else [T_MAIL]
    if rule == "R_E":
        cut = _retention_cutoff(state)
        return [R5_RETENTION, cut[1]] if cut else [R5_RETENTION]
    return list({"R_K1": [K1_MAIL], "R_K4": [K4_LINE, R3_INDUSTRY], "R_K5": [K5_REPLY], "R_F": [F_REPLY],
                 "R_D": [PANEL_MAIL]}[rule])


def deciding(state, rule, key):
    return _deciding_ids(state, rule, key) if key in touched(state, rule) else []


if __name__ == "__main__":
    if "--refresh-base" in sys.argv:
        print("rows", refresh_base())
