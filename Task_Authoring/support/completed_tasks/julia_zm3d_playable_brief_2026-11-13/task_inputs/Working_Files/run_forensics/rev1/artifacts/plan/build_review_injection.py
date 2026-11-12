#!/usr/bin/env python3
"""Write the injection-stage review record: Working_Files/hardness_reviews/evidence_injection_rev1.md and injection.json
(design_readiness schema 1). Run last in the injection stage: the record binds the final manifest, the surface and the SQL by
digest and its evidence files by sha256. Judgements are the authoring session's; nothing here is a platform result."""
import hashlib, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
TOOLS = TASK.parent / "tools"
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(TOOLS))
import design_model as M
import planned_texts as TXT
from review_content import MECH
from design_readiness import input_hashes
import stage_evidence

REV = "rev1"
S, B = M.SEED, M.BASE
OUT = HERE / "out"
man = json.loads((WF / "01_Hardness_Manifest.json").read_text())
surf = json.loads((WF / "01_Gradable_Surface.json").read_text())
ctx = json.loads((WF / "00_Task_Context.json").read_text())
sql_path = TASK / "01_Universe_Inject.sql"
sql_text = sql_path.read_text()
slots = {s["id"]: s for s in surf["slots"]}
nat = json.loads((OUT / "natural_retrieval_injection.json").read_text())
check_sql = (OUT / "check_sql.txt").read_text()
exposure = (OUT / "path_exposure.txt").read_text()

def hits(mid, query):
    q = next(x for x in nat[mid]["queries"] if x["query"] == query)
    n = re.search(r"visible hits=(\d+)", q["base"])
    return int(n.group(1)) if n else None, q["injected"], q["returns_decider"]
def lb_line(rid):
    """The check-sql line that proves the persona reads the record (matched on the record's id or its Slack ts)."""
    key = rid.split("/")[-1]
    line = next((l for l in check_sql.splitlines() if key in l and l.startswith("[YES LB]")), None)
    assert line, f"no [YES LB] check-sql line for {rid}"
    return line.strip()
def off_path(unit):
    line = next((l for l in exposure.splitlines() if f"exposure.unit.{unit}:" in l), "")
    assert "OFF-PATH" in line, (unit, line)
    return line.strip()[:170]

fbx, _, _ = hits("EXPORT", "fbx"); binary, _, _ = hits("EXPORT", "binary"); exporter, _, ok_exp = hits("EXPORT", "exporter")
bath, _, _ = hits("ARTHOLD", "bathroom"); banyo, _, ok_banyo = hits("ARTHOLD", "banyo")
snd_base, snd_inj, ok_snd = hits("AUDIO", "sound")
dyn, dyn_inj, dyn_ok = hits("PICKS", "dynamite"); bow, bow_inj, bow_ok = hits("PICKS", "bow")
outg, outg_inj, ok_out = hits("ZIP", "outgoing"); zp, zp_inj, ok_zip = hits("ZIP", "zip")
assert ok_exp and ok_banyo and ok_snd and ok_out and ok_zip and not dyn_ok and not bow_ok

RETRIEVAL = {
 "EXPORT": dict(unit="A1", query="slack search: fbx · binary · exporter · saved out; slack_read_channel on #zombie-match3d, 25 to 30 Sep",
    returned=[S["a1_post"]["id"]],
    assessment=f"The vendor's own words do not return the post: 'fbx' gives {fbx} visible base messages and 'binary' {binary}, none of them it. 'exporter' returns it with {exporter} base messages, and a read of the channel for the week returns it as a top-level message. What comes back says the models saved out of Unity on Thursday are the text kind and that Claire's are fine; it names no line and no ticket. Which twelve lines those are (the tickets whose note says 'saved out of the project, Thu 25 Sep') and that the vendor refuses the format are still to be joined."),
 "ARTHOLD": dict(unit="A2", query="slack search: bathroom · banyo · uv; slack_read_channel on Julia's DM with Claire after 24 Sep",
    returned=[S["a2_dm"]["id"]],
    assessment=f"The English word does not return the message ('bathroom': {bath} visible base messages, none of them it). 'banyo' returns it with {banyo} base messages, and a read of the DM returns it as the newest message. It is in Turkish, names the game's category and 'the bathroom files I gave on Friday', and no line: which Bathroom lines were handed over on Friday (twelve of thirteen; the Rubber Ducky is not exported) comes from the tickets."),
 "AUDIO": dict(unit="C2", query="gdrive search: sound · sources; gsheets_values_get on the sheet",
    returned=snd_inj,
    assessment=f"A Drive search for 'sound' returns {len(snd_inj)} injected files (the sheet, the notes, the pack list and Brian's log) and {snd_base} visible base files. The sheet's title says what it holds; only reading its cells gives the two rows marked 'no'. It does not name tickets or states: that those two cues are Owed, with Calvin, follows from the notes' rule on sound, and the brief's sound section has to hold them back as well."),
 "PICKS": dict(unit="C3", query="slack search: dynamite · bow · in place of; slack_read_thread on Julia's bow post",
    returned=[S["c3_reply"]["id"]],
    assessment=f"Item names do not return the reply: 'dynamite' gives {dyn} visible base messages plus Robert's 25 Sep post, 'bow' {bow} base messages, neither the reply. It is returned by a thread read under Julia's own bow post, or by its own wording. It names no item: 'it' is the bow of the parent post and 'the last one on my list' is the last item of his 25 Sep post, so both records have to be read together."),
 "ZIP": dict(unit="C4", query="gdrive search: outgoing · zip; gdocs_get_document_text on the log",
    returned=outg_inj,
    assessment=f"A Drive search for 'outgoing' returns the log and the notes ({outg} base files); 'zip' returns the log and the pack list ({zp} visible base files). The ask and the notes do not name the log; the notes' Ready test and every ticket note name the outgoing folder. The log says the zip with Friday's music instruments will not unpack and that those eight are not in the folder any other way; it names no line. Which eight (the tickets whose note says 'zipped with the other instruments') comes from the tickets."),
}

# ---------------------------------------------------------------- evidence note
ev = [f"# Injection-stage hardness review evidence · {M.SLUG} · {REV} (design D2.2)\n",
      f"Authoring-session review of the six mechanisms on the injected universe: `01_Universe_Inject.sql` sha256 {hashlib.sha256(sql_path.read_bytes()).hexdigest()}. "
      "Readability is `persona_view.py check-sql` on that SQL (plan/out/check_sql.txt); natural retrieval is the rehearsal in plan/out/natural_retrieval_injection.txt "
      "(base as the persona, injected rows by their text) and `path_exposure.py` (plan/out/path_exposure.txt). No run, verdict or score is claimed here.\n"]
for mid, r in MECH.items():
    ev += [f"## {mid}\n", f"- First plausible answer: {r['first']}", f"- Deciding evidence (`{r['decider']}`): {r['decide']}", f"- Authority and chronology: {r['chrono']}",
           f"- Fair discovery path: {r['path']}", f"- Outcome change: before: {r['before']} · after: {r['after']}",
           f"- Outcome pair {r['pair'][0]} / {r['pair'][1]}: left passes, right fails when {r['left']}; right passes, left fails when {r['right']}."]
    if mid in RETRIEVAL:
        q = RETRIEVAL[mid]
        ev += [f"- Readable: `{lb_line(r['decider'])}`", f"- Natural retrieval ({q['query']}): {q['assessment']}", f"- Path exposure: `{off_path(q['unit'])}`\n"]
    else:
        ev += ["- Readable: base records; GitHub is unscoped and each Slack message is YES in plan/out/reach_table.md.",
               "- Natural retrieval: plan/out/natural_retrieval_revised.txt (unchanged base).", f"- Path exposure: `{off_path('C1')}`\n"]
ev += ["## Independence\n", "Each mechanism's deciding record is its own row in its own container (#zombie-match3d, Julia's DM with Claire, match3d#462, Calvin's sheet, "
       "the thread under Julia's bow post, Brian's log). None quotes or links another; each decides a disjoint set of lines (12, 12, 3, 2, the board set of two lines, 8).\n"]
rev_dir = WF / "hardness_reviews"; rev_dir.mkdir(exist_ok=True)
ev_path = rev_dir / f"evidence_injection_{REV}.md"
ev_path.write_text("\n".join(ev))

def ref(p):
    p = Path(p); return {"path": p.relative_to(TASK).as_posix(), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
EV = [ref(ev_path), ref(sql_path), ref(HERE / "planned_texts.py"), ref(HERE / "design_model.py")]
EV_READ = EV + [ref(OUT / "check_sql.txt")]
EV_NAT = EV + [ref(OUT / "natural_retrieval_injection.txt"), ref(OUT / "path_exposure.txt")]
EV_BASE = EV + [ref(OUT / "reach_table.md"), ref(OUT / "natural_retrieval_revised.txt"), ref(OUT / "path_exposure.txt")]
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
        "fair_discovery_path": item(r["path"], EV_BASE if mid == "REVISED" else EV_NAT),
        "changed_outcome": item("the solver's truth for the linked slots differs from the natural reading (solver/truth.json against the over-application and ch_miss operators; oracle_kit check PASS)", before=r["before"], after=r["after"]),
        "independent_operation": item("its deciding record is its own row in its own container and decides its own lines; no other rule's record quotes, links or depends on it",
                                      others_solvable_if_missed=[x for x in ids if x != mid]),
        "outcome_slots": linked,
        "channel_kind": "judgment",
        "outcome_pair": item(f"{r['pair'][0]} and {r['pair'][1]} are separate facts in separate deliverables", slots=list(r["pair"]),
                             left_pass_right_fail=r["left"], right_pass_left_fail=r["right"]),
    }
    if mid == "REVISED":
        row["access"] = item("base records: persona_view can-see YES for each scoped record (reach table); GitHub is unscoped", EV_BASE, status="verified")
        row["natural_retrieval"] = item("natural persona searches reviewed on the unchanged base", EV_BASE, query="slack: colorized · github: Objects Revisions",
                                        returned_ids=[B["art_cactus"], B["art_cone"], B["pr462"]],
                                        assessment="the Slack search returns the 24 Sep cactus and cone requests among eight hits, all in channels Julia reads; the GitHub search returns the pull request by title; neither result states which pack lines are affected, so the join to the pack list remains")
    else:
        q = RETRIEVAL[mid]
        row["access"] = item(f"persona_view.py check-sql on the SQL: {lb_line(r['decider'])}", EV_READ, status="verified")
        row["natural_retrieval"] = item("natural persona searches rehearsed on the base and on the injected rows; path_exposure reports the record OFF-PATH", EV_NAT,
                                        query=q["query"], returned_ids=q["returned"], assessment=q["assessment"])
    mechs[mid] = row

review = {
    "schema_version": 1, "stage": "injection", "task_id": stage_evidence.task_identity(TASK), "revision": REV,
    "reviewer": "claude-fable-5-2 (authoring session, /create-injection, design D2.2; two cold coherence reviewers read the ask and the injected records)",
    "difficulty_mode": ctx["difficulty_mode"].lower(), "diversity_channels": ids, "mechanisms": mechs, "dispositions": {},
    "input_hashes": input_hashes("injection", man, surf, sql_text=sql_text),
    "forecast": "UNCALIBRATED: design forecast and injection forecast ids in the Self-review of 01_Grounding_Dossier.md",
}
(rev_dir / "injection.json").write_text(json.dumps(review, indent=1, ensure_ascii=False) + "\n")
print("wrote", ev_path.name, "injection.json")
