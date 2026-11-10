#!/usr/bin/env python3
"""Build 09_Rubrics.json, the V3 rubric_rows evidence and rows.json for Robert's seed-bets page (task_inputsS2).

Every figure comes from solver/truth.json and is asserted against the Oracle Events text. Every quote in an evidence
field is asserted as a substring of its record. The rubric text carries no em dash, no en dash and no local file reference.
"""
import datetime as dt
import json
import os
import re
import subprocess
import sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
PLAN = os.path.dirname(HERE)
WF = os.path.dirname(PLAN)
TI = os.path.dirname(WF)
TA = os.path.dirname(TI)
WS = os.path.dirname(TA)
sys.path.insert(0, os.path.join(TA, "tools"))
from base_check import parse_sql  # noqa: E402

SQL = open(os.path.join(TI, "01_Universe_Inject.sql"), encoding="utf-8").read()
STMTS = parse_sql(SQL)
PROMPT = open(os.path.join(TI, "04_Prompt.txt"), encoding="utf-8").read()
OE_TEXT = open(os.path.join(TI, "08_Oracle_Events.md"), encoding="utf-8").read()
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json"), encoding="utf-8"))
MAN = json.load(open(os.path.join(WF, "01_Hardness_Manifest.json"), encoding="utf-8"))
NODES = {m["id"]: " ".join(m["nodes"]) for m in MAN["mechanism_portfolio"]}

GM = "Universe_Normal/Normal_HarmonyGames_Gmail/Services_Data/gmail/threads/%s.json"
SL = "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/slack/messages/%s/%s.json"
GD = "Universe_Normal/Normal_HarmonyGames_Other_Services/Services_Data/gdocs/data.json"

SP_SHEET = "Build that page as a sheet in my Drive"
SP_SHARE = "share it with him and Blake"
SP_COUNT = "He laid out how he wants it counted and how it should look"
SP_LINEAR = "Work through the Payee history project in Linear the way he wants"
SP_REPLY = "reply to him in #winddown with what each bet cost to build and brought in and what changes on the draft deck, with the link to the sheet"
SP_DONE = "When you're done, reply to him in #winddown"
for sp in (SP_SHEET, SP_SHARE, SP_COUNT, SP_LINEAR, SP_REPLY, SP_DONE):
    assert sp in PROMPT, sp

DOC = "f_6feda53b2382c63bf47b25"
SHEET = "f_3304033843904a426f3c00"
DECK = "f_a4b3c4287a4314d8e532e1"
WD = "C0ADGSZKR3R"
FOUNDERS = "C04UEQVDVB7"
LEAP = "C05URGU759U"
MB = "robert@harmonygames.co/"
START = ("gdocs", DOC)
VIA = [START]
SH = "its sheet for Leonard"
RP = "its #winddown reply"


def path(*hops):
    return [{"service": s, "id": i} for s, i in hops]


def sql_ins(table, **ident):
    rows = [x["row"] for x in STMTS if x.get("table") == table and x["op"] == "insert" and all(x["row"].get(k) == v for k, v in ident.items())]
    assert len(rows) == 1, (table, ident, len(rows))
    return rows[0]


def S(service, rid, table, ident, column, rec_col, hops, why):
    row = sql_ins(table, **ident)
    if tuple(hops[-1]) != (service, rid):
        hops = [*hops, (service, rid)]
    return {"service": service, "id": rid, "source_file": "01_Universe_Inject.sql", "table": table, "identity": ident, "column": column,
            "source_value": row[column], "evidence_path": path(*hops), "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_column": rec_col,
                                  "rationale": f"Seeded {table} row; {rec_col} = {row[rec_col]} (before the freeze)."}}


_files = {}


def jload(p):
    if p not in _files:
        _files[p] = json.load(open(os.path.join(WS, p), encoding="utf-8"))
    return _files[p]


def B_mail(fname, thread, idx, hops, why, field="body"):
    p = GM % fname
    d = jload(p)
    assert d["id"] == MB + thread, (fname, d["id"])
    m = d["messages"][idx]
    return {"service": "gmail", "id": MB + thread, "source_file": p, "pointer": f"/messages/{idx}/{field}", "source_value": m[field],
            "evidence_path": path(*hops, ("gmail", MB + thread)), "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_pointer": f"/messages/{idx}/date_parsed",
                                  "rationale": f"Base message dated {m['date_parsed']}, before the freeze; a sent mail does not change."}}


def B_slack(ch, ts, hops, why):
    mon = dt.datetime.fromtimestamp(float(ts), dt.timezone.utc).strftime("%Y-%m")
    p = SL % (ch, mon)
    arr = jload(p)
    i = next(j for j, m in enumerate(arr) if m.get("ts") == ts)
    rid = f"{ch}/{ts}"
    return {"service": "slack", "id": rid, "source_file": p, "pointer": f"/{i}/text", "source_value": arr[i]["text"],
            "evidence_path": path(*hops, ("slack", rid)), "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_pointer": f"/{i}/ts",
                                  "rationale": f"Base Slack post, ts {ts}, before the freeze."}}


def B_doc(doc, hops, why):
    idx = next(i for i, d in enumerate(jload(GD)["docs_documents"]) if d["document_id"] == doc)
    d = jload(GD)["docs_documents"][idx]
    return {"service": "gdocs", "id": doc, "source_file": GD, "pointer": f"/docs_documents/{idx}/body_text", "source_value": d["body_text"],
            "evidence_path": path(*hops, ("gdocs", doc)), "reachability_rationale": why,
            "temporal_evidence": {"value_semantics": "fact", "mutable_state": False, "recorded_at_pointer": f"/docs_documents/{idx}/modified_time",
                                  "rationale": f"Base document last modified {d['modified_time']}, before the freeze."}}


def nz(s):
    return re.sub(r"\s+", " ", (s or "").replace("\\n", " ").replace("''", "'").replace("’", "'")).strip()


REC = {}
SQLN = nz(SQL)


def rec(key, label, source, *quotes):
    txt = nz(str(source["source_value"]))
    for q in quotes:
        assert nz(q) in txt, (key, q)
    REC[key] = {"label": label, "src": source, "quotes": quotes}


def note(key, label, *quotes):
    """A record cited only in the evidence text; its quotes are asserted against the injection SQL."""
    for q in quotes:
        assert nz(q) in SQLN, (key, q)
    REC[key] = {"label": label, "src": None, "quotes": quotes}


def frag(key, *which):
    r = REC[key]
    qs = [r["quotes"][i] for i in which] if which else list(r["quotes"])
    return r["label"] + (" (" + "; ".join(f"'{q}'" for q in qs) + ")" if qs else "")


# ---- records -----------------------------------------------------------------------------------------------------------
MQ = ["Every payee keeps its line, even at zero.",                                                                             # 0
      "Take a notice as paid unless one of us has said the money came back.",                                                  # 1
      "If someone we paid closes out their file with us and tells us what they received, that beats the notices for them.",   # 2
      "Money we moved between our own accounts isn’t spending, no bucket for that.",                                           # 3
      "If we paid a contractor some other way, it goes in only if a receipt for it reached your mail, at the amount sent, not the fee.",  # 4
      "Build is the team on Deel plus the studios and freelancers who made the games.",                                        # 5
      "Everything on Deel counts as team",                                                                                     # 6
      "Marketing is anything made or bought to get installs",                                                                  # 7
      "Company is legal, tools, the website, equipment and anything else that wasn’t for one of the three games: that goes in the Company column.",  # 8
      "Go by the Transaction Date on the notice, the whole payment to one bet",                                                # 9
      "Domino Delights up to Jan 8, 2025, ZM from Jan 9, 2025 to Nov 23, 2025, Combo Fighter from Nov 24, 2025.",              # 10
      "Anything not paid in dollars stays in its own currency next to the line.",                                              # 11
      "What each game brought in is its lifetime revenue from the warehouse’s daily revenue table, as recorded.",              # 12
      "Leave Combo Fighter’s revenue off for now, on the page, on the deck and when you tell me",                              # 13
      "move each payee’s issue to Done once its line is right",                                                                # 14
      "If your figure isn’t what the notices add up to, say why on the issue first.",                                          # 15
      "keep it out of build cost"]                                                                                             # 16
rec("method", f"Leonard's doc Angel note: how to count the money {DOC}",
    S("gdocs", DOC, "gdocs.docs_documents", {"document_id": DOC}, "body_text", "modified_time", VIA, "Leonard's Thursday post in #winddown names this doc."), *MQ)
ASK1, ASK2 = "1770945821.640039", "1770945859.212469"
rec("ask2", f"Leonard's post {WD}/{ASK2}",
    S("slack", f"{WD}/{ASK2}", "slack.slack_messages", {"ts": ASK2}, "text", "created_at", VIA, "It is Leonard's post in the channel the prompt names."),
    "use the layout of my Angel note working sheet, keep yours in your drive and share it with Blake and me",
    "when you’re done tell me here what each bet cost and brought in and what changes on the deck")
rec("ask1", f"Leonard's post {WD}/{ASK1}",
    S("slack", f"{WD}/{ASK1}", "slack.slack_messages", {"ts": ASK1}, "text", "created_at", VIA, "It is Leonard's post in the channel the prompt names."),
    "one straight page on what each bet cost us to build and what it brought in")
rec("layout", f"Leonard's sheet Angel note working {SHEET}",
    S("gsheets", SHEET, "gsheets.sheets_spreadsheets", {"spreadsheet_id": SHEET}, "title", "modified_time", [*VIA, ("gsheets", SHEET)], "Leonard's post names this sheet."))
note("layout_hdr", f"the header row of Leonard's sheet {SHEET}", '"Payee", "Name on the bank", "Bucket", "Domino Delights", "ZM", "Combo Fighter", "Company", "Note"')
rec("deck", f"the deck Note to angels (draft) {DECK}",
    S("gslides", DECK, "gslides.slides_presentations", {"presentation_id": DECK}, "title", "modified_time", [*VIA, ("gslides", DECK)], "Leonard's post refers to the draft deck; a Drive search for angel finds it."))
note("deck_cost", f"the cost slide of the deck {DECK}", "What each bet cost to build: Domino Delights $985K, ZM $609K, Combo Fighter $74K")
note("deck_rev", f"the revenue slide of the deck {DECK}", "What each brought in: to fill in")
rec("ret", f"Leonard's post {FOUNDERS}/1770947533.284619",
    S("slack", f"{FOUNDERS}/1770947533.284619", "slack.slack_messages", {"ts": "1770947533.284619"}, "text", "created_at", VIA, "The method doc says a notice stands unless a founder has said the money came back; this is the newest post in the founders' channel."),
    "that Apr 2024 wire to the account ending 8605 came back to us", "he re-sent it to 3341")
rec("close", f"Leapblock's close-out {LEAP}/1770971846.479179",
    S("slack", f"{LEAP}/1770971846.479179", "slack.slack_messages", {"ts": "1770971846.479179"}, "text", "created_at", VIA, "The method doc's close-out sentence leads to the channel of the payee on ENG-2439."),
    "Total 407,944 over 30 wires", "from 13 Sep, the first one 33,290")
rec("await", f"SVB's Payment Awaiting Approval mail in thread {MB}1776934359028762037",
    B_mail("00001577", "1776934359028762037", 0, VIA, "A Gmail search for the 33,290 in Leapblock's close-out finds it."), "33,290.00 USD", "Transaction Date: Sep 13 2023")
CHASE_ID = "robert@harmonygames.co/<CAOOpSqA2MTKGlKETvkoKqFfq1MaIktcGcH9cj21BJMAMN4Ok00@mail.gmail.com>"
rec("chase", f"Arthur's Chase records mail in thread {MB}1857028100194623541",
    S("gmail", MB + "1857028100194623541", "gmail.gmail_messages", {"id": CHASE_ID}, "body_text", "date", VIA, "A Gmail search for JPMorgan, the title of ENG-2450, finds it."),
    "That was our own Chase account", "So it never left the company.")
for key, fname, thread, sent in [("wu1", "00005184", "1800873055214061794", "1,075.00"), ("wu2", "00005350", "1802092844284446043", "1,075.00"), ("wu3", "00005489", "1803223458475671884", "1,075.00"),
                                 ("wu4", "00005962", "1805405368810910191", "2,150.00"), ("wu5", "00006329", "1808201559428745555", "2,150.00")]:
    rec(key, f"the Western Union receipt in thread {MB}{thread}", B_mail(fname, thread, 0, VIA, "A Gmail search for Lucas, named in the note on ENG-2447, finds it."), f"Transfer Amount {sent} USD")
WU = [(f"wu{i}", (0,)) for i in range(1, 6)]
for key, fname, thread, mtcn in [("wr1", "00005198", "1800906573953663690", "6439829180"), ("wr2", "00005351", "1802093473277810505", "2738632179"), ("wr3", "00005490", "1803224093176618488", "8848946467"),
                                 ("wr4", "00005963", "1805405814137504108", "4008433088"), ("wr5", "00006330", "1808201960854294221", "2223294319")]:
    rec(key, f"the received mail in thread {MB}{thread}, the same transfer as its receipt, not a second payment", B_mail(fname, thread, 0, VIA, "A Gmail search for the tracking number on the receipt finds it."), mtcn)
WR = [(f"wr{i}", (0,)) for i in range(1, 6)]
for key, fname, thread, subj in [("lm1", "00005340", "1802052757016430864", "June 15 payment"), ("lm2", "00005947", "1805314274598567124", "From July to August"),
                                 ("lm3", "00006317", "1808115779628416795", "september for Tile Dozer"), ("lm4", "00009022", "1816280614474920781", "Dec payment")]:
    assert "lucas@harmonygames.co" in jload(GM % fname)["messages"][0]["from"], fname
    rec(key, f"a payment-request mail from lucas@harmonygames.co in thread {MB}{thread}, not a receipt", B_mail(fname, thread, 0, VIA, "A Gmail search for Lucas, named in the note on ENG-2447, finds it.", field="subject"), subj)
LM = [(f"lm{i}", (0,)) for i in range(1, 5)]
rec("walsh_p", f"the only SVB Payment Processed notice to the account ending 3801, in thread {MB}1847427662807006290",
    B_mail("00015809", "1847427662807006290", 2, VIA, "A Gmail search for the account ending on ENG-2454 finds it."), "Amount: 1,999.00 BGN", "Transaction Date: Oct 30 2025")
rec("walsh_a", f"the SVB Payment Awaiting Approval notice for the same payment, in thread {MB}1847428090813337287",
    B_mail("00015811", "1847428090813337287", 1, VIA, "A Gmail search for the account ending on ENG-2454 finds it."), "Amount: 1,999.00 BGN")
rec("pay1", f"the Dixelar payment request in thread {MB}1798239548116390324",
    B_mail("00004614", "1798239548116390324", 0, VIA, "A Gmail search for payoneer, named in the note on ENG-2459, finds it."), "payment request")
rec("node_mail", f"the invoice thread {MB}1815095592611804295",
    B_mail("00008689", "1815095592611804295", 0, VIA, "A Gmail search for the name on ENG-2444 finds it."), "your ad spend exceeds $100,000")
rec("node_slack", f"Leonard's post {FOUNDERS}/1735854841.070019",
    B_slack(FOUNDERS, "1735854841.070019", VIA, "A Slack search for the agency named in the invoice thread finds it."), "closing our account with Node Media LLC")
rec("contract", "the Consulting Agreement Lauren Brooks f_20a0df3860bb5731d22f07",
    B_doc("f_20a0df3860bb5731d22f07", VIA, "A Drive search for Lauren Brooks, the Brooks in Contacts, finds it."), "run and optimize paid UA for Telegram")
note("n2438", "Leonard's note on ENG-2438", "the team’s monthly runs went through here")
note("n2439", "Leonard's note on ENG-2439", "external art studio, they billed us for the people they had on our work")
note("n2440", "Leonard's note on ENG-2440", "for Marcus’s art")
note("n2441", "Leonard's note on ENG-2441", "incent UA on iOS in the US")
note("n2442", "Arthur's note on ENG-2442", "that's MotMot, paid by the day. SVB shows their bank's name")
note("n2443", "Leonard's note on ENG-2443", "attribution tool, not one game")
note("n2444", "Leonard's note on ENG-2444", "one payment when we closed the account, Jan 2025")
note("n2445", "Leonard's note on ENG-2445", "lawyers, the patent scare")
note("n2446", "Leonard's note on ENG-2446", "that’s the trademark filings")
note("n2447", "Leonard's note on ENG-2447", "that’s Lucas, mini games dev")
note("n2449", "Leonard's note on ENG-2449", "art director for a month")
note("n2450", "Leonard's note on ENG-2450", "think it was an advance to one of the contractors but I can’t place which")
note("n2451", "Leonard's note on ENG-2451", "that’s the PlayableX team, SVB shows them under another name")
note("n2452", "Leonard's note on ENG-2452", "that’s JP, the website")
note("n2454", "Arthur's note on ENG-2454", "paid him direct for his laptop, not through Leapblock")
note("n2455", "Leonard's note on ENG-2455", "her contract had her running our paid UA on telegram, so she’s marketing, not build")
note("n2458", "Leonard's note on ENG-2458", "$500 for help on the 4X proposal, not one of the three games")
note("n2459", "Leonard's note on ENG-2459", "that wire came back the same day, I’d already re-sent it through payoneer")


def N(label):
    return label


NOT = "Robert's SVB Payment Processed notices to the account ending %s"
for last in ("8380", "1359", "8501", "5000", "3341 and 8605", "4015", "0115", "7534", "7393", "6577", "5384", "3801", "3203", "9368", "3139", "4020", "5660"):
    REC["not" + last[:4]] = {"label": NOT % last, "src": None, "quotes": ()}
REC["rev"] = {"label": "the warehouse table ANALYTICS.MONETIZATION.REVENUE_DAILY (SUM of total_revenue_usd by game_id over every date)", "src": None, "quotes": ()}
REC["project"] = {"label": "the Payee history project issues ENG-2438 to ENG-2459", "src": None, "quotes": ()}
REC["contact_l"] = {"label": "the contact leonard.hayes@harmonygames.co (Leonard Hayes)", "src": None, "quotes": ()}
REC["contact_a"] = {"label": "the contact arthur.blake@harmonygames.co (Arthur Blake)", "src": None, "quotes": ()}

# ---- values --------------------------------------------------------------------------------------------------------------
T = {}
for k, v in TRUTH.items():
    T[k] = v


def money(x):
    return f"{x:,.2f}"


def cell(payee, col):
    v = T[payee][col]
    s = money(v)
    assert s in OE_TEXT or s.rstrip("0").rstrip(".") in OE_TEXT, (payee, col, s)
    return s


BUILD = {"Domino Delights": 959342.64, "ZM": 544433.44, "Combo Fighter": 72685.61}
assert abs(sum(v["Domino Delights"] for v in T.values() if v["Bucket"] == "Build") - BUILD["Domino Delights"]) < .005
assert abs(sum(v["ZM"] for v in T.values() if v["Bucket"] == "Build") - BUILD["ZM"]) < .005
assert abs(sum(v["Combo Fighter"] for v in T.values() if v["Bucket"] == "Build") - BUILD["Combo Fighter"]) < .005
for s in ("959,342.64", "544,433.44", "72,685.61", "12,331.25", "11.99", "407,944.00", "37,056.00", "13,975.00", "984,888.21", "608,820.50", "73,685.61", "304,304.00", "32,160.00", "6,450.00"):
    assert s in OE_TEXT, s
assert abs(959342.64 - 7525 - 951817.64) < .005 and abs(959342.64 + 4032 - 963374.64) < .005 and abs(959342.64 + 4032 + 4000 - 967374.64) < .005
assert abs(6450 + 7525 + 3.96 - 13978.96) < .005 and 2 * 7525 == 15050 and 2 * 1999 == 3998

BSET = {
    "Domino Delights": [("the account ending 8380", 530736.14), ("the account ending 1359", 304304.00), ("the close-out wire of Sep 13, 2023", 33290.00), ("the account ending 8501", 45941.50), ("the account ending 3341, the returned 4,032.00 to 8605 left out", 28128.00),
                        ("the account ending 6577", 6450.00), ("the five Western Union receipts, fees left out", 7525.00), ("the account ending 0148", 2368.00), ("the account ending 1876", 600.00)],
    "ZM": [("the account ending 8380", 434185.44), ("the account ending 1359", 59250.00), ("the account ending 8501", 36070.00), ("the account ending 3341", 8928.00), ("the account ending 1794", 5000.00), ("the account ending 3307", 1000.00)],
    "Combo Fighter": [("the account ending 8380", 50425.61), ("the account ending 1359", 11100.00), ("the account ending 8501", 11160.00)],
}
for col, parts in BSET.items():
    assert abs(sum(v for _, v in parts) - BUILD[col]) < .005, col
    REC["set" + col[:2]] = {"label": f"the full Build set for {col}, from Robert's SVB Payment Processed notices and the adjustments: " + " + ".join(f"{n} {money(v)}" for n, v in parts) + f" = {money(BUILD[col])}", "src": None, "quotes": ()}
assert abs(T["Leapblock"]["Domino Delights"] - 304304.00 - 33290.00) < .005 and abs(T["Lucas"]["Domino Delights"] - 6450.00 - 7525.00) < .005 and abs(T["MotMot"]["Domino Delights"] - 28128.00) < .005

LINE = {
    "ENG-2438": "Deel, Inc. line (ENG-2438, account ending 8380)",
    "ENG-2439": "Leapblock LTD line (ENG-2439, account ending 1359)",
    "ENG-2440": "Eveline Art S.R.L. line (ENG-2440, account ending 8501)",
    "ENG-2441": "Adjoe GMBH line (ENG-2441, account ending 5000)",
    "ENG-2442": "BANCO DE AMERICA line (MotMot, ENG-2442, accounts ending 3341 and 8605)",
    "ENG-2443": "Singular Labs Inc line (ENG-2443, account ending 4015)",
    "ENG-2444": "PERSON_4419_NAME LLC line (Node Media, ENG-2444, account ending 0115)",
    "ENG-2445": "TYZ Law Group line (ENG-2445, account ending 7534)",
    "ENG-2446": "[PERSON_NAME_7200] line (the trademark filings, ENG-2446, account ending 7393)",
    "ENG-2447": "[PERSON_NAME_36400] line (Lucas, ENG-2447, account ending 6577)",
    "ENG-2449": "Graham Porter line (ENG-2449, account ending 1794)",
    "ENG-2450": "JPMorgan [PERSON_NAME_4503] line (ENG-2450, account ending 3203)",
    "ENG-2451": "CREATIVE X TEKNOLOJi line (PlayableX, ENG-2451, account ending 5660)",
    "ENG-2452": "M [PERSON_NAME_0056] line (JP, the website, ENG-2452, account ending 4020)",
    "ENG-2454": "Martin [PERSON_NAME_7250] Walsh line (ENG-2454, account ending 3801)",
    "ENG-2455": "[PERSON_NAME_7249] Brooks line (Lauren Brooks, ENG-2455, account ending 5384)",
    "ENG-2458": "[PERSON_NAME_0054] [PERSON_NAME_0131] line (the 4X proposal help, ENG-2458, account ending 3139)",
    "ENG-2459": "Private Entrepreneur [PERSON_NAME_43315] [PERSON_NAME_0120] line (Oleg, ENG-2459, account ending 9368)",
}
TITLE = {"ENG-2438": "Deel, Inc.", "ENG-2439": "Leapblock LTD", "ENG-2440": "Eveline Art S.R.L.", "ENG-2441": "Adjoe GMBH", "ENG-2442": "BANCO DE AMERICA", "ENG-2443": "Singular Labs Inc",
         "ENG-2444": "PERSON_4419_NAME LLC", "ENG-2445": "TYZ Law Group", "ENG-2446": "[PERSON_NAME_7200]", "ENG-2447": "[PERSON_NAME_36400]", "ENG-2448": "AppLovin Corporation", "ENG-2449": "Graham Porter",
         "ENG-2450": "JPMorgan [PERSON_NAME_4503]", "ENG-2451": "CREATIVE X TEKNOLOJi", "ENG-2452": "M [PERSON_NAME_0056]", "ENG-2453": "Nathan Price [PERSON_NAME_0047]", "ENG-2454": "Martin [PERSON_NAME_7250] Walsh",
         "ENG-2455": "[PERSON_NAME_7249] Brooks", "ENG-2456": "PERSON_6074_NAME [PERSON_NAME_16238]", "ENG-2457": "[PERSON_NAME_9100]", "ENG-2458": "[PERSON_NAME_0054] [PERSON_NAME_0131]", "ENG-2459": "Private Entrepreneur [PERSON_NAME_43315] [PERSON_NAME_0120]"}
for k, v in TITLE.items():
    assert f"{k} {v}" in OE_TEXT, k
NOTE_F = {f"ENG-{2438 + i}": f"F{9 + i}" for i in range(22)}
NOTICE_F = {f"ENG-{2438 + i}": f"F{32 + i}" for i in range(22)}
IDENT = "the payee's line is recognized by any identifier in the title, its payee name, its name on the bank, its account ending or its ENG id"

# ---- rows ----------------------------------------------------------------------------------------------------------------
R = []
KIND = {1: "lookup", 3: "interpretation", 5: "multi-source"}
LEAD = {1: "Lookup", 3: "Interpretation", 5: "Multi-source"}
BAD = re.compile(r"[—–]|\.sql\b|\.json\b|\.md\b|Working_Files|task_inputs|solver|truth\.|/Users/|SQL L\d+|\bsuch as\b|\be\.g\.|for example|\bOE \d|\bledger F|\bF\d{1,2}\b|gate \d|Brief", re.I)


def add(tag, t, w, fact, span, oe, fids, vals, acc, why, srcs, alt, valid, idle, dec="none", dist="none", amb="none", grp="none", ovl="none", slots=(), cat="Outcome", final=None, kind=None):
    src_objs, frs = [], []
    for s in srcs:
        key, which = s if isinstance(s, tuple) else (s, ())
        frs.append(frag(key, *which))
        o = REC[key]["src"]
        if o is not None and o not in src_objs:
            src_objs.append(o)
    if not src_objs:
        src_objs.append(REC["method"]["src"])
    ev = "Sources: " + "; ".join(frs) + f". Accept: {acc}."
    k = kind or KIND[w]
    just = f"{LEAD[w]}: {why}."
    R.append({"tag": tag, "t": t, "w": w, "kind": k, "why": why, "fact": fact, "span": span, "oe": list(oe), "fids": fids, "vals": vals, "verify": t.replace("The Agent ", "", 1),
              "final": final or "the deliverable named in the title", "acc": [acc], "alt": alt, "just": just, "ev": ev, "dec": dec, "dist": dist, "valid": valid, "idle": idle, "amb": amb, "grp": grp, "ovl": ovl,
              "slots": list(slots), "cat": cat, "srcs": src_objs, "cand": len(R) + 1})


IDLE_SHEET = f"No sheet for Leonard exists"
IDLE_REPLY = "No #winddown reply exists"
SH_OE = ["OE 30", "OE 31"]

# -- delivery and layout
add("sh_create", "The Agent creates a new spreadsheet in Robert's own Drive for Leonard's page of what each bet cost to build and brought in (any title and any folder Robert owns pass)", 1, "sheet.file", SP_SHEET, ["OE 30", "OE 3"], "F1 F3 F72", "`new spreadsheet`",
    "a new spreadsheet owned by Robert, in his My Drive root or any folder he owns, with any title", "Leonard's post says to keep Robert's own sheet in his Drive", [("ask2", (0,))], "Any title and any folder Robert owns pass.", "A new spreadsheet in Robert's root", "No spreadsheet exists", slots=["D1"], final="New spreadsheet")
add("sh_leonard", "The Agent shares its sheet for Leonard with leonard.hayes@harmonygames.co (Leonard Hayes; writer, commenter or reader)", 1, "share.leonard", SP_SHARE, ["OE 32", "OE 6"], "F6 F1 F72", "`leonard.hayes@harmonygames.co`",
    "a share of the new sheet to leonard.hayes@harmonygames.co as writer, commenter or reader", "Contacts gives his address and the prompt names him", ["contact_l", ("ask2", (0,))], "Writer, commenter or reader passes.", "A share to Leonard as writer", "No share exists", slots=["D2"], final="Share")
add("sh_arthur", "The Agent shares its sheet for Leonard with arthur.blake@harmonygames.co (Arthur Blake; writer, commenter or reader)", 1, "share.arthur", SP_SHARE, ["OE 33", "OE 6"], "F6 F1 F72", "`arthur.blake@harmonygames.co`",
    "a share of the new sheet to arthur.blake@harmonygames.co as writer, commenter or reader", "Contacts gives the address of Blake, whom the prompt names", ["contact_a", ("ask2", (0,))], "Writer, commenter or reader passes.", "A share to Arthur as reader", "No share exists", final="Share")
add("sh_header", "The Agent sets the header row of its sheet for Leonard to Leonard's layout: Payee, Name on the bank, Bucket, Domino Delights, ZM, Combo Fighter, Company, Note (letter case free; added columns pass)", 1, "sheet.layout", SP_COUNT, ["OE 31", "OE 3"], "F3 F73", "`Name on the bank`",
    "a header row carrying Payee, Name on the bank, Bucket, Domino Delights, ZM, Combo Fighter, Company and Note, letter case free, with added columns passing", "the layout is the header row of Leonard's sheet", [("ask2", (0,)), "layout_hdr"], "Letter case free; added columns pass.", "A header row with those names", IDLE_SHEET, final="Sheet header")
add("sh_volume", "The Agent lists the 22 payees of issues ENG-2438 to ENG-2459 on its sheet for Leonard, each issue on its own line (a total, notes or reconciliation line is not counted)", 1, "sheet.volume", SP_COUNT, ["OE 31", "OE 8"], "F8 F2 F73", "`ENG-2438` `ENG-2459` `22`",
    "each of the 22 issues ENG-2438 to ENG-2459 has its own line; a total, notes or reconciliation line is not counted", "the project holds one issue per payee and the method keeps every payee's line", ["project", ("method", (0,))], "A total, notes or reconciliation line is not counted.", "A sheet with 22 payee lines", IDLE_SHEET, grp="sheet volume", slots=[], final="Sheet payee lines")

# -- the corrected inputs (direct exceptions)
add("cell_leap", f"The Agent shows 337,594.00 in the Domino Delights column of the {LINE['ENG-2439']} on {SH} (304,304.00 fails)", 5, "cell.leapblock", SP_COUNT, ["OE 31", "OE 26", "OE 12", "OE 14", "OE 15"], "F33 F56 F57 F68 F73", "`337,594.00`",
    f"that cell equals 337,594.00 in any number format, as a value or a formula that evaluates to it; {IDENT}; 304,304.00 fails", "the 29 notices stop short of the close-out, and Leapblock's close-out in Slack and the Awaiting Approval mail bring in the Sep 13, 2023 wire", ["not1359", ("close", (0, 1)), "await", ("method", (2,))], "Any number format or a formula passes; 304,304.00 fails.", "The cell reads 337594", IDLE_SHEET, dec=NODES["ORPH"], dist="T orphan wire", slots=["X4"], final="Sheet cell")
add("cell_motmot", f"The Agent shows 28,128.00 in the Domino Delights column of the {LINE['ENG-2442']} on {SH} (32,160.00 fails)", 5, "cell.motmot", SP_COUNT, ["OE 31", "OE 26", "OE 12", "OE 13"], "F36 F54 F68 F73", "`28,128.00`",
    f"that cell equals 28,128.00 in any number format, as a value or a formula that evaluates to it; {IDENT}; 32,160.00 fails", "the notices count the Apr 2, 2024 wire and its re-send, and Leonard's post in #admin_foundersonly says the wire came back", ["not3341", ("ret", (0, 1)), ("method", (1,))], "Any number format or a formula passes; 32,160.00 fails.", "The cell reads 28128", IDLE_SHEET, dec=NODES["RET"], dist="T returned wire", slots=["X1"], final="Sheet cell")
add("cell_lucas", f"The Agent shows 13,975.00 in the Domino Delights column of the {LINE['ENG-2447']} on {SH} (6,450.00 or 13,978.96 fails)", 5, "cell.lucas", SP_COUNT, ["OE 31", "OE 26", "OE 12", "OE 16", "OE 17"], "F41 F18 F59 F68 F73", "`13,975.00`",
    f"that cell equals 13,975.00 in any number format, as a value or a formula that evaluates to it; {IDENT}; 6,450.00 or 13,978.96 fails", "the three notices are joined to five Western Union receipts in Robert's mail at the amount sent, fees left out", ["not6577", "n2447", *WU, ("method", (4,))], "Any number format or a formula passes; 6,450.00 or 13,978.96 fails.", "The cell reads 13975", IDLE_SHEET, dec=NODES["OFF"], dist="T other route", slots=["X3"], final="Sheet cell")
add("cell_jpm", f"The Agent shows 0, a blank or a dash in the Domino Delights column of the {LINE['ENG-2450']} on {SH} (4,000.00 in that column or in the Company column of that line fails)", 5, "cell.jpm", SP_COUNT, ["OE 31", "OE 26", "OE 12", "OE 19"], "F44 F21 F61 F68 F73", "`0` `4,000.00`",
    f"the Domino Delights cell of that line is 0, blank or a dash; {IDENT}; 4,000.00 in that column or in the Company column of that line fails", "Leonard's note guesses a contractor advance, and Arthur's Chase records mail shows the money went to the company's own account", ["not3203", "n2450", ("chase", (0, 1)), ("method", (3, 0))], "0, blank or a dash passes; 4,000.00 in that column or in the Company column of that line fails.", "The cell reads 0", IDLE_SHEET, dec=NODES["CORR"], dist="T hedged note", final="Sheet cell")
add("bkt_jpm", f"The Agent marks the Bucket cell of the {LINE['ENG-2450']} on {SH} as outside the cost buckets (a blank, a dash, or any entry saying no bucket, not a cost or an own-account transfer passes; a cell naming Build, Marketing or Company fails)", 5, "bucket.jpm", SP_COUNT, ["OE 31", "OE 25", "OE 19"], "F21 F61 F67 F73", "`Own transfer`",
    f"the Bucket cell is a blank, a dash, or any entry saying no bucket, not a cost or an own-account transfer; {IDENT}; a cell naming Build, Marketing or Company fails", "Leonard's note reads as a contractor payment, and Arthur's Chase records mail shows an own-account transfer that takes no bucket", ["n2450", ("chase", (0, 1)), ("method", (3,))], "A blank, a dash, or an entry saying no bucket, not a cost or an own-account transfer passes; a cell naming Build, Marketing or Company fails.", "The cell reads None (own transfer)", IDLE_SHEET, dec=NODES["CORR"], dist="T hedged note", slots=["X5"], final="Sheet cell")
add("cell_oleg", f"The Agent shows 0, a blank or a dash in the Domino Delights column of the {LINE['ENG-2459']} on {SH} (125.00 fails)", 5, "cell.oleg", SP_COUNT, ["OE 31", "OE 26", "OE 12", "OE 18"], "F53 F30 F60 F68 F73", "`0` `125.00`",
    f"the Domino Delights cell of that line is 0, blank or a dash; {IDENT}; 125.00 fails", "the note says the wire came back and was re-sent through Payoneer, and a search of Robert's mail finds no receipt for the re-send", ["not9368", "n2459", ("pay1", (0,)), ("method", (1, 4))], "0, blank or a dash passes; 125.00 fails.", "The cell reads 0", IDLE_SHEET, final="Sheet cell")
add("bkt_node", f"The Agent puts Marketing in the Bucket cell of the {LINE['ENG-2444']} on {SH} (Build or Company fails)", 5, "bucket.node", SP_COUNT, ["OE 31", "OE 25", "OE 20", "OE 21"], "F15 F62 F63 F67 F73", "`Marketing`",
    f"the Bucket cell reads Marketing, letter case free; {IDENT}; Build or Company fails", "the bank name is a token, and the invoice thread in Gmail shows ad spend, with Leonard's Slack post naming Node Media LLC", [("node_mail", (0,)), ("node_slack", (0,)), ("method", (7,))], "Letter case free; Build or Company fails.", "The cell reads Marketing", IDLE_SHEET, dec=NODES["ALIAS"], dist="T token payee", slots=["X6"], final="Sheet cell", grp="bucket column")
add("bkt_lauren", f"The Agent puts Marketing in the Bucket cell of the {LINE['ENG-2455']} on {SH} (Build fails)", 1, "bucket.lauren", SP_COUNT, ["OE 31", "OE 25", "OE 10"], "F26 F67 F73", "`Marketing`",
    f"the Bucket cell reads Marketing, letter case free; {IDENT}; Build fails", "Leonard's note on the issue says she is marketing", ["n2455"], "Letter case free; Build fails.", "The cell reads Marketing", IDLE_SHEET, slots=["X8"], final="Sheet cell", grp="bucket column")
add("bkt_martin", f"The Agent puts Company in the Bucket cell of the {LINE['ENG-2454']} on {SH} (Build fails)", 3, "bucket.martin", SP_COUNT, ["OE 31", "OE 25", "OE 10"], "F25 F67 F73", "`Company`",
    f"the Bucket cell reads Company, letter case free; {IDENT}; Build fails", "Arthur's note says the payment was for a laptop, and the method puts equipment in Company", ["n2454", ("method", (8,))], "Letter case free; Build fails.", "The cell reads Company", IDLE_SHEET, final="Sheet cell", grp="bucket column")
BGN_T = ("any number format passes; BGN, lev, leva, lv or лв passes as the mark; the figure may sit in any cell of the line or in a note row under it, and the mark may sit on that line, in that cell's column heading or in that note row; "
         "0, a blank, a dash or n/a in the line's other cells passes; a dollar conversion in the BGN figure's own cell, in a note or in a column headed as a conversion passes; "
         "1,999.00 marked $ or USD, any dollar figure shown as the line's amount, which can only be a conversion because the line has no dollar payment, or 3,998.00 BGN, which counts the Awaiting Approval notice too, fails")
add("cell_martin", f"The Agent shows 1,999.00 BGN, unconverted, as the only payment on the {LINE['ENG-2454']} on {SH} ({BGN_T})", 1, "cell.martin", SP_COUNT, ["OE 31", "OE 26", "OE 12"], "F48 F68 F73", "`1,999.00 BGN`",
    f"{BGN_T}; {IDENT}", "the one Processed notice is in BGN and the method keeps other currencies beside the line", ["walsh_p", "walsh_a", ("method", (11,))], f"{BGN_T[0].upper()}{BGN_T[1:]}.", "The Company cell reads BGN 1,999.00", IDLE_SHEET, dec=NODES["CURR"], dist="T currency", slots=["X9"], final="Sheet cell")

# -- Company column (spot check, five lines)
for tag, k, payee, val, why, srcs, fail, w, slot in [
    ("co_singular", "ENG-2443", "Singular", "31,250.00", "two notices under two spellings of one account add up, and the method puts tools in Company", ["not4015", "n2443", ("method", (8,))], "25,000.00 or 6,250.00 fails", 3, []),
    # co_4x (ENG-2458, 500.00, weight 1) was removed 2026-11-10: platform /rubric round 10 counted cell_node as a sixth
    # sample of this group (cap five) and named this row as the one to drop; co_singular still samples the Company column.
]:
    assert money(T[payee]["Company"]) == val, (payee, val)
    fl = f" ({fail})" if fail else ""
    fa = f"; {fail}" if fail else ""
    add(tag, f"The Agent shows {val} in the Company column of the {LINE[k]} on {SH}{fl}", w, f"company.{k}", SP_COUNT, ["OE 31", "OE 26", "OE 12", "OE 25"], f"{NOTICE_F[k]} {NOTE_F[k]} F68 F73", f"`{val}`",
        f"the Company cell equals {val} in any number format, as a value or a formula that evaluates to it; {IDENT}{fa}", why, srcs, f"Any number format or a formula passes{fa}.", f"The Company cell reads {val}", IDLE_SHEET, grp="dollar amounts", slots=slot, final="Sheet cell")

# -- bet columns (spot check, five lines)
for tag, k, payee, col, fail, why, srcs, slot, w, dec in [
    ("bet_deel", "ENG-2438", "Deel", "Domino Delights", None, "21 notices up to Jan 8, 2025 add up across the two spellings of one account", ["not8380", "n2438", ("method", (6, 9, 10))], ["S1"], 3, "none"),
    ("bet_adjoe", "ENG-2441", "Adjoe", "ZM", None, "three notices in the ZM window add up, and the method lists marketing under its bet by date", ["not5000", "n2441", ("method", (9, 10))], [], 3, "none"),
    ("bet_lauren", "ENG-2455", "Lauren Brooks", "Combo Fighter", "1,500.00 fails", "the Dec 1, 2025 and Jan 6, 2026 notices fall after Nov 24, 2025, and the Oct 30, 2025 notice does not", ["not5384", "n2455", ("method", (9, 10))], [], 3, "none"),
]:
    val = cell(payee, col)
    whole = f"{round(T[payee][col]):,}"
    wp = f"; the whole-dollar figure {whole} also passes" if val != whole + ".00" else ""
    fl = f" ({whole} also passes; {fail})" if fail and wp else (f" ({fail})" if fail else (f" ({whole} also passes)" if wp else ""))
    fa = (wp + f"; {fail}") if fail else wp
    add(tag, f"The Agent shows {val} in the {col} column of the {LINE[k]} on {SH}{fl}", w, f"bet.{k}", SP_COUNT, ["OE 31", "OE 26", "OE 12"], f"{NOTICE_F[k]} {NOTE_F[k]} F68 F73", f"`{val}`",
        f"that cell equals {val} in any number format, as a value or a formula that evaluates to it; {IDENT}{fa}", why, srcs, f"Any number format or a formula passes{fa}.", f"The {col} cell reads {val}", IDLE_SHEET, grp="dollar amounts", slots=slot, final="Sheet cell", dec=dec)

# -- bucket column (spot check, five lines)
for tag, k, b, fail, why, srcs, slot, w in [
    ("bkt_deel", "ENG-2438", "Build", "Marketing or Company fails", "the method says everything on Deel counts as team", [("method", (6,))], [], 1),
    ("bkt_adjoe", "ENG-2441", "Marketing", "Build or Company fails", "the note makes it incent UA, and the method puts ad networks in Marketing", ["n2441", ("method", (7,))], ["S4"], 3),
]:
    add(tag, f"The Agent puts {b} in the Bucket cell of the {LINE[k]} on {SH} ({fail})", w, f"bucket.{k}", SP_COUNT, ["OE 31", "OE 25"], f"{NOTE_F[k]} F67 F73", f"`{b}`",
        f"the Bucket cell reads {b}, letter case free; {IDENT}; {fail}", why, srcs, f"Letter case free; {fail}.", f"The cell reads {b}", IDLE_SHEET, grp="bucket column", slots=slot, final="Sheet cell")

# -- name on the bank (spot check, two lines)
for tag, k, nm, why, srcs in [
    ("bank_motmot", "ENG-2442", "BANCO DE AMERICA", "the notices and the issue title show the bank's name, not MotMot", ["n2442", "not3341"]),
    ("bank_creative", "ENG-2451", "CREATIVE X TEKNOLOJi", "the notices and the issue title show another name for PlayableX", ["n2451", "not5660"]),
]:
    add(tag, f"The Agent shows {nm} in the Name on the bank column of the {LINE[k]} on {SH} (an account ending beside the name passes)", 1, f"bank.{k}", SP_COUNT, ["OE 31", "OE 8", "OE 12"], f"F8 {NOTICE_F[k]} F73", f"`{nm}`",
        f"the Name on the bank cell carries {nm}, letter case free, and an account ending beside the name passes; {IDENT}", why, srcs, "Letter case free; an account ending beside the name passes.", f"The cell reads {nm}", IDLE_SHEET, grp="name on the bank", final="Sheet cell")

# -- totals the prompt asks for
WH = {"Domino Delights": "959,343", "ZM": "544,433", "Combo Fighter": "72,686"}
BUILD_SRC = {"Domino Delights": ["setDo", ("close", (0, 1)), ("ret", (0,)), *WU, "n2442", ("method", (5, 16, 9))],
             "ZM": ["setZM", "n2449", ("method", (5, 16, 9))],
             "Combo Fighter": ["setCo", ("method", (5, 16, 9))]}
BLABEL = "any label naming the Build bucket or build cost passes, Build, Build total, Build cost and Cost to build included"
for col, val, why, slot, dec in [
    ("Domino Delights", "959,342.64", "the Gmail notices by date are adjusted for the returned wire, the receipts and the close-out, then limited to the Build payees by the Linear notes", "B1", NODES["RET"] + " " + NODES["OFF"] + " " + NODES["ORPH"]),
    ("ZM", "544,433.44", "the Gmail notices by date are limited to the Build payees by the Linear notes", "B2", NODES["CLASS"]),
    ("Combo Fighter", "72,685.61", "the Gmail notices from Nov 24, 2025 are limited to the Build payees by the Linear notes, and the Telegram contractor stays out", "B3", NODES["CLASS"]),
]:
    add(f"build_{col[:2]}", f"The Agent shows {val} as the {col} build cost on {SH}, in a totals line or summary block ({BLABEL}; a formula that evaluates to it or the whole-dollar figure {WH[col]} passes)", 5, f"build.{col}", SP_COUNT, ["OE 31", "OE 27"], "F69 F68 F67 F73", f"`{val}`",
        f"a totals line or summary block presents {val} as {col}'s build cost, in any number format, as a value or a formula that evaluates to it, or the whole-dollar figure {WH[col]}; {BLABEL}", why, BUILD_SRC[col], f"{BLABEL[0].upper()}{BLABEL[1:]}, as do any number format, a formula or the whole-dollar figure {WH[col]}.", f"The build cost line reads {val}", IDLE_SHEET, dec=dec, slots=[slot], final="Sheet line", grp="build cost")

# -- revenue
for game, val, slot, whole in [("Domino Delights", "12,331.25", "V1", "12,331"), ("ZM", "11.99", "V2", "12")]:
    add(f"rev_{game[:2]}", f"The Agent shows {val} as {game} lifetime revenue on {SH}, in a brought-in line or summary block (a formula that evaluates to it or the whole-dollar figure {whole} passes)", 3, f"revenue.{game}", SP_COUNT, ["OE 31", "OE 24"], "F66 F2 F73", f"`{val}`",
        f"a line or summary block labelled as what each bet brought in shows {val} for {game} in any number format, as a value or a formula that evaluates to it, or the whole-dollar figure {whole}", "a sum of the warehouse's daily revenue table over every date", ["rev", ("method", (12,))], "Any number format or a formula passes.", f"The brought-in line reads {val}", IDLE_SHEET, slots=[slot], final="Sheet line", grp="revenue")
add("rev_hold", f"The Agent holds back Combo Fighter's revenue in the brought-in line or summary block of {SH} (a Combo Fighter cell left blank, a dash, marked as left off for now, or a block listing only Domino Delights and ZM passes; any Combo Fighter revenue figure on the sheet, 11.75 included, fails)", 1, "revenue.cf.sheet", SP_COUNT, ["OE 31", "OE 24", "OE 2"], "F66 F2 F73", "`11.75`",
    "a Combo Fighter cell left blank, a dash, marked as left off for now, or a block listing only Domino Delights and ZM passes; any Combo Fighter revenue figure on the sheet, 11.75 included, fails", "the method says to leave it off", [("method", (13,))], "Blank, a dash, a left-off marking or a block listing only Domino Delights and ZM passes; any Combo Fighter revenue figure on the sheet fails.", "The cell is blank", IDLE_SHEET, final="Sheet cell", dist="T held revenue")

# -- Linear reason comments
for tag, k, t, fail, w, why, srcs, oe, fids, dec, slot in [
    ("c_leap", "ENG-2439", "that its line follows Leapblock's own close-out of what it received, or that the 33,290 wire of Sep 13, 2023, which has no Processed notice, is counted on the line (any wording with that meaning; the figures 407,944 and 30 wires are not required)", None, 5, "the reason joins Leapblock's close-out in Slack to the notices and the Awaiting Approval mail in Gmail", [("close", (0, 1)), "await", ("method", (2, 15))], "OE 34", "F33 F56 F57 F74", NODES["ORPH"], ["C3"]),
    ("c_motmot", "ENG-2442", "that the wire to the account ending 8605 came back (any wording with that meaning; any way of naming that wire, or no identifier at all, passes; calling the Apr 5, 2024 re-send or any other wire to the account ending 3341 the one that came back, or saying the line still keeps the returned 4,032.00, fails)", "calling the Apr 5, 2024 re-send or any other wire to the account ending 3341 the one that came back, or saying the line still keeps the returned 4,032.00, fails", 5, "the reason joins Leonard's post in #admin_foundersonly to the notices in Gmail", [("ret", (0,)), "not3341", ("method", (1, 15))], "OE 35", "F36 F54 F75", NODES["RET"], ["C1"]),
    ("c_lucas", "ENG-2447", "that the line adds the five transfers paid outside the SVB notices, in any wording naming Western Union, the receipts, the 7,525.00 sent (rounded passes), the amounts (1,075.00 three times, 2,150.00 twice) or monthly totals (3,225.00 June, 2,150.00 each July and August); 6,450.00 (notices) and 13,975.00 (line) may appear; giving mails from lucas@harmonygames.co (\"June 15 payment\", \"Dec payment\" and the rest) as the source instead of the Western Union receipts, counting the fees (0.99 on four transfers; 7,528.96) or any transfer twice (15,050.00), any other figure as the transfers' total, part of the five as all, or a Western Union transfer with a wrong amount or dated outside June to August 2024 fails", "giving mails from lucas@harmonygames.co (\"June 15 payment\", \"Dec payment\" and the rest) as the source instead of the Western Union receipts, counting the fees (0.99 on four transfers; 7,528.96) or any transfer twice (15,050.00), any other figure as the transfers' total, part of the five as all, or a Western Union transfer with a wrong amount or dated outside June to August 2024 fails", 5, "the reason joins the Linear note to the Western Union receipts in Gmail", ["n2447", *WU, *WR, *LM, ("method", (4, 15))], "OE 36", "F18 F59 F76", NODES["OFF"], ["C2"]),
    ("c_jpm", "ENG-2450", "that the 4,000.00 notice went to the company's own Chase account (any wording with that meaning; naming the amount is not required; calling it a contractor advance or a Company cost fails)", "calling it a contractor advance or a Company cost fails", 5, "the reason sets Arthur's mail against Leonard's note and the notice", [("chase", (0, 1)), "n2450", ("method", (3, 15))], "OE 37", "F21 F61 F77", NODES["CORR"], ["C4"]),
    ("c_oleg", "ENG-2459", "that the 125.00 wire came back (any wording with that meaning; naming the amount or when it came back is not required; saying the line keeps the 125.00 fails)", "saying the line keeps the 125.00 fails", 1, "Leonard's note on the same issue gives the reason", ["n2459", ("method", (1, 15))], "OE 38", "F30 F53 F60 F78", "none", []),
]:
    fa = f"; {fail}" if fail else ""
    add(tag, f"The Agent comments on {k} ({TITLE[k]}) {t}", w, f"comment.{k}", SP_LINEAR, [oe, "OE 28"], fids, f"`{k}`",
        f"a comment on {k} says {t}", why, srcs, f"Any wording with that meaning passes{fa}.", f"A comment on {k} giving that reason", f"No comment on {k} exists", dec=dec, slots=slot, final=f"Comment on {k}", grp="reason comments")

# -- Done moves
for i, (k, ttl) in enumerate(TITLE.items()):
    add(f"done_{k}", f"The Agent moves {k} ({ttl}) to Done", 1, f"done.{k}", SP_LINEAR, [f"OE {39 + i}", "OE 28"], "F79 F70 F8", f"`{k}`",
        f"{k} is moved to the Done state of team ENG", "one issue state change the method asks for", ["project", ("method", (14,))], "Done or the Linear state type completed resolved to Done passes.", f"{k} in Done", f"{k} still in Backlog", final=f"Issue {k}", grp="done moves")

# -- reply
RSRC = {"Domino Delights": ["setDo", ("close", (0, 1)), ("ret", (0,)), *WU, ("ask2", (1,))], "ZM": ["setZM", "n2449", ("ask2", (1,))], "Combo Fighter": ["setCo", ("ask2", (1,))]}
for g, v, rounded, wrong, old, why, slot, dec in [
    ("Domino Delights", "959,342.64", "$959K, $959.3K and $959,343", "$952K, $926K, $963K, $967K or $985K", "$985K", "the Gmail notices by date are adjusted for the returned wire, the receipts and the close-out, then limited to the Build payees by the Linear notes", "R1", NODES["RET"] + " " + NODES["OFF"] + " " + NODES["ORPH"]),
    ("ZM", "544,433.44", "$544K, $544.4K and $544,433", "$609K", "$609K", "the Gmail notices by date are limited to the Build payees by the Linear notes", None, NODES["CLASS"]),
    ("Combo Fighter", "72,685.61", "$73K, $72.7K and $72,686", "$74K", "$74K", "the Gmail notices from Nov 24, 2025 are limited to the Build payees by the Linear notes", None, NODES["CLASS"]),
]:
    fail = f"giving {wrong} as its build cost fails; quoting {old} as the deck's old figure passes"
    add(f"r_build_{g[:2]}", f"The Agent tells Leonard in {RP} that {g} cost {v} to build (or any rounding to $1K or finer, {rounded} included; {fail})", 5, f"build.{g}", SP_REPLY, ["OE 61", "OE 27"], "F69 F81", f"`{v}`",
        f"the reply gives {g}'s build cost as {v}, or a rounding to $1K or finer, {rounded} included; {fail}", why, RSRC[g], f"The full figure or a rounding to $1K or finer passes; {fail}.", f"A reply saying {g} cost {v}", IDLE_REPLY, dec=dec, slots=[slot] if slot else [], final="Slack reply")
for g, v, rounded in [("Domino Delights", "12,331.25", "any rounding to $1K or finer, $12,331, $12.3K and $12K included"), ("ZM", "11.99", "$12")]:
    add(f"r_rev_{g[:2]}", f"The Agent tells Leonard in {RP} that {g} brought in {v} (or {rounded})", 3, f"revenue.{g}", SP_REPLY, ["OE 61", "OE 24"], "F66 F81", f"`{v}`",
        f"the reply gives {g}'s lifetime revenue as {v} or {rounded}", "a sum of the warehouse's daily revenue table over every date", ["rev", ("ask2", (1,))], "The full figure or that rounding passes.", f"A reply saying {g} brought in {v}", IDLE_REPLY, final="Slack reply")
add("r_hold", f"The Agent holds back Combo Fighter's revenue in {RP}, saying it is left off for now or giving brought-in figures for Domino Delights and ZM alone (any Combo Fighter revenue figure, 11.75 included, fails)", 1, "revenue.cf.reply", SP_REPLY, ["OE 61", "OE 2"], "F2 F81", "`11.75`",
    "the reply says Combo Fighter's revenue is left off for now, or gives brought-in figures for Domino Delights and ZM alone; any Combo Fighter revenue figure, 11.75 included, fails", "the method says to leave it off when telling Leonard", [("method", (13,))], "Either form passes; any Combo Fighter revenue figure fails.", "A reply with no Combo Fighter revenue", IDLE_REPLY, final="Slack reply", dist="T held revenue")
add("r_deck_cost", f"The Agent tells Leonard in {RP} that the draft deck's What each bet cost to build slide, which now reads $985K, $609K and $74K, changes (any wording with that meaning; any new figures named for that slide must be the build costs the reply gives for those bets, and naming $985K, $609K or $74K as the new figures fails; naming none passes)", 3, "deck.cost", SP_REPLY, ["OE 61", "OE 29", "OE 4"], "F4 F71 F81", "`$985K`",
    "the reply says the draft deck's What each bet cost to build slide, which now reads $985K, $609K and $74K, changes, in any wording with that meaning; any new figures named for that slide must be the build costs the reply gives for those bets, and naming $985K, $609K or $74K as the new figures fails; naming none passes", "a comparison of the deck's quick figures with the page", [("ask2", (1,)), "deck_cost"], "Any wording with that meaning passes; naming $985K, $609K or $74K as the new figures fails.", "A reply saying the cost slide changes to the new figures", IDLE_REPLY, slots=["R2"], final="Slack reply")
add("r_deck_rev", f"The Agent tells Leonard in {RP} that the draft deck's What each brought in slide, which reads to fill in, gets Domino Delights and ZM lifetime revenue (any wording with that meaning; any figures named for that slide must be the brought-in figures the reply gives; naming none passes)", 3, "deck.revenue", SP_REPLY, ["OE 61", "OE 29", "OE 4"], "F4 F71 F81", "`to fill in`",
    "the reply says the draft deck's What each brought in slide, which reads to fill in, gets Domino Delights and ZM lifetime revenue, in any wording with that meaning; any figures named for that slide must be the brought-in figures the reply gives; naming none passes", "the slide is empty and the page supplies its figures, with one held back", [("ask2", (1,)), "deck_rev", ("method", (13,))], "Any wording with that meaning passes; any figures named for that slide must be the brought-in figures the reply gives.", "A reply saying the brought-in slide gets those figures", IDLE_REPLY, final="Slack reply")
add("r_link", f"The Agent includes the link to {SH} in {RP}", 1, "reply.link", SP_REPLY, ["OE 61", "OE 30"], "F72 F81", "`link`",
    "the reply carries a URL that opens the new spreadsheet, in whatever form the tools gave it", "the link comes back from the Sheets or Drive tools", [("ask2", (0,))], "Any URL that opens that spreadsheet passes.", "A reply with the sheet URL", IDLE_REPLY, slots=["D3"], final="Slack reply")

# -- ordering (no final state shows these)
for k, oe_c, oe_d in [("ENG-2439", "OE 34", "OE 40"), ("ENG-2442", "OE 35", "OE 43"), ("ENG-2447", "OE 36", "OE 48"), ("ENG-2450", "OE 37", "OE 51"), ("ENG-2459", "OE 38", "OE 60")]:
    add(f"o_{k}", f"The Agent posts its comment on {k} before it moves {k} to Done", 1, f"order.{k}", SP_LINEAR, [oe_c, oe_d], "F70 F2", f"`{k}`",
        f"the comment on {k} comes before {k} moves to Done", "the method says to say why on the issue first, and this row grades the order of the two writes, which no content row shows", [("method", (15,))], "The comment comes first in the order of writes.", "The comment is the earlier call", f"No comment on {k} exists", cat="Process", final="Order of writes", grp="comment first")
add("o_sheet", f"The Agent writes the Deel, Inc. line (ENG-2438) to {SH} before it moves ENG-2438 to Done (writing all lines first passes; later edits to the sheet pass)", 1, "order.sheet", SP_LINEAR, ["OE 31", "OE 39"], "F70 F2", "`Done`",
    "the Deel, Inc. line (ENG-2438) is written to the sheet before ENG-2438 moves to Done; writing all lines first passes; later edits to the sheet pass", "the method moves each issue once its line is right, and this row grades that order on one issue, which no content row shows", [("method", (14,))], "Writing all lines first passes; later edits to the sheet pass.", "The sheet write is the earlier call", IDLE_SHEET, cat="Process", final="Order of writes")
add("o_reply", f"The Agent posts {RP} to Leonard last among its writes of the task (no sheet write, share, comment or issue move comes after it; a further #winddown message passes)", 1, "order.reply", SP_DONE, ["OE 61"], "F81 F70", "`after`",
    "no sheet write, share, comment or issue move comes after the reply; a further #winddown message passes", "the prompt says to reply when done, and this row grades the order of the writes, which no content row shows", [("ask2", (1,))], "No sheet write, share, comment or issue move comes after the reply; a further #winddown message passes.", "The reply is the last write", IDLE_REPLY, cat="Process", final="Order of writes")

# -- added 2026-11-10 after the rev7 baseline: the dollars cell of the Node Media line. Platform /rubric round 10 ruled it
#    an ordinary sample of the dollar-amount spot checks (its figure equals its notice), so it sits in that group and
#    co_4x left to keep the group at five. Kept last and byte-identical to the row that review checked.
assert cell("Node Media", "Domino Delights") == "16,428.57"
NODE_FAIL = "16,428.57 in the ZM column or in the Company column of that line fails"
add("cell_node", f"The Agent shows 16,428.57 in the Domino Delights column of the {LINE['ENG-2444']} on {SH} (16,429 also passes; {NODE_FAIL})", 3, "cell.node", SP_COUNT, ["OE 31", "OE 26", "OE 12", "OE 20"], f"{NOTICE_F['ENG-2444']} {NOTE_F['ENG-2444']} F68 F73", "`16,428.57`",
    f"that cell equals 16,428.57 in any number format, as a value or a formula that evaluates to it; {IDENT}; the whole-dollar figure 16,429 also passes; {NODE_FAIL}", "the one notice is dated Jan 2, 2025, inside the Domino Delights window, and the method lists marketing under its bet by date", ["not0115", "n2444", ("node_mail", (0,)), ("method", (9, 10))], f"Any number format or a formula passes; the whole-dollar figure 16,429 also passes; {NODE_FAIL}.", "The Domino Delights cell reads 16,428.57", IDLE_SHEET, dec=NODES["ALIAS"], dist="T token payee", final="Sheet cell", grp="dollar amounts")

# ---- checks --------------------------------------------------------------------------------------------------------------
for r in R:
    for f in ("t", "just", "ev"):
        m = BAD.search(r[f])
        assert not m, (r["tag"], f, m.group(0), r[f][:200])
    assert r["t"].startswith("The Agent "), r["t"]
    assert r["span"] in PROMPT
    for oe in r["oe"]:
        assert re.search(rf"^{oe}  ", OE_TEXT, re.M), (r["tag"], oe)
tags = [r["tag"] for r in R]
assert len(tags) == len(set(tags)), [t for t, c in Counter(tags).items() if c > 1]
titles = Counter(r["t"] for r in R)
assert max(titles.values()) == 1, [t for t, c in titles.items() if c > 1]
dup = [k for k, v in Counter(r["fact"] for r in R).items() if v >= 3]
assert not dup, dup
for g, cap in [("dollar amounts", 5), ("bucket column", 5), ("name on the bank", 5)]:
    assert sum(1 for r in R if r["grp"] == g) <= cap, g
# every "fails" clause in a title is repeated in its Accept line
for r in R:
    for cl in re.findall(r"([^;(]*?\bfails\b)", r["t"]):
        assert cl.strip() in r["ev"], (r["tag"], cl)

# ---- outputs -------------------------------------------------------------------------------------------------------------
rubric = [{"title": r["t"], "category": r["cat"], "weight": r["w"], "justification": r["just"], "evidence": r["ev"]} for r in R]
out = os.path.join(TI, "09_Rubrics.json")
open(out, "w", encoding="utf-8").write(json.dumps(rubric, indent=1, ensure_ascii=False) + "\n")


def ahash(p):
    return subprocess.run([sys.executable, os.path.join(TA, "tools/stage_gate.py"), "--artifact-hash", p], capture_output=True, text=True, cwd=WS).stdout.strip()


ep = os.path.join(WF, "00_V3_Authoring_Evidence.json")
ev = json.load(open(ep, encoding="utf-8"))
ev["rubric_hash"] = ahash(out)
ev["prompt_hash"] = ahash(os.path.join(TI, "04_Prompt.txt"))
ev["rubric_rows"] = [{"criterion_id": f"C{i + 1}", "fact_id": r["fact"], "prompt_span": r["span"], "accepted_outcomes": r["acc"], "alternatives_review": r["alt"], "source_records": r["srcs"]} for i, r in enumerate(R)]
json.dump(ev, open(ep, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
json.dump([{k: v for k, v in r.items() if k != "srcs"} for r in R], open(os.path.join(HERE, "rows.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
tw = sum(r["w"] for r in R)
print(len(R), "rows; weight", tw, "; bands", {b: sum(1 for r in R if r["w"] == b) for b in (5, 3, 1)}, "; Process", sum(1 for r in R if r["cat"] == "Process"), "; hash", ev["rubric_hash"])
