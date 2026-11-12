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

REV = M.REV
S, B = M.SEED, M.BASE
man = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())
surf = json.loads((WF / "01_Gradable_Surface.json").read_text())
ctx = json.loads((WF / "00_Task_Context.json").read_text())
slots = {s["id"]: s for s in surf["slots"]}
def tick(n): return M.BY_NAME[n]["ticket"]
def names(cls): return ", ".join(l["name"] for l in M.members(cls))

(WF / "00_Readiness_Config.json").write_text(json.dumps({"schema_version": 1, "revision": REV, "injection": "required"}) + "\n")

from review_content import MECH, PT

# ---------------------------------------------------------------- evidence note
ev = [f"# Scenario-stage hardness review evidence · {M.SLUG} · {REV} (design " + M.DESIGN + ")\n",
      "Authoring-session review of the six selected mechanisms against the draft manifest, the gradable surface and the planned record texts. "
      "Planned records are not SQL yet: their readability and natural retrieval are deferred to `/create-injection` (`persona_view.py check-sql`, the cold-solver rehearsal). "
      "Base records were read through `tools/hg.py` and checked with `persona_view.py can-see` (Working_Files/plan/out/reach_table.md).\n",
      "## Planned hub texts (Working_Files/plan/planned_texts.py)\n", "Ask:\n\n> " + TXT.ASK + "\n", "Notes:\n\n> " + TXT.NOTES.replace("\n\n", "\n>\n> ").rstrip("> \n") + "\n"]
for mid, r in MECH.items():
    ev += [f"## {mid}\n", f"- First plausible answer: {r['first']}", f"- Deciding evidence (`{r['decider']}`): {r['decide']}", f"- Authority and chronology: {r['chrono']}",
           f"- Fair discovery path: {r['path']}", f"- Outcome change: before: {r['before']} · after: {r['after']}",
           f"- Outcome pair {r['pair'][0]} / {r['pair'][1]}: left passes, right fails when {r['left']}; right passes, left fails when {r['right']}.",
           f"- Slots linked on the surface: {', '.join(s for s in slots if mid in slots[s].get('mechanisms', []))}", f"- Kind: {r['kind']}\n"]
ev += ["## Independence\n", "Five deciding records in five containers: #zombie-match3d (EXPORT), Julia's DM with Robert (ARTHOLD), Calvin's sheet (AUDIO), "
       "the thread under Julia's bow post (PICKS), and Brian's log of the outgoing folder, which decides two rules (ZIP: eight lines Owed; REVISED: three lines Ready). "
       "None quotes or links another, and the lines they decide are disjoint (12, 12, 2, the board set of two lines, 8 and 3). ZIP and REVISED are one carrier: "
       "a run that opens the log settles both, one that does not misses both; every other rule stays solvable without it.\n",
       "## Natural retrieval on base (REVISED's first-read record)\n", "```\n" + (HERE / "out/natural_retrieval_revised.txt").read_text().rstrip() + "\n```\n"]
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
        "fair_discovery_path": item(r["path"], EV),
        "changed_outcome": item("the surface slots linked to this rule change value between the natural reading and the truth (design_model.py classes; gradable surface mechanisms)", before=r["before"], after=r["after"]),
        "independent_operation": item("its deciding record decides its own lines and no other rule's record quotes, links or depends on it"
                                      + ("; it shares Brian's folder log with " + ("REVISED" if mid == "ZIP" else "ZIP") + " (one carrier, two rules), so missing the log misses both" if mid in ("ZIP", "REVISED") else ""),
                                      others_solvable_if_missed=[x for x in ids if x != mid and not ({x, mid} == {"ZIP", "REVISED"})]),
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
    "reviewer": "claude-opus-5-5 (authoring session, /create-scenario --revise, design D3 for rev2, after the MODE B forensics of rev1 in 01a_Hardening_Report.md; D2 was rebuilt after the two cold reviews in 01b_Redteam_Review.md and .second.md)",
    "difficulty_mode": ctx["difficulty_mode"].lower(), "diversity_channels": [x for x in ids if x != "REVISED"],   # D3: REVISED shares ZIP's deciding record (Brian's log), so it is one loss channel with ZIP
    "mechanisms": mechs, "dispositions": {},
    "input_hashes": input_hashes("scenario", man, surf),
    "forecast": "UNCALIBRATED design forecast: see section 12 of 01_Scenario_Design.md",
}
(rev_dir / "scenario.json").write_text(json.dumps(review, indent=1, ensure_ascii=False) + "\n")
print("wrote", ev_path.name, "scenario.json", "00_Readiness_Config.json")
