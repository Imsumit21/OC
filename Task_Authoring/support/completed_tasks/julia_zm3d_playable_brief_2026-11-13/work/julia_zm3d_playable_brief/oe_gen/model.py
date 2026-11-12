#!/usr/bin/env python3
"""Shared model for the Oracle Event ledger, the drafted events and the check (stage 08).

Every value comes from a record: the statements of 01_Universe_Inject.sql for seeded rows (read as an overlay, never
executed) or the base records re-read through tools/hg.py (oe_gen/out/base_records.json, base_other.json, written by
oe_gen/base_read.py). The plan's design model and solver/truth.json are used only to cross-check; they never supply a value.
"""
import datetime as D, json, re, sys
from pathlib import Path
from zoneinfo import ZoneInfo

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
ROOT = TASK.parents[1]
TOOLS = TASK.parent / "tools"
sys.path.insert(0, str(TOOLS)); sys.path.insert(0, str(WF / "plan"))
from base_check import parse_sql  # noqa: E402
import design_model as M          # noqa: E402  (cross-check only)

PT = ZoneInfo("America/Los_Angeles")
SQL_PATH = TASK / "01_Universe_Inject.sql"
SQL_TEXT = SQL_PATH.read_text()
ROWS = parse_sql(SQL_TEXT)
PROMPT = (TASK / "04_Prompt.txt").read_text()
PERSONA = "julia_lawson"
JULIA = "julia.lawson@harmonygames.co"


# ------------------------------------------------------------------ time
def utc(x):
    if isinstance(x, (int, float)) or re.fullmatch(r"\d{10}\.\d{6}", str(x)):
        return D.datetime.fromtimestamp(float(x), D.timezone.utc)
    return D.datetime.fromisoformat(str(x).replace("Z", "+00:00")).astimezone(D.timezone.utc)

def day_pt(x):
    """'Tue Sep 30 2025' in Pacific time."""
    d = utc(x).astimezone(PT)
    return f"{d:%a %b} {d.day} {d.year}"

def when(x):
    """'Tue Sep 30 2025 11:21 AM PT (2025-09-30T18:21Z)'."""
    u = utc(x); d = u.astimezone(PT)
    return f"{d:%a %b} {d.day} {d.year} {d.hour % 12 or 12}:{d:%M} {'AM' if d.hour < 12 else 'PM'} PT ({u:%Y-%m-%dT%H:%MZ})"


# ------------------------------------------------------------------ seeded rows
def find(table, **kv):
    for r in ROWS:
        vals = r.get("row") or {}
        if r["table"] == table and r["op"] == "insert" and all(str(vals.get(k)) == str(v) for k, v in kv.items()):
            return r
    raise KeyError((table, kv))

def row(table, **kv): return find(table, **kv)["row"]
def line(table, **kv): return find(table, **kv)["line"]
def sql(table, **kv): return f"SQL L{line(table, **kv)}"

S = M.SEED
def slack_seed(key):
    ch, ts = S[key]["id"].split("/")
    r = find("slack.slack_messages", channel_id=ch, ts=ts)
    return {"id": S[key]["id"], "channel": ch, "ts": ts, "text": r["row"]["text"], "user": r["row"]["user_id"], "line": r["line"],
            "thread_parent": r["row"].get("thread_parent_id")}

ASK = slack_seed("ask"); PICKS = slack_seed("picks"); ZPICKS = slack_seed("zpicks"); C3 = slack_seed("c3_reply")
A1 = slack_seed("a1_post"); A2 = slack_seed("a2_dm")
NOTES_ID = S["notes"]["id"]; NOTES = row("gdocs.docs_documents", document_id=NOTES_ID)
LOG_ID = S["c4_log"]["id"]; LOG = row("gdocs.docs_documents", document_id=LOG_ID)
# the SQL writes line breaks as \n inside E'...' literals; the stored text has real line breaks
def _unescape(r): return dict(r, body_text=r["body_text"].replace("\\n", "\n"))
NOTES, LOG = _unescape(NOTES), _unescape(LOG)
assert "\\n" not in NOTES["body_text"] and NOTES["body_text"].count("\n\n") == 7
PACK_ID = S["tracker"]["id"]; PACK_SHEET = row("gsheets.sheets_sheets", spreadsheet_id=PACK_ID)
SOUND_ID = S["c2_sheet"]["id"]; SOUND_SHEET = row("gsheets.sheets_sheets", spreadsheet_id=SOUND_ID)
DECK_ID = S["deck"]["id"]
HOLD_ID = S["hold"]["id"]; HOLD = row("gcal.gcal_events", event_id=HOLD_ID)
CONTACT = row("contacts.contacts", contact_id=S["contact"]["id"])
TRELLO = row("trello.trello_actions", id=S["trello_note"]["id"])
def drive(i): return row("gdrive.drive_files", id=i)

PACK_GRID = json.loads(PACK_SHEET["grid_json"])
SOUND_GRID = json.loads(SOUND_SHEET["grid_json"])
assert PACK_GRID[0] == ["Line", "Kind", "Category", "Went out", "Ticket"], PACK_GRID[0]
DECK_TEXT = {}
for r in ROWS:
    if r["table"] == "gslides.slides_page_elements" and r["row"]["presentation_id"] == DECK_ID:
        DECK_TEXT.setdefault(r["row"]["page_object_id"] if "page_object_id" in r["row"] else r["row"].get("page_id"), []).append(
            (r["line"], next((str(r["row"][c]) for c in ("text", "text_content") if r["row"].get(c)), "")))
DECK_SLIDES = [(v[0][1], v[1][1], v[0][0], v[1][0]) for v in DECK_TEXT.values() if len(v) == 2]   # (title, body, title line, body line)

ISSUES = {r["row"]["id"]: r for r in ROWS if r["table"] == "linear.linear_issues" and r["op"] == "insert"}
COMMENTS = {}
for r in ROWS:
    if r["table"] == "linear.linear_comments" and r["op"] == "insert":
        COMMENTS.setdefault(r["row"]["issue_id"], []).append(r)
PACK_TICKET = "DES-313"
BRIAN_USR = ISSUES[PACK_TICKET]["row"]["creator_id"]

FINAL_EIGHT_SRC = None   # set below from Robert's two messages


# ------------------------------------------------------------------ the 96 lines, read from the pack list, the tickets and the notes
def _picks():
    m = re.search(r"the 8: (.+?) from the reference level, plus (.+?)\.", PICKS["text"])
    first = [x.strip() for x in re.split(r",| and ", m.group(1)) if x.strip()]
    rest = [x.strip() for x in re.split(r",| and ", m.group(2)) if x.strip()]
    return first + rest
EIGHT_25SEP = _picks()                                   # Robert's list of 25 Sep, in his order
assert EIGHT_25SEP == M.PICKS_25SEP, EIGHT_25SEP
assert "in place of the last one on my list" in C3["text"]
EIGHT = [x for x in EIGHT_25SEP[:-1]] + ["Bow"]          # his reply of 26 Sep: the bow in place of the last one on his list
SWAPPED_OUT = EIGHT_25SEP[-1]
assert sorted(EIGHT) == sorted(M.DEFAULT_FINAL) and SWAPPED_OUT == "Dynamite"

OWED_TEXT = {   # what is owed, in words each deciding record supports
    "A1": "a binary FBX export (the models Brian got out of Unity on Thursday are the text kind, and PlayableX take .fbx in Binary format, not ASCII)",
    "A2": "the file again once the UVs are redone (the bathroom files Claire gave Brian on Friday are the old version)",
    "C4": "the file put back in the outgoing folder (the instruments zip got cut off on upload and won't unpack)",
    "C2": "our own version of the sound (this one is from a library or a bought pack)",
}
WHO = {"A1": "Brian", "A2": "Claire", "C4": "Brian", "C2": "Calvin"}
VIS_OWED = [   # (test on Brian's note, what is owed, who has it)
    (r"Waiting on the FBX from Claire", "the FBX from Claire", "Claire"),
    (r"Mine to do, didn't get to it on Friday", "the export", "Brian"),
    (r"Calvin is still cutting the ad track down to a loop", "the loop cut from the ad track", "Calvin"),
    (r"mine to pull as PNG", "the PNG export from Figma", "Brian"),
    (r"Waiting on the \.ttf files from Martin", "the .ttf files", "Martin"),
]
RECOLOURED = ("Cactus Plant", "Chainsaw", "Cone")        # Robert, 29 Sep: "cactus, chainsaw and cones"; rev2: Brian's log of 30 Sep, sent again
LIBRARY_SOUNDS = [r[0] for r in SOUND_GRID[1:] if r[2] == "no" and r[0] in {g[0] for g in PACK_GRID[1:]}]
assert LIBRARY_SOUNDS == ["Rocket sound", "Explosion sound"], LIBRARY_SOUNDS

def classify(name, kind, category, ticket_state, note):
    if ticket_state == "Done":
        return "W", "Delivered", None, None
    if note.startswith("Not exported") or note.startswith("Not sent"):
        for rx, owed, who in VIS_OWED:
            if re.search(rx, note): return "VIS", "Owed", owed, who
        raise ValueError(note)
    if "saved out of the project, Thu 25 Sep" in note: cls = "A1"
    elif category == "Bathroom" and "FBX from Claire, Fri 26 Sep" in note: cls = "A2"
    elif name in RECOLOURED: return "C1", "Ready", None, None     # new colours (29 Sep), sent again and current (log, 30 Sep)
    elif "Zipped with the other instruments" in note: cls = "C4"
    elif name in LIBRARY_SOUNDS: cls = "C2"
    else: return "READY", "Ready", None, None
    return cls, "Owed", OWED_TEXT[cls], WHO[cls]

LINES = []
for g in PACK_GRID[1:]:
    name, kind, category, went, ticket = g
    iss = ISSUES[ticket]; ir = iss["row"]
    assert ir["title"] == name and ir["parent_id"] == PACK_TICKET, (name, ir["title"])
    cs = COMMENTS[ticket]; assert len(cs) == 1, (ticket, len(cs))
    c = cs[0]; cr = c["row"]
    assert cr["author_id"] == BRIAN_USR
    cls, state, owed, who = classify(name, kind, category, ir["state_id"], cr["body"])
    LINES.append({"name": name, "kind": kind, "category": category, "went_out": went, "ticket": ticket,
                  "ticket_state": ir["state_id"], "ticket_line": iss["line"], "ticket_created": ir["created_at"], "completed_at": ir["completed_at"],
                  "note": cr["body"], "note_at": cr["created_at"], "note_line": c["line"], "note_id": cr["id"],
                  "cls": cls, "state": state, "owed": owed, "who": who,
                  "board": ("Default" if name in EIGHT else "Extra") if kind == "Board item" else ""})
BY = {l["name"]: l for l in LINES}
assert len(LINES) == 96 and [l["ticket"] for l in LINES] == [f"DES-{n}" for n in range(314, 410)]

# cross-check against the solver's truth and the design model (neither supplies a value)
TRUTH = json.loads((WF / "solver" / "truth.json").read_text())
for l in LINES:
    t = TRUTH[l["name"]]; m = M.BY_NAME[l["name"]]
    assert (t["State"], t["Who has it"], t["Ticket"], t["Board set"] or "") == (l["state"], l["who"], l["ticket"], l["board"]), (l["name"], t, l)
    assert m["cls"] == l["cls"] and m["note"] == l["note"], (l["name"], m["cls"], l["cls"])

def members(cls): return [l for l in LINES if l["cls"] == cls]
def by_state(s): return [l for l in LINES if l["state"] == s]
COUNTS = {s: len(by_state(s)) for s in ("Delivered", "Ready", "Owed")}
assert COUNTS == {"Delivered": 8, "Ready": 39, "Owed": 49}, COUNTS
WHO_COUNTS = {w: sum(1 for l in LINES if l["who"] == w) for w in ("Brian", "Claire", "Calvin", "Martin")}
assert WHO_COUNTS == {"Brian": 27, "Claire": 18, "Calvin": 3, "Martin": 1}, WHO_COUNTS
BOARD_ITEMS = [l for l in LINES if l["kind"] == "Board item"]
NOT_BOARD = [l for l in LINES if l["kind"] != "Board item"]
assert len(BOARD_ITEMS) == 84 and len(NOT_BOARD) == 12
DONE = [l for l in LINES if l["ticket_state"] == "Done"]; IN_PROGRESS = [l for l in LINES if l["ticket_state"] == "In Progress"]
assert len(DONE) == 8 and len(IN_PROGRESS) == 88

def note_groups():
    """Brian's notes grouped by identical wording, in pack-list order: [(note text, [lines])]."""
    out = {}
    for l in LINES: out.setdefault(l["note"], []).append(l)
    return list(out.items())

OWED_GROUPS = [   # (key, heading, lines) in the order the events use
    ("A1", "Thursday's saves out of Unity", members("A1")),
    ("A2", "Friday's bathroom files", members("A2")),
    ("C4", "Friday's instruments zip", members("C4")),
    ("C2", "the library and bought-pack sounds", members("C2")),
    ("VIS", "not exported or not sent yet", members("VIS")),
]
assert sum(len(g[2]) for g in OWED_GROUPS) == COUNTS["Owed"] == 49
OVERTURNED = [l for k, _, ls in OWED_GROUPS if k != "VIS" for l in ls]          # exported lines a later record makes Owed (34)
ABSENCE_TARGETS = [l for l in LINES if l["state"] in ("Delivered", "Ready") and l["cls"] != "C1"]   # no later word at all (44)
assert len(OVERTURNED) == 34 and len(ABSENCE_TARGETS) == 44 and len(members("C1")) == 3


# ------------------------------------------------------------------ base records (re-read through tools/hg.py by base_read.py)
_B = json.loads((HERE / "out" / "base_records.json").read_text())
_O = json.loads((HERE / "out" / "base_other.json").read_text())
def base(key):
    """A base Slack message: {id, channel, ts, text, user, thread_ts, reply_count, file, pointer}."""
    e = _B[key]; m = json.loads(e["record"]["text"])
    return {"id": e["id"], "channel": m["channel"], "ts": m["ts"], "text": m["text"], "user": m["user"], "thread_ts": m.get("thread_ts"),
            "reply_count": m.get("reply_count"), "files": [f.get("name") for f in m.get("files") or []],
            "src": f"slack/{e['file']}{e['pointer']}"}
def other(key):
    e = _O[key]
    return dict(e["record"], _src=f"{e['file']}{e['pointer']}")
GDD = other("gdd"); GDD_C1 = other("gdd_c1"); GDD_C2 = other("gdd_c2"); PR462 = other("pr462"); ROOT_FOLDER = other("julia_root"); TEAM = other("team_DES")
GDD_TEXT = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", GDD["body"])).replace(" .", ".").replace(" ,", ",")
VENDOR_CH, DESIGN_CH, ART_CH, MATCH3D_CH = M.VENDOR_CH, M.DESIGN_CH, M.ART_CH, M.MATCH3D_CH
DM_FRED, DM_ROBERT = M.DM_FRED, M.DM_ROBERT
NAMES = {"EMPLOYEE_0008_SLACK_ID": "Frederick Stone", "EMPLOYEE_0016_SLACK_ID": "Robert", "EMPLOYEE_0002_SLACK_ID": "Marcus Bennett",
         "EMPLOYEE_0009_SLACK_ID": "Claire Morgan", "EMPLOYEE_0026_SLACK_ID": "Brian Foster", "EMPLOYEE_0005_SLACK_ID": "Julia Lawson"}

def q(text, phrase):
    """Return phrase after asserting it is an exact substring of text (a verbatim quote)."""
    assert phrase in text, f"not a verbatim quote: {phrase!r}"
    return phrase

if __name__ == "__main__":
    print("lines", len(LINES), COUNTS, WHO_COUNTS, "eight", EIGHT, "out", SWAPPED_OUT)
    for note, ls in note_groups(): print(f"{len(ls):3} | {note[:90]} | {', '.join(l['name'] for l in ls)[:120]}")
    print("deck", DECK_SLIDES)
    print("gdd", GDD_TEXT[620:1050])
