#!/usr/bin/env python3
"""rev2 edit of oe_gen/assemble_ledger.py: counts from the model, Robert's note in place of Claire's Turkish DM, the
re-sent recoloured lines Ready on Brian's log, the pull request off the path, the purpose both fair, the vendor's 25 Sep
complaint as a trap on the Plushie Chick line. Idempotent: a passage already replaced is skipped."""
from pathlib import Path
P = Path(__file__).resolve().parent / "assemble_ledger.py"
s = P.read_text()
E = [
 ('''ABSENCE = (f"The 44 Delivered and Ready line names searched in every Slack container Julia can open, from Wed Sep 24 2025 (the first zip) to the clock: {n_hits} hits, "''',
  '''RS = ab["resent"]; assert set(RS) == {"Cactus Plant", "Chainsaw", "Cone"} and all(v["complete"] and v["since"] == 0 for v in RS.values()), RS
ABSENCE = (f"The 44 Delivered and Ready lines that no later record touches (every Delivered or Ready line but Cactus Plant, Chainsaw and Cone) searched by name in every Slack container Julia can open, from Wed Sep 24 2025 (the first zip) to the clock: {n_hits} hits, "'''),
 ('''           f"(Robert's eight and Julia's deck).")''',
  '''           f"(Robert's eight and Julia's deck). Cactus Plant, Chainsaw and Cone: Robert's new colour versions ({O.base('robert_new_colours')['id']}, {d(O.base('robert_new_colours')['id'])}) are "
           f"followed by Brian's log {O.LOG_ID}, whose Tue Sep 30 entry records them sent again; the same search from Tue Sep 30 to the clock finds no message naming any of the three "
           f"(0 hits each, result lists complete).")'''),
 ('''("R5", "Move each Owed line's ticket to Todo (52 tickets)",''', '''("R5", f"Move each Owed line's ticket to Todo ({O.COUNTS['Owed']} tickets)",'''),
 ('''  "linear_update_issue (exists)", "id (state carries the move)", f"the 52 tickets of {F('owed')}; status {F('todo')}", "each of the 52 tickets is in Todo; the 44 Delivered and Ready tickets and DES-313 keep their state",
  "the state Todo, nothing else", DEFER + f"no record holds the ticket moves; Claire's note in {O.A2['id']} that she will write on the tickets when the UVs are done is her own later comment, not a hold; "
  f"the notes {O.NOTES_ID} (last version, modified Tue Sep 30) govern the tickets", "yes"),''',
  '''  "linear_update_issue (exists)", "id (state carries the move)", f"the {O.COUNTS['Owed']} tickets of {F('owed')}; status {F('todo')}",
  f"each of the {O.COUNTS['Owed']} tickets is in Todo; the {O.COUNTS['Delivered'] + O.COUNTS['Ready']} Delivered and Ready tickets and DES-313 keep their state",
  "the state Todo, nothing else", DEFER + f"no record holds the ticket moves; the notes {O.NOTES_ID} (last version, modified Tue Sep 30) govern the tickets", "yes"),'''),
 ('''("R5", "Comment on each Owed line's ticket (52 comments)",''', '''("R5", f"Comment on each Owed line's ticket ({O.COUNTS['Owed']} comments)",'''),
 ('''  "linear_create_comment (exists)", "issueId, body", f"the 52 tickets of {F('owed')}", "each of the 52 tickets carries a new comment by Julia", "what is owed and who has it",''',
  '''  "linear_create_comment (exists)", "issueId, body", f"the {O.COUNTS['Owed']} tickets of {F('owed')}", f"each of the {O.COUNTS['Owed']} tickets carries a new comment by Julia", "what is owed and who has it",'''),
 ('''  "Delivered 8, Ready 36, Owed 52", DEFER + "no record holds the reply; the ask is the only version of the request", "yes"),''',
  '''  f"Delivered {O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, Owed {O.COUNTS['Owed']}", DEFER + "no record holds the reply; the ask is the only version of the request", "yes"),'''),
 ('''  f"{O.A1['id']}, Marcus, the day after the notes: 'the text kind'; {O.base('vendor_formats')['id']}: 'Binary format, not ASCII'"),''',
  '''  f"{O.A1['id']}, Marcus, the day after the notes, to Brian: 'the text kind ... youll need to redo them'; {O.base('vendor_formats')['id']}: 'Binary format, not ASCII'"),'''),
 ('''("T3", f"Brian's note on the 12 bathroom files from Claire ({line_ids('A2')})", F("owed"), f"{O.A2['id']}, Claire, Mon Sep 29, in Turkish: Friday's bathroom files are the old state"),''',
  '''("T3", f"Brian's note on the 12 bathroom files from Claire ({line_ids('A2')})", F("owed"), f"{O.A2['id']}, Robert to Julia, Mon Sep 29: Claire is redoing the UVs on the bathroom objects and the files she gave Brian on Friday are the old version"),'''),
 ('''("T5", f"Brian's note 'first thing' on Chainsaw, Cone and Cactus Plant ({line_ids('C1')})", F("owed"), f"{O.base('robert_new_colours')['id']}, Robert, Mon Sep 29: new colour versions; one of the three is in the eight"),''',
  '''("T5", f"Robert's new colour versions of Chainsaw, Cone and Cactus Plant ({O.base('robert_new_colours')['id']}, Mon Sep 29) make their 'first thing' notes look out of date ({line_ids('C1')})", F("ready"),
  f"{O.LOG_ID}, Brian's log, Tue Sep 30, the latest record: 'Claire sent the three recoloured models again. Opened them, they look right, and they replace Thursday's.'; only Robert's post says which three"),'''),
 ('''"36 of the 88 are Ready and 52 are Owed; the workflow state decides neither"),''',
  '''f"{O.COUNTS['Ready']} of the 88 are Ready and {O.COUNTS['Owed']} are Owed; the workflow state decides neither"),'''),
 ('''"known base issue SC-58: the zombies come from Robert's post and the loss rule from the core mechanic; kept off every Expected line"),
]''',
  '''"known base issue SC-58: the zombies come from Robert's post and the loss rule from the core mechanic; kept off every Expected line"),
 ("T18", f"PlayableX's complaint of Thu Sep 25 about the second zip ({O.base('vendor_blank_scene')['id']}) reads as the chick inside it being unusable", FL("Plushie Chick"),
  "the message names 'the zombie assets' and the package's prefabs; Brian's note on DES-334, written after it, says the problem was the zombie package, not the chick; PlayableX's later 'We have reviewed the assets.' raises only the zombies"),
]'''),
 ('''("8", "The pull request is a second record for the three recoloured items; no event needs it", F("pr462"), "none", "none"),''',
  '''("8", "What the scenario is for has two fair wordings: Frederick's of Sep 12 and the team's of Sep 22 in #zombie-design (coherence sweep fork F30, both fair)", F("purpose"), "rubric (accept both)", "rubric stage"),'''),
 ('''"holds (52 moves, 52 comments)"''', '''f"holds ({O.COUNTS['Owed']} moves, {O.COUNTS['Owed']} comments)"'''),
 ('''"holds (8, 36, 52 in the DM)"''', '''f"holds ({O.COUNTS['Delivered']}, {O.COUNTS['Ready']}, {O.COUNTS['Owed']} in the DM)"'''),
 ('''doc += [f"# 08 OE Writing Ledger — julia-zm3d-playable-brief (injection rev1)",''', '''doc += [f"# 08 OE Writing Ledger — julia-zm3d-playable-brief (injection {O.M.REV})",'''),
 ('''01_Universe_Inject.sql — present (rev1, sha256 {sha(O.SQL_PATH)}; "
        f"the platform ran the same statements without the four header comment lines, sha256 3a76797fbde1) · ''',
  '''01_Universe_Inject.sql — present ({O.M.REV}, sha256 {sha(O.SQL_PATH)}; "
        f"the platform runs the same statements without the four header comment lines) · '''),
 ('''eval_reports: /injection PASS, /prompt PASS, /hardness NON-FAIL on the pre-check run (routes and tool names only)", "",''',
  '''eval_reports: rev1 only (/injection PASS, /prompt PASS, /hardness NON-FAIL); the six rev2 baseline runs in "
        f"07_Baseline_Trajectories-2 (routes and tool names only)", "",'''),
 ('''asserted them equal to solver/truth.json (Delivered 8, Ready 36, Owed 52; Brian 27, Claire 21, "
        "Calvin 3, Martin 1). No-event-text scan''',
  '''asserted them equal to solver/truth.json (Delivered {O.COUNTS['Delivered']}, Ready {O.COUNTS['Ready']}, "
        f"Owed {O.COUNTS['Owed']}; " + ", ".join(f"{w} {n}" for w, n in O.WHO_COUNTS.items()) + "). No-event-text scan'''),
 ('''rests on a search of all 44 names with complete result lists and two positive controls (oe_gen/out/absence_check.json).", "",
        "Unresolved: none blocking. Open risks 1, 2, 5, 6 and 9 go to the rubric stage; 3 and 4 are kept off every Expected line.", ""]''',
  '''rests on a search of all 44 untouched names and of the three re-sent ones since the log's entry, with complete result lists and "
        "two positive controls (oe_gen/out/absence_check.json).", "",
        "Unresolved: none blocking. Open risks 1, 2, 5, 6, 8 and 9 go to the rubric stage; 3 and 4 are kept off every Expected line.", ""]'''),
]
done, skipped, missing = 0, 0, []
for a, b in E:
    if s.count(a) == 1:
        s = s.replace(a, b); done += 1
    elif b.split("\n")[0] in s:
        skipped += 1
    else:
        missing.append(a[:90])
P.write_text(s)
left = [w for w in ("pr462", "Turkish", "52 tickets", "Ready 36", "36 of the 88", "(injection rev1)") if w in s]
print(f"applied {done}, already {skipped}, missing {missing}; rev1 leftovers {left}")
