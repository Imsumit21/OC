#!/usr/bin/env python3
"""Per-mechanism review content shared by the scenario and the injection review records (plan/build_review.py,
plan/build_review_injection.py). Judgements are the authoring session's; nothing here is a platform result."""
import design_model as M
S, B = M.SEED, M.BASE
def tick(n): return M.BY_NAME[n]["ticket"]
def names(cls): return ", ".join(l["name"] for l in M.members(cls))

# ---------------------------------------------------------------- per-mechanism review content
PT = M.PACK_TICKET
MECH = {
 "EXPORT": dict(
    decider=S["a1_post"]["id"], pair=("X1", "W4"),
    first=f"The twelve lines Brian saved out of the project on Thu 25 Sep ({names('A1')}) read as Ready: each ticket ({tick('Retro TV')}, {tick('Refrigerator')} and ten more) says FBX saved out of the project, opens, looks right, in the outgoing folder.",
    decide=f"Marcus Bennett's root post in #zombie-match3d ({S['a1_post']['id']}, 2025-09-26 17:08 UTC) says the models Brian saved out of Unity on Thursday are the text kind, the exporter's default, which open fine in Unity and Max; Claire's files are fine. The vendor takes .fbx in binary format only ({B['vendor_formats']}, {B['vendor_asset_list']}; Frederick relayed it to Julia in {B['fred_asks_julia']}). By the notes' Ready test ('exported in a format they take') the twelve are Owed: export again as binary, Brian.",
    chrono="Brian's ticket notes are of 25 Sep and say the file opens, which is true in Unity. Marcus built and tested the zombie pack on 26 Sep (base) and posts a quarter of an hour after handing it over. The notes say a later word from someone who knows the file counts over the ticket. Nothing after 26 Sep says the files were exported again.",
    path="Julia is a member of #zombie-match3d and posted there six times that week (reach table YES). The post is a top-level message. The vendor's binary-only rule is on the hub path twice and in Julia's own DM with Frederick, and the twelve tickets say 'saved out of the project' while the others say 'FBX from Claire', so asking what kind of file the project writes is the natural check. The post holds no line name, no ticket key and none of the ask's words.",
    before="Refrigerator: Ready; its ticket stays In Progress", after="Refrigerator: Owed (ASCII file, export again as binary), Brian; its ticket to Todo with a comment",
    left="the list marks Refrigerator Owed but the run skips the ticket follow-through, so the ticket stays In Progress", right="the run moves the ticket to Todo in a follow-through pass and leaves the sheet row, written earlier from the ticket note, at Ready",
    kind="done-claim against a later check by a colleague, joined to the vendor's format rule (v2 trap 1)", access="deferred"),
 "ARTHOLD": dict(
    decider=S["a2_dm"]["id"], pair=("X2", "X11"),
    first=f"The twelve exported Bathroom lines ({names('A2')}) read as Ready: each ticket says FBX from Claire, Fri 26 Sep, opens, looks right.",
    decide=f"Claire Morgan's message to Julia in their DM ({S['a2_dm']['id']}, 2025-09-29 12:15 UTC, in Turkish) says she is redoing the UVs of the bathroom objects and that the bathroom files she gave on Friday are the old state. The notes' Ready test ('the current version and nobody is changing it') makes the twelve Owed: the art, Claire.",
    chrono="Brian's notes are of 26 Sep; Claire, who made the files, writes three days later and says she will note the tickets when she is done. No later record says the UVs are finished.",
    path="The DM is Julia's own conversation with Claire (reach table YES), who keeps her posted on object sets for her levels in base. It is a top-level message. It names the game's category, which is a column of the pack list, and no line.",
    before="Bathtub: Ready; who has it: nobody", after="Bathtub: Owed (art being redone), Claire; its ticket to Todo with a comment",
    left="the list marks Bathtub Owed and leaves 'who has it' empty or names Brian", right="the run notes Claire against the bathroom lines from her message while the State cells, filled earlier from the ticket notes, stay Ready",
    kind="a later statement by the artist in another service and language (v2 trap 2)", access="deferred"),
 "REVISED": dict(
    decider=B["pr462"], pair=("X3", "K3"),
    first=f"Cactus Plant, Chainsaw and Cone read as Ready: each ticket's note, written 25 Sep 08:05 UTC, says FBX from Claire first thing, opens, looks right.",
    decide=f"Base: Robert asks for colour versions on 24 Sep in #zombie-art ({B['art_cactus']}, {B['art_cone']}); Claire pushes the changes in a new pull request on 25 Sep ({B['art_claire_pr']}); {B['pr462']} 'Objects Revisions and Changes' is created 2025-09-25 11:43 UTC and merged 23:15 UTC, and its comment ({B['pr462_comment']}) names the chainsaw, cactus and cone models; Robert shows the new coloured versions on 29 Sep ({B['robert_new_colours']}). The notes: 'If the art changed after a file went out or was exported (a fix, a retexture, new colour versions), it goes again'. The three are Owed.",
    chrono="The ticket notes are stamped 08:05 UTC on 25 Sep; the pull request was created at 11:43 UTC and merged at 23:15 UTC the same day. The later state of the art decides, by the notes' rule.",
    path="All base. Julia is a member of #zombie-art (reach table YES for each message) and Robert's 29 Sep post is addressed to her; GitHub is unscoped. A Slack search for 'colorized' returns the cactus and cone requests, and the pull request list after 24 Sep returns #462 (plan/out/natural_retrieval_revised.txt).",
    before="Cactus Plant: Ready; its ticket stays In Progress", after="Cactus Plant: Owed (the model changed after the file was handed over), the current file from Claire; its ticket to Todo with a comment",
    left="the list marks Cactus Plant Owed and no ticket comment says why", right="a ticket comment mentions the new colour versions while the list keeps Ready for a file that opens",
    kind="dates across services (v2 trap 4)", access="verified"),
 "AUDIO": dict(
    decider=S["c2_sheet"]["id"], pair=("X5", "B6"),
    first="All five exported sound cues read as Ready: each sound ticket says exported .wav from the project, plays.",
    decide=f"Calvin Price's sound sources sheet ({S['c2_sheet']['id']}) lists the rocket sound as from a library seat and the explosion sound as from a bought pack, both 'no' under 'OK outside the game', with 'not made yet, Calvin' under 'Replacement'. The notes: 'we only hand over what is ours to hand over. Anything from a library or a bought pack stays here until we have our own version'. The two are Owed: our own version, Calvin. The brief's sound section holds them back.",
    chrono="The rule is Frederick's (the notes); the source column is Calvin's, who made or collected the cues. The tickets state the file type only, so nothing contradicts the sheet. Base agrees on the general picture: Robert uses a Soundly subscription and bought packs, and two sounds were already to be swapped for copyright.",
    path="The sheet is shared with Julia (planned sharing; proven on the SQL at injection). A Drive search for sound, or a look at Calvin's files, returns it; its rows are grid cells, which gsheets_values_get returns.",
    before="Rocket sound: Ready; the brief lists it among the cues PlayableX can use", after="Rocket sound: Owed (not ours to pass on), Calvin; the brief's sound section names it as held back",
    left="the list marks Rocket sound Owed and the brief's sound section is written from the ticket list without the two cues held back", right="the brief holds the two cues back after the sheet is read while the list row written earlier keeps Ready",
    kind="a rule in the data applied to a second carrier (v2 trap 5)", access="deferred"),
 "PICKS": dict(
    decider=S["c3_reply"]["id"], pair=("X13", "B1"),
    first=f"The eight are Robert's 25 Sep post ({S['picks']['id']}), with the dynamite as the last of them.",
    decide=f"Robert's reply under Julia's bow post in #zombie-art ({S['c3_reply']['id']}, 2025-09-26 21:41 UTC, parent {B['art_bow_root']}) puts it, the bow of the parent post, in the eight in place of the last item on his list, as it is now. The last item of his 25 Sep list is the dynamite. The ask keeps his latest word ('unless he's changed them since').",
    chrono="Same person, a day later. No later record re-lists the eight; Julia's deck (23 Sep) is the reference level, older than both.",
    path="The parent is Julia's own post in a channel she is a member of (reach table YES for the root). slack_read_thread on it returns the reply. The reply names no item, so a keyword search on an item name does not return it; the bow comes from the parent and the dynamite from the order of Robert's own list.",
    before="Bow: Extra; Dynamite: Default; the brief lists the dynamite among the eight", after="Bow: Default; Dynamite: Extra; the brief lists the bow among the eight",
    left="the list has Bow as Default while the brief, written from the 25 Sep post, still lists the dynamite", right="the brief lists the bow among the eight while the list's Board set column was filled from the 25 Sep post",
    kind="a later reply under an unrelated parent (v2 trap 2)", access="deferred"),
 "ZIP": dict(
    decider=S["c4_log"]["id"], pair=("X4", "K4"),
    first=f"The eight instruments in Friday's zip ({names('C4')}) read as Ready: each ticket says FBX from Claire, Fri 26 Sep, opens, looks right, zipped with the other instruments, in the outgoing folder.",
    decide=f"Brian Foster's own log of the outgoing folder ({S['c4_log']['id']}, a Google Doc, last edited 2025-09-30 09:12 UTC) says the zip with Friday's music instruments got cut off on upload and will not unpack, that the eight are not in the folder any other way, and that he will put Claire's files back. By the notes' Ready test ('sitting in the outgoing folder, it opens') the eight are Owed: put the files back, Brian.",
    chrono="Brian's own later statement about his own zip; the ticket notes are of 26 Sep, the log line of 30 Sep. Nothing later says it was redone.",
    path="The log is shared with Julia (planned sharing; proven on the SQL). The notes make 'sitting in the outgoing folder' part of Ready and every ticket note ends with that folder, so looking for the folder in Drive is the natural check; a search for it returns the log. Its title and text hold none of the ask's nouns and no line name.",
    before="Cello: Ready; its ticket stays In Progress", after="Cello: Owed (its zip will not unpack), Brian; its ticket to Todo with a comment",
    left="the list marks Cello Owed and no ticket comment says the zip has to be redone", right="a ticket comment says the zip has to be redone while the list row keeps Ready",
    kind="a second record by the list's owner that contradicts his ticket notes (completion elsewhere)", access="deferred"),
}
for _r in MECH.values(): _r["retrieval"] = _r["access"]
