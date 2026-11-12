#!/usr/bin/env python3
"""Build Working_Files/01_Hardness_Manifest.draft.json from design_model.py (scenario stage). No SQL, no prompt text."""
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
OWED_TICKETS = [l for l in M.LINES if l["state"] == "Owed" and l["ticket"]]
CONFIRM = ("task author in chat on 2026-11-11: '220 calls are good with required failure'; and 'my task is a long horizon task "
           "soo i want over 130+ tool calls in each runs and also i want difficulty pass rate under 70% and also have to folllow "
           "all other difficulty guidelines soo you can choose from your self which option is best fit for my requirements in this task'")

requirements = {
    "R1": "list population: every line on Brian's pack list plus anything PlayableX asked for or Robert added that is not on it (103 lines)",
    "R2": "state per line: Delivered, Ready or Owed under Frederick's hand-off notes",
    "R3": "for an Owed line: what is owed and who has it",
    "R4": "the board: the default eight (Robert's picks as he last left them) and every other board object as an extra",
    "R5": "brief content: scenario, how the level plays (tray, win and fail), zombies and primary animation, formats, sound rules, start date",
    "R6": "tickets: an Owed line's ticket back to Todo with a comment saying what is owed and who has it; a new ticket under the pack ticket for a line without one; Delivered and Ready tickets untouched",
    "R7": "delivery: the brief and the hand-off list in Julia's Drive; view-only sharing with the kickoff hold's attendees and PlayableX's intake address; the three counts to Frederick in his DM; both links in the PlayableX channel",
}
services = {
    "slack": {"role": "the ask (Frederick's DM), the PlayableX channel (what was asked for, sent and when), Robert's picks and his later reply, Arthur's object-browser post, Claire's DM; writes: the reply and the channel post",
              "weight_reason": "the ask, the default eight, two withdrawn 'done' states (24 lines) and both message destinations exist only in Slack"},
    "linear": {"role": "the pack ticket ART-793 and its 97 children with their export and art notes; Brian's comment on the pack ticket; writes: Todo moves, comments, six new tickets",
               "weight_reason": "every line's export and art notes are only in its own ticket comments; the music set's failure is only on the pack ticket"},
    "gsheets": {"role": "Brian's pack list (membership, set, delivery, ticket); Calvin's sound source sheet; write: the hand-off list",
                "weight_reason": "the list of lines and each line's set and delivery; which sound cues are ours"},
    "gdocs": {"role": "Frederick's hand-off notes (state definitions, current version, sound, tickets, sharing); write: the brief",
              "weight_reason": "the three states and the follow-through rule are defined only there"},
    "gdrive": {"role": "Julia's Drive root (destination), file metadata and sharing; write: view-only shares",
               "weight_reason": "both deliverables are created there and shared from there"},
    "gslides": {"role": "Julia's reference-level deck (layout, the eight objects as built on 23 Sep, win and fail)",
                "weight_reason": "the level layout for the brief; its object list is the older version of the default eight"},
    "gcal": {"role": "Frederick's kickoff hold on 3 Nov (attendees)", "weight_reason": "who both files are shared with"},
    "contacts": {"role": "PlayableX's intake contact", "weight_reason": "the address both view links are shared with"},
    "github": {"role": "base match3d#462 'Objects Revisions and Changes' (merged 25 Sep)", "weight_reason": "which sent objects changed after they went out"},
    "confluence": {"role": "base design page (7-slot tray, loss only at zero health) and its comments", "weight_reason": "how the level plays, for the brief"},
    "trello": {"role": "Leonard's Playable Kickoff card with his 30 Sep note; the UA/BD 'Playables' card", "weight_reason": "confirms the parked state and who is sorting the pack; not a rule source"},
    "gmail": {"role": "invitation mails for the kickoff hold in the attendees' mailboxes", "weight_reason": "companions of the hold; carry the same attendee list"},
}
anchors = [
    {"id": "A1", "service": "slack", "record": sid("ask"), "locator": sid("ask"), "prompt_reference": "Frederick's playable message",
     "requirement_ids": ["R1", "R4", "R7"]},
    {"id": "A2", "service": "slack", "record": M.VENDOR_CH, "locator": M.VENDOR_CH, "prompt_reference": "the PlayableX channel", "requirement_ids": ["R7"]},
    {"id": "A3", "service": "gdrive", "record": B["julia_root"], "locator": B["julia_root"], "prompt_reference": "my Drive", "requirement_ids": ["R7"]},
]
def frag(fid, service, container, locator, kind, via, seeded, base, by, quote, reqs, names=None, **kw):
    f = {"id": fid, "service": service, "container": container, "locator": locator, "kind": kind, "incorporated_via": via,
         "seeded_ids": seeded, "base_pointers": base, "delegated_by_record": by, "delegation_quote": quote, "requirement_ids": reqs}
    if names: f["names_authorities"] = names
    f.update(kw); return f
ASK, NOTES = sid("ask"), sid("notes")
ask_fragments = [
    frag("K1", "gdocs", NOTES, NOTES, "delegation", ["A1"], [NOTES], [], ASK,
         q(TXT.ASK, "My hand-off notes say what counts as ready and what to do with the tickets"), ["R2", "R3", "R6"],
         [{"id": "H1", "quote": "My hand-off notes"}]),
    frag("K2", "gsheets", sid("tracker"), sid("tracker"), "requirement", ["A1"], [sid("tracker")], [], ASK,
         q(TXT.ASK, "Brian's pack list is where it starts"), ["R1"], [{"id": "H2", "quote": "Brian's pack list"}]),
    frag("K3", "slack", sid("picks"), sid("picks"), "requirement", ["A1"], [sid("picks")], [], ASK,
         q(TXT.ASK, "Robert's picks for the board and the zombies stand"), ["R4"]),
    frag("K4", "slack", f"{M.VENDOR_CH}/1758227288.370029", B["vendor_asset_list"], "requirement", ["A1"], [], [B["vendor_asset_list"]], ASK,
         q(TXT.ASK, "anything they've asked us for in the channel that isn't on it"), ["R1"]),
    frag("K5", "linear", "ART-793", "ART-793", "destination", ["A1", "K1"], ["ART-793"], [], NOTES,
         q(TXT.NOTES, "Tickets live under the pack ticket, one per line"), ["R6"]),
    frag("K6", "confluence", B["gdd"], B["gdd"], "requirement", ["A1", "K1"], [], [f"confluence:{B['gdd']}"], NOTES,
         q(TXT.NOTES, "How the level plays is on the design page"), ["R5"]),
    frag("K7", "gcal", sid("hold"), sid("hold"), "recipient", ["A1", "K1"], [sid("hold")], [], NOTES,
         q(TXT.NOTES, "Everyone on the kickoff hold"), ["R7"], [{"id": "H3", "quote": "the kickoff hold"}]),
    frag("K8", "contacts", sid("contact"), sid("contact"), "recipient", ["A1", "K1"], [sid("contact")], [], NOTES,
         q(TXT.NOTES, "their intake address, which is in Contacts"), ["R7"]),
    frag("K9", "gslides", sid("deck"), sid("deck"), "requirement", ["A1", "K1"], [sid("deck")], [], NOTES,
         q(TXT.NOTES, "your reference-level deck has the layout"), ["R5"]),
    frag("K10", "slack", sid("zpicks"), sid("zpicks"), "requirement", ["A1"], [sid("zpicks")], [B["vendor_zombie_ask"]], ASK,
         q(TXT.ASK, "Robert's picks for the board and the zombies stand"), ["R5"]),
    frag("K11", "slack", B["art_bow_root"], sid("c3_reply"), "amendment", ["A1"], [sid("c3_reply")], [B["art_bow_root"]], ASK,
         q(TXT.ASK, "unless he's changed them since"), ["R4"], supersedes="K3",
         resolver="Robert's own later reply (26 Sep) changes his 23 Sep picks; the ask keeps his latest word"),
    frag("K12", "slack", f"{M.VENDOR_CH}/1757695108.506159", B["vendor_formats"], "format", ["A1", "K1"], [], [B["vendor_formats"], B["vendor_asset_list"]], NOTES,
         q(TXT.NOTES, "What they told us about formats in the channel still holds"), ["R2", "R5"]),
    frag("K15", "slack", B["art_bow_root"], sid("c3_reply"), "requirement", ["A1", "K1"], [sid("c3_reply")], [], NOTES,
         q(TXT.NOTES, "If Robert has added objects since Brian made the list, they go on it too"), ["R1"]),
    frag("K13", "slack", B["vendor_music_rule"], B["vendor_music_rule"], "requirement", ["A1", "K1"], [], [B["vendor_music_rule"]], NOTES,
         q(TXT.NOTES, "so does what they told us about sound last time"), ["R5"]),
    frag("K14", "slack", B["vendor_nov3"], B["vendor_nov3"], "requirement", ["A2"], [], [B["vendor_nov3"]], M.VENDOR_CH,
         "We’re planning the new start date for the game on November 3rd", ["R5"]),
]
authorities = [
    {"id": "H1", "name": "Frederick's hand-off notes", "home_service": "gdocs", "decoy_service": "gdocs", "governs": ["R2", "R3", "R6"],
     "findable_query": "hand-off notes", "seeded_ids": [NOTES], "base_pointers": [], "decoy_seeded_ids": [],
     "decoy_base_pointers": [f"gdocs:{B['playable_feedback_doc']}"],
     "decoy_scope": {"dimension": "game", "decoy": "Domino Delights (the first playable, April 2025: Leonard's Playable Feedback)", "task": "Zombie Match 3D (the second playable)"}},
    {"id": "H2", "name": "Brian's pack list", "home_service": "gsheets", "decoy_service": "slack", "governs": ["R1"],
     "findable_query": "playable pack", "seeded_ids": [sid("tracker")], "base_pointers": [], "decoy_seeded_ids": [],
     "decoy_base_pointers": [B["vendor_asset_list"]],
     "decoy_scope": {"dimension": "issuer", "decoy": "PlayableX's request (asset groups they expect, no lines)", "task": "Brian's list (what was packed, line by line)"}},
    {"id": "H3", "name": "the kickoff hold", "home_service": "gcal", "decoy_service": "trello", "governs": ["R7"],
     "findable_query": "PlayableX kickoff", "seeded_ids": [sid("hold")], "base_pointers": [], "decoy_seeded_ids": [sid("trello_note")],
     "decoy_base_pointers": [f"trello:{B['trello_kickoff']}"],
     "decoy_scope": {"dimension": "issuer", "decoy": "Leonard's own to-do card (no attendees)", "task": "Frederick's calendar hold (the attendee list)"}},
]
cohort = {
    "definition": "every line of the playable pack: the 97 rows of Brian's pack list (78 board objects, 4 zombies, the cannon and its shot, 5 interface pieces, the background, 6 sound cues, the fonts) plus the six board objects Robert added in a later reply",
    "definition_source": [sid("tracker"), sid("c3_reply")], "key": "line", "size": len(M.LINES),
    "evidence_surfaces": [
        {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1.0, "records": len(TICKETS), "seeded": True, "seeded_ids": TICKETS,
         "requirement": "R2", "decides": "state per line: Delivered, Ready or Owed",
         "why_no_bulk": "linear_list_issues and linear_get_issue return no comments; each line's export note (file type, date, how it was exported) and art note are only in its own ticket's comments",
         "short_circuit": "the pack list has no state column: delivery says what went out, not whether the file is in a format they take or is still current; no other record states a line's export"},
        {"service": "linear", "tool": "linear_update_issue + linear_create_comment", "per_record_calls": 2.0, "records": len(OWED_TICKETS), "seeded": False,
         "requirement": "R6", "decides": "an Owed line's ticket back to Todo with a comment saying what is owed and who has it",
         "why_no_bulk": "no batch write exists for state changes or comments; each ticket takes its own calls",
         "short_circuit": "the notes require the Todo state and the comment on every Owed line's ticket; the sheet does not replace them"},
        {"service": "github", "tool": "github_get_pull_request + github_get_pull_request_files", "per_record_calls": 0.4, "records": 5, "seeded": False,
         "requirement": "R2", "decides": "state per line: Delivered, Ready or Owed",
         "why_no_bulk": "a pull request search returns titles and bodies; #462's body is empty, so the objects it changed are only in its file list",
         "short_circuit": "the pack list and the tickets predate the 25 Sep change; nothing on them says the art moved after the files went out"},
    ],
}
chains = [
    {"id": "C1", "root_cause": "A24", "ends_in": "R2", "hops": [
        {"service": "gsheets", "record": sid("tracker"), "finding": "twelve appliance and furniture lines are on the list with no delivery (extras)"},
        {"service": "linear", "record": tick("Washing Machine"), "finding": "Brian's note: model file exported from the object browser, all twelve in one go, 25 Sep, in the outgoing folder; ticket Done"},
        {"service": "slack", "record": sid("a1_post"), "finding": "Arthur, 27 Sep: the browser's new multi-select button writes an empty shell per object; redo by hand anything pushed out with it"}]},
    {"id": "C2", "root_cause": "A11", "ends_in": "R3", "hops": [
        {"service": "gsheets", "record": sid("tracker"), "finding": "twelve lines carry the set Bathroom"},
        {"service": "linear", "record": tick("Bathtub"), "finding": "Brian's note: exported 25 Sep; Claire's earlier note: fine to go"},
        {"service": "slack", "record": sid("a2_dm"), "finding": "Claire, 26 Sep, to Julia: redoing the UVs on the bathroom ones; what Brian pulled on Thursday is the old unwrap; nothing goes until she says"}]},
    {"id": "C3", "root_cause": "A1", "ends_in": "R2", "hops": [
        {"service": "gsheets", "record": sid("tracker"), "finding": "Cactus Plant, Chainsaw and Traffic Cone went in the 24 Sep zip; Dartboard and Candy were exported on the morning of 25 Sep"},
        {"service": "slack", "record": B["art_claire_pr"], "finding": "Claire, 25 Sep 14:02 UTC: pushed the changes Robert asked for (cactus, candy, cone, dartboard) in a new pull request"},
        {"service": "github", "record": B["pr462"], "finding": "'Objects Revisions and Changes' merged 25 Sep 23:15 UTC: the art of five sent or exported lines changed afterwards"},
        {"service": "gdocs", "record": NOTES, "finding": "if the art changed after a file went out, it goes again"}]},
    {"id": "C4", "root_cause": "A14", "ends_in": "R4", "hops": [
        {"service": "slack", "record": sid("picks"), "finding": "Robert, 23 Sep: the eight board objects, the iron among them"},
        {"service": "gslides", "record": sid("deck"), "finding": "Julia's deck shows the level as built that day, with the iron"},
        {"service": "slack", "record": sid("c3_reply"), "finding": "Robert, 26 Sep, under Julia's bow post in #zombie-art: the bow goes on the board instead of the iron; six round objects are missing from Brian's list"}]},
    {"id": "C5", "root_cause": "A13", "ends_in": "R2", "hops": [
        {"service": "linear", "record": tick("Match scale"), "finding": "Brian's note: .wav exported, in the outgoing folder"},
        {"service": "gdocs", "record": NOTES, "finding": "only sound we own outright leaves the studio"},
        {"service": "gsheets", "record": sid("c2_sheet"), "finding": "Calvin's source sheet: the match scale and the explosion are cut from a bought pack, in-game licence only"}]},
    {"id": "C6", "root_cause": "A3", "ends_in": "R3", "hops": [
        {"service": "gsheets", "record": sid("tracker"), "finding": "eight lines carry the set Music"},
        {"service": "linear", "record": tick("Cello"), "finding": "Brian's note: exported .glb, Fri 26 Sep, in the outgoing folder; ticket Done"},
        {"service": "linear", "record": sid("c4_comment"), "finding": "Brian, 29 Sep, on the pack ticket itself: the music set from Friday's export comes in grey in an empty scene; needs another pass"}]},
]
def vr(service, rid, seeded, at, container=None, base=False):
    r = {"service": service, "seeded": seeded, "at": at}
    r["base_pointer" if base else "id"] = rid
    if container: r["container"] = container
    return r
traps = [
    {"id": "T1", "family": "done_gap", "services": ["gsheets", "linear", "slack"], "seeded_ids": [sid("tracker"), tick("Washing Machine"), sid("a1_post")], "base_pointers": [],
     "requirement": "R2", "expected_wrong_reading": "the twelve appliance and furniture lines are Ready: each ticket is Done and says the model file is exported and in the outgoing folder",
     "resolver": "Arthur's 27 Sep post in #zombie-bugs: the object browser's new multi-select button writes an empty shell per object; the twelve were exported in one go on 25 Sep, so each is Owed (re-export one at a time, Brian)",
     "discovery_order": "the pack list and each ticket's comments are read while building the list; the post sits in a channel the ask never names and uses none of the ask's words"},
    {"id": "T2", "family": "superseding", "services": ["linear", "slack"], "seeded_ids": [tick("Bathtub"), sid("a2_dm")], "base_pointers": [],
     "requirement": "R3", "expected_wrong_reading": "the twelve bathroom lines are Ready: exported 25 Sep, and Claire's ticket note says the art is fine to go",
     "resolver": "Claire's 26 Sep DM to Julia: she is redoing the UVs on the bathroom ones and what Brian pulled on Thursday is the old unwrap, so each is Owed (art, Claire)",
     "discovery_order": "Claire's ticket note (24 Sep) is on every bathroom ticket; her DM is a day and a half later, in a direct message that names no object and no ticket",
     "version_records": [vr("linear", M.comment_id("claire_ok_bathtub"), True, "2025-09-24T09:20:00Z", f"linear:{tick('Bathtub')}"),
                         vr("slack", sid("a2_dm"), True, "2025-09-26T08:10:00Z", f"slack:{sid('a2_dm')}")]},
    {"id": "T3", "family": "effective_date", "services": ["gsheets", "slack", "github"], "seeded_ids": [sid("tracker")], "base_pointers": [B["brian_zip1"], B["art_claire_pr"], B["pr462"]],
     "requirement": "R2", "expected_wrong_reading": "Cactus Plant, Chainsaw and Traffic Cone are Delivered (in the 24 Sep zip) and Dartboard and Candy are Ready (exported 25 Sep)",
     "resolver": "base: Robert asked for changes on the evening of 24 Sep, Claire pushed them on 25 Sep and match3d#462 merged at 23:15 UTC; the notes send a file again when the art changed after it went out, so all five are Owed",
     "discovery_order": "the delivery column is the first thing read for these lines; the change is in #zombie-art and GitHub, a day after the zip",
     "version_records": [vr("slack", B["brian_zip1"], False, "2025-09-24T12:39:36Z", f"slack:{M.VENDOR_CH}/1758227288.370029", base=True),
                         vr("github", B["pr462"], False, "2025-09-25T11:43:06Z", f"github:match3d#462", base=True)]},
    {"id": "T4", "family": "authority", "services": ["gdocs", "gsheets", "linear"], "seeded_ids": [NOTES, sid("c2_sheet"), tick("Match scale"), tick("Explosion")], "base_pointers": [],
     "requirement": "R2", "expected_wrong_reading": "all five exported sound cues are Ready (.wav, a format PlayableX takes)",
     "resolver": "the notes let only sound we own outright leave; Calvin's source sheet marks the match scale and the explosion as cut from a bought pack with an in-game licence, so both are Owed (Calvin)",
     "discovery_order": "format is the visible test and all five pass it; the source of each cue is in a sheet no ticket links"},
    {"id": "T5", "family": "superseding", "services": ["slack"], "seeded_ids": [sid("picks"), sid("c3_reply")], "base_pointers": [B["art_bow_root"]],
     "requirement": "R4", "expected_wrong_reading": "the default eight are Robert's 23 Sep picks, the iron among them",
     "resolver": "Robert's 26 Sep reply under Julia's bow post in #zombie-art: the bow goes on the board instead of the iron",
     "discovery_order": "the picks are a root post in #zombie-design, found by searching for Robert's picks; the reply is in another channel under a post about an arrow",
     "version_records": [vr("slack", sid("picks"), True, "2025-09-23T17:00:00Z", f"slack:{sid('picks')}"),
                         vr("slack", sid("c3_reply"), True, "2025-09-26T17:05:00Z", f"slack:{B['art_bow_root']}")]},
    {"id": "T6", "family": "exact_predicate", "services": ["gsheets", "slack", "linear"], "seeded_ids": [sid("tracker"), sid("c3_reply")], "base_pointers": [],
     "requirement": "R1", "expected_wrong_reading": "the list is the 97 rows of Brian's pack list",
     "resolver": "the ask adds anything Robert added that is not on it; his 26 Sep reply names six round objects missing from Brian's list, so the list has 103 lines and six new tickets",
     "discovery_order": "the pack list presents itself as complete; the six are named only in the same reply as the swap"},
    {"id": "T7", "family": "tool_surface", "services": ["linear", "gsheets"], "seeded_ids": [sid("c4_comment"), tick("Cello")], "base_pointers": [],
     "requirement": "R3", "expected_wrong_reading": "the eight music lines are Ready: each ticket is Done and says exported .glb on 26 Sep",
     "resolver": "Brian's 29 Sep comment on the pack ticket itself: the music set from Friday's export comes in grey in an empty scene and needs another pass, so each is Owed (Brian)",
     "discovery_order": "the children's comments are read line by line; the pack ticket's own comments are returned only by a comment read on the parent"},
    {"id": "T8", "family": "superseding", "services": ["slack"], "seeded_ids": [], "base_pointers": [B["vendor_formats"], B["vendor_oct6"], B["vendor_nov3"]],
     "requirement": "R5", "expected_wrong_reading": "the start is 29 September, or 6 October",
     "resolver": "base: the vendor's 30 Sep message sets 3 November",
     "version_records": [vr("slack", B["vendor_formats"], False, "2025-09-16T11:34:19Z", f"slack:{M.VENDOR_CH}/1757695108.506159", base=True),
                         vr("slack", B["vendor_oct6"], False, "2025-09-24T08:18:18Z", f"slack:{M.VENDOR_CH}/1758227288.370029", base=True),
                         vr("slack", B["vendor_nov3"], False, "2025-09-30T09:59:55Z", f"slack:{M.VENDOR_CH}/1759174925.309129", base=True)]},
    {"id": "T9", "family": "distractor", "distractor_type": "withdrawn_ask", "services": ["confluence"], "seeded_ids": [], "base_pointers": [f"confluence:{B['gdd_c1']}", f"confluence:{B['gdd_c2']}"],
     "requirement": "R5", "expected_wrong_reading": "the tray has six slots (Julia's July proposal in the design page comments)",
     "resolver": "base: Robert's reply keeps the page at seven; the page body says a 7-slot tray"},
    {"id": "T10", "family": "completion_elsewhere", "distractor_type": "already_done", "services": ["slack", "linear"], "seeded_ids": [tick("Zombie Chef")], "base_pointers": [B["vendor_blank_scene"], B["brian_pack3"]],
     "requirement": "R6", "expected_wrong_reading": "the zombie lines are Owed because PlayableX said the first package was not exported correctly",
     "resolver": "base: Brian sent the full Unity pack on 26 Sep and PlayableX reviewed it on 29 Sep; the four lines are Delivered and their tickets are not touched",
     "discovery_order": "the 25 Sep complaint is met before the 26 Sep pack when the thread is read in order"},
    {"id": "T11", "family": "near_miss_mention", "distractor_type": "scope_adjacent", "services": ["trello", "gcal"], "seeded_ids": [sid("trello_note"), sid("hold")], "base_pointers": [f"trello:{B['trello_kickoff']}"],
     "requirement": "R7", "expected_wrong_reading": "the kickoff is Leonard's card, so the brief goes to Leonard",
     "resolver": "the notes name the kickoff hold: its attendees are Frederick, Julia, Brian and Robert",
     "discovery_order": "a search for the kickoff returns the Trello card by its title before the calendar hold"},
    {"id": "T12", "family": "distractor", "distractor_type": "other_title", "services": ["slack"], "seeded_ids": [], "base_pointers": [B["vendor_fbx_march"]],
     "requirement": "R5", "expected_wrong_reading": "everything must be FBX (the March rule from the Domino Delights round)",
     "resolver": "base: for this playable the vendor takes .fbx, .glb or .blend for 3D (16 and 19 Sep)"},
    {"id": "T13", "family": "distractor", "distractor_type": "non_authoritative_instruction", "services": ["slack"], "seeded_ids": [], "base_pointers": [B["julia_shuriken_idea"], B["robert_remain"]],
     "requirement": "R4", "expected_wrong_reading": "a board of grenades and shuriken (Julia's own 22 Sep idea)",
     "resolver": "base: Robert answered 'remain as is'; his picks are the board"},
    {"id": "T14", "family": "distractor", "distractor_type": "stale_summary", "services": ["trello"], "seeded_ids": [], "base_pointers": [f"trello:{B['trello_playables']}"],
     "requirement": "R5", "expected_wrong_reading": "playables are 'Not Started' (the UA/BD board card, untouched since March)",
     "resolver": "the channel record: scenario chosen, assets sent, start set for 3 November"},
    {"id": "T15", "family": "mutable_pointer", "services": ["gslides", "slack"], "seeded_ids": [sid("deck"), sid("c3_reply")], "base_pointers": [],
     "requirement": "R4", "expected_wrong_reading": "the default eight are the eight objects on Julia's deck (the level as built on 23 Sep)",
     "resolver": "the deck shows the layout; Robert's later reply changes one object",
     "discovery_order": "the notes send the reader to the deck for the layout, where the eight are listed",
     "version_records": [vr("gslides", sid("deck"), True, "2025-09-23T19:50:00Z", f"file:{sid('deck')}"),
                         vr("slack", sid("c3_reply"), True, "2025-09-26T17:05:00Z", f"slack:{B['art_bow_root']}")]},
    {"id": "T16", "family": "scope_alias", "services": ["slack", "gsheets"], "seeded_ids": [sid("tracker")], "base_pointers": [B["vendor_duck"], B["brian_zip2"], B["vendor_asset_list"]],
     "requirement": "R1", "expected_wrong_reading": "PlayableX's 'duck asset' and 'rocket launcher' are lines missing from the list",
     "resolver": "base: the duck is the plushie Brian sent the same day (Plushie-and-zombies.zip); the launcher is the cannon line"},
    {"id": "T18", "family": "distractor", "distractor_type": "partial_listing", "services": ["slack"], "seeded_ids": [], "base_pointers": [B["fred_scenario1"]],
     "requirement": "R4", "expected_wrong_reading": "the board is grenade, couch and plush doll (Frederick's 15 Sep suggestion 'would be a good start')",
     "resolver": "that message names three objects as a start; Robert's picks list the eight"},
    {"id": "T19", "family": "distractor", "distractor_type": "keyword_collision", "services": ["slack"], "seeded_ids": [], "base_pointers": [f"{M.DESIGN_CH}/1756730298.517369"],
     "requirement": "R1", "expected_wrong_reading": "objects 'removed from the pool' (1 Sep) are lines to drop from the list",
     "resolver": "base: that message is about the card pool in the game's progression, not the pack; the list is Brian's rows plus Robert's six"},
    {"id": "T17", "family": "distractor", "distractor_type": "lookalike_entity", "services": ["gdocs"], "seeded_ids": [], "base_pointers": [f"gdocs:{B['playable_feedback_doc']}"],
     "requirement": "R2", "expected_wrong_reading": "Leonard's Playable Feedback (P0, P1, P2) is the rule for what is ready",
     "resolver": "that doc is feedback on the Domino Delights playable; the notes for this one are Frederick's"},
]
mechanism_portfolio = [
    {"id": "EXPORT", "mechanism": "A24", "prior_family": "done_gap", "prior_family_reason": "v2 trap 1: a done claim on the ticket (exported, in the outgoing folder) with the missing piece (the file is an empty shell) in another service",
     "nodes": ["T1", "C1"], "requirement": "R2", "natural_reading": "the twelve appliance and furniture lines are Ready", "decides": ["State", "What's owed", "Who has it"],
     "controls": ["Rolling Pin"], "over_application": "export_over", "source": "slack-root-unnamed-channel", "signature": "multi-select export from the object browser writes empty shells"},
    {"id": "ARTHOLD", "mechanism": "A11", "prior_family": "superseding", "prior_family_reason": "v2 trap 2: a sign-off withdrawn later in another place (a DM), tied to the same person and the same set",
     "nodes": ["T2", "C2"], "requirement": "R3", "natural_reading": "the twelve bathroom lines are Ready", "decides": ["State", "What's owed", "Who has it"],
     "controls": ["Armchair"], "over_application": "art_over", "source": "slack-dm", "signature": "Claire is redoing the UVs on the bathroom ones"},
    {"id": "REVISED", "mechanism": "A1", "prior_family": "stale_summary", "prior_family_reason": "v2 traps 2 and 4: the delivery column is true and stale; the art changed a day later in base Slack and GitHub",
     "nodes": ["T3", "C3"], "requirement": "R2", "natural_reading": "three lines are Delivered and two are Ready", "decides": ["State", "What's owed"],
     "controls": ["Grenade"], "over_application": "revised_over", "source": "github-and-art-channel", "signature": "match3d#462 changed cactus, cone, chainsaw, dartboard and candy on 25 Sep"},
    {"id": "AUDIO", "mechanism": "A13", "prior_family": "authority", "prior_family_reason": "v2 trap 5: a rule in the notes (only owned sound leaves) whose deciding fact sits in a sheet nothing links",
     "nodes": ["T4", "C5"], "requirement": "R2", "natural_reading": "all five exported cues are Ready", "decides": ["State", "What's owed", "Who has it"],
     "controls": ["Win stinger"], "over_application": "audio_over", "source": "gsheets-unlinked", "signature": "match scale and explosion come from a bought pack"},
    {"id": "PICKS", "mechanism": "A14", "prior_family": "superseding", "prior_family_reason": "v2 traps 2 and 7: Robert's later reply under an unrelated post changes one pick and adds six lines outside the list",
     "nodes": ["T5", "T6", "T15", "C4"], "requirement": "R4", "natural_reading": "the default eight include the iron and the list has 97 lines", "decides": ["Board set", "Line"],
     "controls": ["Grenade"], "over_application": "picks_over", "source": "slack-thread-reply", "signature": "bow instead of the iron; add soccer ball, basketball, toy drum, scooter, bicycle, toy hammer"},
    {"id": "PARENT", "mechanism": "A3", "prior_family": "tool_surface", "prior_family_reason": "a comment on the parent ticket is returned only by a comment read on that ticket; the children's own notes say done",
     "nodes": ["T7", "C6"], "requirement": "R3", "natural_reading": "the eight music lines are Ready", "decides": ["State", "What's owed", "Who has it"],
     "controls": ["Record Player"], "over_application": "parent_over", "source": "linear-parent-comment", "signature": "the music set from Friday's export comes in grey"},
]
def names(cls): return [l["name"] for l in M.members(cls)]
channels = [
    {"id": "CH-EXPORT", "kind": "member", "rule": "EXPORT", "degrade": "appliance and furniture lines Ready", "members": names("A1"), "latent": "#zombie-bugs read past the first page or searched for the object browser", "family": "done_gap"},
    {"id": "CH-ARTHOLD", "kind": "member", "rule": "ARTHOLD", "degrade": "bathroom lines Ready", "members": names("A2"), "latent": "Julia's DM with Claire read", "family": "superseding"},
    {"id": "CH-REVISED", "kind": "member", "rule": "REVISED", "degrade": "sent or exported before the 25 Sep change: Delivered or Ready", "members": names("C1"), "latent": "pull requests or #zombie-art checked for changes after 24 Sep", "family": "stale_summary"},
    {"id": "CH-AUDIO", "kind": "member", "rule": "AUDIO", "degrade": "bought-pack cues Ready", "members": names("C2"), "latent": "Calvin's source sheet opened", "family": "authority"},
    {"id": "CH-PICKS", "kind": "member", "rule": "PICKS", "degrade": "iron stays in the default eight; the six added lines missing", "members": ["Bow", "Iron"] + names("ADD"), "latent": "Robert's reply under the bow post opened", "family": "superseding"},
    {"id": "CH-PARENT", "kind": "member", "rule": "PARENT", "degrade": "music lines Ready", "members": names("C4"), "latent": "the pack ticket's own comments read", "family": "tool_surface"},
]
n_tix, n_owed = len(TICKETS), len(OWED_TICKETS)
call_budget = [
    {"phase": "discovery", "service": "slack", "calls": 9, "reason": "the ask in Frederick's DM; the PlayableX channel (two pages and its two long threads); the #zombie-design playable thread; Robert's picks and his answer on the zombies"},
    {"phase": "discovery", "service": "gdocs", "calls": 2, "reason": "Frederick's hand-off notes; Leonard's Playable Feedback (rejected: the first playable)"},
    {"phase": "discovery", "service": "gdrive", "calls": 3, "reason": "find the notes, the pack list and the deck shared with Julia; list her own root for the destination"},
    {"phase": "discovery", "service": "gsheets", "calls": 2, "reason": "Brian's pack list: sheet metadata and its rows"},
    {"phase": "discovery", "service": "gslides", "calls": 1, "reason": "Julia's reference-level deck (layout, win and fail)"},
    {"phase": "discovery", "service": "confluence", "calls": 2, "reason": "the design page and its comments (tray size, how a level is lost)"},
    {"phase": "discovery", "service": "gcal", "calls": 2, "reason": "find the kickoff hold and read its attendees"},
    {"phase": "discovery", "service": "contacts", "calls": 1, "reason": "PlayableX's intake address"},
    {"phase": "discovery", "service": "trello", "calls": 2, "reason": "the Playable Kickoff card and its comments (rejected as the recipient source)"},
    {"phase": "enumeration", "service": "linear", "calls": 3, "reason": "the pack ticket and two pages of its 97 children (keys, states, assignees)"},
    {"phase": "per-record", "service": "linear", "calls": n_tix, "reason": "each line's ticket comments: how and when it was exported, the art note, what is missing"},
    {"phase": "reconciliation", "service": "linear", "calls": 1, "reason": "the pack ticket's own comments (Brian's note on the music set)"},
    {"phase": "reconciliation", "service": "slack", "calls": 7, "reason": "#zombie-art since 23 Sep and Julia's bow thread; her DM with Claire; #zombie-bugs for the object browser; the sound channel"},
    {"phase": "reconciliation", "service": "github", "calls": 3, "reason": "pull requests on match3d after 24 Sep by the object artist; #462 and its file list"},
    {"phase": "reconciliation", "service": "gsheets", "calls": 2, "reason": "Calvin's sound source sheet: find it and read its rows"},
    {"phase": "reads-before-writes", "service": "linear", "calls": 3, "reason": "team, states and users for the ticket writes"},
    {"phase": "per-record", "service": "linear", "calls": 2 * n_owed, "reason": f"each of the {n_owed} Owed lines with a ticket: a state write (Done to Todo) and a comment saying what is owed and who has it"},
    {"phase": "writes", "service": "linear", "calls": 6, "reason": "a new ticket under the pack ticket for each of the six lines Robert added"},
    {"phase": "writes", "service": "gsheets", "calls": 2, "reason": "create the hand-off list in Julia's Drive and write its 103 rows"},
    {"phase": "writes", "service": "gdocs", "calls": 2, "reason": "create the brief and write its text"},
    {"phase": "writes", "service": "gdrive", "calls": 8, "reason": "share both files view-only with the three other people on the hold and PlayableX's intake address"},
    {"phase": "writes", "service": "slack", "calls": 2, "reason": "the three counts to Frederick in his DM; both links in the PlayableX channel"},
    {"phase": "read-back", "service": "gsheets", "calls": 1, "reason": "read the list back against the pack list's rows"},
    {"phase": "read-back", "service": "linear", "calls": 1, "reason": "list the pack ticket's children to confirm the Todo set and the six new tickets"},
]
writes = [
    {"service": "gsheets", "tool": "gsheets_create_spreadsheet+gsheets_values_update", "count": 2, "depends_on": ["K1", "K2", "C1", "C2", "C3", "C5", "C6", "T6"], "requirements": ["R1", "R2", "R3", "R7"]},
    {"service": "gdocs", "tool": "gdocs_create_document+gdocs_batch_update", "count": 2, "depends_on": ["K3", "K6", "K9", "K10", "K12", "K13", "K14", "C4"], "requirements": ["R4", "R5", "R7"]},
    {"service": "linear", "tool": "linear_create_comment", "count": n_owed, "depends_on": ["K1", "K5", "C1", "C2", "C3", "C5", "C6"], "requirements": ["R6"]},
    {"service": "linear", "tool": "linear_update_issue", "count": n_owed, "template": True, "depends_on": ["K1", "K5", "C1", "C2", "C3", "C5", "C6"], "requirements": ["R6"]},
    {"service": "linear", "tool": "linear_create_issue", "count": 6, "depends_on": ["K5", "K11", "T6"], "requirements": ["R1", "R6"]},
    {"service": "gdrive", "tool": "gdrive_share_file", "count": 8, "template": True, "depends_on": ["K7", "K8"], "requirements": ["R7"]},
    {"service": "slack", "tool": "slack_send_message", "count": 2, "depends_on": ["A1", "A2", "C1", "C2", "C3", "C5", "C6", "T6"], "requirements": ["R7"]},
]
manifest = {
    "_note": "draft manifest (/create-scenario, design D1); /create-injection writes 01_Hardness_Manifest.json keeping every id or listing it in design_delta. Seeded texts quoted in delegation_quote are the planned wording (plan/planned_texts.py).",
    "persona": M.PERSONA,
    "assignment_context": {"context_hash": ctx["context_hash"], "assignment_hash": ctx["assignment_hash"], "policy_hash": ctx["policy_hash"],
                           "freeze_utc": ctx["freeze_utc"], "difficulty_mode": ctx["difficulty_mode"]},
    "horizon": "Long Horizon", "effective_profile": "extreme",
    "author_targets": {"min_calls_per_run": 130, "max_avg_weighted_pass": 0.70, "target_avg_weighted_pass": 0.62, "requester_confirmation": CONFIRM},
    "volume_exception": {"reason": "the cohort is the 103 lines of one playable pack; honest necessary calls are about 250 (a lean correct run about 170): one comment read per line's ticket, two writes per Owed ticket, six new tickets, the two deliverables and two messages; reaching 500 would need invented lines or repeated reads, which fails on its own",
                         "requester_confirmation": CONFIRM + "; the per-record floor of 110 is the author's choice under that delegation",
                         "call_budget_floor": 220, "per_record_floor": 110},
    "requirements": requirements, "services": services, "anchors": anchors, "ask_fragments": ask_fragments, "authorities": authorities,
    "cohort": cohort, "chains": chains, "traps": traps, "mechanism_portfolio": mechanism_portfolio, "channels": channels,
    "call_budget": call_budget, "writes": writes, "hazard_acknowledgements": [], "denied_probes": [],
    "gradable_surface": "01_Gradable_Surface.json",
}
out = WF / "01_Hardness_Manifest.draft.json"
out.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")
tot = sum(r["calls"] for r in call_budget); per = sum(r["calls"] for r in call_budget if r["phase"] == "per-record")
print("manifest ->", out.name, "| budget", tot, "per-record", per, "| owed tickets", n_owed, "| fragments", len(ask_fragments), "traps", len(traps))
