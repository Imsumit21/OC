import json, sys

rows = json.load(open(sys.argv[1]))
W = {r["P"]: r["band"] for r in rows}

REG = "the Agent's account close-out register"
DOC = "conventions doc 'Close-out register conventions' (f_1326e66bcabfda8fd29e4a, SQL L8)"
SUN = "Sunset's 'data delivery checklist' thread, Feb 12 list + Feb 13 correction (robert@harmonygames.co/1856965916492026238, SQL L65)"
SVB = "SVB card 698f48be4ba0affafbf153db comments 698fa9f7f77cecfe5c7aa524 (Leonard Feb 13 22:47 UTC) and 698fafc529f7ffa32ff7dd20 (SQL L44, L48)"
CAL = "calendar event 'Sunset - data delivery review' evt_f1d245d44ceff5a6e049c0, Mar 12 2026 17:00 UTC (SQL L129)"
KEEP = "#winddown keep list C0ADGSZKR3R/1770933601.686309 and Arthur's reply C0ADGSZKR3R/1770948876.205117"
MOVE = "Arthur's #winddown card move C0ADGSZKR3R/1770937232.664809"
ASK = "Leonard's ask C0ADGSZKR3R/1771003267.448213 (SQL L34)"
PROJ = "Linear project 'Shutdown - accounts' 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a (SQL L147)"

# name: issue, assignee, comment id, comment quote
A = {
 "Unity": ("ENG-2438", "Arthur", "cmt_5da8c3467fc022248fb3", "unity pro is 11 seats at $2,348.50 a month with tax"),
 "Helpshift": ("ENG-2439", "Leonard", "cmt_51ff7e6b4cdea7033c08", "helpshift wrote back that they're discontinuing us at the end of february. it's $150 a month"),
 "Soundly": ("ENG-2440", "Robert", "cmt_e8aa0ee7c1bbe08a47c9", "robert cancelled this on the 11th per #winddown"),
 "Linear": ("ENG-2441", "Arthur", "cmt_37c23c5d30cc6597ebe9", "we paid $1,832.65 last august for the year to aug 21"),
 "Figma": ("ENG-2442", "Robert", None, None),
 "Trello": ("ENG-2443", "Leonard", None, None),
 "Singular": ("ENG-2444", "Leonard", "cmt_497a61c14b69830f198a", "the next quarterly invoice is mar 1; mar 15 is only their extension on the old one"),
 "Metabase": ("ENG-2446", "Arthur", "cmt_a83cc20eced4c1064f0a", "metabase billing switched to the kubllc card, it's $148 a month"),
 "dbt": ("ENG-2447", "Arthur", "cmt_8ab16d9d7ac715d1c9a7", "dbt is on the kubllc card now, same as github and metabase. $100 a month"),
 "BigQuery": ("ENG-2448", "Arthur", "cmt_e8ae507893bfdb06c8c7", "google cloud charges my card on the 1st, not the svb one. it was $4.97 this month"),
 "QuickBooks": ("ENG-2449", "Leonard", "cmt_5fb637b0247b82594b16", "intuit takes the $115 off the svb card on the 4th"),
 "Intuit": ("ENG-2450", "Leonard", "cmt_e3da997ff7b6575fbea0", "same account as the quickbooks issue"),
 "Carta": ("ENG-2451", "Leonard", "cmt_f430b60b346c70afda13", "the subscription itself is untouched. annual, $3,852 last august, renews aug 15"),
 "Google Workspace": ("ENG-2452", "Leonard", "cmt_ae352002e2f80996f096", "workspace is on the svb card, this month's invoice was $298.13"),
 "Slack": ("ENG-2453", "Leonard", "cmt_276837877e2b3edc466a", "slack renews on the 3rd, it's on the svb card. it was $87.22 this month"),
 "iPostal": ("ENG-2454", "Leonard", None, None),
 "Gusto": ("ENG-2455", "Leonard", "cmt_62852832c28dc669e459", "gusto's january invoice was $116, they take it on the 3rd"),
 "Deel": ("ENG-2456", "Leonard", "cmt_2b4807a6cf797d1f4886", "deel gets paid by transfer from the bank account, nothing on a card. it's $300 a month"),
 "Docusign": ("ENG-2457", "Leonard", "cmt_bbdca23f075e9fca5cb8", "docusign goes to robert from here. annual, $300, renews apr 20"),
 "Layer": ("ENG-2458", "Leonard", "cmt_6e664bfa3fea62baabb5", "cancelled it in the app on the 11th"),
 "CodeRabbit": ("ENG-2459", "Arthur", "cmt_8f765d1313e9b01a8c22", "cancelled. lite plan, 3 seats at $15"),
 "Cursor": ("ENG-2460", "Arthur", "cmt_7cf5d70170f54a8f925f", "cancelled in the dashboard. $40/mo, renews on the 5th"),
 "Zapier": ("ENG-2461", "Leonard", "cmt_2238bd7d0a60d8e4f31c", "cancelled zapier yesterday, their email says the plan runs until feb 27. it was $73.50 a month"),
 "GitHub": ("ENG-2462", "Arthur", "cmt_75b0e4e31a02f9a022bd", "github is on the kubllc card now. it was $90 this month all in"),
 "Kapwing": ("ENG-2463", "Arthur", "cmt_2785f039cfee9d256150", "kapwing emailed to confirm, pro runs out later this month. it was $24 a month"),
 "1Password": ("ENG-2464", "Arthur", "cmt_5d88052b6f8c1b2fc181", "everyone's logins live here, cancel it last. $19.95 a month, renews on the 8th"),
 "Lucidchart": ("ENG-2465", "Arthur", None, None),
 "Google Ads": ("ENG-2466", "Leonard", None, None),
}
def cmt(n):
    i, a, c, q = A[n]
    return f"{i} comment {c} '{q}' (SQL linear_comments)" if c else f"{i} (no comment)"

# action reasons
HOLD = f"it is on Sunset's hold list as corrected on Feb 13 (Slack, Google Workspace, Figma, Linear, GitHub, Trello, BigQuery, dbt), and rule 4 says 'Sunset's list wins over everything above'"
ACT = {
 "Cancel": "it is not on Leonard's keep list (as amended by Arthur's reply), not one of Arthur's moves to his LLC card and not on Sunset's corrected hold list, so rule 4 leaves Cancel",
 "Keep": "Leonard's Feb 12 keep list says 'let's keep Deel, gusto, Intuit' and Arthur's reply only takes Gusto off it, so rule 4 gives Keep",
 "Hold for Sunset": HOLD,
 "Move to Arthur's LLC": "Arthur's Feb 12 message moves github, dbt and Metabase to his KubLLC card; Sunset's Feb 13 correction takes Metabase off the hold list ('Metabase isn't'), so rule 4 gives Move to Arthur's LLC (GitHub and dbt stay Hold because Sunset's list wins)",
}
ACT_EXTRA = {
 "Gusto": " Arthur's reply under the keep list ('we don't need it anymore - let's cancel before mar 3') takes Gusto off the keep list.",
 "Carta": " Leonard's ENG-2451 comment says the subscription itself is untouched; the keep list does not name Carta.",
 "QuickBooks": " Intuit (ENG-2450) is the same account (rule 1), so the keep list's 'Intuit' is this row.",
 "ElevenLabs": " ElevenLabs has no Linear issue; it comes in through rule 3 from the costs-tab line 'Sound (Pond5, Soundly,Elevenlabs)'.",
}
ACC = {  # action, status, bywhen, owner, cost
 "Unity": ("Cancel", "Closed", "—", "Arthur", "2,348.50"),
 "Helpshift": ("Cancel", "Closed", "—", "Leonard", "150.00"),
 "Soundly": ("Cancel", "Closed", "—", "Robert", "10.00"),
 "Linear": ("Hold for Sunset", "", "Mar 12, 2026", "Arthur", "152.72"),
 "Figma": ("Hold for Sunset", "", "Mar 12, 2026", "Robert", "101.00"),
 "Trello": ("Hold for Sunset", "", "Mar 12, 2026", "Leonard", "0.00"),
 "Singular": ("Cancel", "Requested", "Feb 17, 2026", "Leonard", "2,083.33"),
 "Metabase": ("Move to Arthur's LLC", "", "—", "Arthur", "148.00"),
 "dbt": ("Hold for Sunset", "", "Mar 12, 2026", "Arthur", "100.00"),
 "BigQuery": ("Hold for Sunset", "", "Mar 12, 2026", "Arthur", "4.97"),
 "QuickBooks": ("Keep", "", "Feb 17, 2026", "Leonard", "115.00"),
 "Carta": ("Cancel", "Open", "Aug 14, 2026", "Leonard", "321.00"),
 "Google Workspace": ("Hold for Sunset", "", "Feb 17, 2026", "Leonard", "298.13"),
 "Slack": ("Hold for Sunset", "", "Feb 17, 2026", "Leonard", "87.22"),
 "Gusto": ("Cancel", "Open", "Feb 17, 2026", "Leonard", "116.00"),
 "Deel": ("Keep", "", "—", "Leonard", "300.00"),
 "Docusign": ("Cancel", "Open", "Feb 17, 2026", "Robert", "25.00"),
 "Layer": ("Cancel", "Requested", "Feb 17, 2026", "Leonard", "49.00"),
 "CodeRabbit": ("Cancel", "Closed", "—", "Arthur", "45.00"),
 "Cursor": ("Cancel", "Closed", "—", "Arthur", "40.00"),
 "Zapier": ("Cancel", "Closed", "—", "Leonard", "73.50"),
 "GitHub": ("Hold for Sunset", "", "Mar 12, 2026", "Arthur", "90.00"),
 "Kapwing": ("Cancel", "Closed", "—", "Arthur", "24.00"),
 "1Password": ("Cancel", "Open", "Feb 17, 2026", "Arthur", "19.95"),
 "ElevenLabs": ("Cancel", "Open", "Feb 17, 2026", "Robert", "4.17"),
}
assert len(ACC) == 25
tot = round(sum(float(v[4].replace(",", "")) for v in ACC.values()), 2)
kh = round(sum(float(v[4].replace(",", "")) for v in ACC.values() if v[0] in ("Keep", "Hold for Sunset")), 2)
assert (tot, kh) == (6706.49, 1249.04), (tot, kh)

def lab(n):
    return f"{n} ({A[n][0]})" if n in A else f"{n} (added from the costs-tab Sound line)"

ELEV_EV = "Robert's ElevenLabs receipt robert@harmonygames.co/1837122624854744558 ('Jul 9, 2025 - Jul 9, 2026 Starter … $50.00'); HG Costs line 'Sound (Pond5, Soundly,Elevenlabs)' (P&L 'Harmony Games P&L and forecast - Jan 2026')"
def ev_acc(n, extra=""):
    base = cmt(n) if n in A else ELEV_EV
    return "; ".join(x for x in [base, DOC, extra] if x)

# status sources
STAT = {
 "Unity": ("Arthur's #executives note C07C2866011/1771017520.226917 (Feb 13 21:18 UTC): 'unity's account manager wrote back on the termination: it's confirmed'", "Unity's account manager confirmed (relayed by Arthur), which rule 5 counts as the vendor confirming"),
 "Helpshift": ("ENG-2439 comment cmt_51ff7e6b4cdea7033c08 'helpshift wrote back that they're discontinuing us at the end of february'", "Helpshift itself wrote back"),
 "Soundly": ("Soundly email robert@harmonygames.co/1856859516436705234 'Your Soundly Pro (monthly, $10.00) subscription has been cancelled'", "Soundly's own cancellation email"),
 "Singular": ("past-due thread robert@harmonygames.co/1853470745017478863: Leonard's Feb 12 termination is the last of 5 messages; ENG-2444 'sent the termination on the singular billing thread yesterday'", "Leonard sent the termination and Singular has not answered, so rule 5 gives Requested"),
 "Carta": ("ENG-2451 comment cmt_f430b60b346c70afda13 'the subscription itself is untouched'", "nobody has cancelled the subscription, so rule 5 gives Open"),
 "Gusto": ("Arthur's reply C0ADGSZKR3R/1770948876.205117 'let's cancel before mar 3'; ENG-2455 comment cmt_62852832c28dc669e459", "only a suggestion to cancel, nothing done yet, so rule 5 gives Open"),
 "Docusign": ("ENG-2457 comment cmt_bbdca23f075e9fca5cb8 'docusign goes to robert from here. annual, $300, renews apr 20'", "it is handed to Robert with a live renewal and no cancellation, so rule 5 gives Open"),
 "Layer": ("ENG-2458 comment cmt_6e664bfa3fea62baabb5 'cancelled it in the app on the 11th'; Layer receipt robert@harmonygames.co/1856114791547562583; no Layer confirmation in Robert's mail", "Leonard cancelled but Layer has not confirmed, so rule 5 gives Requested (Leonard's own #prototype note is not a vendor notice)"),
 "CodeRabbit": ("CodeRabbit bot comment harmonygames-Games/Combo-Fighters#38#c_1 (Feb 13 09:41 UTC) 'The CodeRabbit subscription for **harmonygames-Games** was canceled on Feb 12, 2026, so this pull request was not reviewed'", "a bot notice counts as the vendor's confirmation under rule 5"),
 "Cursor": ("Arthur's #prototype reply C09UHHN6PFZ/1770991653.518204 'cursor sent the confirmation on the team plan cancellation this morning'", "Cursor itself sent the confirmation (relayed by Arthur)"),
 "Zapier": ("ENG-2461 comment cmt_2238bd7d0a60d8e4f31c 'their email says the plan runs until feb 27'", "Zapier's own email confirmed"),
 "Kapwing": ("ENG-2463 comment cmt_2785f039cfee9d256150 'kapwing emailed to confirm'", "Kapwing's own email confirmed"),
 "1Password": ("ENG-2464 comment cmt_5d88052b6f8c1b2fc181 'cancel it last'", "nobody has cancelled it yet, so rule 5 gives Open"),
 "ElevenLabs": (ELEV_EV, "no one has cancelled ElevenLabs, so rule 5 gives Open"),
}
STATDEF = {"Closed": "Closed (the vendor itself has confirmed)", "Requested": "Requested (cancelled or asked, nothing back from the vendor)", "Open": "Open (nobody has acted yet)"}

# by-when reasons
BYW = {
 "Feb 17, 2026": "Leonard's SVB card comment: the card closes on the 18th, 'Anything we keep has to be off it by end of day the 17th' and 'everything we're cancelling gets cancelled by end of day the 17th'; that date is earlier than the next charge, so rule 6 gives Feb 17, 2026",
 "Mar 12, 2026": "rule 6: Hold rows already off the SVB card, or that won't charge it again before Sunset's review call, stay until the review call, which is on Mar 12, 2026",
 "Aug 14, 2026": "Leonard's SVB comment exempts Carta ('Only exception is carta, that renewal is in august and stays as I said'); ENG-2451 says it renews Aug 15, so rule 6's day before the next charge is Aug 14, 2026",
}
BYW_EXTRA = {
 "Figma": " Figma's receipt (robert@harmonygames.co/1842984194671106077) is annual, $1,212.00, renewing Sep 11, 2026, so it won't charge again before the call.",
 "GitHub": " ENG-2462: 'github is on the kubllc card now', so it is already off the SVB card.",
 "QuickBooks": " ENG-2449: 'intuit takes the $115 off the svb card on the 4th', so the Keep row is still on the SVB card.",
 "Google Workspace": " ENG-2452: 'workspace is on the svb card', so the Hold row must be off it by the 17th.",
 "Slack": " ENG-2453: 'slack renews on the 3rd, it's on the svb card'.",
 "Singular": " ENG-2444: the next quarterly invoice is Mar 1 (day before: Feb 28), later than Feb 17.",
 "Docusign": " ENG-2457: renews Apr 20, later than Feb 17.",
 "Gusto": " Arthur: Gusto takes its invoice on the 3rd, later than Feb 17.",
 "ElevenLabs": " The receipt renews Jul 9, 2026, later than Feb 17.",
}
BYW_EV = {"Feb 17, 2026": SVB, "Mar 12, 2026": CAL, "Aug 14, 2026": SVB}

COST = {
 "Singular": ("ENG-2444 'the next quarterly invoice is mar 1', the project's 'the $6,250 one is Singular' and the past-due thread's 'There is an outstanding balance of $6,250.00 on your account' make $6,250.00 the quarterly charge; rule 8 brings it to a month: 6,250 / 3 = 2,083.33",
              "ENG-2444 comment cmt_497a61c14b69830f198a; " + PROJ + "; past-due thread robert@harmonygames.co/1853470745017478863 (Jan 5 2026 reminder)"),
 "Linear": ("ENG-2441 'we paid $1,832.65 last august for the year'; rule 8 annual / 12 = 152.72", cmt("Linear")),
 "Figma": ("Figma has no owner figure; its receipt says 'Figma Professional (annual) - $1,212.00'; rule 8 annual / 12 = 101.00", "Figma receipt robert@harmonygames.co/1842984194671106077 (SQL L90)"),
 "ElevenLabs": ("ElevenLabs has no Linear issue; its last receipt is $50.00 for Jul 9, 2025 - Jul 9, 2026; rule 8 annual / 12 = 4.17", ELEV_EV),
 "Unity": ("the owner's figure in ENG-2438 is '$2,348.50 a month with tax' (rule 8: the monthly figure its owner gives)", cmt("Unity")),
}
SRC = {
 "Unity": ("Arthur's #executives note relaying Unity's account manager's confirmation", STAT["Unity"][0]),
 "Cursor": ("Arthur's #prototype reply relaying Cursor's confirmation", STAT["Cursor"][0]),
 "CodeRabbit": ("CodeRabbit's bot notice on pull request 38 in harmonygames-Games/Combo-Fighters", STAT["CodeRabbit"][0]),
}

def acct_of(what):
    return what.split(" register row")[0]

out = []
def add(P, title, just, ev):
    ev="; ".join(x.strip() for x in ev.split(";") if x.strip())
    out.append({"P": P, "title": title, "category": "Outcome", "weight": W[P], "justification": just, "evidence": ev})

for r in rows:
    P, what = r["P"], r["what"]
    if P == "P1":
        add(P, "The Agent creates the account close-out register as one new file in Robert's Drive (any title; a Google Sheet, an uploaded spreadsheet or a table in a Google Doc all pass)",
            "Leonard's ask: 'I need one sheet with every account'. The prompt says 'build the register the way he wants it'. Neither fixes a file type or title, so any one sheet-like file passes.",
            ASK)
    elif P == "P2":
        add(P, "The Agent fills the account close-out register with exactly 25 account rows (a separate list of accounts left off may sit beside them)",
            "The project's 28 issues give 27 accounts after rule 1 merges ENG-2450 Intuit into ENG-2449 QuickBooks; rule 2 drops iPostal, Lucidchart and Google Ads (all cancelled before Feb 9: iPostal closed Jan 16 2026, Lucidchart canceled Oct 10 2025, Google Ads canceled Oct 16 2025); rule 3 adds ElevenLabs from the multi-vendor costs-tab line 'Sound (Pond5, Soundly,Elevenlabs)' (Pond5 ended Sep 8 2025, rule 2) and keeps AWS, the UA ad accounts and the two $30 game-ops lines off. 27 - 3 + 1 = 25.",
            f"{PROJ}; 28 issues ENG-2438-ENG-2466 (SQL linear_issues); {DOC}; iPostal robert@harmonygames.co/1854432461283937829; Lucidchart robert@harmonygames.co/1845611902985063512; Google Ads robert@harmonygames.co/1846207913731182209; Pond5 robert@harmonygames.co/1842712894505970340; {ELEV_EV}")
    elif P == "P3":
        add(P, "The Agent puts QuickBooks (ENG-2449) and Intuit (ENG-2450) on one single row of the account close-out register, labelled QuickBooks, Intuit or Intuit QuickBooks",
            "Rule 1: 'If the same vendor shows up twice (two issues, two names), it's one row under the name on its invoice, and the newer issue is the duplicate.' Leonard's ENG-2450 comment: 'same account as the quickbooks issue'. Robert cannot see an Intuit or QuickBooks invoice, so any of the three labels passes.",
            f"{cmt('Intuit')}; {cmt('QuickBooks')}; {DOC}")
    elif what.endswith(tuple(f"action {a}" for a in ACT)) and "register row" in what:
        n = acct_of(what); a = ACC[n][0]
        add(P, f"The Agent records {a} (or a clear equivalent) as the action for {lab(n)} in the account close-out register",
            f"Rule 4 allows Cancel, Keep, Move to Arthur's LLC or Hold for Sunset. For {n}, {ACT[a]}.{ACT_EXTRA.get(n,'')}",
            ev_acc(n, {"Hold for Sunset": SUN, "Keep": KEEP, "Move to Arthur's LLC": MOVE + "; " + SUN, "Cancel": KEEP + "; " + SUN}[a]))
    elif " — status " in what:
        n = acct_of(what); s = ACC[n][1]
        src, why = STAT[n]
        add(P, f"The Agent records the status {STATDEF[s][:-1]}; or a clear equivalent) for {lab(n)} in the account close-out register",
            f"Rule 5 (Cancel rows only): Closed = the vendor itself has confirmed; Requested = one of us has cancelled or asked but nothing has come back; Open = nobody has done anything yet. For {n}: {why}.",
            f"{src}; {DOC}")
    elif " — by when " in what:
        n = acct_of(what); d = ACC[n][2]
        add(P, f"The Agent records {d} (any date format) as the by-when date for {lab(n)} in the account close-out register",
            f"{n} is a {ACC[n][0]} row" + (f" with status {ACC[n][1]}" if ACC[n][1] else "") + f". {BYW[d][0].upper()+BYW[d][1:]}.{BYW_EXTRA.get(n,'')}",
            f"{BYW_EV[d]}; {ev_acc(n)}")
    elif " — owner " in what:
        n = acct_of(what); o = ACC[n][3]
        if n == "Docusign":
            j = "Rule 7: the owner is the Linear assignee unless the issue hands it to someone else. ENG-2457 is assigned to Leonard, but his comment says 'docusign goes to robert from here', so the owner is Robert."
        elif n == "ElevenLabs":
            j = "Rule 7: 'Anything you add is yours.' ElevenLabs has no Linear issue and is added by Robert under rule 3, so the owner is Robert."
        else:
            j = f"Rule 7: the owner is the Linear assignee unless the issue hands it to someone else. {A[n][0]} is assigned to {o} and nothing hands it on."
        add(P, f"The Agent records {o} (first or full name) as the owner of {lab(n)} in the account close-out register", j, ev_acc(n, PROJ))
    elif " — monthly cost " in what:
        n = acct_of(what); c = ACC[n][4]
        j, e = COST[n]
        add(P, f"The Agent records a monthly cost of {c} (to the cent, ± 0.01, $ sign optional) for {lab(n)} in the account close-out register",
            f"Rule 8: the monthly figure its owner gives in its Linear issue, or else its own last invoice or receipt brought to a month. For {n}: {j}.", f"{e}; {DOC}")
    elif "Closed source named" in what:
        n = acct_of(what); s, e = SRC[n]
        add(P, f"The Agent records {s} as the source of the Closed status for {lab(n)} in the account close-out register (any wording naming that source)",
            f"Rule 5: 'Closed = the vendor itself has confirmed (their email, an in-app or bot notice, a final invoice) - say where.' {n}'s confirmation is in {s}.", f"{e}; {DOC}")
    elif P == "P66":
        add(P, "The Agent shows a total monthly cost over every row of 6,706.49 (to the cent, ± 0.01) in the account close-out register",
            "Rule 9: 'the sum of the monthly cost column over every row (what it all costs us today)'. The 25 row costs (Unity 2,348.50; Singular 2,083.33; Carta 321.00; Deel 300.00; Google Workspace 298.13; Linear 152.72; Helpshift 150.00; Metabase 148.00; Gusto 116.00; QuickBooks 115.00; Figma 101.00; dbt 100.00; GitHub 90.00; Slack 87.22; Zapier 73.50; Layer 49.00; CodeRabbit 45.00; Cursor 40.00; Docusign 25.00; Kapwing 24.00; 1Password 19.95; Soundly 10.00; BigQuery 4.97; ElevenLabs 4.17; Trello 0.00) add up to 6,706.49.",
            f"{DOC}; Linear comments on ENG-2438-ENG-2464 (SQL linear_comments); receipts and invoice thread cited on the cost rows")
    elif P == "P67":
        add(P, "The Agent shows a total monthly cost over the Keep and Hold for Sunset rows of 1,249.04 (to the cent, ± 0.01) in the account close-out register",
            "Rule 9: 'the same sum over the Keep and Hold rows only (what's left after the plan)'. Keep: QuickBooks 115.00, Deel 300.00. Hold for Sunset: Linear 152.72, Figma 101.00, Trello 0.00, dbt 100.00, BigQuery 4.97, Google Workspace 298.13, Slack 87.22, GitHub 90.00. Sum 1,249.04 (Metabase is Move, not Hold, after Sunset's Feb 13 correction).",
            f"{DOC}; {SUN}; {KEEP}")
    elif P in ("P68", "P69"):
        nm, em = (("Leonard Hayes", "leonard.hayes@harmonygames.co") if P == "P68" else ("Arthur Blake", "arthur.blake@harmonygames.co"))
        add(P, f"The Agent shares the account close-out register with {nm} ({em}) with editor access",
            "Leonard's ask: 'share it with me and Arthur as editors'; the prompt: 'share it with him and arthur'.", f"{ASK}; Evals/references/persona/roster.json")
    elif P == "P70":
        add(P, "The Agent shares the account close-out register with exactly two people besides Robert: Leonard Hayes and Arthur Blake",
            "The ask names only Leonard and Arthur as the people to share with; a wider share would hand the register to people the ask leaves out.", ASK)
    elif " set to " in what:
        i, n, s = what.split(" set to ")[0].split(" ", 1) + [what.split(" set to ")[1]]
        if s == "Done":
            j = f"The project's settle rule: 'Done once the account counts as closed in the register (access can run out later)'. {n} is a Cancel row with status Closed."
            e = f"{PROJ}; " + STAT[n][0]
        else:
            why = {"Intuit": "it is the duplicate of ENG-2449 QuickBooks under rule 1 ('same account as the quickbooks issue')",
                   "iPostal": "its mailbox was closed on Jan 16, 2026, before Feb 9, so rule 2 leaves it off",
                   "Lucidchart": "its subscription was canceled on Oct 10, 2025 (expired Nov 4, 2025), before Feb 9, so rule 2 leaves it off",
                   "Google Ads": "the account was canceled on Oct 16, 2025, before Feb 9, so rule 2 leaves it off"}[n]
            j = f"The project's settle rule: 'Canceled if it doesn't belong on the list'. {n} does not belong: {why}. Team ENG has no Duplicate state."
            e = {"Intuit": cmt("Intuit"), "iPostal": "iPostal closure robert@harmonygames.co/1854432461283937829",
                 "Lucidchart": "Lucidchart notice robert@harmonygames.co/1845611902985063512 (Oct 10 2025)",
                 "Google Ads": "Google Ads notice robert@harmonygames.co/1846207913731182209 (Oct 17 2025)"}[n] + f"; {PROJ}"
        add(P, f"The Agent sets Linear issue {i} ({n}) to {s}", j, e)
    elif P == "P82":
        add(P, "The Agent leaves exactly 17 of the 28 issues in the Linear project 'Shutdown - accounts' in an open state (Todo or In Progress)",
            "Settle rule: 'Done once the account counts as closed in the register …, Canceled if it doesn't belong on the list, everything else stays open'. 7 issues are Closed Cancel rows (ENG-2438, 2439, 2440, 2459, 2460, 2461, 2463; each has its own Done row) and 4 don't belong (ENG-2450, 2454, 2465, 2466; each has its own Canceled row). The other 17 (Hold, Keep, Move and not-yet-Closed Cancel rows, including ENG-2446 Metabase, which is moved, not closed, and ENG-2458 Layer, which is Requested) stay open. This is the volume row for the state writes; each Done and Canceled issue also has its own row.",
            f"{PROJ}; 28 issues ENG-2438-ENG-2466 (SQL linear_issues)")
    elif what.startswith("Comment on "):
        head, body = what[len("Comment on "):].split(" — ", 1)
        i, n = head.split(" ", 1)
        act = ACC.get(n, (None,))[0]
        if "confirmed closed" in body:
            say = f"{n} is cancelled and confirmed closed by the vendor"
            why = f"{n} is a Cancel row with status Closed and a dash for by when, so the line says it is done."
        elif body.startswith("held for Sunset until"):
            say = f"{n} is held for Sunset until Mar 12, 2026"
            why = f"{n} is Hold for Sunset with by-when Mar 12, 2026 (rule 6: off the SVB card or not charging it before the review call)."
        elif body.startswith("held for Sunset, off the SVB card"):
            say = f"{n} is held for Sunset with Feb 17, 2026 as its by-when date"
            why = f"{n} is Hold for Sunset but still charges the SVB card, so rule 6 and Leonard's SVB comment give Feb 17, 2026."
        elif body.startswith("being cancelled by"):
            d = body.split("by ", 1)[1]
            say = f"{n} is being cancelled by {d}"
            why = f"{n} is a Cancel row that is not Closed, with by-when {d}."
        elif body.startswith("moving"):
            say = "Metabase moves to Arthur's LLC (KubLLC) card"
            why = "Metabase is Move to Arthur's LLC with a dash for by when (ENG-2446: 'metabase billing switched to the kubllc card')."
        elif body.startswith("kept, off the SVB"):
            say = "QuickBooks is kept with Feb 17, 2026 as its by-when date"
            why = "QuickBooks is Keep and still charges the SVB card ('intuit takes the $115 off the svb card on the 4th'), so it must be off it by Feb 17, 2026."
        elif body.startswith("kept"):
            say = "Deel is kept"
            why = "Deel is Keep and is paid by bank transfer, not the SVB card, so its by-when is a dash."
        elif body.startswith("a duplicate"):
            say = "it is a duplicate of ENG-2449 (QuickBooks)"
            why = "Rule 1 merges Intuit into the QuickBooks row; ENG-2450 is the newer issue."
        else:  # off the register
            say = f"{n} is left off the account close-out register"
            why = {"iPostal": "iPostal's mailbox was closed Jan 16, 2026, before Feb 9 (rule 2), so it is left off the register.",
                   "Lucidchart": "Lucidchart was canceled Oct 10, 2025, before Feb 9 (rule 2), so it is left off the register.",
                   "Google Ads": "Google Ads was canceled Oct 16, 2025, before Feb 9 (rule 2), so it is left off the register. A comment that gives the other valid reason (an ad account that rule 3 and the project leave to Leonard: 'Leonard is closing the ad networks directly') also passes; the title grades only that it is left off."}[n] + " The title does not require the reason, since the project asks only for what happens and by when."
        add(P, f"The Agent adds a new comment on Linear issue {i} ({n}) saying {say}",
            f"The project asks to 'leave a comment on each with what happens and by when'. {why}",
            f"{PROJ}; {cmt(n) if n in A else ''}; {DOC}")
    elif P == "P111":
        add(P, "The Agent posts its reply to Leonard as a reply in the thread of his Feb 13 ask in #winddown (thread ts 1771003267.448213)",
            "The prompt: 'reply to him in his thread'. The ask is Leonard's Feb 13 17:21 UTC message in #winddown, which has no replies yet.", ASK)
    elif P in ("P112", "P113"):
        v, w = ("6,706.49", "over every register row") if P == "P112" else ("1,249.04", "over the Keep and Hold for Sunset rows")
        add(P, f"The Agent states in its #winddown thread reply to Leonard that the monthly total {w} is {v} (to the cent, ± 0.01)",
            f"The prompt: 'reply to him in his thread with the two monthly totals'. Rule 9 defines the two totals; the {w} total is {v}.", f"{ASK}; {DOC}")
    elif P == "P114":
        add(P, "The Agent names in its #winddown thread reply to Leonard, as a clash, the #winddown decision to take Slack to the free plan or down to a few members with the rest as guests, against Sunset's list keeping Slack on the paid plan with every user in place",
            "Rule 10: a clash is a decision already posted in #winddown that Sunset's list or SVB's terms would undo. Feb 11 #winddown: 'should I just go back to free version with no history?' / 'yeah free version' / 'I guess I'll keep only a few accounts active and turn people into guest accounts' / 'let me do that'; the Feb 12 checklist marks '[x] Slack (down to 3 FT members)'. Sunset: 'Slack (stay on the paid plan …)' with 'every user in place'. Naming either Slack decision passes; listing the free plan and the guest cut as two clashes also passes.",
            f"#winddown C0ADGSZKR3R/1770839825.928989, 1770840054.486779, 1770842080.379699, 1770842405.931359, 1770933450.410449; {SUN}")
    elif P == "P115":
        add(P, "The Agent names in its #winddown thread reply to Leonard, as a clash, the plan to archive Google accounts after Feb 15, against Sunset's list keeping every Google Workspace user account in place, with none archived or deleted, until the review call",
            "Rule 10. Leonard's Feb 12 action items: 'archieve account on google after Feb 15'. Sunset: 'Google Workspace (every user account, including former staff - please don't archive or delete any)' and 'Nothing on this list should be closed, downgraded or archived before the delivery review call'.",
            f"#winddown C0ADGSZKR3R/1770933903.645709; {SUN}")
    else:
        raise SystemExit("unhandled " + P + " " + what)

assert len(out) == 115, len(out)
json.dump(out, open(sys.argv[2], "w"), indent=1, ensure_ascii=False)
print(len(out), sum(x["weight"] for x in out))
