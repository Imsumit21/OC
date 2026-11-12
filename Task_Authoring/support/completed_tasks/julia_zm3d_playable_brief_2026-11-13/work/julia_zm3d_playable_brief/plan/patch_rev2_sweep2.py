#!/usr/bin/env python3
"""rev2 coherence sweep, round 2 (reviewer-1's re-review of SQL c6834f64...). Idempotent; prints what was applied.
  * C12 / F2: the Plushie Chick note quoted the vendor's 25 Sep 13:50 UTC message but was stamped 07:27 UTC that morning.
    The note is now written at 14:06 UTC, after that message ('their message today'), and the ticket closes after it,
    as for the Zombie characters line, whose note follows the vendor's 29 Sep message.
  * F9: after 'the setting was wrong that day' the post no longer said who redoes the twelve; Marcus now tells Brian
    ('so youll need to redo them'). No word of the note it corrects and no vendor word ('binary', 'fbx', 'export')."""
from pathlib import Path
HERE = Path(__file__).resolve().parent
EDITS = {
 "design_model.py": [
  ('"Went in the second zip on 24 Sep (the one they called the duck). What they said was wrong with that zip the next day was the zombie package, not the chick."',
   '"Went in the second zip on 24 Sep (the one they called the duck). Their message today about that zip is the zombie package, not the chick."')],
 "build_spec.py": [
  ('''    if n == "Zombie characters": return "2025-09-29T10:21:17Z"      # after the vendor's 10:16 UTC message of 29 Sep that it had reviewed the pack''',
   '''    if n == "Zombie characters": return "2025-09-29T10:21:17Z"      # after the vendor's 10:16 UTC message of 29 Sep that it had reviewed the pack
    if n == "Plushie Chick": return "2025-09-25T14:06:41Z"          # after the vendor's 13:50 UTC message of 25 Sep about the zombie package''')],
 "planned_texts.py": [
  ('''"<@EMPLOYEE_0026_SLACK_ID> fyi the models you got out of unity on thursday are the text kind, the setting was "
           "wrong that day. they open fine in unity and in max so you wouldnt notice. the ones from "''',
   '''"<@EMPLOYEE_0026_SLACK_ID> fyi the models you got out of unity on thursday are the text kind, the setting was "
           "wrong that day so youll need to redo them. they open fine in unity and in max so you wouldnt notice. the ones from "''')],
 "build_findings_map.py": [
  ('''reading_b=rd("Marcus's later post: the models Brian got out of Unity on Thursday are the text kind (the setting was wrong that day); the vendor takes binary FBX only", "Owed: export again as binary, Brian"),''',
   '''reading_b=rd("Marcus's later post: the models Brian got out of Unity on Thursday are the text kind (the setting was wrong that day) and Brian will need to redo them; the vendor takes binary FBX only", "Owed: export again as binary, Brian"),'''),
  ('''how="Marcus's post in #zombie-match3d, dated after the twelve notes, with the vendor's base format rule"),''',
   '''how="Marcus's post in #zombie-match3d, dated after the twelve notes and addressed to Brian ('youll need to redo them'), with the vendor's base format rule"),'''),
  ('''how="the Plushie Chick's note names the vendor's word for it and now says the complaint about that zip was the zombie package, not the chick;''',
   '''how="the Plushie Chick's note, written at 14:06 UTC on 25 Sep after the vendor's 13:50 UTC message, names the vendor's word for it and says that message is about the zombie package, not the chick;'''),
 ],
}
for name, pairs in EDITS.items():
    p = HERE / name; s = p.read_text(); done, skipped, missing = 0, 0, []
    for a, b in pairs:
        if s.count(a) == 1:
            s = s.replace(a, b); done += 1
        elif b in s:
            skipped += 1
        else:
            missing.append(a[:90])
    p.write_text(s)
    print(f"{name}: applied {done}, already {skipped}, missing {missing}")
