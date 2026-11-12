#!/usr/bin/env python3
"""Write Working_Files/01c_Dispositions.json: a written disposition for every mutation result, intervention and liveness flag
(playbook S5b, S5c). The verdicts quoted are the tools' own (out/mutation.txt, out/trap_liveness_sql.txt)."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
sys.path.insert(0, str(HERE))
import design_model as M
S, B, PT = M.SEED, M.BASE, M.PACK_TICKET
def d(disp, reason): return {"disposition": disp, "reason": reason}
mut = {
 "rule:EXPORT": d("live", f"KILLED: ablating EXPORT flips X1, X1b and X16 (Refrigerator and Retro TV state, Refrigerator owner) and the write-content X6, W4, K1; the solver reads 'the text kind' from Marcus's post row ({S['a1_post']['id']})"),
 "rule:ARTHOLD": d("live", f"KILLED: ablating ARTHOLD flips X2, X2b, X11, X11b (Bathtub and Iron state and owner) and X7, K2; the solver reads the bathroom sentence from Robert's note row ({S['a2_dm']['id']})"),
 "rule:REVISED": d("live", f"KILLED: ablating REVISED flips X3, X3b and X8 (Cactus Plant, Cone and Chainsaw state) from Ready to Owed and both counts; the solver reads 'the cone again with the new colours' from Brian's log of the outgoing folder ({S['c4_log']['id']})"),
 "rule:AUDIO": d("live", f"KILLED: ablating AUDIO flips X5 and X12 (Rocket sound state and owner) and X10, K5, B6; the solver reads the 'no' cells of Calvin's grid ({S['c2_sheet']['id']})"),
 "rule:PICKS": d("live", f"KILLED: ablating PICKS flips X13 and X14 (Bow and Dynamite board set) and B1; the solver reads 'in place of the last one on my list' from Robert's reply row ({S['c3_reply']['id']})"),
 "rule:ZIP": d("live", f"KILLED: ablating ZIP flips X4 and X17 (Cello state and owner) and X9, K4; the solver reads \"won't unpack\" from Brian's log of the outgoing folder ({S['c4_log']['id']})"),
 "degrade:export_over": d("live", "KILLED: over-applying EXPORT to its control flips C1 (Rolling Pin state), a sampled control row, and both counts"),
 "degrade:art_over": d("weak-accepted", "WEAK: the control Desk Lamp is not a sampled row, so over-application shows only in the Owed and Ready counts (A1, A2). Accepted: the state_join group already holds five samples (two joins, a REVISED-free control, a self-stated Owed line and Rolling Pin); the counts catch it"),
 "degrade:revised_over": d("live", "KILLED: over-applying the re-send to Fly Zapper (a line waiting on Claire's FBX) flips C2 (Fly Zapper state), a sampled control row, and both counts"),
 "degrade:audio_over": d("weak-accepted", "WEAK: the control Success sound is not a sampled row; over-application moves only the counts. Accepted: B6 (the brief's sound section) names only the rocket and explosion cues, and the counts catch a third held cue"),
 "degrade:picks_over": d("live", "KILLED: dropping Grenade from the eight flips C4 (Grenade board set), a sampled control row"),
 "degrade:zip_over": d("weak-accepted", "WEAK: the control Music Keyboard is not a sampled row; over-application moves only the counts. Accepted: its note says Mon 29 Sep and not zipped, and the counts catch it"),
 "degrade:ch_miss": d("live", "KILLED: a missed deciding record leaves the channel's members at their natural reading, which flips every sampled state, owner and board-set row of that rule"),
 "intervention:rule:EXPORT": d("live", f"load-bearing: removing Marcus's post row ({S['a1_post']['id']}) sends the twelve project-saved lines back to Ready"),
 "intervention:rule:ARTHOLD": d("live", f"load-bearing: removing Robert's note row ({S['a2_dm']['id']}) sends the twelve bathroom lines back to Ready"),
 "intervention:rule:REVISED": d("live", f"load-bearing: removing Brian's log ({S['c4_log']['id']}) sends the three recoloured lines back to Owed (Robert's base post stands alone) and, through ZIP, the eight instruments back to Ready"),
 "intervention:rule:AUDIO": d("live", f"load-bearing: removing Calvin's sheet rows ({S['c2_sheet']['id']}) sends the two cues back to Ready"),
 "intervention:rule:PICKS": d("live", f"load-bearing: removing Robert's reply row ({S['c3_reply']['id']}) puts the dynamite back in the eight"),
 "intervention:rule:ZIP": d("live", f"load-bearing: removing Brian's log ({S['c4_log']['id']}) sends the eight instruments back to Ready"),
}
for op in ("export_over", "art_over", "revised_over", "audio_over", "picks_over", "zip_over", "ch_miss"):
    mut[f"intervention:degrade:{op}"] = d("live", "no-injected-records: an over-application or missed-record operator is a way of reading the records, not a record; nothing to remove")
live = {
 "T3:breadcrumb": d("keep the link; no change", f"rev2 makes T3 a three-version supersession (the 25 Sep note, Robert's base post {B['robert_new_colours']}, Brian's log {S['c4_log']['id']}); each later version points back only by what it describes: Robert's post names the three items and their new colours, the log says 'the three recoloured models' and names none, and the notes' rule ('If the art changed ... it goes again') is the incorporation. No record names the log, its title or its owner; path_exposure reports it OFF-PATH, and the REVISED operator (Fly Zapper called Ready) is KILLED on the sampled control"),
 "T4:breadcrumb": d("keep the link; no change", f"the notes ({S['notes']['id']}) carry the sound rule, as they must for incorporation; they do not name Calvin's sheet ({S['c2_sheet']['id']}), its title or its owner, and the sheet's column heads ('OK outside the game', 'Replacement') do not repeat the notes' words"),
 "T5:breadcrumb": d("keep the link; no change", f"the ask ({S['ask']['id']}) says 'unless he's changed them since': it authorises a later change and gives no place, date or word of it; the reply ({S['c3_reply']['id']}) is under a post about an arrow in #zombie-art and names no item"),
 "T7:breadcrumb": d("keep the link; no change", f"the notes' Ready test says 'sitting in the outgoing folder', and every ticket note ends with that folder: that is the fairness link to Brian's log ({S['c4_log']['id']}); the notes name neither the log, its title nor its owner, and path_exposure reports the record OFF-PATH"),
 "T8:breadcrumb": d("keep the link; no change", f"the three start dates are base messages in the channel the ask names ({M.VENDOR_CH}); a realism trap with no budget weight"),
 "T13:breadcrumb": d("keep the link; no change", f"base distractor on the read path ({B['julia_shuriken_idea']}, answered by {B['robert_remain']}); no budget weight"),
 "T14:breadcrumb": d("keep the link; no change", f"base distractor: Frederick's three items ({B['fred_scenario1']}) and the reference level; Robert's 25 Sep post names the eight; no budget weight"),
 "T15:breadcrumb": d("keep the link; no change", f"the notes send the reader to Julia's deck ({S['deck']['id']}) for what was built; the deck is the older state of the board and carries no budget weight by itself (PICKS decides the eight)"),
 "T16:breadcrumb": d("keep the link; no change", f"base aliases in the hub channel ('the duck asset' {B['vendor_duck']}, the rocket launcher {B['vendor_asset_list']}); resolved by base ({B['brian_zip2']}); no budget weight"),
 "T16:order": d("keep the link; no change", "the vendor's wording is met before Brian's list by anyone who reads the channel first; the list's Plushie Chick and Cannon lines settle both aliases"),
 "T17:breadcrumb": d("keep the link; no change", f"base lookalike ({B['playable_feedback_doc']}, the first playable); the ask names 'My hand-off notes' and the decoy carries no budget weight"),
}
out = {"mutation": mut, "geometry": {}, "liveness": live}
(WF / "01c_Dispositions.json").write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")
print("dispositions: mutation", len(mut), "liveness", len(live))
