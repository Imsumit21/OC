#!/usr/bin/env python3
"""Writes Working_Files/01c_Dispositions.json: one written disposition per difficulty_mutation result and trap_liveness flag."""
import json
from pathlib import Path
W = Path(__file__).resolve().parents[1]
live = lambda r: {"disposition": "live", "reason": r}
weak = lambda r: {"disposition": "weak-accepted", "reason": r}
M = {
 "rule:DONE": live("WEAK only because the tool counts VQ_Oakline as an aggregate slot; the rule also moves banked (B_PA, K_r_banked, write slots the tool can't read). Arthur's reply is the only record that says the wire came back"),
 "rule:CORR": live("KILLED: flips A_adv_PB, V12_Tallwater, VQ_Tallwater; the calendar note is the only record of the $40,000"),
 "rule:ALIAS": live("KILLED: flips S_out_PC; the Kestrel post joined through the signature and Contacts is the only route to Withdrawn"),
 "rule:FILT": live("KILLED: flips six slots on Copperleaf and Redwood, and the first pick falls to Sunfold"),
 "rule:EXC": live("KILLED: flips S_out_PD and S_out_PJ, and the first pick goes to Northglow at $126,000"),
 "rule:INPUT": live("KILLED: flips A_com_PE and V12_Sunfold, and the first pick goes to Sunfold at $90,000"),
 "rule:DATE": live("WEAK only because Q4 cash slots are aggregates: flips VQ_Harbor and VQ_Wavecrest, weight 5 each; ESG's note is the only record of Nov 14"),
 "rule:FOLLOW": live("WEAK in the tool's terms: it moves group organic_note, read by the write-content slots W_1, W_2, W_3 and W_count, which the tool can't read"),
 "degrade:done_over": weak("control trial: reads the returned wire onto Tallwater; flips VQ_Tallwater (aggregate) only, which is all a control needs to show"),
 "degrade:corr_over": weak("SURVIVED: Harbor Lane's Advance cell has no slot, its value and Q4 cash don't move. Kept: the operator is live for node_verdicts, and a slot here would add an always-pass row"),
 "degrade:alias_over": live("KILLED: withdrawing Wavecrest flips S_live_PG, V12_Wavecrest, VQ_Wavecrest"),
 "degrade:filt_over": weak("control trial: adding Homa changes the population, read by S_total (register_keys_exact), a delivery slot the tool doesn't flip"),
 "degrade:exc_over": live("KILLED: ruling Sunfold out flips A_com_PE, V12_Sunfold, VQ_Sunfold"),
 "degrade:input_over": weak("control trial: flips V12_Oakline (aggregate) only"),
 "degrade:date_over": weak("control trial: flips VQ_Sunfold (aggregate) only; net 45 from Nov 14 is Dec 29, still in Q4"),
 "degrade:follow_over": weak("control trial: an extra note to Oakline is a write the drafts slots can see; the tool reads group membership only"),
 "degrade:ch_done": live("the channel behind rule DONE: Oakline's $10,000 stays banked, Q4 cash 20,000"),
 "degrade:ch_corr": live("KILLED: Tallwater keeps $60,000"),
 "degrade:ch_alias": live("KILLED: Moonrail stays Live"),
 "degrade:ch_filt1": live("KILLED: Copperleaf never reaches the model"),
 "degrade:ch_filt2": live("KILLED: Redwood never reaches the model"),
 "degrade:ch_exc": live("KILLED: Northglow and Pinegrove stay Live"),
 "degrade:ch_input": live("KILLED: Sunfold keeps 50,000 installs"),
 "degrade:ch_date": live("the channel behind rule DATE: net-60 advances look like Q4 money; flips VQ_Harbor and VQ_Wavecrest"),
 "degrade:ch_follow": live("the channel behind rule FOLLOW: no organic notes are drafted; read by write-content slots"),
 "intervention:rule:DONE": live("load-bearing: dropping Arthur's reply puts the $10,000 back in banked"),
 "intervention:rule:CORR": weak("no-injected-records is a tool limit: difficulty_mutation indexes rows by id, and a gcal row is keyed event_id. Checked by hand: with the event row removed the solver gives Tallwater advance 60000, value 60000, Q4 60000"),
 "intervention:rule:ALIAS": live("load-bearing: dropping the Kestrel post leaves Moonrail Live"),
 "intervention:rule:FILT": live("load-bearing: dropping Robert's reply loses Copperleaf"),
 "intervention:rule:EXC": live("load-bearing: dropping the term sheet removes the offer; the rights text sits in the sheet itself"),
 "intervention:rule:INPUT": live("load-bearing: dropping the card comment puts Sunfold back at 50,000"),
 "intervention:rule:DATE": live("load-bearing: dropping ESG's note puts signing back to Oct 31"),
 "intervention:rule:FOLLOW": live("load-bearing: dropping the standing line removes the notes"),
}
for op in ("done_over", "corr_over", "alias_over", "filt_over", "exc_over", "input_over", "date_over", "follow_over",
           "ch_done", "ch_corr", "ch_alias", "ch_filt1", "ch_filt2", "ch_exc", "ch_input", "ch_date", "ch_follow"):
    M[f"intervention:degrade:{op}"] = weak("no-injected-records is expected: the operator models a run's behaviour, so no single injected row carries it")
L = {"T21:breadcrumb": weak("structural, not a resolver leak: the hub's delegation to the ground rules is the fairness link that makes every rule reachable. T21 is the co-dev decoy; the deciding records for the traps are none of the hub's direct delegations")}
doc = {"mutation": M, "liveness": L, "_note": f"rev2 dispositions (01c): one per difficulty_mutation result ({len(M)}: 8 rules, 17 degrades, 25 interventions) and one per trap_liveness flag ({len(L)})."}
json.dump(doc, open(W / "01c_Dispositions.json", "w"), indent=1, ensure_ascii=False)
print(doc["_note"])
