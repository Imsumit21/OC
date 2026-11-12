#!/usr/bin/env python3
"""Build Working_Files/01_Hardness_Manifest.draft.json from design_model.py (scenario stage, design D3 = rev2). No SQL, no prompt text."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import design_model as M
import planned_texts as TXT

WF = Path(__file__).resolve().parents[1]
ctx = json.loads((WF / "00_Task_Context.json").read_text())
S, B = M.SEED, M.BASE
sid = lambda k: S[k]["id"]
tick = lambda n: M.BY_NAME[n]["ticket"]
def q(text, needle):
    assert needle in text, needle
    return needle
TICKETS = [l["ticket"] for l in M.LINES if l["ticket"]]
OWED = M.OWED_WITH_TICKET
PT = M.PACK_TICKET
n_all, n_list, n_owed = len(M.LINES), M.N_LIST, len(OWED)
def names(cls): return [l["name"] for l in M.members(cls)]
CONFIRM = ("task author in chat on 2026-11-11: '220 calls are good with required failure'; and 'my task is a long horizon task "
           "soo i want over 130+ tool calls in each runs and also i want difficulty pass rate under 70% and also have to folllow "
           "all other difficulty guidelines soo you can choose from your self which option is best fit for my requirements in this task'")

requirements = {
    "R1": f"list population: one row for every line on Brian's pack list ({n_all} lines)",
    "R2": "state per line: Delivered, Ready or Owed under Frederick's hand-off notes",
    "R3": "for an Owed line: what is owed and who has it (whoever has to do the next thing)",
    "R4": "the board: the eight (Robert's picks as he last left them) marked Default and every other board item Extra",
    "R5": "brief content: the scenario and what it is for, the eight and the extras, the four zombies and the one animation, how a level is won and lost, the tray, sound, the start date",
    "R6": "tickets: an Owed line's ticket to Todo with a comment saying what is owed and who has it; Delivered and Ready tickets left as they are",
    "R7": "delivery: the brief and the hand-off list in Julia's Drive; both files shared view-only with the kickoff hold's attendees and PlayableX's intake address; the count for each state to Frederick in his DM; both links in the PlayableX channel",
}
services = {
    "slack": {"role": "the ask (Frederick's DM); the PlayableX channel; Robert's eight, his zombie answer and his later reply; Marcus's post in #zombie-match3d; Robert's note to Julia about the bathroom objects; writes: the counts and the links",
              "weight_reason": "the hub, three of the six deciding records and both messages"},
    "linear": {"role": f"Brian's pack ticket {PT} and its {n_list} children with his note on each; writes: Todo moves and comments",
               "weight_reason": "the per-line evidence and the ticket follow-through"},
    "gsheets": {"role": "Brian's pack list; Calvin's sound sources sheet; write: the hand-off list", "weight_reason": "the line set, the sound decision and the main deliverable"},
    "gdocs": {"role": "Frederick's hand-off notes; Brian's log of the outgoing folder (the broken zip and the three re-sent items); write: the brief", "weight_reason": "every rule of the task, the deciding record of two rules and the second deliverable"},
    "gdrive": {"role": "where the notes, the list and the deck are found; write: view-only shares of both files", "weight_reason": "discovery of the shared files and the sharing"},
    "gslides": {"role": "Julia's deck of the reference level (the three item types as built on 23 Sep)", "weight_reason": "what was built for the vendor; the older state of the board"},
    "gcal": {"role": "Frederick's kickoff hold on 3 Nov (attendees)", "weight_reason": "who both files are shared with"},
    "contacts": {"role": "PlayableX's intake contact", "weight_reason": "the address both view links are shared with"},
    "github": {"role": "base pull request match3d#462 and its comment (the 25 Sep model change behind Robert's new colour versions)", "weight_reason": "corroboration only; no line's state rests on it"},
    "confluence": {"role": "the design page and its comments (7-slot tray, loss only at zero health)", "weight_reason": "two facts of the brief"},
    "trello": {"role": "Leonard's Playable Kickoff card with his comment", "weight_reason": "the decoy for 'the kickoff'; a status mirror of the pause"},
    "gmail": {"role": "invitation mails for the kickoff hold in the attendees' mailboxes", "weight_reason": "companions of the hold; carry the same attendee list"},
}
anchors = [
    {"id": "A1", "service": "slack", "record": sid("ask"), "locator": sid("ask"), "prompt_reference": "Frederick's playable message",
     "requirement_ids": ["R1", "R4", "R7"]},
    {"id": "A2", "service": "slack", "record": M.VENDOR_CH, "locator": M.VENDOR_CH, "prompt_reference": "the PlayableX channel", "requirement_ids": ["R7"]},
    {"id": "A3", "service": "gdrive", "record": B["julia_root"], "locator": B["julia_root"], "prompt_reference": "my Drive", "requirement_ids": ["R7"]},
]
def frag(fid, service, container, locator, kind, via, seeded, base, by, quote, reqs, names_=None, **kw):
    f = {"id": fid, "service": service, "container": container, "locator": locator, "kind": kind, "incorporated_via": via,
         "seeded_ids": seeded, "base_pointers": base, "delegated_by_record": by, "delegation_quote": quote, "requirement_ids": reqs}
    if names_: f["names_authorities"] = names_
    f.update(kw); return f
ASK, NOTES = sid("ask"), sid("notes")
VTHREAD = f"{M.VENDOR_CH}/1757695108.506159"
ask_fragments = [
    frag("K1", "gdocs", NOTES, NOTES, "delegation", ["A1"], [NOTES], [], ASK,
         q(TXT.ASK, "My hand-off notes say what goes in the brief, what counts as ready, what to do with the tickets and who gets the files"), ["R2", "R3", "R5", "R6"],
         [{"id": "H3", "quote": q(TXT.NOTES, "the kickoff hold")}]),
    frag("K2", "gsheets", sid("tracker"), sid("tracker"), "requirement", ["A1"], [sid("tracker")], [], ASK,
         q(TXT.ASK, "Brian's pack list is where it starts"), ["R1"]),
    frag("K3", "slack", sid("picks"), sid("picks"), "requirement", ["A1"], [sid("picks")], [], ASK,
         q(TXT.ASK, "Robert's picks for the board and the zombies stand"), ["R4"]),
    frag("K4", "linear", PT, PT, "destination", ["A1", "K1"], [PT], [], NOTES,
         q(TXT.NOTES, "Tickets live under Brian's pack ticket, one per line"), ["R6"]),
    frag("K5", "slack", VTHREAD, B["vendor_formats"], "format", ["A1", "K1"], [], [B["vendor_formats"], B["vendor_asset_list"]], NOTES,
         q(TXT.NOTES, "What they told us about formats still holds"), ["R2"]),
    frag("K6", "confluence", B["gdd"], B["gdd"], "requirement", ["A1", "K1"], [], [f"confluence:{B['gdd']}"], NOTES,
         q(TXT.NOTES, "How the level plays is on the design page"), ["R5"]),
    frag("K7", "gcal", sid("hold"), sid("hold"), "recipient", ["A1", "K1"], [sid("hold")], [], NOTES,
         q(TXT.NOTES, "Everyone on the kickoff hold"), ["R7"]),
    frag("K8", "contacts", sid("contact"), sid("contact"), "recipient", ["A1", "K1"], [sid("contact")], [], NOTES,
         q(TXT.NOTES, "their intake address, which is in Contacts"), ["R7"]),
    frag("K9", "gslides", sid("deck"), sid("deck"), "requirement", ["A1", "K1"], [sid("deck")], [], NOTES,
         q(TXT.NOTES, "your deck of the reference level has what we built for them"), ["R5"]),
    frag("K10", "slack", sid("zpicks"), sid("zpicks"), "requirement", ["A1"], [sid("zpicks")], [B["vendor_zombie_ask"]], ASK,
         q(TXT.ASK, "Robert's picks for the board and the zombies stand"), ["R5"]),
    frag("K11", "slack", B["art_bow_root"], sid("c3_reply"), "amendment", ["A1"], [sid("c3_reply")], [B["art_bow_root"]], ASK,
         q(TXT.ASK, "unless he's changed them since"), ["R4"], supersedes="K3",
         resolver="Robert's own later reply (26 Sep) changes his 25 Sep eight; the ask keeps his latest word"),
    frag("K12", "slack", B["vendor_music_rule"], B["vendor_music_rule"], "requirement", ["A1", "K1"], [], [B["vendor_music_rule"]], NOTES,
         q(TXT.NOTES, "so does their rule from last time about when the music may start"), ["R5"]),
    frag("K13", "slack", B["vendor_nov3"], B["vendor_nov3"], "requirement", ["A1"], [], [B["vendor_nov3"]], ASK,
         q(TXT.ASK, "PlayableX are holding Nov 3 for us"), ["R5"]),
    frag("K15", "slack", VTHREAD, B["fred_scenario1"], "requirement", ["A1", "K1"], [], [B["fred_retention"], B["fred_scenario1"]], NOTES,
         q(TXT.NOTES, "which scenario we picked and what it is for"), ["R5"]),
    # the hub itself: the ask names the two authorities it starts from in its own words
    frag("K16", "slack", ASK, ASK, "requirement", ["A1"], [ASK], [], ASK,
         q(TXT.ASK, "write the brief they build from, and tell me where the item pack actually stands"), ["R1", "R7"],
         [{"id": "H1", "quote": q(TXT.ASK, "My hand-off notes")}, {"id": "H2", "quote": q(TXT.ASK, "Brian's pack list")}]),
]
authorities = [
    {"id": "H1", "name": "Frederick's hand-off notes", "home_service": "gdocs", "decoy_service": "gdocs", "governs": ["R2", "R3", "R5", "R6"],
     "findable_query": "hand-off notes", "seeded_ids": [NOTES], "base_pointers": [], "decoy_seeded_ids": [],
     "decoy_base_pointers": [f"gdocs:{B['playable_feedback_doc']}"],
     "decoy_scope": {"dimension": "game", "decoy": "Domino Delights (the first playable, April 2025: Leonard's Playable Feedback)", "task": "Zombie Match 3D (the second playable)"}},
    {"id": "H2", "name": "Brian's pack list", "home_service": "gsheets", "decoy_service": "slack", "governs": ["R1"],
     "findable_query": "playable pack list", "seeded_ids": [sid("tracker")], "base_pointers": [], "decoy_seeded_ids": [],
     "decoy_base_pointers": [B["vendor_asset_list"]],
     "decoy_scope": {"dimension": "issuer", "decoy": "PlayableX's request (asset groups they expect, no lines)", "task": "Brian's list (the pack, line by line)"}},
    {"id": "H3", "name": "the kickoff hold", "home_service": "gcal", "decoy_service": "trello", "governs": ["R7"],
     "findable_query": "playable kickoff", "seeded_ids": [sid("hold")], "base_pointers": [], "decoy_seeded_ids": [sid("trello_note")],
     "decoy_base_pointers": [f"trello:{B['trello_kickoff']}"],
     "decoy_scope": {"dimension": "issuer", "decoy": "Leonard's own to-do card (no attendees)", "task": "Frederick's calendar hold (the attendee list)"}},
]
cohort = {
    "definition": (f"every line of the playable pack: the {n_list} rows of Brian's pack list (84 board items in seven of the game's categories, the cannon, "
                   "the background, the zombie characters, six sound cues, the item visuals, the UI elements, the fonts)"),
    "definition_source": [sid("tracker")], "key": "line", "size": n_all,
    "evidence_surfaces": [
        {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1.0, "records": len(TICKETS), "seeded": True, "seeded_ids": TICKETS,
         "requirement": "R2", "decides": "state per line: Delivered, Ready or Owed",
         "why_no_bulk": "linear_list_issues and linear_get_issue return no comments; Brian's note on a line (where the file came from, when, whether it opens, or that it is not exported) is only in that ticket's comments",
         "short_circuit": "the pack list has no state column and every undelivered ticket is In Progress; each category holds Ready lines, lines Owed on their own note and lines from different exports, so no ticket can stand for its neighbours"},
        {"service": "linear", "tool": "linear_update_issue + linear_create_comment", "per_record_calls": 2.0, "records": n_owed, "seeded": False,
         "requirement": "R6", "decides": "an Owed line's ticket to Todo with a comment saying what is owed and who has it",
         "why_no_bulk": "no batch write exists for state changes or comments; each ticket takes its own calls",
         "short_circuit": "the notes require the Todo state and the comment on every Owed line's ticket; the sheet does not replace them"},
        {"service": "gdocs", "tool": "gdrive_search + gdocs_get_document_text", "per_record_calls": round(2 / 11, 2), "records": 11, "seeded": True, "seeded_ids": [sid("c4_log")],
         "requirement": "R2", "decides": "state per line: Delivered, Ready or Owed",
         "why_no_bulk": "nothing on the eleven tickets, on the pack list or in the notes says the zip will not unpack or that the three were sent again; only Brian's own log of the outgoing folder records it",
         "short_circuit": "the eight tickets say the files are zipped in the outgoing folder and the three say they were handed over on 25 Sep, before Robert's 29 Sep colours; no other record says what is in the folder now"},
    ],
}
chains = [
    {"id": "C1", "root_cause": "A24", "ends_in": "R2", "hops": [
        {"service": "slack", "record": B["vendor_formats"], "finding": "the vendor takes .fbx only in binary format, not ASCII (16 and 19 Sep; Frederick relayed it to Julia on 18 Sep)"},
        {"service": "linear", "record": tick("Refrigerator"), "finding": "Brian's note: FBX saved out of the project, Thu 25 Sep, so the colours come along; opens, looks right, in the outgoing folder (twelve lines in two categories say this)"},
        {"service": "slack", "record": sid("a1_post"), "finding": "Marcus, 26 Sep, #zombie-match3d: the models Brian saved out of Unity on Thursday are the text kind, the setting was wrong that day; Claire's are fine"}]},
    {"id": "C2", "root_cause": "A11", "ends_in": "R3", "hops": [
        {"service": "gsheets", "record": sid("tracker"), "finding": "thirteen lines carry the category Bathroom, the iron, the ironing board and the washing machine among them"},
        {"service": "linear", "record": tick("Bathtub"), "finding": "Brian's note: FBX from Claire, Fri 26 Sep, opens, looks right"},
        {"service": "slack", "record": sid("a2_dm"), "finding": "Robert to Julia, 29 Sep, in their DM: Claire is redoing the UVs on the bathroom objects; the bathroom files she gave Brian on Friday are the old version"}]},
    {"id": "C3", "root_cause": "A25", "ends_in": "R2", "hops": [
        {"service": "linear", "record": tick("Cactus Plant"), "finding": "Brian's note, written 25 Sep 08:06 UTC: FBX from Claire first thing, opens, looks right (also Chainsaw and Cone)"},
        {"service": "slack", "record": B["robert_new_colours"], "finding": "Robert, 29 Sep 23:44 UTC, #zombie-design: new coloured versions of the cactus, the chainsaw and the cones (base)"},
        {"service": "gdocs", "record": NOTES, "finding": "if the art changed after a file went out or was exported, it goes again"},
        {"service": "gdocs", "record": sid("c4_log"), "finding": "Brian's log of the outgoing folder, Tue 30 Sep: Claire sent the three recoloured models again; they open, look right and replace Thursday's (which three: Robert's post)"}]},
    {"id": "C4", "root_cause": "A14", "ends_in": "R4", "hops": [
        {"service": "gslides", "record": sid("deck"), "finding": "Julia's deck: the reference level as built on 23 Sep has three item types"},
        {"service": "slack", "record": sid("picks"), "finding": "Robert, 25 Sep: the eight for the board, the dynamite among them; everything else is an extra"},
        {"service": "slack", "record": sid("c3_reply"), "finding": "Robert, 26 Sep, under Julia's bow post in #zombie-art: it goes in the eight in place of the last item on his list, as it is"}]},
    {"id": "C5", "root_cause": "A13", "ends_in": "R2", "hops": [
        {"service": "linear", "record": tick("Rocket sound"), "finding": "Brian's note: exported .wav from the project, plays, in the outgoing folder"},
        {"service": "gdocs", "record": NOTES, "finding": "we only hand over what is ours to hand over; anything from a library or a bought pack stays until we have our own version"},
        {"service": "gsheets", "record": sid("c2_sheet"), "finding": "Calvin's sources sheet: the rocket sound is from a library seat and the explosion from a bought pack; our own versions are not made yet"}]},
    {"id": "C6", "root_cause": "A3", "ends_in": "R3", "hops": [
        {"service": "gsheets", "record": sid("tracker"), "finding": "ten lines carry the category Music Instruments"},
        {"service": "linear", "record": tick("Cello"), "finding": "Brian's note: FBX from Claire, Fri 26 Sep, opens, looks right, zipped with the other instruments (eight lines say this)"},
        {"service": "gdocs", "record": sid("c4_log"), "finding": "Brian's own log of the outgoing folder, 30 Sep: the zip with Friday's instruments was cut off on upload and will not unpack, and the eight are not in the folder any other way; he will put the files back"}]},
]
def vr(service, rid, seeded, at, container=None, base=False):
    r = {"service": service, "seeded": seeded, "at": at}
    r["base_pointer" if base else "id"] = rid
    if container: r["container"] = container
    return r
traps = [
    {"id": "T1", "family": "done_gap", "services": ["linear", "slack"], "seeded_ids": [tick("Refrigerator"), tick("Retro TV"), sid("a1_post")], "base_pointers": [B["vendor_formats"]],
     "requirement": "R2", "expected_wrong_reading": "the twelve lines saved out of the project are Ready: each ticket says FBX, opens, looks right, in the outgoing folder",
     "resolver": "Marcus's 26 Sep post in #zombie-match3d: those files are the text kind (the setting was wrong that day); the vendor takes binary only, so each is Owed (export again as binary, Brian)",
     "discovery_order": "each ticket's note is read while building the list; the post is in the game's dev channel, which the ask never names, and carries none of the ask's words"},
    {"id": "T2", "family": "superseding", "services": ["linear", "slack"], "seeded_ids": [tick("Bathtub"), sid("a2_dm")], "base_pointers": [],
     "requirement": "R3", "expected_wrong_reading": "the twelve exported bathroom lines are Ready: FBX from Claire on Friday, opens, looks right",
     "resolver": "Robert's 29 Sep note to Julia: Claire is redoing the UVs on the bathroom objects and the files she gave Brian on Friday are the old version, so each is Owed (the art, Claire: the file came from her)",
     "discovery_order": "Brian's note (26 Sep) is on every bathroom ticket; Robert's note is three days later, in Julia's DM with him among his other messages of that day, naming the category and no line, with Claire and Brian tagged rather than named",
     "version_records": [vr("linear", M.comment_id("note_Bathtub"), True, "2025-09-26T11:20:00Z", f"linear:{tick('Bathtub')}"),
                         vr("slack", sid("a2_dm"), True, S["a2_dm"]["at"], f"slack:{sid('a2_dm')}")]},
    {"id": "T3", "family": "superseding", "services": ["linear", "slack", "gdocs"], "seeded_ids": [tick("Cactus Plant"), sid("c4_log")],
     "base_pointers": [B["robert_new_colours"], B["art_cactus"], B["art_cone"], B["pr462"]],
     "requirement": "R2", "expected_wrong_reading": "Cactus Plant, Chainsaw and Cone are Owed: Robert showed new colour versions on 29 Sep, after their 25 Sep files, and the notes send a changed file again",
     "resolver": "Brian's log of the outgoing folder, Tue 30 Sep: Claire sent the three recoloured models again, they open and look right and they replace Thursday's; Robert's post says which three; so each is Ready",
     "discovery_order": "Robert's post sits in #zombie-design next to his picks and is met early; the completion is a later entry in a second document by the list's owner that nothing links, found by looking for the outgoing folder the notes speak of",
     "version_records": [vr("linear", M.comment_id("note_Cactus Plant"), True, "2025-09-25T08:05:00Z", f"linear:{tick('Cactus Plant')}"),
                         vr("slack", B["robert_new_colours"], False, "2025-09-29T23:44:26Z", f"slack:{M.DESIGN_CH}", base=True),
                         vr("gdocs", sid("c4_log"), True, S["c4_log"]["at"], f"file:{sid('c4_log')}")]},
    {"id": "T4", "family": "authority", "services": ["linear", "gdocs", "gsheets"], "seeded_ids": [tick("Rocket sound"), NOTES, sid("c2_sheet")], "base_pointers": [B["robert_copyright"]],
     "requirement": "R2", "expected_wrong_reading": "all five exported sound cues are Ready: .wav is a format the vendor takes and each plays",
     "resolver": "the notes hand over only sound that is ours; Calvin's sources sheet says the rocket sound is from a library seat and the explosion from a bought pack, so both are Owed (our own version, Calvin)",
     "discovery_order": "the tickets state the file type only; the sheet is found by looking for where the sounds came from"},
    {"id": "T5", "family": "superseding", "services": ["slack"], "seeded_ids": [sid("picks"), sid("c3_reply")], "base_pointers": [B["art_bow_root"]],
     "requirement": "R4", "expected_wrong_reading": "the eight are Robert's 25 Sep post, with the dynamite",
     "resolver": "Robert's own reply of 26 Sep under Julia's bow post: it goes in the eight in place of the last item on his list, the dynamite; the ask keeps his latest word",
     "discovery_order": "a search for the playable returns the 25 Sep post in #zombie-design; the reply is in #zombie-art under a post about an arrow",
     "version_records": [vr("slack", sid("picks"), True, S["picks"]["at"], f"slack:{sid('picks')}"),
                         vr("slack", sid("c3_reply"), True, S["c3_reply"]["at"], f"slack:{B['art_bow_root']}")]},
    {"id": "T6", "family": "exact_predicate", "services": ["gdocs", "gsheets"], "seeded_ids": [NOTES, sid("tracker")], "base_pointers": [],
     "requirement": "R4", "expected_wrong_reading": "every line outside the eight is an Extra, the cannon, the zombies, the sound cues and the fonts included",
     "resolver": "the notes: Board set is Default for the eight, Extra for every other board item, and empty for anything that is not a board item; the pack list's Kind column says which lines are board items",
     "discovery_order": "the rule and the Kind column are both on the first-read path; the trap is applying 'Extra' to all 88 other lines"},
    {"id": "T7", "family": "completion_elsewhere", "services": ["linear", "gdocs"], "seeded_ids": [tick("Cello"), sid("c4_log")], "base_pointers": [],
     "requirement": "R3", "expected_wrong_reading": "the eight instruments in Friday's zip are Ready: each ticket says FBX from Claire, opens, looks right, zipped, in the outgoing folder",
     "resolver": "Brian's own log of the outgoing folder (30 Sep): that zip was cut off on upload, will not unpack and is the only copy in the folder, so each is Owed (put the files back, Brian)",
     "discovery_order": "the tickets say the files are in the outgoing folder; the log is a second document by the list's owner that nothing links, found by looking for that folder"},
    {"id": "T8", "family": "effective_date", "services": ["slack"], "seeded_ids": [], "base_pointers": [B["vendor_formats"], B["vendor_oct6"], B["vendor_nov3"]],
     "requirement": "R5", "expected_wrong_reading": "the project starts on 29 September, or on 6 October",
     "resolver": "base: the vendor's last message sets 3 November",
     "discovery_order": "all three dates are in the PlayableX channel; the latest is the last message",
     "version_records": [vr("slack", B["vendor_formats"], False, "2025-09-16T11:34:19Z", f"slack:{VTHREAD}", base=True),
                         vr("slack", B["vendor_oct6"], False, "2025-09-24T08:18:18Z", f"slack:{M.VENDOR_CH}/1758227288.370029", base=True),
                         vr("slack", B["vendor_nov3"], False, "2025-09-30T09:59:55Z", f"slack:{B['fred_pause']}", base=True)]},
    {"id": "T9", "family": "distractor", "distractor_type": "withdrawn_ask", "services": ["confluence"], "seeded_ids": [], "base_pointers": [f"confluence:{B['gdd_c1']}", f"confluence:{B['gdd_c2']}"],
     "requirement": "R5", "expected_wrong_reading": "the tray has six slots (Julia's July proposal in the design page's comments)",
     "resolver": "base: Robert's reply on the page keeps it at seven"},
    {"id": "T10", "family": "completion_elsewhere", "services": ["slack"], "seeded_ids": [tick("Zombie characters")],
     "base_pointers": [B["vendor_blank_scene"], B["anim_pack"], B["brian_pack3"], B["vendor_zombie_ask"]],
     "requirement": "R2", "expected_wrong_reading": "the zombie characters are Owed: the vendor said the package was not exported correctly",
     "resolver": "base: Marcus's pack, tested in an empty project, went on 26 Sep; the vendor reviewed it on 29 Sep and asked for a choice, not for files",
     "discovery_order": "the complaint (25 Sep) comes before the pack (26 Sep) in the same thread"},
    {"id": "T11", "family": "scope_alias", "services": ["trello", "gcal"], "seeded_ids": [sid("trello_note"), sid("hold")], "base_pointers": [f"trello:{B['trello_kickoff']}"],
     "requirement": "R7", "expected_wrong_reading": "the files are shared with whoever is on Leonard's Playable Kickoff card",
     "resolver": "the notes name the kickoff hold: its attendees are Frederick, Julia, Brian and Robert",
     "discovery_order": "a search for the kickoff returns the Trello card by its title before the calendar hold"},
    {"id": "T12", "family": "distractor", "distractor_type": "other_title", "services": ["slack"], "seeded_ids": [], "base_pointers": [B["vendor_fbx_march"]],
     "requirement": "R2", "expected_wrong_reading": "everything has to be FBX (the March rule from the first playable)",
     "resolver": "base: for this playable the vendor takes .fbx (binary), .glb or .blend for 3D (16 and 19 Sep)"},
    {"id": "T13", "family": "distractor", "distractor_type": "non_authoritative_instruction", "services": ["slack"], "seeded_ids": [], "base_pointers": [B["julia_shuriken_idea"], B["robert_remain"]],
     "requirement": "R4", "expected_wrong_reading": "a board of grenades and shuriken (Julia's own 22 Sep idea)",
     "resolver": "base: Robert answered 'remain as is'; his eight are the board"},
    {"id": "T14", "family": "distractor", "distractor_type": "partial_listing", "services": ["slack", "gslides"], "seeded_ids": [sid("deck")], "base_pointers": [B["fred_scenario1"], B["julia_level"]],
     "requirement": "R4", "expected_wrong_reading": "the board is grenade, couch and plush doll (Frederick's 15 Sep 'good start', and the reference level as built)",
     "resolver": "that was the reference level; the vendor asked for an 8-item set and Robert's 25 Sep post names the eight"},
    {"id": "T15", "family": "mutable_pointer", "services": ["gslides", "slack"], "seeded_ids": [sid("deck"), sid("picks")], "base_pointers": [],
     "requirement": "R4", "expected_wrong_reading": "the items on Julia's deck are the board the vendor builds",
     "resolver": "the deck is the level as built on 23 Sep; Robert's eight came two days later",
     "discovery_order": "the notes send the reader to the deck for what was built",
     "version_records": [vr("gslides", sid("deck"), True, S["deck"]["at"], f"file:{sid('deck')}"),
                         vr("slack", sid("picks"), True, S["picks"]["at"], f"slack:{sid('picks')}")]},
    {"id": "T16", "family": "scope_alias", "services": ["slack", "gsheets"], "seeded_ids": [sid("tracker")], "base_pointers": [B["vendor_duck"], B["brian_zip2"], B["vendor_asset_list"]],
     "requirement": "R1", "expected_wrong_reading": "PlayableX's 'duck asset' and 'rocket launcher' are lines missing from the list",
     "resolver": "base: the duck is the Plushie Chick Brian sent the same day; the launcher is the Cannon line"},
    {"id": "T17", "family": "distractor", "distractor_type": "lookalike_entity", "services": ["gdocs"], "seeded_ids": [], "base_pointers": [f"gdocs:{B['playable_feedback_doc']}"],
     "requirement": "R2", "expected_wrong_reading": "Leonard's Playable Feedback (P0, P1, P2) is the rule for what is ready",
     "resolver": "that doc is feedback on the first playable; the notes for this one are Frederick's"},
    {"id": "T18", "family": "near_miss_mention", "services": ["github"], "seeded_ids": [], "base_pointers": [B["pr462_comment"], B["pr460"]],
     "requirement": "R2", "expected_wrong_reading": "every item match3d#462 or #460 touches has to go again (Kettlebell, Dart Board, Candy; the shared texture atlases)",
     "resolver": "Kettlebell, Dart Board and Candy are not lines of the pack; #460 adds new objects and names no line's art as changed"},
    {"id": "T19", "family": "distractor", "distractor_type": "keyword_collision", "services": ["linear"], "seeded_ids": [], "base_pointers": [B["zom97"]],
     "requirement": "R6", "expected_wrong_reading": "the object tickets under ZOM-97 (REVISION FOR ITEMS: Bathtub, Iron, Washing Machine, ...) are the lines' tickets",
     "resolver": "the pack list names each line's ticket; the notes say tickets live under Brian's pack ticket"},
]
mechanism_portfolio = [
    {"id": "EXPORT", "mechanism": "A24", "prior_family": "done_gap", "prior_family_reason": "v2 trap 1: a done claim on the ticket (exported, opens, in the outgoing folder) with the missing piece (the file is in a format the vendor refuses) in another service",
     "nodes": ["T1", "C1"], "requirement": "R2", "natural_reading": "the twelve lines saved out of the project are Ready", "decides": ["State", "What's owed", "Who has it"],
     "controls": ["Rolling Pin"], "over_application": "export_over", "source": "slack-root-unnamed-channel", "signature": "the models saved out of Unity on Thursday are the text kind"},
    {"id": "ARTHOLD", "mechanism": "A11", "prior_family": "superseding", "prior_family_reason": "v2 trap 2: a later statement by someone who knows the art, in another place (Julia's DM with Robert, not with the artist), about a category and no line",
     "nodes": ["T2", "C2"], "requirement": "R3", "natural_reading": "the twelve exported bathroom lines are Ready", "decides": ["State", "What's owed", "Who has it"],
     "controls": ["Desk Lamp"], "over_application": "art_over", "source": "slack-dm", "signature": "Claire is redoing the UVs on the bathroom objects"},
    {"id": "REVISED", "mechanism": "A25", "prior_family": "completion_elsewhere", "prior_family_reason": "v2 move A25: the change is met first (Robert's post, read in every rev1 run); the completion that undoes it is a later entry in a second document by the list's owner",
     "nodes": ["T3", "C3"], "requirement": "R2", "natural_reading": "Cactus Plant, Chainsaw and Cone are Owed (the file again, with Claire)", "decides": ["State", "What's owed", "Who has it"],
     "controls": ["Fly Zapper"], "over_application": "revised_over", "source": "gdocs-second-carrier", "signature": "Claire sent the three recoloured models again"},
    {"id": "AUDIO", "mechanism": "A13", "prior_family": "authority", "prior_family_reason": "v2 trap 5: a rule in the notes (only sound that is ours) whose deciding fact sits in a sheet nothing links",
     "nodes": ["T4", "C5"], "requirement": "R2", "natural_reading": "all five exported cues are Ready", "decides": ["State", "What's owed", "Who has it"],
     "controls": ["Success sound"], "over_application": "audio_over", "source": "gsheets-unlinked", "signature": "the rocket sound is from a library seat and the explosion from a bought pack"},
    {"id": "PICKS", "mechanism": "A14", "prior_family": "superseding", "prior_family_reason": "v2 trap 2: Robert's later reply under an unrelated post changes one pick; the reply names no item",
     "nodes": ["T5", "T15", "C4"], "requirement": "R4", "natural_reading": "the eight include the dynamite", "decides": ["Board set"],
     "controls": ["Grenade"], "over_application": "picks_over", "source": "slack-thread-reply", "signature": "the bow in place of the last item on Robert's list"},
    {"id": "ZIP", "mechanism": "A25", "prior_family": "completion_elsewhere", "prior_family_reason": "a second document by the list's owner says the zipped files cannot be opened; the tickets' own notes say they are in the folder and fine",
     "nodes": ["T7", "C6"], "requirement": "R3", "natural_reading": "the eight instruments in Friday's zip are Ready", "decides": ["State", "What's owed", "Who has it"],
     "controls": ["Music Keyboard"], "over_application": "zip_over", "source": "gdocs-second-carrier", "signature": "the zip with Friday's music instruments will not unpack"},
]
channels = [
    {"id": "CH-EXPORT", "kind": "member", "rule": "EXPORT", "degrade": "lines saved out of the project Ready", "members": names("A1"), "latent": "#zombie-match3d read for the week, or searched for the exporter", "family": "done_gap"},
    {"id": "CH-ARTHOLD", "kind": "member", "rule": "ARTHOLD", "degrade": "exported bathroom lines Ready", "members": names("A2"), "latent": "Julia's DM with Robert read for 29 Sep", "family": "superseding"},
    {"id": "CH-REVISED", "kind": "member", "rule": "REVISED", "degrade": "re-sent recoloured lines Owed", "members": names("C1"), "latent": "Brian's log of the outgoing folder opened", "family": "completion_elsewhere"},
    {"id": "CH-AUDIO", "kind": "member", "rule": "AUDIO", "degrade": "library and bought-pack cues Ready", "members": names("C2"), "latent": "Calvin's sources sheet opened", "family": "authority"},
    {"id": "CH-PICKS", "kind": "member", "rule": "PICKS", "degrade": "the dynamite stays in the eight", "members": ["Bow", "Dynamite"], "latent": "Robert's reply under the bow post opened", "family": "superseding"},
    {"id": "CH-ZIP", "kind": "member", "rule": "ZIP", "degrade": "instruments in Friday's zip Ready", "members": names("C4"), "latent": "Brian's log of the outgoing folder opened", "family": "completion_elsewhere"},
]
call_budget = [
    {"phase": "discovery", "service": "slack", "calls": 10, "reason": "the ask in Frederick's DM; the PlayableX channel (two pages and its two long threads); Robert's two posts in #zombie-design; the 22 Sep playable thread; Julia's DM with Brian about the reference level"},
    {"phase": "discovery", "service": "gdocs", "calls": 2, "reason": "Frederick's hand-off notes; Leonard's Playable Feedback (rejected: the first playable)"},
    {"phase": "discovery", "service": "gdrive", "calls": 3, "reason": "find the notes, the pack list and the deck shared with Julia; look at her own root for the destination"},
    {"phase": "discovery", "service": "gsheets", "calls": 2, "reason": "Brian's pack list: sheet metadata and its rows"},
    {"phase": "discovery", "service": "gslides", "calls": 1, "reason": "Julia's deck of the reference level"},
    {"phase": "discovery", "service": "confluence", "calls": 2, "reason": "the design page and its comments (tray size, how a level is lost)"},
    {"phase": "discovery", "service": "gcal", "calls": 2, "reason": "find the kickoff hold and read its attendees"},
    {"phase": "discovery", "service": "contacts", "calls": 1, "reason": "PlayableX's intake address"},
    {"phase": "discovery", "service": "trello", "calls": 2, "reason": "the Playable Kickoff card and its comment (rejected as the recipient source)"},
    {"phase": "enumeration", "service": "linear", "calls": 3, "reason": f"the pack ticket and two pages of its {n_list} children (keys, states)"},
    {"phase": "per-record", "service": "linear", "calls": len(TICKETS), "reason": "each line's ticket comments: Brian's note on what he did with the line"},
    {"phase": "reconciliation", "service": "gdocs", "calls": 2, "reason": "Brian's log of the outgoing folder: find it and read it"},
    {"phase": "reconciliation", "service": "slack", "calls": 8, "reason": "#zombie-art since 24 Sep and Julia's bow thread; her DM with Robert; #zombie-match3d for the week; #zm-animations for the zombie pack"},
    {"phase": "reconciliation", "service": "gsheets", "calls": 2, "reason": "Calvin's sound sources sheet: find it and read its rows"},
    {"phase": "reads-before-writes", "service": "linear", "calls": 3, "reason": "team, states and users for the ticket writes"},
    {"phase": "per-record", "service": "linear", "calls": 2 * n_owed, "reason": f"each of the {n_owed} Owed lines with a ticket: a state write (In Progress to Todo) and a comment saying what is owed and who has it"},
    {"phase": "writes", "service": "gsheets", "calls": 2, "reason": f"create the hand-off list in Julia's Drive and write its {n_all} rows"},
    {"phase": "writes", "service": "gdocs", "calls": 1, "reason": "create the brief with its text"},
    {"phase": "writes", "service": "gdrive", "calls": 8, "reason": "share both files view-only with the three other people on the hold and PlayableX's intake address"},
    {"phase": "writes", "service": "slack", "calls": 2, "reason": "the three counts to Frederick in his DM; both links in the PlayableX channel"},
    {"phase": "read-back", "service": "gsheets", "calls": 1, "reason": "read the list back against the pack list's rows"},
    {"phase": "read-back", "service": "linear", "calls": 1, "reason": "list the pack ticket's children to confirm the Todo set"},
]
writes = [
    {"service": "gsheets", "tool": "gsheets_create_spreadsheet+gsheets_values_update", "count": 2, "depends_on": ["K1", "K2", "C1", "C2", "C3", "C4", "C5", "C6", "T6"], "requirements": ["R1", "R2", "R3", "R4", "R7"]},
    {"service": "gdocs", "tool": "gdocs_create_document", "count": 1, "depends_on": ["K3", "K6", "K9", "K10", "K12", "K13", "K15", "C4", "C5"], "requirements": ["R5", "R7"]},
    {"service": "linear", "tool": "linear_create_comment", "count": n_owed, "template": True, "depends_on": ["K1", "K4", "C1", "C2", "C3", "C5", "C6"], "requirements": ["R6"]},
    {"service": "linear", "tool": "linear_update_issue", "count": n_owed, "template": True, "depends_on": ["K1", "K4", "C1", "C2", "C3", "C5", "C6"], "requirements": ["R6"]},
    {"service": "gdrive", "tool": "gdrive_share_file", "count": 8, "template": True, "depends_on": ["K7", "K8"], "requirements": ["R7"]},
    {"service": "slack", "tool": "slack_send_message", "count": 2, "depends_on": ["A1", "A2", "C1", "C2", "C3", "C5", "C6"], "requirements": ["R7"]},
]
tot = sum(r["calls"] for r in call_budget); per = sum(r["calls"] for r in call_budget if r["phase"] == "per-record")
manifest = {
    "_note": "draft manifest (/create-scenario --revise, design D3 for injection rev2; rev1's draft is in run_forensics/rev1/artifacts); /create-injection writes 01_Hardness_Manifest.json keeping every id or listing it in design_delta. Seeded texts quoted in delegation_quote are the planned wording (plan/planned_texts.py).",
    "persona": M.PERSONA,
    "assignment_context": {"context_hash": ctx["context_hash"], "assignment_hash": ctx["assignment_hash"], "policy_hash": ctx["policy_hash"],
                           "freeze_utc": ctx["freeze_utc"], "difficulty_mode": ctx["difficulty_mode"]},
    "horizon": "Long Horizon", "effective_profile": "extreme",
    "author_targets": {"min_calls_per_run": 130, "max_avg_weighted_pass": 0.70, "target_avg_weighted_pass": 0.62, "requester_confirmation": CONFIRM},
    "volume_exception": {"reason": (f"the cohort is the {n_all} lines of one playable pack; honest necessary calls are about {tot} (a run that finds no hidden record about 175): "
                                    "one comment read per line's ticket, two writes per Owed ticket, the two deliverables and their delivery; "
                                    "nothing is added to raise the count"),
                         "requester_confirmation": CONFIRM + "; the per-record floor of 110 is the author's choice under that delegation",
                         "call_budget_floor": 220, "per_record_floor": 110},
    "requirements": requirements, "services": services, "anchors": anchors, "ask_fragments": ask_fragments, "authorities": authorities,
    "cohort": cohort, "chains": chains, "traps": traps, "mechanism_portfolio": mechanism_portfolio, "channels": channels,
    "call_budget": call_budget, "writes": writes, "hazard_acknowledgements": [], "denied_probes": [],
    "gradable_surface": "01_Gradable_Surface.json",
}
out = WF / "01_Hardness_Manifest.draft.json"
out.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
print("manifest ->", out.name, "| budget", tot, "per-record", per, "| owed tickets", n_owed, "| fragments", len(ask_fragments), "traps", len(traps))
