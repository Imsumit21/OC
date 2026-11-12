#!/usr/bin/env python3
"""Build Working_Files/01_Gradable_Surface.json from design_model.py (scenario S6b, design D2). No criterion text.
Selectors follow research/selector_guide_D2.md (what tools/surface_grader.py can really read): identifier parameters are
never text, one deliverable reads one tool, one tracked ticket, labelled counts, explicit key names."""
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
ASK_SPAN, CH_SPAN, DRIVE_SPAN = "Frederick's playable message", "the PlayableX channel", "my Drive"   # the three anchor names
ALL = ["EXPORT", "ARTHOLD", "REVISED", "ZIP", "AUDIO"]
GAP = "[ -~\\n]"

# ---- state per line: one sample per deciding record, then the two joins and two controls ------------------------
for sid, name, mech, why in (
    ("X1", "Refrigerator", "EXPORT", "its ticket says FBX saved out of the project, opens, looks right; Marcus's post says those files are the text kind; the vendor takes binary only"),
    ("X2", "Bathtub", "ARTHOLD", "its ticket says FBX from Claire on Friday, looks right; Claire's later message to Julia says she is redoing the bathroom UVs and Friday's files are the old state"),
    ("X3", "Cactus Plant", "REVISED", "its ticket says FBX from Claire first thing on 25 Sep; match3d#462 changed the model later that day and Robert shows the new colour versions on 29 Sep"),
    ("X4", "Cello", "ZIP", "its ticket says zipped with the other instruments, in the outgoing folder; Brian's own log of that folder says the zip will not unpack"),
    ("X5", "Rocket sound", "AUDIO", "its ticket says exported .wav, plays; Calvin's sources sheet says it is from a library seat; the notes hand over only what is ours")):
    slot(sid, f"{name} state", 5, MS, why, "direct", ["field", name, "State"], "sample", [mech], ASK_SPAN, group="state")
slot("X1b", "Retro TV state", 5, MS, "a Living Room line saved out of the project the same day as the kitchen appliances: the join is the ticket note, not the category",
     "direct", ["field", "Retro TV", "State"], "sample", ["EXPORT"], ASK_SPAN, group="state_join")
slot("X2b", "Iron state", 5, MS, "the game files the iron under Bathroom, so Claire's message covers it: the join is the pack list's category",
     "direct", ["field", "Iron", "State"], "sample", ["ARTHOLD"], ASK_SPAN, group="state_join")
slot("X3b", "Cone state", 5, MS, "a second line of the 25 Sep change, named in the pull request's comment by its model file", "direct",
     ["field", "Cone", "State"], "sample", ["REVISED"], ASK_SPAN, group="state_join")
slot("X4b", "Trumpet state", 5, MS, "a second instrument of Friday's zip: the join is the ticket note (zipped with the other instruments)", "direct",
     ["field", "Trumpet", "State"], "sample", ["ZIP"], ASK_SPAN, group="state_join")
slot("X5b", "Explosion sound state", 5, MS, "the second cue Calvin's sheet marks as not ours to pass on", "direct",
     ["field", "Explosion sound", "State"], "sample", ["AUDIO"], ASK_SPAN, group="state_join")
slot("C1", "Rolling Pin state", 3, INT, "control: a kitchen line that came from Claire as FBX and that no later record touches stays Ready",
     "direct", ["field", "Rolling Pin", "State"], "sample", [], ASK_SPAN, group="state_ctl")
slot("C2", "Fly Zapper state", 3, INT, "its own ticket note says it is not exported yet", "direct", ["field", "Fly Zapper", "State"], "sample", [], ASK_SPAN,
     group="state_ctl")
# ---- what is owed: five samples ---------------------------------------------------------------------------------
for sid, name, mech, rx, why in (
    ("X6", "Refrigerator", "EXPORT", r"ascii|binary|text (?:kind|file)|format", "the reason comes from Marcus's post joined to the vendor's binary-only rule"),
    ("X7", "Bathtub", "ARTHOLD", r"UV|unwrap|redo|redone|redoing|rework", "the reason comes from Claire's message, joined to the pack list's category"),
    ("X8", "Cactus Plant", "REVISED", r"chang|revis|current|new(?:er)? version|colou?r|again|re-?send", "the reason comes from the 25 Sep change, joined to the time on the ticket note"),
    ("X9", "Cello", "ZIP", r"zip|unpack|cut off|corrupt|truncat", "the reason comes from Brian's log of the outgoing folder, joined to the ticket note"),
    ("X10", "Rocket sound", "AUDIO", r"librar|licen|own version|Soundly|not ours|replace", "the reason comes from Calvin's sheet, joined to the notes' sound rule")):
    slot(sid, f"{name} what is owed", 5, MS, why, "write_content", ["reason_matches", name, rx], "sample", [mech], ASK_SPAN, group="owed")
# ---- who has it: only where the deciding record itself names the person -----------------------------------------
for sid, name, mech, why in (
    ("X16", "Refrigerator", "EXPORT", "Marcus's post is addressed to Brian, who made the export"),
    ("X11", "Bathtub", "ARTHOLD", "Claire says she is redoing the art herself"),
    ("X11b", "Iron", "ARTHOLD", "the same message, through the pack list's category"),
    ("X12", "Rocket sound", "AUDIO", "Calvin's sheet names him for our own version"),
    ("X17", "Cello", "ZIP", "Brian's log says he will put the files back")):
    slot(sid, f"{name} who has it", 5, MS, why, "direct", ["field", name, "Who has it"], "sample", [mech], ASK_SPAN, group="owner")
# ---- the board set ----------------------------------------------------------------------------------------------
slot("X13", "Bow board set", 5, MS, "Robert's 25 Sep eight as changed by his 26 Sep reply under Julia's bow post", "direct",
     ["field", "Bow", "Board set"], "sample", ["PICKS"], ASK_SPAN, group="set")
slot("X14", "Dynamite board set", 5, MS, "the last item of Robert's 25 Sep eight, which the bow replaced, becomes an extra", "direct", ["field", "Dynamite", "Board set"], "sample", ["PICKS"],
     ASK_SPAN, group="set")
slot("C4", "Grenade board set", 3, INT, "control: a pick Robert did not change", "direct", ["field", "Grenade", "Board set"], "sample", [], ASK_SPAN, group="set")
slot("C5", "Rolling Pin board set", 3, INT, "control: a board item outside the eight is an extra", "direct", ["field", "Rolling Pin", "Board set"], "sample", [],
     ASK_SPAN, group="set")
# ---- the list as a whole ----------------------------------------------------------------------------------------
slot("V1", "hand-off list lines", 3, LR, f"one row for each of the {M.N_LIST} lines of Brian's list, spelled as he spells them", "delivery",
     ["delivery", "register_keys_exact"], "volume", [], ASK_SPAN, fact_id="line_set",
     volume_for=["state", "state_join", "state_ctl", "owed", "owner", "set", "comment"], expected_keys=KEYS)
slot("A1", "owed count on the list", 3, CALC, f"every line's state has to be right for the count ({M.COUNTS['Owed']})", "aggregate", ["total", "Owed"], "core",
     ALL, ASK_SPAN, fact_id="count_owed")
slot("A2", "ready count on the list", 3, CALC, f"the count of lines that can go as they are ({M.COUNTS['Ready']})", "aggregate", ["total", "Ready"], "core",
     ALL, ASK_SPAN, fact_id="count_ready")
slot("A3", "delivered count on the list", 3, CALC, f"the count of lines PlayableX holds ({M.COUNTS['Delivered']})", "aggregate", ["total", "Delivered"], "core",
     [], ASK_SPAN, fact_id="count_delivered")
def count_rx(label, n):
    return (label + "[ A-Za-z:=*_()|>~\\n\\t\\-–—]{0,20}" + str(n) + "\\b|\\b" + str(n) + " (?:lines |line |items |are |is |still )*" + label)
slot("W1", "reply gives the owed count", 3, CALC, "the same count carried into the reply", "write_content", ["text", "slack", count_rx("owed", M.COUNTS["Owed"])],
     "core", ALL, ASK_SPAN, fact_id="count_owed_msg")
slot("W2", "reply gives the ready count", 3, CALC, "the same count carried into the reply", "write_content", ["text", "slack", count_rx("ready", M.COUNTS["Ready"])],
     "core", ALL, ASK_SPAN, fact_id="count_ready_msg")
slot("W3", "reply gives the delivered count", 3, CALC, "the same count carried into the reply", "write_content",
     ["text", "slack", count_rx("delivered", M.COUNTS["Delivered"])], "core", [], ASK_SPAN, fact_id="count_delivered_msg")
# ---- ticket follow-through --------------------------------------------------------------------------------------
slot("W4", f"{tk('Refrigerator')} (Refrigerator) to Todo", 3, INT, "applies that line's Owed call to its own ticket", "delivery",
     ["delivery", "tracker_state", "Todo$"], "core", ["EXPORT"], ASK_SPAN, fact_id="todo_refrigerator")
for sid, mech, rx, why in (
    ("K1", "EXPORT", r"ascii|binary|text (?:kind|format|file)", "a comment carries what is owed for the lines saved out of the project"),
    ("K2", "ARTHOLD", r"UV|unwrap", "a comment carries what is owed for the bathroom lines"),
    ("K3", "REVISED", r"new colou?r|recolou?r|colou?r version|current file|model changed", "a comment carries what is owed for the three changed lines"),
    ("K4", "ZIP", r"unpack|zip (?:it |them |the files )?again|re-?zip|cut off|corrupt", "a comment carries what is owed for the instruments in Friday's zip"),
    ("K5", "AUDIO", r"own version|librar|licen|Soundly", "a comment carries what is owed for the two cues")):
    slot(sid, f"ticket comment: {mech.lower()} lines", 3, INT, why, "write_content", ["text", "comments", rx], "sample", [mech], ASK_SPAN, group="comment")
# ---- the brief --------------------------------------------------------------------------------------------------
slot("B1", "brief: the eight on the board", 5, MS, "Robert's 25 Sep eight as changed by his 26 Sep reply (the bow in, the last item out)", "write_content",
     ["text", "brief", "Shuriken.{0,160}Bow|Bow.{0,160}Shuriken"], "core", ["PICKS"], ASK_SPAN, fact_id="default_eight")
slot("B2", "brief: the scenario", 3, INT, "Frederick chose Scenario 1 on 15 Sep in the PlayableX channel", "write_content",
     ["text", "brief", "Scenario 1"], "core", [], ASK_SPAN, fact_id="scenario")
slot("B2b", "brief: what the scenario is for", 3, INT, "Frederick's 12 Sep reasoning: filter for players who will like the game, true to the core game play",
     "write_content", ["text", "brief", "filter|retention|core game ?play|core mechanic"], "core", [], ASK_SPAN, fact_id="scenario_purpose")
slot("B3", "brief: four zombies and the animation", 3, INT, "Robert's 29 Sep answer to PlayableX's question: walk; Party Girl, Plumber, Magician, Football Player",
     "write_content", ["text", "brief", "Plumber.{0,200}walk|walk.{0,200}Plumber"], "core", [], ASK_SPAN, fact_id="zombies_anim")
slot("B4", "brief: tray size", 3, INT, "the design page says a 7-slot tray; the 6-slot proposal in its comments was not adopted", "write_content",
     ["text", "brief", "(?:7|seven)[ -]?(?:slot|item|space)|tray.{0,40}(?:7|seven)"], "core", [], ASK_SPAN, fact_id="tray")
slot("B4b", "brief: how a level is lost", 3, INT, "the design page and Brian's 24 Sep note to PlayableX: lost when the zombies take our health to zero",
     "write_content", ["text", "brief", "HP|health"], "core", [], ASK_SPAN, fact_id="lose_rule")
slot("B5", "brief: start date", 1, LOOK, "the hub names 3 November", "write_content",
     ["text", "brief", "3 Nov|Nov(?:ember)? 3|3rd of November|2025-11-03"], "core", [], ASK_SPAN, fact_id="start_date")
slot("B6", "brief: what they can use for sound", 5, MS, "the notes' rule applied to Calvin's sheet: the rocket and explosion cues are held back", "write_content",
     ["text", "brief", "(?:rocket|explosion).{0,160}(?:own version|not ours|librar|licen|held back|stays? (?:here|with us)|replac)"],
     "core", ["AUDIO"], ASK_SPAN, fact_id="sound_section")
slot("B7", "brief: music after the first click", 3, INT, "what PlayableX told us about sound on the first playable (14 Apr)", "write_content",
     ["text", "brief", "first (?:click|tap|touch|interaction)"], "core", [], ASK_SPAN, fact_id="first_click")
# ---- delivery ---------------------------------------------------------------------------------------------------
slot("D1", "reply in Frederick's DM", 1, LOOK, "reply where he asked", "delivery", ["delivery", "slack_channel_post", M.DM_FRED, ""], "core", [], ASK_SPAN)
slot("D2", "post in the PlayableX channel", 1, LOOK, "the channel the ask names", "delivery", ["delivery", "slack_channel_post", M.VENDOR_CH, ""], "core", [],
     CH_SPAN)
slot("D4", "hand-off list shared for viewing", 1, LOOK, "the notes: both files, view only", "delivery", ["delivery", "share_reader"], "core", [], DRIVE_SPAN)
slot("D5", "both files shared with PlayableX's intake address", 1, LOOK, "the notes name the address in Contacts", "delivery",
     ["text", "shares", "intake@playablex\\.ai.*intake@playablex\\.ai"], "core", [], DRIVE_SPAN, fact_id="intake_share")
slot("D6", "the list's link posted", 1, LOOK, "both links go in the PlayableX channel", "delivery", ["link", "slack"], "core", [], CH_SPAN, fact_id="link_posted")

surface = {
    "kind": "GRADABLE_SURFACE", "version": 1, "task": M.SLUG, "revision": "D2-design",
    "truth_keys": KEYS, "classes": ["Delivered", "Ready", "Owed"],
    "truth_fields": {"class": "State", "groups": "groups"},
    "deliverables": {
        "handoff": {"kind": "table", "name_regex": "(?!.*brief).*(?:hand.?off|list|sheet|status|tracker|register|pack|asset|owed|deliverable)",
                    "key_column": "Line", "key_regex": "ZZ\\d|" + "|".join(re.escape(k) for k in KEYS),
                    "columns": ["Line", "Category", "Board set", "State", "What's owed", "Who has it", "Ticket", "Kind", "Went out", "Notes", "Extra 1", "Extra 2"],
                    "class_column": "State", "reason_column": "What's owed",
                    "comparators": {"State": "norm", "Board set": "norm", "Category": "norm", "Who has it": "issue_key", "Ticket": "issue_key"}},
        "ticket": {"kind": "text", "tool": "linear_update_issue", "issue": tk("Refrigerator"), "key_regex": "DES-\\d{3}"},
        "brief": {"kind": "json_text", "tool": "gdocs_create_document"},
        "comments": {"kind": "json_text", "tool": "linear_create_comment"},
        "shares": {"kind": "json_text", "tool": "gdrive_share_file"}},
    "slots": slots}
out = WF / "01_Gradable_Surface.json"
out.write_text(json.dumps(surface, indent=1, ensure_ascii=False) + "\n")
by = {}
for s in slots:
    for m in s["mechanisms"] or ["-"]: by[m] = by.get(m, 0) + s["weight"]
print("slots", len(slots), "weight", sum(s["weight"] for s in slots), "->", out.name, "| weight touched per mechanism", by)
