#!/usr/bin/env python3
"""Scenario builder (design stage) for Robert: the seed, bet by bet. Writes 01_Hardness_Manifest.draft.json,
01_Gradable_Surface.json, plan/ids.json, plan/wording.json, plan/cohort.json and plan/tables/*.md.
Design only. The seeded texts in Q are the planned wording /create-injection must use verbatim (delegation quotes are exact
substrings of them). Ids come from research/minted_ids.json (collision-checked across the base). Never executes SQL."""
import datetime as dt, hashlib, json, os, re
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE)
CTX = json.load(open(os.path.join(WF, "00_Task_Context.json")))
MINT = json.load(open(os.path.join(HERE, "research", "minted_ids.json")))
NOT = json.load(open(os.path.join(WF, "00_PreScenario", "svb_processed_robert.json")))
ROB, LEO, ART = "robert@harmonygames.co", "leonard.hayes@harmonygames.co", "arthur.blake@harmonygames.co"
WD, EX, AD, LB, FO = "C0ADGSZKR3R", "C07C2866011", "C04UEQVDVB7", "C05URGU759U", "C04UTBZL6AX"
TG, PX, ART_CH, DM_LR = "C09KU8U4DPF", "C08H78VJG80", "C08FG9924R2", "D04UP2L3E3S"
T = dict(MINT["T"])
T.update({"trello": "2026-02-12T22:36:41Z", "sheet": "2026-02-12T22:44:12Z", "deck": "2026-02-12T22:52:37Z", "trello_comment": "2026-02-12T23:55:07Z", "leonard_reply": "2026-02-13T17:08:37Z"})  # sw2: after Leonard's P&L note and angels note, before Linear
_ep = int(dt.datetime.fromisoformat(T["trello"].replace("Z", "+00:00")).timestamp())
MINT["trello"]["card"] = "%08x" % _ep + MINT["trello"]["card"][8:]; MINT["trello"]["create_action"] = "%08x" % _ep + MINT["trello"]["create_action"][8:]
ASK2_TS = "1770945859.212469"
SALT = "hg-robert-seed-bets|"
def _h(l, n): return hashlib.sha256((SALT + l).encode()).hexdigest()[:n]
def _tid(box, label, iso):
    ms = int(dt.datetime.fromisoformat(iso.replace("Z", "+00:00")).timestamp() * 1000)
    return f"{box}/{(ms << 20) + (int(_h(label + '|' + box, 8), 16) & 0xFFFFF)}"
T["invite"] = (dt.datetime.fromisoformat(T["hold"].replace("Z", "+00:00")) + dt.timedelta(seconds=3)).strftime("%Y-%m-%dT%H:%M:%SZ")
MINT["gmail"]["arthur_chase"]["threads"] = {b: _tid(b, "arthur_chase", T["arthur"]) for b in MINT["gmail"]["arthur_chase"]["threads"]}
MINT["gmail"]["hold_invite"]["threads"] = {b: _tid(b, "hold_invite", T["invite"]) for b in MINT["gmail"]["hold_invite"]["threads"]}
MINT["gmail"]["hold_invite"]["threads"][ART] = _tid(ART, "hold_invite", T["invite"])
MINT["contacts"]["brooks"] = _h("contact-brooks", 24); MINT["contacts"]["helper"] = _h("contact-helper", 24)
cur = lambda x: x.replace("'", "\u2019")   # Leonard types curly apostrophes
def write(p, o):
    with open(p, "w") as f:
        json.dump(o, f, indent=1); f.write("\n")
# ---------------------------------------------------------------- base records (all YES for Robert unless noted)
G = lambda n: f"{ROB}/{n}"
BASE = {
 "wire_fail": f"{AD}/1712331142.975829", "motmot_one": f"{AD}/1712331372.614469", "wrong_acct": f"{AD}/1712331718.859679",
 "returned": f"{AD}/1712901800.684259", "robert_books": f"{AD}/1712901837.860709",
 "lucas_card": f"{AD}/1719603595.852129", "lucas_send": f"{AD}/1719603590.685019", "motmot_4032": f"{AD}/1736978214.260099",
 "ground_truth": f"{AD}/1754445718.724799", "pl_accurate": f"{AD}/1754445622.992119",
 "lb_approve": f"{AD}/1694616672.499829", "lb_done": f"{AD}/1694616951.239909", "lb_noswift": f"{AD}/1694561782.067139",
 "node_close": f"{AD}/1735854841.070019", "brooks_wire": f"{AD}/1761844416.830739", "laptop": f"{AD}/1761844454.096829",
 "angels": f"{WD}/1770934638.035469", "draft_note": f"{WD}/1770664700.848759", "linear_keep": f"{WD}/1770933601.686309",
 "carta_chase": f"{WD}/1770932925.126829", "tg_contract": f"{EX}/1760122065.890659", "cf_start": f"{EX}/1764171306.893909",
 "playable_dd": f"{PX}/1741284538.488439", "playable_paid": f"{EX}/1770082607.231919",
 "n_ban_first": G("1795282860741136988"), "n_ban_mod": G("1795509850966005840"), "n_ban_resend": G("1795511257876658998"),
 "wu1": G("1800873055214061794"), "wu2": G("1802092844284446043"), "wu3": G("1803223458475671884"), "wu4": G("1805405368810910191"), "wu5": G("1808201559428745555"),
 "node_mail": G("1815095592611804295"), "lb_await": G("1776934359028762037"), "deel_recipient": G("1776123041340701955"), "bgn_notice": G("1847427662807006290"), "jpm_notice": G("1807851044809802572"),
 "revenue": "snowflake:ANALYTICS.MONETIZATION.REVENUE_DAILY", "store_tx": "snowflake:ANALYTICS.MONETIZATION.STORE_TRANSACTIONS",
 "pl_costs": "f_605121f4a36752645e0ac3", "msa": "f_322bbfdb37d253aa8624b9", "brooks_contract": "f_20a0df3860bb5731d22f07", "robert_root": "d_9f7ba94f7526d54d8482ba", "founders_board": "640643a3fd8f3ca308d9318e",
}
IDS = {
 "ask": f"{WD}/{MINT['slack']['ask']['ts']}", "ask2": f"{WD}/{ASK2_TS}", "statement": f"{LB}/{MINT['slack']['statement']['ts']}", "return_note": "C04UEQVDVB7/1770947533.284619",
 "method": MINT["drive"]["method"], "sheet": MINT["drive"]["sheet"], "deck": MINT["drive"]["deck"],
 "project": MINT["linear"]["project"], "trello": MINT["trello"]["card"],
 "arthur_mail": MINT["gmail"]["arthur_chase"]["threads"][ROB], "hold_leo": MINT["gcal"]["events"][LEO], "hold_rob": MINT["gcal"]["events"][ROB],
 "invite": MINT["gmail"]["hold_invite"]["threads"][ROB], "c_brooks": MINT["contacts"]["brooks"], "c_helper": MINT["contacts"]["helper"],
}
# ---------------------------------------------------------------- planned wording (verbatim for /create-injection)
Q = {
 "ask": cur("<@EMPLOYEE_0016_SLACK_ID> before I start the angel calls on tuesday I want one straight page on what each bet cost us to build and what it brought in. they'll ask and I don't want to wing it. "
             "you know what each of these people did better than I do, can you own it? how I want it counted is in the doc I just wrote, Angel note: how to count the money. more below"),
 "ask2": cur("I put everyone on the SVB notices into the Payee history project in linear, one issue each, and left what we remember on them. use the layout of my Angel note working sheet, keep yours in your drive and share it with "
             "Blake and me. my quick numbers are on that sheet and on the draft deck. when you're done tell me here what each bet cost and brought in and what changes on the deck, I'll update it myself"),
 "method_title": "Angel note: how to count the money",
 "method": cur("Angel note: how to count the money\n"
            "Angels will ask what each bet cost and what it brought in. This is how we count it so the three of us say the same thing. It replaces the quick plan I left on our board.\n"
            "Go by the bank. SVB's Payment Processed notices are the one place I know with a line per payment, and what the banks say is our ground source of truth. Start at the first SVB wires in Sep 2023 and stop at the last run on Feb 2. Anything paid out of Chase isn't in here.\n"
            "What counts is money that left the company and stayed out. A notice is where you start, not the last word. Take a notice as paid unless one of us has said the money came back. If someone we paid closes out their file with us and tells us what they received, that beats the notices for them. Money we moved between our own accounts isn't spending, no bucket for that. Every payee keeps its line, even at zero.\n"
            "If we paid a contractor some other way, it goes in only if a receipt for it reached your mail, at the amount sent, not the fee.\n"
            "Buckets. Build is the team on Deel plus the studios and freelancers who made the games. Everything on Deel counts as team, don't try to split it. Marketing is anything made or bought to get installs (ad networks, agencies, ad creative, playables, trailers): list it under its bet by date like the rest, but keep it out of build cost, I have those numbers. Company is legal, tools, the website, equipment and anything else that wasn't for one of the three games: that goes in the Company column. Our own pay and anyone on Gusto aren't in here.\n"
            "Which bet. Go by the Transaction Date on the notice, the whole payment to one bet: Domino Delights up to Jan 8, 2025, ZM from Jan 9, 2025 to Nov 23, 2025, Combo Fighter from Nov 24, 2025. Don't try to work out who was on what, that's where we'd start arguing.\n"
            "Anything not paid in dollars stays in its own currency next to the line. Don't add it to a dollar total.\n"
            "What each game brought in is its lifetime revenue from the warehouse's daily revenue table, as recorded. Leave Combo Fighter's revenue off for now, on the page, on the deck and when you tell me, until we've checked its first sales.\n"
            "On the Linear project: move each payee's issue to Done once its line is right. If your figure isn't what the notices add up to, say why on the issue first."),
 "project_name": "Payee history",
 "project_desc": "One issue per payee on the SVB notices, for the angel note. The notes are what we remember.",
 "return_note": "fyi that Apr 2024 wire to the account ending 8605 came back to us. Blake had the wrong number, he re-sent it to 3341",
 "statement": ("Hey guys, our accountant closed the Harmony Games file at Leapblock this morning. For your records, the USD wires Leapblock received from you, "
               "by date of your wire: 2023 (from 13 Sep, the first one 33,290) 104,868; 2024 232,726; 2025 62,950; 2026 7,400. Total 407,944 over 30 wires."),
 "arthur_subject": "Chase records",
 "arthur_mail": ("Going through the Chase statements for Sunset's file. One thing while I'm in there: the $4,000 to JPMorgan ***3203 on the SVB notices in Aug 2024 was me. That was our own Chase account, "
                 "I sent it over to put the money back after Carta's renewal came out of Chase. So it never left the company."),
 "sheet_title": "Angel note working", "sheet_header": ["Payee", "Name on the bank", "Bucket", "Domino Delights", "ZM", "Combo Fighter", "Company", "Note"],
 "sheet_rows": [["All USD notices, by date", "", "", "984,888.21", "608,820.50", "73,685.61", "", "quick pass"]],
 "deck_title": "Note to angels (draft)",
 "deck": ["Note to angels (draft)", "What we built: Domino Delights, ZM, Combo Fighter", "What each bet cost to build: Domino Delights $985K, ZM $609K, Combo Fighter $74K", "What each brought in: to fill in", "What happens next: an orderly wind-down, more once we have clarity on final liabilities"],
 "leonard_reply": cur("ah that's the one I couldn't place, thanks"), "trello_comment": "doing this properly now, it's in a doc",
 "trello_title": "Angel note money page", "trello_desc": "quick plan: add up the notices by date and round them. fine for a first pass",
 "hold_title": "Angel calls", "c_brooks_job": "Telegram Contractor",
}
# issue notes: (author, text). Each repeats only what its cited base record says (sc3 Task 1c).
PAYEES = [
 # key, bank spelling, suffix, bucket, notes
 ("Deel", "Deel, Inc.", "8380", "Build", [("leonard", "the team's monthly runs go through here"), ("arthur", "SVB shows it under two spellings, same account")]),
 ("Leapblock", "Leapblock LTD", "1359", "Build", [("leonard", "the saga map crew early on, Martin and Victor through them"), ("arthur", "they invoice at month end so the wire lands the month after")]),
 ("Eveline Art", "Eveline Art S.R.L.", "8501", "Build", [("leonard", "Marcus's company, monthly")]),
 ("Adjoe", "Adjoe GMBH", "5000", "Marketing", [("leonard", "the incent test, three wires")]),
 ("MotMot", "BANCO DE AMERICA", "3341, 8605", "Build", [("arthur", "that's MotMot, paid by the day. SVB shows their bank's name"), ("leonard", "I always just approved what Blake put in")]),
 ("Singular", "Singular Labs Inc", "4015", "Company", [("leonard", "attribution tool, not one game")]),
 ("Node Media", "PERSON_4419_NAME LLC", "0115", "Marketing", [("leonard", "one payment when we closed the account, Jan 2025")]),
 ("TYZ Law Group", "TYZ Law Group", "7534", "Company", [("leonard", "lawyers, the patent scare")]),
 ("Trademark lawyer", "[PERSON_NAME_7200]", "7393", "Company", [("leonard", "the trademark filings")]),
 ("Lucas", "[PERSON_NAME_36400]", "6577", "Build", [("leonard", "mini games dev on Domino Delights")]),
 ("AppLovin", "AppLovin Corporation", "2532", "Marketing", [("leonard", "past due UA bills")]),
 ("Graham Porter", "Graham Porter", "1794", "Build", [("leonard", "art director for a month")]),
 ("JPMorgan", "JPMorgan [PERSON_NAME_4503]", "3203", "Not a cost", [("leonard", "I approved this one in Aug 2024, think it was an advance to one of the contractors but I can't place which")]),
 ("Creative X", "CREATIVE X TEKNOLOJi", "5660", "Marketing", [("leonard", "the first playable")]),
 ("JP (website)", "M [PERSON_NAME_0056]", "4020", "Company", [("leonard", "the website")]),
 ("Nathan Price", "Nathan Price [PERSON_NAME_0047]", "0148", "Build", [("arthur", "short animation job, coins and chests")]),
 ("Martin Walsh", "Martin [PERSON_NAME_7250] Walsh", "3801", "Company", [("arthur", "paid him direct for this one, not through Leapblock")]),
 ("Lauren Brooks", "[PERSON_NAME_7249] Brooks", "5384", "Marketing", [("leonard", "the contract I sent out in Oct, $500 a month")]),
 ("Ozhan", "PERSON_6074_NAME [PERSON_NAME_16238]", "3307", "Build", [("arthur", "2D animation, about a week")]),
 ("UX contractor", "[PERSON_NAME_9100]", "1876", "Build", [("leonard", "second half of the UX milestone")]),
 ("4X helper", "[PERSON_NAME_0054] [PERSON_NAME_0131]", "3139", "Company", [("leonard", "$500 for help on the 4X proposal, not one of the three games")]),
 ("Oleg", "Private Entrepreneur [PERSON_NAME_43315] [PERSON_NAME_0120]", "9368", "Marketing", [("leonard", "video editor, ad videos")]),
]
ISS = {p[0]: MINT["linear"]["issues"][i] for i, p in enumerate(PAYEES)}
# ---------------------------------------------------------------- truth from the 132 notices
MATCH = [("Deel", "Deel"), ("[ORG_NAME_0057]", "Deel"), ("Leapblock", "Leapblock"), ("Eveline", "Eveline Art"), ("BANCO", "MotMot"), ("Adjoe", "Adjoe"),
         ("[SOURCE_ORG_0351]", "Singular"), ("Singular", "Singular"), ("PERSON_4419", "Node Media"), ("TYZ", "TYZ Law Group"), ("[PERSON_NAME_7200]", "Trademark lawyer"),
         ("[PERSON_NAME_36400]", "Lucas"), ("AppLovin", "AppLovin"), ("Graham", "Graham Porter"), ("JPMorgan", "JPMorgan"), ("CREATIVE", "Creative X"), ("M [PERSON", "JP (website)"),
         ("Nathan", "Nathan Price"), ("Martin", "Martin Walsh"), ("[PERSON_NAME_7249]", "Lauren Brooks"), ("PERSON_6074", "Ozhan"), ("[PERSON_NAME_9100]", "UX contractor"),
         ("[PERSON_NAME_0054]", "4X helper"), ("Private", "Oleg")]
def payee(t):
    return next(v for k, v in MATCH if k in t)
def bet(d):
    return "DD" if d < "2025-01-09" else ("ZM" if d < "2025-11-24" else "CF")
BUCKET = {p[0]: p[3] for p in PAYEES}
ONE_GAME = {}
cell = {}
for n in NOT:
    p = payee(n["to"]); u = n["usd"] or 0.0
    cell.setdefault(p, {"DD": 0.0, "ZM": 0.0, "CF": 0.0, "n": 0})
    cell[p][ONE_GAME.get(p, bet(n["txn"]))] += u; cell[p]["n"] += 1
plain = {p: round(sum(c[b] for b in ("DD", "ZM", "CF")), 2) for p, c in cell.items()}
cell["MotMot"]["DD"] -= 4032.0                # returned wire
cell["Lucas"]["DD"] += 7525.0                 # five Western Union transfers, Jun-Aug 2024
cell["Leapblock"]["DD"] += 33290.0            # the Sep 13, 2023 wire
cell["JPMorgan"]["DD"] -= 4000.0              # money moved to the company's own Chase account: a line at zero
cell["Oleg"]["DD"] -= 125.0                   # the wire came back (Leonard's note) and no receipt for the re-send reached Robert's mail
total = {p: round(sum(c[b] for b in ("DD", "ZM", "CF")), 2) for p, c in cell.items()}
build = {b: round(sum(c[b] for p, c in cell.items() if BUCKET[p] == "Build"), 2) for b in ("DD", "ZM", "CF")}
company = round(sum(total[p] for p in total if BUCKET[p] == "Company"), 2)
assert total["MotMot"] == 37056.0 and total["Lucas"] == 13975.0 and total["Leapblock"] == 407944.0 and plain["Deel"] == 1015347.19, total
assert build == {"DD": 959342.64, "ZM": 544433.44, "CF": 72685.61}, build
REVENUE = {"DD": 12331.25, "ZM": 11.99, "CF": None}   # Combo Fighter left off by the method (NB-26)
print("build", build, "company", company)
write(os.path.join(HERE, "truth_sketch.json"), {"build": build, "company_usd": company, "payee_total": total, "plain": plain, "cell": cell, "revenue": REVENUE})
exec(open(os.path.join(HERE, "build_manifest.py")).read())
