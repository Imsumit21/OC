#!/usr/bin/env python3
"""Grade the six rev4 baseline runs against the rubric rows (local estimate of the verifier).

Reads run_forensics/rev4/baseline/run-*/writes.json (decoded write payloads) and applies each row's predicate.
The predicates follow the row titles; where a title needs judgement (reply lists), the reply text is parsed into
its 'keeping' and 'sign' sections. Prints per-run scores, mean, SD and the failure patterns."""
import json
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
TI = WF.parent
sys.path.insert(0, str(TI.parent / "tools"))
from base_check import parse_sql  # noqa: E402

BASE = WF / "run_forensics/rev4/baseline"
ST = [x for x in parse_sql((TI / "01_Universe_Inject.sql").read_text()) if x["op"] == "insert"]
IDS = json.loads((WF / "plan/sql_ids.json").read_text())["ids"]
TRUTH = json.loads((WF / "solver/truth.json").read_text())
FRED = "frederick.stone@harmonygames.co"
HUB_MID = IDS["msg"]["hub"]
TODO = "640643a3fd8f3ca308d93195"
FOLDER = "d_80a8c04753ba82ba4ba6a5"
ESG = "PERSON_2599_EMAIL"
COS = [k for k, v in TRUTH.items() if v["Decision"]]
ALIAS = {"Lanternfly Publishing": ["lanternfly"], "Pixel Harbor Events": ["pixel harbor"], "Streamcast Talent": ["streamcast"],
         "Orbit Store": ["orbit"], "Driftwood Audio": ["driftwood"], "Kinetic Arcade": ["kinetic"], "Brightlane Studio": ["brightlane"],
         "Motive Forge": ["motive forge"], "Spotlight Fest": ["spotlight"], "Nintendo": ["nintendo"]}

# message id → company (every seeded message in a company thread)
MSG_CO = {}
for x in ST:
    r = x["row"]
    if x["table"] == "gmail.gmail_messages" and r.get("user_email") == FRED:
        for k, tid in IDS["threads"].items():
            if r["thread_id"] == tid:
                MSG_CO[r["id"]] = k
PERSON_EMAIL = {}
for k in COS:
    if k in IDS["threads"]:
        for x in ST:
            r = x["row"]
            if x["table"] == "gmail.gmail_messages" and r.get("thread_id") == IDS["threads"][k] and not r["from_email"].endswith("@harmonygames.co"):
                PERSON_EMAIL[r["from_email"]] = k
PERSON_EMAIL["PERSON_0527_EMAIL"] = "Balancy"
PERSON_EMAIL["billing@paylane.io"] = "Clipforge"


def keys(k):
    return ALIAS.get(k, [k.lower()])


def names_in(text):
    t = (text or "").lower()
    return {k for k in COS if any(a in t for a in keys(k))}


def date_is(cell, y, m, d):
    c = (cell or "").strip()
    mon = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"][m - 1]
    pats = [rf"{y}-{m:02d}-{d:02d}", rf"\b{m}/{d}/{y}\b", rf"\b{m:02d}/{d:02d}/{y}\b", rf"{mon}[a-z]*\.? {d}\b(,? {y})?",
            rf"\b{d} {mon}[a-z]* {y}"]
    return any(re.search(p, c, re.I) for p in pats)


def load(run):
    w = json.loads((BASE / run / "writes.json").read_text())
    ok = [x for x in w if x.get("ok")]
    rows, header_ok, in_folder, log_name = [], False, False, ""
    for x in ok:
        if x["tool"] == "gdrive_copy_file":
            inp = x["input"]
            if inp.get("fileId") == "f_05f0a451b29b19a1c0b90f":
                header_ok = True
            if inp.get("parentId") == FOLDER:
                in_folder = True
            log_name = inp.get("name") or log_name
        if x["tool"] in ("gsheets_values_update", "gsheets_values_append"):
            for v in x.get("values") or []:
                if v and v[0] == "Company":
                    header_ok = header_ok or v[:7] == ["Company", "Contact", "What's waiting", "Decision", "Answered by", "What we told them", "Next date"]
                    continue
                rows.append((v + [""] * 7)[:7])
        if x["tool"] == "gdrive_move_file" and FOLDER in json.dumps(x):
            in_folder = True
    log = {}
    for r in rows:
        ks = names_in(r[0])
        for k in ks:
            log[k] = r
    replies = [x for x in ok if x["tool"] == "gmail_reply_to_message"]
    sends = [x for x in ok if x["tool"] == "gmail_send_message"]
    hub = [x for x in replies if x.get("message_id") == HUB_MID]
    answered = {}
    for x in replies:
        k = MSG_CO.get(x.get("message_id"))
        if k:
            answered.setdefault(k, []).append(x)
    for x in sends:
        for to in x.get("to") or []:
            k = PERSON_EMAIL.get(to)
            if k:
                answered.setdefault(k, []).append(x)
    esg = [x for x in sends if ESG in (x.get("to") or [])]
    cards = [x for x in ok if x["tool"] == "trello_create_card" and x["input"].get("idList") == TODO]
    contacts = [x["input"] for x in ok if x["tool"] == "contacts_add_new_contact"]
    events = []
    for x in ok:
        if x["tool"] == "gcal_create_event":
            e = x["input"].get("event") or x["input"]
            st = e.get("start") or {}
            d = st.get("date") or (st.get("dateTime") or "")[:10]
            events.append((d, (e.get("summary") or "") + " " + (e.get("description") or ""), x["event"]))
    jan5 = [e for e in events if e[0] == "2026-01-05"]
    return dict(log_name=log_name, w=ok, rows=rows, log=log, header_ok=header_ok, in_folder=in_folder, hub=hub, answered=answered, esg=esg,
                cards=cards, contacts=contacts, jan5=jan5)


def reply_sections(body):
    b = body or ""
    low = b.lower()
    i_keep = low.find("keep")
    i_sign = low.find("sign", i_keep + 1 if i_keep >= 0 else 0)
    keep = b[i_keep:i_sign] if i_keep >= 0 and i_sign > i_keep else ""
    m = re.search(r"\n\s*\n\s*(also|everything else|the rest|ended|other)", b[i_sign:], re.I) if i_sign >= 0 else None
    sign = b[i_sign:i_sign + m.start()] if m else b[i_sign:i_sign + 1800]
    return names_in(keep), names_in(sign)


def body_of(d, k):
    return " ".join((x.get("body") or "") for x in d["answered"].get(k, []))


def esg_about(d, co):
    out = []
    for x in d["esg"]:
        ns = names_in((x.get("subject") or "") + " " + (x.get("body") or ""))
        if ns == {co}:
            out.append(x)
    return out


def told_no(cell):
    return bool(re.search(r"\bno\b|declin|pass(ed)? on|not (going|book|tak|proceed|mov|go ahead)|no thanks|said no|won't|turn(ed)? down|not interested|cancel", cell or "", re.I))


def ans_by(cell, who):
    return who.lower() in (cell or "").lower()


def order(d, kind_events):
    if not d["hub"] or not kind_events:
        return False
    h = d["hub"][0]["event"]
    return any(e < h for e in kind_events) and not any(e > h for e in kind_events)


def cellof(d, co, i):
    return d["log"].get(co, [""] * 7)[i]


def said(d, co, pat):
    return bool(re.search(pat, body_of(d, co), re.I))


NO = r"\bno\b|declin|pass(ed|ing)? on|not (to )?(go|book|tak|proceed|mov|continu|renew|pursu|sign|commit|start|do\b|be doing)|decided not|no thanks|said no|won't|turn(ed|ing)? down|not interested|cancel|decided against|unable to"
JAN = r"january|\bjan\.? \d|new year|early 2026|\bq1\b"
KEEP = r"keep|stay|continu|confirm|renew|go ahead|carry on"
# round 2: a reply that sends this agreement to the lawyers for review first fails (the template mention and step 4's conditional pass)
LAWYERS_FIRST = r"\b(goes|go|going|send(ing)?|sent|forward(ing|ed)?|pass(ing)?)\s+(it\s+|this\s+|them\s+)?(over\s+)?to\s+(our\s+)?(lawyers|counsel|legal|ESG)\b[^.]{0,60}\b(first|review)"


def esg_has(d, co, pat):
    return any(re.search(pat, (x.get("subject") or "") + " " + (x.get("body") or ""), re.I) for x in esg_about(d, co))


def reply_has(d, part, co):
    return bool(d["hub"]) and co in reply_sections(d["hub"][0]["body"])[part]


def contact(d, first, email, co):
    return any(c.get("first_name") == first and c.get("email") == email and any(a in (c.get("job") or "").lower() for a in keys(co))
               for c in d["contacts"])


def order_all(d):
    if not d["hub"]:
        return False
    h = d["hub"][0]["event"]
    others = [x["event"] for x in d["w"] if x is not d["hub"][0]]
    return bool(others) and all(e < h for e in others)


P = {
    "log_folder": lambda d: d["in_folder"],
    "log_type": lambda d: d["header_ok"] or any(x["tool"] == "gsheets_create_spreadsheet" for x in d["w"]),
    "log_name": lambda d: re.sub(r"\s+", " ", d["log_name"]).strip().lower() == "q4 commitments log",
    "log_header": lambda d: d["header_ok"],
    "log_rows": lambda d: len(d["rows"]) == 36 and len(d["log"]) == 36,
    "nin_decision": lambda d: cellof(d, "Nintendo", 3).strip().lower() == "sign",
    "fw_decision": lambda d: cellof(d, "Framewell", 3).strip().lower() == "park",
    "lf_decision": lambda d: cellof(d, "Lanternfly Publishing", 3).strip().lower() == "answered",
    "sp_decision": lambda d: cellof(d, "Spotlight Fest", 3).strip().lower() == "answered",
    "pw_decision": lambda d: cellof(d, "Pingwise", 3).strip().lower() == "keep",
    "rev_contact": lambda d: bool(re.search(r"hana|PERSON_9708_EMAIL", cellof(d, "Reviewly", 1), re.I)),
    "sv_waiting": lambda d: bool(re.search(r"licen[cs]|trailer|music", cellof(d, "Soundvault", 2), re.I)),
    "lf_by": lambda d: ans_by(cellof(d, "Lanternfly Publishing", 4), "leonard"),
    "sp_by": lambda d: ans_by(cellof(d, "Spotlight Fest", 4), "robert"),
    "bal_by": lambda d: ans_by(cellof(d, "Balancy", 4), "leonard"),
    "mf_by": lambda d: ans_by(cellof(d, "Motive Forge", 4), "arthur"),
    "mf_when": lambda d: any(date_is(c, 2025, 9, 19) for c in d["log"].get("Motive Forge", [])),
    "nin_next": lambda d: date_is(cellof(d, "Nintendo", 6), 2025, 10, 15),
    "cf_next": lambda d: date_is(cellof(d, "Clipforge", 6), 2025, 10, 15),
    "ph_next": lambda d: date_is(cellof(d, "Pixel Harbor Events", 6), 2025, 10, 10),
    "pw_next": lambda d: date_is(cellof(d, "Pingwise", 6), 2025, 11, 1),
    "lf_next": lambda d: date_is(cellof(d, "Lanternfly Publishing", 6), 2026, 1, 5),
    "ph_told": lambda d: told_no(cellof(d, "Pixel Harbor Events", 5)),
    "lf_told": lambda d: bool(re.search(r"(after|until|before) the raise|no new", cellof(d, "Lanternfly Publishing", 5), re.I)),
    "sv_told": lambda d: told_no(cellof(d, "Soundvault", 5)),
    "kin_told": lambda d: bool(re.search(r"counsel|lawyer|legal|ESG", cellof(d, "Kinetic Arcade", 5), re.I)),
    "ww_told": lambda d: told_no(cellof(d, "Wishwave", 5)),
    "ans_count": lambda d: set(d["answered"]) == {k for k, v in TRUTH.items() if "written_answer" in v["groups"]},
    "cf_cancel": lambda d: any("billing@paylane.io" in (x.get("to") or []) for x in d["answered"].get("Clipforge", [])),
    "cf_priya": lambda d: any(x["tool"] == "gmail_reply_to_message" or "PERSON_9704_EMAIL" in (x.get("to") or [])
                              for x in d["answered"].get("Clipforge", [])),
    "rev_cancel": lambda d: said(d, "Reviewly", r"cancel"),
    "ans_certwell": lambda d: said(d, "Certwell", KEEP),
    "ans_vaultline": lambda d: said(d, "Vaultline", KEEP),
    "ans_pingwise": lambda d: said(d, "Pingwise", KEEP + r"|team") and not said(d, "Pingwise", r"\b(please|go ahead and|can you) (downgrade|drop) us\b|\b(move|switch|drop) us (back )?to (the )?free"),
    "ans_orbit": lambda d: said(d, "Orbit Store", r"leonard|arthur") and not said(d, "Orbit Store", LAWYERS_FIRST),
    "ans_bundle": lambda d: said(d, "Bundlehouse", r"lawyer|counsel|legal|ESG"),
    "ans_bundle_sign": lambda d: said(d, "Bundlehouse", r"leonard|arthur"),
    "ans_kin_lawyers": lambda d: said(d, "Kinetic Arcade", r"lawyer|counsel|legal|ESG"),
    "ans_kin_sign": lambda d: said(d, "Kinetic Arcade", r"leonard|arthur"),
    "ans_lumen_lawyers": lambda d: said(d, "Lumencloud", r"lawyer|counsel|legal|ESG"),
    "ans_lumen_sign": lambda d: said(d, "Lumencloud", r"leonard|arthur"),
    "ans_markward": lambda d: said(d, "Markward", r"leonard|arthur") and not said(d, "Markward", LAWYERS_FIRST),
    "ans_playfuse": lambda d: said(d, "Playfuse", r"leonard|arthur") and not said(d, "Playfuse", LAWYERS_FIRST),
    "esg_count": lambda d: len(d["esg"]) == 3,
    "esg_lumen": lambda d: esg_has(d, "Lumencloud", r"36|three years"),
    "esg_lumen_date": lambda d: esg_has(d, "Lumencloud", r"Oct(ober)?\.? 31|10/31|2025-10-31"),
    "esg_lumen_cost": lambda d: esg_has(d, "Lumencloud", r"no charge|\$0\b|free|no cost|nothing|\bnone\b"),
    "esg_lumen_signer": lambda d: esg_has(d, "Lumencloud", r"leonard|arthur"),
    "esg_kinetic": lambda d: esg_has(d, "Kinetic Arcade", r"12[- ]month|12 months|one year") and esg_has(d, "Kinetic Arcade", r"exclusiv"),
    "esg_kin_date": lambda d: esg_has(d, "Kinetic Arcade", r"Oct(ober)?\.? 20|10/20|2025-10-20"),
    "esg_kin_cost": lambda d: esg_has(d, "Kinetic Arcade", r"no fee|revenue share|no cost|free"),
    "esg_kin_signer": lambda d: esg_has(d, "Kinetic Arcade", r"leonard|arthur"),
    "esg_bundle": lambda d: esg_has(d, "Bundlehouse", r"licen[cs]|\bIP\b"),
    "esg_bh_term": lambda d: esg_has(d, "Bundlehouse", r"18[- ]month|18 months|eighteen"),
    "esg_bh_date": lambda d: esg_has(d, "Bundlehouse", r"Nov(ember)?\.? 1\b|11/1/|11/01|2025-11-01"),
    "esg_bh_cost": lambda d: esg_has(d, "Bundlehouse", r"no cost|free|revenue share|nothing"),
    "esg_bh_signer": lambda d: esg_has(d, "Bundlehouse", r"leonard|arthur"),
    "card_count": lambda d: len(d["cards"]) == 7 and all(len(names_in(x["input"]["name"])) >= 1 for x in d["cards"]),
    "card_nin": lambda d: any(names_in(x["input"]["name"]) == {"Nintendo"} for x in d["cards"]),
    "card_kin": lambda d: any(names_in(x["input"]["name"]) == {"Kinetic Arcade"} for x in d["cards"]),
    "card_mark": lambda d: any(names_in(x["input"]["name"]) == {"Markward"} for x in d["cards"]),
    "ct_count": lambda d: len(d["contacts"]) == 32 and all((c.get("job") or "").strip() for c in d["contacts"]),
    "ct_hoot": lambda d: contact(d, "Gemma", "PERSON_9722_EMAIL", "Hootline"),
    "ct_rev": lambda d: contact(d, "Hana", "PERSON_9708_EMAIL", "Reviewly"),
    "ct_wen": lambda d: contact(d, "Wen", "PERSON_9702_EMAIL", "Lanternfly Publishing"),
    "rem_count": lambda d: len(d["jan5"]) == 14,
    "rem_fw": lambda d: any(names_in(s) == {"Framewell"} for _, s, _ in d["jan5"]),
    "rem_lf": lambda d: any(names_in(s) == {"Lanternfly Publishing"} for _, s, _ in d["jan5"]),
    "rem_hoot": lambda d: any(names_in(s) == {"Hootline"} for _, s, _ in d["jan5"]),
    "reply_keep_count": lambda d: bool(d["hub"]) and len(reply_sections(d["hub"][0]["body"])[0]) == 3,
    "reply_sign_count": lambda d: bool(d["hub"]) and len(reply_sections(d["hub"][0]["body"])[1]) == 7,
    "order_reply": order_all,
}
for co, w in [("Pixel Harbor Events", "pixel"), ("Brightlane Studio", "brightlane"), ("Soundvault", "soundvault"),
              ("Streamcast Talent", "streamcast"), ("Lingora", "lingora"), ("Panelpulse", "panelpulse"), ("Ascendo", "ascendo"),
              ("Wishwave", "wishwave")]:
    P[f"ans_{w}"] = (lambda c: lambda d: said(d, c, NO))(co)
for co, w in [("Framewell", "framewell"), ("Retainly", "retainly"), ("Hootline", "hootline"), ("Glyphworks", "glyphworks"),
              ("Cloudlark", "cloudlark"), ("Echohall", "echohall"), ("Pressbeam", "pressbeam"), ("Quillcraft", "quillcraft"),
              ("Tilecast", "tilecast"), ("Benchmarkly", "benchmarkly"), ("Loopnote", "loopnote"), ("Driftwood Audio", "driftwood")]:
    P[f"ans_{w}"] = (lambda c: lambda d: said(d, c, JAN))(co)
for co in ("Pingwise", "Certwell", "Vaultline"):
    P[f"reply_{co.lower()}"] = (lambda c: lambda d: reply_has(d, 0, c))(co)
for co in ("Markward", "Nintendo", "Bundlehouse", "Kinetic Arcade", "Lumencloud", "Orbit Store", "Playfuse"):
    P[f"reply_{co.split()[0].lower()}"] = (lambda c: lambda d: reply_has(d, 1, c))(co)

RUB = json.loads((HERE / "rows.json").read_text())
assert {r["tag"] for r in RUB} == set(P), {r["tag"] for r in RUB} ^ set(P)
ROWS = [(r["tag"], r["w"], P[r["tag"]]) for r in RUB]  # weights come from the rubric itself

if __name__ == "__main__":
    total = sum(w for _, w, _ in ROWS)
    runs = sorted(p.name for p in BASE.glob("run-*"))
    scores, fails = [], {}
    for run in runs:
        d = load(run)
        failed = [t for t, w, f in ROWS if not f(d)]
        s = 1 - sum(w for t, w, _ in ROWS if t in failed) / total
        scores.append(s)
        fails[run] = failed
        print(f"{run}: {s:.3f}  rows {len(d['rows'])} answered {len(d['answered'])} esg {len(d['esg'])} cards {len(d['cards'])} "
              f"contacts {len(d['contacts'])} jan5 {len(d['jan5'])} | failed: {' '.join(failed)}")
    print(f"rows {len(ROWS)} weight {total} · mean {statistics.mean(scores):.3f} · SD {statistics.pstdev(scores):.3f} (sample {statistics.stdev(scores):.3f})")
    pats = {}
    for run, f in fails.items():
        pats.setdefault(tuple(f), []).append(run)
    print("failure patterns:", len(pats), "largest", max(len(v) for v in pats.values()), "of", len(runs))
    always = set.intersection(*(set(f) for f in fails.values()))
    print("failed by every run:", sorted(always))
