"""rev7 written dispositions for every mutation result, channel degrade and intervention (01c_Dispositions.json)
plus the flat mutation file the mutate CLI takes. Liveness and v2 sections are filled from their rev7 runs."""
import json, pathlib
WF = pathlib.Path('Task_Authoring/task_inputs/Working_Files')
P = WF / '01c_Dispositions.json'
old = json.loads(P.read_text(encoding='utf-8'))

L = 'live'; W = 'weak-accepted'
mut = {
 "rule:R_K1": (L, "ablation flips the 13 sessions of Claire's gathering back to counted (S-K1a on the solver view, S-G1); the text slots it also moves (S-K1b, S-H1, S-G2, S-DEC, S-BRIAN, S-ST1, S-ST2) are not read by the tool."),
 "rule:R_K3": (L, "ablation drops the 13 Samsung sessions (S-K3a, S-K3b, S-G1); two-sided in rev7: the natural reading now excludes, the matrix includes."),
 "rule:R_K4": (L, "ablation flips Brian's 9 sessions back to counted (S-K4a, S-G1)."),
 "rule:R_K5": (L, "ablation flips the 13 build-1943 sessions back to counted (S-K5a, S-G1)."),
 "rule:R_G": (L, "ablation flips ZOM-598 and ZOM-622 back to counted (S-Ga, S-Gb, S-G1)."),
 "rule:R_T": (W, "WEAK on the solver view: the two late sessions have no ticket key the register can be keyed on in advance, so the tool sees only S-G1; their declared slots S-Ta and S-Tb (weight 5 each, text on linear_create_issue) are write-content slots the tool does not read."),
 "rule:R_F": (W, "SURVIVED: moves the rerun field on 13 sessions and no solver-read slot; its only effect is the declared 3-weight text slot S-F1. Side channel, weight not raised."),
 "rule:R_D": (W, "SURVIVED: moves panel_mean 3.33 to 3.1; only the 3-weight text slot S-D1 reads it. Context value by design."),
 "rule:R_E": (W, "SURVIVED: moves retention_d7 10.47 to 9.09; only the 3-weight text slot S-E1 reads it. Context value by design."),
 "degrade:over:K1_all_sessions_that_day": (L, "over-application to the other Sep 26 sessions; flips the control S-O2 and S-G1."),
 "degrade:over:K3_all_android": (L, "over-application of the device gate to every non-iPhone session; flips S-O1 (ZOM-643, Pixel 8a) and S-G1; in rev7 it also flips S-K3a/S-K3b."),
 "degrade:over:K4_any_group_nickname": (W, "WEAK: moves ZOM-626/627 and only S-G1 reads them (at most 5 samples per group); the count still catches it."),
 "degrade:over:K5_all_android": (L, "over-application of the store-builds clause to every Android build; flips S-O1, S-K3a, S-K3b and S-G1."),
 "degrade:over:G_any_tech_job": (W, "WEAK: moves ZOM-590 and ZOM-633 (non-games technical-sounding jobs) and only S-G1 reads them; the count catches it."),
 "degrade:over:F_rerun_all_notcounted": (W, "SURVIVED: re-run notes on every not-counted ticket; only the presence slot S-F1 reads the notes, by design."),
 "degrade:slip:verdict": (L, "the scale channel: one wrong row moves direct verdict slots and S-G1."),
}
for r in ("R_K1", "R_K4", "R_K5", "R_G", "R_T", "R_F", "R_D", "R_E"):
    mut["intervention:rule:" + r] = (L, "load-bearing: removing the rule's deciding records changes only keys in its own closure.")
mut["intervention:rule:R_K3"] = (L, "escaped, declared coupling: the deciding set includes the gate Doc f_748d26e760e54651eaa0d8, which also carries the store-builds clause (H-GATE governs R2 and R3 in the manifest), so removing it moves the build-1943 sessions too; the matrix records alone stay in R_K3's closure.")
for op in ("over:K1_all_sessions_that_day", "over:K3_all_android", "over:K4_any_group_nickname", "over:K5_all_android",
           "over:G_any_tech_job", "over:F_rerun_all_notcounted", "slip:verdict"):
    mut["intervention:degrade:" + op] = (L, "no-injected-records is expected: a degrade is a reading error, not a record; inert by design.")
flat = {k: {"disposition": d, "reason": r} for k, (d, r) in mut.items()}
(WF / 'plan' / 'out_rev7' / 'mut_disp.json').write_text(json.dumps(flat, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
new = dict(old)
new['mutation'] = flat
new['geometry'] = old.get('geometry') or {}
new['geometry']['L_max'] = {"disposition": "weak-accepted", "reason": "L_max UNSUPPORTED (9 mechanisms, exact combinations only); U 96/98 PASS is the blocking bound. Advisory, UNCALIBRATED."}
lv = pathlib.Path(WF / 'plan' / 'out_rev7' / 'live_disp.json')
if lv.is_file():
    new['liveness'] = json.loads(lv.read_text(encoding='utf-8'))
v2 = pathlib.Path(WF / 'plan' / 'out_rev7' / 'v2_disp.json')
if v2.is_file():
    new['hardness_v2'] = json.loads(v2.read_text(encoding='utf-8'))
P.write_text(json.dumps(new, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(len(flat), 'mutation dispositions;', list(new))
