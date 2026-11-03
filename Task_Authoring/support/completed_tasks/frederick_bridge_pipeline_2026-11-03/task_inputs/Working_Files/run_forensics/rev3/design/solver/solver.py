"""Solver for the Frederick bridge-pipeline task (tools/oracle_kit.py contract).

Truth for the fundraising register as of end of day Tue Sep 30, 2025 (Pacific), from the base universe plus the
injection SQL (parsed with tools/base_check.parse_sql; never executed). One rule per mechanism_portfolio entry; each
rule has a natural-reading fallback that `disable` switches on, whole or per key set.

Base statuses for list firms the task does not hinge on come from BASE_STATUS (each with its base record ids);
firms whose base record set supports two fair readings carry them in `accepted`.
"""
import collections
import json
from pathlib import Path

KEY_REGEX = r".+"
FIELDS = ["Firm", "Build access", "Committed", "Soft-circled", "Keep warm"]
CLASS_FIELD, GROUPS_FIELD = "Status", "groups"

FRED = "frederick.stone@harmonygames.co"
# seeded deciding records (ids as written by Working_Files/plan/build_sql.py)
S_ROB_SCI = "cf10d4f7f88143dc7ab976df27513790"          # C096HFA5Z8W/1759184040.552871, Robert: Sciplay out
S_ANGELS = "4921f321db5d08f936aac24a6a1d2af8"           # C07C2866011/1758303600.418207, Leonard: angels "in"
CT_EDITH, CT_ILSE, CT_KARTHIC = "e3a91c07d5b48f26a0c7e314", "b72f0d6e19c3a84e5d21f9a0", "5d0e8b31f7a29c64e1b0d3a8"
EVT_BRIGHT = "evt_2f86b0d4c9e17a35b64e0d"
LIN_DENTSU, LIN_TACC = "lc_b549f3057640a5eb08f7581e", "lc_94eb35d962cfbdd31e1bd496"
TR_KW_CMT = "68c64270d660c977c4696986"

# deciding message rows (Frederick's copies; ids as written by build_sql.py)
M_ANTON = "frederick.stone@harmonygames.co/<CACJhvEE55qdWXuKC3BWlscoxBKrLUWavLQ3cpTJ@mail.gmail.com>"
M_DS_ANTON = "frederick.stone@harmonygames.co/<CAiKDPIoVSAFUBccUSRRBTi6dsmJdhof2EzteoIx@mail.gmail.com>"
M_PAUL = "frederick.stone@harmonygames.co/<CAP6Gn2LV490e3El5rBDCgCItvhOdc7S6Wpb8nNq@mail.gmail.com>"
M_HIRO = "frederick.stone@harmonygames.co/<CAwC4Lcoz_m48Uv82Dq_lp6f26Gm0Vi7deiv8pmy@mail.gmail.com>"
M_DENTSU = "frederick.stone@harmonygames.co/<CA0tK15jPm2APp9fC951nDe67wjSrpCEicNbVOjE@mail.gmail.com>"
M_BRIGHT = "frederick.stone@harmonygames.co/<CAwe90nFO3DL0_sgKjxqq__2-_n1R0a1bFAGg6-W@mail.gmail.com>"
M_BRIGHT_RE = "frederick.stone@harmonygames.co/<CAU-1_oDVchbv0CU8Qh_b3GSyAC9wFFrR0VLiLrX@mail.gmail.com>"

RULES = {
    "DONE1": {"mechanism": "A24", "requirement": "R3", "nodes": ["T1", "C1"], "decides": ["Committed", "Soft-circled"],
              "natural_reading": "an angel posted as 'in' counts as committed at the posted amount",
              "family": "done_gap", "source": "signing", "controls": ["Anton Bernstein"], "over_application": "done1_over"},
    "INPUT": {"mechanism": "A11", "requirement": "R3", "nodes": ["T4"], "decides": ["Committed", "Soft-circled"],
              "natural_reading": "Anton at the $40K posted in #executives",
              "family": "superseding", "source": "angel_mail", "controls": ["Paul Heydon"], "over_application": "input_over"},
    "DONE2": {"mechanism": "A24", "requirement": "R4", "nodes": ["T2"], "decides": ["Build access"],
              "natural_reading": "Dentsu on both platforms because Leonard's mail says invites are out to all three",
              "family": "done_gap", "source": "tester_ticket", "controls": ["T-accelerate"], "over_application": "done2_over"},
    "CORR": {"mechanism": "A14", "requirement": "R2", "nodes": ["T3", "C2"], "decides": ["Status", "Keep warm"],
             "natural_reading": "Sciplay In talks from its own mail thread",
             "family": "superseding", "source": "slack_reply", "controls": ["Dentsu Ventures"], "over_application": "corr_over"},
    "ALIAS": {"mechanism": "A7", "requirement": "R2", "nodes": ["T5", "C3"], "decides": ["Status", "Keep warm"],
              "natural_reading": "Hiro Capital Awaiting reply from the list row",
              "family": "scope_alias", "source": "contacts", "controls": ["Makers Fund"], "over_application": "alias_over"},
    "FILT": {"mechanism": "A17", "requirement": "R1", "nodes": ["T6", "T7", "C4"], "decides": ["groups"],
             "natural_reading": "register = the 2025 list rows only",
             "family": "exact_predicate", "source": "calendar", "controls": ["T-accelerate"], "over_application": "filt_over"},
    "FOLLOW": {"mechanism": "A15", "requirement": "R6", "nodes": ["T8", "C5"], "decides": ["Keep warm"],
               "natural_reading": "no keep-warm checklist items",
               "family": "authority", "source": "card_rule", "controls": ["Dentsu Ventures"], "over_application": "follow_over"},
}
DEGRADES = {
    "done1_over": "treat the signed angel (Anton) as unsigned too",
    "input_over": "lower Paul's amount as if he had revised it",
    "done2_over": "mark T-Accelerate iOS only although the ticket confirms both tracks",
    "corr_over": "read Dentsu (in talks) as passed",
    "alias_over": "map an unrelated partner reply onto Makers Fund (passed)",
    "filt_over": "split PXLite off T-Accelerate as its own off-list firm",
    "follow_over": "add every firm in talks (Dentsu) to keep-warm",
    "filt_miss": "a member of the off-list population is not found (calendar-call channel)",
}
CHANNELS = {
    "CH-FILT-HOMA": {"kind": "scale", "degrade": "filt_miss", "members": ["Homa"], "latent": "member",
                     "family": "exact_predicate", "rule": "FILT", "source": "calendar",
                     "description": "Homa's call (person-titled event; HOMA only in the invitation body) is not found"},
    "CH-FILT-BRIGHT": {"kind": "scale", "degrade": "filt_miss", "members": ["Brightwater Games Fund"], "latent": "member",
                       "family": "exact_predicate", "rule": "FILT", "source": "calendar",
                       "description": "the Sep 25 'Ilse Marrow and Leonard Hayes' call is not mapped to Brightwater"},
}

OFFLIST = ["Homa", "Brightwater Games Fund"]
PASS_AFTER_PITCH = ["London Venture Partners"]          # base: call Sep 9 (evt_e59dc0a675d0c407b79acf), pass Sep 25
IN_TALKS = ["Dentsu Ventures", "NCsoft", "GFR Fund", "T-accelerate", "Homa", "Brightwater Games Fund"]
BASE_STATUS = {   # firm -> (status, accepted alternatives, base evidence)
    "London Venture Partners": ("Passed", [], [f"{FRED}/1842277743427687737"]),
    "Grishin Robotics": ("Passed", [], [f"{FRED}/1842278603974731778"]),
    "Lakestar Ventures": ("Passed", [], ["C096HFA5Z8W/1757345124.546449"]),
    "Play Ventures": ("Passed", ["Awaiting reply"], ["C096HFA5Z8W/1757955553.793529", "C096HFA5Z8W/1758671737.632949"]),
    "Andreessen Horowitz": ("In talks", ["Passed"], [f"{FRED}/1842277213140775733", f"{FRED}/1844748127814183717"]),
    "Dentsu Ventures": ("In talks", [], [f"{FRED}/1843473831194478743"]),
    "NCsoft": ("In talks", [], [f"{FRED}/1832208184829815962"]),
    "GFR Fund": ("In talks", [], [f"{FRED}/1843547312959065138"]),
    "T-accelerate": ("In talks", [], [f"{FRED}/1842283406259093714"]),
    "Sciplay": ("In talks", [], [f"{FRED}/1842285743246816270"]),          # overturned by CORR
    "Hiro Capital": ("Awaiting reply", [], ["f_48247af79428823c3cac92"]),  # overturned by ALIAS
    "Makers Fund": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "Raine Ventures": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "BBQ Capital": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "General Catalyst": ("Awaiting reply", ["Not contacted this round"], ["f_48247af79428823c3cac92"]),
    "Sony Mobile": ("Awaiting reply", [], ["f_48247af79428823c3cac92"]),
    "Revo Capital": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "e2vc": ("Awaiting reply", [], ["C096HFA5Z8W/1757345124.546449"]),
    "Superplay": ("Awaiting reply", ["Not contacted this round"], ["f_48247af79428823c3cac92"]),
    "Mattel": ("Awaiting reply", ["In talks"], ["C096HFA5Z8W/1756941551.539229"]),
    "Treo VC": ("Awaiting reply", ["In talks"], ["C096HFA5Z8W/1757345124.546449"]),
    "BITKRAFT Ventures": ("Awaiting reply", ["Not contacted this round"], ["C096HFA5Z8W/1758563861.649039"]),
    "Triptyq": ("Awaiting reply", ["Not contacted this round"], ["C096HFA5Z8W/1757716998.377299"]),
    "Turkven": ("Awaiting reply", ["Not contacted this round"], ["C096HFA5Z8W/1757716998.377299"]),
    "Harlem Capital": ("Awaiting reply", ["Not contacted this round"], ["C096HFA5Z8W/1757716998.377299"]),
    "Transcend Fund": ("Not contacted this round", ["Awaiting reply"], ["f_48247af79428823c3cac92"]),
    "Acterra": ("Not contacted this round", ["Awaiting reply"], ["f_48247af79428823c3cac92"]),
    "March Gaming Fund": ("Not contacted this round", ["Passed"], ["f_48247af79428823c3cac92"]),
    "Index Ventures": ("Not contacted this round", ["Passed"], ["C096HFA5Z8W/1757345124.546449"]),
}
ANGELS = {"Paul Heydon": 50000, "Anton Bernstein": 40000}   # as posted in #executives (S_ANGELS)


def _list_keys():
    import ast
    here = Path(__file__).resolve()
    data = here.parents[4] / "Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gsheets/data.json"
    d = json.loads(data.read_text())
    sp = next(x for x in d["sheets_spreadsheets"] if x["spreadsheet_id"] == "f_48247af79428823c3cac92")
    sh = ast.literal_eval(sp["sheets"]) if isinstance(sp["sheets"], str) else sp["sheets"]
    seen, keys = set(), []
    for r in sh[0]["grid"][1:]:
        f = (r[1] if len(r) > 1 else "").strip()
        if f and f.lower() not in seen:
            seen.add(f.lower())
            keys.append(f)
    return keys


def load_state(sql_text, revision=None):
    from base_check import parse_sql
    rows = [x for x in parse_sql(sql_text) if x["op"] == "insert"]
    by_id = {}
    for x in rows:
        r = x["row"]
        for k in ("id", "contact_id", "event_id", "spreadsheet_id"):
            if r.get(k):
                by_id[str(r[k])] = r
    texts = " ".join(json.dumps(x["row"], ensure_ascii=False) for x in rows)
    return {"by_id": by_id, "text": texts, "list_keys": _list_keys(), "revision": revision or "rev1"}


def _hit(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def keys_of(state):
    return state["list_keys"] + OFFLIST


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    b = state["by_id"]
    have = lambda i: i in b
    posted = have(S_ANGELS)                       # the #executives post is the only record of the angels' amounts
    paul_completed = "Completed: Complete with docusign: Harmony Games SAFE - Paul Heydon" in state["text"]
    anton_completed = have(M_DS_ANTON)
    anton_latest = 25000 if have(M_ANTON) else ANGELS["Anton Bernstein"]
    out = {}
    universe = list(keys_ or keys_of(state))
    if _hit(degrade, "filt_over", "T-accelerate") and "T-accelerate" in universe:
        universe.append("PXLite")
    for k in universe:
        missed = k in OFFLIST and (_hit(disable, "FILT", k) or _hit(degrade, "filt_miss", k))
        if k in OFFLIST:
            ok = have(M_BRIGHT) and have(M_BRIGHT_RE) if k == "Brightwater Games Fund" else True
            if not ok:
                missed = True
        status, accepted, ev = BASE_STATUS.get(k, ("Not contacted this round", [], ["f_48247af79428823c3cac92"]))
        if k in OFFLIST or k == "PXLite":
            status, accepted, ev = "In talks", [], [EVT_BRIGHT] if k == "Brightwater Games Fund" else ["evt_89381fe5a15b802c5652a9"]
        if k == "Sciplay" and have(S_ROB_SCI) and not _hit(disable, "CORR", k):
            status, ev = "Passed", [S_ROB_SCI]
        if k == "Hiro Capital" and have(M_HIRO) and have(CT_EDITH) and not _hit(disable, "ALIAS", k):
            status, ev = "Passed", [CT_EDITH]
        if k == "T-accelerate" and _hit(degrade, "filt_over", k):
            status = "Not contacted this round"
        if k == "Dentsu Ventures" and _hit(degrade, "corr_over", k):
            status = "Passed"
        if k == "Makers Fund" and _hit(degrade, "alias_over", k):
            status = "Passed"
        access = None
        if status == "In talks":
            access = "none"
            if k == "Dentsu Ventures":
                access = "iOS and Android" if (_hit(disable, "DONE2", k) or not have(LIN_DENTSU)) else "iOS only"
            if k == "T-accelerate":
                access = "iOS only" if _hit(degrade, "done2_over", k) else "iOS and Android"
        committed = soft = None
        if k in ANGELS and not posted:
            pass
        elif k == "Paul Heydon":
            if _hit(disable, "DONE1", k) or paul_completed:
                committed = ANGELS[k]
            else:
                soft = ANGELS[k] if not _hit(degrade, "input_over", k) else 25000
        elif k == "Anton Bernstein":
            amount = ANGELS[k] if _hit(disable, "INPUT", k) else anton_latest
            if _hit(degrade, "done1_over", k) or not anton_completed:
                soft = amount
            else:
                committed = amount
        pitched_pass = status == "Passed" and (k in PASS_AFTER_PITCH or k in ("Sciplay", "Hiro Capital"))
        keep = "yes" if (pitched_pass and have(TR_KW_CMT) and not _hit(disable, "FOLLOW", k)) else "no"
        if k == "Dentsu Ventures" and _hit(degrade, "follow_over", k):
            keep = "yes"
        groups = ["register"] + (["keepwarm"] if keep == "yes" else []) + (["in_talks"] if status == "In talks" else [])
        if missed:      # the firm is left off the register: no row is written for it
            status, access, groups, accepted = None, None, [], []
        firm_ev = [x for x in ev if x in b]
        out[k] = {"Firm": k, "Status": status, "accepted_status": accepted, "Build access": access,
                  "Committed": committed, "Soft-circled": soft, "Keep warm": keep, "groups": groups,
                  "evidence": {"Status": ev, "Firm": firm_ev}}
    return out


def aggregates(rows):
    groups = collections.defaultdict(list)
    for k in sorted(rows):
        for g in rows[k]["groups"]:
            groups[g].append(k)
    committed = sum(v["Committed"] or 0 for v in rows.values())
    soft = sum(v["Soft-circled"] or 0 for v in rows.values())
    return {"classes": dict(sorted(collections.Counter(v["Status"] for v in rows.values()).items())),
            "groups": {g: groups[g] for g in sorted(groups)},
            "totals": {"register_size": len(rows), "committed_total": committed, "soft_circled_total": soft,
                       "keep_warm": len(groups.get("keepwarm", []))}}


def evidence(rows, key, field):
    if field == "Firm":
        return list(rows[key]["evidence"]["Firm"])
    return []


def touched(state, rule):
    return {"DONE1": {"Paul Heydon"}, "INPUT": {"Anton Bernstein"}, "DONE2": {"Dentsu Ventures"}, "CORR": {"Sciplay"},
            "ALIAS": {"Hiro Capital"}, "FILT": set(OFFLIST), "FOLLOW": {"London Venture Partners", "Sciplay", "Hiro Capital"}}[rule]


def deciding(state, rule, key):
    return {"DONE1": [S_ANGELS, M_DS_ANTON], "INPUT": [M_ANTON], "DONE2": [LIN_DENTSU], "CORR": [S_ROB_SCI],
            "ALIAS": [M_HIRO], "FILT": [M_BRIGHT, M_BRIGHT_RE], "FOLLOW": [TR_KW_CMT]}[rule]


def base_route(record_id):
    return None
