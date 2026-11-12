#!/usr/bin/env python3
"""persona_view can-see for every load-bearing scoped base record; writes out/reach_table.md (design section 10)."""
import subprocess, sys, os, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import design_model as M
ROOT = "/Users/sumitkumar/Source/Outlier/OC"
os.environ["TASK_AUTHORING_TASK_DIR"] = ROOT + "/Task_Authoring/task_inputs"
B = M.BASE
rows = [("slack", B[k], why) for k, why in (
    ("vendor_asset_list", "what PlayableX expects, by group (K4)"), ("vendor_formats", "formats; the 8-item set and extra items (K12)"),
    ("vendor_zombie_ask", "the question Robert's zombie picks answer (K10)"), ("vendor_duck", "the 'duck asset' (T16)"),
    ("brian_zip1", "the 24 Sep zip (T3 older version)"), ("brian_zip2", "the plushie zip the same day (T16)"),
    ("brian_pack3", "the full zombie pack, 26 Sep (T10)"), ("brian_winfail", "win and fail as told to PlayableX (R5)"),
    ("vendor_blank_scene", "the 25 Sep complaint and the blank-scene request (T10, C4)"), ("fred_scenario1", "Scenario 1 chosen (R5, T18)"),
    ("fred_pause", "the pause"), ("vendor_nov3", "start 3 November (K14)"), ("vendor_oct6", "start 6 October (T8 older version)"),
    ("vendor_music_rule", "music starts after the first click (K13)"), ("vendor_fbx_march", "the March FBX rule (T12)"),
    ("julia_dd_brief", "Julia's brief for the first playable (role remit)"), ("brian_asks_level", "Brian asks Julia for the reference level (role remit)"),
    ("julia_shuriken_idea", "Julia's own idea (T13)"), ("robert_remain", "Robert: remain as is (T13)"),
    ("robert_new_colours", "new coloured cactus, chainsaw and cones, 29 Sep (C1)"),
    ("art_cactus", "Robert asks for a recoloured cactus plant (C1)"), ("art_candy", "Candy texture issue (C1)"), ("art_cone", "recoloured cone (C1)"),
    ("art_dart", "dartboard colour (C1)"), ("art_claire_pr", "Claire pushed the changes (C1)"), ("art_bow_root", "Julia's bow post, parent of Robert's reply (C3)"))]
rows += [("slack", M.DM_FRED, "the DM the ask and the reply sit in"), ("slack", M.DM_CLAIRE, "the DM Claire's message sits in"),
         ("slack", M.BUGS_CH, "the channel Arthur's post sits in"), ("slack", "C09A7PDFYCV", "the sound channel (decoy for the source sheet)"),
         ("gdocs", B["playable_feedback_doc"], "Leonard's Playable Feedback (H1 decoy, T17)"), ("gdrive", B["julia_root"], "destination of both deliverables")]
out = ["| Service | Record | Verdict | Why it is load-bearing |", "|---|---|---|---|"]
bad = 0
for svc, rid, why in rows:
    r = subprocess.run(["python3", ROOT + "/Task_Authoring/tools/persona_view.py", "can-see", "julia_lawson", svc, rid], capture_output=True, text=True, cwd=ROOT)
    m = re.search(r": (YES|NO|UNVERIFIED)", r.stdout); v = m.group(1) if m else "?"
    bad += v != "YES"
    out.append(f"| {svc} | `{rid}` LB | {v} | {why} |")
for svc, rid, why in (("github", B["pr462"], "the 25 Sep art change (C1)"), ("confluence", B["gdd"], "tray size and how a level is lost (K6, T9)"),
                      ("trello", B["trello_kickoff"], "Leonard's card (H3 decoy, T11)"), ("trello", B["trello_playables"], "UA/BD card, Not Started (T14)")):
    out.append(f"| {svc} | `{rid}` LB | YES (unscoped service) | {why} |")
Path(__file__).resolve().parent.joinpath("out", "reach_table.md").write_text("\n".join(out) + "\n")
print(len(rows), "scoped rows, not YES:", bad)
