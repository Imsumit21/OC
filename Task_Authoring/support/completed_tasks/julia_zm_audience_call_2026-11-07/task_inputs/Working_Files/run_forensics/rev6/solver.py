"""julia_zm_audience_read solver: the tools/oracle_kit.py contract for rev1.

Truth owner for the 60 friend sessions (ZOM-568 to ZOM-627) plus the two context values (panel, retention).
Parses the injection SQL as data through tools/base_check.parse_sql; never executes SQL. Every session field is read
from its seeded record (ticket header, ticket comment, notes Doc) and every rule reads its deciding record, so
removing a record from the SQL text changes the truth. The one base input is the warehouse table the retention rule
names; it is read through tools/hg.py records (refresh with `python3 solver.py --refresh-base`) and held in
base_retention_rows.json so that repeated solves stay deterministic and fast.
"""
import collections
import json
import pathlib
import re
import subprocess
import sys
import tempfile
from datetime import date, timedelta

KEY_REGEX = r"ZOM-(?:5(?:6[89]|[7-9]\d)|6[01]\d|62[0-7])"
FIELDS = ["ticket", "observer", "session_date", "audience", "rating", "device", "build"]
CLASS_FIELD, GROUPS_FIELD = "verdict", "groups"
REVISIONS = ("rev1", "rev2")
HERE = pathlib.Path(__file__).resolve().parent
BASE_ROWS = HERE / "base_retention_rows.json"
TOOLS = HERE.parents[2] / "tools"
ROOT = HERE.parents[3]

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

RULES = {
    "R_K1": {"mechanism": "A13", "family": "A13", "requirement": "R1", "nodes": ["T-K1", "CH-K1"], "decides": ["verdict"],
             "natural_reading": "the form's no-coaching line stands, so the 13 sessions count",
             "source": "gmail:k1-host-mail", "signature": "Claire, Friday, before the group played",
             "authority": [K1_MAIL], "controls": ["ZOM-605", "ZOM-621", "ZOM-625"],
             "over_application": "over:K1_all_sessions_that_day"},
    "R_K3": {"mechanism": "A24", "family": "done_gap", "requirement": "R2", "nodes": ["T-K3", "CH-K3"], "decides": ["verdict"],
             "natural_reading": "the Done ticket and owner's line clear the device group, so the 11 sessions count",
             "source": "github:476-rc27", "signature": "editor play mode, no phone, inline note on the PR",
             "authority": [GATE_DOC, RC27], "controls": ["ZOM-598", "ZOM-589", "ZOM-625"],
             "over_application": "over:K3_all_android"},
    "R_K4": {"mechanism": "A18", "family": "A18", "requirement": "R4", "nodes": ["T-K4", "CH-K4"], "decides": ["verdict"],
             "natural_reading": "Brian's clean label stands, so the 9 sessions count",
             "source": "slack:brian-dm", "signature": "the group works in games",
             "authority": [K4_LINE, R3_INDUSTRY], "controls": ["ZOM-626", "ZOM-627"],
             "over_application": "over:K4_any_group_nickname"},
    "R_K5": {"mechanism": "A17", "family": "A17", "requirement": "R3", "nodes": ["T-K5", "CH-K5"], "decides": ["verdict"],
             "natural_reading": "build id 1943 is treated as ordinary, so the 10 sessions count",
             "source": "slack:k5-reply", "signature": "Android #1943 never went through a store",
             "authority": [K5_REPLY, GATE_DOC], "controls": ["ZOM-598", "ZOM-597", "ZOM-623"],
             "over_application": "over:K5_all_android"},
    "R_F": {"mechanism": "A14", "family": "A14", "requirement": "R8", "nodes": ["T-F"], "decides": ["rerun"],
            "natural_reading": "no re-run note, or a note on all 43 not-counted tickets",
            "source": "slack:robert-dm", "signature": "technical drops get a re-run note",
            "authority": [F_REPLY], "controls": ["ZOM-568", "ZOM-569"],
            "over_application": "over:F_rerun_all_notcounted"},
    "R_D": {"mechanism": "A19", "family": "A19", "requirement": "R10", "nodes": ["T-PANEL"], "decides": ["panel_mean"],
            "natural_reading": "mean of all 10 ratings, 3.1",
            "source": "gmail:panel-forward", "signature": "void leaves sum and count", "authority": [PANEL_MAIL, R4_PANEL]},
    "R_E": {"mechanism": "A15", "family": "A15", "requirement": "R11", "nodes": ["T-RET"], "decides": ["retention_d7"],
            "natural_reading": "simple cohort mean from the KPI tab",
            "source": "slack:retention-reply", "signature": "install-weighted, mature cohorts", "authority": [R5_RETENTION]},
}

DEGRADES = {
    "over:K1_all_sessions_that_day": "the coached reading spreads to every session dated the day of the gathering",
    "over:K3_all_android": "the device gate spreads from Samsung to every non-iPhone session",
    "over:K4_any_group_nickname": "the industry exclusion spreads to any one-observer batch that shares a relation",
    "over:K5_all_android": "the store-builds clause spreads from build 1943 to every Android build",
    "over:F_rerun_all_notcounted": "a re-run note goes on all not-counted sessions, not only the technical drops",
    "slip:verdict": "a single row goes wrong while 60 verdicts are written",
}


def _session_keys():
    return [f"ZOM-{n}" for n in range(568, 628)]


CHANNELS = {
    "scale:verdict": {"kind": "scale", "degrade": "slip:verdict", "members": _session_keys(), "latent": "member",
                      "family": "row association at scale (A2 slip)",
                      "description": "a single row goes wrong while 60 verdicts are written"},
    "tool_surface:state_writes": {"kind": "tool_surface", "degrade": None, "members": [], "slots": ["S-ST1", "S-ST2"],
                                  "latent": "run",
                                  "description": "a run stops partway through 60 state writes; the solver cannot express "
                                                 "a partial close-out, so surface slots carry it"},
    "delegation:handling": {"kind": "delegation", "degrade": None, "members": [], "slots": ["S-F1"], "latent": "batch",
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


def load_state(sql_text, revision=None):
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
            "doc": doc["document_id"] if doc else None, "comment": note["id"] if note else None}
    sheets = {(r["spreadsheet_id"], r["title"]): json.loads(r["grid_json"]) for r in tables["gsheets.sheets_sheets"]}
    return {"revision": revision or REVISIONS[-1], "sessions": sessions, "docs": docs, "slack": slack, "mail": mail,
            "reviews": reviews, "sheets": sheets, "comments": {r["id"]: r for r in tables["linear.linear_comments"]},
            "base_retention": _base_retention()}


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


def _samsung(st, device):
    """The gate Doc's one device group, read from its own family and model-number lists."""
    doc = st["docs"].get(GATE_DOC)
    if not doc or not device:
        return False
    text = " ".join(_text(doc["body_text"]).split())
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
    """A pass covers a device only if it ran on that device; the job owner's note says this job ran with no phone."""
    note = st["reviews"].get(RC27)
    return not (note and "no phone in the loop" in str(note["body"]))


def _k4_groups(st):
    """Relation values the DM line says work in games, once the industry rule exists."""
    line, rule = st["slack"].get(K4_LINE), st["slack"].get(R3_INDUSTRY)
    if not line or not rule or "game-industry people don" not in str(rule["text"]):
        return set()
    text = str(line["text"])
    if "oyun sektör" not in text:
        return set()
    return {s["relation"] for s in st["sessions"].values() if s["relation"] and s["relation"] in text}


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
    if not _on(disable, "R_K3", key) and _samsung(st, s["device"]) and not _pass_on_device(st):
        return "device", "R_K3"
    if not _on(disable, "R_K4", key) and s["relation"] in _k4_groups(st):
        return "game_industry", "R_K4"
    build_id = (re.search(r"\((\d+)\)", s["build"] or "") or [None, None])[1]
    if not _on(disable, "R_K5", key) and build_id in _k5_builds(st):
        return "build", "R_K5"
    return None, None


def _session_row(st, key, disable, degrade):
    s = st["sessions"][key]
    reason, rule = _reason(st, key, disable)
    truth_reason = _reason(st, key, frozenset())[0]
    # over-application reaches only the rule's controls: sessions the truth counts, whatever other mistakes a run makes
    if truth_reason is None:
        k1 = _k1_scope(st)
        android = not str(s["device"]).startswith("iPhone")
        if k1 and _on(degrade, "over:K1_all_sessions_that_day", key) and s["session_date"] == k1[1]:
            reason = "coached"
        elif _on(degrade, "over:K3_all_android", key) and android:
            reason = "device"
        elif _on(degrade, "over:K4_any_group_nickname", key) and _batch_shares_relation(st, key):
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
    return {"ticket": key, "observer": s["observer"], "session_date": s["session_date"], "audience": s["audience"],
            "rating": s["rating"], "device": s["device"], "build": s["build"], "age": s["age"], "relation": s["relation"],
            "verdict": verdict, "reason": reason, "rerun": rerun, "groups": [reason] if reason else [],
            "evidence": {"ticket": key, "doc": s["doc"], "comment": s["comment"],
                         "verdict": list(RULES[rule]["authority"]) if rule else [key]}}


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


def _retention_row(st, disable):
    rule = st["slack"].get(R5_RETENTION)
    grid = st["sheets"].get((KPI_SHEET, "KPI")) or []
    kpi = next((float(r[-1]) for r in grid if r and r[0] == "D7 mean"), None)
    if rule and "install-weighted D7" in str(rule["text"]) and not _on(disable, "R_E", "retention"):
        mature = [r for r in st["base_retention"] if r.get("d14_ret") is not None and r.get("d7_ret") is not None]
        installs = sum(r["installs"] for r in mature)
        value = round(sum(r["d7_ret"] * r["installs"] for r in mature) / installs, 2) if installs else None
        return {"item": "retention", "retention_d7": value, "retention_rows": len(mature), "retention_method": "install-weighted",
                "groups": [], "evidence": {"retention_d7": [R5_RETENTION]}}
    return {"item": "retention", "retention_d7": kpi, "retention_rows": sum(1 for r in grid[1:] if r and r[0] != "D7 mean"),
            "retention_method": "kpi simple mean", "groups": [], "evidence": {"retention_d7": [KPI_SHEET]}}


def keys(state):
    return list(state["sessions"]) + ["panel", "retention"]


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    out = {}
    for k in (keys_ if keys_ is not None else keys(state)):
        if k == "panel":
            out[k] = _panel_row(state, disable)
        elif k == "retention":
            out[k] = _retention_row(state, disable)
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
            "decision": "hold" if lead == "casual" else "keep", "rerun": sorted(k for k, v in sess.items() if v["rerun"])}


def evidence(rows, key, field):
    ev = rows[key].get("evidence") or {}
    if field in ("ticket", "observer", "session_date"):
        return [ev["ticket"]]
    if field == "device":
        return [ev["comment"]] if ev.get("comment") else []
    if field == "build" and "1943" in str(rows[key].get("build")):
        return [ev["doc"], BUILDS_1943_TS]
    if field in ("audience", "rating", "build", "age", "relation"):
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


_DECIDING = {"R_K1": [K1_MAIL], "R_K3": [RC27], "R_K4": [K4_LINE, R3_INDUSTRY], "R_K5": [K5_REPLY], "R_F": [F_REPLY],
             "R_D": [PANEL_MAIL], "R_E": [R5_RETENTION]}


def deciding(state, rule, key):
    return list(_DECIDING[rule]) if key in touched(state, rule) else []


if __name__ == "__main__":
    if "--refresh-base" in sys.argv:
        print("rows", refresh_base())
