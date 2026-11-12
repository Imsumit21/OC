#!/usr/bin/env python3
"""Design model for julia_zm3d_playable_brief (scenario stage, design D1).

Single source of truth for the cohort, the units, the planned records and their minted ids. build_scenario.py turns it
into the draft manifest, the gradable surface, the difficulty budget and the design tables. Nothing here is SQL and no
prompt, Oracle Event or criterion text is written here. Base ids are real synth-cut records read through tools/hg.py;
planned (seeded) ids are minted below and collision-checked by check_ids.py.
"""
import hashlib, uuid

SLUG = "julia_zm3d_playable_brief"
PERSONA = "julia_lawson"

# ---------------------------------------------------------------- base records (read this session)
VENDOR_CH = "C08H78VJG80"          # PlayableX shared channel (private, Julia member)
DESIGN_CH = "C090N54TG79"          # #zombie-design
ART_CH = "C08R8CHB0QL"             # #zombie-art
BUGS_CH = "C08R27X0EAH"            # #zombie-bugs
DM_FRED = "D05SD5QLG94"            # Julia - Frederick
DM_CLAIRE = "D05HMBQUC8Z"          # Julia - Claire
BASE = {
    "vendor_asset_list": f"{VENDOR_CH}/1758283671.878269",     # 2025-09-19 P6078: assets expected, by group
    "vendor_formats": f"{VENDOR_CH}/1758022459.227279",        # 2025-09-16 P6078: 8-item set, editable items, Spine
    "vendor_zombie_ask": f"{VENDOR_CH}/1759140968.965099",     # 2025-09-29 P6078: primary animation + 4 zombies
    "vendor_duck": f"{VENDOR_CH}/1758723504.085039",           # 2025-09-24 P6078: only the duck asset missing
    "brian_zip1": f"{VENDOR_CH}/1758717576.077489",            # 2025-09-24 12:39 Brian: assets zip
    "brian_zip2": f"{VENDOR_CH}/1758729487.922339",            # 2025-09-24 15:58 Brian: Plushie-and-zombies.zip
    "brian_pack3": f"{VENDOR_CH}/1758906043.375719",           # 2025-09-26 17:00 Brian: zombies Unity pack
    "brian_winfail": f"{VENDOR_CH}/1758717625.209649",         # 2025-09-24 Brian: sample level, win/fail condition
    "vendor_blank_scene": f"{VENDOR_CH}/1758808234.045839",    # 2025-09-25 P6078: test the package in a blank project
    "fred_scenario1": f"{VENDOR_CH}/1757956024.883249",        # 2025-09-15 Frederick: Scenario 1; grenade, couch, plush doll
    "fred_pause": f"{VENDOR_CH}/1759174925.309129",            # 2025-09-29 19:42 Frederick: pause for a month or so
    "vendor_nov3": f"{VENDOR_CH}/1759226395.551469",           # 2025-09-30 09:59 P6078: new start 3 November
    "vendor_oct6": f"{VENDOR_CH}/1758701898.919999",           # 2025-09-24 P6078: start moved to 6 October
    "vendor_music_rule": f"{VENDOR_CH}/1744637266.363689",     # 2025-04-14 P6073: music starts after first click
    "vendor_fbx_march": f"{VENDOR_CH}/1742892985.601399",      # 2025-03-25 P6073: everything in fbx (Domino Delights round)
    "julia_dd_brief": f"{VENDOR_CH}/1741963515.221549",        # 2025-03-14 Julia: storyboard / brief for the first playable
    "brian_asks_level": f"{DESIGN_CH}/1758568735.563539",      # 2025-09-22 Brian asks Julia for the reference level
    "playable_thread": f"{DESIGN_CH}/1758567201.262949",       # 2025-09-22 playable scenario thread root (26 replies)
    "julia_shuriken_idea": f"{DESIGN_CH}/1758569824.148029",   # 2025-09-22 Julia: grenades and shuriken idea
    "robert_remain": f"{DESIGN_CH}/1758569885.985319",         # 2025-09-22 Robert: remain as is
    "robert_current_form": f"{DESIGN_CH}/1758569655.409719",   # 2025-09-22 Robert: test the current form
    "leonard_priorities": f"{DESIGN_CH}/1758517286.431379",    # 2025-09-22 Leonard: priorities, pivot options
    "robert_new_colours": f"{DESIGN_CH}/1759189466.554739",    # 2025-09-29 23:44 Robert: new colored cactus, chainsaw, cones
    "art_cactus": f"{ART_CH}/1758752145.583769",               # 2025-09-24 22:15 Robert: colorized cactus plant
    "art_candy": f"{ART_CH}/1758752921.740419",                # 2025-09-24 22:28 Robert: Candy 1 texture atlas issue
    "art_cone": f"{ART_CH}/1758754866.994649",                 # 2025-09-24 23:01 Robert: colorized cone
    "art_dart": f"{ART_CH}/1758754916.837729",                 # 2025-09-24 23:01 Robert: dartboard colour
    "art_claire_pr": f"{ART_CH}/1758808937.107229",            # 2025-09-25 14:02 Claire: pushed the changes in new pr
    "art_bow_root": f"{ART_CH}/1758904025.123869",             # 2025-09-26 16:27 Julia: arrow to go with the bow (root)
    "pr462": "harmonygames-Games/match3d#462",                 # Objects Revisions and Changes, merged 2025-09-25T23:15:41Z
    "gdd": "page_zm3d_gdd",                                    # Confluence: 7-slot tray, loss only at zero health
    "gdd_c1": "comment_zm3d_gdd_c1", "gdd_c2": "comment_zm3d_gdd_c2",
    "playable_feedback_doc": "f_05bedd1540d3e01a90ab16",       # Leonard's Playable Feedback (Domino Delights round)
    "july_export": "f_7efae6c05be5c2414e8798",                 # ExportedLevelItems First Appearence (Robert, 2025-07-23)
    "trello_kickoff": "688c4d14c312a27fa2747e40",              # Playable Kickoff card (Leonard's board)
    "trello_playables": "67bdf36fa1136aff58740a55",            # Playables card, UA/BD board, Not Started
    "julia_root": "d_8140f09bf9f1b94cb8ee2d",                  # Julia's Drive root (owner)
    "art792": "ART-792",                                       # Frederick's marketing screenshots epic (precedent)
}

def h(label, n):
    return hashlib.sha256(("julia_zm3d_playable_brief|" + label).encode()).hexdigest()[:n]

COMMENT_NS = uuid.uuid5(uuid.NAMESPACE_URL, "hg-task/julia_zm3d_playable_brief")
def comment_id(label):
    """Linear comment ids are uuid5(namespace, name), the generators' linear.comment_uuid/1 convention."""
    return str(uuid.uuid5(COMMENT_NS, label))

def slack_id(channel, ts):
    return hashlib.sha256(f"{channel}|{ts}".encode()).hexdigest()[:32]

# ---------------------------------------------------------------- planned records (minted ids; UTC times)
SEED = {
    # hub and rules
    "ask": {"svc": "slack", "id": f"{DM_FRED}/1759255800.418239", "at": "2025-09-30T18:10:00Z", "by": "Frederick Stone",
            "what": "Frederick's DM to Julia: the job, its destinations, and the three things it starts from"},
    "notes": {"svc": "gdocs", "id": "f_" + h("notes", 22), "at": "2025-09-30T17:52:00Z", "by": "Frederick Stone",
              "what": "Frederick's hand-off notes (created 2025-09-26): what Delivered, Ready and Owed mean; current version; sound; tickets; sharing"},
    "tracker": {"svc": "gsheets", "id": "f_" + h("tracker", 22), "at": "2025-09-26T15:20:00Z", "by": "Brian Foster",
                "what": "Brian's pack list (created 2025-09-23): one row per line, set, delivery, ticket; no state column"},
    "picks": {"svc": "slack", "id": f"{DESIGN_CH}/1758646800.552319", "at": "2025-09-23T17:00:00Z", "by": "Robert",
              "what": "Robert's picks for the outside level: the eight board objects (root post in #zombie-design)"},
    "zpicks": {"svc": "slack", "id": f"{DESIGN_CH}/1759167000.736119", "at": "2025-09-29T17:30:00Z", "by": "Robert",
               "what": "Robert's answer to the vendor's question: walk as the primary animation; Chef, Bike Kid, Boxer, Mayor"},
    "ticket_parent": {"svc": "linear", "id": "ART-793", "at": "2025-09-19T16:30:00Z", "by": "Frederick Stone",
                      "what": "pack ticket (Team Epic, assigned Brian); children ART-794 to ART-890, one per line"},
    "deck": {"svc": "gslides", "id": "f_" + h("deck", 22), "at": "2025-09-23T19:50:00Z", "by": "Julia Lawson",
             "what": "Julia's reference-level deck: layout, the eight board objects as built, win and fail"},
    "hold": {"svc": "gcal", "id": "evt_" + h("hold_julia", 22), "at": "2025-09-30T17:40:00Z", "by": "Frederick Stone",
             "what": "kickoff hold Mon 3 Nov 2025 17:00 UTC; attendees Frederick, Julia, Brian, Robert (one row per calendar)"},
    "contact": {"svc": "contacts", "id": h("contact_playablex", 24), "at": "2025-09-19T16:40:00Z", "by": "Frederick Stone",
                "what": "PlayableX intake contact (outside partner): the address a view link is shared with"},
    "trello_note": {"svc": "trello", "id": "68dc207c" + h("trello_note", 16), "at": "2025-09-30T18:25:00Z", "by": "Leonard Hayes",
                    "what": "Leonard's comment on his Playable Kickoff card: parked until 3 November, Frederick and Julia are sorting the brief and the pack"},
    # deciding records of the units
    "a1_post": {"svc": "slack", "id": f"{BUGS_CH}/1758963900.284719", "at": "2025-09-27T09:05:00Z", "by": "Arthur Blake",
                "what": "A1: root post in #zombie-bugs: the object browser's new multi-select button writes empty shells; single export is fine"},
    "a2_dm": {"svc": "slack", "id": f"{DM_CLAIRE}/1758874200.613049", "at": "2025-09-26T08:10:00Z", "by": "Claire Morgan",
              "what": "A2: Claire's DM to Julia: she is redoing the UVs on the bathroom ones; what Brian pulled on Thursday is the old unwrap"},
    "c3_reply": {"svc": "slack", "id": f"{ART_CH}/1758906300.447189", "at": "2025-09-26T17:05:00Z", "by": "Robert",
                 "what": "C3: Robert's reply under Julia's bow thread: the bow replaces the iron on the board; six round objects are missing from Brian's list"},
    "c4_comment": {"svc": "linear", "id": comment_id("c4_comment"), "at": "2025-09-29T08:40:00Z", "by": "Brian Foster",
                   "what": "C4: Brian's comment on the pack ticket ART-793: the music set from Friday's export comes in grey in an empty scene"},
    "c2_sheet": {"svc": "gsheets", "id": "f_" + h("c2_sheet", 22), "at": "2025-09-26T13:30:00Z", "by": "Calvin Price",
                 "what": "C2: Calvin's sound source sheet: where each cue came from (made here / bought pack, in-game licence only)"},
}

# ---------------------------------------------------------------- the cohort (103 lines)
# cls: W = delivered and usable; READY = exported, current, nothing changing; VIS = owed, stated on the line's own ticket;
#      a unit id = owed, decided by that unit's record; ADD = not on Brian's list, added by Robert (owed, no ticket).
DELIVERED = [("Grenade", "W"), ("Couch", "W"), ("Iron", "W"), ("Shuriken", "W"), ("Bow", "W"), ("Cute Axe", "W"),
             ("Cute Hammer", "W"), ("Gift Box", "W"), ("Plushie Chick", "W"),
             ("Cactus Plant", "C1"), ("Chainsaw", "C1"), ("Traffic Cone", "C1")]
EXTRAS = {
    "Appliances and furniture": [(n, "A1") for n in ("Washing Machine", "Oven", "Refrigerator", "Toaster", "Coffee Machine", "Microwave",
                                                     "Stove", "Kitchen Mixer", "Ice Cream Machine", "Safe", "Ironing Board", "Square Table")],
    "Bathroom": [(n, "A2") for n in ("Bathroom Scale", "Bathtub", "Hair Dryer", "Wash Basin", "Wash Basin Cabinet", "Toilet",
                                     "Toilet Paper", "Plunger", "Wooden Hairbrush", "Electric Hair Trimmer", "Slippers", "Paper Towel")],
    "Music": [(n, "C4") for n in ("Acoustic Guitar", "Electric Guitar", "Cello", "Harp", "Trumpet", "Tambourine", "Cymbals", "Xylophone")],
    "Games": [("Dartboard", "C1"), ("Candy", "C1")],
    "Storage": [("Wooden Crate", "VIS"), ("Wooden Bucket", "VIS"), ("Large Barrel", "VIS"), ("GrandPiano", "VIS"), ("Wheelbarrow", "VIS")],
    "Kitchenware": [(n, "READY") for n in ("Rolling Pin", "Patterned Teapot", "Dutch Oven", "Round Pan", "Square Pan", "Spatula", "Whisk",
                                           "Round Kettle", "Small Kettle", "Tall Kettle", "Cup", "Mug", "Plate", "Fancy Plate", "Wine Bottle",
                                           "Milk Carton")],
    "Living room": [(n, "READY") for n in ("Armchair", "RetroTV", "Small Lamp", "Desk Lamp", "Alarm Clock", "Record Player", "Flower Pot",
                                           "Watering Can", "Dynamite", "Garden Shears", "Dice")],
}
ADDED = ["Soccer Ball", "Basketball", "Toy Drum", "Scooter", "Bicycle", "Toy Hammer"]
OTHER = [("Zombie Chef", "Zombie", "W"), ("Zombie Bike Kid", "Zombie", "W"), ("Zombie Boxer", "Zombie", "W"), ("Zombie Mayor", "Zombie", "W"),
         ("Cannon", "Weapon", "W"), ("Cannon shot", "Weapon", "W"),
         ("Tray", "UI", "W"), ("Monster HP bar", "UI", "W"), ("Item frame", "UI", "W"), ("Win and lose panels", "UI", "W"), ("Buttons", "UI", "VIS"),
         ("Board background", "Background", "VIS"),
         ("Match scale", "Sound", "C2"), ("Explosion", "Sound", "C2"), ("Cannon sound", "Sound", "READY"), ("Win stinger", "Sound", "READY"),
         ("Lose stinger", "Sound", "READY"), ("Music", "Sound", "VIS"),
         ("Fonts", "Font", "VIS")]
DEFAULT_PICKS = ["Grenade", "Couch", "Plushie Chick", "Iron", "Shuriken", "Cute Axe", "Cactus Plant", "Gift Box"]   # Robert, 23 Sep
DEFAULT_FINAL = ["Grenade", "Couch", "Plushie Chick", "Bow", "Shuriken", "Cute Axe", "Cactus Plant", "Gift Box"]    # after C3
ZOMBIES = ["Chef", "Bike Kid", "Boxer", "Mayor"]
PRIMARY_ANIMATION = "walk"
# Every line ticket is Done at the clock: Brian closed each one as he dealt with it (23-26 Sep) and left a note saying what he
# did. Workflow state therefore tells nothing about a line's state; the note on the ticket does.
TICKET_STATE = "Done"

VIS_REASON = {"Wooden Crate": ("prefab only, no model file exported", "Brian Foster"),
              "Wooden Bucket": ("prefab only, no model file exported", "Brian Foster"),
              "Large Barrel": ("prefab only, no model file exported", "Brian Foster"),
              "GrandPiano": ("not exported yet", "Brian Foster"), "Wheelbarrow": ("not exported yet", "Brian Foster"),
              "Buttons": ("flat PNG, parts not separated", "Brian Foster"),
              "Board background": ("PSD only, no PNG", "Brian Foster"),
              "Music": ("no track chosen for the ad", "Frederick Stone"),
              "Fonts": ("no font files yet", "Martin Walsh")}
UNIT_REASON = {"A1": ("re-export one at a time: the file sent to the outgoing folder is an empty shell", "Brian Foster"),
               "A2": ("art is being redone (UVs); the exported file is the old unwrap", "Claire Morgan"),
               "C1": ("the art changed after it went out (25 Sep); send the current version", "Brian Foster"),
               "C2": ("not ours outright (bought pack, in-game licence only); needs a cue we own", "Calvin Price"),
               "C4": ("the Friday export comes in without textures; needs another pass", "Brian Foster"),
               "ADD": ("not on the pack list; not exported yet", "Brian Foster")}

def lines():
    out = []; n = 0
    def add(name, kind, sset, delivery, cls):
        nonlocal n
        n += 1
        on_list = cls != "ADD"
        ticket = f"ART-{793 + n}" if on_list else None
        state = "Delivered" if cls == "W" else "Ready" if cls == "READY" else "Owed"
        reason, owner = (None, None)
        if cls == "VIS": reason, owner = VIS_REASON[name]
        elif cls not in ("W", "READY"): reason, owner = UNIT_REASON[cls]
        out.append({"n": n, "name": name, "kind": kind, "set": sset, "delivery": delivery, "cls": cls, "ticket": ticket,
                    "state": state, "owed": reason, "owner": owner, "on_list": on_list})
    for name, cls in DELIVERED:
        add(name, "Board object", "Outside level", "zip 24 Sep (2)" if name == "Plushie Chick" else "zip 24 Sep", cls)
    for sset, members in EXTRAS.items():
        for name, cls in members:
            add(name, "Board object", sset, "", cls)
    for name, kind, cls in OTHER:
        delivery = {"Zombie": "pack 26 Sep", "Weapon": "zip 24 Sep"}.get(kind, "zip 24 Sep" if (kind == "UI" and cls == "W") else "")
        add(name, kind, kind, delivery, cls)
    for name in ADDED:
        add(name, "Board object", "(added by Robert)", "", "ADD")
    return out

LINES = lines()
BY_NAME = {l["name"]: l for l in LINES}
def members(cls): return [l for l in LINES if l["cls"] == cls]
COUNTS = {s: sum(1 for l in LINES if l["state"] == s) for s in ("Delivered", "Ready", "Owed")}
NAIVE = {"Delivered": sum(1 for l in LINES if l["on_list"] and l["delivery"]),
         "Owed": len(members("VIS"))}
NAIVE["Ready"] = sum(1 for l in LINES if l["on_list"]) - NAIVE["Delivered"] - NAIVE["Owed"]

if __name__ == "__main__":
    print("lines", len(LINES), "on list", sum(l["on_list"] for l in LINES), "tickets ART-794 ..", [l["ticket"] for l in LINES if l["ticket"]][-1])
    print("truth counts", COUNTS, "| naive", NAIVE)
    for c in ("W", "READY", "VIS", "A1", "A2", "C1", "C2", "C4", "ADD"):
        print(f"  {c:5} {len(members(c)):3}", ", ".join(l["name"] for l in members(c))[:150])
    for k, v in SEED.items(): print(f"  {k:13} {v['svc']:8} {v['id']}")
