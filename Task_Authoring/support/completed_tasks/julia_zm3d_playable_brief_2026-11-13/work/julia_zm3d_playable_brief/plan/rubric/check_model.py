#!/usr/bin/env python3
"""The 153-row model behind the rubric check (stage 09, check mode).

Built from the reviewed row model of the plan (rows.json, 126 rows), the round 1 fix map (fix_round1_map.json) and the
exported 09_Rubrics.json itself. Nothing here edits the rubric: titles, weights, categories and evidence are read from
the file. Source values are read back through tools/v3_artifact_checks._source_value, the gate's own reader, so every
cited value is the record's actual field."""
import json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
TASK = WF.parent
BUNDLE = TASK.parent
WS = BUNDLE.parent
sys.path.insert(0, str(WF / "oe_gen")); sys.path.insert(0, str(BUNDLE / "tools"))
import model as M                      # noqa: E402
import v3_artifact_checks as V         # noqa: E402

RUB = json.loads((TASK / "09_Rubrics.json").read_text())
N = len(RUB)
OLD = json.loads((HERE / "rows.json").read_text())
FIX = json.loads((HERE / "fix_round1_map.json").read_text())
PROMPT = (TASK / "04_Prompt.txt").read_text()
CONTEXT = json.loads((WF / "00_Task_Context.json").read_text())
SPAN = {"msg": "Frederick's playable message from yesterday", "every": "everything he's asking for in it", "start": "start to finish",
        "drive": "The files he wants should end up in my Drive", "links": "once they're ready the links go in the PlayableX channel like he says"}
for v in SPAN.values(): assert v in PROMPT, v
BASE = json.loads((WF / "oe_gen" / "out" / "base_records.json").read_text())
BASE_OTHER = json.loads((WF / "oe_gen" / "out" / "base_other.json").read_text())
BY_TICKET = {l["ticket"]: l for l in M.LINES}
BY_NAME = M.BY
FULL = {"Brian": "Brian Foster", "Claire": "Claire Morgan", "Calvin": "Calvin Price", "Martin": "Martin Walsh"}

ASK, NOTES, PACK, LOG, SOUND = M.ASK["id"], M.NOTES_ID, M.PACK_ID, M.LOG_ID, M.SOUND_ID
A1, A2 = M.A1["id"], M.A2["id"]

# ------------------------------------------------------------------ rows
def _entry(k):
    es = [e for e in FIX if e["new"] == f"R{k}"]
    assert len(es) == 1, (k, es)
    return es[0]

ROWS = []
for k in range(1, N + 1):
    e = _entry(k); r = RUB[k - 1]
    parent = OLD[int(e["from"][1:]) - 1] if e["from"] else None
    title, ev = r["title"], r["evidence"]
    part = e.get("part")
    m = re.search(r"\bDES-\d+\b", title)
    ticket = m.group(0) if m and m.group(0) in BY_TICKET else None
    line = BY_TICKET.get(ticket)
    if line is None:
        hit = [l for l in M.LINES if re.search(rf"\b{re.escape(l['name'])}\b", title)]
        if parent is not None and parent["tag"].split("_")[0] in ("x", "o", "h", "bs", "sheet") and hit:
            line = max(hit, key=lambda l: len(l["name"]))
    tag = e["tag"]
    if part == "owed": fact = f"owed_item:{line['name']}"
    elif part == "holder": fact = f"holder:{line['name']}"
    elif part == "state_delivered": fact = "state:Plushie Chick"; line = BY_NAME["Plushie Chick"]
    elif part == "board_empty": fact = "board_set:Cannon"; line = BY_NAME["Cannon"]
    elif part == "order_brief": fact = "order:brief_before_link"
    elif part == "order_list": fact = "order:list_before_link"
    else:
        fact = parent["fact"]
        if fact.startswith("whats_owed:"): fact = "owed_item:" + fact.split(":", 1)[1]      # the same fact as the ticket comment's owed part
        if fact.startswith("who_has_it:"): fact = "holder:" + fact.split(":", 1)[1]        # the same fact as the ticket comment's holder part
    span = parent["span"] if parent else {"state_delivered": "every", "board_empty": "every", "order_brief": "links", "order_list": "links"}[part]
    oes = [int(x) for x in re.findall(r"\d+", re.search(r"OE ([\d, ]+)\.?\s*$", ev).group(1))]
    acc = re.search(r"Accept: (.*?)(?= Reject: )", ev)
    rej = re.search(r"Reject: (.*?)(?= OE [\d, ]+\.?\s*$)", ev)
    ROWS.append({"k": k, "cid": f"C{k}", "title": title, "weight": r["weight"], "category": r["category"], "tag": tag, "part": part,
                 "fact": fact, "span": SPAN[span], "span_key": span, "oes": oes, "slot": (parent or {}).get("slot", []) if not part or part in ("owed",) else [],
                 "decided": e.get("decided", "—"), "line": line, "ticket": ticket, "from": e["from"], "change": e["change"],
                 "accept": acc.group(1).strip() if acc else "", "reject": rej.group(1).strip() if rej else "", "evidence": ev,
                 "justification": r["justification"], "parent": parent})
assert len(ROWS) == 153 and [r["k"] for r in ROWS] == list(range(1, 154))
BYK = {r["k"]: r for r in ROWS}

def fam(r):
    t = r["tag"]
    for p, name in (("brief_doc", "brief_doc"), ("b_scenario", "b_scenario"), ("b_purpose", "b_purpose"), ("b_eight_", "b_eight"), ("b_extras", "b_extras"),
                    ("b_zombie_", "b_zombie"), ("b_anim", "b_anim"), ("b_win", "b_win"), ("b_lose", "b_lose"), ("b_tray", "b_tray"), ("b_use_", "b_use"),
                    ("b_music", "b_music"), ("b_start", "b_start"), ("sheet_doc", "sheet_doc"), ("sheet_header", "sheet_header"), ("sheet_volume", "sheet_volume"),
                    ("x_", "state"), ("new_state_delivered", "state"), ("o_", "owed_cell"), ("h_", "holder_cell"), ("bs_", "board_set"), ("new_board_empty", "board_set"),
                    ("sheet_ticket", "ticket_cell"), ("sheet_category", "category_cell"), ("move_volume", "move_volume"), ("move_", "move"),
                    ("comment_", "comment"), ("share_", "share"), ("dm_", "dm"), ("post_", "post"), ("new_order_", "order")):
        if t.startswith(p):
            if name == "comment": return {"owed": "comment_owed", "holder": "comment_holder"}.get(r["part"], "comment_both")
            return name
    raise KeyError(t)
for r in ROWS: r["fam"] = fam(r)

# ------------------------------------------------------------------ source records (values read back through the gate's reader)
def _seeded_slack(cid):
    ch, ts = cid.split("/")
    try: M.find("slack.slack_messages", channel_id=ch, ts=ts)
    except KeyError: return None
    return {"service": "slack", "id": cid, "source_file": "01_Universe_Inject.sql", "table": "slack.slack_messages",
            "identity": {"channel_id": ch, "ts": ts}, "column": "text",
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": "created_at",
                                  "rationale": f"Seeded slack.slack_messages row; a posted message with no edit, sent {M.when(ts)}, before the freeze."}}

def _base_slack(cid):
    ch, ts = cid.split("/")
    for key, b in BASE.items():
        if b["file"].startswith(f"messages/{ch}/") and f'"ts":"{ts}"' in b["record"]["text"]:
            return {"service": "slack", "id": cid, "source_file": b["record"]["file"], "pointer": b["pointer"] + "/text",
                    "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_pointer": b["pointer"] + "/ts",
                                          "rationale": f"Base Slack message, sent {M.when(ts)}, before the freeze; Slack messages in the export carry no edit."}}
    return None

def _doc(fid):
    row = M.row("gdocs.docs_documents", document_id=fid)
    return {"service": "gdocs", "id": fid, "source_file": "01_Universe_Inject.sql", "table": "gdocs.docs_documents", "identity": {"document_id": fid},
            "column": "body_text",
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": "modified_time",
                                  "rationale": f"Seeded gdocs.docs_documents row; modified_time = {row['modified_time']} (before the freeze); the SQL holds one revision, so this body is its state at the freeze."}}

def _sheet(fid):
    row = M.row("gsheets.sheets_spreadsheets", spreadsheet_id=fid)
    return {"service": "gsheets", "id": fid, "source_file": "01_Universe_Inject.sql", "table": "gsheets.sheets_spreadsheets", "identity": {"spreadsheet_id": fid},
            "column": "title",
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": "modified_time",
                                  "rationale": f"Seeded gsheets.sheets_spreadsheets row; modified_time = {row['modified_time']} (before the freeze). The cells are the grid_json of its one gsheets.sheets_sheets row, which has no time column of its own."}}

def _deck(fid):
    row = M.row("gslides.slides_presentations", presentation_id=fid)
    return {"service": "gslides", "id": fid, "source_file": "01_Universe_Inject.sql", "table": "gslides.slides_presentations", "identity": {"presentation_id": fid},
            "column": "title",
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": "modified_time",
                                  "rationale": f"Seeded gslides.slides_presentations row; modified_time = {row['modified_time']} (before the freeze)."}}

def _event(eid):
    row = M.row("gcal.gcal_events", event_id=eid)
    return {"service": "gcal", "id": eid, "source_file": "01_Universe_Inject.sql", "table": "gcal.gcal_events", "identity": {"event_id": eid},
            "column": "attendees_json",
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": "updated",
                                  "rationale": f"Seeded gcal.gcal_events row; updated = {row['updated']} (before the freeze); the attendee list is as last saved."}}

def _note(ticket):
    l = BY_TICKET[ticket]
    return {"service": "linear", "id": "team_DES", "source_file": "01_Universe_Inject.sql", "table": "linear.linear_comments", "identity": {"id": l["note_id"]},
            "column": "body",
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": "created_at",
                                  "rationale": f"Seeded linear.linear_comments row on {ticket}; created_at = {l['note_at']} (before the freeze); is_edited is false."}}

def _gdd():
    b = BASE_OTHER["gdd"]
    path = CONTEXT["source"]["paths"]["confluence"]
    rel = str(Path(path).resolve().relative_to(WS.resolve())) + "/" + b["file"]
    return {"service": "confluence", "id": "page_zm3d_gdd", "source_file": rel, "pointer": b["pointer"] + "/title",
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": True, "recorded_at_pointer": b["pointer"] + "/updated_at",
                                  "rationale": "Base Confluence page; its updated_at precedes the freeze, and the synth-cut export is cut at the clock.",
                                  "state_at_freeze_review": {"reviewer": "build agent (Claude), /create-rubric-writing check",
                                                             "rationale": "The page's updated_at is its last edit and precedes the freeze, so the exported body is the body at the freeze; the tray and loss rules the rows grade are in that body (oe_gen/out/base_other.json, re-read through tools/hg.py).",
                                                             "evidence_ids": ["page_zm3d_gdd"]}}}

PATHS = {   # record id -> (path before the record, reachability rationale)
    ASK: ([], "The prompt names Frederick's playable message from yesterday; Julia is a party to the DM."),
    NOTES: ([("slack", ASK)], "Frederick's message: 'My hand-off notes say what goes in the brief, what counts as ready, what to do with the tickets and who gets the files'; the doc is shared with Julia."),
    PACK: ([("slack", ASK)], "Frederick's message: 'Brian's pack list is where it starts'; the sheet is shared with Julia."),
    A1: ([("slack", ASK), ("gdocs", NOTES)], "The notes: 'if someone who knows the file or the art has said something since, that counts'. Marcus's post is in zombie-match3d, where Julia is a member, the day after Brian's Thursday saves."),
    A2: ([("slack", ASK), ("gdocs", NOTES)], "The notes: 'if someone who knows the file or the art has said something since, that counts'. Robert's note is in Julia's own DM with him."),
    LOG: ([("slack", ASK), ("gdocs", NOTES)], "The notes define Ready as 'sitting in the outgoing folder, it opens'; Brian's log of that folder is shared with Julia."),
    SOUND: ([("slack", ASK), ("gdocs", NOTES)], "The notes: 'Anything from a library or a bought pack stays here until we have our own version'; Calvin's sheet of where each cue came from is shared with Julia."),
    M.PICKS["id"]: ([("slack", ASK)], "Frederick's message: 'Robert's picks for the board and the zombies stand unless he's changed them since'; the picks are in a channel Julia is in."),
    M.ZPICKS["id"]: ([("slack", ASK)], "Frederick's message: 'Robert's picks for the board and the zombies stand unless he's changed them since'; the picks are in a channel Julia is in."),
    M.C3["id"]: ([("slack", ASK)], "Frederick's message: 'Robert's picks for the board and the zombies stand unless he's changed them since'; Robert's reply about the bow is the change."),
    M.DECK_ID: ([("slack", ASK), ("gdocs", NOTES)], "The notes: 'your deck of the reference level has what we built for them'; the deck is Julia's own."),
    M.HOLD_ID: ([("slack", ASK), ("gdocs", NOTES)], "The notes: 'Everyone on the kickoff hold'; the hold is on Julia's calendar."),
    "page_zm3d_gdd": ([("slack", ASK), ("gdocs", NOTES)], "The notes: 'How the level plays is on the design page'; Confluence is unscoped."),
}
GENERIC = ([("slack", ASK), ("gdocs", NOTES)], "The notes list what goes in the brief ('What they told us about formats still holds, and so does their rule from last time about when the music may start'); this message is in a channel Julia is in and carries the fact the row grades.")
NOTE_PATH = ([("slack", ASK), ("gdocs", NOTES), ("gsheets", PACK)],
             "The pack list's Ticket column names the ticket, and the notes say 'Brian's note on each ticket says what he did with the line'. Linear is unscoped. The gate's Linear lookup reads base data only, so the seeded ticket is cited through its base DES team; the row itself is the seeded comment named in identity.")

_cache = {}
def source(rid, kind=None):
    key = (rid, kind)
    if key in _cache: return json.loads(json.dumps(_cache[key]))
    if kind == "note": spec, (pre, why) = _note(rid), NOTE_PATH
    else:
        if rid in (NOTES, LOG): spec = _doc(rid)
        elif rid in (PACK, SOUND): spec = _sheet(rid)
        elif rid == M.DECK_ID: spec = _deck(rid)
        elif rid == M.HOLD_ID: spec = _event(rid)
        elif rid == "page_zm3d_gdd": spec = _gdd()
        elif "/" in rid: spec = _seeded_slack(rid) or _base_slack(rid)
        else: spec = None
        if spec is None: return None
        pre, why = PATHS.get(rid, GENERIC)
    spec["evidence_path"] = [{"service": s, "id": i} for s, i in pre] + [{"service": spec["service"], "id": spec["id"]}]
    spec["reachability_rationale"] = why
    spec["source_value"] = V._source_value(spec, TASK, CONTEXT, WS)
    errs = V._temporal(spec, CONTEXT, TASK, WS)
    assert not errs, (rid, errs)
    ordered = {k: spec[k] for k in ("service", "id", "source_file", "table", "identity", "column", "pointer", "source_value", "evidence_path",
                                    "reachability_rationale", "temporal_evidence") if k in spec}
    _cache[key] = ordered
    return json.loads(json.dumps(ordered))

RX_IDS = re.compile(r"\b[CDG](?=[A-Z0-9]*\d)[A-Z0-9]{8,11}/\d{10}\.\d{6}\b|\b[fd]_[0-9a-f]{22}\b|\bevt_[0-9a-f]{8,}\b|\bpage_zm3d_gdd\b")
CONTACT_ID = M.S["contact"]["id"]

def sources_for(r):
    out, seen, notes = [], set(), []
    for rid in RX_IDS.findall(r["evidence"]):
        if rid in seen: continue
        seen.add(rid)
        s = source(rid)
        if s is None: notes.append(rid); continue
        out.append(s)
    if r["line"] is not None and r["fam"] not in ("b_eight", "b_use"):
        out.append(source(r["line"]["ticket"], "note"))
    if r["fam"] in ("state", "owed_cell", "holder_cell", "board_set", "ticket_cell", "category_cell", "sheet_volume", "sheet_header", "move_volume", "dm") and PACK not in seen:
        out.append(source(PACK)); seen.add(PACK)
    if not out or r["fam"] in ("share", "sheet_doc", "brief_doc", "post", "order", "dm", "move", "move_volume", "comment_owed", "comment_holder", "comment_both"):
        for rid in ((ASK,) if r["fam"] in ("sheet_doc", "brief_doc", "post", "order", "dm") else (NOTES,)):
            if rid not in seen: out.insert(0, source(rid)); seen.add(rid)
    assert out, r["cid"]
    return out, notes


if __name__ == "__main__":
    import collections
    print(collections.Counter(r["fam"] for r in ROWS))
    c = collections.Counter(r["fact"] for r in ROWS)
    print("facts", len(c), "graded twice:", sum(1 for v in c.values() if v == 2), "three or more:", [k for k, v in c.items() if v >= 3])
    unresolved = collections.Counter()
    for r in ROWS:
        s, notes = sources_for(r)
        for x in notes: unresolved[x] += 1
    print("ids with no source spec:", dict(unresolved))
    print("distinct source records:", len(_cache))
