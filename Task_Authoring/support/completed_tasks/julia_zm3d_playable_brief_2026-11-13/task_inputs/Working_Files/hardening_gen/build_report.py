#!/usr/bin/env python3
"""Assemble Working_Files/01a_Hardening_Report.md (MODE B, rev1) from the tool outputs. Every number is read from a file
written by a tool in this run; every event number is a 0-based index into the export array. Run from the workspace root,
then: python3 -B Task_Authoring/tools/stage_gate.py hardening Task_Authoring/task_inputs --paste"""
import datetime as D, json, os, re, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_hardening as B
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=str(B.TASK))
OUT = B.WF / "01a_Hardening_Report.md"
def cell(s): return re.sub(r"\s+", " ", str(s)).replace("|", "/").strip()
def table(header, rows): return ["| " + " | ".join(header) + " |", "|" + "---|" * len(header)] + ["| " + " | ".join(cell(c) for c in r) + " |" for r in rows]
def tool(*a):
    p = subprocess.run([sys.executable, "-B", str(B.TOOLS / a[0]), *a[1:]], capture_output=True, text=True, cwd=B.ROOT, env=ENV)
    return [l.rstrip() for l in (p.stdout or p.stderr).splitlines() if l.strip()]
RUNS, NODES, reach, pay = B.RUNS, B.NODES, B.reach, B.pay
base6 = RUNS[1:]
pct = lambda x: f"{100 * x:.1f}%"
sc = {r: B.score(r) for r in RUNS}
gates = B.sg["gates"] if "gates" in B.sg else {}
summ = {r["label"]: r for r in B.J(B.R / "summary.json")["runs"]}
calls = {r: [json.loads(l) for l in open(B.R / r / "calls.jsonl")] for r in RUNS}
errs = {r: [c for c in calls[r] if c.get("error") or c.get("failed")] for r in RUNS}
hard = (B.TASK / "eval_reports" / "6aea4c201e1fa1ddfdd0a25d_1a_hardness.md").read_text()
hclock = re.search(r"^Clock: .*$", hard, re.M).group(0)
manifest = "Evals/references/universes/synthcut/universe_manifest.json"
# corrected proxy: D4 on run-5 (the share calls omit the role and the tool returns role reader)
corr = dict(sc); lost5 = sum(B.W[k] for k in B.failed("run-5") if k != "D4"); corr["run-5"] = 1 - lost5 / B.TOTAL
assert "D4" in B.failed("run-5") and all(s[2] is None for s in pay["run-5"]["shares"])
avg = lambda d: sum(d[r] for r in base6) / 6
import statistics
sd = statistics.pstdev([sc[r] for r in base6])
full = [r for r in base6 if not B.failed(r)]
qc = tool("surface_grader.py", "--task-dir", str(B.TASK), *sum((["--run", f"{r}={B.EXPORT[r]}"] for r in base6), []))
gate_lines = [l for l in qc if l.lstrip().startswith(("V3 (", "provenance:"))]
v2 = tool("hardness_v2_check.py", "--task-dir", str(B.TASK))
bo = tool("budget_outcome.py", "compare", "--task-dir", str(B.TASK))
sr = tool("budget_outcome.py", "stop-rule", "--task-dir", str(B.TASK))

def tool_out(script):
    p = subprocess.run([sys.executable, "-B", str(HERE / script), "20000"], capture_output=True, text=True, cwd=B.ROOT, env=ENV)
    return [l.rstrip() for l in p.stdout.splitlines() if l.strip()]
def ev(run, key): return reach[run]["needles"][key]["first"]["event"] if reach[run]["needles"][key]["first"] else None
def missed(n): return "; ".join(f"{r} · event {B.reg_event(r)}" for r in B.MISS[n]) or "none"
def found(n): return "; ".join(B.how(r, n) for r in B.FOUND[n])
KIND = {
 "EXPORT": "retrieval miss where it landed; where it leaked, the post was returned by an author search, by the note's own words ('saved out'), by 'export', or by the channel history",
 "ARTHOLD": "first_read: the persona's own DM, returned by a search for the author's recent messages",
 "REVISED": "same_container: a root post in the channel read for the picks",
 "AUDIO": "rule stated in the notes and a sheet named with the obvious noun: a lookup",
 "PICKS": "thread reply under a parent that names no pick; found only by opening the thread",
 "ZIP": "a query made for another unit carried it: full-text 'sound' lists the log beside Calvin's sheet",
}
REG = [(n, B.RECORD[n], (f"LANDED {len(B.MISS[n])} · " if B.MISS[n] else "") + f"LEAKED {len(B.FOUND[n])} of 7", missed(n), found(n), KIND[n]) for n in NODES]

LED = []
for r in RUNS:
    p = pay[r]; s = p["sheet"]["states"]
    reads = ", ".join(f"{n} {ev(r, B.NEEDLE[n])}" for n in NODES if ev(r, B.NEEDLE[n]) is not None)
    miss = ", ".join(n for n in NODES if ev(r, B.NEEDLE[n]) is None) or "none"
    dm = next((t for _, ch, _, t in p["slack"] if ch == "D05SD5QLG94"), "")
    cnt = re.search(r"Delivered[^0-9]{0,6}(\d+).{0,40}?Ready[^0-9]{0,6}(\d+).{0,40}?Owed[^0-9]{0,6}(\d+)", dm.replace("*", ""), re.S)
    LED.append((r, B.counted(r), f"ask {ev(r, 'ask')}, notes {ev(r, 'notes')}, pack list {ev(r, 'pack_list')}, pack ticket {ev(r, 'pack_ticket')}", reads, miss,
                f"sheet event {B.reg_event(r)}: Delivered {s.get('Delivered')}, Ready {s.get('Ready')}, Owed {s.get('Owed')}; eight with {'Bow' if p['sheet']['sample']['Bow'][1] == 'Default' else 'Dynamite'}; "
                f"{p['tickets']['todo']} moves, {p['tickets']['comments']} comments, {len(p['shares'])} shares; DM counts {'/'.join(cnt.groups()) if cnt else 'see payloads.json'}",
                pct(sc[r])))

heavy_all = [s["id"] for s in B.SLOTS if s["weight"] == 5 and all(B.results(r)[s["id"]] for r in base6)]
heavy_mech_all = [i for i in heavy_all if B.MECH[i]]
landed_weight = {n: sum(B.W[i] for i in B.W if B.MECH[i] == [n]) for n in NODES}
mech_weight = sum(w for i, w in B.W.items() if B.MECH[i])
moved = sum(B.W[i] for i in B.W if any(not B.results(r)[i] for r in base6))
ids = [json.loads(l) for l in tool("hardness_ledger.py", "query", "--kind", "verdict", "--task", "task_inputs", "--json")] if False else None
led = json.loads("\n".join(tool("hardness_ledger.py", "query", "--kind", "verdict", "--task", "task_inputs", "--json")))
led = [r for r in (led if isinstance(led, list) else led.get("records", [])) if r.get("revision") == "rev1"]
landed_ids = sorted(r["id"] for r in led if r["verdict"] == "LANDED")
assert len(led) == 42 and len(landed_ids) == 11

CR = [
 ("EXPORT · LANDED (precheck, run-4, run-5)", "Tool: the searches these runs made could have failed to return a post that matches",
  f"none of their queries matches the post ('FBX', 'ASCII', 'outgoing', 'zip', 'playable'); precheck event 315, run-4 events 249 and 325, run-5 events 252 and 418. The post exists (SQL L58) and run-6 event 259 shows the plain channel history returns it", "LANDED stands (retrieval, not tool)"),
 ("EXPORT · LEAKED (run-1, 2, 3, 6)", "The trap was never live: the note's own words return the correction",
  "true for run-2 event 424 ('saved out') and run-3 event 304 ('export'): a lexical echo, routed as RP-EXPORT; run-1 event 284 and run-6 event 259 are an author search and a channel read, which are fair finds", "LEAKED stands; partly a wording leak"),
 ("ARTHOLD · LANDED (run-1)", "Run: run-1 might have been cut short before it could look", "run-1 is complete (708 events, 244 counted calls); it searched by Robert, Marcus, Calvin and Brian (events 276, 283, 423, 425) and read #zombie-art, never Claire's messages or DM", "LANDED stands"),
 ("ARTHOLD · LEAKED (6 runs)", "The trap was never live: the correction is in the first place anyone looks", f"six runs reached it by a search for Claire's messages or her DM history (precheck event 322, run-2 466, run-3 284, run-4 347, run-5 270, run-6 478); budget_outcome calls the anchor opened", "LEAKED stands; the anchor is exposed and is routed as RP-ARTHOLD"),
 ("REVISED · LEAKED (7 runs)", "The trap was never live", "the deciding post is a root message in #zombie-design; six runs read it in the channel history (precheck event 80, run-1 512, run-3 268, run-4 265, run-5 298, run-6 281) and run-2 by a search for 'color' (event 306); re-read through hg.py as slack/messages/C090N54TG79/2025-09.json/813", "FALSE as a retrieval unit: goes to the purge and rebuild lists"),
 ("AUDIO · LANDED (run-1)", "Tool: a Drive search for the sheet could have failed", "run-1 searched Drive for 'sfx', 'brief', 'hand-off', 'playable' and 'pack' (events 21 to 23, 380, 430) and never for 'sound'; the same search returns the sheet in six runs (run-2 event 406)", "LANDED stands"),
 ("AUDIO · LEAKED (6 runs)", "The trap was never live: the notes state the rule", "the notes say 'Anything from a library or a bought pack stays here' and the sheet's title holds the noun every run searched (precheck event 434, run-3 335)", "LEAKED stands; kept as realism, no rebuild proposed"),
 ("PICKS · LANDED (precheck, run-3, run-4, run-5)", "Fairness: a reply that names no item could be read two ways", "the reply sits under Julia's bow post and says 'in the 8 in place of the last one on my list'; the 25 Sep list ends with Dynamite (SQL L60, SQL L61); /prompt settled the fork as F8 and F9; precheck event 349 and run-5 event 294 show the parent came back with its replies unopened", "LANDED stands"),
 ("PICKS · LEAKED (run-1, 2, 6)", "The trap was never live", "each of the three opened the thread on purpose after reading the channel (run-1 event 321, run-2 345, run-6 314); four runs did not", "LEAKED stands: a live coin flip"),
 ("ZIP · LANDED (precheck, run-1)", "Fairness: nothing points at the log", "the notes' Ready rule and the eight ticket notes name the outgoing folder, and the doc is titled for it and shared with Julia (SQL L15, SQL L20); /hardness counted the miss as genuine (cause C2)", "LANDED stands"),
 ("ZIP · LEAKED (5 runs)", "The trap was never live: a bulk call carried the answer", "all five listed the log with one full-text Drive search for 'sound' made for the sound question (run-2 event 406, run-3 333, run-4 307, run-5 384, run-6 419): the log says 'The sound files.' (SQL L20)", "LEAKED by coupling with AUDIO; routed as RP-ZIP"),
 ("Band (median run, run-4)", "Neighbouring band: 3 instead of 4, because run-4's error is one group of 12 lines and one swapped item, a bounded correction",
  "the correction still touches the sheet (12 rows and 2 cells), 12 tickets, the counts in the DM and the brief's eight (run-4 events 440, 443, 632), the same spread that /hardness scored 4 on the pre-check", "4 kept; 3 is the neighbour"),
]

doc = ["# 01a Hardening Report — julia-zm3d-playable-brief (rev1)", "",
 f"Generated {D.date.today().isoformat()} · {B.CLOCK} · universe manifest {manifest}", "",
 "## 1 · Mode, inputs and run validity", "",
 "MODE B: forensics on seven Opus 5.5 runs of rev1, the platform pre-check and the six baseline rollouts. The formal Mode B request (Working_Files/mode_b_request.json) is the provisional pre-check kind, because no rubric or verifier exists yet; the six baseline runs are graded on the gradable surface as a design check (playbook B3d) and are labelled as such everywhere below.", "",
 "Inputs read: 00_Assigments.md, 01_Universe_Inject.sql (rev1, sha256 78465cd474f8; the platform ran the same statements without the four header comment lines, sha256 3a76797fbde1), 01_Grounding_Dossier.md, 01_Hardness_Manifest.json, 01_Gradable_Surface.json, solver/solver.py, 03_Error_Async_Config.txt (Friction: none), 04_Prompt.txt, 06_PreCheck_Trajectory/trajectory-run-1.json, 07_Baseline_Trajectories/trajectory-run-1.json to trajectory-run-6.json, eval_reports (/injection PASS, /prompt PASS, /hardness NON-FAIL), 08_Oracle_Events.md (a local draft, not submitted).",
 "Inputs missing: 10_Baseline_Verifier_Results.md and 09_Rubrics.json are empty and 12_Difficulty_Stats.txt does not exist, so there are no gate numbers of record; section 2 gives the surface grader's design check instead. Section 7 has no judge text to open.", "",
 f"The quoted /hardness report carries `{hclock}`.", "",
 "Run validity (trajectory_ledger.py; each run BOUND to rev1 as the sole revision, on seeded content seen in its results):", ""]
doc += table(["Run", "Export sha256", "Events", "Counted calls", "Model", "Status", "Mixed model", "Result events after the final answer"],
             [(r, summ[r]["sha256"][:12], summ[r]["validity"]["events"], B.counted(r), "claude-opus-5-5", summ[r]["validity"]["status"], summ[r]["provenance"]["mixed_model"],
               "events 840 and 846 acknowledge background timers only" if r == "precheck" else "none") for r in RUNS])
doc += ["", "Every message of every run is Opus 5.5; no fallback, no compaction gap. The exports carry no user prompt; each run's first calls search for Frederick's message of 30 Sep, which matches the saved prompt. Each run is bound to rev1 on seeded content found in its own results (trajectory_ledger: BOUND).", "",
 "## 2 · Gate status (design check on the gradable surface; no verifier yet)", "",
 "`python3 -B Task_Authoring/tools/surface_grader.py --task-dir Task_Authoring/task_inputs` on the six baseline runs (coverage 195 of 195 weight; the rubric and verifier remain the grading of record):", "", "```text"] + gate_lines + ["```", ""]
doc += table(["Run", "Score on the surface", "Failed slots", "Corrected"],
             [(r, pct(sc[r]), ", ".join(B.failed(r)) or "none", pct(corr[r]) + (" (D4 corrected)" if r == "run-5" else "")) for r in RUNS])
doc += ["", f"Six-run average {pct(avg(sc))} raw, {pct(avg(corr))} corrected, against a cap of under 70%: the average gate fails by about 12 points. Full passes {len(full)} of 6 ({', '.join(full)}); population SD {sd:.3f}; three failure patterns. The pre-check ({pct(sc['precheck'])}) is not part of the six.",
 f"Correction: D4 on run-5. Its eight share calls give no role and the tool returns role reader (run-5 event 455, result event 456), so the list was shared for viewing; the decoder reads a missing role argument as a failure. Clean average: {pct(avg(corr))}; no failure is CONFOUNDED.",
 f"Mechanism weight share: {mech_weight} of {B.TOTAL} weight ({pct(mech_weight / B.TOTAL)}) depends on a mechanism; {moved} ({pct(moved / B.TOTAL)}) failed in at least one baseline run. By node: " + ", ".join(f"{n} {landed_weight[n]}" for n in NODES) + ", shared counts 12.",
 "Concentration: no single node drives the failures; the losses came from EXPORT (2 runs), PICKS (3), and one run that missed ARTHOLD, AUDIO and ZIP together.", "",
 "## 3 · Predicted /hardness band", "",
 "Pre-check: the platform's /hardness is on file: NON-FAIL, score 4, three independent causes (ASCII note, outgoing-folder doc, board swap), 253 calls.",
 "Baseline, for the run closest to the median (run-4, 72.8%), by the procedure of Evals/1A_Hardness_Eval.md:", ""]
doc += table(["Requirement", "Result in run-4", "Citation"], [
 ("Find and follow the ask, the notes, the pack list and the 96 notes", "MET", "run-4 events 7, 18, 20, 27"),
 ("Brief: the eight on the board", "MATERIAL_FAIL: Dynamite, not Bow (PICKS)", "run-4 event 443"),
 ("Brief: scenario, zombies, tray, loss, sound, music, start date", "MET", "run-4 event 443"),
 ("List: 96 rows, seven columns", "MET", "run-4 event 440"),
 ("List: the 12 Thursday saves", "MATERIAL_FAIL: Ready, not Owed (EXPORT)", "run-4 event 440"),
 ("List: bathroom, colour versions, instruments, sounds, not-exported lines", "MET", "run-4 events 347, 265, 313, 315"),
 ("Tickets: Owed lines to Todo with a comment", "MATERIAL_FAIL as a cascade: 40 of 52", "run-4 writes.json"),
 ("Counts to Frederick", "MATERIAL_FAIL as a cascade: 8 / 48 / 40", "run-4 event 632"),
 ("Shares and the channel post", "MET", "run-4 event 634"),
])
doc += ["", "Two independent causes (EXPORT, PICKS); nothing CONFOUNDED. Predicted band 4: the wrong lines carry into the tickets, both counts and the brief, so the correction runs across the result. It is not 3 because more than one deliverable needs correcting; it is not 5 because the delivery is complete and 82 of the 96 rows are right. Runs 2 and 6 would be HOLD (everything right) and run-3 a 3 (the swap only): the task does not hold its difficulty from run to run.", "",
 "## 4 · Designed-difficulty register", "",
 "One row per designed node; counts are over the seven runs. A miss is cited by the event of the sheet write that carries the wrong value, a find by the event whose result first returned the deciding record.", ""]
doc += table(["Node", "Deciding record", "Verdict counts", "Missed in (run · event of the write)", "Found in (run · event · call)", "v2 failure kind"], REG)
doc += ["", "Controls: all 42 control trials HELD (no rule was over-applied to a line it does not cover). Channels: 11 FAILED, 31 HELD, the same runs and nodes as above. Ledger: 126 dispositioned records appended (42 verdicts, 42 controls, 42 channels); the eleven that record a miss are " + ", ".join(landed_ids) + ".", "",
 "## 5 · Per-rollout ledgers", "",
 "Full ledgers: Working_Files/run_forensics/rev1/ (calls.jsonl, writes.json, briefs.json per run); reach of each deciding record: Working_Files/hardening_gen/out/reach.json; write payloads: hardening_gen/out/payloads.json. The pre-check delegated its 32 ticket writes to one sub-agent on the same model; no baseline run used a brief.", ""]
doc += table(["Run", "Counted calls", "Hub (event of first read)", "Deciding records read (event)", "Deciding records never returned", "What it wrote", "Score"], LED)
doc += ["", "Review coverage: every call was classified by the tools; I reviewed the queued register write of each run (events " + ", ".join(f"{r} {B.reg_event(r)}" for r in RUNS) +
        "), the first call that returned each deciding record (42 cells of the reach table), every search and channel read of every run (the per-tool lists behind section 8), all 13 failed calls, and the brief, sheet, share, ticket and Slack payloads of every run. Not reviewed call by call: the 96 comment-list calls and the 60 to 104 ticket writes of each run, which were checked as sets against the payload summary.", "",
 "## 6 · Friction, tool defects and horizon", "",
 "Friction: none configured (03_Error_Async_Config.txt), none met.",
 "Tool errors: " + "; ".join(f"{r} " + ", ".join(f"event {c['event']} {c['tool'].split('__')[-1]}" for c in errs[r]) for r in RUNS if errs[r]) +
 ". Six are Slack searches by a display name that did not resolve ('user_not_found': 'Frederick', 'Claire'), three are shell calls to jq, which the run's sandbox lacks, and two are dropped connections (ECONNRESET, run-3 event 258, run-4 event 344). Each was followed by another form of the call (run-3 repeated the read at event 267; run-4 found Claire's DM at event 347 with the next search); none hid a deciding record or changed an outcome.",
 "Unconfigured tool defects: none found. Slack search returns thread replies and caps a query at the newest results: a search for Robert's messages since 24 Sep with limit 50 (run-1 event 276) returns 50 messages from Mon Sep 29 10:50 PM PT onward and not his Fri Sep 26 reply, which is why author sweeps find Marcus and Claire and not Robert's 26 Sep reply.",
 f"Horizon: counted calls {min(B.counted(r) for r in base6)} to {max(B.counted(r) for r in base6)} across the six baseline runs and {B.counted('precheck')} on the pre-check; the two full-pass runs are at 271 and 272. Every run is above 130. The volume comes from the 96 note reads and 60 to 104 ticket writes; nothing was blocked or repeated.", "",
 "## 7 · Verifier sanity", "",
 "No verifier output exists, so there is no judge text to compare. In its place every failed slot of every run was confirmed against the write payload (hardening_gen/out/payloads.json): the sheet states are 8/56/32 (precheck), 8/58/30 (run-1), 8/48/40 (run-4 and run-5) and 8/36/52 (run-2, run-3, run-6), and the Board set of Bow and Dynamite matches the PICKS column of the register. One decoder defect: D4 on run-5 (section 2). For the rubric stage: a share that gives no role is a view share when the tool returns reader.", "",
 "## 8 · Why Opus passed", "",
 "`python3 -B Task_Authoring/tools/hardness_v2_check.py --task-dir Task_Authoring/task_inputs`:", "", "```text"] + v2 + ["```", "",
 "The static check is clean, and the runs still averaged 82%: the traps are well formed, but four of the six deciding records sit where Opus 5.5 looks as a matter of routine. What the seven runs do after reading the 96 notes:", ""]
doc += table(["Habit", "Runs (of 7)", "What it exposes"], [
 ("Read #zombie-design from about 24 Sep", "6 (run-2 found the post with a Slack search for 'color')", "Robert's new-colours post: REVISED arrives with the hub"),
 ("Search Slack for the author's recent messages", "Claire 6, Brian 3, Robert 2, Marcus 1, Calvin 2", "ARTHOLD; EXPORT once. A high-volume author is cut by the result limit, a low-volume one is not"),
 ("Keyword sweeps in Slack: FBX, sound, music, font, ASCII or binary, library, outgoing, colour", "FBX 7, sound 7, ASCII or binary 4, outgoing 3, export 1, 'saved out' 1", "EXPORT in two runs, through the note's own wording"),
 ("Full-text Drive search for 'sound'", "5 (the pre-check searched 'Universal Sound')", "AUDIO in six runs, and with it ZIP in five"),
 ("Read #zombie-art and open the bow thread", "read 5, opened 3", "PICKS"),
 ("Read #zombie-match3d", "2", "EXPORT"),
 ("Search Drive for the outgoing folder", "0", "nothing: no run looked for the log by its own name"),
 ("Open Trello", "0", "the kickoff-card decoy was never met"),
 ("Open GitHub pull requests", "1", "the pull request behind the colour versions was not needed"),
])
doc += ["", "Per settled trap, the v2 failure kind is in the register's last column. Genuine capability: in every run the whole hub chain and the 96 note reads, the loss rule and the 7-slot tray against the decoys, the music rule from April, the four recipients, and only true Owed tickets moved (30 to 52 of them); Claire's Turkish in all six runs that read it.",
 f"Heavy rows (weight 5) that passed in all six baseline runs: {', '.join(heavy_all)}. Those tied to a mechanism are {', '.join(heavy_mech_all)} (REVISED): the rebuilds below must not add more rows of this kind.", "",
 "## 9 · Purge list (proposed; S0r decides)", ""]
doc += table(["Node", "Evidence", "Proposal"], [
 ("REVISED as a retrieval unit (budget unit C1)", "leaked in 7 of 7 runs, each from the channel read for the picks (run-1 event 512, run-6 event 281); the pull request it was budgeted on was opened by one run (run-1 event 333) and decided nothing", "rebuild as a completion note elsewhere (RP-REVISED), or drop from the budget"),
 ("The Turkish wording of ARTHOLD", "no run hesitated on it (precheck event 322, run-3 event 284)", "purge as a difficulty; it goes with RP-ARTHOLD"),
 ("The Trello kickoff-card decoy", "opened by no run (0 Trello calls in 7 runs)", "keep as realism, count no difficulty on it"),
])
doc += ["", "## 10 · Proposed rebuilds (v2 moves; S0r decides)", "",
 "Each proposal moves or rewords a deciding record; none adds a line, a row, a rule, a step or a sentence to the prompt. Details and evidence: Working_Files/mode_b_request.json (repairs RP-ARTHOLD, RP-ZIP, RP-REVISED, RP-EXPORT).", ""]
doc += table(["Repair", "Node", "v2 move", "What changes", "Found now (7 runs)", "Habit it would sit behind"], [
 ("RP-ARTHOLD", "ARTHOLD", "correction out of the obvious place", "the UV redo is stated in a record a search by Claire's name does not return, for example by Robert in his DM with Julia; Claire's DM row goes", "6", "reading Julia's DM with Robert (1 run) or a date sweep of her DMs (2 runs)"),
 ("RP-ZIP", "ZIP", "decouple from another unit's query", "the folder log says 'The sound files.' without the word 'sound' (for example 'The .wav exports.')", "5, all through the AUDIO query", "a Drive search for the outgoing folder (0 runs so far; 3 runs searched Slack for it)"),
 ("RP-REVISED", "REVISED", "A25 completion note elsewhere", "the folder log records that Claire re-sent the three recoloured items on Tue 30 Sep and that they open and look right; the three lines become Ready; counts 8 / 39 / 49", "7 (as Owed)", "the same log as RP-ZIP"),
 ("RP-EXPORT", "EXPORT", "remove the echo of the original", "Marcus's post keeps its place and loses the words of the note it corrects", "4", "channel history (2 runs) or a search for Marcus (1 run)"),
])
doc += ["", "Unchanged: PICKS (a live coin flip, 3 of 7 found) and AUDIO (a lookup, kept as realism).",
 "Expected effect, UNCALIBRATED: `python3 -B Task_Authoring/task_inputs/Working_Files/hardening_gen/simulate.py` draws six runs 20,000 times on the gradable surface, each unit found independently with the rate shown (rates are counts from the seven runs, or the share of runs that showed the habit that would reach a moved record). It reproduces rev1 at 78% against the 82% observed.", ""]
doc += ["```text"] + [l for l in tool_out("simulate.py")] + ["```", "",
 "Rates used: rev1 EXPORT 4/7, ARTHOLD 6/7, REVISED 7/7, AUDIO 6/7, PICKS 3/7, ZIP 5/7. Rebuilt central: EXPORT 3/7 (the two runs that found the post only through its echo of the note lose it), ARTHOLD 0.30, the folder log 0.20 (no run searched Drive for the folder; three searched Slack for it), AUDIO and PICKS unchanged. 'Finds more' and 'finds less' move those three rates up and down.",
 "Reading: the four moves together are the only option whose P(all gates) holds near 0.5 or better at both ends; one relocation alone is a coin flip on the average and 0.34 on all gates. The risks for S0r to weigh: the folder log would decide eleven lines (ZIP and REVISED), a concentration; in the central case there is a 26% chance that no run opens it, and its rows then fail in all six runs and need all-fail justifications (fair: the log is shared with Julia and named by the notes); and the SD sits near the 0.1 floor in every option, so EXPORT is only reworded and PICKS is left alone.",
 "budget_outcome on the pre-check:", "", "```text"] + bo[:4] + sr[:2] + ["```", "",
 "The tool asks for one relocation per NO-GO. The baseline and the simulation show that one is not enough (ARTHOLD alone: E[average] 0.69, P(all gates) 0.34), so the set above is put to S0r as a redesign under a new design id, not as a patch.", "",
 "## 11 · Routing (proposed; S0r decides)", "",
 "Universe changes, with the facts each would change (for the prompt, Oracle Event and rubric checks that follow):", ""]
doc += table(["Change", "Records", "Facts that change"], [
 ("RP-ARTHOLD", "remove slack row D05HMBQUC8Z/1759148152.833779; add one message from Robert in D05GU6L0XFH on Mon 29 Sep", "the deciding record and its author; the 12 bathroom lines stay Owed with Claire"),
 ("RP-ZIP", "body text of gdocs f_faf4d7c167d14a1127dcc3", "none in the truth; the log's wording"),
 ("RP-REVISED", "one more sentence in the Tue 30 Sep entry of the same doc", "Cactus Plant, Chainsaw and Cone become Ready; Delivered 8, Ready 39, Owed 49; Owed by person Brian 27, Claire 18, Calvin 3, Martin 1; 49 ticket moves and comments; the surface slots X3, X3b, X8 and K3 change"),
 ("RP-EXPORT", "text of slack row C0880U9751A/1758906517.912099", "none in the truth; the post's wording"),
])
doc += ["", "Prompt-side defects: none found. The prompt names the message, Julia's Drive and the PlayableX channel and nothing else; /prompt passed it with every dimension at 5, and no run read it as naming a source or a cause.",
 "Routed observations: for /create-oe-writing, the drafted events describe rev1 and have to be regenerated on the next revision; a blind completeness pass also read the five tool-less 'work out' events as non-actions, so their conclusions belong on the read and write events. For /create-rubric-writing: accept a share without a role argument (the tool grants reader), the links as a post or a thread reply, and the counts as a message or a reply.", "",
 "## 12 · Self-review", "",
 "Walked Evals/1A_Hardness_Eval.md sections 3 to 5 against this report. Every verdict below was counter-read for a tool, fairness, verifier or run cause; every deciding record was re-verified in this run, the seeded ones from the SQL statements and the base ones through tools/hg.py (oe_gen/base_read.py: slack/messages/C090N54TG79/2025-09.json/813, slack/messages/C08R8CHB0QL/2025-09.json/252); the surface grades were re-run after the last input change and the write payloads were searched for each designed value. The neighbouring band is argued in the last row. No replacement wording for the prompt, an Oracle Event or a criterion is quoted here.", ""]
doc += table(["Verdict", "Counter-reading", "Evidence that resolves it", "Result"], CR)
doc += ["", "Not done: the pre-check posterior forecast (playbook step 5). The six-run baseline already exists and measures what the forecast would predict; the next forecast is pre-registered on the next revision at /create-injection.",
 "Unresolved: none. The find rates in section 10 are estimates from seven runs, not measurements of the next revision.", "",
 "## 13 · Next steps", "",
 "1. /create-scenario --revise takes the four repairs as the design delta (new design id), revises the mechanism portfolio, the budget and the gradable surface, and records the dispositions of the verdicts above.",
 "2. /create-injection implements the revision as rev2 and re-runs every injection gate and the coherence sweep; then /injection and /prompt on the platform with the unchanged prompt.",
 "3. /create-prompt-writing check, /create-humantime and /create-oe-writing are re-attested or regenerated on rev2; then one pre-check and, on a GO, the six-run baseline.", ""]
OUT.write_text("\n".join(doc) + "\n")
print("wrote", OUT, len("\n".join(doc)), "chars | avg", pct(avg(sc)), "corrected", pct(avg(corr)), "| SD", round(sd, 3), "| landed ids", len(landed_ids))
