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
    ("vendor_scenarios", "the four scenarios as the vendor described them (R5)"), ("fred_retention", "what Scenario 1 is for (K15)"),
    ("fred_scenario1", "Scenario 1 chosen; grenade, couch, plush doll 'a good start' (K15, T14)"),
    ("vendor_formats", "formats (binary fbx), the 8-item set and editable extras (K5, C1)"), ("vendor_asset_list", "what PlayableX expects, by group (H2 decoy, T16)"),
    ("vendor_oct6", "start 6 October (T8 older version)"), ("brian_zip1", "the first zip, 24 Sep (Delivered lines)"),
    ("brian_winfail", "win and fail as told to PlayableX (R5)"), ("brian_later", "more items later on (the extras)"),
    ("vendor_duck", "the 'duck asset' (T16)"), ("brian_zip2", "the plushie zip the same day (T16)"),
    ("vendor_blank_scene", "the 25 Sep complaint about the zombie package (T10)"), ("brian_pack3", "the zombie pack, 26 Sep (T10)"),
    ("vendor_zombie_ask", "the question Robert's zombie picks answer (K10, T10)"), ("fred_pause", "the pause"), ("vendor_nov3", "start 3 November (K13)"),
    ("vendor_music_rule", "music starts after the first click (K12)"), ("vendor_fbx_march", "the March FBX rule (T12)"),
    ("julia_dd_brief", "Julia's brief for the first playable (role remit)"), ("vendor_thanks_brief", "the vendor's thanks for that brief (role remit)"),
    ("fred_asks_julia", "Frederick relays the vendor's formats to Julia, 18 Sep (C1 fairness)"), ("brian_asks_level", "Brian asks Julia for the reference level (role remit)"),
    ("julia_shuriken_idea", "Julia's own idea (T13)"), ("robert_remain", "Robert: remain as is (T13)"),
    ("brian_robert_ok", "Robert was fine with Frederick's items for the reference level (T14)"), ("julia_level", "Julia builds the grenade, couch, plushie level (T14, deck)"),
    ("robert_new_colours", "new coloured cactus, chainsaw and cones, 29 Sep (C3 chain, T3)"), ("art_cactus", "Robert asks for a recoloured cactus plant (T3)"),
    ("art_cone", "recoloured cone (T3)"), ("art_claire_pr", "Claire pushed the changes (T3)"), ("art_bow_root", "Julia's bow post, parent of Robert's reply (K11, K14)"),
    ("art_bounce", "the bounce items thread of 2 Sep (T6)"), ("anim_zombies", "the nine zombies of the pack (zombie picks)"),
    ("anim_pack", "Marcus's zombie pack, tested in an empty project (T10)"), ("robert_copyright", "two sounds to be swapped for copyright (sound sheet's origin)"))]
rows += [("slack", M.DM_FRED, "the DM the ask and the reply sit in"), ("slack", M.DM_CLAIRE, "the DM Claire's message sits in"),
         ("slack", M.MATCH3D_CH, "the channel Marcus's post sits in"), ("slack", M.VENDOR_CH, "the PlayableX channel (anchor A2, the links)"),
         ("gdocs", B["playable_feedback_doc"], "Leonard's Playable Feedback (H1 decoy, T17)"), ("gdrive", B["julia_root"], "destination of both deliverables")]
out = ["| Service | Record | Verdict | Why it is load-bearing |", "|---|---|---|---|"]
bad = 0
for svc, rid, why in rows:
    r = subprocess.run(["python3", ROOT + "/Task_Authoring/tools/persona_view.py", "can-see", "julia_lawson", svc, rid], capture_output=True, text=True, cwd=ROOT)
    m = re.search(r": (YES|NO|UNVERIFIED)", r.stdout); v = m.group(1) if m else "?"
    bad += v != "YES"
    out.append(f"| {svc} | `{rid}` LB | {v} | {why} |")
for svc, rid, why in (("github", B["pr462"], "the 25 Sep model change and its comment (C1 unit)"), ("github", B["pr460"], "new objects, merged after the first zip (T18)"),
                      ("confluence", B["gdd"], "tray size and how a level is lost (K6, T9)"), ("linear", B["zom97"], "the object revision tickets (T19)"),
                      ("trello", B["trello_kickoff"], "Leonard's card (H3 decoy, T11)")):
    out.append(f"| {svc} | `{rid}` LB | YES (unscoped service) | {why} |")
Path(__file__).resolve().parent.joinpath("out", "reach_table.md").write_text("\n".join(out) + "\n")
print(len(rows), "scoped rows, not YES:", bad)
