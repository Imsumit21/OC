#!/usr/bin/env python3
"""Design model for julia_zm3d_playable_brief (scenario stage, design D3 = injection rev2).

Single source of truth for the cohort, the units, the planned records and their minted ids. The other generators in this
folder turn it into the draft manifest, the gradable surface, the difficulty budget and the design tables. Nothing here is
SQL and no prompt, Oracle Event or criterion text is written here. Base ids are real synth-cut records read through
tools/hg.py; planned (seeded) ids are minted below and collision-checked by check_ids.py.

D2 replaces D1 after two cold reviews (01b_Redteam_Review.md, .second.md) and the base fact pack
(research/base_facts_D2.md, research/object_categories.csv). What changed, in one place:
  - Delivered lines are exactly what base shows went out on 24 and 26 Sep (the reference level's items, the cannon, the
    background, the zombie characters). Robert's eight are dated after the first zip, as the vendor's "8-item set".
  - The pack list's Category column is the game's own object category (Assets/Data/Objects/<Category>); every category
    holds lines of several classes, so a line's state needs its own ticket note.
  - Tickets live in the Design team (DES), created by Brian: its last base ticket is DES-312 of 7 May 2025, so DES-313 onward
    follow in number and date (in ZOM they would sit above ZOM-566 of 30 Sep), and Brian's own last tickets there are a parent
    (DES-307) with bare-titled children made seconds apart. Object work in base is ticketed in ZOM (ZOM-97 and its 51 children).
    Delivered tickets are Done, every other ticket In Progress: workflow state says nothing about Ready or Owed.
  - EXPORT is the vendor's own format rule (binary, not ASCII): twelve lines were saved out of the Unity project; only
    Marcus's post says what kind of file that gives. Armchair and First Aid Kit are off the list (D2 re-check).
  - Claire's message to Julia is in Turkish, as their whole DM is.
  - D2.2 (path exposure at injection): Robert's reply names no item (the bow through its thread parent, the dynamite as the
    last item on his list) and adds no line; the broken zip is in Brian's own log of the outgoing folder, a Google Doc, not
    in a comment on the pack ticket.
  - Objects with an open base ticket or a base change that would fork are not on the list (Gas Can, Helmet, Indoor Plant,
    Maracas, Curling Iron, Toy Truck, Clef, Music Note 1/2, Kettlebell, Dart Board, Candy).

D3 (rev2) is the revision after the pre-check and the six-run baseline of rev1 (01a_Hardening_Report.md, MODE B: six-run
average 81.8% on the gradable surface against a cap under 70%). Four deciding records move or change wording; no line,
rule, row, step or prompt sentence is added:
  - ARTHOLD: the bathroom UV redo is stated by Robert in his DM with Julia, not by Claire in hers (an author sweep for
    Claire returned her DM in 6 of 7 runs). Claire's DM row is gone.
  - ZIP: Brian's folder log says 'The .wav exports.' instead of 'The sound files.' (a full-text Drive search for 'sound',
    made for the sound question, listed the log in 5 of 6 baseline runs).
  - REVISED: a completion note elsewhere (v2 move A25): the same log records on Tue 30 Sep that Claire re-sent the three
    recoloured items and that they open and look right, so Cactus Plant, Chainsaw and Cone are Ready; a run that stops at
    Robert's 29 Sep post writes them Owed (the post was read in 7 of 7 runs).
  - EXPORT: Marcus's post keeps its place and loses the words of the note it corrects ('saved out of', 'exporter').
"""
import datetime as _dt, hashlib, uuid

SLUG = "julia_zm3d_playable_brief"
PERSONA = "julia_lawson"
DESIGN = "D3"
REV = "rev2"                         # the injection revision this design builds; rev1 is history (run_forensics/rev1)

# ---------------------------------------------------------------- base records (read this session or by the fact pack)
VENDOR_CH = "C08H78VJG80"          # PlayableX shared channel (private, Julia member)
DESIGN_CH = "C090N54TG79"          # #zombie-design
ART_CH = "C08R8CHB0QL"             # #zombie-art
MATCH3D_CH = "C0880U9751A"         # #zombie-match3d (private, 25 members, Julia posts there)
ANIM_CH = "C09ATAJ220H"            # #zm-animations
DM_FRED = "D05SD5QLG94"            # Julia - Frederick (English; last base message 18 Sep)
DM_CLAIRE = "D05HMBQUC8Z"          # Julia - Claire (Turkish throughout; last base message 24 Sep 16:49)
DM_BRIAN = "D076RBM29JS"           # Julia - Brian (Turkish)
DM_ROBERT = "D05GU6L0XFH"          # Julia - Robert
BASE = {
    "vendor_scenarios": f"{VENDOR_CH}/1756393065.804409",      # 2025-08-28 vendor: the four scenarios, one line each
    "vendor_simple": f"{VENDOR_CH}/1756452358.461719",         # 2025-08-29 vendor: recommends Scenario 1, simplest form
    "fred_retention": f"{VENDOR_CH}/1757695108.506159",        # 2025-09-12 Frederick: Scenario 1 filters for players who will like the game
    "fred_scenario1": f"{VENDOR_CH}/1757956024.883249",        # 2025-09-15 Frederick: go with Scenario 1; grenade, couch, plush doll a good start
    "vendor_formats": f"{VENDOR_CH}/1758022459.227279",        # 2025-09-16 vendor: start 29 Sep; the 8-item set; editable items; formats (binary fbx)
    "vendor_asset_list": f"{VENDOR_CH}/1758283671.878269",     # 2025-09-19 vendor: assets expected, by group; formats again
    "vendor_oct6": f"{VENDOR_CH}/1758701898.919999",           # 2025-09-24 vendor: start moved to 6 October
    "brian_zip1": f"{VENDOR_CH}/1758717576.077489",            # 2025-09-24 12:39 Brian: Playable-assets zip
    "brian_winfail": f"{VENDOR_CH}/1758717625.209649",         # 2025-09-24 Brian: reference level video; win and fail conditions
    "brian_later": f"{VENDOR_CH}/1758717701.940139",           # 2025-09-24 Brian: more items and zombie types later on
    "vendor_duck": f"{VENDOR_CH}/1758723504.085039",           # 2025-09-24 vendor: only the duck asset missing; zombies as Unity package
    "brian_zip2": f"{VENDOR_CH}/1758729487.922339",            # 2025-09-24 15:58 Brian: Plushie-and-zombies.zip
    "vendor_blank_scene": f"{VENDOR_CH}/1758808234.045839",    # 2025-09-25 vendor: zombie package has prefabs only; test in a blank project
    "brian_pack3": f"{VENDOR_CH}/1758906043.375719",           # 2025-09-26 17:00 Brian: zombies_Characters_UnityPack.zip
    "vendor_reviewed": f"{VENDOR_CH}/1759130898.184939",       # 2025-09-29 vendor: will review the assets
    "vendor_zombie_ask": f"{VENDOR_CH}/1759140968.965099",     # 2025-09-29 vendor: one primary animation and four zombies
    "fred_pause": f"{VENDOR_CH}/1759174925.309129",            # 2025-09-29 19:42 Frederick: pause for a month or so
    "vendor_nov3": f"{VENDOR_CH}/1759226395.551469",           # 2025-09-30 09:59 vendor: new start 3 November
    "vendor_music_rule": f"{VENDOR_CH}/1744637266.363689",     # 2025-04-14 vendor: music starts after the first click (first playable)
    "vendor_fbx_march": f"{VENDOR_CH}/1742892985.601399",      # 2025-03-25 vendor: everything in fbx (first playable)
    "julia_dd_brief": f"{VENDOR_CH}/1741963515.221549",        # 2025-03-14 Julia: storyboard and brief for the first playable
    "vendor_thanks_brief": f"{VENDOR_CH}/1742063341.276529",   # 2025-03-15 vendor: thank you for this detailed brief
    "fred_asks_julia": f"{DM_FRED}/1758220925.518329",         # 2025-09-18 Frederick to Julia: the vendor's formats; who can give access
    "julia_names_brian": f"{DM_FRED}/1758221343.478869",       # 2025-09-18 Julia: Brian fished out the assets for the Domino playable
    "brian_asks_level": f"{DESIGN_CH}/1758568735.563539",      # 2025-09-22 Brian asks Julia for the reference level
    "playable_thread": f"{DESIGN_CH}/1758567201.262949",       # 2025-09-22 playable thread root
    "julia_shuriken_idea": f"{DESIGN_CH}/1758569824.148029",   # 2025-09-22 Julia: grenades and shuriken idea
    "robert_remain": f"{DESIGN_CH}/1758569885.985319",         # 2025-09-22 Robert: remain as is
    "brian_robert_ok": f"{DM_BRIAN}/1758638497.621679",        # 2025-09-23 Brian to Julia: Robert is fine with Frederick's items
    "julia_level": f"{DM_BRIAN}/1758638743.317009",            # 2025-09-23 Julia: making the grenade, couch, plushie level
    "leonard_pause_q": f"{DESIGN_CH}/1759114097.776589",       # 2025-09-29 Leonard: should we pause the playable
    "brian_sent": f"{DESIGN_CH}/1759141833.339099",            # 2025-09-29 Brian: I sent them the assets, they haven't started
    "robert_new_colours": f"{DESIGN_CH}/1759189466.554739",    # 2025-09-29 23:44 Robert: new coloured cactus, chainsaw and cones
    "art_cactus": f"{ART_CH}/1758752145.583769",               # 2025-09-24 22:15 Robert: colourised cactus plant
    "art_cone": f"{ART_CH}/1758754866.994649",                 # 2025-09-24 23:01 Robert: colourised cone
    "art_claire_pr": f"{ART_CH}/1758808937.107229",            # 2025-09-25 14:02 Claire: pushed the changes in a new pr
    "art_bow_root": f"{ART_CH}/1758904025.123869",             # 2025-09-26 16:27 Julia: arrow to go with the bow (root, 1 reply)
    "art_bow_claire": f"{ART_CH}/1758904103.894649",           # 2025-09-26 16:28 Claire: Of course
    "art_bounce": f"{ART_CH}/1756813716.024339",               # 2025-09-02 thread that names the six items Robert later adds (among other bounce items)
    "anim_zombies": f"{ANIM_CH}/1758881579.188609",            # 2025-09-26 Brian: the nine zombies (four names unmasked)
    "anim_pack": f"{ANIM_CH}/1758905604.787929",               # 2025-09-26 16:53 Marcus: zombie pack, tested in an empty project
    "marcus_fbx_settings": f"{MATCH3D_CH}/1738678859.796159",  # 2025-02-04 Marcus: fbx export settings (in character for A1)
    "robert_copyright": f"{DM_ROBERT}/1757519060.984519",      # 2025-09-10 Robert to Julia: two sounds have to be swapped (copyright)
    "sfx_scale": "C09A7PDFYCV/1755464752.078539",              # 2025-08-17 Calvin: pitched the scale from the sample Robert gave
    "pr462": "harmonygames-Games/match3d#462",                 # Objects Revisions and Changes, created 2025-09-25T11:43:06Z, merged 23:15:41Z
    "pr462_comment": "harmonygames-Games/match3d#462#c_1",     # CodeRabbit: candy, chainsaw, cactus, cone, dart models; five colour prefabs
    "pr460": "harmonygames-Games/match3d#460",                 # New Objects, merged 2025-09-24T21:51:38Z (additions; two shared atlases)
    "gdd": "page_zm3d_gdd",                                    # Confluence: 7-slot tray, loss only at zero health; Design: Julia Lawson
    "gdd_c1": "comment_zm3d_gdd_c1", "gdd_c2": "comment_zm3d_gdd_c2",
    "playable_feedback_doc": "f_05bedd1540d3e01a90ab16",       # Leonard's Playable Feedback (first playable)
    "trello_kickoff": "688c4d14c312a27fa2747e40",              # Playable Kickoff card (Leonard's board; no comments in base)
    "julia_root": "d_8140f09bf9f1b94cb8ee2d",                  # Julia's Drive root (owner)
    "des312": "DES-312",                                       # the Design team's last base ticket (Brian, 2025-05-07T19:31:13Z, child of DES-307)
    "des307": "DES-307",                                       # Brian's parent ticket of that day, with bare-titled children
    "zom97": "ZOM-97",                                         # REVISION FOR ITEMS: 51 children titled with object names (precedent)
}

def h(label, n):
    return hashlib.sha256(("julia_zm3d_playable_brief|" + label).encode()).hexdigest()[:n]

COMMENT_NS = uuid.uuid5(uuid.NAMESPACE_URL, "hg-task/julia_zm3d_playable_brief")
def comment_id(label):
    """Linear comment ids are uuid5(namespace, name), the generators' linear.comment_uuid/1 convention."""
    return str(uuid.uuid5(COMMENT_NS, label))

def slack_id(channel, ts):
    return hashlib.sha256(f"{channel}|{ts}".encode()).hexdigest()[:32]

SLACK_USER = {"Frederick Stone": "EMPLOYEE_0008_SLACK_ID", "Robert": "EMPLOYEE_0016_SLACK_ID", "Marcus Bennett": "EMPLOYEE_0002_SLACK_ID",
              "Claire Morgan": "EMPLOYEE_0009_SLACK_ID", "Brian Foster": "EMPLOYEE_0026_SLACK_ID", "Julia Lawson": "EMPLOYEE_0005_SLACK_ID"}
def _ts(channel, iso, who):
    """The generators' slack.ts/1 convention: the given second plus five digits of sha256(channel|epoch|user) and a final 9."""
    epoch = int(_dt.datetime.fromisoformat(iso.replace('Z', '+00:00')).timestamp())
    digest = hashlib.sha256(f"{channel}|{epoch}|{SLACK_USER[who]}".encode()).hexdigest()
    return f"{epoch:010d}.{int(digest[:8], 16) % 100000:05d}9"

TEAM, TEAM_ID = "DES", "team_DES"
PACK_TICKET = "DES-313"            # base highest DES number is 312 (conventions.json linear.max_number; lookup of every minted key)
FIRST_CHILD = 314

# ---------------------------------------------------------------- planned records (minted ids; UTC times)
SEED = {
    # hub and rules
    "ask": {"svc": "slack", "id": f"{DM_FRED}/{_ts(DM_FRED, '2025-09-30T18:21:34Z', 'Frederick Stone')}", "at": "2025-09-30T18:21:34Z", "by": "Frederick Stone",
            "what": "Frederick's DM to Julia: the job, its destinations, and the three things it starts from"},
    "notes": {"svc": "gdocs", "id": "f_" + h("notes", 22), "at": "2025-09-30T16:58:00Z", "by": "Frederick Stone",
              "what": "Frederick's hand-off notes (created 2025-09-30 16:25, before his 17:30 investor call): what the brief covers, the list's columns, the three states, tickets, sharing"},
    "tracker": {"svc": "gsheets", "id": "f_" + h("tracker", 22), "at": "2025-09-26T17:25:00Z", "by": "Brian Foster",
                "what": "Brian's pack list (created 2025-09-25): one row per line: Line, Kind, Category, Went out, Ticket; no state column"},
    "picks": {"svc": "slack", "id": f"{DESIGN_CH}/{_ts(DESIGN_CH, '2025-09-25T18:12:26Z', 'Robert')}", "at": "2025-09-25T18:12:26Z", "by": "Robert",
              "what": "Robert's eight for the board, the vendor's '8-item set': the reference level's three plus five (root post in #zombie-design)"},
    "zpicks": {"svc": "slack", "id": f"{DESIGN_CH}/{_ts(DESIGN_CH, '2025-09-29T17:31:08Z', 'Robert')}", "at": "2025-09-29T17:31:08Z", "by": "Robert",
               "what": "Robert's answer to the vendor's 29 Sep question: walk as the one animation; Party Girl, Plumber, Magician, Football Player"},
    "ticket_parent": {"svc": "linear", "id": PACK_TICKET, "at": "2025-09-25T07:05:00Z", "by": "Brian Foster",
                      "what": "Brian's pack ticket in the Design team; children DES-314 to DES-409, one per line of the pack list"},
    "deck": {"svc": "gslides", "id": "f_" + h("deck", 22), "at": "2025-09-23T19:55:00Z", "by": "Julia Lawson",
             "what": "Julia's deck of the reference level as built on 23 Sep: grenade, couch, plushies; mixed zombies; win and fail"},
    "hold": {"svc": "gcal", "id": "evt_" + h("hold_julia", 22), "at": "2025-09-30T16:41:00Z", "by": "Frederick Stone",
             "what": "kickoff hold Mon 3 Nov 2025 17:00 UTC; attendees Frederick, Julia, Brian, Robert (one row per calendar)"},
    "contact": {"svc": "contacts", "id": h("contact_playablex", 24), "at": "2025-09-19T16:40:00Z", "by": "Frederick Stone",
                "what": "PlayableX intake contact (outside partner): the address a view link is shared with"},
    "trello_note": {"svc": "trello", "id": "68dc381b" + h("trello_note", 16), "at": "2025-09-30T20:05:47Z", "by": "Leonard Hayes",
                    "what": "Leonard's comment on his Playable Kickoff card: parked until 3 November, Julia is pulling the brief and the pack status together for Frederick"},
    # deciding records of the units
    "a1_post": {"svc": "slack", "id": f"{MATCH3D_CH}/{_ts(MATCH3D_CH, '2025-09-26T17:08:37Z', 'Marcus Bennett')}", "at": "2025-09-26T17:08:37Z", "by": "Marcus Bennett",
                "what": "A1: root post in #zombie-match3d: the models Brian saved out of Unity on Thursday are the text kind (the setting was wrong that day); Claire's are fine"},
    "a2_dm": {"svc": "slack", "id": f"{DM_ROBERT}/{_ts(DM_ROBERT, '2025-09-29T20:38:52Z', 'Robert')}", "at": "2025-09-29T20:38:52Z", "by": "Robert",
              "what": "A2: Robert to Julia in their DM (English, between his messages of 29 Sep): Claire is redoing the UVs of the bathroom objects; the bathroom files she gave Brian on Friday are the old ones"},
    "c3_reply": {"svc": "slack", "id": f"{ART_CH}/{_ts(ART_CH, '2025-09-26T21:41:19Z', 'Robert')}", "at": "2025-09-26T21:41:19Z", "by": "Robert",
                 "what": "C3: Robert's reply under Julia's bow post: the bow goes in the eight in place of the last item on his list (the dynamite), as it is; the reply names no item"},
    "c4_log": {"svc": "gdocs", "id": "f_" + h("c4_log", 22), "at": "2025-09-30T09:12:26Z", "by": "Brian Foster",
               "what": "C4: Brian's own log of what he put in the outgoing folder (a Google Doc, created 25 Sep): on Tue 30 Sep Claire re-sent the three recoloured items, which open and look right; the zip with Friday's music instruments was cut off on upload and will not unpack, and the eight are not in the folder any other way"},
    "c2_sheet": {"svc": "gsheets", "id": "f_" + h("c2_sheet", 22), "at": "2025-09-26T20:10:00Z", "by": "Calvin Price",
                 "what": "C2: Calvin's sound sources sheet (created 2025-09-12): where each cue came from, whether it is ours to pass on, who makes our own version"},
}

# ---------------------------------------------------------------- the cohort
# cls: W = delivered and usable; READY = exported, opens, current, nobody changing it; VIS = owed, stated on the line's own ticket;
#      A1/A2/C1/C2/C4 = owed, decided by that unit's record; ADD = not on Brian's list, added by Robert (owed, no ticket).
THU, FRI, MON = "Thu 25 Sep", "Fri 26 Sep", "Mon 29 Sep"
def R(day): return ("READY", day)
BOARD = {   # game category (Assets/Data/Objects/<Category>) -> [(object, class or (class, day)), ...]
    "Living Room": [("Couch", "W"), ("Couch and Pillow", "W"), ("Alarm Clock", "A1"), ("Record Player", "A1"),
                    ("Retro TV", "A1"), ("Desk Lamp", R(FRI)), ("Small Lamp", R(FRI)), ("Fly Zapper", "VIS")],
    "Survival": [("Grenade", "W"), ("Chainsaw", "C1"), ("Cute Axe", R(THU)), ("Cute Hammer", R(THU)), ("Dynamite", R(THU)), ("Shuriken", R(THU)),
                 ("Saber", R(FRI)), ("Safe", R(FRI)), ("Flashlight", R(MON)), ("Fire Extinguisher", "VIS"),
                 ("Propane Tank", "VIS")],
    "Toys": [("Plushie Bunny", "W"), ("Plushie Chick", "W"), ("Bow", R(MON)), ("Cone", "C1"), ("Dice", R(THU)), ("Gift Box", R(THU)),
             ("Plushie Dog", R(FRI)), ("Plushie Whale", R(FRI)), ("Whistle", R(FRI)), ("Wooden Tower", R(MON)), ("Toy Car", R(MON)),
             ("Toy Boat", R(MON)), ("Toy Airplane", R(MON)), ("Toy Train", "VIS"), ("Beach Ball", "VIS")],
    "Bathroom": [(n, "A2") for n in ("Bathroom Scale", "Bathtub", "Cabinet Sink", "Flip Flops", "Iron", "Ironing Board", "Plunger", "Slippers",
                                     "Toilet", "Toilet Paper", "Wash Basin", "Washing Machine")] + [("Rubber Ducky", "VIS")],
    "Kitchen": [(n, "A1") for n in ("Coffee Machine", "Cooler", "Ice Cream Machine", "Kitchen Mixer", "Microwave", "Oven", "Refrigerator", "Stove", "Toaster")]
               + [("Dutch Oven", R(FRI)), ("Rolling Pin", R(FRI)), ("Round Kettle", R(FRI)), ("Round Pan", R(MON)), ("Spatula", R(MON)),
                  ("Whisk", R(MON)), ("Ladle", R(MON)), ("Small Kettle", "VIS"), ("Tall Kettle", "VIS")],
    "Music Instruments": [(n, "C4") for n in ("Acoustic Guitar", "Cello", "Cymbals", "Electric Guitar", "Harp", "Tambourine", "Trumpet", "Xylophone")]
                         + [("Music Keyboard", R(MON)), ("Grand Piano", "VIS")],
    "Garden": [("Cactus Plant", "C1"), ("Barrel", R(FRI)), ("Bench", R(FRI)), ("Flower Pot", R(FRI)), ("Garden Shears", R(MON)),
               ("Watering Can", R(MON)), ("Wooden Bucket", R(MON)), ("Wheelbarrow", "VIS"), ("Wooden Crate", "VIS")],
}
OTHER = [("Cannon", "Weapon", "W"), ("Background", "Background", "W"), ("Zombie characters", "Zombies", "W"),
         ("Matching sound", "Sound", "READY"), ("Rocket sound", "Sound", "C2"), ("Explosion sound", "Sound", "C2"),
         ("Success sound", "Sound", "READY"), ("Failure sound", "Sound", "READY"), ("Background music", "Sound", "VIS"),
         ("Item visuals", "2D", "VIS"), ("UI elements", "2D", "VIS"), ("Fonts", "Font", "VIS")]
ADDED = []     # D2.2: no line is added outside Brian's list (a reply naming items would sit on the keyword-swept path)
PICKS_25SEP = ["Grenade", "Couch", "Plushie Chick", "Shuriken", "Cute Axe", "Gift Box", "Cactus Plant", "Dynamite"]     # Robert, 25 Sep (the dynamite last)
DEFAULT_FINAL = ["Grenade", "Couch", "Plushie Chick", "Shuriken", "Cute Axe", "Gift Box", "Bow", "Cactus Plant"]        # after his 26 Sep reply
ZOMBIES = ["Party Girl", "Plumber", "Magician", "Football Player"]       # the four unmasked names of base's nine (C09ATAJ220H/1758881579.188609)
PRIMARY_ANIMATION = "walk"
REFERENCE_LEVEL = ["Grenade", "Couch", "Couch and Pillow", "Plushie Bunny", "Plushie Chick"]   # base: D07G5QWN3TM/1758712833.442809

# Brian's note on each ticket (planned wording; raw facts, never the state). {day} is the day he got or made the file.
NOTE = {
    "W": "In the first zip, 24 Sep.",
    "READY": "FBX from Claire, {day}. Opens, looks right. In the outgoing folder.",
    "A1": "FBX saved out of the project, Thu 25 Sep, so the colours come along. Opens, looks right. In the outgoing folder.",
    "A2": "FBX from Claire, Fri 26 Sep. Opens, looks right. In the outgoing folder.",
    "C1": "FBX from Claire, Thu 25 Sep, first thing. Opens, looks right. In the outgoing folder.",
    "C4": "FBX from Claire, Fri 26 Sep. Opens, looks right. Zipped with the other instruments, in the outgoing folder.",
    "SOUND": "Exported .wav from the project, Fri 26 Sep. Plays. In the outgoing folder.",
}
NOTE_W = {"Plushie Chick": "Went in the second zip on 24 Sep (the one they called the duck). Their message today about that zip is the zombie package, not the chick.",
          "Zombie characters": "Unity pack from Marcus, sent Fri 26 Sep. They have been through it and will re-rig the characters from it. They want us to pick one animation and four of the zombies, that one is for Robert.",
          "Cannon": "In the first zip, 24 Sep, with its projectile. It is what they call the rocket launcher.",
          "Background": "In the first zip, 24 Sep. The background of the reference level."}
VIS_NOTE = {   # line -> (Brian's note, what is owed, who has it)
    "Fly Zapper": ("Not exported yet. Waiting on the FBX from Claire.", "the FBX", "Claire Morgan"),
    "Fire Extinguisher": ("Not exported yet. Waiting on the FBX from Claire.", "the FBX", "Claire Morgan"),
    "Propane Tank": ("Not exported yet. Mine to do, didn't get to it on Friday.", "the export", "Brian Foster"),
    "Toy Train": ("Not exported yet. Mine to do, didn't get to it on Friday.", "the export", "Brian Foster"),
    "Beach Ball": ("Not exported yet. Waiting on the FBX from Claire.", "the FBX", "Claire Morgan"),
    "Rubber Ducky": ("Not exported yet. Waiting on the FBX from Claire.", "the FBX", "Claire Morgan"),
    "Small Kettle": ("Not exported yet. Mine to do, didn't get to it on Friday.", "the export", "Brian Foster"),
    "Tall Kettle": ("Not exported yet. Mine to do, didn't get to it on Friday.", "the export", "Brian Foster"),
    "Grand Piano": ("Not exported yet. Waiting on the FBX from Claire.", "the FBX", "Claire Morgan"),
    "Wheelbarrow": ("Not exported yet. Waiting on the FBX from Claire.", "the FBX", "Claire Morgan"),
    "Wooden Crate": ("Not exported yet. Mine to do, didn't get to it on Friday.", "the export", "Brian Foster"),
    "Background music": ("Not exported. Calvin is still cutting the ad track down to a loop.", "the loop for the ad", "Calvin Price"),
    "Item visuals": ("Not exported yet. The item icons are in Figma, mine to pull as PNG.", "the PNG export", "Brian Foster"),
    "UI elements": ("Not exported yet. In Figma, mine to pull as PNG.", "the PNG export", "Brian Foster"),
    "Fonts": ("Not sent. Waiting on the .ttf files from Martin.", "the font files", "Martin Walsh"),
}
UNIT_REASON = {"A1": ("the file is ASCII, not a format they take: export it again as binary", "Brian Foster"),
               "A2": ("the art is being redone (UVs); the exported file is the old state", "Claire Morgan"),
               "C1": ("the art changed after the file was handed over (25 Sep); the current file has to come again", "Claire Morgan"),   # D3: the natural reading only (a run that misses the log)
               "C2": ("not ours to pass on (library or bought pack); needs our own version", "Calvin Price"),
               "C4": ("the zip it sits in is cut off and will not unpack, and it is not in the outgoing folder any other way; put the files back", "Brian Foster"),
               "ADD": ("not on the pack list; not exported, no ticket", "Brian Foster")}

def lines():
    out = []
    def add(name, kind, category, cls, day=None):
        n = len(out) + 1
        on_list = cls != "ADD"
        ticket = f"{TEAM}-{FIRST_CHILD + n - 1}" if on_list else None
        state = "Delivered" if cls == "W" else "Ready" if cls in ("READY", "C1") else "Owed"     # D3: C1 re-sent (Brian's log, 30 Sep)
        owed = owner = None
        if cls == "VIS": note, owed, owner = VIS_NOTE[name]
        elif cls == "W": note = NOTE_W.get(name, NOTE["W"])
        elif cls == "ADD": note = None
        elif kind == "Sound": note = NOTE["SOUND"]
        else: note = NOTE[cls].format(day=day)
        if cls in UNIT_REASON and state == "Owed": owed, owner = UNIT_REASON[cls]
        went = {"Plushie Chick": "zip 24 Sep (second)", "Zombie characters": "pack 26 Sep"}.get(name, "zip 24 Sep") if cls == "W" else ""
        board = None
        if kind == "Board item": board = "Default" if name in DEFAULT_FINAL else "Extra"
        out.append({"n": n, "name": name, "kind": kind, "category": category, "went_out": went, "cls": cls, "day": day, "ticket": ticket,
                    "state": state, "owed": owed, "owner": owner, "who": owner.split()[0] if owner else None,   # truth of 'Who has it': the first name (issue_key comparator)
                    "on_list": on_list, "note": note, "board_set": board,
                    "ticket_state": ("Done" if cls == "W" else "In Progress") if on_list else None})
    for cat, members_ in BOARD.items():
        for name, c in members_:
            cls, day = c if isinstance(c, tuple) else (c, None)
            add(name, "Board item", cat, cls, day)
    for name, kind, cls in OTHER:
        add(name, kind, "", cls)
    for name, cat in ADDED:
        add(name, "Board item", cat, "ADD")
    return out

LINES = lines()
BY_NAME = {l["name"]: l for l in LINES}
def members(cls): return [l for l in LINES if l["cls"] == cls]
COUNTS = {s: sum(1 for l in LINES if l["state"] == s) for s in ("Delivered", "Ready", "Owed")}
NAIVE = {"Delivered": len(members("W")), "Owed": len(members("VIS"))}
NAIVE["Ready"] = sum(1 for l in LINES if l["on_list"]) - NAIVE["Delivered"] - NAIVE["Owed"]
N_LIST = sum(1 for l in LINES if l["on_list"])
OWED_WITH_TICKET = [l for l in LINES if l["state"] == "Owed" and l["ticket"]]
LAST_CHILD = f"{TEAM}-{FIRST_CHILD + N_LIST - 1}"

if __name__ == "__main__":
    assert len({l["name"] for l in LINES}) == len(LINES), "duplicate line name"
    import csv, pathlib
    tree = {}
    for r in csv.DictReader(open(pathlib.Path(__file__).resolve().parents[1] / "research/object_categories.csv")):
        tree[r["object"]] = r["category"]
    bad = [(l["name"], l["category"], tree.get(l["name"])) for l in LINES if l["kind"] == "Board item" and tree.get(l["name"]) != l["category"]]
    print("board items not matching the game's category tree:", bad or "none")
    print("lines", len(LINES), "on list", N_LIST, f"tickets {TEAM}-{FIRST_CHILD} ..", LAST_CHILD)
    print("truth counts", COUNTS, "| naive", NAIVE, "| owed with a ticket", len(OWED_WITH_TICKET))
    for c in ("W", "READY", "VIS", "A1", "A2", "C1", "C2", "C4", "ADD"):
        print(f"  {c:5} {len(members(c)):3}", ", ".join(l["name"] for l in members(c))[:170])
    for k, v in SEED.items(): print(f"  {k:13} {v['svc']:8} {v['id']}")
