import json, sys, os, collections

R = os.path.dirname(os.path.abspath(__file__))

def load(service):
    p = os.path.join(R, "out_%s.json" % service)
    if not os.path.exists(p):
        return None
    try:
        return json.load(open(p))
    except Exception as e:
        return {"_error": str(e)}

def summarize(service):
    d = load(service)
    if d is None:
        print("== %s: missing" % service); return
    if "_error" in d:
        print("== %s: BAD JSON %s" % (service, d["_error"])); return
    qs = d.get("queries") or {}
    print("== %s (files_selected=%s scan_complete=%s)" % (service, d.get("files_selected"), d.get("scan_complete")))
    for qid, q in qs.items():
        ms = q.get("matches") or []
        recs = []
        for m in ms:
            recs.append((m.get("service_file") or m.get("file"), m.get("parent_pointer") or m.get("pointer")))
        uniq = len(dict.fromkeys(recs))
        first = ms[0] if ms else None
        fp = ""
        if first:
            fp = "%s%s" % (short(first.get("service_file") or ""), first.get("parent_pointer"))
        print("  %-20s matches=%-5d recs=%-5d complete=%-5s %s" % (
            qid, len(ms), uniq, q.get("scan_complete"), fp))
        if q.get("errors"):
            print("      errors:", q["errors"])
    print()

def short(f):
    f = f.replace("Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/", "")
    f = f.replace("Universe_SynthCut/SynthCut_HarmonyGames_Gmail/Services_Data/", "")
    f = f.replace("Universe_SynthCut/SynthCut_HarmonyGames_GitHub/Services_Data/", "")
    return f

if __name__ == "__main__":
    for s in sys.argv[1:]:
        summarize(s)
