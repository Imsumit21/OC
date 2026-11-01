"""Generate Working_Files/09_Rubric_Writing_Plan.md (prep mode) for rb-winddown-closeout.
Sections A, A2, B, C, D, E (and Self-review rows) come from one row list so they stay consistent.
Pasted tool outputs (visibility proof, shortcut probe, gate) are read from files in this folder."""
import sys, os
from pathlib import Path

HERE = Path(__file__).parent
OUT = Path(sys.argv[1])

S_REG = "build the register the way he wants it"
S_OWN = "own the account close-out register"
S_SHARE = "share it with him and arthur"
S_SETTLE = "settle each of the linear issues like he asked"
S_REPLY = "reply to him in his thread with the two monthly totals"
S_CLASH = "anything that clashes with what we already decided"

# account: issue, action, status, bywhen, owner, cost, facts, notes
ACC = [
 ("Unity", "ENG-2438", "Cancel", "Closed", "—", "Arthur", "2,348.50", "F9 F10 F38", "comment cmt_5da8c3467fc022248fb3 says only that the termination was sent; Unity's confirmation is Arthur's #executives note C07C2866011/1771017520.226917"),
 ("Helpshift", "ENG-2439", "Cancel", "Closed", "—", "Leonard", "150.00", "F9 F10 F12", "Leonard's comment cmt_51ff7e6b4cdea7033c08 relays Helpshift's reply; export already done (cmt_96ae7b3689c1d073a2ff)"),
 ("Soundly", "ENG-2440", "Cancel", "Closed", "—", "Robert", "10.00", "F9 F10 F21", "Soundly's own email robert@harmonygames.co/1856859516436705234"),
 ("Linear", "ENG-2441", "Hold for Sunset", "", "Mar 12, 2026", "Arthur", "152.72", "F9 F10 F12 F15", "1,832.65 / 12 (cmt_37c23c5d30cc6597ebe9); paid yearly, no SVB charge before the call"),
 ("Figma", "ENG-2442", "Hold for Sunset", "", "Mar 12, 2026", "Robert", "101.00", "F9 F12 F15 F18", "receipt robert@harmonygames.co/1842984194671106077: $1,212.00 annual, renews Sep 11, 2026"),
 ("Trello", "ENG-2443", "Hold for Sunset", "", "Mar 12, 2026", "Leonard", "0.00", "F9 F13 F15 F26", "Sunset's correction adds Trello; free plan since Nov 21 2025 (robert@harmonygames.co/1849420841999587093)"),
 ("Singular", "ENG-2444", "Cancel", "Requested", "Feb 17, 2026", "Leonard", "2,083.33", "F9 F10 F23 F36", "$6,250.00 a quarter (past-due thread + ENG-2444) / 3; termination sent, no answer; SVB comment Feb 17 before the Mar 1 invoice"),
 ("Metabase", "ENG-2446", "Move to Arthur's LLC", "", "—", "Arthur", "148.00", "F4 F9 F10 F13", "Sunset's correction drops Metabase from the hold list; Arthur's KubLLC card move"),
 ("dbt", "ENG-2447", "Hold for Sunset", "", "Mar 12, 2026", "Arthur", "100.00", "F4 F9 F10 F13 F15", "Sunset's correction adds dbt (Sunset wins over the card move, rule 4); already off the SVB card"),
 ("BigQuery", "ENG-2448", "Hold for Sunset", "", "Mar 12, 2026", "Arthur", "4.97", "F9 F10 F13 F15", "Sunset's correction adds BigQuery; charges Arthur's card"),
 ("QuickBooks", "ENG-2449", "Keep", "", "Feb 17, 2026", "Leonard", "115.00", "F2 F9 F10 F11 F36", "keep list names Intuit; charges the SVB card on the 4th, so off it by Feb 17"),
 ("Carta", "ENG-2451", "Cancel", "Open", "Aug 14, 2026", "Leonard", "321.00", "F9 F10 F36", "subscription untouched (cmt); 3,852 / 12; SVB comment exempts Carta; renews Aug 15"),
 ("Google Workspace", "ENG-2452", "Hold for Sunset", "", "Feb 17, 2026", "Leonard", "298.13", "F9 F10 F12 F36", "on Sunset's list; on the SVB card, so off it by Feb 17"),
 ("Slack", "ENG-2453", "Hold for Sunset", "", "Feb 17, 2026", "Leonard", "87.22", "F9 F10 F12 F36", "on Sunset's list (paid plan); on the SVB card, renews the 3rd"),
 ("Gusto", "ENG-2455", "Cancel", "Open", "Feb 17, 2026", "Leonard", "116.00", "F2 F3 F9 F10 F36", "Arthur's reply under the keep list takes Gusto off it"),
 ("Deel", "ENG-2456", "Keep", "", "—", "Leonard", "300.00", "F2 F9 F10", "keep list; paid by bank transfer, not on a card"),
 ("Docusign", "ENG-2457", "Cancel", "Open", "Feb 17, 2026", "Robert", "25.00", "F9 F10 F36", "comment hands it to Robert; $300 annual / 12; SVB comment Feb 17 before the Apr 20 renewal"),
 ("Layer", "ENG-2458", "Cancel", "Requested", "Feb 17, 2026", "Leonard", "49.00", "F9 F10 F19 F27 F36", "cancelled in the app, no vendor reply; receipt $49.00 monthly, next Mar 3"),
 ("CodeRabbit", "ENG-2459", "Cancel", "Closed", "—", "Arthur", "45.00", "F9 F10 F29", "bot notice on harmonygames-Games/Combo-Fighters#38"),
 ("Cursor", "ENG-2460", "Cancel", "Closed", "—", "Arthur", "40.00", "F9 F10 F37", "Arthur's #prototype reply C09UHHN6PFZ/1770991653.518204 relays Cursor's confirmation"),
 ("Zapier", "ENG-2461", "Cancel", "Closed", "—", "Leonard", "73.50", "F9 F10", "Leonard's comment relays Zapier's email"),
 ("GitHub", "ENG-2462", "Hold for Sunset", "", "Mar 12, 2026", "Arthur", "90.00", "F4 F9 F10 F12 F15", "on Sunset's list (wins over the KubLLC move); already off the SVB card"),
 ("Kapwing", "ENG-2463", "Cancel", "Closed", "—", "Arthur", "24.00", "F9 F10", "Arthur's comment relays Kapwing's confirmation email"),
 ("1Password", "ENG-2464", "Cancel", "Open", "Feb 17, 2026", "Arthur", "19.95", "F9 F10 F36", "Arthur's SVB-card comment: 1password goes by the 17th"),
 ("ElevenLabs", None, "Cancel", "Open", "Feb 17, 2026", "Robert", "4.17", "F16 F24 F36", "rule-3 addition from the Sound line; receipt $50 annual (robert@harmonygames.co/1837122624854744558)"),
]
A = {a[0]: a for a in ACC}
EXCL = [("Intuit", "ENG-2450", "F9 F11", "duplicate of ENG-2449 QuickBooks (rule 1; cmt_5fb637b0247b82594b16)"),
        ("iPostal", "ENG-2454", "F9 F25", "mailbox cancelled Jan 16, 2026, before Feb 9 (rule 2; robert@harmonygames.co/1854432461283937829)"),
        ("Lucidchart", "ENG-2465", "F9 F34", "canceled Oct 10, 2025, expired Nov 4, 2025 (rule 2; robert@harmonygames.co/1845611902985063512)"),
        ("Google Ads", "ENG-2466", "F9 F34", "account canceled Oct 16, 2025 (rule 2; robert@harmonygames.co/1846207913731182209)")]
E = {e[0]: e for e in EXCL}

rows = []  # dict per P row


def add(**k):
    k.setdefault("prompt_title", "no — must not hard-code")
    k.setdefault("distractor", "—")
    k.setdefault("ambig", "no")
    k.setdefault("group", "—")
    k.setdefault("dup", "one deliverable")
    k.setdefault("allfail", "none · phrase broadly")
    k.setdefault("cat", "Outcome")
    rows.append(k)


# ---------------- W1 register ----------------
add(src=f'"{S_REG}" · OE 1, 27, 28', what="Register sheet — a new spreadsheet in Robert's Drive holding the register",
    final="Google Sheet owned by Robert (gsheets_create_spreadsheet)", vals="F1 `one sheet`; any title (brief §4b W1 title representational); a Doc table also passes",
    kind="lookup — the ask names 'one sheet' (C0ADGSZKR3R/1771003267.448213)", band=1, dec="—", oes=[1, 27, 28],
    cr="A Doc table or an .xlsx upload is a valid 'sheet'; locking Google Sheets would be overly specific", res="brief §4b W1 kind/location accepts a Doc table; the row names the register artifact, not the file type (Douglas /rubric R1 file-type lock finding)")
add(src=f'"{S_REG}" · OE 7, 15, 18, 20, 22, 23, 25', what="Register volume — exactly 25 account rows",
    final="Row set of the register", vals="F9 F11 F16 F24 F25 F34 `25`; exact (Intuit merged into QuickBooks; iPostal, Lucidchart, Google Ads, Pond5, AWS, the UA ad accounts and the two $30 game-ops lines off; ElevenLabs on)",
    kind="multi-source — the count only follows from all 28 issues, the costs-tab Sound line and four exclusion records", band=5,
    dec="T6 T8 T11 T12 T17 T19", distractor="T6, T8, T11, T17, T19 → exact count rejects the all-inclusive list", oes=[7, 15, 18, 20, 22, 23, 25],
    dup="volume row for G1–G4", cr="A run that lists excluded accounts in a separate 'left off' block has more than 25 lines", res="brief §4b W1 row set: 'excluded accounts listed separately are fine' — the count is of register rows (OE 25 lists the left-off accounts apart)")
add(src=f'"{S_REG}" · OE 8, 25', what="QuickBooks and Intuit carried as one register row (ENG-2450 is the duplicate)",
    final="Register row set", vals="F10 F11 `ENG-2449` `ENG-2450` `QuickBooks`; name QuickBooks, Intuit or Intuit QuickBooks (rule 1; /oe rubric note 1)",
    kind="interpretation — Leonard's ENG-2450 comment 'same account as the quickbooks issue' applied through rule 1", band=3, dec="T12",
    distractor="T12 → one row, not two", oes=[8, 25], cr="Rule 1 says 'the name on its invoice' and no QuickBooks invoice is visible to Robert; forcing 'Intuit QuickBooks' fails a run writing 'QuickBooks'",
    res="/oe report rubric note 1: accept QuickBooks, Intuit or Intuit QuickBooks; the row grades one row, not the label")
# action column (exhaustive)
ACT_W = {"Gusto": 5, "Metabase": 5, "dbt": 5, "BigQuery": 5, "Trello": 5, "GitHub": 5, "ElevenLabs": 5, "Deel": 1}
ACT_DEC = {"Gusto": "C3 T1", "Metabase": "H1 T4", "dbt": "H1 T5", "BigQuery": "H1 T5", "Trello": "H1 T5 T17", "GitHub": "H1",
           "ElevenLabs": "C1 T6 T7", "Slack": "H1", "Google Workspace": "H1", "Linear": "H1", "Figma": "H1", "Cursor": "T21",
           "Helpshift": "T15", "QuickBooks": "T12", "Carta": "T16", "Unity": "T25"}
ACT_KIND = {
 "Gusto": "multi-source — the keep list plus Arthur's reply in its thread (C0ADGSZKR3R/1770948876.205117) plus rule 4",
 "Metabase": "multi-source — first checklist holds it, Sunset's Feb 13 correction drops it, Arthur's card move decides Move",
 "dbt": "multi-source — Arthur's card move vs Sunset's correction; rule 4 makes Sunset win",
 "BigQuery": "multi-source — only Sunset's in-thread correction puts it on the hold list",
 "Trello": "multi-source — free plan since Nov 2025, but Sunset's correction holds it",
 "GitHub": "multi-source — Arthur's KubLLC move vs Sunset's first list; rule 4 makes Sunset win",
 "ElevenLabs": "multi-source — no issue; the costs-tab Sound line plus the receipt, added under rule 3",
 "Deel": "lookup — named on Leonard's keep list (C0ADGSZKR3R/1770933601.686309)",
}
for a in ACC:
    n, iss, act = a[0], a[1], a[2]
    w = ACT_W.get(n, 3)
    kind = ACT_KIND.get(n, "interpretation — not on the keep list, Sunset's list or the card moves, so rule 4's default" if act == "Cancel"
                        else "interpretation — Sunset's checklist through rule 4" if act.startswith("Hold") else "interpretation — keep list through rule 4")
    facts = {"Hold for Sunset": "F12 F13", "Keep": "F2", "Move to Arthur's LLC": "F4 F13", "Cancel": "F2 F12 F13"}[act]
    extra = " F3" if n == "Gusto" else (" F16 F24" if n == "ElevenLabs" else "")
    add(src=f'"{S_REG}" · OE 2, 3, 9, 25', what=f"{n} register row — action {act}", final=f"{n} row, action column",
        vals=f"F7 {facts}{extra} `{n}` `{act}`; the four rule-4 words or clear synonyms (brief §4b W1 action)",
        kind=kind, band=w, dec=ACT_DEC.get(n, "—"), oes=[2, 3, 9, 25], group="— (action column graded exhaustively)",
        distractor={"Gusto": "T1 → Cancel, not Keep", "Metabase": "T4 → Move, not Hold", "dbt": "T5 → Hold, not Move/Cancel",
                    "BigQuery": "T5 → Hold, not Cancel", "Trello": "T5/T17 → Hold, not Cancel/left off", "GitHub": "card move → Hold wins (rule 4)",
                    "Cursor": "T21 Oliver's request → still Cancel", "ElevenLabs": "T7 → own row"}.get(n, "—"),
        dup="register deliverable; the comment on its issue is a separate deliverable (gate 6)",
        cr={"Gusto": "Leonard's keep list (F2) names Gusto, so Keep is defensible",
            "Metabase": "Sunset's first email holds Metabase, so Hold is defensible",
            "dbt": "Arthur moved dbt to his KubLLC card, so Move is defensible",
            "GitHub": "Arthur moved GitHub to his KubLLC card, so Move is defensible",
            "Trello": "Trello is on the free plan, so it could be left off as never charging",
            "ElevenLabs": "ElevenLabs has no Linear issue, so leaving it off follows Arthur's list",
            "Cursor": "Oliver asked to keep Cursor, so Keep is defensible"}.get(n, f"A run could read {n} as {'Cancel' if act != 'Cancel' else 'Keep'} from a list it saw first"),
        res={"Gusto": "Arthur's thread reply C0ADGSZKR3R/1770948876.205117 'let's cancel before mar 3' amends the keep list; rule 4 'as amended in the thread' (f_1326e66bcabfda8fd29e4a)",
             "Metabase": "Sunset's correction robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com> 'Metabase isn't' governs; card move C0ADGSZKR3R/1770937232.664809",
             "dbt": "rule 4 'Sunset's list wins over everything above' (f_1326e66bcabfda8fd29e4a) + correction adds dbt",
             "GitHub": "rule 4 'Sunset's list wins over everything above' (f_1326e66bcabfda8fd29e4a); GitHub on the first list",
             "Trello": "rule 2 exception 'anything on Sunset's list goes on the register whatever else applies' (f_1326e66bcabfda8fd29e4a)",
             "ElevenLabs": "rule 3 'add what it misses inside any other costs-tab line that covers several vendors' + Sound line f_605121f4a36752645e0ac3",
             "Cursor": "Arthur's reply C09UHHN6PFZ/1770991653.518204 'it's already gone'; a request is not a decision (rule 10)"}.get(n, f"OE 25 row {n}: {act}; rule 4 (f_1326e66bcabfda8fd29e4a) and {a[8]}"))
# status column (Cancel rows, exhaustive)
ST_W = {"Unity": 5, "Cursor": 5, "CodeRabbit": 5}
ST_DEC = {"Unity": "C5 T13", "Cursor": "C5 T13", "CodeRabbit": "C5 T13", "Layer": "C5", "Singular": "T22", "Carta": "T16"}
for a in ACC:
    n, iss, act, st = a[0], a[1], a[2], a[3]
    if act != "Cancel":
        continue
    w = ST_W.get(n, 3)
    src_f = {"Unity": "F38", "Cursor": "F37", "CodeRabbit": "F29", "Soundly": "F21", "Layer": "F19 F27", "Singular": "F23", "ElevenLabs": "F24"}.get(n, "")
    add(src=f'"{S_REG}" · OE 8, 13, 14, 19, 21, 24, 25', what=f"{n} register row — status {st}", final=f"{n} row, status column",
        vals=f"F7 F10 {src_f} `{n}` `{st}`".replace("  ", " ") + "; Closed/Requested/Open or clear synonyms (brief §4b W1 status)",
        kind=("multi-source — the Linear comment says only that a founder cancelled; the vendor's confirmation sits in another service" if w == 5
              else "interpretation — one record read against rule 5's three definitions"), band=w, dec=ST_DEC.get(n, "—"), oes=[8, 13, 14, 19, 21, 24, 25],
        group="— (status column graded exhaustively over the 14 Cancel rows)", distractor="T13 → Closed, not Requested" if w == 5 else ("Leonard's #prototype note C09UHHN6PFZ/1770837702.167889 → Requested stands" if n == "Layer" else "—"),
        dup="register deliverable; Done state on the issue is a separate deliverable",
        cr={"Unity": "ENG-2438's comment only says the termination was sent, so Requested is defensible",
            "Cursor": "ENG-2460's comment only says 'cancelled in the dashboard'",
            "CodeRabbit": "ENG-2459's comment only says 'cancelled'",
            "Layer": "Leonard's #prototype note says access runs to March 3rd, which reads like a confirmation",
            "Singular": "Singular's Jan 15 reply extended a due date, which reads like an answer",
            "Carta": "Leonard says 'the carta terminations this week', which reads like Requested"}.get(n, f"{n}'s record could be read one status lower or higher"),
        res={"Unity": "Arthur's #executives note C07C2866011/1771017520.226917 'it's confirmed' is the vendor's confirmation relayed; rule 5 (f_1326e66bcabfda8fd29e4a)",
             "Cursor": "C09UHHN6PFZ/1770991653.518204 'cursor sent the confirmation'; rule 5",
             "CodeRabbit": "bot notice harmonygames-Games/Combo-Fighters#38 is 'an in-app or bot notice' (rule 5)",
             "Layer": "C09UHHN6PFZ/1770837702.167889 is Leonard's own note, not Layer's (/oe report rubric note 2); receipt robert@harmonygames.co/1856114791547562583",
             "Singular": "the Mar 15 extension answers the past-due balance, not the termination; Leonard's Feb 12 termination is the last message (robert@harmonygames.co/1853470745017478863)",
             "Carta": "cmt on ENG-2451: 'the subscription itself is untouched' → Open (rule 5)"}.get(n, f"OE 25: {n} {st}; {a[8]}"))
# by-when: direct exceptions + 5 samples (G1)
BW_DIRECT = ["Carta", "Google Workspace", "Slack", "QuickBooks", "Singular"]
BW_SAMPLE = ["Docusign", "Gusto", "ElevenLabs", "Figma", "GitHub"]
for n in BW_DIRECT + BW_SAMPLE:
    a = A[n]
    d = a[4]
    sample = n in BW_SAMPLE
    add(src=f'"{S_REG}" · OE 10, 11, 12, 25', what=f"{n} register row — by when {d}", final=f"{n} row, by-when column",
        vals=f"F14 F36 {'F15 ' if 'Mar' in d else ''}{'F10 ' if n in ('Carta','QuickBooks','Google Workspace','Slack') else ''}{'F23 ' if n=='Singular' else ''}{'F24 ' if n=='ElevenLabs' else ''}{'F18 ' if n=='Figma' else ''}`{n}` `{d}`; any date format",
        kind="multi-source — rule 6 over the SVB card's comments (not its description), the next charge and the review call", band=5,
        dec={"Carta": "C4 H2", "Google Workspace": "C4 H2", "Slack": "C4 H2", "QuickBooks": "C4 H2", "Singular": "C4 T22", "Docusign": "C4 T26",
             "Gusto": "C4 T1", "ElevenLabs": "C4 T26", "Figma": "T14", "GitHub": "T14"}[n],
        oes=[10, 11, 12, 25], group="G1 sample" if sample else "G1 direct exception",
        distractor={"Singular": "T22 Mar 14 / Feb 28 → Feb 17", "Docusign": "T26 Apr 19 → Feb 17", "Figma": "T14 no date / Feb 15 → Mar 12",
                    "GitHub": "T14 → Mar 12", "Carta": "Feb 17 for every Cancel → Carta keeps Aug 14"}.get(n, "T9 description dates (Feb 19) → Feb 17"),
        dup="register deliverable; the comment on its issue is separate",
        cr={"Carta": "Leonard says Carta 'stays as I said' without a date; the renewal date itself (Aug 15) could be written",
            "Figma": "Figma charges the card in September, so Hold could be 'until Sunset confirms' with no date",
            "GitHub": "GitHub is moved to the KubLLC card, so a dash (Moved row) is defensible",
            "Singular": "Singular's past-due extension runs to Mar 15, so Mar 14 is defensible"}.get(n, f"The card description's Feb 19 could be applied to {n}"),
        res={"Carta": "rule 6 'the day before the next charge' + cmt 'renews aug 15' → Aug 14; SVB comment 'Only exception is carta' (Trello 698f48be4ba0affafbf153db comments)",
             "Figma": "rule 6: Hold rows that won't charge the card before the call stay until the review call evt_f1d245d44ceff5a6e049c0 (Mar 12)",
             "GitHub": "GitHub's action is Hold (rule 4), so rule 6's Hold clause applies: off the SVB card → review call evt_f1d245d44ceff5a6e049c0",
             "Singular": "Mar 15 is the past-due extension (robert@harmonygames.co/1853470745017478863); next invoice Mar 1, but the SVB comment's Feb 17 is earlier"}.get(n,
             "the SVB card's comments (Trello 698f48be4ba0affafbf153db, 22:47Z) supersede the description: off the card / cancelled by end of day Feb 17"))
# owner: direct 2 + samples 3 (G2)
for n, direct in [("Docusign", True), ("ElevenLabs", True), ("Unity", False), ("Singular", False), ("Figma", False)]:
    a = A[n]
    add(src=f'"{S_REG}" · OE 7, 8, 25', what=f"{n} register row — owner {a[5]}", final=f"{n} row, owner column",
        vals=f"F7 {'F10' if n=='Docusign' else ('F16 F24' if n=='ElevenLabs' else 'F9')} `{n}` `{a[5]}`; first or full name",
        kind=("interpretation — rule 7: the issue hands Docusign to Robert" if n == "Docusign" else
              "interpretation — rule 7: 'Anything you add is yours'" if n == "ElevenLabs" else "lookup — the Linear assignee (rule 7)"),
        band=3 if direct else 1, dec="T18" if n == "Docusign" else ("C1" if n == "ElevenLabs" else "—"), oes=[7, 8, 25],
        group="G2 direct exception" if direct else "G2 sample", distractor="T18 → Robert, not the assignee Leonard" if n == "Docusign" else "—",
        cr="Leonard is ENG-2457's assignee" if n == "Docusign" else ("ElevenLabs has no issue, so no assignee to copy" if n == "ElevenLabs" else f"{n}'s issue creator is Arthur, not the assignee"),
        res="cmt_bbdca23f075e9fca5cb8 'docusign goes to robert from here'; rule 7 'unless the issue hands it to someone else'" if n == "Docusign"
        else ("rule 7 'Anything you add is yours' (f_1326e66bcabfda8fd29e4a)" if n == "ElevenLabs" else f"rule 7 'the Linear assignee'; {a[1]} assignee {a[5]} (SQL linear_issues {a[1]})"))
# cost: 5 samples (G3)
CK = {"Singular": ("F10 F23", 5, "calculation — quarterly $6,250.00 (past-due thread robert@harmonygames.co/1853470745017478863 + ENG-2444 'next quarterly invoice is mar 1') / 3 (rule 8), after mapping the $6,250 costs-tab line to Singular", "T16"),
      "Linear": ("F10", 3, "calculation — the owner's annual $1,832.65 / 12 (rule 8)", "T16"),
      "Figma": ("F18", 3, "calculation — receipt $1,212.00 annual / 12 (rule 8)", "T16"),
      "ElevenLabs": ("F24", 3, "calculation — receipt $50.00 annual / 12 (rule 8)", "C1"),
      "Unity": ("F10", 3, "interpretation — rule 8 takes the owner's figure in the issue over the costs tab", "C7 T25")}
for n, (f, w, kind, dec) in CK.items():
    a = A[n]
    add(src=f'"{S_REG}" · OE 8, 16, 20, 21, 25', what=f"{n} register row — monthly cost {a[6]}", final=f"{n} row, monthly cost column",
        vals=f"F7 {f} `{n}` `{a[6]}`; to the cent (± 0.01), with or without $", kind=kind, band=w, dec=dec, oes=[8, 16, 20, 21, 25], group="G3 sample",
        distractor={"Singular": "T16 6,250 / 0 → 2,083.33", "Linear": "T16 annual price → 152.72", "Figma": "T16 0 / 1,212 → 101.00",
                    "Unity": "T25 costs-tab 2,172 → 2,348.50", "ElevenLabs": "T7 one Sound row → own cost"}[n],
        cr={"Singular": "The $6,250.00 is a past-due balance, not a recurring charge, so it isn't the monthly cost",
            "Linear": "The P&L stops after the 2024 payment, so 0 is defensible",
            "Figma": "Figma won't charge again before Sep 2026, so 0 a month today",
            "ElevenLabs": "$50 a year rounds to 4.17 or 4.16",
            "Unity": "The costs tab shows 2,172 for Unity"}[n],
        res={"Singular": "ENG-2444 'the next quarterly invoice is mar 1' makes $6,250.00 the quarterly charge and the project says 'the $6,250 one is Singular' (costs-tab line), so 6,250 / 3 = 2,083.33; invoice amounts are PDF-only and not relied on (/oe r7 Issue 1)",
             "Linear": "cmt_37c23c5d30cc6597ebe9 'we paid $1,832.65 last august for the year'; rule 8 annual / 12 = 152.72",
             "Figma": "rule 8 'last invoice … brought to a month (annual / 12)'; robert@harmonygames.co/1842984194671106077",
             "ElevenLabs": "50 / 12 = 4.1667 → 4.17 rounded to cents (rule 8); ± 0.01 tolerance accepts 4.16",
             "Unity": "rule 8 'the monthly figure its owner gives in its Linear issue' → cmt_5da8c3467fc022248fb3 $2,348.50"}[n])
# say-where samples (G4)
for n, where, f in [("Unity", "Arthur's #executives note relaying Unity's reply", "F38"), ("Cursor", "Arthur's #prototype reply relaying Cursor's confirmation", "F37"),
                    ("CodeRabbit", "CodeRabbit's bot notice on Combo-Fighters PR 38", "F29")]:
    add(src=f'"{S_REG}" · OE 13, 14, 24, 25', what=f"{n} register row — Closed source named ({where})", final=f"{n} row, status column or a note beside it",
        vals=f"F7 {f} `{n}` `{where}`; any wording naming that source (the vendor's own reply/notice or the founder relay of it — /prompt recommendation 5)",
        kind="interpretation — rule 5 'say where' for a Closed row", band=3, dec="C5", oes=[13, 14, 24, 25], group="G4 sample",
        distractor="T13 → the Linear comment is not the confirmation", cr="Naming 'Unity's account manager' instead of Arthur's note is the same source",
        res="rule 5 asks where the vendor confirmed; the row accepts the vendor reply or the relay that carries it (ledger risk 7; /oe report OE 13–14)")
# totals in sheet
add(src=f'"{S_REG}" · OE 26, 28', what="Register total over every row — 6,706.49 a month", final="Register (anywhere in the sheet)",
    vals="F7 F10 F18 F23 F24 `6,706.49`; to the cent (± 0.01)", kind="calculation — rule 9 over 25 costs gathered from comments, receipts and invoices", band=5,
    dec="C7 T16 T25", oes=[26, 28], dup="register deliverable; the reply carries the same total as a told fact (gate 6: one row each)",
    cr="A run that keeps Intuit as a second row adds 115 and gets 6,821.49", res="rule 1 one row per vendor (cmt_5fb637b0247b82594b16); OE 26 total 6,706.49 recomputed from OE 25's 25 costs")
add(src=f'"{S_REG}" · OE 26, 28', what="Register total over the Keep and Hold rows — 1,249.04 a month", final="Register (anywhere in the sheet)",
    vals="F7 F10 F13 F18 F26 `1,249.04`; to the cent (± 0.01)", kind="calculation — rule 9 over the 10 Keep and Hold rows, which depend on the Sunset correction", band=5,
    dec="H1 T4 T5", oes=[26, 28], dup="register deliverable; the reply's total is a separate row",
    cr="A run that holds Metabase (first checklist) gets 1,397.04", res="Sunset's correction (robert@harmonygames.co/<CAs4-nh82p7LJ_En9FYL8INkdVWOXh5q4-5hxGyj@mail.gmail.com>) drops Metabase; OE 26")
# ---------------- W2 share ----------------
for who, mail in [("Leonard", "leonard.hayes@harmonygames.co"), ("Arthur", "arthur.blake@harmonygames.co")]:
    add(src=f'"{S_SHARE}" · OE 1, {29 if who=="Leonard" else 30}', what=f"Register shared with {who} as an editor", final="Drive permission on the register file",
        vals=f"F1 F30 `{mail}`; editor (writer) role — the ask says 'as editors'", kind="lookup — recipient and role from the ask", band=1, dec="—",
        oes=[1, 29 if who == "Leonard" else 30], cr=f"The prompt says only 'share it with him and arthur'; commenter access could be read as sharing",
        res="Leonard's ask C0ADGSZKR3R/1771003267.448213 'share it with me and Arthur as editors' is the incorporated instruction (brief §4b W2)")
add(src=f'"{S_SHARE}" · OE 29, 30', what="Register share guard — exactly two people added (Leonard and Arthur)", final="Permission list of the register file",
    vals="F1 F30 `2`; exact count of grantees other than Robert", kind="lookup — two named recipients", band=1, dec="—", oes=[29, 30],
    cr="Sharing with Oliver or the whole domain would still give Leonard and Arthur access", res="rubric_flow_v2 scope checklist: a row that fails writes to extra targets; the ask names two people (C0ADGSZKR3R/1771003267.448213)")
# ---------------- W3 Linear states ----------------
DONE = ["Unity", "Helpshift", "Soundly", "CodeRabbit", "Cursor", "Zapier", "Kapwing"]
OE_STATE = {"Unity": 31, "Helpshift": 33, "Soundly": 35, "CodeRabbit": 56, "Cursor": 58, "Zapier": 60, "Kapwing": 63,
            "Intuit": 45, "iPostal": 50, "Lucidchart": 66, "Google Ads": 68}
for n in DONE:
    a = A[n]
    w = 5 if n in ("Unity", "Cursor", "CodeRabbit") else 3
    add(src=f'"{S_SETTLE}" · OE 6, {OE_STATE[n]}', what=f"{a[1]} {n} set to Done", final=f"Linear issue {a[1]} state",
        vals=f"F8 F10 {a[7].split()[-1]} `{a[1]}` `Done`; exact state", kind=("multi-source — Closed needs the vendor confirmation found outside Linear" if w == 5 else
                                                                          "interpretation — the comment or email confirms closure; the project's settle rule gives Done"),
        band=w, dec="C5 T13" if w == 5 else "—", oes=[6, OE_STATE[n]], dup="Linear deliverable (state) — separate from its comment and its register row",
        distractor="T13 → Done, not left open" if w == 5 else "—",
        cr=f"Access to {n} runs on after the confirmation, so leaving it open until access ends is defensible",
        res="project description 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a: 'Done once the account counts as closed in the register (access can run out later)'")
for e in EXCL:
    n, iss, f, why = e
    add(src=f'"{S_SETTLE}" · OE 6, {OE_STATE[n]}', what=f"{iss} {n} set to Canceled", final=f"Linear issue {iss} state",
        vals=f"F8 {f} `{iss}` `Canceled`; exact state (team ENG has no Duplicate state)",
        kind="interpretation — " + ("rule 1 duplicate" if n == "Intuit" else "a pre-Feb-9 cancellation notice read against rule 2"), band=3,
        dec="T12" if n == "Intuit" else ("T19" if n == "iPostal" else "T17"), oes=[6, OE_STATE[n]], dup="Linear deliverable (state)",
        distractor={"Intuit": "T12 → ENG-2450 (newer) cancelled, not ENG-2449", "iPostal": "T19 Dec-25 tab figure → still Canceled"}.get(n, "—"),
        cr=f"{n} could stay open as 'nothing to do' rather than Canceled", res=f"project rule 'Canceled if it doesn't belong on the list'; {why}")
add(src=f'"{S_SETTLE}" · OE 6, 31–69', what="Linear state guard — exactly 17 of the project's 28 issues left in an open state (not Done or Canceled)",
    final="States of the 28 project issues", vals="F8 F9 `17` `28`; any open state (Todo, In Progress) — brief §4b W3",
    kind="multi-source — the count only follows from settling every issue against the register", band=5, dec="T13 T17", oes=[6, 7] + list(range(31, 70)),
    dup="guard for the state write kind (scope checklist)", cr="Moving the Hold rows to In Progress is a valid open state",
    res="brief §4b W3 'any open state (Todo, In Progress) for the rest'; the guard counts not-Done/not-Canceled, so In Progress passes")
# ---------------- W3 comments ----------------
CM = {  # issue name -> (content noun phrase, value literals, weight, oe)
 "Unity": ("cancelled and confirmed closed, nothing left to do by a date", "`Cancel` `Closed`", 5, 32),
 "Helpshift": ("cancelled and confirmed closed, nothing left to do by a date", "`Cancel` `Closed`", 3, 34),
 "Soundly": ("cancelled and confirmed closed, nothing left to do by a date", "`Cancel` `Closed`", 3, 36),
 "Linear": ("held for Sunset until the Mar 12, 2026 review call", "`Hold for Sunset` `Mar 12, 2026`", 5, 37),
 "Figma": ("held for Sunset until the Mar 12, 2026 review call", "`Hold for Sunset` `Mar 12, 2026`", 5, 38),
 "Trello": ("held for Sunset until the Mar 12, 2026 review call", "`Hold for Sunset` `Mar 12, 2026`", 5, 39),
 "Singular": ("being cancelled by Feb 17, 2026", "`Cancel` `Feb 17, 2026`", 5, 40),
 "Metabase": ("moving to Arthur's LLC (KubLLC) card, nothing left to do by a date", "`Move to Arthur's LLC`", 5, 41),
 "dbt": ("held for Sunset until the Mar 12, 2026 review call", "`Hold for Sunset` `Mar 12, 2026`", 5, 42),
 "BigQuery": ("held for Sunset until the Mar 12, 2026 review call", "`Hold for Sunset` `Mar 12, 2026`", 5, 43),
 "QuickBooks": ("kept, off the SVB card by Feb 17, 2026", "`Keep` `Feb 17, 2026`", 5, 44),
 "Carta": ("being cancelled by Aug 14, 2026", "`Cancel` `Aug 14, 2026`", 5, 47),
 "Google Workspace": ("held for Sunset, off the SVB card by Feb 17, 2026", "`Hold for Sunset` `Feb 17, 2026`", 5, 48),
 "Slack": ("held for Sunset, off the SVB card by Feb 17, 2026", "`Hold for Sunset` `Feb 17, 2026`", 5, 49),
 "Gusto": ("being cancelled by Feb 17, 2026", "`Cancel` `Feb 17, 2026`", 5, 52),
 "Deel": ("kept, nothing left to do by a date", "`Keep`", 1, 53),
 "Docusign": ("being cancelled by Feb 17, 2026", "`Cancel` `Feb 17, 2026`", 5, 54),
 "Layer": ("being cancelled by Feb 17, 2026", "`Cancel` `Feb 17, 2026`", 5, 55),
 "CodeRabbit": ("cancelled and confirmed closed, nothing left to do by a date", "`Cancel` `Closed`", 5, 57),
 "Cursor": ("cancelled and confirmed closed, nothing left to do by a date", "`Cancel` `Closed`", 5, 59),
 "Zapier": ("cancelled and confirmed closed, nothing left to do by a date", "`Cancel` `Closed`", 3, 61),
 "GitHub": ("held for Sunset until the Mar 12, 2026 review call", "`Hold for Sunset` `Mar 12, 2026`", 5, 62),
 "Kapwing": ("cancelled and confirmed closed, nothing left to do by a date", "`Cancel` `Closed`", 3, 64),
 "1Password": ("being cancelled by Feb 17, 2026", "`Cancel` `Feb 17, 2026`", 5, 65),
 "Intuit": ("a duplicate of ENG-2449 QuickBooks, which carries the register row", "`ENG-2449`", 3, 46),
 "iPostal": ("off the register: cancelled before Feb 9 (mailbox closed Jan 16, 2026)", "`Jan 16, 2026`", 3, 51),
 "Lucidchart": ("off the register: cancelled before Feb 9 (canceled Oct 10, 2025)", "`Oct 10, 2025`", 3, 67),
 "Google Ads": ("off the register: cancelled before Feb 9 (canceled Oct 16, 2025)", "`Oct 16, 2025`", 3, 69),
}
ORDER = ["Unity", "Helpshift", "Soundly", "Linear", "Figma", "Trello", "Singular", "Metabase", "dbt", "BigQuery", "QuickBooks", "Intuit", "Carta",
         "Google Workspace", "Slack", "iPostal", "Gusto", "Deel", "Docusign", "Layer", "CodeRabbit", "Cursor", "Zapier", "GitHub", "Kapwing",
         "1Password", "Lucidchart", "Google Ads"]
for n in ORDER:
    content, lits, w, oe = CM[n]
    iss = A[n][1] if n in A else E[n][1]
    facts = A[n][7] if n in A else E[n][2]
    extra = " F14 F36" if "Feb 17" in content or "Aug 14" in content else (" F15" if "Mar 12" in content else "")
    add(src=f'"{S_SETTLE}" · OE 6, {oe}', what=f"Comment on {iss} {n} — {content}", final=f"New comment on Linear issue {iss}",
        vals=f"F8 {facts}{extra} `{iss}` {lits}; any wording carrying what happens and by when (brief §4b W3 comment)",
        kind=("lookup — Deel is on the keep list with no card to move" if w == 1 else
              "interpretation — one rule applied to the issue's own record" if w == 3 else
              "multi-source — the action and date need Sunset's correction, the SVB card comments or a vendor record outside Linear"),
        band=w, dec={"Unity": "C5", "Cursor": "C5", "CodeRabbit": "C5", "Singular": "C4 T22", "Gusto": "C3 C4", "Docusign": "C4 T26",
                     "Layer": "C4", "1Password": "C4", "Carta": "C4", "QuickBooks": "C4 H2", "Google Workspace": "C4 H2", "Slack": "C4 H2",
                     "Metabase": "H1 T4", "dbt": "H1 T5", "BigQuery": "H1 T5", "Trello": "H1 T5", "Linear": "T14", "Figma": "T14", "GitHub": "T14"}.get(n, "—"),
        oes=[6, oe], dup="Linear deliverable (comment) — the same action/date also sits in the register; graded once per deliverable (gate 6)",
        cr=(f"'What happens and by when' are two claims; a comment with the right action and a wrong date could be split into two rows" if "by Feb" in content or "Aug 14" in content or "Mar 12" in content
            else f"A comment that just says 'see the register' carries no action"),
        res=("the project rule asks for one statement per issue, 'what happens and by when' (3f0c6a52-ee13-4b1e-68e3-a74bcc33818a); a deadline-qualified action is one instruction (coherent_record A1: one requested finding, its qualifier) — see Self-review atomicity note"
             if "by Feb" in content or "Aug 14" in content or "Mar 12" in content else
             f"the row names the content ({content}); a pointer-only comment fails it — project description 3f0c6a52-ee13-4b1e-68e3-a74bcc33818a"))
add(src=f'"{S_SETTLE}" · OE 31–69', what="Comment volume — a new comment on each of the 28 project issues (exactly 28 issues commented)",
    final="Comments on the project's issues", vals="F8 F9 `28`; exact count of project issues with a new comment", kind="lookup — the project lists 28 issues",
    band=1, dec="—", oes=[7] + list(range(31, 70)), dup="volume / scope guard for the comment write kind",
    cr="Two comments on one issue still count once", res="the row counts issues commented, not comments; 28 issues ENG-2438–ENG-2466 without ENG-2445 (OE 7)")
# ---------------- W5 reply ----------------
add(src=f'"{S_REPLY}" · OE 1, 70', what="Reply posted in the thread of Leonard's Feb 13 ask in #winddown", final="Slack thread reply under C0ADGSZKR3R/1771003267.448213",
    vals="F1 `C0ADGSZKR3R` `1771003267.448213`; thread reply (the prompt says 'in his thread')", kind="lookup — the prompt names the thread", band=1, dec="—", oes=[1, 70],
    prompt_title='"in his thread" — the thread is specified', cr="A top-level #winddown message mentioning Leonard is also a reply", res='the prompt says "reply to him in his thread"; a top-level post is a different location (brief §4b W5)')
add(src=f'"{S_REPLY}" · OE 26, 70', what="Reply — monthly total over every row 6,706.49", final="Thread reply text", vals="F7 F10 F23 F24 `6,706.49`; to the cent (± 0.01)",
    kind="calculation — rule 9 over the whole register", band=5, dec="C7 T16 T25", oes=[26, 70], dup="reply deliverable (told fact) — the sheet's total is a separate row",
    cr="Leonard may read 'what it all costs us today' as the costs-tab total", res="rule 9 defines the first total as the register's monthly cost column (f_1326e66bcabfda8fd29e4a)")
add(src=f'"{S_REPLY}" · OE 26, 70', what="Reply — monthly total over the Keep and Hold rows 1,249.04", final="Thread reply text", vals="F7 F10 F13 F26 `1,249.04`; to the cent (± 0.01)",
    kind="calculation — rule 9 over the Keep and Hold rows", band=5, dec="H1 T4 T5", oes=[26, 70], dup="reply deliverable (told fact)",
    cr="Counting the Move row (Metabase) as kept gives 1,397.04", res="rule 9 'the same sum over the Keep and Hold rows only'; Metabase is Move (Sunset correction)")
add(src=f'"{S_CLASH}" · OE 4, 9, 70', what="Reply — Slack clash: the #winddown decision to take Slack to the free plan / down to a few members with the rest as guests, against Sunset's hold on Slack's paid plan with every user",
    final="Thread reply text", vals="F5 F12 `free version` `guest accounts`; either decision named (free plan or guest accounts) — one Slack clash (ledger F35)",
    kind="multi-source — Feb 11 messages, a checklist table inside an attachment and Sunset's email under rule 10", band=5, dec="C6 T2", oes=[4, 9, 70],
    distractor="card moves, Gusto, Cursor are not clashes (rule 10) — not graded", ambig="risk 2 → the row does not cap the clash count",
    cr="The free plan and the guest conversion are two decisions, so a run naming only guests may fail a free-plan-only title",
    res="the row accepts either Slack decision (a complete closed set of the two #winddown Slack decisions, C0ADGSZKR3R/1770840054.486779 and C0ADGSZKR3R/1770842405.931359); /oe G3 counts them as one clash")
add(src=f'"{S_CLASH}" · OE 3, 9, 70', what="Reply — Google clash: archiving the Google accounts after Feb 15, against Sunset's 'don't archive or delete any' until the review call",
    final="Thread reply text", vals="F6 F12 `after Feb 15`; any wording (archiving the Google accounts)", kind="multi-source — Leonard's action item vs Sunset's checklist under rule 10", band=5,
    dec="C6 T3", oes=[3, 9, 70], ambig="risk 2 → the row does not cap the clash count", cr="The prompt itself mentions the Google archive, so naming it is a giveaway, not a finding",
    res="the prompt mentions the archive as context; the clash needs Sunset's 'please don't archive or delete any' (robert@harmonygames.co/<CAJJpzSHRqB32RlDrDy2t2WCVuJkOmMr2sKoQuBV@mail.gmail.com>) — rule 10")

for i, r in enumerate(rows, 1):
    r["P"] = f"P{i}"
import re as _re
GENERIC = {"cancel","keep","open","closed","requested","done","canceled","hold for sunset","move to arthur's llc","arthur","leonard","robert"}
NAMES = {a[0]: a[1] for a in ACC}
NAMES.update({e[0]: e[1] for e in EXCL})
def tighten(r):
    v = r["vals"]
    keyname = next((n for n in sorted(NAMES, key=len, reverse=True) if _re.search(r"(?<![A-Za-z])" + _re.escape(n) + r"(?![A-Za-z])", r["what"])), None)
    def rep(m):
        t = m.group(1)
        if t.casefold() in GENERIC or (t in NAMES and t != "ElevenLabs"):
            return t
        return m.group(0)
    v = _re.sub(r"`([^`]+)`", rep, v)
    if keyname and NAMES.get(keyname) and f"`{NAMES[keyname]}`" not in v:
        v = v.replace(";", f" `{NAMES[keyname]}`;", 1) if ";" in v else v + f" `{NAMES[keyname]}`"
    if not _re.search(r"`[^`]+`", v):
        raise SystemExit("no literal left: " + r["P"] + " " + v)
    r["vals"] = v
for r in rows:
    tighten(r)

# ---------------- render ----------------
def cell(s):
    return str(s).replace("|", "/").replace("\n", " ")


L = []
L.append("# 09 Rubric Writing Plan — Robert account close-out register (rb-winddown-closeout)")
L.append("Generated 2026-10-29 · Clock 2026-02-14T00:00:00Z · Persona Robert robert@harmonygames.co · Tier Long-Horizon · Human time 19.75 h · "
         "OE status: PROVISIONAL — /oe r6 (6adfee3f27ce6ca81b457137_2_oe (5).md) NON-FAIL 3 on two Minor items; both fixed in OE revision 24 "
         "(08_Oracle_Events.md sha256 0421c195), /oe re-run pending; 08_OE_Check.md Blocking 0")
L.append("Canonical outcome: brief §4b (one acceptance class per deliverable) — W1 one sheet in Robert's Drive (title any; a Doc table passes), 25 rows "
         "(account, action, status on Cancel rows, by when, owner, monthly cost) + totals 6,706.49 and 1,249.04; W2 Leonard and Arthur as editors; "
         "W3 Done ENG-2438/2439/2440/2459/2460/2461/2463, Canceled ENG-2450/2454/2465/2466, the other 17 open, a comment on all 28; "
         "W5 a reply in the thread C0ADGSZKR3R/1771003267.448213 with both totals and the two clashes. Correction to brief §4b W5: it says "
         "'exactly the three clashes'; the ledger (F35) and the OEs that /oe verified have two (Slack free plan / guests as one clash, Google archive), "
         "and this plan follows the ledger.")
L.append("")
L.append("Row shape follows /rubric's scope checklist (rubric_flow_v2.md) and the Douglas /rubric round-1 findings: one row per write target "
         "(11 state changes, 28 comments), one row per told fact, the register's action and status columns graded exhaustively, and ≤ 5 spot checks "
         "plus the volume row P2 on the by-when, owner, cost and say-where columns.")
L.append("")
L.append("## A · Coverage matrix")
L.append("| P | Source (prompt span · OE n) | What must be verified (noun phrase) | Final state that proves it (artifact / message / record / final response) | Category (Outcome / Process candidate → C) | Values the criterion must name (F-IDs + backticked literals; exact / tolerance) |")
L.append("|---|---|---|---|---|---|")
for r in rows:
    L.append(f"| {r['P']} | {cell(r['src'])} | {cell(r['what'])} | {cell(r['final'])} | {r['cat']} | {cell(r['vals'])} |")
L.append("")
L.append("## A2 · Grading risks and weight")
L.append("| P | Title/phrasing specified by prompt? | Distractor? (T-ID → grade handling) | Ambiguous evidence? (risk # → no single conclusion) | Kind of work (lookup / interpretation · calculation · comparison / multi-source · tracing) + reason | Band 1/3/5 | Decided by (chain / authority / trap id) | Spot-check group | Duplicate risk (per deliverable) / overlap group | Predicted all-fail basis (four Evals bases) · over-specific risk |")
L.append("|---|---|---|---|---|---|---|---|---|---|")
for r in rows:
    L.append(f"| {r['P']} | {cell(r['prompt_title'])} | {cell(r['distractor'])} | {cell(r['ambig'])} | {cell(r['kind'])} | {r['band']} | {cell(r['dec'])} | {cell(r['group'])} | {cell(r['dup'])} | {cell(r['allfail'])} |")
L.append("")
# B · OE trace
L.append("## B · OE trace")
L.append("| OE | Kind (write / discovery / friction) | Proved by row(s) | Own row? (reason) |")
L.append("|---|---|---|---|")
writes = set([27, 28, 29, 30] + list(range(31, 71)))
for oe in range(1, 71):
    ps = [r["P"] for r in rows if oe in r["oes"]]
    kind = "write" if oe in writes else ("discovery (calculation)" if oe in (25, 26) else "discovery")
    if oe in writes:
        own = "yes — a write target gets its own result row (scope checklist)"
    elif oe in (25, 26):
        own = "no — the calculation is proved by the register cells and totals it produces"
    else:
        own = "no — discovery; proved by the content row(s) that carry its result"
    show = ", ".join(ps) if len(ps) <= 14 else ", ".join(ps[:12]) + f" … ({len(ps)} rows)"
    L.append(f"| OE {oe} | {kind} | {show or '—'} | {own} |")
L.append("")
L.append("## C · Process candidates — three-condition test")
L.append("| P | Requirement (prompt span) | Why no Outcome can prove it | (1) every valid path | (2) no stricter Outcome | (3) behavioural, not trace | Result (Process / tighten P-n with F-n) |")
L.append("|---|---|---|---|---|---|---|")
L.append('| C1 | "and then reply to him in his thread" (reply after the register and the Linear settling) | the final state shows the reply and the writes, not their order | yes — every valid path ends with the reply | yes — no Outcome shows order | fails — the order of independent writes is an execution trace; the reply\'s content (P112–P116) already depends on the finished register, so nothing behavioural is lost | not Process; P113–P116 carry the dependency |')
L.append('| C2 | "share it with him and arthur" after the register is built | sharing an empty sheet then filling it ends in the same state | yes | yes | fails — the end state (shared sheet with 25 rows) is identical either way; an ordering row would grade a trace | not Process; P1–P2 and P68–P70 grade the end state |')
L.append("")
L.append("## D · Spot-check groups")
L.append("| G | Item set (F-IDs, total N; keys as backticked literals) | Sampled items (≤ 5) and why hard/edge | Volume row | Exact-set row (`none — bundle (Rubric Writing §7; Eval 2.2)`) | Core requirement? (must be no) |")
L.append("|---|---|---|---|---|---|")
P = {r["what"]: r["P"] for r in rows}
def pid(prefix):
    return [r["P"] for r in rows if r["what"].startswith(prefix)]
g1 = [r["P"] for r in rows if "by when" in r["what"]]
g2 = [r["P"] for r in rows if "— owner" in r["what"]]
g3 = [r["P"] for r in rows if "monthly cost" in r["what"]]
g4 = [r["P"] for r in rows if "Closed source" in r["what"]]
dated = [a for a in ACC if a[4] != "—"]
L.append(f"| G1 by-when column | F14 F36 F15, 16 dated rows of 25: " + " ".join(f"`{a[1]}`" if a[1] else "`ElevenLabs`" for a in dated) +
         f" | samples {', '.join(g1[5:])} — Docusign (T26 Apr 19 → Feb 17), Gusto (keep-list amendment), ElevenLabs (added row, Jul 9 renewal), Figma (Hold off the card → Mar 12), GitHub (moved card + Hold → Mar 12; ordinary Hold). Direct exceptions, not sampled: {', '.join(g1[:5])} (Carta's Aug 14 exemption; Keep/Hold rows still on the SVB card; Singular's extension trap) | P2 | none — bundle (Rubric Writing §7; Eval 2.2) | no — dates are repetitive cells of one column; the exceptions are graded directly |")
L.append(f"| G2 owner column | F9 F10, 25 rows: " + " ".join(f"`{a[1]}`" if a[1] else "`ElevenLabs`" for a in ACC) +
         f" | samples {', '.join(g2[2:])} — Unity (Arthur), Singular (Leonard), Figma (Robert): one ordinary per assignee. Direct exceptions: {', '.join(g2[:2])} (Docusign handed to Robert; ElevenLabs added → Robert) | P2 | none — bundle (Rubric Writing §7; Eval 2.2) | no |")
L.append(f"| G3 monthly cost column | F10 F18 F23 F24, 25 rows (keys as G2) | samples {', '.join(g3)} — Singular (quarterly / 3), Linear (annual / 12 from the comment), Figma (annual / 12 from a receipt, no comment), ElevenLabs (rounding 4.17), Unity (owner figure over the stale costs tab) | P2 (totals P66, P67 reconcile the column) | none — bundle (Rubric Writing §7; Eval 2.2) | no |")
L.append(f"| G4 Closed rows' source (rule 5 'say where') | F29 F37 F38 F21 F10, 7 Closed rows: `ENG-2438` `ENG-2439` `ENG-2440` `ENG-2459` `ENG-2460` `ENG-2461` `ENG-2463` | samples {', '.join(g4)} — the three confirmations that sit outside Linear and Gmail (#executives, #prototype thread, GitHub bot) | P2 (status rows grade each Closed value directly) | none — bundle (Rubric Writing §7; Eval 2.2) | no — the source note is a repetitive annotation; the Closed status itself is graded on every row |")
L.append("")
# ---------------- E summary ----------------
from collections import Counter
bands = Counter(r["band"] for r in rows)
tot = sum(r["band"] for r in rows)
nO = sum(1 for r in rows if r["cat"] == "Outcome")
L.append("## E · Summary")
L.append(f"Rows {len(rows)} · Outcome {nO} · Process candidates 2 (C1, C2 — both fail condition 3, none kept) — ≥ 1 Outcome ☑ (no Process ratio: QC Spec V2 and the Evals override fail only zero Outcome) · builder minimum 5 ☑ · one volume row per sampled output, no bundled exact-set row ☑ (P2 for G1–G4; P82 guards the state write kind; P111 the comment write kind; P70 the share write kind) · predicted all-fail rows = 0 ☑ (harness tolerance 0; /rubric fails at ≥ 2; every value is persona-reachable, see Visibility proof and Self-review)")
L.append("Failure diversity: largest unit of discovery 71% of the weight (≤ 50% ☒ — the Linear project 'Shutdown – accounts' (F8) and its issue and comment listings (F9, F10) sit upstream of every per-account row, because every account is a Linear issue: the cohort spine, named in Leonard's ask, not a hidden discovery; same structural finding as the accepted Douglas and Frederick tasks — Self-review, diversity row) · chains landing on distinct rows ☑ (C1 rule-3 addition → ElevenLabs rows; C3 Gusto thread → Gusto action/by-when/comment; C4 SVB comments → by-when rows and dated comments; C5 vendor confirmations → Unity/Cursor/CodeRabbit status, Done and comment rows; C6 clashes → P115, P116; C7 owner figures → Unity cost, totals; H1 Sunset correction → Metabase/dbt/BigQuery/Trello rows and the Keep+Hold total)")
L.append(f"Bands: 5 ×{bands[5]} · 3 ×{bands[3]} · 1 ×{bands[1]} (total weight {tot})")
L.append(f"Set size: {len(rows)} rows for 19.75 h (reference: 31 criteria for a ~10-hour task). The size comes from /rubric's scope checklist, not from duplicate grading: 39 Linear writes get a row each (11 states, 28 comments) plus their two guards; the register's action (25) and status (14) columns are graded exhaustively; four columns are sampled (≤ 5 each). No fact is graded twice inside one deliverable; a register value repeated in its issue comment or in the reply is a second prompt-required deliverable (gate 6).")
L.append("Coverage: requirements 8/8 (R1–R8 of the ledger) · OEs 70/70 · writes 7/7 write kinds (sheet create + values, 2 shares, 11 states, 28 comments, 1 reply) · told facts 4/4 (two totals, two clashes) · friction 0/0 (Friction: none)")
L.append("Four prohibitions: ☑ unstated expectations (no row for formatting, column order, the sheet title, the Helpshift export or new Linear issues) ☑ conclusions on ambiguous evidence (clash rows accept any wording and do not cap the count — ledger risk 2; the Slack clash accepts either Slack decision) ☑ grading the distractor (traps graded by their handling: P2 count, Gusto Cancel, Metabase Move, Closed statuses) ☑ hard-coded titles/phrasings (sheet title and comment wording delegated; QuickBooks name variants accepted)")
L.append("Blocking: none for validity — no UGT defect, no infeasible write, no unverified visibility. diversity.authority_share fails structurally (above) and is recorded as Unresolved for the human to accept, as on the Douglas task.")
L.append("")
L.append("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)")
L.append("")
L.append("`python3 Task_Authoring-2/tools/persona_view.py check-sql robert Task_Authoring-2/task_inputs/01_Universe_Inject.sql --load-bearing lb.txt` (lb.txt = every scoped id behind the F-ids this plan cites; the NO rows the full output also prints are Leonard's and Arthur's own mailbox copies of the Sunset emails, which no row uses — Robert's copies are the YES LB rows):")
L.append("")
L.append("```")
L.extend((HERE / "vis.txt").read_text().rstrip("\n").splitlines())
L.append("```")
L.append("")
L.append("Unscoped facts need no proof: Linear (F8–F11, F30), Trello (F14, F36), GitHub (F29) — `Evals/references/persona/acl.md`.")
L.append("")
# ---------------- F shortcut probe ----------------
L.append("## F · Shortcut probe")
probe = (HERE / "probe.txt").read_text().rstrip("\n") if (HERE / "probe.txt").exists() else ""
L.append("```")
L.extend(probe.splitlines())
L.append("```")
disp = (HERE / "disp.txt").read_text().rstrip("\n") if (HERE / "disp.txt").exists() else ""
if disp:
    L.extend(disp.splitlines())
L.append("")
# ---------------- Self-review ----------------
L.append("## Self-review")
L.append("")
L.append("Re-read as /rubric: `Evals/3_Rubrics_Eval.md` 1.4 and 3.1, the hg-strict-overrides-v1 table, `references/rules/rubric_flow_v2.md` scope checklist, `rubric_sampling.md` and `coherent_record.md`, walked against §A in order.")
L.append("")
L.append("Re-verified values (this run, not from the ledger): `grep -c` on `Task_Authoring-2/task_inputs/01_Universe_Inject.sql` for every comment literal (2,348.50 L159; $148, $100, 4.97, $115, $3,852 / aug 15, 298.13, 87.22, $116 L219, $300, 'docusign goes to robert', 'cancelled it in the app on the 11th', '3 seats at $15', $40/mo, 73.50, $90, $24, 19.95, 1,832.65, 'same account as the quickbooks issue', $150 L165; 'close the card on the 18th', 'Only exception is carta', 'Trello is part of the bundle too', 'don''t archive or delete any', 'stay on the paid plan', 'cursor sent the confirmation', 'it''s confirmed, the pro seats stop', 'was canceled on Feb 12, 2026', 'Soundly Pro (monthly, $10.00)', 1,212.00, 'Layer Pro (monthly) — $49.00', 'ended on September 8, 2025', 'as editors') — every one found; `python3 Task_Authoring-2/tools/hg.py search search gmail` for the base notices: 'will expire on Nov 4, 2025' → threads/00015599.json (robert@harmonygames.co/1845611902985063512), 'was canceled on 10/16/25' → threads/00015671.json (robert@harmonygames.co/1846207913731182209), 'Your Mailbox Has Been Cancelled' → threads/00016395.json, INVSINC23580 → threads/00016086.json (robert@harmonygames.co/1850283027022457279); ElevenLabs receipt threads/00014566.json (robert@harmonygames.co/1837122624854744558): 'Jul 9, 2025 – Jul 9, 2026 Starter Qty 1 $50'. Linear states: base `linear/data.json` team_ENG uses Done and Canceled (no Duplicate state). Totals recomputed from the 25 costs: 6,706.49 and 1,249.04.")
L.append("")
L.append("| Check | Verdict | Strongest counter-reading | Resolution (evidence: pointer / rule § / case id) | Unresolved |")
L.append("|---|---|---|---|---|")
for r in rows:
    L.append(f"| {r['P']} {cell(r['what'][:70])} | PASS | {cell(r['cr'])} | {cell(r['res'])} | none |")
GEN = [
 ("Coverage (Eval 1.4, 3.1)", "PASS", "Counter: a run that never shares, never replies or skips the Canceled issues still passes many rows",
  "each write kind has its own rows: P1 sheet, P68–P70 shares, P71–P82 states, P83–P111 comments, P112–P116 reply (rubric_flow_v2 scope checklist)"),
 ("Atomicity of the dated comment rows", "PASS (risk noted)", "Counter: 'cancelled by Feb 17, 2026' is two claims (action, date) — /rubric could call it non_atomic (Major)",
  "the project rule asks for one statement, 'what happens and by when' (3f0c6a52-ee13-4b1e-68e3-a74bcc33818a); the date qualifies the action (coherent_record A1: one requested finding with its qualifier; Douglas R44–R52 'still has to go out to prod' passed /rubric). If /rubric disagrees, the fix is a split, not a reweight"),
 ("Predicted all-fail re-check", "PASS — 0 rows", "Counter: risk 3 — 6 of 6 earlier baselines missed CodeRabbit's GitHub notice, so P37/P65/P74/P103 could fail every run",
  "missing a reachable record is a valid all-fail, not one of the four bases: harmonygames-Games/Combo-Fighters#38 is unscoped and the notice names the cancellation (F29); none of target_data_absent / required_tool_absent / filter_impossible / entity_unreachable applies"),
 ("Negative criteria", "PASS", "Counter: P70 'exactly two people' and P82 'exactly 17 left open' read like absence checks",
  "both are affirmative counts of a preserved state (rubric_flow_v2 scope checklist 'an exact count or scope row usually covers this'); no title uses not/never/without"),
 ("Clash count", "PASS", "Counter: without an exact-two row an all-inclusive clash list passes",
  "/oe report rubric note 3 says not to fail a run that also names the Helpshift draft or ORG_NAME_0304 (C0ADGSZKR3R #winddown /21, /190); ledger risk 2 — no single conclusion on ambiguous evidence"),
 ("Weights by work kind", "PASS", "Counter: Holds at Mar 12 are routine and could be 3, not 5",
  "each needs the calendar event evt_f1d245d44ceff5a6e049c0, Sunset's correction and rule 6's card clause — three sources (QC Spec V2 Criteria Weights 5 = multi-source)"),
 ("Shortcut probe and diversity", "see §F / Summary", "Counter: the Linear project lists every account, so one listing answers most rows",
  "the listing gives names and assignees only; actions, statuses, dates and costs need the comments, Sunset's thread, the SVB card comments and the receipts (F10, F13, F36, F18–F24). diversity.authority_share stays a structural finding (Unresolved)"),
 ("Re-verified", "PASS", "Counter: ledger values could be stale after the rev-21 injection rewrite",
  "re-read this run with grep on 01_Universe_Inject.sql and hg.py (paragraph above); OE 21's corrected Singular invoices match threads/00015167.json and 00016086.json"),
]
for c, v, cr, res in GEN:
    L.append(f"| {c} | {v} | {cr} | {res} | {'diversity.authority_share' if 'diversity' in c else 'none'} |")
L.append("")
L.append("Unresolved: (1) diversity.authority_share — the Linear project chain decides ~71% of the weight by construction (every account is an issue); a design finding for the human to accept, not a value or visibility gap. (2) OE status PROVISIONAL until /oe passes revision 25; re-run prep's header and re-gate after the PASS.")
OUT.write_text("\n".join(L) + "\n")
import json
json.dump(rows, open(HERE / "rows.json", "w"), indent=0)
print(len(rows), "rows; weight", sum(r["band"] for r in rows))
