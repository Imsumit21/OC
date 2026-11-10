"""Solver for Robert: the seed, bet by bet (tools/oracle_kit.py contract), rev1.

Truth = the sheet Robert should write at the end of Fri Feb 13, 2026: one row per payee on the SVB Payment Processed
notices (22), columns Payee, Name on the bank, Bucket, Domino Delights, ZM, Combo Fighter, Company, Note. The three bet
columns show each payee's figure where the Transaction Date puts it, whatever the bucket (design section 2); build cost
per bet is the column summed over the Build rows only. Company shows a Company row's dollars, or its own currency. The
hidden fields (paid, notices_sum, notices, company_usd, company_bgn) carry the arithmetic for aggregates().

Built from the base universe plus the injection SQL (parsed with tools/base_check.parse_sql; never executed).
Per-payee values no mechanism changes come from the notices (00_PreScenario/svb_processed_robert.json, all 132 re-read
through tools/hg.py: payee, amount, currency, Transaction Date) and plan/cohort.json. One rule per mechanism_portfolio
entry, read from the draft manifest with the manifest's channels, so the solver and the design can't drift. A rule acts
only while the method carries its sentence and its seeded record is in the SQL; it falls back to its natural reading when
`disable` switches it off (whole or per key set), when `ch_miss` hits the key, or when either record is absent.
Over-application operators act on the declared controls only. The solver is key-local: a rule, a channel and an
operator each touch their own keys.

The method doc gates all seven rules, so it is not in deciding(): an intervention removing it would flip every rule and
hide a dead rule-level record. Each rule's deciding() record is the one it has alone. plan/run_preflight.sh checks the
method removal separately.

Comment ids come from plan/sql_ids.json and note text is never matched, so per-payee notes can be reworded or added. The
statement's first wire and Arthur's mail are read as text: their amounts come from the SQL rows.
"""
import collections
import datetime as dt
import json
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
PLAN = WF / "plan"
COHORT = json.loads((PLAN / "cohort.json").read_text())
SQLIDS = json.loads((PLAN / "sql_ids.json").read_text())
_IDS = json.loads((PLAN / "ids.json").read_text())
IDS, BASE, ISSUE = _IDS["IDS"], _IDS["BASE"], _IDS["issues"]
DRAFT = json.loads((WF / "01_Hardness_Manifest.draft.json").read_text())
NOTICES = json.loads((WF / "00_PreScenario" / "svb_processed_robert.json").read_text())

ROB = "robert@harmonygames.co"
DD, ZM, CF = "Domino Delights", "ZM", "Combo Fighter"
BETS = (DD, ZM, CF)
KEY_REGEX = r"(?:Payee 1|[A-Za-z0-9][A-Za-z0-9 .()&/-]*)"
FIELDS = ["Payee", "Name on the bank", "Bucket", DD, ZM, CF, "Company", "Note"]
CLASS_FIELD, GROUPS_FIELD = "Bucket", "groups"
MOTMOT, LUCAS, LEAPBLOCK, JPM, NODE, BROOKS, MARTIN = ("MotMot", "Lucas", "Leapblock", "JPMorgan", "Node Media",
                                                       "Lauren Brooks", "Martin Walsh")

# ---- base values, fixed here; each re-read through tools/hg.py
REVENUE = {DD: 12331.25, ZM: 11.99, CF: None}   # the method leaves Combo Fighter's off for now (NB-26); the table holds 11.75   # ANALYTICS.MONETIZATION.REVENUE_DAILY (snowflake.json /tables/12, 2,284 rows),
                                                 # SUM(total_revenue_usd) by game_id, last date 2026-02-09
RETURNED = 403200                # BANCO ***8605 $4,032, Transaction Date 2024-04-02 (threads/00004088.json); Arthur "messed up
                                 # the bank account number" C04UEQVDVB7/1712331718.859679; Leonard "money returned to us"
                                 # C04UEQVDVB7/1712901800.684259; the Apr 5 wire to ***3341 (threads/00004124.json) stands
RETURNED_DATE = "2024-04-02"
WU = (("2024-06-03", 107500), ("2024-06-17", 107500), ("2024-06-29", 107500), ("2024-07-23", 215000), ("2024-08-23", 215000))
                                 # the five Western Union receipts, amount sent without the fee: threads/00005184, 00005350,
                                 # 00005489, 00005962, 00006329 (robert@harmonygames.co/1800873055214061794 ... 1808201559428745555)
BGN_CENTS = 199900               # Martin Walsh ***3801, 1,999.00 BGN, 2025-10-30 (threads/00015809.json message 2); his laptop
                                 # C04UEQVDVB7/1761844454.096829
BGN_DATE = "2025-10-30"
# the over-application values, also base records
LB_AUG_REPEAT = 370000           # Leapblock $3,700 on 2025-08-01 and again on 2025-08-29: separate months, both stand
ANIMATOR = 540000                # "$5400 for 9 characters" D04UP2L3E3S, on a card, no receipt (T13)
EVELINE_AWAITING = 372000        # Eveline Art $3,720 Awaiting Approval, threads/00016669.json, before its Feb 2, 2026 wire
SINGULAR_2025 = 625000           # Singular $6,250, 2025-09-26
BROOKS_FIRST = 50000             # Lauren Brooks $500, 2025-10-30
BASE_PAYEE_TS = {NODE: "1735854841.070019",      # Leonard: "closing our account with Node Media LLC"
                 LUCAS: "1719603220.131689"}     # Robert: "2nd half of June's payment to Lucas OK to go?"
SLACK_TS_CHANNEL = {"1735854841.070019": "C04UEQVDVB7", "1719603220.131689": "C04UEQVDVB7"}

# the method sentence each rule needs (seeded doc IDS["method"], read from the SQL)
CLAUSE = {"RET": "unless one of us has said the money came back", "OFF": "only if a receipt for it reached your mail",
          "ORPH": "closes out their file with us", "CORR": "between our own accounts",
          "ALIAS": "Marketing is anything made or bought to get installs",
          "CLASS": "Marketing is anything made or bought to get installs",
          "CURR": "Anything not paid in dollars stays in its own currency"}
DECIDES = {"RET": [DD, ZM, "Note"], "OFF": [DD, ZM, "Note"], "ORPH": [DD, CF, "Note"], "CORR": ["Bucket", ZM, "Company", "Note"],
           "ALIAS": ["Bucket", "Note"], "CLASS": ["Bucket", "Note"], "CURR": ["Bucket", ZM, "Company", "Note"]}
TOUCHED = {"RET": MOTMOT, "OFF": LUCAS, "ORPH": LEAPBLOCK, "CORR": JPM, "ALIAS": NODE, "CLASS": BROOKS, "CURR": MARTIN}
# alias_over's own words name a studio; the portfolio's control Adjoe is already Marketing and it can't move there
EXTRA_CONTROLS = {"ALIAS": [LEAPBLOCK]}

RULES = {p["id"]: {"mechanism": p["mechanism"], "requirement": p["requirement"], "nodes": list(p["nodes"]),
                   "decides": DECIDES[p["id"]], "family": p["prior_family"], "source": p["source"],
                   "natural_reading": p["natural_reading"], "signature": p["signature"],
                   "controls": list(p["controls"]) + EXTRA_CONTROLS.get(p["id"], []),
                   "over_application": p["over_application"].split(":", 1)[0].strip()}
         for p in DRAFT["mechanism_portfolio"]}
DEGRADES = {p["over_application"].split(":", 1)[0].strip(): p["over_application"].split(":", 1)[1].strip()
            for p in DRAFT["mechanism_portfolio"]}
DEGRADES["ch_miss"] = "a channel member's deciding record is not found: the member takes its rule's natural reading"
CHANNELS = {c["id"]: {k: c[k] for k in ("kind", "degrade", "members", "latent", "family", "rule", "source", "description")}
            for c in DRAFT["channels"]}
MEMBER_RULES = collections.defaultdict(set)
for _c in CHANNELS.values():
    for _m in _c["members"]:
        MEMBER_RULES[_m].add(_c["rule"])

MATCH = (("Deel", "Deel"), ("[ORG_NAME_0057]", "Deel"), ("Leapblock", LEAPBLOCK), ("Eveline", "Eveline Art"), ("BANCO", MOTMOT),
         ("Adjoe", "Adjoe"), ("[SOURCE_ORG_0351]", "Singular"), ("Singular", "Singular"), ("PERSON_4419", NODE),
         ("TYZ", "TYZ Law Group"), ("[PERSON_NAME_7200]", "Trademark lawyer"), ("[PERSON_NAME_36400]", LUCAS),
         ("AppLovin", "AppLovin"), ("Graham", "Graham Porter"), ("JPMorgan", JPM), ("CREATIVE", "Creative X"),
         ("M [PERSON", "JP (website)"), ("Nathan", "Nathan Price"), ("Martin", MARTIN), ("[PERSON_NAME_7249]", BROOKS),
         ("PERSON_6074", "Ozhan"), ("[PERSON_NAME_9100]", "UX contractor"), ("[PERSON_NAME_0054]", "4X helper"), ("Private", "Oleg"))


def bet(date):
    """Which bet a Transaction Date falls in, the whole payment to one bet (the method's calendar)."""
    return DD if date <= "2025-01-08" else (ZM if date <= "2025-11-23" else CF)


def _payee(to):
    return next(v for k, v in MATCH if k in to)


CELL, COUNT = {p[0]: {b: 0 for b in BETS} for p in COHORT}, collections.Counter()
for _n in NOTICES:
    _p = _payee(_n["to"])
    COUNT[_p] += 1
    CELL[_p][bet(_n["txn"])] += round((_n["usd"] or 0) * 100)    # the one non-dollar notice has usd None: see BGN_CENTS


def _notes(key):
    return [c["id"] for c in SQLIDS["linear"].get(key, {}).get("comments", [])]


R_STATEMENT = SQLIDS["slack"]["statement"]["id"]             # Leapblock's closing statement in #leapblock
R_ARTHUR = SQLIDS["gmail"]["arthur_mail"][ROB]["message"]    # Arthur's Chase mail, Robert's copy
SEEDED = {"RET": _notes(MOTMOT), "OFF": _notes(LUCAS), "ORPH": [R_STATEMENT], "CORR": [R_ARTHUR], "ALIAS": _notes(NODE),
          "CLASS": _notes(BROOKS), "CURR": _notes(MARTIN)}


def load_state(sql_text, revision=None):
    from base_check import parse_sql
    by_id, method = {}, ""
    for x in parse_sql(sql_text):
        if x["op"] != "insert":
            continue
        r = x["row"]
        for k in ("id", "identifier", "document_id", "spreadsheet_id", "presentation_id", "event_id", "contact_id"):
            if r.get(k):
                by_id[str(r[k])] = r
        if x["table"].endswith("docs_documents") and r.get("document_id") == IDS["method"]:
            method = str(r.get("body_text") or "")
    return {"by_id": by_id, "method": method, "revision": revision or "rev1"}


def _hit(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def _on(state, rule, key, disable, degrade):
    if _hit(disable, rule, key) or (rule in MEMBER_RULES.get(key, ()) and _hit(degrade, "ch_miss", key)):
        return False
    return CLAUSE[rule] in state["method"] and any(i in state["by_id"] for i in SEEDED[rule])


def _statement_wire(state):
    """(date, cents) of the wire only Leapblock's statement proves, from the statement's own words, else None."""
    m = re.search(r"(\d{4}) \(from (\d{1,2}) ([A-Z][a-z]{2}), the first one ([\d,]+)\)",
                  str((state["by_id"].get(R_STATEMENT) or {}).get("text") or ""))
    if not m:
        return None
    date = dt.datetime.strptime(f"{m.group(2)} {m.group(3)} {m.group(1)}", "%d %b %Y").strftime("%Y-%m-%d")
    return date, int(m.group(4).replace(",", "")) * 100


def _own_account(state):
    """True when Arthur's mail says the JPMorgan wire went to the company's own Chase account for the notice's amount."""
    text = " ".join(str((state["by_id"].get(R_ARTHUR) or {}).get("body_text") or "").split())
    m = re.search(r"\$([\d,]+) to JPMorgan", text)
    return bool(m) and "own Chase account" in text and int(m.group(1).replace(",", "")) * 100 == sum(CELL[JPM].values())


def _row(state, p, disable, degrade):
    k, spell, _, bucket = p[0], p[1], p[2], p[3]
    b = state["by_id"]
    on = lambda rule: _on(state, rule, k, disable, degrade)      # noqa: E731
    c = dict(CELL[k])
    note, bgn, ev_fix = "", 0, []
    # ---- RET: the Apr 2 wire to ***8605 came back; the re-send to ***3341 stands
    if k == MOTMOT and on("RET"):
        c[bet(RETURNED_DATE)] -= RETURNED
        note = "net of the $4,032 wire to ***8605 the bank returned in Apr 2024"
        ev_fix = [BASE["wrong_acct"], BASE["returned"], BASE["n_ban_first"]]
    # ---- OFF: five Western Union transfers on the company card, each by its own date, at the amount sent
    if k == LUCAS and on("OFF"):
        for date, cents in WU:
            c[bet(date)] += cents
        note = "with $7,525 sent by Western Union on the company card, Jun to Aug 2024"
        ev_fix = [BASE[f"wu{i}"] for i in range(1, 6)]
    # ---- ORPH: the wire with no Processed notice, on the statement's word
    if k == LEAPBLOCK and on("ORPH") and _statement_wire(state):
        date, cents = _statement_wire(state)
        c[bet(date)] += cents
        note = "with the $33,290 wire of Sep 13, 2023, which has no Processed notice; Leapblock's statement counts it"
        ev_fix = [R_STATEMENT, BASE["lb_await"], BASE["lb_done"]]
    # ---- CORR: the company's own Chase account is not a cost, so the line stays at zero (the method: every payee keeps its
    # line); natural reading: a cost of the bet running that month
    if k == JPM:
        if on("CORR") and _own_account(state):
            c = {bt: 0 for bt in BETS}
            note = "$4,000 to the company's own Chase account, put back after Carta's renewal; it never left"
            ev_fix = [R_ARTHUR]
        else:
            bucket = "Build"
    # ---- ALIAS: the token LLC is Node Media, a UA agency; natural reading: a build vendor of the bet running that day
    if k == NODE:
        if on("ALIAS"):
            note = "Node Media, the UA agency: Sept, Oct and Nov 2024 invoices"
            ev_fix = [BASE["node_close"], BASE["node_mail"]]
        else:
            bucket = "Build"
    # ---- CLASS: her contract's work decides the bucket; natural reading: a monthly contractor is build cost
    if k == BROOKS:
        if on("CLASS"):
            note = "paid UA on Telegram under her contract"
            ev_fix = [IDS["c_brooks"], BASE["brooks_contract"]]
        else:
            bucket = "Build"
    # ---- CURR: Martin's laptop stays in BGN on the Company line; natural reading: $1,999 of build cost by date
    if k == MARTIN:
        if on("CURR"):
            bgn = BGN_CENTS
            note = "his laptop, paid in BGN; out of every dollar total"
            ev_fix = [BASE["bgn_notice"], BASE["laptop"]]
        else:
            bucket = "Build"
            c[bet(BGN_DATE)] += BGN_CENTS
    # ---- Leonard's ENG-2459 note: the wire came back, and the Payoneer re-send left no receipt in Robert's mail (a line at zero)
    if k == "Oleg" and any("came back" in str((b.get(i) or {}).get("body") or "") for i in _notes(k)):
        c = {bt: 0 for bt in BETS}
        note = "the wire came back the same day; no receipt for the re-send reached this mail, so the line is zero"
        ev_fix = _notes(k)
    # ---- over-application operators on the controls
    if k == LEAPBLOCK and _hit(degrade, "ret_over", k):
        c[ZM] -= LB_AUG_REPEAT
    if k == "Graham Porter" and _hit(degrade, "off_over", k):
        c[ZM] += ANIMATOR
    if k == "Eveline Art" and _hit(degrade, "orph_over", k):
        c[CF] += EVELINE_AWAITING
    if k == "Singular" and _hit(degrade, "corr_over", k):
        c[ZM] -= SINGULAR_2025
    if k == LEAPBLOCK and _hit(degrade, "alias_over", k):
        bucket = "Marketing"
    if k == "Graham Porter" and _hit(degrade, "class_over", k):
        bucket = "Marketing"
    if k == BROOKS and _hit(degrade, "curr_over", k):
        c[ZM] -= BROOKS_FIRST
    # ---- the row
    paid = sum(c.values())
    plain = sum(CELL[k].values())
    company = paid if bucket == "Company" else 0
    row = {"Payee": k, "Name on the bank": spell, "Bucket": bucket, DD: c[DD] / 100, ZM: c[ZM] / 100, CF: c[CF] / 100,
           "Company": f"{bgn / 100:,.2f} BGN" if bgn else company / 100, "Note": note, "paid": paid / 100,
           "notices_sum": plain / 100, "notices": COUNT[k], "company_usd": company / 100, "company_bgn": bgn / 100}
    groups = [bucket.lower().replace(" ", "_")]
    if paid != plain:
        groups.append("reason_comment")       # the method: say why on the issue when the figure isn't the notices'
    row["groups"] = sorted(groups)
    ev = {}
    issue = ISSUE[k]
    if issue in b:
        ev["Name on the bank"] = [issue]
        ev["Bucket"] = [i for i in _notes(k) if i in b] or [issue]
        if k in str(b[issue].get("title") or ""):
            ev["Payee"] = [issue]
    if "Payee" not in ev:
        said = [i for i in _notes(k) if i in b and k in str(b[i].get("body") or "")]
        if said:
            ev["Payee"] = said[:1]
        elif k in BASE_PAYEE_TS:
            ev["Payee"] = [BASE_PAYEE_TS[k]]
    if ev_fix:
        ev["adjustment"] = ev_fix
    row["evidence"] = ev
    return row


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    out = {}
    for p in COHORT:
        if keys_ is None or p[0] in keys_:
            out[p[0]] = _row(state, p, disable, degrade)
    return out


def _cents(v):
    return round(v * 100)


def totals(rows):
    build = {bt: sum(_cents(r[bt]) for r in rows.values() if r["Bucket"] == "Build") / 100 for bt in BETS}
    marketing = sum(_cents(r["paid"]) for r in rows.values() if r["Bucket"] == "Marketing") / 100
    left_out = sum(_cents(r["notices_sum"]) for r in rows.values() if r["Bucket"] == "Not a cost") / 100
    return {"build": build, "company_usd": sum(_cents(r["company_usd"]) for r in rows.values()) / 100,
            "company_bgn": sum(_cents(r["company_bgn"]) for r in rows.values()) / 100, "marketing_usd": marketing,
            "not_a_cost_usd": left_out, "revenue": dict(REVENUE)}


def aggregates(rows):
    groups = collections.defaultdict(list)
    for k in sorted(rows):
        for g in rows[k]["groups"]:
            groups[g].append(k)
    return {"classes": dict(sorted(collections.Counter(v["Bucket"] for v in rows.values()).items())),
            "groups": {g: groups[g] for g in sorted(groups)}, "totals": totals(rows)}


def evidence(rows, key, field):
    return list((rows[key].get("evidence") or {}).get(field, []))


def touched(state, rule):
    return {TOUCHED[rule]}


def deciding(state, rule, key):
    return list(SEEDED[rule]) if key == TOUCHED[rule] else []


def base_route(record_id):
    """Where a base record used as golden evidence lives in the exports; seeded records are read from the SQL index."""
    rid = str(record_id or "")
    if rid in SLACK_TS_CHANNEL:
        month = dt.datetime.fromtimestamp(float(rid), dt.timezone.utc).strftime("%Y-%m")
        return {"service": "slack", "file": f"messages/{SLACK_TS_CHANNEL[rid]}/{month}.json", "pointer": "", "field": "ts"}
    return None
