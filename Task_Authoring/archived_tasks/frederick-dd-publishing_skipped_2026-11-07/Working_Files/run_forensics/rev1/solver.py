"""Solver for frederick_dd_publishing (tools/oracle_kit.py contract), rev1.

Truth = the Domino Delights publishing model Frederick should build on Wed Oct 1, 2025, from the base universe plus the
injection SQL (parsed with tools/base_check.parse_sql; never executed). Status follows Leonard's ground rules doc top to
bottom (Withdrawn, Out on rights, Live, Passed, Waiting on us, No reply). A Live offer's 12-month value is the larger of
(rev share x monthly installs x 12 x $0.50) and the total advance. Q4 cash is advance money landing Oct 1 to Dec 31, 2025.

Terms, thread states and overrides are read from their records in the SQL. Names and the two base threads come from the
cohort table M of Working_Files/plan/build_scenario.py. One rule per mechanism_portfolio entry; each falls back to its
natural reading when `disable` switches it off (whole or per key set), its channel operator fires, or the record is
absent. Over-application operators act on the rule's declared controls.
"""
import collections
import contextlib
import datetime as D
import io
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "plan"))
with contextlib.redirect_stdout(io.StringIO()):
    import build_scenario as B  # noqa: E402  (the cohort table; writes nothing on import)

KEY_REGEX = r".+"
FIELDS = ["Publisher", "Status", "Advance", "Monthly installs", "12-month value", "Q4 cash"]
CLASS_FIELD, GROUPS_FIELD = "Status", "groups"
I = B.IDS
IDS = json.loads((HERE.parent / "plan" / "sql_ids.json").read_text())["ids"]
SL, MSG = IDS["slack_mid"], IDS["msg"]
FRED = "frederick.stone@harmonygames.co"
Q4_START, Q4_END = D.date(2025, 10, 1), D.date(2025, 12, 31)
ORIGINAL_SIGNING = D.date(2025, 10, 31)
ARPI = 0.50
OUT_KEYS = ["Homa", "NCsoft"]            # named in the rules doc as out of scope: control rows only

RULES = {
    "DONE": {"mechanism": "A24", "requirement": "R5", "nodes": ["T1", "C1"], "decides": ["Q4 cash", "Banked"],
             "natural_reading": "Oakline's $10,000 counts as banked", "family": "done_gap", "source": "slack-reply",
             "signature": "Oakline wire SVB returned", "controls": ["Tallwater Games"], "over_application": "done_over"},
    "CORR": {"mechanism": "A11", "requirement": "R3", "nodes": ["T2", "C2"], "decides": ["Advance", "12-month value", "Q4 cash"],
             "natural_reading": "the term sheet's advance stands", "family": "superseding", "source": "gcal-note",
             "signature": "Tallwater advance $40,000", "controls": ["Harbor Lane Games"], "over_application": "corr_over"},
    "ALIAS": {"mechanism": "A7", "requirement": "R2", "nodes": ["T3", "C3"], "decides": ["Status"],
              "natural_reading": "Moonrail is Live", "family": "scope_alias", "source": "alias-join",
              "signature": "Anika Kestrel Moonrail", "controls": ["Wavecrest Play"], "over_application": "alias_over"},
    "FILT": {"mechanism": "A17", "requirement": "R1", "nodes": ["T4", "T5", "C4"], "decides": ["Status", "12-month value"],
             "natural_reading": "the outreach sheet and the inbox are the population", "family": "exact_predicate",
             "source": "outside-filter", "signature": "Copperleaf Redwood outside the sheet",
             "controls": ["Homa", "NCsoft"], "over_application": "filt_over"},
    "EXC": {"mechanism": "A15", "requirement": "R6", "nodes": ["T6", "T14", "C5"], "decides": ["Status", "12-month value"],
            "natural_reading": "value alone decides", "family": "authority", "source": "sync-record",
            "signature": "retain code IP non-mobile", "controls": ["Sunfold Mobile"], "over_application": "exc_over"},
    "INPUT": {"mechanism": "A11", "requirement": "R3", "nodes": ["T7", "C6"], "decides": ["Monthly installs", "12-month value"],
              "natural_reading": "the term sheet's commitment feeds the forecast", "family": "superseding",
              "source": "card-comment", "signature": "Sunfold 30,000 installs", "controls": ["Oakline Games"],
              "over_application": "input_over"},
    "DATE": {"mechanism": "A4", "requirement": "R5", "nodes": ["T9", "C7"], "decides": ["Q4 cash"],
             "natural_reading": "signing is Oct 31", "family": "boundary_date", "source": "esg-thread",
             "signature": "Nov 14 signing", "controls": ["Sunfold Mobile"], "over_application": "date_over"},
    "FOLLOW": {"mechanism": "A15", "requirement": "R12", "nodes": ["T8", "C8"], "decides": ["groups"],
               "natural_reading": "no note is owed", "family": "authority", "source": "bridge-reply",
               "signature": "May one-pager organic note", "controls": ["Oakline Games"], "over_application": "follow_over"},
}
DEGRADES = {
    "done_over": "reads the returned wire onto Tallwater too, as if its advance never lands in Q4",
    "corr_over": "cuts Harbor Lane's advance after its call, though that call changed nothing",
    "alias_over": "withdraws Wavecrest, though no founder note is about it",
    "filt_over": "pulls Homa's co-dev talk into the population",
    "exc_over": "rules Sunfold's mobile-only offer out on rights",
    "input_over": "cuts Oakline's installs because its card has a comment",
    "date_over": "pushes Sunfold's net-45 advance out of Q4, though Dec 29 is still inside it",
    "follow_over": "owes Oakline an organic note, though it got the intro only",
    "ch_done": "the SVB reply is not read: Oakline's $10,000 stays banked",
    "ch_corr": "the calendar note is not read: Tallwater keeps $60,000",
    "ch_alias": "Kestrel is not joined to Moonrail: it stays Live",
    "ch_filt1": "Robert's pasted offer is missed: Copperleaf never reaches the model",
    "ch_filt2": "the ticket comment is missed: Redwood never reaches the model",
    "ch_exc": "the August rights position is not applied",
    "ch_input": "the card comment is not read: Sunfold keeps 50,000 installs",
    "ch_date": "the lawyers' date is not read: signing stays Oct 31",
    "ch_follow": "the standing line is not read: no organic note is drafted",
}
def _channel(op, rule, members, source, family, description):
    return {"kind": "scale", "degrade": op, "members": members, "latent": "member", "family": family,
            "rule": rule, "source": source, "description": description}
CHANNELS = {
    "CH-DONE": _channel("ch_done", "DONE", ["Oakline Games"], "slack-reply", "done_gap", "Arthur's reply under the banker post is not found: the money looks banked"),
    "CH-CORR": _channel("ch_corr", "CORR", ["Tallwater Games"], "gcal-note", "superseding", "the note past the agenda on the Tallwater event is not read"),
    "CH-ALIAS": _channel("ch_alias", "ALIAS", ["Moonrail Studios"], "alias-join", "scope_alias", "Robert's Kestrel post is not joined to Moonrail through the signature or Contacts"),
    "CH-FILT1": _channel("ch_filt1", "FILT", ["Copperleaf Games"], "slack-thread-reply", "exact_predicate", "Robert's pasted offer in a reply under an unrelated #executives post is not found"),
    "CH-FILT2": _channel("ch_filt2", "FILT", ["Redwood Arcade"], "linear-comment", "exact_predicate", "the ENG-2362 comment behind Arthur's #analytics pointer is not opened"),
    "CH-EXC": _channel("ch_exc", "EXC", ["Northglow Publishing", "Pinegrove Games"], "sync-record", "authority", "the August position is not applied to the terms that take what we keep"),
    "CH-INPUT": _channel("ch_input", "INPUT", ["Sunfold Mobile"], "card-comment", "superseding", "the comment on F/up with Lena is not read"),
    "CH-DATE": _channel("ch_date", "DATE", ["Harbor Lane Games", "Wavecrest Play"], "esg-thread", "effective_date", "the ESG thread is not read: net-60 advances look like Q4 money"),
    "CH-FOLLOW": _channel("ch_follow", "FOLLOW", ["Tallwater Games", "Harbor Lane Games", "Wavecrest Play"], "bridge-reply", "authority", "Leonard's standing line under the Matthew post is not found"),
    "CH-SLIP": {"kind": "scale", "degrade": None, "members": [], "latent": "member", "family": "slip",
                "slots": ["S_live_PA", "S_live_PG", "S_passed_1", "S_silent_1", "V12_Harbor"],
                "description": "a base slip on a control row"},
}
OPS = {c["degrade"]: (c["rule"], frozenset(c["members"])) for c in CHANNELS.values() if c.get("degrade")}
TOUCHED = {"DONE": {"Oakline Games"}, "CORR": {"Tallwater Games"}, "ALIAS": {"Moonrail Studios"},
           "FILT": {"Copperleaf Games", "Redwood Arcade"}, "EXC": {"Northglow Publishing", "Pinegrove Games"},
           "INPUT": {"Sunfold Mobile"}, "DATE": {"Harbor Lane Games", "Wavecrest Play"},
           "FOLLOW": {"Tallwater Games", "Harbor Lane Games", "Wavecrest Play", "Moonrail Studios"}}
EXISTING_CARD = {"Oakline Games": I["oakline_card"], "Sunfold Mobile": I["sunfold_card"]}
EXISTING_CONTACT = {"Moonrail Studios": I["anika_contact"], "Sunfold Mobile": I["lena_contact"]}
BASE_THREAD = {"Appodeal": B.BASE["appodeal_thread"], "Rayking Game": B.BASE["rayking_thread"]}


def load_state(sql_text, revision=None):
    from base_check import parse_sql
    by_id, mail = {}, collections.defaultdict(list)
    for x in parse_sql(sql_text):
        if x["op"] != "insert":
            continue
        r = x["row"]
        for k in ("id", "identifier", "contact_id", "spreadsheet_id", "document_id", "presentation_id", "event_id"):
            if r.get(k):
                by_id[str(r[k])] = r
        if x["table"] == "gmail.gmail_messages" and r.get("user_email") == FRED:
            mail[r["thread_id"]].append(r)
    for rs in mail.values():
        rs.sort(key=lambda r: r["date"])
    return {"by_id": by_id, "mail": dict(mail), "revision": revision or "rev1"}


def _hit(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def _off(rule, key, disable, degrade):
    return _hit(disable, rule, key) or any(r == rule and key in ms and _hit(degrade, op, key) for op, (r, ms) in OPS.items())


def _money(text):
    return int(text.replace(",", ""))


def _terms(text):
    """Rev share, advance, installs, net days and response date from a publisher's own wording."""
    share = re.search(r"(\d+)% of net", text, re.I)
    adv = re.search(r"\$([\d,]+) advance", text, re.I)
    inst = re.search(r"([\d,]+) installs a month", text, re.I)
    net = re.search(r"net (\d+) from signature", text, re.I)
    resp = re.search(r"respond by Oct (\d+)", text, re.I)
    if not (share and adv and inst and net and resp):
        return None
    return {"share": int(share.group(1)) / 100, "adv": _money(adv.group(1)), "inst": _money(inst.group(1)),
            "net": int(net.group(1)), "respond": D.date(2025, 10, int(resp.group(1)))}


def _sent(state):
    grid = json.loads(state["by_id"][I["outreach_sheet"]]["grid_json"])
    head = grid[0]
    return {row[0]: row[head.index("What we sent")] for row in grid[1:] if row and row[0]}


def _thread_state(rows):
    """(a real reply came back, it was a no, the last real message is theirs)."""
    real = [r for r in rows if not str(r["subject"]).startswith("Automatic reply")]
    theirs = [r for r in real if r["from_email"] != FRED]
    no = any(re.search(r"\bpass\b", str(r["body_text"])) for r in theirs)
    return bool(theirs), no, bool(real) and real[-1]["from_email"] != FRED


def _signing(state):
    note = state["by_id"].get(MSG["esg_note"])
    hit = re.search(r"for signature is Nov (\d+)", str((note or {}).get("body_text")))
    return D.date(2025, 11, int(hit.group(1))) if hit else None


def _payments(k, t, sign, oak_first_look_returned):
    """Advance money as (amount, landing date); landing None means already banked before Oct 1."""
    if k == "Oakline Games":
        first = 10000                # Arthur, Sep 30: resent next week, so it lands in Q4 once the reply is read
        rest = t["adv"] - first
        return [(first, D.date(2025, 10, 8) if oak_first_look_returned else None), (rest, sign + D.timedelta(days=30))]
    return [(t["adv"], sign + D.timedelta(days=t["net"]))]


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    b = state["by_id"]
    have = lambda i: i in b          # noqa: E731
    sent = _sent(state)
    out = {}
    for m in B.M:
        k = m["key"]
        if keys_ is not None and k not in keys_:
            continue
        # ---- terms in writing, wherever they are
        terms, ev = None, []
        if k == "Copperleaf Games":
            if have(SL["copperleaf_relay"]) and not _off("FILT", k, disable, degrade):
                terms, ev = _terms(b[SL["copperleaf_relay"]]["text"]), [SL["copperleaf_relay"]]
        elif k == "Redwood Arcade":
            if have(I["eng2362_comment"]) and not _off("FILT", k, disable, degrade):
                terms, ev = _terms(b[I["eng2362_comment"]]["body"]), [I["eng2362_comment"]]
        elif k in B.TERM_DOCS and have(B.term(k)):
            terms, ev = _terms(b[B.term(k)]["body_text"]), [B.term(k)]
        if k in ("Copperleaf Games", "Redwood Arcade") and terms is None:
            out[k] = _blank(k)       # outside the sheet and the inbox: never reaches the model
            continue
        # ---- designed corrections to the latest terms
        if terms and k == "Tallwater Games" and have(I["pb_event"]) and not _off("CORR", k, disable, degrade):
            hit = re.search(r"advance is \$([\d,]+) now", str(b[I["pb_event"]]["description"]))
            if hit:
                terms["adv"] = _money(hit.group(1))
        if terms and k == "Sunfold Mobile" and have(I["sunfold_comment"]) and not _off("INPUT", k, disable, degrade):
            hit = re.search(r"commit ([\d,]+) installs", str(b[I["sunfold_comment"]]["data_json"]))
            if hit:
                terms["inst"] = _money(hit.group(1))
        # ---- over-application of the corrections
        if terms and k == "Harbor Lane Games" and _hit(degrade, "corr_over", k):
            terms["adv"] = 20000
        if terms and k == "Oakline Games" and _hit(degrade, "input_over", k):
            terms["inst"] = 12000
        # ---- status, first that fits
        tid = BASE_THREAD.get(k) or B.thr(k)
        rows = state["mail"].get(tid, [])
        replied, said_no, theirs_last = _thread_state(rows)
        takes_rights = bool(terms) and k in B.TERM_DOCS and re.search(
            r"all digital storefronts|source code", b[B.term(k)]["body_text"]) is not None
        if k == "Moonrail Studios" and have(SL["kestrel_post"]) and not _off("ALIAS", k, disable, degrade):
            status = "Withdrawn"
        elif takes_rights and have(B.term(k)) and not _off("EXC", k, disable, degrade):
            status = "Out on rights"
        elif terms:
            status = "Live"
        elif said_no:
            status = "Passed"
        elif k in BASE_THREAD or (replied and theirs_last):
            status = "Waiting on us"
        else:
            status = "No reply"
        if k == "Wavecrest Play" and _hit(degrade, "alias_over", k):
            status = "Withdrawn"
        if k == "Sunfold Mobile" and _hit(degrade, "exc_over", k):
            status = "Out on rights"
        # ---- valuing a Live offer
        adv = inst = v12 = q4 = None
        banked = 0
        if status == "Live":
            adv, inst = terms["adv"], terms["inst"]
            gross = inst * 12 * ARPI
            v12 = round(max(terms["share"] * gross, adv))
            date_off = _off("DATE", k, disable, degrade)
            sign = (_signing(state) if not date_off else None) or ORIGINAL_SIGNING
            returned = have(SL["arthur_cash"]) and not _off("DONE", k, disable, degrade)
            pays = _payments(k, terms, sign, returned)
            banked = sum(a for a, d in pays if d is None)
            q4 = sum(a for a, d in pays if d and Q4_START <= d <= Q4_END)
            if k == "Tallwater Games" and _hit(degrade, "done_over", k):
                q4 = 0
            if k == "Sunfold Mobile" and _hit(degrade, "date_over", k):
                q4 = 0
        # ---- writes this publisher is owed
        groups = ["register"]
        gave_terms_or_no = bool(terms) or said_no
        if gave_terms_or_no and m.get("person") and k not in EXISTING_CONTACT:
            groups.append("contact_add")
        if status in ("Live", "Waiting on us", "No reply"):
            groups.append("card_comment" if k in EXISTING_CARD else "card_new")
        if status == "Live":
            groups.append("reminder")
        if status == "No reply":
            groups.append("nudge")
        owes_note = status == "Live" and sent.get(k) == "May one-pager" and have(SL["standing_line"]) \
            and not _off("FOLLOW", k, disable, degrade)
        if owes_note or (k == "Oakline Games" and _hit(degrade, "follow_over", k)):
            groups.append("organic_note")
        if not ev:
            ev = [BASE_THREAD[k]] if k in BASE_THREAD else [rows[-1]["id"]] if rows else []
        out[k] = {"Publisher": k, "Status": status, "Advance": adv, "Monthly installs": inst, "12-month value": v12,
                  "Q4 cash": q4, "Banked": banked, "Respond by": terms["respond"].isoformat() if status == "Live" else None,
                  "groups": sorted(groups), "evidence": {"Publisher": ev}}
    for k in OUT_KEYS:
        if keys_ is not None and k not in keys_:
            continue
        out[k] = _blank(k)
        if k == "Homa" and _hit(degrade, "filt_over", k):
            out[k].update({"Status": "Waiting on us", "groups": ["card_new", "register"]})
    return out


def _blank(k):
    return {"Publisher": k, "Status": None, "Advance": None, "Monthly installs": None, "12-month value": None,
            "Q4 cash": None, "Banked": 0, "Respond by": None, "groups": [], "evidence": {"Publisher": []}}


def aggregates(rows):
    groups = collections.defaultdict(list)
    for k in sorted(rows):
        for g in rows[k]["groups"]:
            groups[g].append(k)
    listed = [v for v in rows.values() if v["Status"]]
    live = sorted((v for v in listed if v["Status"] == "Live"), key=lambda v: (-v["12-month value"], v["Publisher"]))
    top = live[0] if live else None
    keep = round(sum(B.KEEP_MONTHS.values()) / 3 * 12, 2)
    n = lambda g: len(groups.get(g, []))     # noqa: E731
    classes = dict(sorted(collections.Counter(v["Status"] for v in listed).items()))
    return {"classes": classes, "groups": {g: groups[g] for g in sorted(groups)},
            "totals": {"publishers": len(listed), "first_pick": top["Publisher"] if top else None,
                       "first_pick_value": top["12-month value"] if top else None,
                       "first_pick_q4": top["Q4 cash"] if top else None,
                       "banked": sum(v["Banked"] for v in listed), "keep_value": keep,
                       "contacts_added": n("contact_add"), "cards_new": n("card_new"), "card_comments": n("card_comment"),
                       "reminders": n("reminder"), "organic_notes": n("organic_note"), "nudges": n("nudge"),
                       "checklists": len(classes), "checklist_items": len(listed)}}


def evidence(rows, key, field):
    return list(rows[key]["evidence"]["Publisher"]) if field == "Publisher" else []


def touched(state, rule):
    return set(TOUCHED[rule])


def deciding(state, rule, key):
    return {"DONE": [SL["arthur_cash"]], "CORR": [I["pb_event"]], "ALIAS": [SL["kestrel_post"], I["anika_contact"]],
            "FILT": [SL["copperleaf_relay"] if key == "Copperleaf Games" else I["eng2362_comment"]],
            "EXC": [B.term(key)] if key in B.TERM_DOCS else [], "INPUT": [I["sunfold_comment"]], "DATE": [MSG["esg_note"], MSG["esg_leo"]],
            "FOLLOW": [SL["standing_line"]]}[rule]


def base_route(record_id):
    if record_id in BASE_THREAD.values():
        return {"service": "gmail", "file": "threads/frederick@harmonygames.co_" + record_id.split("/")[1] + ".json",
                "pointer": "/messages", "field": "thread_id"}
    return None
