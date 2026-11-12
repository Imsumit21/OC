#!/usr/bin/env python3
"""Rubric repair after /rubric round 1 (eval_reports/6aea4c201e1fa1ddfdd0a25d_3_rubric.md, FAIL, score 1).

Applies the report's Fix List to the export it reviewed (plan/rubric/09_Rubrics.rubric_round1_reviewed.json,
sha256 1c44f4af…) and writes <task>/09_Rubrics.json plus plan/rubric/fix_round1_map.json (per new row: the reviewed
row it comes from, the plan tag, the part of a split row and the kind of change).

Repair protocol (GEN_EXECUTION §8): titles and weights are the report's, pasted unchanged; every row the report does
not list keeps its bytes; the only other edits are the evidence changes the report states, the kind-of-work label of a
row whose weight moved, and a Reject line that quoted a title the report replaced. Re-running is idempotent: the input
is the reviewed copy, never the current export."""
import hashlib
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
TASK = WF.parent
sys.path.insert(0, str(WF / "oe_gen"))
import model as O  # noqa: E402

REVIEWED_SHA = "1c44f4afdac193c101b93484db81af719349703251a5e38fd8776b0cb51b5b92"
raw = (HERE / "09_Rubrics.rubric_round1_reviewed.json").read_bytes()
assert hashlib.sha256(raw).hexdigest() == REVIEWED_SHA, "not the export /rubric round 1 reviewed"
old = json.loads(raw)
plan = json.loads((HERE / "rows.json").read_text())
assert len(old) == len(plan) == 126
BY_T = {l["ticket"]: l for l in O.BY.values()}
FULL = {"Brian": "Brian Foster", "Claire": "Claire Morgan", "Calvin": "Calvin Price"}
NOTES_WHO = (f"the notes {O.NOTES_ID} ('For an Owed line say what is owed, and who has it, meaning whoever has to do "
             f"the next thing.')")
MARCUS = "Marcus's post C0880U9751A/1758906517.912099"
ROBERT = "Robert's note D05GU6L0XFH/1759178332.042459"
LOG = "Brian's log f_faf4d7c167d14a1127dcc3"
SHEET = "Calvin's sheet f_b2387e31d46d3a7b3fa2a9"
FORMATS = ("PlayableX's rule C08H78VJG80/1758022459.227279 ('*3D assets*: .fbx, .glb, or .blend (when exporting .fbx, "
           "please make sure it’s exported in *Binary format*, not ASCII)')")
assert "whoever has to do the next thing" in O.NOTES["body_text"]
assert "youll need to redo them" in O.A1["text"] and "is redoing the UVs on the bathroom objects" in O.A2["text"]
assert "I'll put them back when we pick this up again." in O.LOG["body_text"]
assert ["Rocket sound", "Soundly library (Robert's seat)", "no", "not made yet, Calvin"] in O.SOUND_GRID

DELETE = {21, 22, 32, 34, 35, 36, 38, 39, 40, 41, 43}

# ---- titles, pasted from the Fix List (rows whose title the report replaces) --------------------------------------
TITLE = {
    2: "The Agent names Scenario 1 in its brief as the scenario picked for the playable",
    3: ("The Agent states the playable's purpose in its brief as testing the game as it is today with the players who "
        "will like it (Frederick's 'filtering out the players that won't like our game, while remaining true to our "
        "core game play' or Robert's 'test the current form and audience fit' each counts)"),
    4: "The Agent lists Grenade in its brief among the eight items on the board",
    5: "The Agent lists Couch in its brief among the eight items on the board",
    6: "The Agent lists Plushie Chick in its brief among the eight items on the board",
    7: "The Agent lists Shuriken in its brief among the eight items on the board",
    8: "The Agent lists Cute Axe in its brief among the eight items on the board",
    9: "The Agent lists Gift Box in its brief among the eight items on the board",
    10: "The Agent lists Cactus Plant in its brief among the eight items on the board",
    11: "The Agent lists the Bow in its brief among the eight items on the board",
    12: "The Agent states in its brief that every other board item on Brian's pack list is an extra PlayableX can swap in",
    13: "The Agent names Party Girl in its brief as one of the four zombies",
    14: "The Agent names Plumber in its brief as one of the four zombies",
    15: "The Agent names Magician in its brief as one of the four zombies",
    16: "The Agent names Football Player in its brief as one of the four zombies",
    17: "The Agent names walk in its brief as the one animation",
    18: "The Agent states in its brief that a level is won when every zombie on screen is eliminated",
    19: ("The Agent gives our health (HP) running out as the brief's only way to lose a level (the zombies getting to "
         "us and draining it, or simply zero health, both count; the word 'only' need not appear)"),
    20: "The Agent states in its brief that the tray has 7 slots",
    23: "The Agent lists the Matching sound in its brief among the sounds PlayableX can use",
    24: "The Agent lists the Success sound in its brief among the sounds PlayableX can use",
    25: "The Agent lists the Failure sound in its brief among the sounds PlayableX can use",
    26: ("The Agent states in its brief that the music may start only after the player's first click or tap (a first "
         "touch or other first interaction also counts)"),
    27: "The Agent gives the start date in its brief as November 3, 2025 (November 3 without the year also counts)",
    29: "The Agent gives its hand-off list the columns Line, Category, Board set, State, What's owed, Who has it and Ticket",
    30: "The Agent writes 96 data rows into its hand-off list",
    31: "The Agent gives Refrigerator (DES-367) the State 'Owed' in its hand-off list",
    33: "The Agent gives Bathtub (DES-349) the State 'Owed' in its hand-off list",
    37: "The Agent gives Chainsaw (DES-323) the State 'Ready' in its hand-off list",
    42: "The Agent gives Rolling Pin (DES-371) the State 'Ready' in its hand-off list",
    44: ("The Agent records in its hand-off list that what is owed for Refrigerator (DES-367) is a new binary FBX "
         "export (a re-export, .glb or .blend also counts)"),
    45: "The Agent records in its hand-off list that what is owed for Bathtub (DES-349) is the file again once the UVs are redone",
    46: "The Agent records in its hand-off list that what is owed for Cello (DES-380) is the file put back in the outgoing folder",
    47: "The Agent records in its hand-off list that what is owed for Rocket sound (DES-402) is our own version of the sound",
    48: "The Agent names Brian in its hand-off list as who has Refrigerator (DES-367)",
    49: "The Agent names Claire in its hand-off list as who has Bathtub (DES-349)",
    50: "The Agent names Claire in its hand-off list as who has Iron (DES-352)",
    51: "The Agent names Calvin in its hand-off list as who has Rocket sound (DES-402)",
    52: "The Agent names Brian in its hand-off list as who has Cello (DES-380)",
    53: "The Agent gives Bow (DES-335) the Board set 'Default' in its hand-off list",
    54: "The Agent gives Dynamite (DES-326) the Board set 'Extra' in its hand-off list",
    55: "The Agent gives Grenade (DES-322) the Board set 'Default' in its hand-off list",
    56: "The Agent gives Rolling Pin (DES-371) the Board set 'Extra' in its hand-off list",
    57: "The Agent gives the Cannon row the Ticket DES-398 in its hand-off list",
    58: "The Agent gives the Iron row the Category Bathroom in its hand-off list",
    64: "The Agent moves exactly 49 tickets under Brian's pack ticket DES-313 to Todo",
}

# ---- weights the report moves, with the kind-of-work label that goes with the new band -----------------------------
WEIGHT = {2: 1, 18: 1, 26: 1, 30: 1, 48: 1, 49: 1, 50: 1, 51: 1, 52: 1, 55: 1, 56: 1, 59: 5, 60: 5, 61: 5, 122: 5, 123: 5}
JUST = {
    2: "Lookup: one literal from Frederick's reply that makes the pick ('lets go with Scenario 1.').",
    18: "Lookup: one literal, stated in Brian's message to PlayableX and on the deck.",
    26: "Lookup: one literal, PlayableX's rule from the first playable ('music has to start after first click as a rule').",
    30: "Lookup: the row count of the Pack tab of Brian's pack list.",
    48: "Lookup: the deciding record names the holder (Marcus's post tells Brian 'youll need to redo them').",
    49: "Lookup: the deciding record names the holder (Robert's note: Claire 'is redoing the UVs on the bathroom objects').",
    50: "Lookup: the deciding record names the holder (Robert's note: Claire 'is redoing the UVs on the bathroom objects').",
    51: "Lookup: the deciding record names the holder (Calvin's sheet: 'not made yet, Calvin').",
    52: "Lookup: the deciding record names the holder (Brian's log: 'I'll put them back when we pick this up again.').",
    55: "Lookup: Grenade is on Robert's list of the eight.",
    56: "Lookup: Rolling Pin is a board item that is not on Robert's list of the eight.",
    59: f"Multi-source: the move rests on the same join as the line's State ({MARCUS} against the line's own note).",
    60: f"Multi-source: the move rests on the same join as the line's State ({ROBERT} against the line's own note).",
    61: f"Multi-source: the move rests on the same join as the line's State ({LOG} against the line's own note).",
    64: "Multi-source: the count needs the full audit of all 96 lines.",
    122: "Multi-source: the count needs the full audit of all 96 lines.",
    123: "Multi-source: the count needs the full audit of all 96 lines.",
}

# ---- evidence edits: (text in the reviewed evidence, replacement); each must match exactly once --------------------
EVID = {
    2: [("so 'The Agent's brief names Scenario 1' fails", "so the Scenario 1 row fails")],
    3: [("Expected: filtering out the players that won't like our game; true to our core game play; current form and "
         "audience fit.",
         "Expected: the playable tests the game as it is today with the players who will like it, in Frederick's "
         "wording ('filtering out the players that won't like our game, while remaining true to our core game play') "
         "or Robert's ('test the current form and audience fit')."),
        ("Accept: 'Scenario 1 tests the game in its current form with the players who'll like it, true to the core "
         "game' (also accepted: any wording of that one purpose).",
         "Accept: either wording, or a paraphrase of it: 'Scenario 1 tests the game in its current form with the "
         "players who'll like it, true to the core game' passes."),
        ("Reject: no brief exists, so the purpose row fails; a more hardcore-friendly playable; Julia's 'more "
         "hardcore friendly playable': a brief giving it as the purpose fails.",
         "Reject: no brief exists, so the purpose row fails; a hardcore-friendly or tailored version given as the "
         "purpose (Julia's 'more hardcore friendly playable').")],
    11: [("Expected: Bow in place of Dynamite.", "Expected: Bow among the eight."),
         ("Robert's Sep 25 list with Dynamite: a brief keeping Dynamite fails.",
          "Robert's Sep 25 list as it stood: a list of the eight without the Bow fails.")],
    19: [("Accept: 'You lose when the zombies get to you and your HP runs out; a full tray is a blunder, not a loss'.",
          "Accept: 'You lose when the zombies get to you and your HP runs out; a full tray is a blunder, not a loss' "
          "(also accepted: 'the level is lost only at zero health'; the same one condition without the word 'only')."),
         ("a full tray as a loss.", "a full tray given as a loss.")],
    29: [("close equivalents ('What is owed')", "'What is owed' for 'What's owed'")],
    30: [("Accept: 96 rows in any order, Line spelled as on Brian's list.", "Accept: 96 rows in any order.")],
    44: [("Expected: Refrigerator What's owed binary FBX export.", "Expected: Refrigerator What's owed a new binary FBX export."),
         ("PlayableX's rule C08H78VJG80/1758022459.227279 ('please make sure it’s exported in *Binary format*, not ASCII')",
          FORMATS),
         ("with What's owed binary FBX export (also accepted: export again as binary FBX; a binary re-export).",
          "with What's owed a new binary FBX export (also accepted: export again as binary FBX; a binary re-export; a "
          "re-export; a .glb or .blend file)."),
         ("an answer naming the ASCII/text kind.",
          "an entry saying the current FBX can go as it is, or that the FBX from Claire is owed.")],
    46: [("(also accepted: re-upload; re-zip or send the eight again; the zip won't unpack)",
          "(also accepted: re-upload; re-zip or send the eight again)")],
    47: [("an answer naming the library or bought-pack file.", "an entry saying the library sound itself can be handed over.")],
    64: [("Expected: 49 moves; template: one state change to Todo per Owed line (the notes); the Delivered and Ready "
          "tickets keep their state.",
          "Expected: 49 moves. This is the volume row of the move group (template: one state change to Todo per Owed "
          "line, from the notes); the five move rows on DES-367, DES-349, DES-380, DES-321 and DES-409 are its samples."),
         ("Accept: the 49 Owed tickets in Todo, in any order.", "Accept: exactly 49 tickets under DES-313 in Todo, in any order."),
         ("Reject: an idle run moves no ticket, so the volume row fails.",
          "Reject: an idle run moves no ticket, so the volume row fails; fewer or more than 49 tickets moved.")],
}
for n, name in zip(range(4, 11), ["Grenade", "Couch", "Plushie Chick", "Shuriken", "Cute Axe", "Gift Box", "Cactus Plant"]):
    EVID[n] = [(f"so 'lists {name} among the eight' fails", f"so the {name} row fails")]


def sub(text, a, b, where):
    assert text.count(a) == 1, f"{where}: expected one match of {a!r}, found {text.count(a)}"
    return text.replace(a, b)


def tail(e):
    m = re.search(r"OE [\d, ]+\.$", e)
    assert m, e[-80:]
    return m.group()


def split_comment(n, row):
    """One reviewed comment row → (owed row, weight 5) + (holder row, weight 1), per the Fix List."""
    t = re.search(r"DES-\d+", row["title"]).group()
    l = BY_T[t]
    cls, who, name, e = l["cls"], l["who"], l["name"], row["evidence"]
    w = f"R{n}"
    assert f"({name})" in row["title"] and row["weight"] == 3
    e = sub(e, f"; who has it: {who}.", ".", w)
    if cls == "A1":
        owed_title = f"The Agent comments on {t} ({name}) that a new binary FBX export is owed (a re-export, .glb or .blend also counts)"
        e = sub(e, "what is owed: binary FBX export.", "what is owed: a new binary FBX export.", w)
        e = sub(e, f"Source: {MARCUS};",
                f"Source: {MARCUS} ('the text kind, the setting was wrong that day so youll need to redo them') with {FORMATS};", w)
        e = sub(e, f"'A binary fbx export is owed; {who} has it' (also accepted: export again as binary FBX; a binary re-export).",
                "'A new binary FBX export is owed' (also accepted: export again as binary FBX; a binary re-export; a "
                "re-export; a .glb or .blend file).", w)
        e = sub(e, "an answer naming the ASCII/text kind.",
                "a comment saying the current file is fine or that the FBX from Claire is owed.", w)
        owed_just = f"Multi-source: what is owed follows from {MARCUS} with PlayableX's format rule, against the line's own note."
        decider = f"{MARCUS} ('youll need to redo them', said to Brian)"
    elif cls == "A2":
        owed_title = f"The Agent comments on {t} ({name}) that the file is owed again once the UVs are redone"
        e = sub(e, f"'The file is owed again once the uvs are redone; {who} has it'", "'The file is owed again once the UVs are redone'", w)
        owed_just = f"Multi-source: what is owed follows from {ROBERT}, against the line's own note."
        decider = f"{ROBERT} ('is redoing the UVs on the bathroom objects', said of Claire)"
    elif cls == "C4":
        owed_title = f"The Agent comments on {t} ({name}) that the file is owed back in the outgoing folder"
        e = sub(e, f"'The file is owed back in the outgoing folder; {who} has it' (also accepted: re-upload; re-zip or send "
                   "the eight again; the zip won't unpack).",
                "'The file is owed back in the outgoing folder' (also accepted: re-upload; re-zip or send the eight again).", w)
        owed_just = f"Multi-source: what is owed follows from {LOG}, against the line's own note."
        decider = f"{LOG} ('I still have Claire's files, I'll put them back when we pick this up again.')"
    elif cls == "C2":
        owed_title = f"The Agent comments on {t} ({name}) that our own version of the sound is owed"
        e = sub(e, f"'Our own version of the sound is owed; {who} has it' (also accepted: a replacement made here).",
                "'Our own version of the sound is owed', with or without the library or pack named as the reason (also "
                "accepted: a replacement made here).", w)
        e = sub(e, "an answer naming the library or bought-pack file.", "a comment saying the current sound can be handed over.", w)
        owed_just = f"Multi-source: what is owed follows from {SHEET} with the notes' sound rule, against the line's own note."
        decider = f"{SHEET} ('not made yet, Calvin' under 'Replacement')"
    else:
        raise AssertionError((n, cls))
    owed = {"title": owed_title, "category": "Outcome", "weight": 5, "justification": owed_just, "evidence": e}
    holder = {
        "title": f"The Agent names {who} as who has it in its comment on {t} ({name})",
        "category": "Outcome", "weight": 1,
        "justification": "Lookup: the notes give the holder as whoever has to do the next thing, and the deciding record names that person.",
        "evidence": (f"Expected: {t}; who has it: {who}. Source: {NOTES_WHO}; {decider}; Brian's note on {t} ('{l['note']}'). "
                     f"Accept: a comment by Julia on {t} that names {who} as who has it: '{who} has it' (also accepted: "
                     f"{who} ({FULL[who]})). Reject: an idle run adds no comment, so the {t} holder row fails; a comment on "
                     f"{t} that names someone else, or nobody, as who has it. {tail(row['evidence'])}"),
    }
    return owed, holder


def new_rows_after(n):
    """Rows the Fix List adds after reviewed row n: (part, criterion)."""
    if n == 42:
        l = BY_T["DES-334"]
        assert l["name"] == "Plushie Chick" and l["state"] == "Delivered"
        return [("state_delivered", {
            "title": "The Agent gives Plushie Chick (DES-334) the State 'Delivered' in its hand-off list",
            "category": "Outcome", "weight": 3,
            "justification": "Interpretation: the notes' state tests applied to the line's own note, which says this line is "
                             "the one PlayableX called the duck.",
            "evidence": (f"Expected: Plushie Chick State Delivered. Source: the notes {O.NOTES_ID} ('Delivered: PlayableX has "
                         f"the current file and can use it.'); Brian's note on DES-334 ('{l['note']}'). Accept: a row "
                         "'Plushie Chick' with State Delivered (also accepted: the state word in any case). Reject: no "
                         "spreadsheet exists, so the Plushie Chick State row fails; Ready or Owed on that row. OE 5, 22."),
        })]
    if n == 56:
        l = BY_T["DES-398"]
        assert l["name"] == "Cannon" and l["kind"] == "Weapon" and l["board"] == ""
        return [("board_empty", {
            "title": "The Agent gives the Cannon (DES-398) row an empty Board set in its hand-off list",
            "category": "Outcome", "weight": 1,
            "justification": "Lookup: the pack list gives Cannon the Kind 'Weapon', and the notes leave Board set empty "
                             "for anything that isn't a board item.",
            "evidence": (f"Expected: Cannon Board set empty. Source: the notes {O.NOTES_ID} ('Board set is Default for the "
                         "eight on the board and Extra for every other board item; leave it empty for anything that isn't a "
                         f"board item.'); the Pack tab of {O.PACK_ID} (the Cannon row's Kind is 'Weapon'). Accept: a row "
                         "'Cannon' whose Board set cell is empty. Reject: no spreadsheet exists, so the Cannon Board set "
                         "row fails; 'Default' or 'Extra' on the Cannon row. OE 2, 3, 22."),
        })]
    if n == 126:
        ask = f"Frederick's ask {O.ASK['id']} ('post both links in the PlayableX channel so they know what's still coming from us')"
        out = []
        for part, what, its, oes in (("order_brief", "the brief", "the brief's", "20, 130"),
                                     ("order_list", "the hand-off list", "the hand-off list's", "21, 22, 130")):
            out.append((part, {
                "title": f"The Agent finishes writing {what} before it posts {its} link in the PlayableX channel ({O.VENDOR_CH})",
                "category": "Process", "weight": 1,
                "justification": ("Lookup: the prompt states the order ('once they're ready the links go in the PlayableX "
                                  "channel'). The finished file and the post do not show which came first, every valid "
                                  "path writes the file before it posts the link, and the order is a property of how the "
                                  "work is done, not one tool call."),
                "evidence": (f"Expected: {what} is written before the channel message that carries its link. Source: the "
                             "prompt ('once they're ready the links go in the PlayableX channel like he says'); "
                             f"{ask}. Accept: the content of {what} is in place before the message with its link is sent in "
                             f"{O.VENDOR_CH} (also accepted: both links in one message or in two; the shares made before or "
                             f"after the post). Reject: an idle run writes no file and posts no link, so the ordering row "
                             f"fails; the link posted while {what} is still empty or still being written. OE {oes}."),
            }))
        return out
    return []


SPLIT_CLS = {"A1", "A2", "C4", "C2"}
out, meta = [], []
for n, (row, p) in enumerate(zip(old, plan), 1):
    assert p["P"] == f"P{n}"
    base = {"from": f"R{n}", "tag": p["tag"], "decided": p["decided"], "slot": p.get("slot") or []}
    if n in DELETE:
        meta.append({**base, "new": None, "change": "deleted"})
        continue
    is_comment = p["tag"].startswith("comment_")
    if is_comment and BY_T[p["tag"][len("comment_"):]]["cls"] in SPLIT_CLS:
        owed, holder = split_comment(n, row)
        out.append(owed)
        meta.append({**base, "new": f"R{len(out)}", "part": "owed", "change": "split"})
        out.append(holder)
        meta.append({**base, "new": f"R{len(out)}", "part": "holder", "change": "split"})
        continue
    new = dict(row)
    changed = []
    if n in TITLE:
        assert new["title"] != TITLE[n]
        new["title"] = TITLE[n]
        changed.append("title")
    if n in WEIGHT:
        assert new["weight"] != WEIGHT[n]
        new["weight"] = WEIGHT[n]
        changed.append("weight")
    if n in JUST:
        new["justification"] = JUST[n]
        changed.append("justification")
    for a, b in EVID.get(n, []):
        new["evidence"] = sub(new["evidence"], a, b, f"R{n}")
        if "evidence" not in changed:
            changed.append("evidence")
    out.append(new)
    meta.append({**base, "new": f"R{len(out)}", "change": "+".join(changed) if changed else "unchanged"})
    for part, crit in new_rows_after(n):
        out.append(crit)
        meta.append({"from": None, "after": f"R{n}", "tag": f"new_{part}", "decided": "—", "slot": [], "new": f"R{len(out)}",
                     "part": part, "change": "added"})

# ---- checks ---------------------------------------------------------------------------------------------------------
assert set(TITLE) | set(WEIGHT) | set(JUST) | set(EVID) <= set(range(1, 127)) - DELETE
split = sorted({int(m["from"][1:]) for m in meta if m["change"] == "split"})
assert split == [65, 66, 67] + list(range(73, 85)) + list(range(86, 95)) + list(range(97, 105)) + [108, 109], split
keep = [1, 28, 62, 63, 68, 69, 70, 71, 72, 85, 95, 96, 105, 106, 107, 110, 111, 112, 113, 124, 125, 126] + list(range(114, 122))
same = sorted(int(m["from"][1:]) for m in meta if m["change"] == "unchanged")
assert same == sorted(keep), (same, sorted(keep))
for m in meta:                                       # an untouched row keeps its bytes
    if m["change"] == "unchanged":
        assert out[int(m["new"][1:]) - 1] == old[int(m["from"][1:]) - 1]
assert len(out) == 153 and sum(c["category"] == "Process" for c in out) == 2
assert all(set(c) == {"title", "category", "weight", "justification", "evidence"} for c in out)
assert all(c["weight"] in (1, 3, 5) and c["category"] in ("Outcome", "Process") for c in out)
assert all(all(str(c[k]).strip() for k in c) for c in out)
assert not any(c["title"].startswith("The Agent's") for c in out)
assert len({c["title"] for c in out}) == len(out)
assert not any(x in " ".join(map(str, c.values())) for c in out for x in ("e.g.", "such as", "for example"))
report = (TASK / "eval_reports" / "6aea4c201e1fa1ddfdd0a25d_3_rubric.md").read_text()
fixlist = report[report.index("## Fix List"):report.index("### Phase 1")]
for m in meta:                                       # every new or changed title is the report's text, verbatim
    if m["change"] in ("unchanged", "deleted") or "title" not in m["change"] and m["change"] not in ("split", "added"):
        continue
    t = out[int(m["new"][1:]) - 1]["title"]
    assert f'"{t}"' in fixlist, f"not in the Fix List: {t}"

(TASK / "09_Rubrics.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
(HERE / "fix_round1_map.json").write_text(json.dumps(meta, indent=1, ensure_ascii=False) + "\n")
w = [c["weight"] for c in out]
print(f"wrote 09_Rubrics.json: {len(out)} criteria (Outcome {sum(c['category'] == 'Outcome' for c in out)}, Process "
      f"{sum(c['category'] == 'Process' for c in out)}) · weight {sum(w)} (5 ×{w.count(5)} · 3 ×{w.count(3)} · 1 ×{w.count(1)})")
print("sha256", hashlib.sha256((TASK / "09_Rubrics.json").read_bytes()).hexdigest())
kinds = {}
for m in meta:
    kinds[m["change"]] = kinds.get(m["change"], 0) + 1
print("changes:", ", ".join(f"{k} {v}" for k, v in sorted(kinds.items())))
