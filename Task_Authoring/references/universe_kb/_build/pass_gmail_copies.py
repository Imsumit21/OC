"""Second, targeted Gmail pass: re-read only files holding messages copied into 2+ mailboxes and
classify copy differences (redaction-only vs material) with difflib ratios."""
import re, json, collections, difflib
from common import *

TD = GMAIL + "/threads"
RED = re.compile(r"\[[A-Z_]+_\d+\]|\b[A-Z]+_\d+_[A-Z_]+\b|harmony ?games|\[source_org_\d+\]", re.I)


def norm(s):
    s = RED.sub(" ", s or "")
    s = re.sub(r"<[^>]*>|https?://\S+", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()


def main():
    G = jload(CACHE + "/kb_gmail.json")
    mc = G["multi_copy_files"]
    need = collections.defaultdict(set)
    for rfc, lst in mc.items():
        for mb, fn in lst:
            need[fn].add(rfc)
    msgs = collections.defaultdict(dict)
    for fn, rfcs in need.items():
        t = jload(TD + "/" + fn)
        for m in t.get("messages") or []:
            r = (m.get("id") or "").split("/", 1)[-1]
            if r in rfcs:
                msgs[r][t["user_email"] + " " + fn] = (m.get("subject") or "", m.get("body") or "", m.get("from") or "", m.get("date_parsed") or m.get("date"), len(m.get("attachments") or []))
    cls = collections.Counter()
    ex = collections.defaultdict(list)
    pair_cls = collections.defaultdict(collections.Counter)
    for r, copies in msgs.items():
        ks = sorted(copies)
        if len(ks) < 2:
            continue
        a = copies[ks[0]]
        for k in ks[1:]:
            b = copies[k]
            if k.split(" ")[0] == ks[0].split(" ")[0]:
                continue
            pair = " | ".join(sorted([ks[0].split(" ")[0], k.split(" ")[0]]))
            if a[1] == b[1] and a[0] == b[0]:
                c = "identical"
            else:
                na, nb = norm(a[0] + " " + a[1][:6000]), norm(b[0] + " " + b[1][:6000])
                if na == nb:
                    c = "differs only by redaction tokens / company-name masking"
                else:
                    ratio = difflib.SequenceMatcher(None, na[:3000], nb[:3000]).ratio()
                    if ratio >= 0.97:
                        c = "near-identical after normalisation (>=0.97)"
                    elif ratio >= 0.8:
                        c = "partly different (0.80-0.97)"
                    else:
                        c = "materially different (<0.80)"
            if a[4] != b[4]:
                cls["attachment count differs"] += 1
                if len(ex["attachment count differs"]) < 10:
                    ex["attachment count differs"].append([ks[0], k, r[:90]])
            cls[c] += 1
            pair_cls[pair][c] += 1
            if len(ex[c]) < 10:
                ex[c].append([ks[0], k, r[:90]])
            break
    out = {"classes": dict(cls), "examples": dict(ex), "by_pair": {k: dict(v) for k, v in sorted(pair_cls.items(), key=lambda kv: -sum(kv[1].values()))[:25]}}
    jdump(out, CACHE + "/kb_gmail_copies.json")
    print(json.dumps(out["classes"]))


if __name__ == "__main__":
    main()
