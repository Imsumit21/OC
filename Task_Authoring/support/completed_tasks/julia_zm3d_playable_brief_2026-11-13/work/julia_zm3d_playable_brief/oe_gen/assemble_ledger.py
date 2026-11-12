#!/usr/bin/env python3
"""Assemble Working_Files/08_OE_Writing_Ledger.md (prep mode of /create-oe-writing) from oe_gen/facts.py.
Runs persona_view check-sql and can-see for the visibility proof and pastes their lines verbatim. Run from the workspace
root, then: python3 -B Task_Authoring/tools/stage_gate.py oe-writing Task_Authoring/task_inputs --paste"""
import datetime as D, hashlib, json, os, re, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import model as O
import facts as FX
F, FL = FX.F, FX.FL
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(O.TASK))
OUT = O.WF / "08_OE_Writing_Ledger.md"
REL = "Task_Authoring/task_inputs"
ctx = json.loads((O.WF / "00_Task_Context.json").read_text())
CLOCK = re.sub(r"^Clock:\s*", "", ctx["universe"]["clock_line"])
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]
def cell(s): return re.sub(r"\s+", " ", str(s)).replace("|", "/").strip()
def table(header, rows):
    return ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)] + ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
def span(s):
    assert s in O.PROMPT, s
    return '"' + s + '"'

# ------------------------------------------------------------------ absence fact text (from oe_gen/out/absence_check.json)
ab = json.loads((HERE / "out" / "absence_check.json").read_text())
T = ab["targets"]
assert len(T) == 44 and all(v["complete"] for v in T.values())
n_hits = sum(v["since"] for v in T.values())
def hit(name, hid):
    assert any(h["id"] == hid for h in T[name]["hits"]), (name, hid)
    return hid
reskins = [hit("Bench", "C090N54TG79/1758757026.873959"), hit("Wooden Tower", "C090N54TG79/1758757641.634929"),
           hit("Desk Lamp", "C090N54TG79/1758759686.056119"), hit("Spatula", "C090N54TG79/1758760095.485329")]
plane = hit("Toy Airplane", "C05433XK267/1758833093.686429"); pot = hit("Flower Pot", "C08R8CHB0QL/1758752162.419659")
tower = hit("Wooden Tower", "D05GU6L0XFH/1758905765.333669")
ctl = ab["controls"]
assert "C090N54TG79/1759189466.554739" in [h["id"] for h in ctl["cactus"]["hits"]] and "C08R8CHB0QL/1758904025.123869" in [h["id"] for h in ctl["bow"]["hits"]]
seeded_other = sorted({f"SQL L{h['line']}" for v in ab["seeded"].values() for h in v})
def d(i): return O.day_pt(i.split("/")[1])
RS = ab["resent"]; assert set(RS) == {"Cactus Plant", "Chainsaw", "Cone"} and all(v["complete"] and v["since"] == 0 for v in RS.values()), RS
ABSENCE = (f"The 44 Delivered and Ready lines that no later record touches (every Delivered or Ready line but Cactus Plant, Chainsaw and Cone) searched by name in every Slack container Julia can open, from Wed Sep 24 2025 (the first zip) to the clock: {n_hits} hits, "
           f"all 44 result lists complete. None says that a Delivered or Ready file changed after it went out or was exported, or is being redone. Hits that name an item: "
           f"Robert's posts {', '.join(reskins)} ({d(reskins[0])}) show other items built on the bench, wooden tower, desk lamp and spatula models and are older than those four files "
           f"({O.BY['Bench']['note'][:28]} {O.BY['Wooden Tower']['note'][:28]}); the build note 'Toy Airplane Redone (Still not working)' is first listed in {plane} ({d(plane)}), "
           f"older than that file ('{O.BY['Toy Airplane']['note'][:28]}'); {pot} ({d(pot)}) is older than the Flower Pot file ('{O.BY['Flower Pot']['note'][:28]}'); "
           f"{tower} ({d(tower)}) is older than the Wooden Tower file; the vendor's question in {O.base('vendor_zombie_ask')['id']} is answered in {F('zpicks')}; "
           f"the rest match part of a word (safety, bowl, background) or design talk. Positive controls found by the same search: C090N54TG79/1759189466.554739 (cactus), "
           f"C08R8CHB0QL/1758904025.123869 (bow). In the overlay the 44 names occur outside their own ticket, note and list row only in {', '.join(seeded_other)} "
           f"(Robert's eight and Julia's deck). Cactus Plant, Chainsaw and Cone: Robert's new colour versions ({O.base('robert_new_colours')['id']}, {d(O.base('robert_new_colours')['id'])}) are "
           f"followed by Brian's log {O.LOG_ID}, whose Tue Sep 30 entry records them sent again; the same search from Tue Sep 30 to the clock finds no message naming any of the three "
           f"(0 hits each, result lists complete).")
for f in FX.FACTS:
    if f["key"] == "absence": f["expected"] = ABSENCE

# ------------------------------------------------------------------ A
line_ids = lambda cls: ", ".join(FL(l["name"]) for l in O.members(cls))
all_lines = f"{FL(O.LINES[0]['name'])} to {FL(O.LINES[-1]['name'])}"
A = [
 ("R1", span("Frederick's playable message from yesterday"), "Discovery: the source message, his DM of Tue Sep 30 2025", "Explicit", F("ask")),
 ("R2", span("Can you do everything he's asking for in it, start to finish?"), "Constraint: every ask in the message applies, with the three things it starts from and his hand-off notes",
  f"Explicit (contents through {F('ask')} and {F('notes')})", f"{F('ask')}, {F('notes')}, {F('pack')}, {F('ticket')}"),
 ("R3", span("everything he's asking for in it"), f"Write: the brief as a doc ({F('ask')}: 'write the brief they build from'; 'Brief as a doc')",
  f"Implicit: the span takes in the message, and the message asks for the brief", ", ".join(F(k) for k in ("notes", "scenario", "purpose", "eight", "zpicks", "deck", "gdd", "winfail", "c2", "music", "nov3"))),
 ("R4", span("everything he's asking for in it"), f"Discovery and Write: where the item pack stands, as the hand-off list, a sheet with one row per line of the pack list ({F('ask')}: 'tell me where the item pack actually stands'; 'the hand-off list as a sheet')",
  "Implicit: the message asks for it; the notes set its columns and the three states",
  f"{F('pack')}, {F('ticket')}, {all_lines}, " + ", ".join(F(k) for k in ("formats", "a1", "a2", "c1", "c4", "c2", "sent", "absence", "delivered", "ready", "owed", "boardset"))),
 ("R5", span("start to finish"), f"Write: the ticket follow-through ({F('ask')}: 'what to do with the tickets'; {F('notes')}: 'An Owed line's ticket goes to Todo with a comment saying what is owed and who has it')",
  "Implicit: the message hands the tickets to the notes", f"{F('notes')}, {F('ticket')}, {F('todo')}, {F('owed')}"),
 ("R6", span("start to finish"), f"Write: both files shared view only ({F('ask')}: 'who gets the files'; {F('notes')}: 'Sharing: both files, view only')",
  "Implicit: the message hands the sharing to the notes", f"{F('notes')}, {F('hold')}, {F('contact')}, {F('recipients')}"),
 ("R7", span("everything he's asking for in it"), f"Tell: the count for each state, to Frederick in the DM ({F('ask')}: 'Then give me the count for each state here')",
  "Implicit: the message asks for it", f"{F('ask')}, {F('counts')}"),
 ("R8", span("The files he wants should end up in my Drive"), "Constraint: both files are in Julia's Drive", "Explicit", f"{F('drive')}, {F('ask')}"),
 ("R9", span("once they're ready the links go in the PlayableX channel like he says"), "Write: both links posted in the PlayableX channel", "Explicit", f"{F('channel')}, {F('ask')}"),
]

# ------------------------------------------------------------------ B
B = [(f["F"], f["fact"], f["service"], f["tools"], f["locator"], f["origin"], f["expected"], f["result"], f["visible"], f["depends"], f["source"]) for f in FX.FACTS]
b_text = "\n".join(table(["F", "Fact / value", "Service", "Tool family (catalog)", "Locator", 'Locator origin (prompt · F-n · search "query text")',
                          "Expected data (dates typed: created / starts / due)",
                          "Ledger result for the Expected line (VERIFIED quote · not_a_claim · ABSENCE evidence_check · UNRESOLVED)",
                          "Persona-visible? (proof)", "Depends on", "Source pointer"], B))

# ------------------------------------------------------------------ visibility proof
sys.path.insert(0, str(O.TOOLS))
import stage_gate as G
need = sorted({(svc, x) for r in B for svc, x in G.scoped_ids(" ".join(r))})
seeded_ids = sorted({x for _, x in need if x in O.SQL_TEXT or x.split("/")[-1] in O.SQL_TEXT and x.split("/")[0] in O.SQL_TEXT})
lb = HERE / "out" / "oe_lb_ids.txt"
lb.write_text("\n".join(seeded_ids) + "\n")
p = subprocess.run([sys.executable, "-B", str(O.TOOLS / "persona_view.py"), "check-sql", O.PERSONA, str(O.SQL_PATH), "--load-bearing", str(lb)],
                   capture_output=True, text=True, cwd=O.ROOT, env=ENV)
cs = p.stdout.splitlines()
head = next(l for l in cs if l.startswith("CHECK-SQL as"))
lbrows = [l for l in cs if l.startswith("[YES LB]") or l.startswith("[NO") or l.startswith("[UNVERIFIED")]
verdict = next(l for l in cs if l.startswith("verdict:"))
assert verdict.startswith("verdict: PASS"), verdict
covered = {x for l in lbrows if l.startswith("[YES") for _, x in G.scoped_ids(l)}
rest = [(svc, x) for svc, x in need if x not in covered]
cansee = []
for svc, x in rest:
    r = subprocess.run([sys.executable, "-B", str(O.TOOLS / "persona_view.py"), "can-see", O.PERSONA, svc, x], capture_output=True, text=True, cwd=O.ROOT, env=ENV)
    first = (r.stdout.splitlines() or [r.stderr.strip()[:200]])[0]
    cansee.append(first)
    assert first.rstrip().endswith(": YES"), first
print("scoped ids in B:", len(need), "| by check-sql:", len(covered & {x for _, x in need}), "| by can-see:", len(cansee))

# ------------------------------------------------------------------ C
ds = json.loads((HERE / "out" / "defer_search.json").read_text())
n_sc, n_un = len(ds["scoped"]), len(ds["unscoped"])
assert all(v["complete"] and not v["error"] for v in ds["scoped"].values()) and all(v["scan_complete"] for v in ds["unscoped"].values())
ASKID = O.ASK["id"]; fp = O.base("fred_pause")["id"]; lp = O.base("leonard_pause_q")["id"]
DEFER = (f"Slack (every channel and DM Julia can open), Gmail (her mailbox), Calendar, Drive, Docs, Sheets, Slides through persona_view; Linear, Trello, Confluence, GitHub, Contacts through "
         f"tools/hg.py; the overlay through its statements: {n_sc + n_un} searches (oe_gen/out/defer_search.json), terms hold off, not yet, wait, defer, freeze, pause, parked, postpone, as-is, "
         f"as is, accept, cancel, on hold, don't send, do not send, playable, PlayableX, pack list, hand-off, DES-313, brief, dated hits from Sep 16 2025 to the clock; population complete, "
         f"pagination complete (visible_total equals the returned list on all {n_sc} persona searches; scan_complete true on all {n_un} unscoped searches) · candidates: {fp} "
         f"(Frederick asks PlayableX to pause, Mon Sep 29), {lp} (Leonard asks whether to pause, Mon Sep 29), Trello comment {O.TRELLO['id']} ('Parked until Nov 3 … Julia is pulling the brief "
         f"and the pack status together for Frederick in the meantime') · governing version: Frederick's ask {ASKID} of Tue Sep 30 is later than all three and says 'While it's parked, can you do for "
         f"this one what you did for the Dominoes playable' and 'Write it for the game as it is today' · result: ")
C = [
 ("R3", "Create the brief", f"\"everything he's asking for in it\" with {F('ask')}: 'write the brief they build from' and 'Brief as a doc'", "gdocs_create_document (exists)",
  "title (bodyText carries the brief)", f"{F('drive')}; content from " + ", ".join(F(k) for k in ("scenario", "purpose", "eight", "zpicks", "deck", "gdd", "c2", "music", "nov3")),
  "a new Google Doc that Julia owns, in her Drive, with the brief in its body",
  "the scenario and what it is for; the eight on the board and that every other board item on the list is an extra; the four zombies and the one animation; how a level is won and lost; "
  "the tray's slots; what they can use for sound and when the music may start; the start date",
  DEFER + "no record holds or defers the brief; Julia owns no file about this playable other than her deck " + O.DECK_ID, "yes"),
 ("R4", "Create the hand-off list and write its rows", f"\"everything he's asking for in it\" with {F('ask')}: 'tell me where the item pack actually stands' and 'the hand-off list as a sheet'",
  "gsheets_create_spreadsheet (exists), gsheets_values_update (exists)", "title; spreadsheetId, range, values", f"{F('drive')}; rows from {all_lines}, {F('boardset')}",
  "a new spreadsheet that Julia owns, in her Drive, with the header and 96 rows", "Line, Category, Board set, State, What's owed, Who has it, Ticket; one row per line of Brian's pack list",
  DEFER + "no record holds or defers the list; no hand-off list exists yet (0 files named for it among the Drive hits)", "yes"),
 ("R5", f"Move each Owed line's ticket to Todo ({O.COUNTS['Owed']} tickets)", f"\"start to finish\" with {F('ask')}: 'what to do with the tickets' and {F('notes')}: 'An Owed line's ticket goes to Todo'",
  "linear_update_issue (exists)", "id (state carries the move)", f"the {O.COUNTS['Owed']} tickets of {F('owed')}; status {F('todo')}",
  f"each of the {O.COUNTS['Owed']} tickets is in Todo; the {O.COUNTS['Delivered'] + O.COUNTS['Ready']} Delivered and Ready tickets and DES-313 keep their state",
  "the state Todo, nothing else", DEFER + f"no record holds the ticket moves; the notes {O.NOTES_ID} (last version, modified Tue Sep 30) govern the tickets", "yes"),
 ("R5", f"Comment on each Owed line's ticket ({O.COUNTS['Owed']} comments)", f"\"start to finish\" with {F('notes')}: 'with a comment saying what is owed and who has it'",
  "linear_create_comment (exists)", "issueId, body", f"the {O.COUNTS['Owed']} tickets of {F('owed')}", f"each of the {O.COUNTS['Owed']} tickets carries a new comment by Julia", "what is owed and who has it",
  DEFER + f"no record holds the comments; the notes {O.NOTES_ID} (last version, modified Tue Sep 30) govern them", "yes"),
 ("R6", "Share both files, view only (8 shares)", f"\"start to finish\" with {F('ask')}: 'who gets the files' and {F('notes')}: 'Sharing: both files, view only. Everyone on the kickoff hold, and PlayableX through their intake address'",
  "gdrive_share_file (exists)", "fileId (emailAddress and role carry the person and the access)", f"{F('recipients')}", "four people hold reader access on each of the two files",
  "role reader", DEFER + f"no record restricts sharing with any of the four; the hold {O.HOLD_ID} has one version (sequence 0) and the same four attendees on Julia's copy", "yes"),
 ("R7", "Give Frederick the count for each state", f"\"everything he's asking for in it\" with {F('ask')}: 'Then give me the count for each state here'",
  "slack_send_message (exists)", "channel, text (thread_ts optional)", f"{F('ask')} (DM {O.DM_FRED}); {F('counts')}", "one message from Julia in the DM, sent, with the three counts",
  f"Delivered {O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, Owed {O.COUNTS['Owed']}", DEFER + "no record holds the reply; the ask is the only version of the request", "yes"),
 ("R9", "Post both links in the PlayableX channel", "\"once they're ready the links go in the PlayableX channel like he says\"",
  "slack_send_message (exists)", "channel, text", f"{F('channel')}", "one message from Julia in the channel, sent, with the two links", "the link of the brief and the link of the hand-off list",
  DEFER + f"no record holds the post; the pause in {fp} stops the build, and the ask, a day later, has the links posted 'so they know what's still coming from us'", "yes"),
]

# ------------------------------------------------------------------ E, F
dk = O.DECK_ID; vo = O.base("vendor_oct6")["id"]
E = [
 ("T1", f"Robert's eight of 25 Sep with Dynamite ({F('picks')}, {O.PICKS['id']})", F("eight"), f"his own reply {O.C3['id']} a day later, under Julia's bow post: 'in place of the last one on my list'"),
 ("T2", f"Brian's note 'Opens, looks right. In the outgoing folder.' on the 12 files he saved out of the project ({line_ids('A1')})", F("owed"),
  f"{O.A1['id']}, Marcus, the day after the notes, to Brian: 'the text kind ... youll need to redo them'; {O.base('vendor_formats')['id']}: 'Binary format, not ASCII'"),
 ("T3", f"Brian's note on the 12 bathroom files from Claire ({line_ids('A2')})", F("owed"), f"{O.A2['id']}, Robert to Julia, Mon Sep 29: Claire is redoing the UVs on the bathroom objects and the files she gave Brian on Friday are the old version"),
 ("T4", f"Brian's note 'Zipped with the other instruments, in the outgoing folder' on 8 lines ({line_ids('C4')})", F("owed"),
  f"{O.LOG_ID}, his own log, Tue Sep 30: the zip 'got cut off on upload'; Music Keyboard ({FL('Music Keyboard')}) is a Mon Sep 29 file outside that zip and stays Ready"),
 ("T5", f"Robert's new colour versions of Chainsaw, Cone and Cactus Plant ({O.base('robert_new_colours')['id']}, Mon Sep 29) make their 'first thing' notes look out of date ({line_ids('C1')})", F("ready"),
  f"{O.LOG_ID}, Brian's log, Tue Sep 30, the latest record: 'Claire sent the three recoloured models again. Opened them, they look right, and they replace Thursday's.'; only Robert's post says which three"),
 ("T6", f"Five notes 'Exported .wav from the project, Fri 26 Sep. Plays.' ({', '.join(FL(n) for n in ('Matching sound', 'Rocket sound', 'Explosion sound', 'Success sound', 'Failure sound'))})", F("owed"),
  f"{O.SOUND_ID}: 'no' under 'OK outside the game' on Rocket sound and Explosion sound only"),
 ("T7", f"The sheet's Background music row says 'yes' ({F('c2')}, {O.SOUND_ID})", FL("Background music"), "the line's own note: 'Not exported. Calvin is still cutting the ad track down to a loop.'"),
 ("T8", f"Two earlier start dates in the channel: 'September 29' ({O.base('vendor_formats')['id']}) and 'October 6th' ({vo})", F("nov3"), f"{O.base('vendor_nov3')['id']}, Tue Sep 30, the latest of the three"),
 ("T9", f"Julia's deck lists five board items and 'A mix, nothing fixed yet.' for zombies ({F('deck')}, {dk})", f"{F('eight')}, {F('zpicks')}", f"the deck is of Tue Sep 23; {O.PICKS['id']} and {O.ZPICKS['id']} are later"),
 ("T10", f"Frederick's Sep 15 suggestion of grenade, couch and plush doll ({F('scenario')}, {O.base('fred_scenario1')['id']})", F("eight"), f"the ask {ASKID}: 'Robert's picks for the board and the zombies stand'"),
 ("T11", f"Julia's own comment on the design page about a 6-slot test ({F('gdd')}, page_zm3d_gdd, comment_zm3d_gdd_c1)", F("gdd"), "comment_zm3d_gdd_c2, Robert, the same day: 'keep the GDD at 7 for now'; the page says 7-slot tray"),
 ("T12", f"Leonard's Trello card 'Playable Kickoff' with his comment {O.TRELLO['id']} reads as the kickoff record", F("hold"), f"the card has no attendees; the notes say 'the kickoff hold', which is the calendar event {O.HOLD_ID}"),
 ("T13", f"Ticket state In Progress on 88 tickets reads as one state ({F('ticket')}, DES-313)", f"{F('ready')}, {F('owed')}", f"{O.COUNTS['Ready']} of the 88 are Ready and {O.COUNTS['Owed']} are Owed; the workflow state decides neither"),
 ("T14", f"Rubber Ducky is in the Bathroom category ({FL('Rubber Ducky')}, DES-360)", F("owed"), "its note says 'Not exported yet. Waiting on the FBX from Claire.': owed for the FBX, not for Friday's files; Claire has it either way"),
 ("T15", f"PlayableX's open question on the zombie pack ({O.base('vendor_zombie_ask')['id']}) reads as the pack not being usable", FL("Zombie characters"),
  f"'We have reviewed the assets.'; DES-400 is Done; Robert answers the question in {O.ZPICKS['id']}"),
 ("T16", f"The vendor's names for two lines: 'the duck asset' and 'rocket launcher' ({O.base('vendor_duck')['id']}, {O.base('vendor_asset_list')['id']})", f"{FL('Plushie Chick')}, {FL('Cannon')}",
  "Brian's notes on DES-334 and DES-398 give both names"),
 ("T17", f"The design page's roster and its boss mode ({F('gdd')}, page_zm3d_gdd)", f"{F('zpicks')}, {F('gdd')}", "known base issue SC-58: the zombies come from Robert's post and the loss rule from the core mechanic; kept off every Expected line"),
 ("T18", f"PlayableX's complaint of Thu Sep 25 about the second zip ({O.base('vendor_blank_scene')['id']}) reads as the chick inside it being unusable", FL("Plushie Chick"),
  "the message names 'the zombie assets' and the package's prefabs; Brian's note on DES-334, written after it, says the problem was the zombie package, not the chick; PlayableX's later 'We have reviewed the assets.' raises only the zombies"),
 ("T19", "A build note of Fri Sep 26 in #builds, 'fix hammer collection asset' (C05433XK267/2025-09.json /979 and /980), reads as a fix to the Cute Hammer model after its Thu Sep 25 file", FL("Cute Hammer"),
  "'hammer collection' is the game's hammer-collecting mechanic in base talk ('snowballing the hammer collection', 'the hammer collection pace', C04UTBZL6AX, June 2024); no record names the Cute Hammer model or Claire's file; raised as UNSURE by the rev2 blind O3 pass and resolved here: DES-325 stays Ready"),
 ("T20", f"Julia's Sep 22 line 'let's do a more hardcore friendly playable' (C090N54TG79/1758569707.508219) reads as what the playable is for", F("purpose"),
  "Robert answers in the same thread three minutes later, 'Doesn't really matter' (C090N54TG79/1758569872.578829) and 'I think we should remain as is' (C090N54TG79/1758569885.985319); the ask says 'Write it for the game as it is today'"),
]
Frisk = [
 ("1", "The links may be a top-level post or a reply in the thread of the pause; the counts may be a new DM message or a reply under the ask (brief 4b)", f"{F('channel')}, {F('ask')}", "rubric (accept both positions)", "rubric stage"),
 ("2", "Either file may sit in a folder of Julia's Drive instead of its root (brief 4b)", F("drive"), "rubric (accept)", "rubric stage"),
 ("3", "What a full tray does is not graded: the page's sentence on it sits beside a remark Julia cannot open", F("gdd"), "OE accuracy / rubric", "kept off every Expected line"),
 ("4", "The design page's roster and boss mode are a known base issue (SC-58)", F("gdd"), "OE accuracy / rubric", "kept off every Expected line"),
 ("5", "What's owed is free wording: any text that names the same thing as the deciding record is right", F("owed"), "rubric (accept wording)", "rubric stage"),
 ("6", "Category is empty on Brian's list for the 12 lines that are not board items; a blank cell is right", F("pack"), "rubric (accept blank)", "rubric stage"),
 ("7", "A share to an outside address rests on the catalog entry of gdrive_share_file; the pre-check run's eight shares, one of them to the intake address, returned success", F("recipients"), "feasibility (supported)", "none"),
 ("8", "What the scenario is for: Julia's Sep 22 'more hardcore friendly playable' line could be taken for the purpose; it is walked back in the same thread (trap T20), so the brief carries one purpose (platform /oe round 1)", F("purpose"), "OE accuracy / rubric", "settled: OE 10 and OE 20 carry the one purpose"),
 ("9", f"'Toy Airplane Redone (Still not working)' is a build note of Thu Sep 25, older than the Mon Sep 29 file; it does not change the line ({F('absence')})", FL("Toy Airplane"), "rubric (Ready)", "rubric stage"),
]

# ------------------------------------------------------------------ self-review
CR = [
 ("R1", "'Frederick's playable message' could be one of his posts in the PlayableX channel, or the calendar invite he sent the same day",
  f"{ASKID} is his only message to Julia on Tue Sep 30 and the only one that asks for files, counts and a post; the invite of {O.HOLD_ID} asks for nothing", "holds"),
 ("R2", "'everything' could stop at the sentences of the DM and leave the notes out", f"{ASKID}: 'My hand-off notes say what goes in the brief, what counts as ready, what to do with the tickets and who gets the files' ({F('notes')})", "holds"),
 ("R3", "the brief could be a message in the channel instead of a doc", f"{ASKID}: 'Brief as a doc'; {O.NOTES_ID}: 'One doc PlayableX can build from'", "holds (a Google Doc)"),
 ("R4", "the list could cover the 84 board items only, or only the lines that are not delivered", f"{O.NOTES_ID}: 'One row per line of Brian's pack list'; {O.PACK_ID} has 96 rows ({F('pack')})", "holds (96 rows)"),
 ("R5", "the tickets could all move, or the Owed ones could get a comment without a state change", f"{O.NOTES_ID}: 'An Owed line's ticket goes to Todo with a comment'; 'Leave the Delivered and Ready ones as they are'", f"holds ({O.COUNTS['Owed']} moves, {O.COUNTS['Owed']} comments)"),
 ("R6", "'everyone on the kickoff hold' could be Leonard's Trello card, or could include Julia herself", f"{O.HOLD_ID} lists four attendees and Julia owns the files; the card {O.TRELLO['id']} sits on has no attendees ({F('hold')})", "holds (3 people and the intake address)"),
 ("R7", "the counts could be asked for in the channel, or over the board items only", f"{ASKID}: 'give me the count for each state here', written in DM {O.DM_FRED}; the states cover the 96 lines ({F('counts')})", f"holds ({O.COUNTS['Delivered']}, {O.COUNTS['Ready']}, {O.COUNTS['Owed']} in the DM)"),
 ("R8", "'my Drive' could mean a shared folder the team uses", f"{ASKID}: 'both in your Drive'; d_8140f09bf9f1b94cb8ee2d is Julia's own root ({F('drive')})", "holds"),
 ("R9", "the links could go in the DM with the counts", f"{ASKID}: 'post both links in the PlayableX channel so they know what's still coming from us'; the prompt names the channel ({F('channel')})", "holds"),
]
n_abs = 1
n_notclaim = 0
doc = []
doc += [f"# 08 OE Writing Ledger — julia-zm3d-playable-brief (injection {O.M.REV})",
        f"Generated {D.date.today().isoformat()} · Clock {CLOCK} · seed bound {ctx['freeze_utc']} · Persona Julia Lawson {O.JULIA} (Product Manager) · Tier Long-Horizon · Mode Hard",
        f"Status: READY — every requirement has verified facts, every scoped fact is persona-visible (pasted proof below), all 7 write families map to cataloged tools, friction is none",
        f"Inputs read: 04_Prompt.txt — present (sha256 {sha(O.TASK / '04_Prompt.txt')}) · 00_Assigments.md — present · 01_Universe_Inject.sql — present ({O.M.REV}, sha256 {sha(O.SQL_PATH)}; "
        f"the platform runs the same statements without the four header comment lines) · 01_Grounding_Dossier.md — present (leads only) · 01_Scenario_Design.md and "
        f"01_Hardness_Manifest.json — present (leads for traps only) · 03_Error_Async_Config.txt — present (Friction: none) · 02_Reference_Files_Manifest.md — absent (no attachments) · "
        f"04_Prompt_Writing_Brief.md — present (4b accepted outcomes) · eval_reports: rev1 only (/injection PASS, /prompt PASS, /hardness NON-FAIL); the six rev2 baseline runs in "
        f"07_Baseline_Trajectories-2 (routes and tool names only)", "",
        "Persona binding: roster entry julia_lawson, Julia Lawson, Product Manager, julia.lawson@harmonygames.co. Scoped services: Gmail (own mailbox), Slack (channels she is a member of and her DMs), "
        "Calendar (own calendar), Drive, Docs, Sheets and Slides (files she owns or that are shared with her). Unscoped: Linear, Trello, Contacts, Confluence, GitHub.", "",
        "Dates: Pacific first, UTC beside it. 'sent', 'posted', 'created' and 'modified' mark record times, all at or before the seed bound; 'starts' marks a semantic future date (the kickoff hold and the "
        "3 November start). SQL line numbers refer to the task folder's 01_Universe_Inject.sql.", "",
        "## A · Requirements (traced to the prompt)"]
doc += table(["R", "Prompt span (quoted)", "Type (Discovery / Write / Tell / Constraint)", "Explicit / implicit", "Fact IDs"], A)
doc += ["", "## B · Facts", b_text, "", "Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)", "",
        f"`python3 Task_Authoring/tools/persona_view.py check-sql julia_lawson {REL}/01_Universe_Inject.sql --load-bearing oe_gen/out/oe_lb_ids.txt` ({len(seeded_ids)} seeded ids; "
        "load-bearing rows and the verdict line kept):", "", "```text", head] + lbrows + [verdict, "```", "",
        f"`python3 Task_Authoring/tools/persona_view.py can-see julia_lawson slack` and `gdrive`, one call per id ({len(cansee)} base ids, first line of each):", "", "```text"] + cansee + ["```", "",
        "## C · Write capability"]
doc += table(["R", "Required write", "Prompt authority (quoted; agent, not user-reserved)", "Catalog tool (exists?)", "Required parameters", "Target (fact ID)", "Completing end state",
              "Content the prompt requires", "Defer search (services · population · pagination complete · governing version · result, or UNRESOLVED)", "Feasible?"], C)
doc += ["", "## D · Friction facts"]
doc += table(["Function (01_)", "Mode / rate / wait", "Facts blocked", "Alternative path (service, locator)", "Alternative facts", "Visible?"],
             [("none", "Friction: none (03_Error_Async_Config.txt)", "—", "—", "—", "—")])
doc += ["", "## E · Traps and distractors"]
doc += table(["T", "What the agent meets (pointer)", "Competes with (fact ID)", "Discriminator (timestamp / author / ID)"], E)
doc += ["", "## F · Open risks"]
doc += table(["#", "Risk", "Facts affected", "Consequence (OE accuracy / rubric / UGT / feasibility)", "Check needed"], Frisk)
doc += ["", "## G · Tally",
        f"Requirements {len(A)} · facts {len(B)} · writes {len(C)} (feasible {len(C)}) · friction items 0 · expected values {len(B)} (quoted {len(B) - n_abs - n_notclaim} · not_a_claim {n_notclaim} · "
        f"ABSENCE-checked {n_abs}) · unverified visibility 0 · blocking 0", "",
        "## Self-review", "",
        "Walked Evals/2_Oracle_Events_Eval.md 1.1, 2.1–2.6 and 3.1–3.5 against this ledger in order. Every requirement has facts; every write family has its prompt authority, a cataloged tool with its "
        "required parameters, a completing end state and a defer search; friction is none; every scoped fact carries pasted visibility proof. Every value in section B was re-verified in this run: seeded rows "
        "re-parsed from 01_Universe_Inject.sql, base records re-read through tools/hg.py (oe_gen/base_read.py), every quote asserted to be an exact substring of its record, and oe_gen/model.py recomputed "
        "the state, the holder and the Board set of all 96 lines from the notes and the deciding records and asserted them equal to solver/truth.json (Delivered {O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, "
        f"Owed {O.COUNTS['Owed']}; " + ", ".join(f"{w} {n}" for w, n in O.WHO_COUNTS.items()) + "). No-event-text scan: section B holds facts and dependency edges only; nothing here is event text.", ""]
doc += table(["R", "Counter-reading (strongest other reading of the span, or a competing location)", "Evidence that resolves it", "Result"], CR)
doc += ["", "Competing locations checked: the eight (T1), the start date (T8), the tray's slots (T11), the kickoff record (T12) and each overturned note (T2 to T7) have their discriminator in section E. "
        f"The one absence fact ({F('absence')}) rests on a search of all 44 untouched names and of the three re-sent ones since the log's entry, with complete result lists and "
        "two positive controls (oe_gen/out/absence_check.json).", "",
        "Unresolved: none blocking. Open risks 1, 2, 5, 6 and 9 go to the rubric stage; 3 and 4 are kept off every Expected line; 8 is settled on OE 10 and OE 20 (platform /oe round 1).", ""]
OUT.write_text("\n".join(doc) + "\n")
print("wrote", OUT, len("\n".join(doc)), "chars;", len(A), "requirements,", len(B), "facts,", len(C), "writes,", len(E), "traps")
