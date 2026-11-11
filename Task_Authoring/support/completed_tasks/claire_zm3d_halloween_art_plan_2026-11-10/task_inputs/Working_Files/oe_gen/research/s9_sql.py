import re
s = open("/Users/sumit/Source/OC/Task_Authoring/task_inputsN2/01_Universe_Inject.sql", encoding="utf8").read()
pats = ["Fri Oct 10","re-recorded 3","ship these","julia on the ad statics","Unity retention restart","end card 001 still","Marketing Video Refresh","vacation","ART-826","ART-831"]
for p in pats:
    print("=== ", p)
    n = 0
    for m in re.finditer(re.escape(p), s, re.I):
        n += 1
        if n > 4: continue
        a = max(0, m.start()-420); b = min(len(s), m.end()+320)
        print(f"[{m.start()}]", s[a:b].replace("\n", " "))
        print()
    print("hits", n)
