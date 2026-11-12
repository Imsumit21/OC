#!/usr/bin/env python3
"""Write plan/sweep_settlements.json: what each coherence finding led to, and the base check of every seeded fact.

Hand-written judgements, kept as code so the ids stay tied to the model. plan/build_sweep.py merges this file into
Working_Files/01d_Coherence_Sweep.json. Base counts come from plan/out/sweep_candidates_base.json (the tool's literal
searches, 156 queries over 13 services) and plan/out/sweep_base_topics.json (topic searches through tools/hg.py)."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import design_model as M
S, B = M.SEED, M.BASE
def tk(n): return M.BY_NAME[n]["ticket"]
def note(n): return M.comment_id("note_" + n)
topics = json.loads((HERE / "out" / "sweep_base_topics.json").read_text())
def n(svc, term): return topics[svc][term]["count"]
NOTES, LOG, SHEET, LIST = S["notes"]["id"], S["c4_log"]["id"], S["c2_sheet"]["id"], S["tracker"]["id"]
ASK, PICKS, ZPICKS, REPLY, A1, A2 = (S[k]["id"] for k in ("ask", "picks", "zpicks", "c3_reply", "a1_post", "a2_dm"))
HOLD, TRELLO, CONTACT = S["hold"]["id"], S["trello_note"]["id"], S["contact"]["id"]
REV = M.REV

# ---------------------------------------------------------------- base consistency: one entry per seeded fact of the manifest
base_consistency = {
 "files saved out of Unity are the text kind": dict(
    search="all services: 'the text kind' (0 hits); slack: 'ASCII'", result_count=n("slack", "ASCII"),
    disposition=f"the ten Slack hits are the vendor's format rule ({B['vendor_formats']}, {B['vendor_asset_list']}) and its copies in four DMs, a font-atlas note and two unrelated uses; none says how any file of the pack was exported. The seeded post agrees with the rule (binary only) and contradicts nothing"),
 "bathroom UVs being redone": dict(
    search="all services: 'redoing the UVs' (0 hits); slack: 'redoing the UV' (0), 'bathroom objects' (0), 'the UVs'", result_count=n("slack", "redoing the UV") + n("slack", "bathroom objects") + n("slack", "the UVs"),
    disposition="the 34 'the UVs' hits run from 2023 to May 2025 (art how-tos, weapon and tile UVs, colour shifting); none is about the bathroom objects and no message of September 2025 says their UVs are finished or untouched, so Robert's note is the only record of the redo and contradicts nothing (rev1's searches for the Turkish wording are retired with that message)"),
 "Friday's bathroom files are the old version": dict(
    search="slack and gmail: \"Friday's\"; slack: 'old version'", result_count=n("slack", "Friday's") + n("gmail", "Friday's") + n("slack", "old version"),
    disposition="ten Slack messages of 2023 to March 2025 and two newsletter mails for \"Friday's\"; 76 'old version' hits from 2023 to September 2025 (builds, slides, funnel views), the two of September dated 2 and 19 Sep, before the files of Fri 26 Sep existed. None is about Claire's files or the playable"),
 "three recoloured items sent again": dict(
    search="all services: 'Claire sent the three recoloured models again' (0 hits); slack: 'colored version', 'recolo', 'sent again'; gdocs: 'recolo' (0)",
    result_count=n("slack", "colored version") + n("slack", "recolo") + n("slack", "sent again") + n("gdocs", "recolo"),
    conflicts=[{"id": B["robert_new_colours"], "disposition": "Robert's post of 29 Sep 23:44 UTC ('new colored version of cactus, chainsaw and cones') is the one base record of the new colour versions and names the three; the log's re-send of 30 Sep follows it and agrees with it. Nothing in base says the new versions were or were not sent"}],
    disposition="the other hits are a July build note (pull request #295), an unrelated Spanish DM and a 2023 'Sent again'; none speaks of these three files"),
 "re-sent items open and look right": dict(
    search="all services: \"they replace Thursday's\" (0 hits); gdocs: 'look right' (0)", result_count=n("gdocs", "look right"),
    disposition="no base record speaks of the three files after Robert's post; the check is Brian's own, in the words of his notes ('Opens, looks right'), and nothing contradicts it"),
 "bow replaces the last pick": dict(
    search=f"all services: 'in place of the last one on my list' (0 hits); the base thread under {B['art_bow_root']}", result_count=2,
    conflicts=[{"id": B["art_bow_claire"], "disposition": f"Claire's 'Of course' to Julia's question about an arrow (26 Sep 16:28 UTC) could be read as a change to the bow. Robert's reply in the same thread ({REPLY}) keeps the bow as it is and makes the arrow its own item, and the bow's file in the outgoing folder is of Mon 29 Sep ({tk('Bow')}), after the thread"}]),
 "instruments' zip will not unpack": dict(
    search="all services: \"won't unpack\" (0 hits); slack: 'unzip'", result_count=n("slack", "unzip"),
    disposition="seven messages of 2023 to August 2025 about other archives; base holds no statement about a zip of the playable's instruments, so Brian's log is the only record of it"),
 "rocket sound source": dict(
    search="all services: \"Soundly library (Robert's seat)\" (0 hits); gsheets: 'Soundly'", result_count=n("gsheets", "Soundly"),
    disposition="seven cells in budget sheets ('Sound (Pond5, Soundly,Elevenlabs)', 'Soundly Pro Monthly'); Slack has Robert's Soundly subscription (C05UQKDLGAU/1724968883.174899). Base agrees that the studio uses a Soundly seat and says nothing on where the rocket sound came from"),
 "explosion sound source": dict(
    search="slack: 'Universal Sound'", result_count=n("slack", "Universal Sound"),
    disposition="one message with a Unity Asset Store link to the Universal Sound FX pack (C07JYF2CFFU/1737054449.137119, three matched fields); consistent with a bought pack"),
 "the eight of 25 Sep": dict(
    search="slack: '8-item' (1 hit), 'Cute Axe'", result_count=1 + n("slack", "Cute Axe"),
    disposition=f"the vendor's own 8-item request ({B['vendor_formats']}) and nine item mentions in level and art chat; no base message picks the playable's board beyond the reference level's three ({B['julia_level']}), which Robert's post keeps"),
 "the four zombies": dict(
    search="slack: 'PartyGirl', 'Footballplayer', 'Party Girl'", result_count=n("slack", "PartyGirl") + n("slack", "Footballplayer") + n("slack", "Party Girl"),
    conflicts=[{"id": B["gdd"], "disposition": f"the design page's roster does not list Party Girl, Plumber or Football Player and puts Magician under 'in development' (card SC-58: the roster is not cited or graded). Base Slack has all four in the pack Brian asked Marcus for ({B['anim_zombies']}), and Robert's post now says all four are in the pack Marcus sent"}]),
 "saved out of the project (twelve notes)": dict(search="all services: 'FBX saved out of the project, Thu 25 Sep'", result_count=0),
 "zipped with the other instruments (eight notes)": dict(search="all services: 'Zipped with the other instruments'", result_count=0),
 "handed over first thing on 25 Sep (three notes)": dict(search="all services: 'FBX from Claire, Thu 25 Sep, first thing'", result_count=0),
 "PlayableX intake address": dict(
    search="all services: 'intake@playablex.ai' (0 hits); contacts: 'playablex', 'intake' (0 hits); slack: 'intake'", result_count=n("slack", "intake"),
    disposition="thirteen unrelated Slack hits (food, an ad network's form); base holds no e-mail address for the vendor in Contacts, Slack or mail, so the seeded contact duplicates and contradicts nothing"),
 "kickoff hold": dict(
    search="all services: 'ZM3D playable kickoff with PlayableX' (0 hits); gcal: '2025-11-03', 'PlayableX', 'playable' (0 hits); trello: 'kickoff'", result_count=n("trello", "kickoff"),
    disposition=f"the five Trello hits are Leonard's card {B['trello_kickoff']} and its actions; it has no attendees and no date. The calendar has more than forty events titled '... Kickoff' (art and feature kickoffs) and none on 3 Nov 2025 or naming the playable or the vendor. The date agrees with the vendor's message {B['vendor_nov3']}"),
 "pack ticket rule": dict(
    search="linear: 'playable', 'PlayableX'", result_count=n("linear", "playable") + n("linear", "PlayableX"),
    disposition="fifteen older tickets with 'playable' or 'unplayable' in the text (2023 to 2025), none about the playable ad or its assets; no base ticket tracks the pack, so the rule on closing a line's ticket conflicts with nothing"),
}
for v in base_consistency.values():
    v.setdefault("conflicts", [])
    v.setdefault("disposition", "no base hit")

out = {"base_consistency": base_consistency}
extra = HERE / "sweep_findings_map.json"       # forks, defects, open sets and dismissals keyed to the reviewers' current finding ids
if extra.is_file():
    out.update(json.loads(extra.read_text()))
(HERE / "sweep_settlements.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print("wrote sweep_settlements.json:", len(base_consistency), "facts;", {k: len(v) for k, v in out.items() if k != "base_consistency"})
