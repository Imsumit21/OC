#!/usr/bin/env python3
"""The rubric plan's rows (prep mode of /create-rubric-writing, playbook 09), built from the OE ledger's model
(oe_gen/model.py and facts.py: every value read from the SQL rows or the base records re-read through tools/hg.py) and the
gradable surface. Writes plan/rubric/rows.json; plan/rubric/build_plan.py renders 09_Rubric_Writing_Plan.md from it.

Shape (gate 15 and the platform rules of gate 15a):
  * the brief: one row per prompt-set element; lists (the eight on the board, the four zombies, the usable and the
    held-back sounds) get one row per member, since a list in one title is a filtered list (non_atomic);
  * the hand-off list: table cells under the table spot-check rule: one volume row, direct rows on the members an
    authority singles out (each trap group: two members, the two named sounds) and ordinary samples (the controls);
  * ticket moves: one template (state to Todo), so five samples plus one volume row that states the template;
  * ticket comments: content differs by line group, so one row per comment, never sampled;
  * shares: one row per share; the DM and the channel post: their content rows prove the write;
  * no count over the list's rows (count-bundle-v1): the three counts are graded once, in the DM."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
sys.path.insert(0, str(WF / "oe_gen"))
import model as O            # noqa: E402
import facts as FX           # noqa: E402
F, FL = FX.F, FX.FL
EV = json.loads((WF / "oe_gen" / "out" / "oe_events.json").read_text())
PROMPT = O.PROMPT
def oe(prefix):
    hits = [e["n"] for e in EV if e["head"].startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return hits[0]
N = {k: oe(v) for k, v in {"ask": "Find Frederick's message", "notes": "Find Frederick's hand-off notes", "pack": "Find Brian's pack list",
     "ticket": "Open DES-314", "tnotes": "Read Brian's note", "thr1": "Find the PlayableX channel", "thr2": "Read the thread under Frederick's Sep 18",
     "thr3": "Read the thread under Frederick's Sep 29", "music": "Search Slack for \"music\"", "design": "Read #zombie-design", "bow": "Check whether Robert changed",
     "a1": "Read #zombie-match3d", "a2": "Read Julia's direct messages with Robert", "log": "Find Brian's log", "sound": "Find Calvin's sound sources",
     "deck": "Read Julia's deck", "gdd": "Open the design page", "hold": "Find the kickoff hold", "contact": "Look up PlayableX",
     "brief": "Create the brief", "sheet": "Create the hand-off list", "rows": "Write the header", "dm": "Give Frederick the count", "post": "Post both links"}.items()}
def share_oe(label, who): return oe(f"Share {label} (OE {N['brief'] if label == 'the brief' else N['sheet']}) with {who} ")
def move_oe(t): return [e["n"] for e in EV if e["head"].startswith(f"Move {t} (")][0]
def comm_oe(t): return [e["n"] for e in EV if e["head"].startswith(f"Comment on {t} (")][0]
def label(n): return f"OE {n}"

S = {"msg": "Frederick's playable message from yesterday", "every": "everything he's asking for in it", "start": "start to finish",
     "drive": "The files he wants should end up in my Drive", "links": "once they're ready the links go in the PlayableX channel like he says"}
for v in S.values(): assert v in PROMPT, v

MECH = {"A1": ("EXPORT", "T1, C1"), "A2": ("ARTHOLD", "T2, C2"), "C1": ("REVISED", "T3, C3"), "C4": ("ZIP", "T7, C6"), "C2": ("AUDIO", "T4, C5")}
DECIDE_F = {"A1": ["a1", "formats"], "A2": ["a2"], "C1": ["c1", "c4"], "C4": ["c4"], "C2": ["c2"], "VIS": [], "READY": [], "W": ["sent"]}
SRC = {"A1": f"Marcus's post {O.A1['id']} ('the text kind, the setting was wrong that day so youll need to redo them') with PlayableX's rule {O.base('vendor_formats')['id']} ('please make sure it’s exported in *Binary format*, not ASCII')",
       "A2": f"Robert's note {O.A2['id']} ('is redoing the UVs on the bathroom objects', 'the bathroom files she gave … on Friday are the old version too')",
       "C1": f"Robert's post {O.base('robert_new_colours')['id']} ('new colored version of cactus, chainsaw and cones'), then Brian's log {O.LOG_ID} ('Claire sent the three recoloured models again … they replace Thursday's')",
       "C4": f"Brian's log {O.LOG_ID} ('The zip with Friday's music instruments got cut off on upload … those eight aren't in the folder any other way. I still have Claire's files, I'll put them back when we pick this up again.')",
       "C2": f"Calvin's sheet {O.SOUND_ID} ('no' under 'OK outside the game'; 'not made yet, Calvin') with the notes' rule ('Anything from a library or a bought pack stays here until we have our own version')",
       "VIS": "the line's own note", "READY": "the line's own note, with no later word on it", "W": "the line's Done ticket and its note"}
OWED_ACCEPT = {"A1": "binary FBX export (accept: export again as binary FBX; a binary re-export; not the ASCII/text kind)",
               "A2": "the file again once the UVs are redone (accept: re-UV'd FBX; the updated bathroom file once Claire redoes the UVs)",
               "C4": "the file put back in the outgoing folder (accept: re-upload; re-zip or send the eight again; the zip won't unpack)",
               "C2": "our own version of the sound (accept: a replacement made here; not the library or bought-pack file)"}
HOLD = {"Brian": "Brian (Brian Foster)", "Claire": "Claire (Claire Morgan)", "Calvin": "Calvin (Calvin Price)", "Martin": "Martin (Martin Walsh)"}

rows = []
def add(**r):
    r.setdefault("cat", "Outcome"); r.setdefault("dist", "—"); r.setdefault("amb", "—"); r.setdefault("decided", "—")
    r.setdefault("group", "—"); r.setdefault("dup", "—"); r.setdefault("allfail", "none · over-specific risk: low"); r.setdefault("reach", "PROMPT_LINKED")
    r.setdefault("slot", [])
    assert r["span"] in S, r["tag"]
    rows.append(r)
def fids(*keys): return ", ".join(F(k) if not k.startswith("line:") else FL(k[5:]) for k in keys)
L = O.BY

# ------------------------------------------------------------------ deliverable 1: the brief (OE brief)
add(tag="brief_doc", span="drive", oes=[N["brief"]], fact="brief_location", what="the brief is a Google Doc in Julia's own Drive",
    final="a Google Doc owned by julia.lawson@harmonygames.co", title="The Agent creates the brief as a Google Doc owned by Julia (julia.lawson@harmonygames.co), in her own Drive",
    values=f"owner `julia.lawson@harmonygames.co` · Google Doc · accepts: her Drive root or any folder she owns (brief §4b) · {fids('drive', 'ask')}",
    kind=("lookup", "the ask names the place ('both in your Drive') and the doc type ('Brief as a doc')"), band=1,
    valid="a Google Doc titled anything, owned by Julia, in her root or a folder of hers",
    nothing="no Google Doc exists, so 'The Agent creates the brief as a Google Doc owned by Julia' fails")
add(tag="b_scenario", span="every", oes=[N["thr1"], N["brief"]], fact="scenario", slot=["B2"], what="the brief names the scenario picked",
    final="the brief says Scenario 1", title="The Agent's brief names Scenario 1 as the scenario picked for the playable",
    values=f"`Scenario 1` · source {O.base('fred_scenario1')['id']} ('lets go with Scenario 1.') · accepts: 'Scenario 1', 'scenario one' · {fids('scenario')}",
    kind=("interpretation", "the pick is made in a reply under Frederick's thread among four vendor scenarios"), band=3,
    valid="'We picked Scenario 1, the core game in its simplest form'", nothing="no brief exists, so 'The Agent's brief names Scenario 1' fails")
add(tag="b_purpose", span="every", oes=[N["thr1"], N["design"], N["brief"]], fact="scenario_purpose", slot=["B2b"], what="the brief says what the scenario is for",
    final="the purpose: filter for the players who will like the game, true to its core game play, testing the game as it is",
    title="The Agent's brief says the playable is there to test the game as it is today, filtering for the players who will like it while staying true to its core game play",
    values=(f"`filtering out the players that won't like our game` · `true to our core game play` · `current form and audience fit` · sources {O.base('fred_retention')['id']} (Frederick, Sep 12), "
            f"C090N54TG79/1758569655.409719 and the walk-back C090N54TG79/1758569885.985319 ('I think we should remain as is'); the ask 'Write it for the game as it is today' · "
            f"accepts: any wording of that one purpose; rejects: a more hardcore-friendly playable (walked back, /oe round 1) · {fids('purpose', 'ask')}"),
    kind=("interpretation", "Frederick's reasoning, read with the Sep 22 thread where a hardcore line is walked back"), band=3, dist="ledger T20 (Julia's 'more hardcore friendly playable') → a brief giving it as the purpose fails",
    amb="ledger risk 8 (settled: one purpose)", valid="'Scenario 1 tests the game in its current form with the players who'll like it, true to the core game'",
    nothing="no brief exists, so the purpose row fails")
EIGHT_KEEP = [n for n in O.EIGHT if n != "Bow"]
for n in EIGHT_KEEP:
    add(tag=f"b_eight_{n}", span="every", oes=[N["design"], N["bow"], N["brief"]], fact=f"board_eight:{n}", slot=["B1"] if n == "Shuriken" else [],
        what=f"the brief lists {n} among the eight on the board", final=f"{n} is one of the brief's eight board items",
        title=f"The Agent's brief lists {n} among the eight items on the board", values=f"`{n}` · source {O.PICKS['id']} (Robert, Sep 25: the 8) · {fids('picks', 'eight')}",
        kind=("lookup", "named in Robert's Sep 25 list and unchanged by his reply"), band=1, group="—", dup=("fact also in the Board set sample P(C4)" if n == "Grenade" else "—"),
        valid=f"a list of the eight board items that includes {n}", nothing=f"no brief exists, so 'lists {n} among the eight' fails")
add(tag="b_eight_Bow", span="every", oes=[N["design"], N["bow"], N["brief"]], fact="board_eight:Bow", slot=["B1"],
    what="the brief lists the Bow among the eight, in place of the Dynamite", final="the brief's eight include Bow and not Dynamite",
    title="The Agent's brief lists the Bow among the eight items on the board, in place of the Dynamite",
    values=f"`Bow` in place of `Dynamite` · source {O.C3['id']} ('Let's have it in the 8 in place of the last one on my list') under {O.base('art_bow_root')['id']}; the last on {O.PICKS['id']} is Dynamite · {fids('c3', 'picks', 'eight')}",
    kind=("multi-source", "Robert's Sep 25 list read with his Sep 26 reply under an unrelated post in another channel"), band=5, decided="T5, T15, C4",
    dist="ledger T1 (Robert's Sep 25 list with Dynamite) → a brief keeping Dynamite fails; T9/T10 (the deck's board, Frederick's three) → not graded",
    dup="fact also in P(X13) Board set Bow (2 rows)", valid="'On the board: Grenade, Couch, Plushie Chick, Shuriken, Cute Axe, Gift Box, Cactus Plant and Bow'",
    nothing="no brief exists, so the Bow row fails")
add(tag="b_extras", span="every", oes=[N["notes"], N["brief"]], fact="board_extras", what="the brief says every other board item on the list is an extra",
    final="the brief says the other board items on Brian's list are extras PlayableX can swap in",
    title="The Agent's brief says every other board item on Brian's pack list is an extra PlayableX can swap in",
    values=f"`extra` · source the notes {O.NOTES_ID} ('every other board item on the list is an extra they can swap in') and {O.PICKS['id']} ('Everything else … is extras they can swap in') · accepts: 'extras', 'they can swap in any of the others' · {fids('notes', 'picks')}",
    kind=("lookup", "stated in the notes and in Robert's post"), band=1, valid="'Every other board item on Brian's list is an extra you can swap in'", nothing="no brief exists, so the extras row fails")
for n in ["Party Girl", "Plumber", "Magician", "Football Player"]:
    add(tag=f"b_zombie_{n}", span="every", oes=[N["design"], N["brief"]], fact=f"zombie:{n}", slot=["B3"] if n == "Plumber" else [],
        what=f"the brief names {n} among the four zombies", final=f"{n} is one of the brief's four zombies",
        title=f"The Agent's brief names {n} as one of the four zombies", values=f"`{n}` · source {O.ZPICKS['id']} (Robert, Sep 29) · {fids('zpicks')}",
        kind=("lookup", "named in Robert's Sep 29 answer"), band=1, dist="ledger T9 (the deck's 'A mix, nothing fixed yet.') → a brief with no fixed zombies fails",
        valid=f"'The four zombies: Party Girl, Plumber, Magician and Football Player'", nothing=f"no brief exists, so the {n} row fails")
add(tag="b_anim", span="every", oes=[N["design"], N["brief"]], fact="animation", slot=["B3"], what="the brief names the one animation",
    final="the brief says walk", title="The Agent's brief names walk as the one animation", values=f"`walk` · source {O.ZPICKS['id']} ('one animation, walk') · {fids('zpicks')}",
    kind=("lookup", "named in Robert's Sep 29 answer"), band=1, valid="'one animation: walk'", nothing="no brief exists, so the animation row fails")
add(tag="b_win", span="every", oes=[N["thr2"], N["deck"], N["brief"]], fact="win_rule", what="the brief says how a level is won",
    final="won when every zombie on screen is eliminated", title="The Agent's brief says a level is won when every zombie on screen is eliminated",
    values=f"`eliminating all the zombies on screen` · sources {O.base('brian_winfail')['id']} (Brian to PlayableX), the deck {O.DECK_ID} · accepts: 'kill all the zombies', 'clear every zombie' · {fids('winfail', 'deck')}",
    kind=("interpretation", "Brian's message and the deck agree; older level documents speak of a boss"), band=3, amb="sweep fork F26 (settled by the notes' pointer to the design page)",
    valid="'You win by killing every zombie on screen'", nothing="no brief exists, so the win row fails")
add(tag="b_lose", span="every", oes=[N["thr2"], N["gdd"], N["brief"]], fact="loss_rule", slot=["B4b"], what="the brief says how a level is lost",
    final="lost only when the zombies take our health to zero; a full tray is not a loss",
    title="The Agent's brief says a level is lost only when the zombies reach us and take our health (HP) to zero",
    values=f"`HP` / `health` to zero · sources {O.GDD['id']} ('not a fail state - the loss screen only appears at zero health'), {O.base('brian_winfail')['id']} ('deplete our HP') · rejects: a full tray as a loss · {fids('gdd', 'winfail')}",
    kind=("interpretation", "the design page's rule over a full tray, read with Brian's message"), band=3, amb="sweep fork F26 (settled)",
    valid="'You lose when the zombies get to you and your HP runs out; a full tray is a blunder, not a loss'", nothing="no brief exists, so the loss row fails")
add(tag="b_tray", span="every", oes=[N["gdd"], N["brief"]], fact="tray_slots", slot=["B4"], what="the brief says how many slots the tray has",
    final="7 slots", title="The Agent's brief says the tray has 7 slots", values=f"`7` slots · source {O.GDD['id']} ('7-slot tray'); comment {O.GDD_C2['id']} ('keep the GDD at 7 for now') · accepts: 7, seven · {fids('gdd')}",
    kind=("interpretation", "the page says 7; a comment on it tries 6 in a branch and is answered 'keep the GDD at 7'"), band=3, dist="ledger T11 (Julia's 6-slot comment) → a brief saying 6 fails",
    valid="'a 7-slot tray'", nothing="no brief exists, so the tray row fails")
for n in ("Rocket sound", "Explosion sound"):
    add(tag=f"b_held_{n}", span="every", oes=[N["sound"], N["brief"]], fact=f"sound_held:{n}", slot=["B6"] if n == "Rocket sound" else [],
        what=f"the brief says PlayableX cannot use the {n} yet", final=f"the brief holds the {n} back",
        title=f"The Agent's brief says PlayableX cannot use the {n} yet", values=f"`{n}` held back · source {O.SOUND_ID} ('{[r for r in O.SOUND_GRID if r[0] == n][0][1]}', 'no'); the notes' sound rule · {fids('c2', 'notes')}",
        kind=("multi-source", "the notes' sound rule applied to Calvin's sheet, which nothing links, against the ticket's 'Plays. In the outgoing folder.'"), band=5, decided="T4, C5",
        dist="ledger T6 (the five .wav notes) → a brief listing every exported sound as usable fails", valid=f"'Hold off on the {n.lower()} for now; we're making our own'",
        nothing=f"no brief exists, so the {n} row fails")
for n in ("Matching sound", "Success sound", "Failure sound"):
    add(tag=f"b_use_{n}", span="every", oes=[N["sound"], N["brief"]], fact=f"sound_usable:{n}", what=f"the brief says PlayableX can use the {n}",
        final=f"the {n} is among the sounds PlayableX can use", title=f"The Agent's brief lists the {n} among the sounds PlayableX can use",
        values=f"`{n}` usable · source {O.SOUND_ID} ('made here', 'yes') · {fids('c2')}", kind=("interpretation", "the sound rule applied to the sheet's row"), band=3,
        valid=f"'Sounds you can use: matching, success and failure'", nothing=f"no brief exists, so the {n} row fails")
add(tag="b_music", span="every", oes=[N["music"], N["brief"]], fact="music_start", slot=["B7"], what="the brief says when the music may start",
    final="after the player's first click or tap", title="The Agent's brief says the music may start only after the player's first click or tap",
    values=f"`after first click` · source {O.base('vendor_music_rule')['id']} ('music has to start after first click as a rule') · accepts: click, tap, touch, interaction · {fids('music')}",
    kind=("interpretation", "PlayableX's rule from the first playable, found in an older thread"), band=3, dist="Leonard's feedback doc (music at the first match) → not graded; a brief saying 'first match' fails",
    valid="'Music starts after the first tap'", nothing="no brief exists, so the music row fails")
add(tag="b_start", span="every", oes=[N["thr3"], N["brief"]], fact="start_date", slot=["B5"], what="the brief gives the start date",
    final="November 3, 2025", title="The Agent's brief gives the start date as November 3, 2025",
    values=f"`November 3` · source {O.base('vendor_nov3')['id']} ('the new start date for the game on November 3rd') · accepts: Nov 3, 3 November, 2025-11-03 (a date only; no time required) · {fids('nov3')}",
    kind=("lookup", "PlayableX's latest message in the pause thread"), band=1, dist="ledger T8 ('September 29', 'October 6th') → a brief with an earlier date fails",
    valid="'Start: Nov 3'", nothing="no brief exists, so the start-date row fails")

# ------------------------------------------------------------------ deliverable 2: the hand-off list (OE sheet, rows)
add(tag="sheet_doc", span="drive", oes=[N["sheet"]], fact="list_location", what="the hand-off list is a Google Sheet in Julia's own Drive",
    final="a Google Sheet owned by julia.lawson@harmonygames.co", title="The Agent creates the hand-off list as a Google Sheet owned by Julia (julia.lawson@harmonygames.co), in her own Drive",
    values=f"owner `julia.lawson@harmonygames.co` · Google Sheet · accepts: her root or any folder she owns · {fids('drive', 'ask')}", kind=("lookup", "the ask names the place and the type ('the hand-off list as a sheet')"), band=1,
    valid="a spreadsheet owned by Julia", nothing="no spreadsheet exists, so the location row fails")
add(tag="sheet_header", span="every", oes=[N["notes"], N["rows"]], fact="list_columns", what="the list has the notes' seven columns",
    final="columns Line, Category, Board set, State, What's owed, Who has it, Ticket", title="The Agent's hand-off list has the columns Line, Category, Board set, State, What's owed, Who has it and Ticket",
    values=f"`Line` `Category` `Board set` `State` `What's owed` `Who has it` `Ticket` · source the notes {O.NOTES_ID} ('with these columns: …') · accepts: header case and order as written or close equivalents ('What is owed') · {fids('notes')}",
    kind=("lookup", "the notes list the header"), band=1, valid="a header row with those seven names", nothing="no spreadsheet exists, so the header row fails")
keys = [l["name"] for l in O.LINES]
add(tag="sheet_volume", span="every", oes=[N["pack"], N["rows"]], fact="list_rows", slot=["V1"], what="one row per line of Brian's pack list",
    final="96 data rows, one for each line of the pack list, each line once", title="The Agent's hand-off list has 96 data rows, one for each line of Brian's pack list",
    values=f"`96` rows · source the Pack tab of {O.PACK_ID} (96 rows: 84 board items, 12 others) · {fids('pack')}",
    kind=("limited reconciliation", "a row per pack-list line, copied and checked line by line"), band=3, group="G1, G2, G3 volume",
    valid="96 rows in any order, Line spelled as on Brian's list", nothing="no spreadsheet exists, so the volume row fails")

def cell_row(tag, name, col, val, band, kind, slot, group, decided="—", dist="—", amb="—", accept="", extra_oes=(), dup="—"):
    l = L[name]; cls = l["cls"]
    src = SRC[cls] if col != "Board set" else (f"Robert's list {O.PICKS['id']} and his reply {O.C3['id']}" if name in ("Bow", "Dynamite") else f"Robert's list {O.PICKS['id']}")
    deciders = DECIDE_F.get(cls, []) if col != "Board set" else (["picks", "c3", "eight"] if name in ("Bow", "Dynamite") else ["picks", "eight"])
    oes = [N["tnotes"]] + list(extra_oes) + [N["rows"]]
    add(tag=tag, span="every", oes=oes, fact=f"{col.lower().replace(' ', '_').replace(chr(39), '')}:{name}", slot=slot,
        what=f"the {name} row's {col}", final=f"{col} {val} on the {name} row",
        title=f"The Agent's hand-off list gives {name} ({l['ticket']}) the {col} '{val}'" if col in ("State", "Board set") else
              (f"The Agent's hand-off list says what is owed for {name} ({l['ticket']}) is {val}" if col == "What's owed" else
               f"The Agent's hand-off list names {val} as who has {name} ({l['ticket']})"),
        values=f"`{name}` {col} `{val.split(' (')[0]}` · source {src}; note '{l['note'][:70]}' · {accept}{' · ' if accept else ''}{fids('line:' + name, *deciders)}",
        kind=kind, band=band, decided=decided, group=group, dist=dist, amb=amb, dup=dup,
        valid=f"a row '{name}' with {col} {val.split(' (')[0]}", nothing=f"no spreadsheet exists, so the {name} {col} row fails")

def st(tag, name, slot, group="G1 exception", band=5):
    l = L[name]; cls = l["cls"]
    m = MECH.get(cls)
    kind = ("multi-source", f"{SRC[cls].split(' (')[0]} against the line's own note") if m else ("interpretation", "the notes' state tests applied to the line's own note")
    extra = {"A1": (N["thr1"], N["a1"]), "A2": (N["a2"],), "C1": (N["design"], N["log"]), "C4": (N["log"],), "C2": (N["sound"],)}.get(cls, ())
    dist = {"A1": "ledger T2 (the note 'Opens, looks right') → Ready fails", "A2": "ledger T3 (the note 'FBX from Claire … Opens, looks right') → Ready fails",
            "C1": "ledger T5 (Robert's new colour versions) → Owed fails; the log's re-send makes it Ready", "C4": "ledger T4 (the note 'Zipped with the other instruments') → Ready fails",
            "C2": "ledger T6 (the note 'Exported .wav … Plays') → Ready fails"}.get(cls, "—")
    cell_row(tag, name, "State", l["state"], band if m else 3, kind, slot, group if m else "G1 sample (ordinary control)", decided=m[1] if m else "—", dist=dist,
             accept="accepts: the state word in any case", extra_oes=extra,
             dup=("fact also on the ticket move P(" + name + " move) (2 rows)" if name in ("Refrigerator", "Bathtub", "Cello", "Fly Zapper") else "—"))
for tag, name, slot in [("x_Refrigerator", "Refrigerator", ["X1"]), ("x_RetroTV", "Retro TV", ["X1b"]), ("x_Bathtub", "Bathtub", ["X2"]), ("x_Iron", "Iron", ["X2b"]),
                        ("x_Cactus", "Cactus Plant", ["X3"]), ("x_Cone", "Cone", ["X3b"]), ("x_Chainsaw", "Chainsaw", ["X8"]), ("x_Cello", "Cello", ["X4"]),
                        ("x_Trumpet", "Trumpet", ["X4b"]), ("x_Rocket", "Rocket sound", ["X5"]), ("x_Explosion", "Explosion sound", ["X5b"]),
                        ("x_RollingPin", "Rolling Pin", ["C1"]), ("x_FlyZapper", "Fly Zapper", ["C2"])]:
    st(tag, name, slot)
for tag, name, slot in [("o_Refrigerator", "Refrigerator", ["X6"]), ("o_Bathtub", "Bathtub", ["X7"]), ("o_Cello", "Cello", ["X9"]), ("o_Rocket", "Rocket sound", ["X10"])]:
    l = L[name]; cls = l["cls"]
    cell_row(tag, name, "What's owed", OWED_ACCEPT[cls].split(" (accept")[0], 5, ("multi-source", f"what is owed follows from {SRC[cls].split(' (')[0]}"), slot, "G2 exception",
             decided=MECH[cls][1], accept=OWED_ACCEPT[cls][OWED_ACCEPT[cls].index("(accept"):].strip("()"), extra_oes={"A1": (N["thr1"], N["a1"]), "A2": (N["a2"],), "C4": (N["log"],), "C2": (N["sound"],)}[cls],
             dup="fact also in the comment row for " + l["ticket"] + " (2 rows)")
for tag, name, slot in [("h_Refrigerator", "Refrigerator", ["X16"]), ("h_Bathtub", "Bathtub", ["X11"]), ("h_Iron", "Iron", ["X11b"]), ("h_Rocket", "Rocket sound", ["X12"]), ("h_Cello", "Cello", ["X17"])]:
    l = L[name]; cls = l["cls"]
    cell_row(tag, name, "Who has it", HOLD[l["who"]].split(" (")[0], 5, ("multi-source", "the holder follows from the deciding record and the notes' 'whoever has to do the next thing'"), slot, "G2 exception",
             decided=MECH[cls][1], accept=f"accepts: {HOLD[l['who']]}", extra_oes={"A1": (N["a1"],), "A2": (N["a2"],), "C4": (N["log"],), "C2": (N["sound"],)}[cls],
             amb={"C4": "sweep fork F17 (settled: Brian holds Claire's files)", "A1": "sweep fork F15 (settled: Marcus tells Brian)", "A2": "sweep fork F16 (settled: the file came from Claire)"}.get(cls, "—"),
             dup="fact also in the comment row for " + l["ticket"] + " (2 rows)")
for tag, name, slot, band, grp, dec in [("bs_Bow", "Bow", ["X13"], 5, "G3 exception", "T5, T15, C4"), ("bs_Dynamite", "Dynamite", ["X14"], 5, "G3 exception", "T5, T15, C4"),
                                        ("bs_Grenade", "Grenade", ["C4"], 3, "G3 sample (ordinary)", "—"), ("bs_RollingPin", "Rolling Pin", ["C5"], 3, "G3 sample (ordinary)", "—")]:
    cell_row(tag, name, "Board set", L[name]["board"], band, ("multi-source", "Robert's list read with his later reply") if band == 5 else ("interpretation", "the notes' Board set rule applied to Robert's list"),
             slot, grp, decided=dec, accept="accepts: the word in any case", extra_oes=(N["design"], N["bow"]),
             dup="fact also in the brief row on " + name + " (2 rows)" if name in ("Bow", "Grenade") else "—")
add(tag="sheet_ticket", span="every", oes=[N["pack"], N["rows"]], fact="ticket_col:Cannon", what="a row's Ticket as on Brian's list",
    final="the Cannon row's Ticket is DES-398", title="The Agent's hand-off list gives the Cannon row the Ticket DES-398",
    values=f"`Cannon` `DES-398` · source the Pack tab of {O.PACK_ID} · accepts: DES-398 or the ticket's link · {fids('pack', 'line:Cannon')}",
    kind=("lookup", "copied from the pack list"), band=1, group="G4 sample (Ticket column; the line PlayableX calls the rocket launcher)", valid="'DES-398' in the Cannon row", nothing="no spreadsheet exists, so the Ticket row fails")
add(tag="sheet_category", span="every", oes=[N["pack"], N["rows"]], fact="category_col:Iron", what="a row's Category as on Brian's list",
    final="the Iron row's Category is Bathroom", title="The Agent's hand-off list gives the Iron row the Category Bathroom",
    values=f"`Iron` `Bathroom` · source the Pack tab of {O.PACK_ID} · {fids('pack', 'line:Iron')}", kind=("lookup", "copied from the pack list"), band=1,
    group="G4 sample (Category column; a laundry item filed under Bathroom, sweep fork F10)", valid="'Bathroom' in the Iron row", nothing="no spreadsheet exists, so the Category row fails")

# ------------------------------------------------------------------ deliverable 3: the tickets (moves sampled; comments one row each)
MOVE_SAMPLES = [("Refrigerator", "W4", "EXPORT group"), ("Bathtub", None, "ARTHOLD group"), ("Cello", None, "ZIP group"), ("Fly Zapper", None, "an Owed line on its own note (waiting on Claire)"),
                ("Fonts", None, "the one line held outside the team (Martin)")]
for name, slot, why in MOVE_SAMPLES:
    l = L[name]; cls = l["cls"]; m = MECH.get(cls)
    add(tag=f"move_{name}", span="start", oes=[N["ticket"], move_oe(l["ticket"])], fact=f"ticket_state:{l['ticket']}", slot=[slot] if slot else [],
        what=f"{l['ticket']} moved to Todo", final=f"{l['ticket']} ({name}) in state Todo", title=f"The Agent moves {l['ticket']} ({name}) to Todo",
        values=f"`{l['ticket']}` `Todo` · rule: the notes ('An Owed line's ticket goes to Todo'); {name} is Owed by {SRC[cls].split(' (')[0]} · {fids('line:' + name, 'todo', *DECIDE_F.get(cls, []))}",
        kind=("interpretation", "the move follows the line's state") if m else ("lookup", "the line's own note leaves it Owed"), band=3 if m else 1, decided=m[1] if m else "—",
        group=f"G5 sample ({why})", dup=("fact also in the State row of " + name + " (2 rows)") if name in ("Refrigerator", "Bathtub", "Cello", "Fly Zapper") else "—",
        valid=f"{l['ticket']} in Todo", nothing=f"an idle run leaves {l['ticket']} In Progress, so the move row fails")
owed = O.by_state("Owed")
add(tag="move_volume", span="start", oes=[N["ticket"]] + [move_oe(l["ticket"]) for l in owed], fact="ticket_moves", what="one move to Todo per Owed line, and no other ticket moved",
    final=f"exactly {len(owed)} of DES-314 to DES-409 in Todo: the tickets of the Owed lines", title=f"The Agent moves exactly {len(owed)} of the pack's tickets (DES-314 to DES-409) to Todo, one for each Owed line of the hand-off list",
    values=f"`{len(owed)}` moves · template: one state change to Todo per Owed line (the notes) · the Delivered and Ready tickets keep their state · {fids('owed', 'todo')}",
    kind=("multi-source", "the exact set needs the full audit of all 96 lines"), band=5, decided="T1, T2, T4, T7, C1, C2, C5, C6", group="G5 volume",
    valid=f"the {len(owed)} Owed tickets in Todo, in any order", nothing="an idle run moves no ticket, so the volume row fails")
COMMENT = {"A1": ("a binary FBX export is owed", "Brian"), "A2": ("the file is owed again once the UVs are redone", "Claire"),
           "C4": ("the file is owed back in the outgoing folder", "Brian"), "C2": ("our own version of the sound is owed", "Calvin")}
for l in owed:
    cls = l["cls"]; m = MECH.get(cls)
    if cls in COMMENT: what, who = COMMENT[cls]
    else: what, who = f"{l['owed']} {'are' if l['owed'].endswith('files') else 'is'} owed", l["who"]
    extra = {"A1": [N["thr1"], N["a1"]], "A2": [N["a2"]], "C4": [N["log"]], "C2": [N["sound"]]}.get(cls, [N["tnotes"]])
    add(tag=f"comment_{l['ticket']}", span="start", oes=[N["ticket"]] + extra + [comm_oe(l["ticket"])], fact=f"comment:{l['ticket']}",
        slot={"A1": ["K1"], "A2": ["K2"], "C4": ["K4"], "C2": ["K5"]}.get(cls, []) if l["name"] in ("Refrigerator", "Bathtub", "Cello", "Rocket sound") else [],
        what=f"the comment on {l['ticket']} says what is owed and who has it", final=f"a comment on {l['ticket']}: {what}; {who} has it",
        title=f"The Agent comments on {l['ticket']} ({l['name']}) that {what} and that {who} has it",
        values=f"`{l['ticket']}` · owed: {OWED_ACCEPT.get(cls, l['owed'])} · who: `{who}` · source {SRC[cls].split(' (')[0]}; note '{l['note'][:60]}' · {fids('line:' + l['name'], *DECIDE_F.get(cls, []))}",
        kind=("interpretation", "what is owed and the holder follow from the deciding record and the notes' rule") if m else ("lookup", "the line's own note names the missing piece and who has it"),
        band=3 if m else 1, decided=m[1] if m else "—",
        dup=("facts also in the What's owed / Who has it rows of " + l["name"] + " (2 rows each)") if l["name"] in ("Refrigerator", "Bathtub", "Cello", "Rocket sound", "Iron") else "—",
        amb={"C4": "sweep fork F17 (settled)", "A1": "sweep fork F15 (settled)", "A2": "sweep fork F16 (settled)"}.get(cls, "—"),
        valid=f"a comment by Julia on {l['ticket']}: '{what.capitalize()}; {who} has it'", nothing=f"an idle run adds no comment, so the {l['ticket']} comment row fails")

# ------------------------------------------------------------------ shares (one row per share)
att = json.loads(O.HOLD["attendees_json"])
recips = [a["email"] for a in att if a["email"] != O.JULIA] + [O.CONTACT["email"]]
for lab, short, slotmap in (("the brief", "brief", {}), ("the hand-off list", "list", {"brian.foster@harmonygames.co": "D4"})):
    for r in recips:
        sl = slotmap.get(r) or ("D5" if r == O.CONTACT["email"] and short == "brief" else None)
        add(tag=f"share_{short}_{r.split('@')[0]}", span="start", oes=[N["hold"] if r != O.CONTACT["email"] else N["contact"], share_oe(lab, r)], fact=f"share:{short}:{r}",
            slot=[sl] if sl else [], what=f"{r} can view {lab}", final=f"{r} has reader access to {lab}",
            title=f"The Agent gives {r} view-only (reader) access to {lab}",
            values=f"`{r}` reader · source {'the contact ' + O.CONTACT['contact_id'] if r == O.CONTACT['email'] else 'the kickoff hold ' + O.HOLD_ID} and the notes ('Sharing: both files, view only') · {fids('recipients', 'hold' if r != O.CONTACT['email'] else 'contact')}",
            kind=("lookup", "the address is on the hold or in Contacts"), band=1, valid=f"{r} as a viewer of {lab}", nothing=f"an idle run shares nothing, so the {r} share row fails")

# ------------------------------------------------------------------ the DM and the channel post (content rows prove each write)
for s_, slot in (("Owed", "W1"), ("Ready", "W2"), ("Delivered", "W3")):
    add(tag=f"dm_{s_}", span="every", oes=[N["ask"], N["rows"], N["dm"]], fact=f"count:{s_}", slot=[slot] + (["D1"] if s_ == "Owed" else []),
        what=f"the reply to Frederick gives the {s_} count", final=f"a message from Julia in DM {O.DM_FRED} with {s_} {O.COUNTS[s_]}",
        title=f"The Agent tells Frederick in their DM that {O.COUNTS[s_]} lines are {s_}",
        values=f"`{s_}` `{O.COUNTS[s_]}` · DM `{O.DM_FRED}` · recomputed from the 96 lines (oe_gen/model.py, equal to solver/truth.json) · {fids('counts', 'ask')}",
        kind=("calculation", "a count over the full audit of the list"), band=3,
        decided={"Owed": "T1, T2, T4, T7, C1, C2, C5, C6", "Ready": "T1, T2, T3, T4, T7, C1, C2, C3, C5, C6", "Delivered": "—"}[s_],
        valid=f"'Delivered {O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, Owed {O.COUNTS['Owed']}' in the DM", nothing=f"an idle run sends nothing, so the {s_} count row fails")
for lab, short, slot in (("the brief", "brief", ["D2"]), ("the hand-off list", "list", ["D6"])):
    add(tag=f"post_{short}", span="links", oes=[N["ask"], N["thr1"], N["post"]], fact=f"post_link:{short}", slot=slot,
        what=f"the link of {lab} is posted in the PlayableX channel", final=f"a message from Julia in {O.VENDOR_CH} carrying the link of {lab}",
        title=f"The Agent posts the link of {lab} in the PlayableX channel ({O.VENDOR_CH})",
        values=f"channel `{O.VENDOR_CH}` · the link of {lab} (the file the Agent created) · accepts: a top-level post or a reply in the channel (brief §4b) · {fids('channel', 'drive')}",
        kind=("lookup", "the ask names the channel"), band=1, valid=f"a channel message holding the {lab} link", nothing=f"an idle run posts nothing, so the {lab} link row fails")

# the shortcut probe tests backticked literals: keep backticks only on answer-bearing literals (line names, ticket keys,
# addresses, distinctive phrases); generic words (column names, state words, first names, numbers) match hundreds of records
GENERIC = {"State", "Ticket", "Line", "Category", "Board set", "What's owed", "Who has it", "Default", "Extra", "Ready", "Owed", "Delivered", "extra",
           "Todo", "HP", "health", "walk", "Brian", "Claire", "Calvin", "Martin", "Bathroom", O.JULIA, O.DM_FRED, O.VENDOR_CH}
def degeneric(t):
    return re.sub(r"`([^`]+)`", lambda m: m.group(1) if (m.group(1) in GENERIC or m.group(1).isdigit()) else m.group(0), t)
for r in rows:
    r["values"] = degeneric(r["values"])
# a Values cell with no literal makes the probe fall back to the ledger's whole Expected cell (sentences that match
# nothing and take an hour on Snowflake); give each such row the short form its answer takes in the deliverable
PROBE_LIT = {"brief_doc": "Google Doc", "sheet_doc": "Google Sheet", "b_extras": "swap in", "b_anim": "one animation",
             "b_lose": "zero health", "b_tray": "7-slot", "sheet_header": "Who has it", "sheet_volume": "96 rows",
             "move_volume": "49 tickets", "dm_Owed": "Owed 49", "dm_Ready": "Ready 39", "dm_Delivered": "Delivered 8",
             "post_brief": O.VENDOR_CH, "post_list": O.VENDOR_CH}
LIT_RX = re.compile(r"`[^`]+`|\"[^\"]+\"|“[^”]+”")
for r in rows:
    if not LIT_RX.search(r["values"]):
        lit = PROBE_LIT[r["tag"]]
        r["values"] = f"probe form `{lit}` · " + r["values"]
assert all(LIT_RX.search(r["values"]) for r in rows)
for i, r in enumerate(rows, 1):
    r["P"] = f"P{i}"
TAG = {r["tag"]: r["P"] for r in rows}
for r in rows:   # resolve the P(...) placeholders in the duplication notes
    r["dup"] = re.sub(r"P\(([^)]+)\)", lambda m: TAG.get({"C4": "bs_Grenade", "X13": "bs_Bow"}.get(m.group(1), ""), None) or
                      TAG.get("move_" + m.group(1).replace(" move", ""), None) or m.group(0), r["dup"])
assert not [r for r in rows if "P(" in r["dup"]], [r["dup"] for r in rows if "P(" in r["dup"]]
assert len({r["fact"] for r in rows}) == len(rows), "a fact id is used twice"
(HERE / "rows.json").write_text(json.dumps(rows, indent=1, ensure_ascii=False) + "\n")
if __name__ == "__main__":
    from collections import Counter
    print(len(rows), "rows; weight", sum(r["band"] for r in rows), "; bands", Counter(r["band"] for r in rows))
