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

REV = M.REV
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

fbx, _, _ = hits("EXPORT", "fbx"); binary, _, _ = hits("EXPORT", "binary"); _, _, ok_saved = hits("EXPORT", "saved out"); _, _, ok_export = hits("EXPORT", "export")
_, _, ok_textkind = hits("EXPORT", "text kind")
bath, _, ok_bath = hits("ARTHOLD", "bathroom"); _, _, ok_claire = hits("ARTHOLD", "Claire")
snd_base, snd_inj, ok_snd = hits("AUDIO", "sound")
dyn, dyn_inj, dyn_ok = hits("PICKS", "dynamite"); bow, bow_inj, bow_ok = hits("PICKS", "bow")
outg, outg_inj, ok_out = hits("ZIP", "outgoing"); zp, zp_inj, ok_zip = hits("ZIP", "zip"); _, _, zip_by_sound = hits("ZIP", "sound")
_, rev_inj, ok_recol = hits("REVISED", "recoloured"); _, _, rev_by_chainsaw = hits("REVISED", "chainsaw")
assert ok_textkind and not ok_saved and not ok_export and ok_bath and not ok_claire and ok_snd and ok_out and ok_zip and not zip_by_sound
assert ok_recol and not rev_by_chainsaw and not dyn_ok and not bow_ok

RETRIEVAL = {
 "EXPORT": dict(unit="C1", query="slack search: fbx · binary · saved out · export · text kind; slack_read_channel on #zombie-match3d, 25 to 30 Sep",
    returned=[S["a1_post"]["id"]],
    assessment=f"Neither the vendor's words nor the note's own words return the post: 'fbx' gives {fbx} visible base messages and 'binary' {binary}, none of them it; 'saved out' and 'export' do not return it (D3 took the note's wording out of it). Only its own phrase 'text kind', a search for Marcus's messages or a read of the channel for the week returns it, as a top-level message. It names no line and no ticket: which twelve lines (the notes that say 'saved out of the project, Thu 25 Sep') and that the vendor refuses the format are still to be joined."),
 "ARTHOLD": dict(unit="A2", query="slack search: bathroom · uv · Claire · texture; slack_read_channel on Julia's DM with Robert for 29 Sep",
    returned=[S["a2_dm"]["id"]],
    assessment=f"A search for Claire's name does not return the note: she is tagged, not named. 'bathroom' returns it among {bath} visible base messages, and 'uv' among many; no rev1 run searched either word (01a_Hardening_Report.md §8). A read of Julia's DM with Robert around 29 Sep returns it between his other messages of that day; a search for Robert's own messages with the usual limit does not reach back to it. It names the game's category and 'the bathroom files she gave' Brian on Friday, and no line: which Bathroom lines were handed over on Friday (twelve of thirteen; the Rubber Ducky is not exported) comes from the tickets, and the holder from the notes' rule (the file came from Claire)."),
 "AUDIO": dict(unit="C2", query="gdrive search: sound · sources; gsheets_values_get on the sheet",
    returned=snd_inj,
    assessment=f"A Drive search for 'sound' returns {len(snd_inj)} injected files (the sheet, the notes and the pack list; no longer Brian's log) and {snd_base} visible base files. The sheet's title says what it holds; only reading its cells gives the two rows marked 'no'. It does not name tickets or states: that those two cues are Owed, with Calvin, follows from the notes' rule on sound, and the brief's sound section has to hold them back as well."),
 "PICKS": dict(unit="C3", query="slack search: dynamite · bow · in place of; slack_read_thread on Julia's bow post",
    returned=[S["c3_reply"]["id"]],
    assessment=f"Item names do not return the reply: 'dynamite' gives {dyn} visible base messages plus Robert's 25 Sep post, 'bow' {bow} base messages, neither the reply. It is returned by a thread read under Julia's own bow post, or by its own wording. It names no item: 'it' is the bow of the parent post and 'the last one on my list' is the last item of his 25 Sep post, so both records have to be read together."),
 "ZIP": dict(unit="A1", query="gdrive search: outgoing · zip · sound; gdocs_get_document_text on the log",
    returned=outg_inj,
    assessment=f"A Drive search for 'outgoing' returns the log and the notes ({outg} base files); 'zip' returns the log and the pack list ({zp} visible base files); 'sound', the search made for the sound cues, no longer returns it (D3). The ask and the notes do not name the log; the notes' Ready test and every ticket note name the outgoing folder. The log says the zip with Friday's music instruments will not unpack and that those eight are not in the folder any other way; it names no line. Which eight (the tickets whose note says 'zipped with the other instruments') comes from the tickets."),
 "REVISED": dict(unit="A1", query="gdrive search: outgoing · gdocs: recoloured · chainsaw · cactus; gdocs_get_document_text on the log",
    returned=rev_inj,
    assessment="The same log, found the same way (the outgoing folder); a search for an item's name ('chainsaw', 'cactus') does not return it, because the entry says only 'the three recoloured models'. Robert's base post on the new colour versions (cactus, chainsaw and cones) says which three and is read by most runs; the log's later entry says Claire sent them again and that they open and look right, so the three are Ready. A run that reads Robert's post and not the log writes them Owed."),
}

# ---------------------------------------------------------------- evidence note
ev = [f"# Injection-stage hardness review evidence · {M.SLUG} · {REV} (design {M.DESIGN})\n",
      f"Authoring-session review of the six mechanisms on the injected universe: `01_Universe_Inject.sql` sha256 {hashlib.sha256(sql_path.read_bytes()).hexdigest()}. "
      "Readability is `persona_view.py check-sql` on that SQL (plan/out/check_sql.txt); natural retrieval is the rehearsal in plan/out/natural_retrieval_injection.txt "
      "(base as the persona, injected rows by their text) and `path_exposure.py` (plan/out/path_exposure.txt). No run, verdict or score is claimed here.\n"]
for mid, r in MECH.items():
    ev += [f"## {mid}\n", f"- First plausible answer: {r['first']}", f"- Deciding evidence (`{r['decider']}`): {r['decide']}", f"- Authority and chronology: {r['chrono']}",
           f"- Fair discovery path: {r['path']}", f"- Outcome change: before: {r['before']} · after: {r['after']}",
           f"- Outcome pair {r['pair'][0]} / {r['pair'][1]}: left passes, right fails when {r['left']}; right passes, left fails when {r['right']}."]
    q = RETRIEVAL[mid]
    ev += [f"- Readable: `{lb_line(r['decider'])}`", f"- Natural retrieval ({q['query']}): {q['assessment']}", f"- Path exposure: `{off_path(q['unit'])}`\n"]
ev += ["## Independence\n", "Five deciding records in five containers: #zombie-match3d (EXPORT), Julia's DM with Robert (ARTHOLD), Calvin's sheet (AUDIO), the thread under "
       "Julia's bow post (PICKS) and Brian's log of the outgoing folder, which decides two rules (ZIP: eight lines Owed; REVISED: three lines Ready). None quotes or links "
       "another; the lines they decide are disjoint (12, 12, 2, the board set of two lines, 8 and 3). ZIP and REVISED are one carrier and one loss channel.\n"]
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
        "fair_discovery_path": item(r["path"], EV_NAT),
        "changed_outcome": item("the solver's truth for the linked slots differs from the natural reading (solver/truth.json against the over-application and ch_miss operators; oracle_kit check PASS)", before=r["before"], after=r["after"]),
        "independent_operation": item("its deciding record decides its own lines and no other rule's record quotes, links or depends on it"
                                      + ("; it shares Brian's folder log with " + ("REVISED" if mid == "ZIP" else "ZIP") + " (one carrier, two rules)" if mid in ("ZIP", "REVISED") else ""),
                                      others_solvable_if_missed=[x for x in ids if x != mid and not ({x, mid} == {"ZIP", "REVISED"})]),
        "outcome_slots": linked,
        "channel_kind": "judgment",
        "outcome_pair": item(f"{r['pair'][0]} and {r['pair'][1]} are separate facts in separate deliverables", slots=list(r["pair"]),
                             left_pass_right_fail=r["left"], right_pass_left_fail=r["right"]),
    }
    if True:
        q = RETRIEVAL[mid]
        row["access"] = item(f"persona_view.py check-sql on the SQL: {lb_line(r['decider'])}", EV_READ, status="verified")
        row["natural_retrieval"] = item("natural persona searches rehearsed on the base and on the injected rows; path_exposure reports the record OFF-PATH", EV_NAT,
                                        query=q["query"], returned_ids=q["returned"], assessment=q["assessment"])
    mechs[mid] = row

review = {
    "schema_version": 1, "stage": "injection", "task_id": stage_evidence.task_identity(TASK), "revision": REV,
    "reviewer": "claude-opus-5-5 (authoring session, /create-injection rev2, design D3; two cold coherence reviewers read the ask and the injected records)",
    "difficulty_mode": ctx["difficulty_mode"].lower(), "diversity_channels": [x for x in ids if x != "REVISED"],   # D3: REVISED shares ZIP's deciding record (Brian's log), so it is one loss channel with ZIP
    "mechanisms": mechs, "dispositions": {},
    "input_hashes": input_hashes("injection", man, surf, sql_text=sql_text),
    "forecast": "UNCALIBRATED: design forecast and injection forecast ids in the Self-review of 01_Grounding_Dossier.md",
}
(rev_dir / "injection.json").write_text(json.dumps(review, indent=1, ensure_ascii=False) + "\n")
print("wrote", ev_path.name, "injection.json")
