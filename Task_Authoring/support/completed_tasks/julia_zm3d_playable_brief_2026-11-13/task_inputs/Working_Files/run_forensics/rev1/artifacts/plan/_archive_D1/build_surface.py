#!/usr/bin/env python3
"""Build Working_Files/01_Gradable_Surface.json from design_model.py (scenario S6b). No criterion text."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import design_model as M

WF = Path(__file__).resolve().parents[1]
T = M.BY_NAME
def tk(name): return T[name]["ticket"]
KEYS = [l["name"] for l in M.LINES]
slots = []
def slot(sid, title, weight, kind, reason, cls, selector, role, mechs, span, **kw):
    s = {"id": sid, "title": title, "weight": weight, "work_kind": kind, "work_reason": reason, "class": cls,
         "selector": selector, "role": role, "mechanisms": mechs, "incorporating_span": span}
    s.update(kw); slots.append(s)

MS, LR, CALC, INT, LOOK = "multi_source_reconciliation", "limited_reconciliation", "calculation", "interpretation", "lookup"
SPAN_SHEET = "the hand-off list goes in my Drive"
SPAN_BRIEF = "the brief goes in my Drive"
SPAN_TIX = "anything we still owe goes back on its ticket"
SPAN_REPLY = "reply to him with the counts"
SPAN_VENDOR = "post both links in the PlayableX channel"

# ---- state per line: five samples, one per deciding record ------------------------------------------------------
for sid, name, mech, why in (
    ("X1", "Washing Machine", "EXPORT", "pack list and ticket say the model file is in the outgoing folder; Arthur's #zombie-bugs post says a multi-select export writes an empty shell"),
    ("X2", "Bathtub", "ARTHOLD", "ticket says the art is fine and the file is exported; Claire's DM says she is redoing the UVs on the bathroom ones"),
    ("X3", "Cactus Plant", "REVISED", "pack list says it went in the 24 Sep zip; base #zombie-art and match3d#462 show the art changed on 25 Sep"),
    ("X4", "Cello", "PARENT", "its ticket says exported 26 Sep; Brian's later comment on the pack ticket says the music set comes in without textures"),
    ("X5", "Match scale", "AUDIO", "its ticket says exported .wav; Calvin's source sheet says it is cut from a bought pack; the notes let only owned sound leave")):
    slot(sid, f"{name} state", 5, MS, why, "direct", ["field", name, "State"], "sample", [mech], SPAN_SHEET, group="state")
# ---- what is owed: five samples ---------------------------------------------------------------------------------
for sid, name, mech, rx, why in (
    ("X6", "Washing Machine", "EXPORT", r".*([Rr]e-?export|[Ee]mpty|[Ss]hell|one (at a time|by one)).*", "the reason comes from Arthur's post, joined to the ticket's export note"),
    ("X7", "Bathtub", "ARTHOLD", r".*(UV|[Uu]nwrap|[Rr]edo|[Rr]edone|[Rr]edoing|[Aa]rt).*", "the reason comes from Claire's DM, joined to the pack list's set"),
    ("X8", "Cactus Plant", "REVISED", r".*([Cc]hanged|[Rr]evis|[Cc]urrent|[Nn]ew(er)? version|[Rr]e-?send|[Cc]olou?r).*", "the reason comes from the 25 Sep revision, joined to the 24 Sep delivery"),
    ("X9", "Cello", "PARENT", r".*([Tt]exture|[Gg]r[ae]y|[Rr]e-?export|another pass).*", "the reason comes from Brian's pack-ticket comment, joined to the pack list's set"),
    ("X10", "Match scale", "AUDIO", r".*([Ll]icen[cs]|[Bb]ought|[Pp]ack|[Oo]wn|[Rr]eplace).*", "the reason comes from Calvin's source sheet, joined to the notes' sound rule")):
    slot(sid, f"{name} what is owed", 5, MS, why, "write_content", ["reason_matches", name, rx], "sample", [mech], SPAN_SHEET, group="owed")
# ---- who has it: five samples -----------------------------------------------------------------------------------
for sid, name, mech, who, why, w, kind in (
    ("X11", "Bathtub", "ARTHOLD", "Claire", "the owner follows from Claire's DM (she is redoing the art)", 5, MS),
    ("X12", "Match scale", "AUDIO", "Calvin", "the owner follows from Calvin's source sheet (he keeps the cues)", 5, MS),
    ("C1", "Fonts", None, "Martin", "the line's own ticket says no font files have come from Martin", 3, INT),
    ("C2", "Music", None, "Frederick", "the line's own ticket says the track choice is with Frederick", 3, INT),
    ("X16", "Washing Machine", "EXPORT", "Brian", "the owner follows from Arthur's post (redo by hand what was pushed out) joined to the ticket's export note", 5, MS)):
    slot(sid, f"{name} who has it", w, kind, why, "direct", ["reason_matches", name, f".*{who}.*"] if False else ["field", name, "Who has it"],
         "sample", [mech] if mech else [], SPAN_SHEET, group="owner")
# ---- board set: five samples ------------------------------------------------------------------------------------
for sid, name, mech, why, w, kind in (
    ("X13", "Bow", "PICKS", "Robert's 23 Sep picks list the iron; his 26 Sep reply under another post puts the bow on the board instead", 5, MS),
    ("X14", "Iron", "PICKS", "same two records: the iron leaves the default eight", 5, MS),
    ("X15", "Soccer Ball", "PICKS", "not on Brian's list; Robert's 26 Sep reply adds it to what goes over", 5, MS),
    ("C4", "Grenade", None, "on Robert's 23 Sep picks and unchanged", 3, INT),
    ("C5", "Rolling Pin", None, "on the pack list, not on Robert's picks: an extra", 3, INT)):
    slot(sid, f"{name} board set", w, kind, why, "direct", ["field", name, "Board set"], "sample", [mech] if mech else [], SPAN_SHEET, group="set")
# ---- volume and totals ------------------------------------------------------------------------------------------
slot("V1", "hand-off list lines", 5, MS, "97 lines on Brian's list plus the six Robert added in a reply elsewhere", "delivery",
     ["delivery", "register_keys_exact"], "volume", ["PICKS"], SPAN_SHEET, fact_id="line_set",
     volume_for=["state", "owed", "owner", "set"], expected_keys=KEYS)
ALL = ["EXPORT", "ARTHOLD", "REVISED", "PARENT", "AUDIO", "PICKS"]
slot("A1", "owed count on the list", 3, CALC, "the count of Owed lines after every deciding record is applied (54)", "aggregate",
     ["total", "Owed"], "core", ALL, SPAN_SHEET, fact_id="count_owed")
slot("A2", "ready count on the list", 3, CALC, "the count of Ready lines (30)", "aggregate", ["total", "Ready"], "core",
     ["EXPORT", "ARTHOLD", "PARENT", "AUDIO", "REVISED"], SPAN_SHEET, fact_id="count_ready")
slot("A3", "delivered count on the list", 3, CALC, "the count of lines PlayableX holds and can use (19)", "aggregate",
     ["total", "Delivered"], "core", ["REVISED"], SPAN_SHEET, fact_id="count_with")
slot("W1", "reply gives the owed count", 3, CALC, "same count carried into the reply (54)", "write_content",
     ["text", "replies", r".*54.*"], "core", ALL, SPAN_REPLY, fact_id="count_owed")
slot("W2", "reply gives the ready count", 3, CALC, "same count carried into the reply (30)", "write_content",
     ["text", "replies", r".*30.*"], "core", ["EXPORT", "ARTHOLD", "PARENT", "AUDIO", "REVISED"], SPAN_REPLY, fact_id="count_ready")
slot("W3", "reply gives the delivered count", 3, CALC, "same count carried into the reply (19)", "write_content",
     ["text", "replies", r".*19.*"], "core", ["REVISED"], SPAN_REPLY, fact_id="count_with")
# ---- ticket follow-through: samples naming their targets --------------------------------------------------------
for sid, name, mech in (("W4", "Washing Machine", "EXPORT"), ("W5", "Bathtub", "ARTHOLD"), ("W6", "Cactus Plant", "REVISED"),
                        ("W7", "Cello", "PARENT"), ("W8", "Match scale", "AUDIO")):
    slot(sid, f"{name} ticket back to Todo", 3, INT, "applies that line's Owed call to its own ticket", "write_content",
         ["text", "updates", rf".*{tk(name)}.*[Tt]odo.*"], "sample", [mech], SPAN_TIX, group="moves")
slot("W9", "tickets moved to Todo", 3, CALC, "exactly the 48 Owed lines that have a ticket (39 decided off the ticket, nine on the ticket's own note); every line ticket starts Done", "write_content",
     ["text", "updates", r".*[Tt]odo.*"], "volume", ALL[:5], SPAN_TIX, fact_id="moves_48", volume_for=["moves"], atoms=1)
slot("W10", "new ticket for Soccer Ball", 5, MS, "a line Robert added has no ticket: one is opened under the pack ticket", "write_content",
     ["text", "creates", r".*[Ss]occer [Bb]all.*"], "core", ["PICKS"], SPAN_TIX, fact_id="new_ticket_soccer")
slot("W11", "new ticket for Toy Drum", 5, MS, "a line Robert added has no ticket: one is opened under the pack ticket", "write_content",
     ["text", "creates", r".*[Tt]oy [Dd]rum.*"], "core", ["PICKS"], SPAN_TIX, fact_id="new_ticket_drum")
slot("W12", "comment on the Wooden Crate ticket", 3, INT, "the line's own ticket states what is owed; the comment repeats it for the owner", "write_content",
     ["text", "comments", rf".*{tk('Wooden Crate')}.*"], "core", [], SPAN_TIX, fact_id="comment_crate")
# ---- the brief --------------------------------------------------------------------------------------------------
slot("B1", "brief: default eight", 5, MS, "Robert's 23 Sep picks as changed by his 26 Sep reply (bow in, iron out)", "write_content",
     ["text", "brief", r".*Bow.*"], "core", ["PICKS"], SPAN_BRIEF, fact_id="default_eight")
slot("B2", "brief: scenario", 3, INT, "Frederick chose Scenario 1 on 15 Sep in the PlayableX channel", "write_content",
     ["text", "brief", r".*[Ss]cenario 1.*"], "core", [], SPAN_BRIEF, fact_id="scenario")
slot("B3", "brief: zombies and animation", 3, INT, "Robert's 29 Sep answer to PlayableX's question: walk; Chef, Bike Kid, Boxer, Mayor", "write_content",
     ["text", "brief", r".*[Ww]alk.*"], "core", [], SPAN_BRIEF, fact_id="zombies_anim")
slot("B4", "brief: tray size", 3, INT, "the design page says a 7-slot tray; the 6-slot proposal in its comments was not adopted", "write_content",
     ["text", "brief", r".*(7|seven)[- ]slot.*"], "core", [], SPAN_BRIEF, fact_id="tray")
slot("B5", "brief: start date", 3, INT, "29 Sep, then 6 Oct, then 3 Nov in the PlayableX channel: the last stands", "write_content",
     ["text", "brief", r".*(3 Nov|Nov 3|November 3|2025-11-03).*"], "core", [], SPAN_BRIEF, fact_id="start_date")
slot("B6", "brief: sound section", 5, MS, "the notes' rule (only sound we own leaves) applied to Calvin's source sheet: two cues are out", "write_content",
     ["text", "brief", r".*([Mm]atch scale|[Ee]xplosion).*"], "core", ["AUDIO"], SPAN_BRIEF, fact_id="sound_section")
# ---- delivery ---------------------------------------------------------------------------------------------------
slot("D1", "reply in Frederick's DM", 1, LOOK, "reply where he asked", "delivery", ["delivery", "slack_channel_post", M.DM_FRED, r".*"], "core", [], SPAN_REPLY)
slot("D2", "post in the PlayableX channel", 1, LOOK, "the channel the ask names", "delivery",
     ["delivery", "slack_channel_post", M.VENDOR_CH, r".*"], "core", [], SPAN_VENDOR)
slot("D3", "hand-off list in Julia's Drive", 1, LOOK, "created under her own root", "delivery",
     ["delivery", "register_parent", M.BASE["julia_root"]], "core", [], SPAN_SHEET)
slot("D4", "both files shared for viewing", 1, LOOK, "the notes: both files, view only, to the people on the kickoff hold and PlayableX's intake address", "delivery",
     ["delivery", "share_reader"], "core", [], SPAN_BRIEF)

surface = {
    "kind": "GRADABLE_SURFACE", "version": 1, "task": M.SLUG, "revision": "D1-design",
    "truth_keys": KEYS, "classes": ["Delivered", "Ready", "Owed"],
    "truth_fields": {"class": "State", "groups": "groups"},
    "deliverables": {
        "handoff": {"kind": "table", "name_regex": r"(?i).*(hand-?off|pack|playable).*", "key_column": "Line",
                    "key_regex": r"[A-Z][A-Za-z ]*[0-9][A-Za-z0-9 ]*|[A-Z][A-Za-z ]+", "columns": ["Line", "Kind", "Board set", "State", "What's owed", "Who has it", "Ticket"],
                    "class_column": "State", "reason_column": "What's owed", "comparators": {"State": "norm", "Board set": "norm", "Who has it": "norm", "Ticket": "issue_key"}},
        "brief": {"kind": "json_text", "tool": "gdocs_batch_update"},
        "comments": {"kind": "json_text", "tool": "linear_create_comment"},
        "updates": {"kind": "json_text", "tool": "linear_update_issue"},
        "creates": {"kind": "json_text", "tool": "linear_create_issue"},
        "replies": {"kind": "json_text", "tool": "slack_send_message"},
        "share": {"kind": "calls", "tool": "gdrive_share_file"}},
    "slots": slots}
out = WF / "01_Gradable_Surface.json"
out.write_text(json.dumps(surface, indent=1, ensure_ascii=False) + "\n")
print("slots", len(slots), "weight", sum(s["weight"] for s in slots), "->", out.name)
