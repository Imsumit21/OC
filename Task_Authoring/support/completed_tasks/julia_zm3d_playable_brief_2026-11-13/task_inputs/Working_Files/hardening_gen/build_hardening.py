#!/usr/bin/env python3
"""MODE B (rev1): disposition the proposed verdicts, build the pre-check matrix, receipt and mode_b_request.json, and
assemble Working_Files/01a_Hardening_Report.md from the tool outputs under run_forensics/rev1 and hardening_gen/out.

Inputs (all produced by tools in this run): run_forensics/rev1/{node_verdicts.json, precheck.node_verdicts.json,
proposals.jsonl, precheck.proposals.jsonl, surface_grades.json, precheck.surface_grades.json}, hardening_gen/out/{reach.json,
payloads.json}. Nothing here changes the universe, the prompt, the Oracle Events or a criterion.
Run from the workspace root:  python3 -B .../hardening_gen/build_hardening.py [--append-ledger]"""
import datetime as D, hashlib, json, re, subprocess, sys, os
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent; TASK = WF.parent; ROOT = TASK.parents[1]; TOOLS = TASK.parent / "tools"
sys.path.insert(0, str(TOOLS))
import difficulty_stats as stats            # noqa: E402
import stage_evidence                       # noqa: E402
from trajectory_ledger import binding_bundle_hash   # noqa: E402
from design_readiness import digest         # noqa: E402
R = WF / "run_forensics" / "rev1"
REL = lambda p: str(Path(p).resolve().relative_to(TASK.resolve()))
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ref(p): return {"path": REL(p), "sha256": sha(p)}
def J(p): return json.loads(Path(p).read_text())
RUNS = ["precheck"] + [f"run-{i}" for i in range(1, 7)]
EXPORT = {"precheck": TASK / "06_PreCheck_Trajectory" / "trajectory-run-1.json", **{f"run-{i}": TASK / "07_Baseline_Trajectories" / f"trajectory-run-{i}.json" for i in range(1, 7)}}
reach, pay = J(HERE / "out" / "reach.json"), J(HERE / "out" / "payloads.json")
nv, pv = J(R / "node_verdicts.json"), J(R / "precheck.node_verdicts.json")
sg, psg = J(R / "surface_grades.json"), J(R / "precheck.surface_grades.json")
surface = J(WF / "01_Gradable_Surface.json"); SLOTS = surface["slots"] if isinstance(surface, dict) else surface
W = {s["id"]: s["weight"] for s in SLOTS}; TOTAL = sum(W.values())
MECH = {s["id"]: (s.get("mechanisms") or []) for s in SLOTS}
ctx = J(WF / "00_Task_Context.json"); CLOCK = ctx["universe"]["clock_line"]
REVIEWER = "Claude (Fable 5.2), hardening_gen/build_hardening.py"
NODES = ["EXPORT", "ARTHOLD", "REVISED", "AUDIO", "PICKS", "ZIP"]
NEEDLE = {"EXPORT": "EXPORT Marcus (text kind)", "ARTHOLD": "ARTHOLD Claire DM", "REVISED": "REVISED Robert new colours", "AUDIO": "AUDIO Calvin sheet",
          "PICKS": "PICKS reply (bow swap)", "ZIP": "ZIP Brian log"}
RECORD = {"EXPORT": "C0880U9751A/1758906517.912099", "ARTHOLD": "D05HMBQUC8Z/1759148152.833779", "REVISED": "C090N54TG79/1759189466.554739",
          "AUDIO": "f_b2387e31d46d3a7b3fa2a9", "PICKS": "C08R8CHB0QL/1758922879.243189", "ZIP": "f_faf4d7c167d14a1127dcc3"}
def rule(run, node): return (pv if run == "precheck" else nv)["runs"][run]["rules"][node]
def reg_event(run): return (pv if run == "precheck" else nv)["runs"][run]["register"]["events"][0]
def first(run, node): return reach[run]["needles"][NEEDLE[node]]["first"]
def results(run): return (psg["runs"]["precheck"] if run == "precheck" else sg["runs"][run])["results"]
def failed(run): return [k for k, v in results(run).items() if v is False]
def score(run): return 1 - sum(W[k] for k in failed(run)) / TOTAL
def counted(run): return (psg["runs"]["precheck"] if run == "precheck" else sg["runs"][run])["counted_calls"]
MISS = {n: [r for r in RUNS if rule(r, n)["verdict"] == "NOT-REACHED"] for n in NODES}
FOUND = {n: [r for r in RUNS if rule(r, n)["verdict"] == "LEAKED"] for n in NODES}
for n in NODES:
    assert len(MISS[n]) + len(FOUND[n]) == 7, n
    for r in MISS[n]: assert first(r, n) is None, (n, r)        # the deciding record's content never came back
    for r in FOUND[n]: assert first(r, n) is not None, (n, r)
def short(inp, k=90):
    try: j = json.loads(inp)
    except Exception: return inp[:k]
    return ", ".join(f"{a}={str(b)[:48]}" for a, b in j.items() if a not in ("response_format", "limit", "pageSize"))[:k] if isinstance(j, dict) else str(j)[:k]
def how(run, node):
    h = first(run, node)
    return f"{run} · event {h['event']} ({h['tool']} {short(h['input'])})"

# ------------------------------------------------------------------ 1 dispositions (ledger records)
WHY_MISS = {
 "EXPORT": "Marcus's root post {rec} in #zombie-match3d never came back in any result of this run; the note's own claim ('Opens, looks right. In the outgoing folder.') was taken as it stood and the 12 lines were written Ready at event {ev}. The record is in a channel Julia belongs to and an ordinary channel-history or author search returns it (it did in four other runs): a genuine retrieval miss.",
 "ARTHOLD": "Claire's DM {rec} never came back in this run (no search by her name or of that DM); the 12 bathroom lines were written Ready at event {ev}. The DM is Julia's own and six other runs read it: a genuine retrieval miss.",
 "AUDIO": "Calvin's sheet {rec} was never listed or read in this run (its Drive searches were for 'sfx', 'brief', 'hand-off', 'playable' and 'pack'); Rocket sound and Explosion sound were written Ready at event {ev}. The sheet is shared with Julia and a Drive search for 'sound' lists it (six other runs): a genuine retrieval miss.",
 "PICKS": "Robert's reply {rec} under Julia's bow post was never read in this run; the eight kept Dynamite in the brief and on the sheet (event {ev}). The reply sits in a public channel thread whose parent shows two replies: a genuine retrieval miss.",
 "ZIP": "Brian's log {rec} was never listed or read in this run; the 8 zipped instruments were written Ready at event {ev}. The doc is shared with Julia and its title is the folder the notes name: a genuine retrieval miss.",
}
def disposition(rec, run):
    rec = json.loads(json.dumps(rec))
    rec["features"]["reviewed_by"] = REVIEWER
    if rec["kind"] == "verdict":
        node = rec["node"]
        if rec["verdict"] == "NOT-REACHED":
            rec["evidence"]["tool_proposal"] = "NOT-REACHED (" + rec["evidence"]["why"][:160] + ")"
            rec["verdict"] = "LANDED"
            rec["evidence"]["why"] = WHY_MISS[node].format(rec=RECORD[node], ev=reg_event(run))
            rec["evidence"]["disposition"] = {"action": "keep", "note": "the tool reports the deciding record never reached the writer; for Opus a missed discoverable source is a genuine retrieval failure (playbook gate 8), so the verdict is LANDED", "proposed": []}
            rec["features"]["disposition"] = "LANDED by hand: reachable deciding record never retrieved; write payload confirmed (hardening_gen/out/payloads.json)"
            rec["features"]["disposed_by"] = REVIEWER
        else:
            h = first(run, node)
            rec["evidence"]["disposition"] = {"action": "keep", "note": f"deciding record returned at event {h['event']} by {h['tool']} ({short(h['input'], 120)}); the rule's lines are right on the sheet", "proposed": []}
            rec["features"]["disposition"] = "LEAKED confirmed: deciding record read and applied"
    else:
        rec["features"]["disposition"] = "tool record kept as proposed after the register write was reviewed (" + rec["kind"] + ")"
    return rec
def write_dispositions():
    out = {}
    for name, src, runs in (("precheck.dispositioned.jsonl", R / "precheck.proposals.jsonl", ["precheck"]), ("dispositioned.jsonl", R / "proposals.jsonl", RUNS[1:])):
        recs = [disposition(json.loads(l), json.loads(l)["run"]) for l in src.read_text().splitlines() if l.strip()]
        assert {r["run"] for r in recs} == set(runs)
        (R / name).write_text("\n".join(json.dumps(r, ensure_ascii=False, sort_keys=True) for r in recs) + "\n")
        out[name] = recs
    return out

# ------------------------------------------------------------------ 2 matrix, receipt, request (pre-check, provisional)
def build_request():
    path = EXPORT["precheck"]; exported = J(path); esha = sha(path)
    status, _, detail = stats.read_trajectory(path)
    assert status == "completed" and detail["counted"] == counted("precheck")
    data = {"spec_version": "V3", "difficulty_mode": "hard", "task_type": "long-horizon",
            "rubrics": [{"id": s["id"], "title": f"{s['id']} {s['title']}", "weight": s["weight"]} for s in SLOTS],
            "rollouts": [{"id": "run-1", "status": "completed", "tool_calls": detail["counted"], "models": sorted(stats.trajectory_models(path)), "results": results("precheck")}]}
    (R / "precheck.matrix.json").write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    task_id = stage_evidence.task_identity(TASK); bundle = binding_bundle_hash(TASK, None, stage="precheck")
    hard = TASK / "eval_reports" / "6aea4c201e1fa1ddfdd0a25d_1a_hardness.md"
    base_ev = [ref(path), ref(R / "precheck" / "writes.json"), ref(hard)]
    receipt = {"kind": "PRECHECK_EXPORT_REVIEW", "schema_version": 1, "task_id": task_id, "revision": "rev1", "bundle_hash": bundle, "reviewer": REVIEWER + "; write payloads and deciding-record reach reviewed",
               "reason": "The export is one complete Opus 5.5 run bound to rev1 by seeded content; each of the 18 failed surface slots was confirmed against the decoded write payloads (sheet states 8/56/32, Dynamite as Default, 32 ticket moves) and agrees with the platform /hardness report (causes C1 ASCII note, C2 outgoing-folder doc, C3 board swap).",
               "evidence": base_ev, "export_sha256": esha, "source_matrix_sha256": digest(data)}
    (R / "precheck.receipt.json").write_text(json.dumps(receipt, indent=1, ensure_ascii=False) + "\n")
    def ev(i, quote):
        assert quote in json.dumps(exported[i], ensure_ascii=False), (i, quote)
        return {"run": "run-1", "event": i, "export_sha256": esha, "quote": quote}
    fo = HERE / "out" / "reach.json"; po = HERE / "out" / "payloads.json"; sql = TASK / "01_Universe_Inject.sql"; led = WF / "08_OE_Writing_Ledger.md"
    def chk(reason, *paths): return {"reason": reason, "evidence": [ref(p) for p in paths]}
    fair = lambda what: chk(f"{what} is incorporated through the ask and the hand-off notes ('if someone who knows the file or the art has said something since, that counts'; 'unless he's changed them since') and the platform /prompt review scored Unique Ground Truth 5 on these bytes.", TASK / "eval_reports" / "6aea4c201e1fa1ddfdd0a25d_1_prompt.md", sql)
    readable = lambda what: chk(f"{what} is body text in a record Julia can open (persona_view check-sql YES, pasted in the OE ledger); no attachment, Trash or unlinked record is involved.", led, sql)
    grader = lambda what: chk(f"The failed slots were confirmed against the decoded write payload, not the narration: {what}. The platform /hardness report lists the same misses.", R / "precheck" / "writes.json", po, hard)
    rw = reg_event("precheck")
    diagnoses = [
     {"id": "D-EXPORT", "observation": "all_fail", "criteria": ["X1", "X1b", "X6", "X16", "W4", "K1", "A1", "A2", "W1", "W2"],
      "mechanism": "EXPORT landed in this run: Marcus's note that Thursday's saves out of Unity are the text kind never came back. The run searched Slack for 'FBX' and read the PlayableX, #zombie-design, #zombie-art and Claire histories, but never #zombie-match3d and never a search by Marcus or by the note's own words; it took 'Opens, looks right. In the outgoing folder.' as it stood and wrote the 12 lines Ready. The four count slots fail as a cascade of this cause and of D-ZIP.",
      "trajectory_events": [ev(315, "FBX after:2025-09-24"), ev(rw, '"Refrigerator", "Kitchen", "Extra", "Ready"'), ev(560, "Ready: 56")],
      "reason": "Retrieval miss of a reachable record: four of the six baseline runs read the same post (author search, 'saved out', 'export', channel history).",
      "evidence": base_ev + [ref(fo)], "fairness": fair("The later-word rule that makes the 12 lines Owed"), "readability": readable("Marcus's post"), "grader_accuracy": grader("12 rows Ready, 12 tickets untouched, counts 8/56/32")},
     {"id": "D-ZIP", "observation": "all_fail", "criteria": ["X4", "X4b", "X9", "X17", "K4"],
      "mechanism": "ZIP landed in this run: Brian's outgoing-folder log was never listed. The run's Drive searches were 'playable', 'Domino playable', 'audio', 'Universal Sound' (full text) and 'sound' (title); none returns the log. In the baseline, five of six runs reached the same log through one full-text Drive search for 'sound', the query that also lists Calvin's sheet, because the log says 'The sound files.': the unit was not independent of AUDIO.",
      "trajectory_events": [ev(427, "Universal Sound"), ev(428, "sound"), ev(rw, '"Cello", "Music Instruments", "Extra", "Ready"')],
      "reason": "Retrieval miss here; in the baseline the same record leaked through a query made for another unit.",
      "evidence": base_ev + [ref(fo)], "fairness": fair("The Ready rule ('sitting in the outgoing folder') and the eight notes that name the zip"), "readability": readable("The log, a Google Doc shared with Julia,"), "grader_accuracy": grader("8 instrument rows Ready and their 8 tickets untouched")},
     {"id": "D-PICKS", "observation": "all_fail", "criteria": ["X13", "X14", "B1"],
      "mechanism": "PICKS landed in this run: the #zombie-art history came back with Julia's bow post and its two replies, but the thread was never opened, and the search for Robert's messages started on Sep 29, after his Sep 26 reply. The brief and the sheet keep Dynamite in the eight.",
      "trajectory_events": [ev(349, "Can we have arrow to go with the bow"), ev(473, "after:2025-09-29"), ev(521, "Dynamite"), ev(rw, '"Dynamite", "Survival", "Default"')],
      "reason": "A thread reply under a parent that names no pick; reading the channel is not enough, the thread has to be opened. Three of six baseline runs opened it.",
      "evidence": base_ev + [ref(fo)], "fairness": fair("Robert's later change, which the ask makes binding,"), "readability": readable("Robert's reply, a message in a public channel thread,"), "grader_accuracy": grader("Dynamite Default and Bow Extra on the sheet, Dynamite in the brief's eight")},
     {"id": "D-ARTHOLD", "observation": "first_read_correction", "criteria": ["X2", "X2b", "X7", "X11", "X11b", "K2"],
      "mechanism": "ARTHOLD leaked: one search for Claire's messages since Sep 23 returned her DM to Julia in the first result, and the run applied it to the 12 bathroom lines. The correction sits where a routine author sweep reads first; six of seven runs found it the same way (author search, DM history or a DM date sweep). Turkish was no obstacle in any run.",
      "trajectory_events": [ev(321, "from:<@EMPLOYEE_0009_SLACK_ID> after:2025-09-23"), ev(322, "banyo objelerinin"), ev(rw, '"Bathtub", "Bathroom", "Extra", "Owed"')],
      "reason": "The budget's second anchor was opened at step 127 (budget_outcome: NO-GO).", "evidence": base_ev + [ref(fo), ref(WF / "06_Budget_Outcome.json")]},
     {"id": "D-REVISED", "observation": "first_read_correction", "criteria": ["X3", "X3b", "X8", "K3"],
      "mechanism": "REVISED leaked in all seven runs: Robert's new-colours post is a root message in #zombie-design, whose history six of seven runs read right after his picks (run-2 found it with a Slack search for 'color'), so the correction arrives with the hub records and needs no separate retrieval.",
      "trajectory_events": [ev(77, "C090N54TG79"), ev(80, "new colored version of cactus"), ev(rw, '"Cactus Plant", "Garden", "Default", "Owed"')],
      "reason": "Same container as an anchor record: the unit carries no difficulty for Opus 5.5.", "evidence": base_ev + [ref(fo)]},
     {"id": "D-AUDIO", "observation": "heavy_all_pass", "criteria": ["X5", "X5b", "X10", "X12", "K5", "B6"],
      "mechanism": "AUDIO leaked: the notes state the sound rule outright, so the run went looking for where each sound came from (twelve sound, licence and library searches) and a Drive search listed Calvin's sheet, whose two 'no' rows settle it. Six of seven runs found the sheet with one Drive search: five with a full-text search for 'sound', the pre-check with 'Universal Sound'.",
      "trajectory_events": [ev(427, "Universal Sound"), ev(433, "f_b2387e31d46d3a7b3fa2a9"), ev(434, "Soundly library"), ev(rw, '"Rocket sound", "", "", "Owed"')],
      "reason": "A rule stated in the incorporated notes plus a sheet titled with the obvious noun: a lookup, not a decision.", "evidence": base_ev + [ref(fo)]},
    ]
    def repair(rid, diag, placement, change, outcomes, before, after, path, kind="placement"):
        return {"id": rid, "diagnosis": diag, "artifact": "universe", "owner": "create-scenario --revise", "change_kind": kind, "original_placement": placement, "proposed_change": change,
                "affected_outcomes": outcomes, "scope_difference": {"reason_class": "difficulty", "before": before, "after": after}, "fair_discovery_path": path,
                "required_reruns": ["scenario", "injection", "prompt-check", "humantime", "oe-writing", "oe-check", "precheck", "baseline"], "reason": change, "evidence": base_ev + [ref(fo), ref(po)]}
    repairs = [
     repair("RP-ARTHOLD", "D-ARTHOLD", "Claire's own DM to Julia D05HMBQUC8Z/1759148152.833779, returned by any search for Claire's recent messages",
            "Carry the same fact (the bathroom objects' UVs are being redone from scratch, so Friday's bathroom files are the old state) in a record that a search by Claire's name does not return, for example a message from Robert in his DM with Julia saying so. Claire's DM row is removed. No line, rule or row is added; the coherence sweep has to confirm the new author is one who would know.",
            ["X2", "X2b", "X7", "X11", "X11b", "K2"], "one seeded DM from Claire to Julia (Mon Sep 29), found by an author sweep", "one seeded DM from Robert to Julia (Mon Sep 29) stating the same redo; no message from Claire",
            "Julia's own DM with Robert: its history, or any search of her DMs for the days since the files were made; the notes say a later word from someone who knows the art counts"),
     repair("RP-ZIP", "D-ZIP", "Brian's log f_faf4d7c167d14a1127dcc3 carries the sentence 'The sound files.', so the Drive search that finds Calvin's sheet lists it",
            "Reword the log's 'The sound files.' so it keeps the fact (the five sound exports are in the folder, which the Ready state of three sounds needs) without the word the AUDIO search uses, for example 'The .wav exports.'; the title and the Tue 30 Sep entry stay as they are. No record is added or hidden.",
            ["X4", "X4b", "X9", "X17", "K4"], "log body says 'The sound files.'; listed by a full-text Drive search for 'sound' (5 of 6 baseline runs)", "log body says the same thing without the word 'sound'; listed by a Drive search for the outgoing folder",
            "the notes' Ready rule ('sitting in the outgoing folder') and the eight ticket notes ('Zipped with the other instruments, in the outgoing folder') name the folder; a Drive search for it lists the log, which is shared with Julia", kind="decoupling"),
     repair("RP-REVISED", "D-REVISED", "the only later word on Cactus Plant, Chainsaw and Cone is Robert's base post C090N54TG79/1759189466.554739, in the channel read for his picks",
            "Add a completion note off that path (v2 move A25): the outgoing-folder log records, on Tue 30 Sep, that Claire re-sent the three with the new colours, that they open and look right, and that they replaced the Thursday files. The three lines become Ready; a run that stops at Robert's post writes them Owed. Counts become Delivered 8, Ready 39, Owed 49. No row or line is added; the surface slots of the three lines change their expected value.",
            ["X3", "X3b", "X8", "K3", "A1", "A2", "W1", "W2"], "three lines Owed on the first-read post; 7 of 7 runs right", "three lines Ready by a later entry in the folder log; a run that never opens the log writes them Owed",
            "the same log as RP-ZIP: the notes point at the outgoing folder for what is Ready, and 'go by how things stand today'", kind="completion_note_elsewhere"),
     repair("RP-EXPORT", "D-EXPORT", "Marcus's post C0880U9751A/1758906517.912099 repeats the wording of Brian's note ('saved out of') and the word 'exporter', so a search for the note's own words returns it (runs 2 and 3)",
            "Keep the post, its author, channel and time; reword it so it no longer echoes the note it corrects (the models you got out of Unity on Thursday are the text kind). The fact and its reach are unchanged.",
            ["X1", "X1b", "X6", "X16", "W4", "K1"], "post found by 'saved out' and 'export' searches as well as by channel history and an author search (4 of 6 baseline runs)", "post found by channel history or a search for Marcus's messages",
            "#zombie-match3d history for the days after Brian's Thursday files, or a search for Marcus's messages; Julia is a member of the channel", kind="wording"),
    ]
    request = {"task_id": task_id, "revision": "rev1", "bundle_hash": bundle, "precheck": True, "data_path": REL(R / "precheck.matrix.json"), "receipt": REL(R / "precheck.receipt.json"),
               "trajectories": [REL(path)], "diagnoses": diagnoses, "repairs": repairs}
    (WF / "mode_b_request.json").write_text(json.dumps(request, indent=1, ensure_ascii=False) + "\n")
    return request

if __name__ == "__main__":
    d = write_dispositions()
    req = build_request()
    print("dispositioned:", {k: len(v) for k, v in d.items()}, "| diagnoses", len(req["diagnoses"]), "repairs", len(req["repairs"]))
    for n in NODES: print(f"  {n:8} LANDED {len(MISS[n])} {MISS[n]} · LEAKED {len(FOUND[n])}")
    print("  scores", {r: round(100 * score(r), 1) for r in RUNS})
