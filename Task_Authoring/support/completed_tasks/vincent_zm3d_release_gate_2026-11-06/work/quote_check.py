import json, re, html
WS = "/Users/sumitkumar/Source/Outlier/OC"
U = WS + "/Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data"
rub = json.load(open(WS + "/Task_Authoring/task_inputs/09_Rubrics.json"))
sql = open(WS + "/Task_Authoring/task_inputs/01_Universe_Inject.sql").read().replace("''", "'")
corpus = [sql, open(WS + "/Task_Authoring/task_inputs/04_Prompt.txt").read()]
for f in ["/linear/data.json", "/slack/messages/C05433XK267/2025-09.json", "/slack/messages/D079SNE2TL4/2025-09.json",
          "/confluence/confluence_working.json", "/trello/data.json"]:
    t = open(U + f).read()
    corpus.append(t)
    try:
        corpus.append(json.dumps(json.loads(t), ensure_ascii=False))
    except Exception:
        pass
big = "\n".join(corpus)
big2 = html.unescape(re.sub(r"<[^>]+>", " ", big))
norm = lambda s: re.sub(r"\s+", " ", s.replace("\u2019", "'"))
B = norm(big) + "\n" + norm(big2)
bad = []
nq = 0
for i, r in enumerate(rub, 1):
    for fld in ("title", "justification", "evidence"):
        txt = r[fld]
        # quotes: '...' preceded by space/( and "..." pairs
        qs = re.findall(r'"([^"]{6,})"', txt) + re.findall(r"(?:(?<=[\s(:])|^)'(.{6,}?)'(?=[\s).;,:]|$)", txt)
        for q in qs:
            nq += 1
            qq = norm(q.strip())
            if qq and qq not in B:
                bad.append((f"C{i}", fld, q[:160]))
ids = set()
for r in rub:
    ids |= set(re.findall(r"\b(?:cmt_[a-z0-9_]+|f_[0-9a-f]{22}|evt_[0-9a-f]{22}|[0-9a-f]{24}|C0[0-9A-Z]{8,9}/\d+\.\d+|D0[0-9A-Z]{8,9}/\d+\.\d+)\b", json.dumps(r)))
missing_ids = sorted(x for x in ids if x.split("/")[-1] not in B and x not in B)
print("quotes checked", nq, "not found", len(bad))
for b in bad:
    print("  ", b)
print("ids", len(ids), "missing", missing_ids)
