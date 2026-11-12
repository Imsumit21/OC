#!/usr/bin/env python3
"""Write the scenario-stage review records: Working_Files/hardness_reviews/evidence_rev1.md and scenario.json
(design_readiness schema 1), plus 00_Readiness_Config.json. Run after the manifest and the surface are final;
the record binds their digests. Judgements are the authoring session's; nothing here is a platform result."""
import hashlib, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
TOOLS = TASK.parent / "tools"
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(TOOLS))
import design_model as M
import planned_texts as TXT
from design_readiness import input_hashes
import stage_evidence

REV = "rev1"
S, B = M.SEED, M.BASE
man = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())
surf = json.loads((WF / "01_Gradable_Surface.json").read_text())
ctx = json.loads((WF / "00_Task_Context.json").read_text())
slots = {s["id"]: s for s in surf["slots"]}
def tick(n): return M.BY_NAME[n]["ticket"]
def names(cls): return ", ".join(l["name"] for l in M.members(cls))

(WF / "00_Readiness_Config.json").write_text(json.dumps({"schema_version": 1, "revision": REV, "injection": "required"}) + "\n")

# ---------------------------------------------------------------- per-mechanism review content
MECH = {
 "EXPORT": dict(
    decider=S["a1_post"]["id"], pair=("X1", "W4"),
    first=f"The twelve 'Appliances and furniture' lines ({names('A1')}) read as Ready: each line ticket ({tick('Washing Machine')} to {tick('Square Table')}) is Done and Brian's note on it says the model file was exported from the object browser, all twelve in one go, 25 Sep, and is in the outgoing folder; the pack list {S['tracker']['id']} lists them with no delivery.",
    decide=f"Arthur Blake's root post in #zombie-bugs ({S['a1_post']['id']}, 2025-09-27 09:05 UTC) says the object browser's multi-select export writes empty shells and a single export is fine. Joined to 'all twelve in one go' on the tickets, the twelve files do not open, so by the notes' Ready test ('it opens') they are Owed: re-export one at a time, Brian.",
    chrono="Brian's ticket notes are of 25 Sep and report what he did; Arthur wrote the export button, posts two days later and reports what the tool does. The notes make 'it opens' part of Ready, so the later statement by the tool's author decides. Nothing after 27 Sep says the files were re-exported.",
    path="Julia is a member of #zombie-bugs (base channel C08R27X0EAH, reach table YES for the channel). The post is a top-level message, so slack_read_channel over the last week or a search for the export or the object browser returns it. It names no object, no ticket and no word of the ask, so a search on the task's nouns does not.",
    before="Washing Machine: Ready; its ticket stays Done", after="Washing Machine: Owed (re-export one at a time, Brian); its ticket back to Todo with a comment",
    left="the list marks Washing Machine Owed but the run skips the ticket follow-through, so the ticket stays Done", right="the run moves the ticket to Todo from a per-ticket pass after the sheet was written and leaves the sheet row Ready",
    kind="done-claim against the tool author's later report (v2 trap 1)", access="deferred", retrieval="deferred"),
 "ARTHOLD": dict(
    decider=S["a2_dm"]["id"], pair=("X2", "W5"),
    first=f"The twelve 'Bathroom' lines ({names('A2')}) read as Ready: on each ticket Claire's 24 Sep note says the art is fine to go and Brian's 25 Sep note says it was exported on its own as .fbx.",
    decide=f"Claire Morgan's DM to Julia ({S['a2_dm']['id']}, 2025-09-26 08:10 UTC) says she is redoing the UVs on the bathroom ones and that what Brian pulled on Thursday is the old unwrap. The notes' Ready test ('nobody is changing it', 'the current version') makes the twelve Owed: art, Claire.",
    chrono="Same person, later: Claire's ticket notes are of 24 Sep, her DM of 26 Sep withdraws them for one set. Brian's export of 25 Sep (a Thursday) predates the DM. No later record says the UVs are finished.",
    path="The DM is Julia's own conversation with Claire (D05HMBQUC8Z, reach table YES). It is a top-level message; reading the DM's recent history returns it. It names the set ('the bathroom ones'), not the lines; the pack list's set column maps the set to twelve lines.",
    before="Bathtub: Ready; who has it: nobody", after="Bathtub: Owed (art being redone), Claire Morgan; its ticket back to Todo with a comment",
    left="the list marks Bathtub Owed with Claire and the ticket is not moved", right="the ticket is moved because the run comments every Bathroom ticket after reading the DM, while the sheet row was filled earlier from the ticket notes",
    kind="a correction by the same person in another service (v2 trap 2)", access="deferred", retrieval="deferred"),
 "REVISED": dict(
    decider=B["pr462"], pair=("X3", "W6"),
    first=f"Cactus Plant, Chainsaw and Traffic Cone read as Delivered (in the zip of 24 Sep, {B['brian_zip1']}); Dartboard and Candy read as Ready (exported on their own on the morning of 25 Sep).",
    decide=f"Base: Robert asks for colour versions and fixes on 24 Sep in #zombie-art ({B['art_cactus']}, {B['art_candy']}, {B['art_cone']}, {B['art_dart']}); Claire pushes them in a new pull request on 25 Sep ({B['art_claire_pr']}); {B['pr462']} 'Objects Revisions and Changes' is created 2025-09-25 11:43 UTC and merged 23:15 UTC; Robert confirms the new coloured objects on 29 Sep ({B['robert_new_colours']}). The notes: 'If the art changed after a file went out (a fix, a retexture, new colour versions), it goes again'. The five are Owed: send the current version.",
    chrono="The zip went out on 24 Sep 12:39 UTC and the two single exports are of the morning of 25 Sep; the art change merged at 23:15 UTC on 25 Sep. The later state of the art decides, by the notes' current-version rule.",
    path="All base. Julia is a member of #zombie-art (reach table YES for each of the five messages); GitHub is unscoped. A natural search for 'colorized' in Slack returns the cactus and cone requests, and a pull-request list after 24 Sep returns #462 (plan/out/natural_retrieval_revised.txt).",
    before="Cactus Plant: Delivered; its ticket stays Done", after="Cactus Plant: Owed (the art changed after it went out, send the current version), Brian; its ticket back to Todo with a comment",
    left="the list marks Cactus Plant Owed and the ticket is left Done", right="the ticket is moved and commented while the list keeps Delivered for a line PlayableX already holds",
    kind="dates across services (v2 trap 4)", access="verified", retrieval="verified"),
 "AUDIO": dict(
    decider=S["c2_sheet"]["id"], pair=("X5", "B6"),
    first="All five exported sound cues read as Ready: each sound ticket says 'Exported .wav', a type PlayableX takes.",
    decide=f"Calvin Price's sound source sheet ({S['c2_sheet']['id']}, 2025-09-26) marks Match scale and Explosion as cut from a bought pack with an in-game licence only; the notes say 'Sound: only what we own outright leaves the studio'. The two are Owed: a cue we own, Calvin. The brief's sound section leaves them out.",
    chrono="The rule is Frederick's (the notes, the authority for what leaves); the source column is Calvin's, who handles sound. The tickets only state the file type and are silent on ownership, so nothing contradicts the sheet.",
    path="The sheet is shared with Julia (planned sharing; proven on the SQL at injection). A Drive search for sound or a look at Calvin's files returns it; its rows are in the grid, which gsheets_values_get returns.",
    before="Match scale: Ready; the brief lists it among the cues PlayableX can use", after="Match scale: Owed (not ours outright), Calvin Price; the brief's sound section names it as held back",
    left="the list marks Match scale Owed and the brief's sound section is written from the ticket list without the two held-back cues named", right="the brief names the two cues as held back after the sheet is read while the list row written earlier keeps Ready",
    kind="a rule in the data applied to a second carrier (v2 trap 5)", access="deferred", retrieval="deferred"),
 "PICKS": dict(
    decider=S["c3_reply"]["id"], pair=("X13", "W10"),
    first=f"The default eight are Robert's 23 Sep picks ({S['picks']['id']}) with the iron, as Julia's deck also shows; the list has the 97 lines of Brian's pack list.",
    decide=f"Robert's reply under Julia's bow post in #zombie-art ({S['c3_reply']['id']}, 2025-09-26 17:05 UTC, parent {B['art_bow_root']}) puts the bow in place of the iron and names six round objects missing from Brian's list. The ask keeps his latest word ('unless he's changed them since') and the notes add his objects ('If Robert has added objects since Brian made the list, they go on it too').",
    chrono="Same person, three days later. No later record re-lists the eight or re-asserts the iron; the deck (23 Sep) is the older version.",
    path="The parent is Julia's own post in a channel she is a member of (reach table YES for the root). slack_read_thread on it, or a search for the iron or the bow, returns the reply.",
    before="Bow: Extra; Iron: Default; 97 lines; no new ticket", after="Bow: Default; Iron: Extra; 103 lines; a new ticket under ART-793 for each of the six added lines",
    left="the list has Bow as Default but the six added lines get no ticket", right="the run opens the six tickets from the reply and leaves the board-set column as the 23 Sep picks",
    kind="a later reply under an unrelated parent, plus lines outside the list (v2 traps 2 and 7)", access="deferred", retrieval="deferred"),
 "PARENT": dict(
    decider=S["c4_comment"]["id"], pair=("X4", "W7"),
    first=f"The eight 'Music' lines ({names('C4')}) read as Ready: each ticket is Done and Brian's note says exported as .glb, Fri 26 Sep.",
    decide=f"Brian Foster's comment on the pack ticket ART-793 ({S['c4_comment']['id']}, 2025-09-29 08:40 UTC) says the music set from Friday's export comes in grey in an empty scene and needs another pass. By 'it opens' and 'the current version' the eight are Owed: another export pass, Brian.",
    chrono="Brian's own later statement about his own export; the child notes are of 26 Sep, the parent comment of 29 Sep. Nothing later says the pass was done.",
    path="Linear is unscoped for Julia. linear_list_comments on ART-793 returns the comment; linear_get_issue on the parent or the children does not. The comment names the set, which the pack list maps to eight lines.",
    before="Cello: Ready; its ticket stays Done", after="Cello: Owed (the export comes in without textures), Brian; its ticket back to Todo with a comment",
    left="the list marks Cello Owed and the ticket is not moved", right="the ticket is moved in the follow-through pass while the list row keeps Ready",
    kind="a note on the parent record that the child read does not return (tool surface)", access="deferred", retrieval="deferred"),
}

# ---------------------------------------------------------------- evidence note
ev = [f"# Scenario-stage hardness review evidence · {M.SLUG} · {REV} (design D1)\n",
      "Authoring-session review of the six selected mechanisms against the draft manifest, the gradable surface and the planned record texts. "
      "Planned records are not SQL yet: their readability and natural retrieval are deferred to `/create-injection` (`persona_view.py check-sql`, the cold-solver rehearsal). "
      "Base records were read through `tools/hg.py` and checked with `persona_view.py can-see` (Working_Files/plan/out/reach_table.md).\n",
      "## Planned hub texts (Working_Files/plan/planned_texts.py)\n", "Ask:\n\n> " + TXT.ASK + "\n", "Notes:\n\n> " + TXT.NOTES.replace("\n\n", "\n>\n> ").rstrip("> \n") + "\n"]
for mid, r in MECH.items():
    ev += [f"## {mid}\n", f"- First plausible answer: {r['first']}", f"- Deciding evidence (`{r['decider']}`): {r['decide']}", f"- Authority and chronology: {r['chrono']}",
           f"- Fair discovery path: {r['path']}", f"- Outcome change: before: {r['before']} · after: {r['after']}",
           f"- Outcome pair {r['pair'][0]} / {r['pair'][1]}: left passes, right fails when {r['left']}; right passes, left fails when {r['right']}.",
           f"- Slots linked on the surface: {', '.join(s for s in slots if mid in slots[s].get('mechanisms', []))}", f"- Kind: {r['kind']}\n"]
ev += ["## Independence\n", "Each mechanism has its own deciding record in its own container: #zombie-bugs, Julia's DM with Claire, match3d#462 with #zombie-art, Calvin's sheet, "
       "the thread under Julia's bow post, the pack ticket's comments. None quotes or links another, and each decides a disjoint set of lines "
       "(12, 12, 5, 2, the board set with 6 added lines, 8). Missing one leaves every other solvable.\n",
       "## Natural retrieval on base (REVISED)\n", "```\n" + (HERE / "out/natural_retrieval_revised.txt").read_text().rstrip() + "\n```\n"]
rev_dir = WF / "hardness_reviews"; rev_dir.mkdir(exist_ok=True)
ev_path = rev_dir / f"evidence_{REV}.md"
ev_path.write_text("\n".join(ev))

def ref(p):
    p = Path(p); return {"path": p.relative_to(TASK).as_posix(), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
EV = [ref(ev_path), ref(HERE / "planned_texts.py"), ref(HERE / "design_model.py")]
EV_BASE = EV + [ref(HERE / "out/reach_table.md"), ref(HERE / "out/natural_retrieval_revised.txt")]
def item(reason, evidence=None, **kw):
    d = {"reason": reason, "evidence": evidence or EV}; d.update(kw); return d

ids = list(MECH)
assert set(ids) == {m["id"] for m in man["mechanism_portfolio"]}, "review must cover exactly the manifest's mechanisms"
mechs = {}
for mid, r in MECH.items():
    linked = [s for s in slots if mid in slots[s].get("mechanisms", [])]
    assert set(r["pair"]) <= set(linked), (mid, r["pair"], linked)
    row = {
        "initial_plausible_answer": item(r["first"]),
        "deciding_evidence": item(r["decide"], record_id=r["decider"]),
        "authority_chronology": item(r["chrono"]),
        "fair_discovery_path": item(r["path"], EV_BASE if mid == "REVISED" else EV),
        "changed_outcome": item("the surface slots linked to this rule change value between the natural reading and the truth (design_model.py classes; gradable surface mechanisms)", before=r["before"], after=r["after"]),
        "independent_operation": item("its deciding record sits in its own container and decides its own lines; no other selected rule's record quotes, links or depends on it",
                                      others_solvable_if_missed=[x for x in ids if x != mid]),
        "outcome_slots": linked,
        "channel_kind": "judgment",
        "outcome_pair": item(f"{r['pair'][0]} and {r['pair'][1]} are separate facts in separate deliverables", slots=list(r["pair"]),
                             left_pass_right_fail=r["left"], right_pass_left_fail=r["right"]),
    }
    if r["access"] == "verified":
        row["access"] = item("base records: persona_view can-see YES for each scoped record (reach table); GitHub is unscoped", EV_BASE, status="verified")
        row["natural_retrieval"] = item("natural persona searches reviewed", EV_BASE, query="slack: colorized · github: Objects Revisions",
                                        returned_ids=[B["art_cactus"], B["art_cone"], B["pr462"]],
                                        assessment="the Slack search returns the 24 Sep cactus and cone requests among eight hits, all in channels Julia reads; the GitHub search returns the pull request by title; neither result states which pack lines are affected, so the join to the pack list remains")
    else:
        row["access"] = {"status": "deferred", "required_at": "injection", "reason": "planned record: readability is proven on the SQL with persona_view.py check-sql"}
        row["natural_retrieval"] = {"status": "deferred", "required_at": "injection", "reason": "planned record: the natural query and its result are reviewed on the SQL (cold-solver rehearsal, path_exposure.py)"}
    mechs[mid] = row

review = {
    "schema_version": 1, "stage": "scenario", "task_id": stage_evidence.task_identity(TASK), "revision": REV,
    "reviewer": "claude-fable-5-2 (authoring session, /create-scenario, design D1); two cold reviewer passes recorded in 01b_Redteam_Review.md and .second.md",
    "difficulty_mode": ctx["difficulty_mode"].lower(), "diversity_channels": ids, "mechanisms": mechs, "dispositions": {},
    "input_hashes": input_hashes("scenario", man, surf),
    "forecast": "UNCALIBRATED design forecast: see section 12 of 01_Scenario_Design.md",
}
(rev_dir / "scenario.json").write_text(json.dumps(review, indent=1, ensure_ascii=False) + "\n")
print("wrote", ev_path.name, "scenario.json", "00_Readiness_Config.json")
