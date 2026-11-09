#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Writing_Brief.md (brief mode) from the SQL ids, the solver truth, the persona searches
(plan/brief_searches.json/.txt) and the entity output (plan/brief_entity.txt). Facts and locators only; no rubric or OE text."""
import importlib.util, json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
S = json.load(open(os.path.join(HERE, "sql_ids.json")))
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
spec = importlib.util.spec_from_file_location("solver_mod", os.path.join(WF, "solver", "solver.py"))
SOLV = importlib.util.module_from_spec(spec)
sys.path.insert(0, os.path.join(TI, "..", "tools"))
spec.loader.exec_module(SOLV)
AGG = SOLV.aggregates(TRUTH)
SUM = AGG["summary"]
SRCH = json.load(open(os.path.join(HERE, "brief_searches.json")))
MB, ROB, ART = "leonard.hayes@harmonygames.co", "robert@harmonygames.co", "arthur.blake@harmonygames.co"
GM = {k: v["message"] for k, v in S["gmail"].items()}
GT = {k: v["thread"] for k, v in S["gmail"].items()}
P, NOTES, OLD, SHEET, DECK, FOLDER = "ec2ea957-fc8e-4958-b809-0fb735b1e916 (team_ENG)", "f_a37b403d5200d4f0a31d31", "f_762c60832854d3e7a7f7df", "f_5ecaa967db3adcfa440b09", "f_75dddccabb26eeea4842c8", "d_601064334a0b493022fe83"
CARD, EVT, FAM, ORIGIN, LIST, DRAFT = "698e5a10c3f24b7e9d16a0e4", "evt_6f1a2c9e4b7d3a58c0e1d2", "C0ADGSZKR3R/1770949310.220519", "C0ADGSZKR3R/1770938120.410229", "C0ADGSZKR3R/1770934638.035469", "C0ADGSZKR3R/1770664700.848759"
PROMISE, SEG, TOR, CLAIRE, LETTERS, CARTA = "D04UC0UEN2V/1770665186.368229", "D04UC0UEN2V/1770664988.379119", "D09R59580EM/1762285888.654689", "C51ECE5102ED/1770903714.600249", "C0ADGSZKR3R/1770841239.761999", "C0ADGSZKR3R/1770935621.095649"
OWNER = f"{MB}/1816809274978043917"
ADVT, TERM, CHARTER, SIDE, SPA, TASKLIST = "f_6a37227593d0977fdbdd7a", "f_11040fe5d66821bd6951aa", "f_90c029015fc474199cf736", "f_6201c7027d02997bfb2c84", "f_966445655f653d26dc8537", "f_31115ddb6ed866f2b10d60"
BOARDTH, MATTTH, SIGNTH, ES14TH, LETTERTH, VINCTH, FAMTH, FREDTH = (f"{MB}/1856958794180374704", f"{MB}/1830959847543474636", f"{MB}/1777052222643175480", f"{MB}/1856960478782792748",
                                                                  f"{MB}/1856861400116562076", f"{MB}/1849344928983425627", f"{MB}/1770141224265557526", f"{MB}/1847335165884050330")


def rd(n):
    p = os.path.join(HERE, n)
    return open(p).read().rstrip() if os.path.exists(p) else f"({n} missing)"


L = []
A = L.append


def table(head, rows):
    A("| " + " | ".join(head) + " |")
    A("|" + "---|" * len(head))
    for r in rows:
        A("| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in r) + " |")
    A("")


A("# Prompt Brief — leonard_stockholder_closeout · prep")
A("> Built 2026-11-08 from 00_Assigments.md, Working_Files/00_Task_Context.json, Working_Files/01_Grounding_Dossier.md (injection rev1, SQL sha256 6f3b18994e1a; the platform /injection PASS "
  "plateform_reports/6aed9d01a1cb8067d8ac7dee_0_injection.md reviewed the earlier sha256 bc72db9c31e9, so /injection re-runs with /prompt), 01_Universe_Inject.sql, "
  "01_Scenario_Design.md, 01_Hardness_Manifest.json, solver/truth.json · no 03_Error_Async_Config.txt (Friction: none by default), no 02_Reference_Files_Manifest.md (no attachment) "
  "· Persona view verified: all (check-sql PASS on every seeded load-bearing record; base records by persona_view search, §5a) · Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) · "
  "Leonard's today: Saturday Feb 14, 2026.")
A("> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human.")
A("")
A("## 1 · Assignment fit")
A("")
table(["Axis", "Assigned value", "What it requires here (cited)"], [
 ["Business function", "Executive", "Founders / Exec / Strategy in `Evals/references/rules/task_categories.md`: a founder closes out the company's stockholders, the board and the auditor after the Feb 11, 2026 shutdown (C0ADGSZKR3R/1770934638.035469)."],
 ["Persona", f"Leonard Hayes · {MB} · Co-founder & Creative Director (roster.json persona_key leonard_hayes, Executive)",
  f"Voice: plain and direct to his assistant, short sentences (C0ADGSZKR3R/1770934638.035469 'next things for me are'). Remit: he promised to reach every angel himself ({PROMISE}), runs the Carta terminations ({CARTA}) and answers KPMG every year ({MB}/1817557789846606177). "
  "Read scope: his mailbox and calendar, his Drive, #winddown C0ADGSZKR3R, his DMs (D04UC0UEN2V, D09R59580EM, D04UGG61DUM) and group DM C51ECE5102ED; Linear and Trello unscoped."],
 ["Competency", "Finance", f"Cap table and equity reconciliation: stock by line apart from advisor options, options outstanding at the clock and at KPMG's date, holders' last days, the auditor's confirmation ({GM['kpmg']}). Expected outputs: a holder schedule, a confirmation reply, investor communications."],
 ["Task skill", "Authoring", f"Authored artifacts: the holder sheet, 14 personal messages, the investor letter (from {DRAFT}), the KPMG reply and the Griffin heads-up."],
 ["Task type", "long-horizon (Long Horizon; difficulty mode medium, V3 cap < 85 %; requester target < 70 %, 130+ counted calls)",
  f"Services carrying weight: Linear (26 issues, 52 notes, 26 state moves, 12 reason comments; {P}), Gmail (14 Carta notices, six letters, owner list, KPMG, Sunset, side letter chain, resignations, 14 drafts, 2 replies), Slack (#winddown, three DMs, a group DM), Drive/Docs/Sheets/Slides (notes, advisor table, term sheet, charter, side letter, the sheet and letter), Trello, GCal, Contacts. hardness_gate (extreme): PASS in the dossier."],
])
A("## 2 · Situation")
A("")
table(["Symptom", "Seen by", "Where it shows (locator)", "Relevant records the persona cannot see"], [
 [f"Leonard promised to reach out to each investor himself, and his Feb 12 list in #winddown still shows the angels as open.", "Leonard", f"{PROMISE}; {LIST}", "none needed"],
 [f"He has set up one Linear issue per holder on Carta and written close-out notes on how each holder gets handled.", "Leonard", f"{P}; {NOTES}", "—"],
 [f"KPMG asked on Feb 13 for Griffin's FY25 confirmation, and Sunset's legal asked for a stockholder sheet for the intake.", "Leonard", f"{GM['kpmg']}; {GM['sunset']}", "—"],
 [f"The investor email he drafted on Feb 9 predates the signing, the resignations and the Carta entries.", "Leonard", f"{DRAFT}", "—"],
])
A("## 3 · Investigation → action")
A("")
A("Questions to resolve (no answers here):")
for q in ["Who holds what today, line by line, and how much of each merged owner-list line is stock?",
          "Which option lines are live at the clock, and what is each one's last day?",
          "Who has already had a written message about the closing, sent to them directly and delivered?",
          "What is each holder owed under the notes, and whose last day comes first?",
          "Which lines does one family member speak for?",
                   "Who is on the board now, and who holds the preferred vote?",
          "What did the company have outstanding at KPMG's date, using effective dates?",
          "Did any holder ask something about their holding that was never answered?"]:
    A(f"- {q}")
A("")
A("Writes those answers feed: the holder sheet, the personal messages as drafts, the Linear states and reason comments, the letter, the KPMG reply, the Griffin heads-up and the #winddown reply. Every write depends on the investigation.")
A("")
A("## 4 · Pinned final state (UGT anchor)")
A("")
table(["Deliverable", "Required contents", "Destination", "Recipients", "Catalog write", "Fed by"], [
 ["Holder sheet (Google Sheet)", "one row per project issue (ENG-2438 to ENG-2463) with holder, stock, options, last day, told, label; totals of shares and options; count by label; directors and the preferred vote",
  f"close-out folder {FOLDER}", f"shared with {ROB} and {ART}", "gsheets create + values update; gdrive move + share", "every §3 question"],
 ["Personal messages (14 Gmail drafts)", "the closing where not told, the last day where there is one, what they hold, an answer to an open question", f"Leonard's drafts ({MB})", "the 14 holders owed one; one to Enes for the family's three lines", "gmail create draft", "told, owed, family, ask"],
 ["Linear issues", "state per the project description; a reason comment on every issue with no note of its own", f"project {P}", "—", "linear update issue ×26; linear create comment ×12", "owed"],
 ["Investor letter (Google Doc)", f"the #winddown draft {DRAFT} brought up to date", f"close-out folder {FOLDER}", f"shared with {ROB}", "gdocs create; gdrive move + share", "board, Sunset, options"],
 ["KPMG reply", "shares by class with each fund's holding; each option line and the total at Dec 31, 2025; shares plus those options; later events", f"reply to all on {GT['kpmg']}", "PERSON_3088_EMAIL, cc PERSON_4416_EMAIL, PERSON_2322_EMAIL, PERSON_2847_EMAIL", "gmail reply to message", "as-of figures"],
 ["Griffin heads-up", "a request for Griffin's vote as preferred holders on the dissolution", f"reply to all on the partner's own Feb 12 mail in {BOARDTH}", "PERSON_4337_EMAIL, cc PERSON_2847_EMAIL", "gmail reply to message", "board, vote"],
 ["#winddown reply", "who goes first", f"thread under {LIST}", "the founders in #winddown", "slack send message (thread)", "last days"],
])
A("Alternatives a careful run could defend, and how each is settled: editing the draft sheet in the folder instead of a new sheet (accepted: same folder, contents and sharing); the KPMG reply or the Griffin heads-up left as drafts (settled: the project says 'Send KPMG's confirmation as a reply to all', the notes say the heads-up 'can go out once the sheet is done'); "
  "three messages for the family (settled by the reply under the list, " + FAM + "); the letter sent by mail (settled: H1 'a letter I can send', in the folder); a new top-level #winddown post instead of a thread reply (settled: 'reply under my list').")
A("")
A("### 4b · Canonical outcome (all fair outcomes)")
A("")
table(["Deliverable", "Field", "Fixed value (or closed accepted set, with sources)", "Delegated by (quoted span, or —)", "Allowed equivalence class", "Material / representational"], [
 ["Holder sheet", "rows", "26 rows keyed by ENG-2438 to ENG-2463; the founders only in the totals; counts by rows", f"'One row per issue on the sheet, and the counts go by rows' ({NOTES})", "extra summary rows; any column order", "material"],
 ["Holder sheet", "label per row", f"Nothing 6, Already told 4, Closing 6, Covered 2, Last day 6, Closing and last day 2 (solver/truth.json)", f"'Labels for the sheet' ({NOTES}); 'Mark those lines Covered' ({FAM})", "First note = Closing; Date note = Last day; Full note = Closing and last day", "material"],
 ["Holder sheet", "stock lines", "Griffin II 2,662,255; Side Fund 84,438; Segerstrale and TOR 50,865; eight lines 25,432", f"Sunset's list ({GM['sunset']})", "with or without separators", "material"],
 ["Holder sheet", "options", "advisor grants 61,038, 30,518, 6,104, 6,104; live vested lines per Carta", f"'(for options, what's vested)' ({GM['sunset']})", "in an options column or beside the stock", "material"],
 ["Holder sheet", "totals", f"Series Seed {SUM['Series Seed total']:,}; common {SUM['Common']:,}; options now {SUM['Options outstanding now']:,}", f"'Total shares and options outstanding' ({GM['sunset']})", "shares issued 9,051,879 may also appear", "material"],
 ["Holder sheet", "board", "directors in office Leonard Hayes and Robert; preferred vote Griffin, 90.0 %", f"'Directors in office, and who holds the preferred vote' ({GM['sunset']}); 'That leaves Leonard and me on the board' ({GM['board_leo']})", "Griffin's two funds named together", "material"],
 ["Holder sheet", "destination and sharing", f"in {FOLDER}; shared with {ROB} and {ART}", f"'everything goes in the close-out folder' and 'Share it ... with Robert' ({NOTES}); 'the sheet goes to you as well as Robert' ({FAM})", "reader or writer role", "representational (role)"],
 ["Messages", "set", "14 drafts: Closing to Schaeppi, Bergmann, Enes (for three lines), TOR, Deepak; Last day to ES-1, ES-4, ES-7, ES-13, ES-15; Closing and last day to ES-3, ES-12, ES-14 and ES-18 (Collins was told on Feb 12 as Akin)", f"'as Gmail drafts' and the handling rules ({NOTES})", "any order", "material"],
 ["Messages", "content", "each states what they hold; Claire's answers her open equity question; Enes's covers the three lines and says what each holds", f"'Each note says what they hold'; 'Anything they asked ... gets answered' ({NOTES}); {FAM}", "any wording", "material"],
 ["Messages", "address", "the email on the holder's issue description (ENG-2438 to ENG-2463)", f"'Messages go to the email on each holder's issue' ({NOTES})", "—", "material"],
 ["Linear", "states", f"Canceled 5, Todo 14, Done 7", f"project description ({P})", "—", "material"],
 ["Linear", "reason comments", "12, one on each issue with no note of its own, Canceled included", f"'On every issue with no note of its own, Canceled included, say why' ({P})", "any wording", "material"],
 ["Letter", "contents", "the draft brought up to date: the closing, Sunset running it, no distribution expected, tax papers, IP and code, the board, options", f"'take my draft from #winddown and bring it up to date' ({NOTES})", "any wording; the outline's sections in any order", "material"],
 ["KPMG reply", "figures", f"options at Dec 31, 2025 {SUM['Options outstanding at Dec 31']:,}; shares plus options {SUM['Issued plus options at Dec 31']:,}; Griffin II 2,662,255 and Side Fund 84,438; the closing as a later event", f"items 1-4 ({GM['kpmg']}) and the follow-up ({GM['kpmg_follow']})", "per-line table in any order", "material"],
 ["KPMG reply", "delivery", f"sent, reply to all on {GT['kpmg']}", f"'Send KPMG's confirmation as a reply to all' ({P})", "—", "material"],
 ["Griffin heads-up", "delivery", f"sent, reply on {BOARDTH}", f"'That one can go out once the sheet is done' ({NOTES})", "—", "material"],
 ["#winddown reply", "who goes first", "ES-3 (Calvin Price), last day Feb 20, 2026 by Carta's Jan 23 update; then ES-14 (Vincent Parker), Feb 21", f"'reply under my list in #winddown and say who goes first' ({NOTES})", "name, token or issue key", "material"],
 ["All", "dates", f"Pacific or UTC (clock line in {MB}'s view)", "—", "Feb 21 or 2026-02-21", "representational"],
])
A("## 5 · Discovery map")
A("")
DISC = [
 ("F1", "holder project", "26 issues, description with states and asks", P, "YES (unscoped)", "—", "low", "Yes: anchor AN2"),
 ("F2", "investor email draft", "Leonard's Feb 9 draft", DRAFT, "YES", "—", "low", "Yes: anchor AN1"),
 ("F3", "KPMG request", "as of Dec 31, 2025, effective dates as Carta shows them", GM["kpmg"], "YES", "FY24 request (as of Sep 30, 2024)", "medium", "Yes: anchor AN3"),
 ("F4", "close-out notes", "the closed rule and the asks", NOTES, "YES (owner)", f"earlier notes {OLD}", "low", "Yes: the persona's own doc"),
 ("F5", "earlier notes", "one mail to everyone", OLD, "YES (owner)", f"replaced by {NOTES}", "low", "No"),
 ("F6", "Sunset's ask", "what the intake needs", GM["sunset"], "YES", "—", "low", "No"),
 ("F7", "family rule", "one note covers the family's lines", FAM, "YES (#winddown member)", f"H1 'at most one note per person' ({NOTES})", "high (thread reply)", "No: never in the prompt"),
 ("F8", "Robert's reply", "Nebojsa told on Feb 12", GM["robert_leo"], "YES (cc)", f"the Feb 12 list {LIST}", "high", "No: never in the prompt"),
 ("F9", "Carta notices", "14 lines, effective dates and last days", ES14TH, "YES", "term sheet 268,772", "medium", "No"),
 ("F10", "Feb 11 letters", "six letters, no last day", LETTERTH, "YES", f"'All termination letters are sent' {LETTERS}", "high", "No: never in the prompt"),
 ("F11", "letters done claim", "a founder's done line", LETTERS, "YES", "the six letters", "medium", "No"),
 ("F12", "Carta done claim", "terminations entered", CARTA, "YES", "no last day sent", "medium", "No"),
 ("F13", "Feb 12 list", "angels open", LIST, "YES", f"{SEG}; {GM['robert_leo']}", "low", "No"),
 ("F14", "Segerstrale told", "Feb 9 DM", SEG, "YES (DM)", f"{LIST}", "high", "No: never in the prompt"),
 ("F15", "Tor DM", "runway warning, not the closing", TOR, "YES (DM)", "—", "medium", "No"),
 ("F16", "owner list", "merged lines", OWNER, "YES", f"advisor table {ADVT}", "medium", "No"),
 ("F17", "advisor table", "103,764 in four grants", ADVT, "YES (share)", "—", "high", "No: never in the prompt"),
 ("F18", "term sheet", "3,051,879 and 268,772", TERM, "YES (share)", "Carta notices", "medium", "No"),
 ("F19", "signed side letter chain", "Segerstrale added as a party", SIGNTH, "YES", f"Drive copy {SIDE}", "high", "No: never in the prompt"),
 ("F20", "side letter Drive copy", "Tor only", SIDE, "YES (share)", f"{SIGNTH}", "medium", "No"),
 ("F21", "Collins resigns", "May 1, 2025", MATTTH, "YES", f"financing documents {SPA}", "medium", "No: never in the prompt"),
 ("F22", "Griffin's director resigns", "Feb 12, 2026", BOARDTH, "YES", f"{SPA}", "low", "No"),
 ("F23", "charter", "protective provision: a vote of the preferred", CHARTER, "YES (share)", "—", "medium", "No"),
 ("F24", "Claire's question", "equity question unanswered", CLAIRE, "YES (group DM member)", "Leonard's replies answer another question", "high", "No: never in the prompt"),
 ("F25", "family addresses", "Enes gives all three", FAMTH, "YES", "the owner list shows no shared surname", "high", "No"),
 ("F26", "ES-14 resignation", "left Nov 21, 2025", VINCTH, "YES", "#company-internal membership", "medium", "No"),
 ("F27", "Trello card", "order of work", CARD, "YES (unscoped)", "—", "low", "No"),
 ("F28", "Tuesday hold", "Feb 17", EVT, "YES (owner)", "—", "low", "No: never in the prompt"),
 ("F29", "Task List row", "send email to investors", TASKLIST, "YES (share)", "—", "low", "No"),
 ("F30", "draft sheet", "copied Nov 2024 figures", SHEET, "YES (owner)", "Carta and the project", "low", "No"),
 ("F31", "outline deck", "letter sections", DECK, "YES (owner)", "—", "low", "No"),
 ("F32", "close-out folder", "destination", FOLDER, "YES (owner)", "the Wind Down folder", "low", "No"),
 ("F33", "Bergmann contact", "PERSON_0693_EMAIL", "contacts d3c6e5b57e0ee6656a1bdd2c", "YES (unscoped)", "patrick@ mail", "low", "No"),
 ("F34", "ES-17 letter", "34,409 and Jan 22, deferring to Carta", FREDTH, "YES", "Carta 34,439 and Jan 28", "medium", "No"),
 ("F35", "advisor agreement", "Nebojsa's grant", "f_3ee38465decc57e61df6e5", "YES (share)", "—", "medium", "No"),
 ("F36", "board after Feb 12", "Leonard and Robert", GM["board_leo"], "YES (cc)", f"financing documents {SPA}; the Feb 11 notes", "low", "No"),
 ("F37", "seed figure correction", "the Jan 14 modelling runs 2 high", "C07C2866011/1768418331.402719", "YES (#executives member)", "C07C2866011/1768416262.426129", "medium", "No"),
 ("F38", "SSP-10 holder", "Husnu Matthew Collins", f"{MB}/1777100628672295991", "YES", "owner-list token", "low", "No"),
]
table(["Fact", "Value", "Locator", "Persona-readable", "Met first / overturned by", "Search risk", "Name in prompt?"],
      [[f"{d[0]} {d[1]}", d[2], d[3], d[4], d[5], d[6], d[7]] for d in DISC])
A("## 5a · Search-as-persona proof")
A("")
table(["Fact (§5 row)", "Service", "Natural query", "Visible hits", "Hidden by ACL", "First visible hit (id)", "Found?"],
      [[r["fid"], r["service"], r["query"], f"{r['base']} base + {r['seeded']} seeded", r["hidden"], r["first"], r["found"]] for r in SRCH])
A("Outputs (persona_view.py search, verbatim):")
A("")
A("```")
A(rd("brief_searches.txt"))
A("```")
A("")
A("## 6 · Triggers, incorporation and implicit requirements")
A("")
table(["Graded requirement", "Seeded where", "Trigger category the prompt must carry", "Incorporating source (locator · persona-readable · unique · instructions-not-answer)", "Inferable"], [
 ["holder sheet, its rows, labels, totals, board", f"{NOTES}; {GM['sunset']}", "deliverable (the close-out the project and notes lay out)", f"{P} · YES · one project · says what goes where, no figures", "yes"],
 ["messages as drafts", NOTES, "deliverable + constraint (drafts)", f"{NOTES} · YES · one doc · rule text only", "yes"],
 ["Linear states and reason comments", P, "deliverable (the project)", f"{P} · YES · one project · state rule only", "yes"],
 ["the letter", f"{NOTES}; {DRAFT}", "deliverable (the investor email draft)", f"{DRAFT} · YES · one draft · the old text to update", "yes"],
 ["KPMG reply", f"{GM['kpmg']}; {P}", "deliverable (KPMG's request)", f"{GM['kpmg']} · YES · one FY25 request · asks, no figures", "yes"],
 ["Griffin heads-up", NOTES, "scope (the notes' list)", f"{NOTES} · YES · one doc · says where and when", "yes"],
 ["#winddown reply", NOTES, "scope (the notes' list)", f"{NOTES} · YES · one doc · says where", "yes"],
 ["family rule", FAM, "none: a record found by reading the thread the notes name", f"{FAM} · YES · one thread · rule only", "yes"],
])
table(["Anchor", "May be named"], [
 ["AN1", "the investor email draft in #winddown; my investor email draft"],
 ["AN2", "the holder project in Linear; the holder project"],
 ["AN3", "KPMG's audit request for Griffin; KPMG's audit request"],
 ["H1", "my close-out notes; my close-out notes doc"],
])
A("## 7 · Dates and constraints")
A("")
table(["Item", "Absolute date or value", "Source", "Past fact or deadline"], [
 ["Today", "Saturday Feb 14, 2026 (Pacific); clock 2026-02-14 00:00 UTC", f"00_Task_Context.json universe.persona_today; KPMG's Fri Feb 13 mail {GM['kpmg']} is yesterday", "fact"],
 ["KPMG request", "Fri Feb 13, 2026 08:48 PT (16:48 UTC)", GM["kpmg"], "past fact: 'yesterday'"],
 ["KPMG due", "2/27/2026", GM["kpmg"], "deadline (never in the prompt)"],
 ["Notes due", "Tue Feb 17, 2026", f"{NOTES}; {EVT}", "deadline (never in the prompt)"],
 ["KPMG as-of date", "December 31, 2025", GM["kpmg"], "fact"],
 ["First last day", "Feb 21, 2026 (ES-14)", ES14TH, "deadline"],
 ["Investor email draft", "Mon Feb 9, 2026", DRAFT, "past fact"],
])
A("## 8 · Difficulty levers")
A("")
table(["Lever", "Used", "Load-bearing", "Where it lives", "Prompt-side condition"], [
 ["Ambiguity", "yes", "yes", f"the closed rule in {NOTES}; the family rule in {FAM}; who was told across mail and DMs", "the prompt names where to start, never who is told or owed"],
 ["Dynamic change", "yes", "yes", f"{LETTERS} and {LIST} met first; {GM['robert_leo']}, {SEG} and the letters overturn them", "names neither the claim nor the correction"],
 ["Multi-source", "yes", "yes", "Linear, Gmail, Slack, Drive family, Trello, GCal, Contacts", "no source named as an exact artifact beyond the anchors"],
 ["Async", "no", "no", "Friction: none", "—"],
 ["Error recovery", "no", "no", "Friction: none", "—"],
 ["Access control", "no", "no", "every deciding record is Leonard-readable (1.E)", "—"],
])
A("## 9 · Must not appear in the prompt")
A("")
for g, items in [
 ("Tool and server names", "any catalog tool name or parameter (gmail_create_draft, linear_update_issue, slack_send_message, gsheets_create_spreadsheet, gdrive_share_file, ...); MCP server names; 'the X tool'"),
 ("Opaque ids", "ENG-2438 to ENG-2463 as a list, f_/d_ ids, thread ids, channel ids, evt_ ids, the Trello card id"),
 ("Answers and findings", "who is told or owed; the family rule; ES-14 or ES-18 having no letter; advisor options inside the owner list; 103,764; 3,051,879; 164,114; 243,757; 9,295,636; Griffin 90.0 %; the board; Calvin first; Owen's bounced letter; Calvin's Feb 20; Akin; Claire's question; the side letter's second party"),
 ("Hidden records", "Robert's reply, the reply under the Feb 12 list, the Feb 9 DM, the advisor table, the side letter chain, the resignation mails, the charter, KPMG's follow-up"),
 ("Dates", "Tuesday or Feb 17; Feb 27; Feb 21"),
 ("Form", "markdown, numbered steps, per-deliverable content lists, if-chains, a riddle or hint about a trap"),
]:
    A(f"- {g}: {items} (01_Grounding_Dossier.md 'Constraints for the prompt brief'; 01_Scenario_Design.md §11 Must-not).")
A("")
A("## 10 · Entity traps")
A("")
A("```")
A(rd("brief_entity.txt"))
A("```")
A("")
table(["Correct entity (exact)", "Lookalike(s)", "How they differ", "Locator (email or record id)"], [
 ["Martin Walsh (ES-13)", "Martin Lewis", "different person; Martin Walsh holds ES-13", "martin.walsh@harmonygames.co; PERSON_0394_EMAIL"],
 ["Marcus Bennett (ES-7)", "Marcus Lee, Oscar Bennett", "only Marcus Bennett holds an option line", "marcus.bennett@harmonygames.co"],
 ["Owen Baker (ES-12)", "Thomas Baker", "different people", "owen.baker@harmonygames.co"],
 ["Oliver Brooks (ES-18)", "Lauren Brooks", "different people", "oliver.brooks@harmonygames.co"],
 ["Julia Lawson (ES-1)", "Peter Lawson", "different people", "julia.lawson@harmonygames.co"],
 ["Calvin Price (ES-3)", "Nathan Price", "different people", "calvin.price@harmonygames.co"],
 ["Patrick Lewis (ENG-2444)", "Bergmann (patrick@ mail)", "the patrick@ address also carries Bergmann's mail; the contact row gives Bergmann's own address", "PERSON_0693_EMAIL; " + FAMTH],
 ["Griffin Gaming Partners II and its Side Fund", "one merged owner-list line", "two Carta lines", OWNER],
 ["Matthew Collins", "contact card 'Independent Director'", "resigned from the board May 1, 2025", MATTTH],
])
A("## 11 · Pre-submit checklist")
A("")
for b in ["Leonard's voice; one plain request; clean spelling", "names only the three anchors and his own notes", "no tool names, ids, figures, rules or findings (§9)",
          "says the messages stay drafts; nothing else about send vs draft that contradicts the records", "no date beyond 'yesterday' for KPMG", "no numbered steps, no markdown, no if-chain",
          "every deliverable in §4 is reachable from the prompt's triggers (§6)", "persona today Saturday Feb 14, 2026", "20-4,000 words"]:
    A(f"- [ ] {b}")
A("")
A("## 12 · Blockers and routed defects")
A("")
A("- None routed. /injection must re-run on the current SQL (sha256 6f3b18994e1a) together with /prompt; the platform PASS covered sha256 bc72db9c31e9.")
A("- The snapshot advisory in that report (gslides notes, table_json, ordinal; linear_projects.links_json) is kept: the same columns ran in six live LLC baseline runs.")
A("")
A("## 13 · Self-review")
A("")
A(rd("brief_selfreview.md"))
A("")
open(os.path.join(WF, "04_Prompt_Writing_Brief.md"), "w").write("\n".join(L) + "\n")
print("wrote 04_Prompt_Writing_Brief.md", len("\n".join(L)))
