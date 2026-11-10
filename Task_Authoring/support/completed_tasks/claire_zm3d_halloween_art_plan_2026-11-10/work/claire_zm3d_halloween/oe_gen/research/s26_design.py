import re
base = "/Users/sumit/Source/OC/Task_Authoring/task_inputsN2/"
for f in ["Working_Files/01_Scenario_Design.md","Working_Files/01a_Hardening_Report.md","Working_Files/prompt_eval/evidence_pack.md"]:
    s = open(base+f, encoding="utf8").read()
    print("=====", f, len(s))
    for p in ["1759211437","zm-animations","company-internal","Marketing Video Refresh"]:
        ms = list(re.finditer(re.escape(p), s))
        print("  --", p, len(ms))
        for m in ms[:2]:
            print("    ", s[max(0,m.start()-260):m.end()+260].replace("\n"," "))
for f in ["08_Oracle_Events.md","10_Baseline_Verifier_Results.md"]:
    s = open(base+f, encoding="utf8").read()
    print("=====", f, len(s)); print(s[:700])
