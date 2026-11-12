#!/usr/bin/env python3
"""rev2 coherence fix F2 (reviewer 2, round 1 of rev2): Marcus's post said 'thats the default if you dont change the
setting', which lets a reader carry the text-kind problem back to the 24 Sep zip. The post now scopes it to Thursday
('the setting was wrong that day'); every generator that quoted the old wording follows. Idempotent."""
from pathlib import Path
HERE = Path(__file__).resolve().parent
OLD_POST = ('"<@EMPLOYEE_0026_SLACK_ID> fyi the models you got out of unity on thursday are the text kind, thats the default "\n'
            '           "if you dont change the setting. they open fine in unity and in max so you wouldnt notice. the ones from "')
NEW_POST = ('"<@EMPLOYEE_0026_SLACK_ID> fyi the models you got out of unity on thursday are the text kind, the setting was "\n'
            '           "wrong that day. they open fine in unity and in max so you wouldnt notice. the ones from "')
EDITS = {
 "planned_texts.py": [(OLD_POST, NEW_POST)],
 "review_content.py": [("are the text kind, the default if the setting is not changed, which open fine",
                        "are the text kind (the setting was wrong that day), which open fine")],
 "build_manifest.py": [("are the text kind, the exporter's default; Claire's are fine", "are the text kind, the setting was wrong that day; Claire's are fine"),
                       ("those files are the text kind (the exporter's default)", "those files are the text kind (the setting was wrong that day)")],
 "design_model.py": [("are the text kind (exporter default); Claire's are fine", "are the text kind (the setting was wrong that day); Claire's are fine")],
 "literal_sweep.py": [('"change_the_setting": "change the setting"', '"setting_wrong": "the setting was wrong that day"')],
 "build_findings_map.py": [("are the text kind (the default setting); the vendor", "are the text kind (the setting was wrong that day); the vendor")],
 "assemble_design.py": [("(D3: 'got out of unity', 'the default if you dont change the setting')",
                         "(D3: 'got out of unity'; rev2 sweep: 'the setting was wrong that day', so the 24 Sep zip is not drawn in)")],
}
for name, pairs in EDITS.items():
    p = HERE / name; s = p.read_text(); done, skipped, missing = 0, 0, []
    for a, b in pairs:
        if s.count(a) == 1:
            s = s.replace(a, b); done += 1
        elif b in s:
            skipped += 1
        else:
            missing.append(a[:80])
    p.write_text(s)
    print(f"{name}: applied {done}, already {skipped}, missing {missing}")
