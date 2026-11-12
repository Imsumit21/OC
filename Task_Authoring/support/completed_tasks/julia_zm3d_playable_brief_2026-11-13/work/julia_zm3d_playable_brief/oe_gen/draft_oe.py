#!/usr/bin/env python3
"""Draft 08_Oracle_Events.md (draft mode of /create-oe-writing) from the ledger's model: oe_gen/model.py and facts.py.
Every quoted span is asserted to be an exact substring of its record (model.q); every count is computed from the rows.
Also writes oe_gen/out/oe_events.json (event number -> kind, ledger facts, records) for the check. Run from the workspace root.

rev2: every event is a tool action (read or write). The rev1 'derive' events (the eight, the Delivered, Owed and Ready
sets, the counts) were reasoning steps with no tool, which the rev1 completeness pass rated as non-action events; their
conclusions now sit on the read that settles them (the deciding record's read) or on the write that records them."""
import json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import model as O
import facts as FX
q, F, FL = O.q, FX.F, FX.FL

def pt(x): return O.when(x).split(" (")[0]            # 'Tue Sep 30 2025 11:21 AM PT'
def names(ls): return ", ".join(l["name"] for l in ls)
def tick(ls): return ", ".join(f"{l['name']} {l['ticket']}" for l in ls)
def Q(text, phrase): return '"' + q(text, phrase) + '"'

EV = []          # (kind, heading text, expected text, ledger facts, record ids)
def ev(kind, head, expected, facts=(), records=()):
    assert kind in ("read", "write"), kind
    EV.append({"kind": kind, "head": head, "expected": expected, "facts": [F(k) if not k.startswith("F") else k for k in facts], "records": list(records)})
    return len(EV)

G = {k: ls for k, _, ls in O.OWED_GROUPS}
def owed_line(ls): return f"{ls[0]['owed'].split(' (')[0]}, with {ls[0]['who']}"
ASK, NOTES = O.ASK["text"], O.NOTES["body_text"]
# ------------------------------------------------------------------ 1 the ask
n_ask = ev("read", f"Find Frederick's message of yesterday in Slack: search for \"playable\" on Sep 30 2025 and read Julia's direct messages with Frederick Stone",
   f"Frederick Stone, {pt(O.ASK['ts'])}, DM {O.DM_FRED}, ts {O.ASK['ts']}: \"{ASK}\"", ["ask"], [O.ASK["id"]])

# ------------------------------------------------------------------ 2 the notes
paras = [p.strip() for p in NOTES.split("\n\n") if p.strip()]
assert paras[0] == O.NOTES["title"] and len(paras) == 8, len(paras)
n_notes = ev("read", f"Find Frederick's hand-off notes in Google Drive (search \"hand-off notes\") and read the document in Google Docs (OE {n_ask})",
   f"Document \"{O.NOTES['title']}\", owner {O.drive(O.NOTES_ID)['owner_email']}, file {O.NOTES_ID}. " + " ".join(Q(NOTES, re.sub(r"\s*\n\s*", " ", p)) if "\n" not in p else Q(NOTES, p) for p in paras[1:]),
   ["notes"], [O.NOTES_ID])

# ------------------------------------------------------------------ 3 the pack list
cats = {}
for l in O.BOARD_ITEMS: cats.setdefault(l["category"], []).append(l)
kinds = {}
for l in O.NOT_BOARD: kinds.setdefault(l["kind"], []).append(l)
went = {}
for l in O.LINES:
    if l["went_out"]: went.setdefault(l["went_out"], []).append(l)
n_pack = ev("read", f"Find Brian's pack list in Google Drive (search \"pack list\") and read every row of its Pack tab in Google Sheets (OE {n_ask})",
   f"Spreadsheet \"{O.row('gsheets.sheets_spreadsheets', spreadsheet_id=O.PACK_ID)['title']}\", owner {O.drive(O.PACK_ID)['owner_email']}, file {O.PACK_ID}, tab \"Pack\", columns "
   f"{', '.join(O.PACK_GRID[0])}. 96 rows. Kind \"Board item\" on 84 rows, by Category, each line with its Ticket. "
   + " ".join(f"{c}: {tick(ls)}." for c, ls in cats.items())
   + f" The other 12 rows have no Category: " + "; ".join(f"Kind \"{k}\": {tick(ls)}" for k, ls in kinds.items()) + ". "
   + "Went out is filled on 8 rows: " + "; ".join(f"\"{w}\" on {names(ls)}" for w, ls in went.items()) + ".",
   ["pack"], [O.PACK_ID])

# ------------------------------------------------------------------ 4 the pack ticket
pt_ = O.ISSUES[O.PACK_TICKET]["row"]
n_ticket = ev("read", f"Open DES-314, the first ticket on the list, in Linear, go to its parent and list the parent's sub-tickets (OE {n_pack})",
   f"Parent {O.PACK_TICKET} \"{pt_['title']}\", team Design, created by Brian Foster (brian.foster@harmonygames.co in Linear), state {pt_['state_id']}: {Q(pt_['description'], 'One sub-ticket per line of the pack list, kept in Design so it stays off the ZM3D board. I leave a note on each one saying what I did with it. A line' + chr(39) + 's ticket closes when PlayableX have the file.')} "
   f"96 sub-tickets, DES-314 to DES-409, each titled with its line. State Done on 8: {tick(O.DONE)}. State In Progress on the other 88.",
   ["ticket"], [O.PACK_TICKET, "DES-314"])

# ------------------------------------------------------------------ 5 the notes on the tickets, and the lines they leave Owed themselves
groups = O.note_groups()
def gtxt(note, ls):
    if len(ls) == 1: return f"{ls[0]['name']}: \"{note}\""
    return f"\"{note}\" on {len(ls)}: {names(ls)}."
vis = {}
for l in G["VIS"]: vis.setdefault((l["owed"], l["who"]), []).append(l)
n_tnotes = ev("read", f"Read Brian's note, the one comment, on each of the 96 sub-tickets in Linear (list the comments of DES-314 to DES-409) (OE {n_ticket})",
   "One comment by Brian Foster (brian.foster@harmonygames.co) on every ticket. " + " ".join(gtxt(n, ls) for n, ls in groups)
   + f" By the notes' Owed rule (OE {n_notes}), these lines are Owed on their own note: "
   + " ".join(f"{names(ls)}: {owed}, with {who}." for (owed, who), ls in vis.items()),
   ["ticket", "owed"] + [FL(l["name"]) for l in O.LINES], [l["ticket"] for l in O.LINES])

# ------------------------------------------------------------------ 6-9 the PlayableX channel
fr, fs, vf = O.base("fred_retention"), O.base("fred_scenario1"), O.base("vendor_formats")
n_thr1 = ev("read", f"Find the PlayableX channel in Slack (channel search \"playablex\", private channels included; it is {O.VENDOR_CH}), read its history for September 2025 and the thread under Frederick's Sep 12 message (OE {n_notes})",
   f"Channel {O.VENDOR_CH}. Frederick Stone, {pt(fr['ts'])}, ts {fr['ts']}: {Q(fr['text'], 'I think Scenario 1 is a good bet for filtering out the players that won' + chr(39) + 't like our game, while remaining true to our core game play.')} "
   f"Frederick Stone, {pt(fs['ts'])}, ts {fs['ts']}: {Q(fs['text'], 'lets go with Scenario 1.')} "
   f"{vf['user']} of PlayableX, {pt(vf['ts'])}, ts {vf['ts']}: {Q(vf['text'], 'aside from the 8-item set that you will provide for the board, you can also test any additional items you’d like to try in the game')}; "
   f"{Q(vf['text'], '*3D assets*: .fbx, .glb, or .blend (when exporting .fbx, please make sure it’s exported in *Binary format*, not ASCII)')}; {Q(vf['text'], '*Sound*: .mp3 or .wav')}",
   ["purpose", "scenario", "formats", "channel"], [fr["id"], fs["id"], vf["id"]])

z1, bw, vd, z2, vb, z3, vz = (O.base(k) for k in ("brian_zip1", "brian_winfail", "vendor_duck", "brian_zip2", "vendor_blank_scene", "brian_pack3", "vendor_zombie_ask"))
DELIVERED = O.by_state("Delivered")
n_thr2 = ev("read", f"Read the thread under Frederick's Sep 18 message in the PlayableX channel in Slack, where Brian sent the assets (thread ts {z1['thread_ts']}) (OE {n_tnotes})",
   f"Brian Foster, {pt(z1['ts'])}, ts {z1['ts']}: {Q(z1['text'], 'You can access the game assets here.')} with the file {z1['files'][0]}. "
   f"Brian Foster, {pt(bw['ts'])}, ts {bw['ts']}: {Q(bw['text'], 'The fail condition in the game is when zombies reach us and deplete our HP, while the win condition is eliminating all the zombies on screen')}. "
   f"{vd['user']} of PlayableX, {pt(vd['ts'])}, ts {vd['ts']}: {Q(vd['text'], 'At this stage, the only missing piece seems to be the duck asset used in the reference.')} "
   f"Brian Foster, {pt(z2['ts'])}, ts {z2['ts']}: {Q(z2['text'], 'Sure, I’m sending the files.')} with the file {z2['files'][0]}. "
   f"{vb['user']} of PlayableX, {pt(vb['ts'])}, ts {vb['ts']}: {Q(vb['text'], FX.VB_SENT)} "
   f"Brian Foster, {pt(z3['ts'])}, ts {z3['ts']}: {Q(z3['text'], 'Sorry, it took a little while, I had to get help from our animator')} with the file {z3['files'][0]}. "
   f"{vz['user']} of PlayableX, {pt(vz['ts'])}, ts {vz['ts']}: {Q(vz['text'], 'We have reviewed the assets.')}; {Q(vz['text'], 'Select the primary animation you want us to use (attack, idle, die, or walk), and')}; "
   f"{Q(vz['text'], 'Specify the 4 zombie characters to which this animation should be applied.')} "
   f"With the Done tickets and their notes (OE {n_ticket}, OE {n_tnotes}) and the notes' Delivered rule (OE {n_notes}), these {len(DELIVERED)} lines are Delivered: {names(DELIVERED)}.",
   ["sent", "winfail", "delivered"], [z1["id"], bw["id"], vd["id"], z2["id"], vb["id"], z3["id"], vz["id"]])

fp, vn = O.base("fred_pause"), O.base("vendor_nov3")
n_thr3 = ev("read", f"Read the thread under Frederick's Sep 29 message in the PlayableX channel in Slack (thread ts {fp['ts']}) for the start date (OE {n_ask})",
   f"Frederick Stone, {pt(fp['ts'])}, ts {fp['ts']}: {Q(fp['text'], 'I think we should pause development of the playable for a month or so')}. "
   f"{vn['user']} of PlayableX, {pt(vn['ts'])}, ts {vn['ts']}: {Q(vn['text'], 'We’re planning the new start date for the game on November 3rd.')}",
   ["pause", "nov3"], [fp["id"], vn["id"]])

vm = O.base("vendor_music_rule")
n_music = ev("read", f"Search Slack for \"music\" in the PlayableX channel to find their rule from the first playable about when the music may start (OE {n_notes})",
   f"{vm['user']} of PlayableX, {pt(vm['ts'])}, ts {vm['ts']}, in {O.VENDOR_CH}: {Q(vm['text'], 'music has to start after first click as a rule')}",
   ["music"], [vm["id"]])

# ------------------------------------------------------------------ 10-11 #zombie-design and Robert's picks
rc, p22r, p22j = O.base("robert_new_colours"), O.base("purpose_robert_22sep"), O.base("purpose_julia_22sep")
p22q, p22m, p22s = O.base("julia_shuriken_idea"), O.base("purpose_robert_matter"), O.base("robert_remain")
n_design = ev("read", f"Read #zombie-design in Slack from Sep 22 2025 on (channel history, and the thread under Brian's Sep 22 post about the playable scenario) for what the playable is for, Robert's picks and what he posted after them (OE {n_ask})",
   f"Robert, {pt(p22r['ts'])}, ts {p22r['ts']}: {Q(p22r['text'], 'the idea is to test the current form and audience fit')}; Julia Lawson, {pt(p22j['ts'])}, ts {p22j['ts']}: "
   f"{Q(p22j['text'], 'do a more hardcore friendly playable and see how they do with the funnel')}; Julia Lawson, {pt(p22q['ts'])}, ts {p22q['ts']}: "
   f"{Q(p22q['text'], 'Do you want to try a cute level with lots of grenades and shruiken then?')}; Robert, {pt(p22m['ts'])}, ts {p22m['ts']}: {Q(p22m['text'], 'Doesn' + chr(39) + 't really matter')}; "
   f"Robert, {pt(p22s['ts'])}, ts {p22s['ts']}: {Q(p22s['text'], 'I think we should remain as is')}. So the playable tests the game in its current form and its audience fit; the "
   f"hardcore-friendly line is walked back (with the ask's {Q(ASK, 'Write it for the game as it is today')}, OE {n_ask}). "
   f"Robert, {pt(O.PICKS['ts'])}, ts {O.PICKS['ts']}: {Q(O.PICKS['text'], 'For the playable board, the 8: Grenade, Couch and Plushie Chick from the reference level, plus Shuriken, Cute Axe, Gift Box, Cactus Plant and Dynamite.')} "
   f"{Q(O.PICKS['text'], 'Everything else')} Brian Foster (tagged) {Q(O.PICKS['text'], 'sends them is extras they can swap in.')} "
   f"Robert, {pt(O.ZPICKS['ts'])}, ts {O.ZPICKS['ts']}: {Q(O.ZPICKS['text'], 'one animation, walk. The 4 zombies: Party Girl, Plumber, Magician, Football Player. All four are in the pack Marcus sent.')} "
   f"Robert, {pt(rc['ts'])}, ts {rc['ts']}: {Q(rc['text'], 'Got new colored version of cactus, chainsaw and cones that can probably come in handy:')} — later than the Thu Sep 25 notes on "
   f"{names(O.members('C1'))} (OE {n_tnotes}).",
   ["purpose", "picks", "zpicks", "c1"], [p22r["id"], p22j["id"], p22q["id"], p22m["id"], p22s["id"], O.ASK["id"], O.PICKS["id"], O.ZPICKS["id"], rc["id"]])

bow, bowc = O.base("art_bow_root"), O.base("art_bow_claire")
n_bow = ev("read", f"Check whether Robert changed a pick since Sep 25: search Slack for his messages from that day on and read the thread under Julia's bow post in #zombie-art (OE {n_ask}, OE {n_design})",
   f"Julia Lawson, {pt(bow['ts'])}, ts {bow['ts']}: {Q(bow['text'], 'Can we have arrow to go with the bow?')} Claire Morgan, {pt(bowc['ts'])}, ts {bowc['ts']}: \"{bowc['text']}\". "
   f"Robert, {pt(O.C3['ts'])}, ts {O.C3['ts']}: \"{O.C3['text']}\" His Sep 25 list ends with {O.SWAPPED_OUT}, so the eight on the board are {', '.join(O.EIGHT)}; "
   f"{O.SWAPPED_OUT} stays on the pack list as an extra.",
   ["bowroot", "c3", "eight"], [bow["id"], bowc["id"], O.C3["id"]])

# ------------------------------------------------------------------ 12-15 the deciding records, each with the lines it settles
n_a1 = ev("read", f"Read #zombie-match3d in Slack from Sep 25 2025 on (channel history) for anything said about Brian's exports after his notes (OE {n_notes}, OE {n_tnotes})",
   f"Marcus Bennett, {pt(O.A1['ts'])}, ts {O.A1['ts']}, tagging Brian Foster: {Q(O.A1['text'], 'fyi the models you got out of unity on thursday are the text kind, the setting was wrong that day so youll need to redo them. they open fine in unity and in max so you wouldnt notice.')} "
   f"{Q(O.A1['text'], 'the ones from')} Claire Morgan (tagged) {Q(O.A1['text'], 'are ok')}. With PlayableX's Binary-only rule (OE {n_thr1}), the {len(G['A1'])} lines whose note says "
   f"\"FBX saved out of the project, Thu 25 Sep\" (OE {n_tnotes}) are Owed: {owed_line(G['A1'])}: {names(G['A1'])}.",
   ["a1", "owed"], [O.A1["id"]] + [l["ticket"] for l in G["A1"]])

n_a2 = ev("read", f"Read Julia's direct messages with Robert in Slack from Sep 25 2025 on (conversation history) (OE {n_notes}, OE {n_tnotes})",
   f"Robert, {pt(O.A2['ts'])}, DM {O.DM_ROBERT}, ts {O.A2['ts']}, tagging Claire Morgan: {Q(O.A2['text'], 'is redoing the UVs on the bathroom objects from scratch, so the old ones will show in the levels for a bit.')} "
   f"{Q(O.A2['text'], 'the bathroom files she gave')} Brian Foster (tagged) {Q(O.A2['text'], 'on Friday are the old version too')}. So the {len(G['A2'])} Bathroom lines whose note says "
   f"\"FBX from Claire, Fri 26 Sep\" (OE {n_tnotes}) are Owed: {owed_line(G['A2'])}: {names(G['A2'])}.",
   ["a2", "owed"], [O.A2["id"]] + [l["ticket"] for l in G["A2"]])

LOG = O.LOG["body_text"]
C1 = O.members("C1")
n_log = ev("read", f"Find Brian's log of the outgoing folder in Google Drive (search \"outgoing folder\") and read it in Google Docs (OE {n_notes}, OE {n_tnotes})",
   f"Document \"{O.LOG['title']}\", owner {O.drive(O.LOG_ID)['owner_email']}, file {O.LOG_ID}. {Q(LOG, 'Fri 26 Sep: more files from Claire. The music instruments went in as one zip. The .wav exports.')} "
   + Q(LOG, "Tue 30 Sep: Claire sent the three recoloured models again. Opened them, they look right, and they replace Thursday's.") + " "
   + Q(LOG, "The zip with Friday's music instruments got cut off on upload, it won't unpack on my side, and those eight aren't in the folder any other way. I still have Claire's files, I'll put them back when we pick this up again.")
   + f" So {names(C1)}, the three with new colour versions (OE {n_design}), are current and in the folder again: Ready. The {len(G['C4'])} instrument lines whose note says "
   f"\"Zipped with the other instruments\" (OE {n_tnotes}) are Owed: {owed_line(G['C4'])}: {names(G['C4'])}.",
   ["c4", "c1", "ready", "owed"], [O.LOG_ID] + [l["ticket"] for l in C1 + G["C4"]])

SG = {r[0]: r for r in O.SOUND_GRID[1:]}
def srow(n): return f"{n}: " + ", ".join(f"\"{c}\"" for c in SG[n][1:] if c)
assert SG["Matching sound"][1:] == SG["Success sound"][1:] == SG["Failure sound"][1:] == ["made here", "yes", ""]
n_sound = ev("read", f"Find Calvin's sound sources sheet in Google Drive (search \"sound\") and read its Sources tab in Google Sheets (OE {n_notes})",
   f"Spreadsheet \"{O.row('gsheets.sheets_spreadsheets', spreadsheet_id=O.SOUND_ID)['title']}\", owner {O.drive(O.SOUND_ID)['owner_email']}, file {O.SOUND_ID}, tab \"Sources\", columns {', '.join(O.SOUND_GRID[0])}. "
   f"Matching sound, Success sound and Failure sound: \"made here\", \"yes\". {srow('Rocket sound')}. {srow('Explosion sound')}. {srow('Background music')}. "
   f"By the notes' sound rule (OE {n_notes}), {names(G['C2'])}, exported on Fri 26 Sep (OE {n_tnotes}), are Owed: {owed_line(G['C2'])}.",
   ["c2", "owed"], [O.SOUND_ID] + [l["ticket"] for l in G["C2"]])

# ------------------------------------------------------------------ 16-19 the brief's other sources, the hold, the contact
DS = {t: b for t, b, _, _ in O.DECK_SLIDES}
n_deck = ev("read", f"Read Julia's deck of the reference level in Google Slides (search Google Drive for \"reference level\") (OE {n_notes})",
   f"Presentation \"{O.drive(O.DECK_ID)['name']}\", owner {O.drive(O.DECK_ID)['owner_email']}, file {O.DECK_ID}. Slide \"Board\": \"{DS['Board']}\" Slide \"Zombies\": \"{DS['Zombies']}\" "
   f"Slide \"Win and lose\": \"{DS['Win and lose']}\"",
   ["deck"], [O.DECK_ID])

n_gdd = ev("read", f"Open the design page in Confluence (search \"7-slot tray\" or the title) and read its core mechanic and its comments (OE {n_notes})",
   f"Page \"{O.GDD['title']}\", {O.GDD['id']}: {Q(O.GDD_TEXT, 'the player drags items into a 7-slot tray')}; {Q(O.GDD_TEXT, 'It is a tempo penalty, not a fail state - the loss screen only appears at zero health.')} "
   f"Comments: Julia Lawson: {Q(O.GDD_C1['body'], 'I pulled the 7-slot tray down to 6 in a soft-test branch')}; Robert: {Q(O.GDD_C2['body'], 'keep the GDD at 7 for now')}.",
   ["gdd"], [O.GDD["id"]])

att = json.loads(O.HOLD["attendees_json"])
n_hold = ev("read", f"Find the kickoff hold on Julia's calendar in Google Calendar (search \"kickoff\", November 2025) (OE {n_notes})",
   f"Event \"{O.HOLD['summary']}\", {O.HOLD_ID}, starts {pt(O.HOLD['start_ts'])}, organizer {O.HOLD['organizer_email']}. Attendees: {', '.join(a['email'] for a in att)}.",
   ["hold"], [O.HOLD_ID])

n_contact = ev("read", f"Look up PlayableX's intake address in Contacts (search \"PlayableX\") (OE {n_notes})",
   f"Contact \"{O.CONTACT['first_name']} {O.CONTACT['last_name']}\", \"{O.CONTACT['job']}\", {O.CONTACT['email']}.",
   ["contact"], [O.CONTACT["contact_id"]])

# ------------------------------------------------------------------ the two files
n_brief = ev("write", f"Create the brief as a Google Doc in Julia's Drive (Google Docs, a new document with its text) (OE {n_ask}, OE {n_notes})",
   f"A new document owned by Julia, in her Drive, that PlayableX can build from. It says: the scenario is Scenario 1, picked to filter out the players that won't like our game while remaining true to our core game play "
   f"(OE {n_thr1}), and there to test the game in its current form and its audience fit, not what the game could be tailored to become (OE {n_design}); "
   f"the eight on the board are {', '.join(O.EIGHT)}, and every other board item on Brian's list is an extra they can swap in (OE {n_bow}); "
   f"the four zombies are Party Girl, Plumber, Magician and Football Player and the one animation is walk (OE {n_design}); a level is won when every zombie on screen is eliminated and lost when the zombies reach us and "
   f"our HP runs out (OE {n_thr2}, OE {n_deck}, OE {n_gdd}); the tray has 7 slots (OE {n_gdd}); for sound they can use Matching sound, Success sound and Failure sound, Rocket sound and Explosion sound stay with us until we have our own "
   f"versions, and the background music is a new track for the ad that Calvin is still cutting (OE {n_sound}, OE {n_tnotes}); the music may start after the first click (OE {n_music}); the start date is November 3 (OE {n_thr3}).",
   ["drive", "scenario", "purpose", "eight", "zpicks", "deck", "gdd", "winfail", "c2", "music", "nov3"])

n_sheet = ev("write", f"Create the hand-off list as a Google Sheet in Julia's Drive (Google Sheets, a new spreadsheet) (OE {n_ask})",
   "A new spreadsheet owned by Julia, in her Drive.", ["drive"])

OWED_SRC = {"VIS": n_tnotes, "A1": n_a1, "A2": n_a2, "C4": n_log, "C2": n_sound}
READY = O.by_state("Ready")
n_rows = ev("write", f"Write the header and the 96 rows into the hand-off list (Google Sheets, update values on the spreadsheet of OE {n_sheet})",
   f"Header: Line, Category, Board set, State, What's owed, Who has it, Ticket. One row per line of Brian's pack list, 96 rows, with Line, Category and Ticket as on his list (OE {n_pack}). "
   f"Board set is Default on the eight of OE {n_bow}, Extra on the other 76 board items and empty on the 12 lines that are not board items. "
   f"State is Delivered on the {O.COUNTS['Delivered']} lines of OE {n_thr2}; Owed on the {O.COUNTS['Owed']} lines of " + ", ".join(f"OE {OWED_SRC[k]}" for k in ("VIS", "A1", "A2", "C4", "C2"))
   + f", each with what is owed and who has it as stated there; and Ready on the other {O.COUNTS['Ready']}, whose note says the file is exported, opens or plays and is in the outgoing folder "
   f"(OE {n_tnotes}, with {names(C1)} current again by OE {n_log}): {names(READY)}.",
   ["boardset", "delivered", "ready", "owed"])

# ------------------------------------------------------------------ shares
recips = [a["email"] for a in att if a["email"] != O.JULIA] + [O.CONTACT["email"]]
assert recips == ["brian.foster@harmonygames.co", "frederick.stone@harmonygames.co", "robert@harmonygames.co", "intake@playablex.ai"], recips
for label, n_file in (("the brief", n_brief), ("the hand-off list", n_sheet)):
    for r in recips:
        src = f"OE {n_contact}" if r == O.CONTACT["email"] else f"OE {n_hold}"
        ev("write", f"Share {label} (OE {n_file}) with {r} as a viewer in Google Drive (OE {n_notes}, {src})",
           f"{r} has reader access to {label}.", ["recipients"])

# ------------------------------------------------------------------ tickets
COMMENT = {"A1": "a binary FBX export is owed; Brian has it", "A2": "the file is owed again once the UVs are redone; Claire has it",
           "C4": "the file is owed back in the outgoing folder; Brian has it", "C2": "our own version of the sound is owed; Calvin has it"}
def comment_text(l):
    if l["cls"] in COMMENT:
        assert COMMENT[l["cls"]].endswith(l["who"] + " has it")
        return COMMENT[l["cls"]]
    plural = l["owed"].endswith("files")
    return f"{l['owed']} {'are' if plural else 'is'} owed; {l['who']} has {'them' if plural else 'it'}"
for l in O.by_state("Owed"):
    ev("write", f"Move {l['ticket']} ({l['name']}) to Todo in Linear (OE {n_notes}, OE {OWED_SRC[l['cls']]})", f"{l['ticket']} is in state Todo.", [FL(l["name"])], [l["ticket"]])
    ev("write", f"Comment on {l['ticket']} ({l['name']}) in Linear what is owed and who has it (OE {n_notes}, OE {OWED_SRC[l['cls']]})",
       f"A comment by Julia on {l['ticket']}: {comment_text(l)}.", [FL(l["name"])], [l["ticket"]])

# ------------------------------------------------------------------ the two messages
ev("write", f"Give Frederick the count for each state in Slack, in the direct messages where he asked (OE {n_ask}, OE {n_rows})",
   f"A message from Julia in DM {O.DM_FRED}: Delivered {O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, Owed {O.COUNTS['Owed']}.", ["counts", "ask"], [O.DM_FRED])
SHARE_N = [i + 1 for i, e in enumerate(EV) if e["head"].startswith("Share ")]
assert len(SHARE_N) == 8
ev("write", f"Post both links in the PlayableX channel in Slack once both files are written and shared (OE {n_ask}, OE {n_thr1}, OE {n_brief}, OE {n_sheet}, OE {n_rows}, "
   + ", ".join(f"OE {k}" for k in SHARE_N) + ")",
   f"A message from Julia in {O.VENDOR_CH} with the link of the brief (OE {n_brief}) and the link of the hand-off list (OE {n_sheet}).", ["channel"], [O.VENDOR_CH])

# ------------------------------------------------------------------ output
blocks = [f"OE {i}  {e['head']}\nExpected: {e['expected']}" for i, e in enumerate(EV, 1)]
text = "\n\n".join(blocks) + "\n"
assert "|" not in text.replace("||", ""), "pipe in event text"
# every line is set once: Delivered on the hand-over read, Owed on the read of its deciding record, Ready on the rows write
settled = {"Delivered": EV[n_thr2 - 1]["expected"], "Ready": EV[n_rows - 1]["expected"]}
for l in O.LINES:
    where = settled.get(l["state"]) or EV[OWED_SRC[l["cls"]] - 1]["expected"]
    assert l["name"] in where, (l["name"], l["state"])
if __name__ == "__main__":
    (O.TASK / "08_Oracle_Events.md").write_text(text)
    for i, e in enumerate(EV, 1): e["n"] = i
    (HERE / "out" / "oe_events.json").write_text(json.dumps(EV, indent=1, ensure_ascii=False) + "\n")
    kinds_ = {}
    for e in EV: kinds_[e["kind"]] = kinds_.get(e["kind"], 0) + 1
    print("events", len(EV), kinds_, "| characters", len(text), "(300-50,000)", "| longest", max(len(b) for b in blocks))
