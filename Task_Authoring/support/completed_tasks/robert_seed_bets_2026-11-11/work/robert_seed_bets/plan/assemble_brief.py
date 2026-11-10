#!/usr/bin/env python3
"""Assemble Working_Files/04_Prompt_Writing_Brief.md (brief mode) from solver/truth.json, the SQL, and this run's persona
searches (plan/brief_searches.json/.txt) and entity output (plan/brief_entity.txt). Facts and locators only; no prompt,
OE or rubric text. Stops without writing if a figure disagrees with this run's VERIFY lines, a cause word reaches §1-§4,
or an excluded #winddown ts appears. Re-run after any SQL or truth change, then write_brief_evidence.py, then the gate."""
import hashlib, importlib.util, json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
spec = importlib.util.spec_from_file_location("solver_mod", os.path.join(WF, "solver", "solver.py"))
SOLV = importlib.util.module_from_spec(spec)
spec.loader.exec_module(SOLV)
AGG = SOLV.aggregates(TRUTH)
TOT = AGG["totals"]
SRCH = {r["fid"]: r for r in json.load(open(os.path.join(HERE, "brief_searches.json")))}
RAW = open(os.path.join(HERE, "brief_searches.txt")).read().rstrip()
ENT = open(os.path.join(HERE, "brief_entity.txt")).read().rstrip()
MAN = json.load(open(os.path.join(WF, "01_Hardness_Manifest.json")))
sys.path.insert(0, os.path.join(TI, "..", "tools"))
from base_check import parse_sql  # noqa: E402

SQL_TEXT = open(os.path.join(TI, "01_Universe_Inject.sql")).read()
SQLSHA = hashlib.sha256(SQL_TEXT.encode()).hexdigest()[:12]
STMT = [x for x in parse_sql(SQL_TEXT) if x["op"] == "insert"]
NOTES = sum(x["table"] == "linear.linear_comments" for x in STMT)
PROMPT_WORDS = len(open(os.path.join(HERE, "prompt_candidate.txt")).read().split())
P4 = open(os.path.join(TI, "04_Prompt.txt")).read()
P4SHA = hashlib.sha256(P4.encode()).hexdigest()[:12]
assert P4.split() == open(os.path.join(HERE, "prompt_candidate.txt")).read().split(), "04_Prompt.txt and the candidate differ"
PLAT = "plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md"
ATTEMPT = "6aeed82596dcfe103f9f74d9"
assert os.path.exists(os.path.join(TI, PLAT))
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputsS2", PYTHONDONTWRITEBYTECODE="1")

ROB, LEO, ART = "robert@harmonygames.co", "leonard.hayes@harmonygames.co", "arthur.blake@harmonygames.co"
A, ADM = ROB + "/", "C04UEQVDVB7/"
ASK1, ASK2 = "C0ADGSZKR3R/1770945821.640039", "C0ADGSZKR3R/1770945859.212469"
METHOD, SHEET, DECK = "f_6feda53b2382c63bf47b25", "f_3304033843904a426f3c00", "f_a4b3c4287a4314d8e532e1"
PROJECT = "linear:project/0742c172-85de-47ed-a111-316e5c8cb187"
CARD, EVT, ROOT = "698e55f9af74d68d679de7b3", "evt_f21476dc404329f67fd60d", "d_9f7ba94f7526d54d8482ba"
STATEMENT = "C05URGU759U/1770971846.479179"
ARTHUR_MAIL = A + "<CAOOpSqA2MTKGlKETvkoKqFfq1MaIktcGcH9cj21BJMAMN4Ok00@mail.gmail.com>"
LEO_REPLY = A + "<CAPBs_a5xhlLhxf4uFEerJEygHD5CJ2ob3qegV9nV-erG4foiIU@mail.gmail.com>"
RECEIPTS = [A + x for x in ("1800873055214061794", "1802092844284446043", "1803223458475671884", "1805405368810910191", "1808201559428745555")]
ENDING = {"Deel": "8380", "Leapblock": "1359", "Eveline Art": "8501", "Adjoe": "5000", "MotMot": "3341, 8605", "Singular": "4015", "Node Media": "0115",
          "TYZ Law Group": "7534", "Trademark lawyer": "7393", "Lucas": "6577", "AppLovin": "2532", "Graham Porter": "1794", "JPMorgan": "3203",
          "Creative X": "5660", "JP (website)": "4020", "Nathan Price": "0148", "Martin Walsh": "3801", "Lauren Brooks": "5384", "Ozhan": "3307",
          "UX contractor": "1876", "4X helper": "3139", "Oleg": "9368"}
ISSUE = json.load(open(os.path.join(HERE, "ids.json")))["issues"]
assert set(ISSUE) == set(TRUTH) == set(ENDING)


def gate_current(path, stage):
    """True only if the file's pasted PASS was issued on the SQL now on disk: an older PASS is never claimed."""
    lines = [l for l in open(path, errors="replace") if f"STAGE GATE {stage}: PASS" in l]
    return bool(lines) and f"01_Universe_Inject.sql#{SQLSHA}" in lines[-1]


INJ_OK = gate_current(os.path.join(WF, "01_Grounding_Dossier.md"), "injection")
ERR_OK = gate_current(os.path.join(TI, "03_Error_Async_Config.txt"), "error-async")


def money(v):
    return f"{v:,.2f}"


def check_against_this_run():
    """Every notice sum in truth.json must equal what this run re-derived from Robert's mail."""
    got = {m.group(1): float(m.group(2).replace(",", "")) for m in re.finditer(r"^VERIFY ending (\d{4}): ([\d,.]+) over", RAW, re.M)}
    bad = []
    for k, t in TRUTH.items():
        if k == "Martin Walsh":
            if "VERIFY ending 3801 BGN: 1,999.00" not in RAW:
                bad.append(k)
            continue
        s = sum(got.get(e.strip(), 0) for e in ENDING[k].split(","))
        if abs(s - t["notices_sum"]) > 0.005:
            bad.append(f"{k}: run {s} truth {t['notices_sum']}")
    for need in ("984,888.21", "608,820.50", "73,685.61", "132 Processed payments", "total 7,525.00", "VERIFY census as Robert, 'Thanks for your payment': 0 threads"):
        if need not in RAW:
            bad.append(need)
    if abs(sum(TOT["build"].values()) - 1576461.69) > 0.005:
        bad.append("build total")
    if abs(TOT["marketing_usd"] - 73965.63) > 0.005 or TRUTH["Oleg"]["paid"] != 0:
        bad.append("Marketing total or the ENG-2459 line")
    if sorted(AGG["groups"]["reason_comment"]) != ["JPMorgan", "Leapblock", "Lucas", "MotMot", "Oleg"]:
        bad.append("reason-comment set")
    if bad:
        sys.exit("STOP: truth.json disagrees with this run: " + "; ".join(bad))


check_against_this_run()
L = []
P = L.append


def table(head, rows):
    P("| " + " | ".join(head) + " |")
    P("|" + "---|" * len(head))
    for r in rows:
        P("| " + " | ".join(str(c).replace("|", "/") for c in r) + " |")
    P("")


def bucket_cells(bucket):
    out = []
    for k, t in TRUTH.items():
        if t["Bucket"] != bucket:
            continue
        if k in ("Martin Walsh", "Oleg"):
            continue                   # each has its own §4b row: no dollar figure here
        if bucket == "Company":
            parts = [f"Company {money(t['Company'])}"]
        else:
            parts = [f"{col} {money(t[col])}" for col in ("Domino Delights", "ZM", "Combo Fighter") if t[col]]
        out.append(f"{ISSUE[k]} ***{ENDING[k]} " + (", ".join(parts) or "zero"))
    return "; ".join(out)


h03 = subprocess.run([sys.executable, "-B", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", "Task_Authoring/task_inputsS2/03_Error_Async_Config.txt"],
                     cwd=WS, capture_output=True, text=True, env=ENV).stdout.strip().splitlines()[-1]
budget = sum(r["calls"] for r in MAN["call_budget"])
NOS = [f for f, r in SRCH.items() if r["found"] == "NO"]

P("# Prompt Brief — robert_seed_bets · prep")
INJ = "injection stage PASS on this SQL" if INJ_OK else "the injection gates are being re-run on this SQL, so no upstream PASS is claimed here yet"
ERR = f"with its own gate PASS (digest {h03})" if ERR_OK else f"(digest {h03}); its gate PASS predates this SQL and is being re-run"
HARD = "HARDNESS GATE (extreme): PASS in the dossier." if INJ_OK else "The dossier's HARDNESS GATE PASS predates this SQL and is being re-run."
P(f"> Built 2026-11-08 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Grounding_Dossier.md, 01_Universe_Inject.sql (rev6, sha256 {SQLSHA}; {INJ}), "
  "03_Error_Async_Config.txt, 01_Scenario_Design.md, 01_Hardness_Manifest.json, 01_Gradable_Surface.json, solver/truth.json, plan/unresolved.md, plan/research/sc4_habits.md, plan/research/pw1_prompt_lessons.md and the platform /prompt report " + PLAT + " · "
  f"Persona view verified: every scoped record is readable by Robert (check-sql PASS for seeded rows, search or can-see for base rows). Exceptions: {', '.join(NOS)} are readable but a natural search does not reach them, so each is marked NO and routed (§5a, §12) · "
  "Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal) · Robert's today: Saturday Feb 14, 2026.")
P(f"> 04_Prompt.txt is written ({len(P4.split())} words, sha256 {P4SHA}) and unchanged since the platform /prompt review of rev4 ({PLAT}, attempt {ATTEMPT}); plan/prompt_candidate.txt holds the same words. This brief states requirements and quotes the prompt only where a check needs its words.")
P(f"> The requester skipped the error/async stage. Friction is none, and 03_Error_Async_Config.txt records that {ERR}. There are no reference files: no 02_Reference_Files_Manifest.md exists and 02_Reference_Files/ holds only the template README.")
P("")

# ---------------------------------------------------------------- 1
P("## 1 · Assignment fit")
P("")
table(["Axis", "Assigned value", "What it requires here (cited)"], [
    ["Business function", "Executive", "Maps to Founders / Exec / Strategy in `Evals/references/rules/task_categories.md` (strategic decisions, pitches, executive coordination). The work is a founder's account to investors, and that file says a finance task must fit a real person's responsibilities and creates no CFO persona. Reconciliation alone reads as Finance / Legal / HR / Ops, so the investor framing ('angel calls', 'bet', the draft deck) has to stay in the prompt (pw1_prompt_lessons.md row 3)."],
    ["Persona", f"Robert · {ROB} · Co-founder & Creative Director (roster.json persona_key robert, listed there as Co-Founder & Creative Director, department Executive)",
     f"Voice: short, plain, first person to his assistant. Remit: Leonard hands it to him by name, 'you know what each of these people did better than I do, can you own it?' ({ASK1}), and Robert handled contractor payments with his co-founders ({ADM}1732216147.969439). "
     f"Read scope: his own mailbox and calendar; Drive files he owns or that are shared with him; member of C0ADGSZKR3R (#winddown), C04UEQVDVB7 (#admin_foundersonly), C05URGU759U (#leapblock) and C06MXPL9536; Linear, Trello, Contacts and Snowflake unscoped."],
    ["Competency", "Finance", f"Taxonomy screen 9: focus budget, forecast, cap table, fundraising; expected outputs models, spreadsheets, decks. Here: an account of how the seed money was spent for the angel calls ({EVT}), delivered as a spreadsheet with deck corrections."],
    ["Task skill", "Analysis and synthesis", f"Taxonomy: combine information from multiple sources and compute, model, reconcile or diagnose to reach findings. Exercised by reconciling the bank notices against the method ({METHOD}), the payee notes (ENG-2438 to ENG-2459) and the warehouse, then writing the sheet. Stacked: Actions (22 issue closes, the reply)."],
    ["Task type", "long-horizon (Long Horizon; difficulty mode easy, V3 cap below 90%)",
     f"Measured this run: Gmail 88 threads holding 132 Processed payments; Linear 22 issues and {NOTES} notes, 22 closes and 5 reason comments; Snowflake 2,284 revenue rows; Slack, Docs, Sheets, Slides, Drive, Contacts, Trello and Calendar carry the rest. "
     f"call_budget {budget} (01_Hardness_Manifest.json, requester-confirmed volume and cohort exceptions, floors {MAN['volume_exception']['call_budget_floor']} and {MAN['cohort_exception']['cohort_floor']}). {HARD}"],
])

# ---------------------------------------------------------------- 2
P("## 2 · Situation")
P("")
table(["Symptom", "Seen by", "Where it shows (locator)", "Relevant records the persona cannot see"], [
    ["Leonard wants one straight page on what each bet cost to build and what it brought in before his angel calls, and asks Robert to own it.", "Robert (mentioned by name)", f"{ASK1}, {ASK2}", "—"],
    ["The only figures so far are Leonard's own quick numbers, and the deck's brought-in slide still says to fill it in.", "Robert (shared with him)", f"{SHEET}, {DECK}", "—"],
    ["22 payee issues sit in Backlog with bank spellings as titles and short notes of what the founders remember.", "Robert (Linear, unscoped)", f"{PROJECT}, ENG-2438 to ENG-2459", "leonard.hayes@harmonygames.co/1798427314394417287, Leonard's mailbox only (can-see NO, pasted in §5a); not needed, §5 F36 and F37 carry what Robert can read"],
])

# ---------------------------------------------------------------- 3
P("## 3 · Investigation → action")
P("")
P("Questions to resolve (no answers here):")
for q in ["Who is each payee, where the bank shows a token or another name?",
          "Which payments count under the method for each payee, and does anything outside the notices belong in?",
          "Which bucket does each payee fall in?",
          "Which bet does each counted payment belong to?",
          "What did each bet cost to build, and what did each bring in?",
          "Where does a figure differ from what the notices add up to, and why?",
          "What changes on the draft deck?"]:
    P(f"- {q}")
P("")
P("Writes those answers feed: the sheet (one row per payee, the bet totals), a reason on each issue whose figure differs, each issue moved to Done, and the reply to Leonard. Every write depends on the investigation.")
P("")

# ---------------------------------------------------------------- 4
P("## 4 · Pinned final state (UGT anchor)")
P("")
table(["Deliverable", "Required contents", "Destination", "Recipients", "Catalog write", "Fed by"], [
    ["The sheet", f"one row per payee in the layout of {SHEET} (Payee, Name on the bank, Bucket, Domino Delights, ZM, Combo Fighter, Company, Note), each bet's build cost and what each bet brought in, with Combo Fighter's left off as the method says", f"Robert's Drive; his root is {ROOT}", f"shared with {LEO} and {ART}", "gsheets_create_spreadsheet, gsheets_values_update, gdrive_share_file", "every §3 question"],
    ["Payee issues", "all 22 moved to Done once the row is right; a reason comment first wherever the figure differs from the notices' sum", f"{PROJECT}, ENG-2438 to ENG-2459", f"read by {LEO} and {ART}", "linear_create_comment, linear_update_issue", "bucket, count and figure questions"],
    ["Reply to Leonard", "what each bet cost and brought in (Combo Fighter's left off), what changes on the deck, and the link to the sheet", f"#winddown C0ADGSZKR3R: a thread under {ASK1} or {ASK2}, or top-level", LEO, "slack_send_message", "the totals and the sheet"],
])
P(f"Alternatives a careful run could defend, each accepted or settled in §4b: a thread under either of Leonard's two posts or a new post in #winddown ({ASK2} says 'tell me here'); editing the deck as well as reporting on it, though he says he will update it himself ({DECK}); a one-page doc beside the sheet ({ASK1}); where the brought-in figures sit on the sheet, since the layout has no column for them ({SHEET}); and whether Marketing and Company dollars also fill the bet columns ({METHOD}).")
P("")
P("### 4b · Canonical outcome (all fair outcomes)")
P("")
b = TOT["build"]
rows4b = [
    ["Sheet", "owner and place", "owned by Robert, in his Drive", "'keep yours in your drive'", f"his root {ROOT} or any folder he owns; not a folder of Leonard's", "material (owner) / representational (folder)", ASK2],
    ["Sheet", "title", "—", "'keep yours in your drive'", "any title", "representational", ASK2],
    ["Sheet", "columns", "Payee · Name on the bank · Bucket · Domino Delights · ZM · Combo Fighter · Company · Note", "'use the layout of my Angel note working sheet'", "same columns; extra columns and a totals row free", "material (columns) / representational (order)", SHEET],
    ["Sheet", "rows", "22, one per payee, with the zero rows kept", "—", "matched on the account ending (NB-12), never on a token name; Payee label free, bank spelling or the name the notes give", "material", METHOD + ", ENG-2438"],
    ["Sheet", "Build rows", bucket_cells("Build"), "—", "to the cent or the whole dollar", "material", "ENG-2438, " + METHOD],
    ["Sheet", "Marketing rows", bucket_cells("Marketing"), "—", "dollars in the bet columns, or in the row with the bet named; kept out of every build total. Marketing total 73,965.63 if shown", "material (bucket) / representational (cell)", "ENG-2441, " + METHOD],
    ["Sheet", "ENG-2459 row", "ENG-2459 ***9368 at zero in every money cell, Bucket Marketing", "'Every payee keeps its line, even at zero'", "zero or blank cells", "material", "ENG-2459, " + METHOD],
    ["Sheet", "Company rows", bucket_cells("Company"), "'that goes in the Company column'", "dollars in the Company column, with or without the same amount in a bet column; Company total 49,625.00", "material (Company figure) / representational (bet cells)", "ENG-2443, " + METHOD],
    ["Sheet", "Non-dollar row", "ENG-2454 ***3801 1,999.00 BGN, on the Company line, never in a dollar total", "'stays in its own currency next to the line'", "in the Company cell or that row's Note; '1,999 BGN' or 'BGN 1,999'", "material (currency, bucket) / representational (cell)", "ENG-2454, " + METHOD],
    ["Sheet", "ENG-2450 row", "ENG-2450 ***3203 at zero in every money cell", "'Every payee keeps its line, even at zero'", "any bucket label that marks it as no cost: 'Not a cost', 'None', blank or similar; zero or blank cells", "material (zero) / representational (label)", "ENG-2450, " + METHOD],
    ["Sheet", "bet totals", f"build cost Domino Delights {money(b['Domino Delights'])} · ZM {money(b['ZM'])} · Combo Fighter {money(b['Combo Fighter'])}", "—", "a totals row or anywhere on the sheet; the sum of a whole bet column need not equal it, because Marketing or Company cells may sit there", "material", METHOD],
    ["Sheet", "brought in", "Domino Delights 12,331.25 · ZM 11.99, as recorded, table totals only. Combo Fighter's is left off: 'Leave Combo Fighter’s revenue off for now, on the page'", "'Leave Combo Fighter’s revenue off for now'", "anywhere on the sheet, in any row or tab, because the layout has no column for it. Combo Fighter's cell blank, marked held or 'to come'; a Combo Fighter figure is outside acceptance but nothing grades it (NB-26)", "material (figures) / representational (place)", "snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY, " + METHOD],
    ["Sheet", "Note column", "a reason on the five rows whose figure differs", "—", "wording free; the same reason may sit on the issue only", "representational", "ENG-2439, ENG-2442, ENG-2447, ENG-2450, ENG-2459"],
    ["Sheet", "sharing", f"{LEO} and {ART}", "'share it with Blake and me'", "editor, viewer or commenter", "material (people) / representational (role)", ASK2],
    ["Issues", "state", "Done on all 22, ENG-2438 to ENG-2459", "—", "assignee free", "material", METHOD],
    ["Issues", "reason comment", "before Done on ENG-2439, ENG-2442, ENG-2447, ENG-2450 and ENG-2459, the five whose figure differs from the notices' sum", "—", "wording free; an extra comment on any other issue, such as ENG-2454, is not penalised", "material (the five) / representational (wording)", METHOD],
    ["Reply", "destination", "#winddown C0ADGSZKR3R", "—", f"a thread under {ASK1}, a thread under {ASK2}, or a top-level post", "material (channel) / representational (placement)", ASK2],
    ["Reply", "what each bet cost", f"{money(b['Domino Delights'])} · {money(b['ZM'])} · {money(b['Combo Fighter'])}", "—", "exact, whole dollars, or rounded ($959K, $544K, $73K; $0.96M, $0.54M; $72.7K)", "material (figure) / representational (rounding)", METHOD],
    ["Reply", "what each brought in", "Domino Delights 12,331.25 · ZM 11.99; Combo Fighter's left off ('and when you tell me')", "'Leave Combo Fighter’s revenue off for now'", "exact, or rounded ($12.3K, $12); Combo Fighter's omitted, marked held or 'to come'; a Combo Fighter figure is outside acceptance but nothing grades it", "material (figure) / representational (rounding)", "snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY, " + METHOD],
    ["Reply", "what changes on the deck", "the three cost figures ($985K, $609K, $74K) move to the new ones, and the brought-in slide gets Domino Delights and ZM, with Combo Fighter left off", "'what changes on the deck'", "any wording; Marketing and Company totals optional", "material", DECK],
    ["Reply", "link", "a link to the sheet", "—", "a Drive or Sheets URL", "material", ASK2],
    ["Deck", "edit", "left unchanged: 'I’ll update it myself'", "'what changes on the deck, I’ll update it myself'", "an edit to the deck is not penalised", "representational", DECK + ", " + ASK2],
    ["Trello card", "state", "left untouched: no write is asked of it", "—", "—", "representational", CARD],
]
table(["Deliverable", "Field", "Fixed value (or closed accepted set, with sources)", "Delegated by (quoted span, or —)", "Allowed equivalence class", "Material / representational", "Source"], rows4b)

# ---------------------------------------------------------------- 5
DM = [
    ("F1", "Leonard's ask, first post", "wants one page on what each bet cost and brought in; names the doc", ASK1, "YES (#winddown; check-sql)", "met first (anchor AN1)", "—", "Yes (AN1)"),
    ("F2", "Leonard's ask, second post", "the project, the layout, his Drive, who to share with, where to report, and that he will update the deck himself", ASK2, "YES (#winddown; check-sql)", "met second; a run that reads only the first post misses the deliverables", "the words 'more below' are the only pointer to it", "Yes (AN1)"),
    ("F3", "the method", "every counting rule, including 'that beats the notices for them', 'move each payee's issue to Done' and 'say why on the issue first'", METHOD, "YES (shared; check-sql)", "named by F1; replaces F9", "—", "No (F1 names it)"),
    ("F4", "the working sheet", "the layout; its row is a quick pass, 984,888.21 / 608,820.50 / 73,685.61, every notice by date", SHEET, "YES (shared; check-sql)", "overturned by F3 for the figures, kept for the layout", "figures copied as truth", "No"),
    ("F5", "the draft deck", "$985K, $609K, $74K; brought-in slide empty", DECK, "YES (shared; check-sql)", "overturned by the sheet's results", "—", "No"),
    ("F6", "the project", "'One issue per payee on the SVB notices'", PROJECT + " ENG-2438", "YES (unscoped)", "named by F2", "—", "Yes (AN2)"),
    ("F7", "the 22 issues", "bank spellings and account endings; state Backlog", "ENG-2438 to ENG-2459", "YES (unscoped)", "—", "12 titles carry tokens (NB-12)", "No"),
    ("F8", f"the {NOTES} notes", "what the founders remember, including ENG-2443 'attribution tool, not one game' (with F3's 'tools' it closes Singular as Company) and ENG-2457 'second half of the UX job on the dominoes game'; the notes on ENG-2454 and ENG-2455 are F31 and F39", "ENG-2443, ENG-2457 and every issue's comments", "YES (unscoped)", "read per issue", "comments are not searchable, one read per issue", "No"),
    ("F9", "the quick plan card", "'add up the notices by date and round them'", CARD, "YES (unscoped)", "overturned by F3 ('replaces the quick plan') and the card's comment", "first hit on the board", "No"),
    ("F10", "the angel calls", "Tue Feb 17, 2026, 9:00 to 10:30 PT (17:00 to 18:30Z)", EVT, "YES (own calendar; check-sql)", "—", "—", "No (the prompt may say Tuesday)"),
    ("F11", "the notices", "132 Processed payments in 88 threads, 131 USD and 1 BGN, Sep 5, 2023 to Feb 2, 2026 (re-derived this run, VERIFY lines in §5a)", A + "1776227799449805411", "YES (his mailbox)", "named by F3", "several payments per thread; bodies need a full read", "No"),
    ("F12", "the ***8605 notice", "$4,032.00 Processed Apr 2, 2024. Root cause, never in the prompt: this wire went to a bad account number and came back", A + "1795282860741136988", "YES (his mailbox)", "met first / overturned by F13 and F14", "the bank says Processed", "No"),
    ("F13", "the Apr 5, 2024 exchange", "'This wire didn’t go through', 'I think I messed up the bank account number', 'Fixed up and resubmitted the payment'", f"{ADM}1712331142.975829 {ADM}1712331372.614469 {ADM}1712331718.859679", "YES (#admin_foundersonly member)", "overturns F12", "no run has read a founder channel; 0 of 24 followed a hit into its neighbours (sc4 §3)", "No"),
    ("F14", "the Apr 12, 2024 note", "'bank returned our money': MotMot nets $37,056.00, not $41,088.00", f"{ADM}1712901800.684259 {ADM}1712901837.860709", "YES (#admin_foundersonly member)", "overturns F12", "'returned' was searched 0 of 147 times (sc4 §3)", "No"),
    ("F15", "the Recipient Modified mail", "account ***3341 set Apr 5, 2024, 15:40Z, after the ***8605 wire and before the resend at 16:02Z", A + "1795509850966005840", "YES (his mailbox)", "sits between F12 and the resend", "—", "No"),
    ("F16", "the off-bank route", "Robert paid the mini games dev by company card before the bank had him", f"{ADM}1719603220.131689 {ADM}1719603590.685019 {ADM}1719603595.852129", "YES (#admin_foundersonly member)", "overturns the ENG-2447 note ('the bank has him from Sep 2024' read as the whole story)", "the 'Lucas' hit needs a read around it", "No"),
    ("F17", "the first receipt", "Western Union, Jun 3, 2024, $1,075.00", RECEIPTS[0], "YES (his mailbox)", "admitted by F3's receipt sentence", "68 hits; only 2 of 5 receipts inside the limit", "No"),
    ("F18", "all five receipts", "$7,525.00 sent to [PERSON_NAME_36400], the token on ENG-2447: Lucas totals $13,975.00. Thread 1802092844284446043 also holds a Fwd of its own receipt, same tracking number, so a per-message sum gives $8,600.00, wrongly", " ".join(RECEIPTS), "YES (his mailbox)", "overturns the $6,450.00 notice sum", "the forwarded copy double counts", "No"),
    ("F19", "Leapblock's statement", "30 wires, $407,944; the first one 33,290. F3: closing a file and saying what they received 'beats the notices'", STATEMENT, "YES (#leapblock member; check-sql)", "overturns the notices' $374,654.00", "a Feb 13 post in a channel runs read only by name", "No"),
    ("F20", "the Awaiting notice", "$33,290.00, Sep 13, 2023, no Processed notice follows", A + "1776934359028762037", "YES (his mailbox)", "a Processed-only read never sees it", "—", "No"),
    ("F21", "Arthur's 'Done!'", "the approval run on Sep 13, 2023; corroborates F19 and F20, which settle the figure without it", f"{ADM}1694616691.082479 {ADM}1694616951.239909", "YES (#admin_foundersonly member)", "—", "the post names no payee and no amount", "No"),
    ("F22", "Arthur's Chase mail", "the $4,000 went to the company's own Chase account, so it never left the company", ARTHUR_MAIL, "YES (his INBOX; check-sql)", "overturns F24 and the ENG-2450 note", "subject is about Chase, not the payee", "No"),
    ("F23", "Leonard's reply", "'ah that’s the one I couldn’t place, thanks'", LEO_REPLY, "YES (his INBOX; check-sql)", "confirms F22", "—", "No"),
    ("F24", "the JPMorgan notice", "$4,000.00, Aug 19, 2024, ***3203", A + "1807851044809802572", "YES (his mailbox)", "met first / overturned by F22", "—", "No"),
    ("F25", "Chase is the company's", "'Chase account closed. Cashiers check deposited into SVB.' Oct 31, 2025: Chase was a company account, still open in Aug 2024", ADM + "1761954952.006759", "YES (#admin_foundersonly member)", "supports F22", "—", "No"),
    ("F26", "the post naming Node Media", "'closing our account with Node Media LLC', Jan 2, 2025", ADM + "1735854841.070019", "YES (#admin_foundersonly member)", "gives the display name only; F27 settles the bucket", "the note's wording differs from the post's", "No"),
    ("F27", "the agency's invoice mail", "invoices for services with an ad-spend clause: Marketing, not Build", A + "1815095592611804295", "YES (his mailbox)", "overturns a by-date Build reading of PERSON_4419_NAME LLC", "the name is a token in mail", "No"),
    ("F28", "the contact row", "Lauren Brooks, Telegram Contractor", "564155d70112411151e512a6", "YES (unscoped)", "spells the name the notices token out", "—", "No"),
    ("F29", "her contract", "Exhibit A opens 'plan, launch, and scale Telegram distribution': with F39 and F38 it closes ENG-2455 as Marketing, not Build", "f_20a0df3860bb5731d22f07", "YES (shared)", "overturns a by-date Build reading of ENG-2455", "the note says only 'the contract'", "No"),
    ("F30", "the BGN notice", "1,999.00 BGN, Oct 30, 2025", A + "1847427662807006290", "YES (his mailbox)", "a USD-only parser drops or adds it", "'BGN' alone is past the limit", "No"),
    ("F31", "Martin's note on ENG-2454", "'paid him direct for his laptop, not through Leapblock': equipment, so Company. #admin_foundersonly agrees: 'did you handle Martin’s laptop?', then 'we are doing that as direct wire'", f"ENG-2454 (comment_e89f05a3984064bdb00bc2b1fe6ffee2) {ADM}1761844454.096829 {ADM}1761844624.408899", "YES (unscoped; the exchange: #admin_foundersonly member)", "overturns a Build reading of the payment, which the platform report made on the older note (its F10 row)", "a note read per issue", "No"),
    ("F32", "lifetime revenue", "Domino Delights 12,331.25 · ZM 11.99, 2,284 rows; REVENUE_DAILY_V2 equal (summed this run). F3 holds Combo Fighter's figure off the page, the deck and the reply, so it is no value here (NB-26; platform I3)", "snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY", "YES (unscoped)", "named by role in F3", "a run may report Combo Fighter's anyway", "No"),
    ("F33", "the P&L", "monthly lines, no per-payee figures; a decoy, not called wrong by F3", "f_605121f4a36752645e0ac3", "YES (shared)", "F3 sends the count to the notices instead", "NB-2: no P&L cost is graded", "No"),
    ("F34", "the balance posts", "'discrepancy between the cash in bank' and 'matching what banks say' concern balances, not payees", f"{ADM}1754445622.992119 {ADM}1754445718.724799", "YES (#admin_foundersonly member)", "distractor", "—", "No"),
    ("F35", "the Leapblock MSA", "the saga map work: Build", "f_322bbfdb37d253aa8624b9", "YES (shared)", "supports the ENG-2439 notes", "—", "No"),
    ("F36", "Leonard's third note on ENG-2459", "'that wire came back the same day, I’d already re-sent it through payoneer': F3's test takes the $125.00 notice out, and the Payoneer route then needs a receipt in Robert's mail (F37)", "ENG-2459 (comment_3906b5b40dfcdabdc83381f0060bac82)", "YES (unscoped)", "overturns the $125.00 notice. C06MXPL9536/1715113013.494939 and C06MXPL9536/1715064961.427529 agree but are not needed", "a note read per issue; the run must then look for a receipt", "No"),
    ("F37", "no receipt for the re-send", "Robert's mail holds only two 'Dixelar sent you a payment request' mails, May 5 and Sep 25, 2024. A request is not a receipt, so the line is zero with a reason and Marketing stays its bucket. The Payoneer receipts are in Leonard's mailbox only, and Robert's mail has no Upwork receipt either (census and positive control, VERIFY lines in §5a)", f"{A}1798239548116390324 {A}1811158112675912556", "YES (his mailbox)", "closes F36's route under F3's receipt sentence", "a request can be misread as a receipt; the absence is shown only by searching", "No"),
    ("F38", "her role post", "'She will lead our Telegram distribution strategy', Oct 10, 2025", "C05KNDCHAAG/1760125440.959149", "YES (#company-internal member)", "with F39 and F29 closes ENG-2455 as Marketing", "—", "No"),
    ("F39", "Leonard's third note on ENG-2455", "'her contract had her running our paid UA on telegram, so she’s marketing, not build'", "ENG-2455 (comment_990674712ad0127e26f780eadb5418ea)", "YES (unscoped)", f"settles the bucket the platform found open (UGT 2, Clarity 1; {PLAT} I1, attempt {ATTEMPT}); F29 and F38 agree", "a note read per issue", "No"),
]
assert [d[0] for d in DM] == list(SRCH), "§5 rows and the search list differ"
PLATFORK = {"F12": "F2", "F13": "F2", "F14": "F2", "F17": "F6", "F18": "F6", "F19": "F3", "F20": "F3", "F22": "F4", "F24": "F4", "F27": "F7", "F36": "F5", "F37": "F5"}
DM = [(f, a, v, l, pr, mf + f"; settled at the platform /prompt, fork {PLATFORK[f]}" if f in PLATFORK else mf, r, n) for f, a, v, l, pr, mf, r, n in DM]
P("## 5 · Discovery map")
P("")
P(f"Root causes and findings appear here and nowhere earlier, and never in the prompt. Rows marked 'settled at the platform /prompt' cite the deep-recheck forks of {PLAT} (attempt {ATTEMPT}, rev4 SQL 872bbb307710), which found each settled by a record Robert can see; rev6 changes none of those records.")
P("")
table(["Fact", "Value", "Locator", "Persona-readable", "Met first / overturned by", "Search risk", "Name in prompt?"],
      [[f"{fid} {fact}", val, loc, pr, mf, risk, nm] for fid, fact, val, loc, pr, mf, risk, nm in DM])

# ---------------------------------------------------------------- 5a
ADJ = {"F13": "the hit sits in the exchange; the two target posts are its neighbours, reached by reading around it",
       "F16": "the hit sits in the exchange; the target post follows it the same day, reached by reading around it",
       }
ROUTE = {"F21": "NO — routed to /create-injection (§12): no natural query reaches it; F19 and F20 settle the figure without it",
         "F26": "NO — routed to /create-injection (§12): the note's own words return nothing and the name can't be formed cold; F27 settles the bucket"}
P("## 5a · Search-as-persona proof")
P("")
P("Every query uses only what an agent knows at that step: the prompt, an issue title or note, or a record already found. A verbatim quote from a target does not count as a natural query. "
  "Seeded records never appear in `persona_view.py search`, which reads base data only: those rows are counted from the SQL overlay and proven by `check-sql`, and each says so. "
  "Limits of the proof: the tool matches a contiguous phrase, so a multi-word query can return 0 where a live search might not ('Martin laptop' 0, 'Martin’s laptop' 1), and it lists oldest first where live Slack lists newest first (sc4 §3), so limit 10 is not the live ranking.")
P("")
rows5a = []
for fid, *_ in DM:
    r = SRCH[fid]
    found = ROUTE.get(fid, r["found"]) if r["found"] == "NO" else r["found"]
    if fid in ADJ:
        found = f"YES (base hit; {ADJ[fid]})"
    rows5a.append([fid, r["service"], f"{r['query']} ({r['how']})", f"{r['base']} base + {r['seeded']} seeded", r["hidden"], r["first"] or "—", found])
table(["Fact (§5 row)", "Service", "Natural query", "Visible hits", "Hidden by ACL", "First visible hit (id)", "Found?"], rows5a)
P("Outputs verbatim, then the check-sql rows for these facts, the can-see lines and this run's VERIFY lines:")
P("```")
P(RAW)
P("```")
P("")

# ---------------------------------------------------------------- 6
P("## 6 · Triggers, incorporation and implicit requirements")
P("")
table(["Graded requirement", "Seeded where", "Trigger category the prompt must carry", "Incorporating source (locator · persona-readable · unique · instructions-not-answer)", "Inferable"], [
    ["count by the method", METHOD, "scope: Leonard's ask, and that he laid out how to count it", f"{ASK1} names the doc by title · YES · one doc with that title · rules, no figures", "yes, once the ask is followed"],
    ["sheet layout", SHEET, "a pointer that he set how it should look; no layout clause", f"{ASK2} 'use the layout of my Angel note working sheet' · YES · one working sheet · layout only; its figures are the quick pass", "yes, once the ask is followed"],
    ["sheet in his Drive, shared", ASK2, "destination and recipients", f"{ASK2} · YES · named by the prompt too · instruction", "yes"],
    ["issues to Done, reason first", METHOD, "deliverable: work through the project the way he wants", f"{METHOD} last paragraph · YES · unique · instruction", "gotcha with a record trigger"],
    ["the five figures that differ", "F12 to F24, F36, F37", "none in the prompt", f"{METHOD} 'A notice is where you start, not the last word' and 'that beats the notices for them' · YES · unique · states the tests, not the payees", "gotcha with a record trigger"],
    ["buckets and the bet calendar", METHOD, "none in the prompt", f"{METHOD} · YES · unique · rules only", "gotcha with a record trigger"],
    ["brought-in figures", "snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY", "deliverable: what each bet brought in, on the page; the method holds Combo Fighter's", f"{METHOD} names the table by role · YES · V2 sums equal · no sums given", "gotcha with a record trigger"],
    ["reply with figures, deck changes, link", ASK2, "destination and content", f"{ASK2} 'tell me here' · YES · one channel · instruction; the link comes from the prompt", "yes"],
])
P(f"Prompt text: 04_Prompt.txt, {len(P4.split())} words, sha256 {P4SHA}, the text the platform reviewed. It says 'how it should look' and 'Build that page as a sheet' in place of a layout clause, 'reply to him in #winddown', and 'the draft deck'.")
P("")
P("Anchor-name table (noun phrases of at most 6 words; `;` separates synonyms):")
P("")
table(["Anchor", "May be named"], [["AN1", "Leonard's ask in #winddown"], ["AN2", "the Payee history project"]])

# ---------------------------------------------------------------- 7
P("## 7 · Dates and constraints")
P("")
table(["Item", "Absolute date or value", "Source", "Past fact or deadline"], [
    ["Robert's today", "Saturday Feb 14, 2026 (clock 2026-02-14T00:00Z = Fri Feb 13, 4:00 PM PT)", f"00_Task_Context.json universe.persona_today; latest ask post {ASK2}", "—"],
    ["Leonard's ask", "Thu Feb 12, 2026, 5:23 and 5:24 PM PT (Fri Feb 13, 01:23 and 01:24Z). 'Thursday' is the Pacific day", f"{ASK1}, {ASK2}", "past fact"],
    ["the method", "written Thu Feb 12, 3:52 PM PT (23:52Z), edited 4:41 PM PT (Feb 13, 00:41Z)", METHOD, "past fact"],
    ["the working sheet and deck", "Thu Feb 12, 2:44 and 2:52 PM PT (22:44 and 22:52Z)", f"{SHEET}, {DECK}", "past fact"],
    ["Leapblock's statement", "Fri Feb 13, 12:37 AM PT (08:37Z), before the Slack export end (NB-6)", STATEMENT, "past fact"],
    ["Arthur's mail and Leonard's reply", "Fri Feb 13, 8:26 and 9:08 AM PT (16:26 and 17:08Z)", f"{ARTHUR_MAIL} {LEO_REPLY}", "past fact"],
    ["the notices' window", "Sep 5, 2023 to Feb 2, 2026", A + "1776227799449805411", "past fact"],
    ["the bet calendar", "Domino Delights to Jan 8, 2025; ZM Jan 9 to Nov 23, 2025; Combo Fighter from Nov 24, 2025. No payment falls near a boundary", METHOD, "rule"],
    ["the angel calls", "Tue Feb 17, 2026, 9:00 to 10:30 AM PT (17:00 to 18:30Z)", EVT, "deadline (future event)"],
    ["shutdown premise", "Feb 14 is after the wind-down began: no business as usual, and the deck itself says orderly wind-down", DECK, "past fact"],
    ["Leonard's notes on ENG-2455 and ENG-2459", "Thu Feb 12, 4:45 and 4:58 PM PT (Feb 13, 00:45 and 00:58Z)", "ENG-2455, ENG-2459", "past fact"],
    ["known issues touched", f"NB-1 and NB-6 (only founders and Leapblock's contact post late, all before 10:03Z Feb 13); NB-2 (no P&L cost graded); NB-12 (key on account endings); NB-24 (no base Linear comments, all {NOTES} notes are seeded); NB-26 (the method holds Combo Fighter's revenue, so no Combo Fighter figure is graded)", f"f_605121f4a36752645e0ac3, ENG-2438, {STATEMENT}", "constraint"],
])

# ---------------------------------------------------------------- 8
P("## 8 · Difficulty levers")
P("")
table(["Lever", "Used", "Load-bearing", "Where it lives", "Prompt-side condition"], [
    ["Ambiguity", "yes", "yes", "who each payee is and which payments count sit across notes, mail, Slack and a contract (F12 to F31)", "the prompt names the two anchors only, never where an answer lives"],
    ["Dynamic change", "yes", "yes", "the notices and quick numbers come first; F13, F14, F19 and F22 overturn them", "the prompt names neither the first summary nor the correction"],
    ["Multi-source", "yes", "yes", "Gmail, Linear, Slack, Docs, Sheets, Slides, Snowflake, Contacts, Trello, Calendar, Drive", "no source named as an exact artifact beyond the anchors"],
    ["Async", "no", "no", "friction none (03_Error_Async_Config.txt)", "—"],
    ["Error recovery", "no", "no", "friction none", "—"],
    ["Access control", "no", "no", "every graded record is Robert-visible (check-sql PASS); records outside his reach are off the graded path (F37)", "no ask to read someone else's scoped data"],
])

# ---------------------------------------------------------------- 9
P("## 9 · Must not appear in the prompt")
P("")
for grp, items in [
    ("Tool and server names (catalog.json)", "slack_send_message, slack_read_channel, slack_read_thread, slack_search_public_and_private, linear_list_issues, linear_list_comments, linear_create_comment, linear_update_issue, gsheets_create_spreadsheet, gsheets_values_update, gsheets_values_get, gdrive_share_file, gdrive_search, gdocs_get_document_text, gslides_get_presentation_text, gmail_search_messages, gmail_get_messages_batch, gmail_get_thread, snowflake_execute_query, snowflake_describe_table, trello_search, trello_get_card, contacts_search_contacts, gcal_list_events; any MCP server name; 'the X tool'"),
    ("The dossier's never-name list", "the method's rules, the bet dates, the buckets, any payee, any figure, the notices, #leapblock, #admin_foundersonly, the Chase mail, the contract, Western Union, the warehouse table"),
    ("Opaque ids and filenames", f"{METHOD}, {SHEET}, {DECK}, {CARD}, the project id, ENG-2438 to ENG-2459, {ASK1}, {ASK2}, {STATEMENT}, REVENUE_DAILY"),
    ("Findings and root causes (§5)", "that any wire came back or was re-sent; card, Payoneer or other off-bank payments; the wire with no Processed notice; the company's own account; Combo Fighter's revenue or that it is held; who any token is; every total, per-payee figure, count of differing issues or deck replacement"),
    ("Hidden authorities", "the method's contents, the Trello card, the P&L, Arthur's mail, the #leapblock post"),
    ("Format and choreography", "markdown, numbered steps, a per-column content list, a service list, a call count, 'first … then …', and 'payee by payee', which reads as enumeration (pw1_prompt_lessons.md span 11)"),
    ("Copied wording", "'Can you take care of what he asked for?', word for word the LLC prompt (pw1_prompt_lessons.md span 4)"),
    ("Friction and files", "none configured; no reference files or /app/artifact paths"),
]:
    P(f"- **{grp}:** {items}.")
P("")

# ---------------------------------------------------------------- 10
P("## 10 · Entity traps")
P("")
P("`entity.py collisions` and `entity.py resolve` for every name below, verbatim:")
P("```")
P(ENT)
P("```")
table(["Correct entity (exact)", "Lookalike(s)", "How they differ", "Locator (email or record id)"], [
    ["Leonard Hayes", "no exact match on 'Leonard' alone; one candidate", "co-founder, sender of the ask", LEO],
    ["Arthur Blake ('Blake')", "no exact match on 'Blake' alone; one candidate. Mail files use blake@harmonygames.co", "one person; share to the arthur.blake address", ART],
    ["Robert", "—", "the persona; Slack EMPLOYEE_0016_SLACK_ID", ROB],
    ["Martin Walsh (ENG-2454)", "Martin Lewis (PERSON_0394_EMAIL); Martin on the Leapblock notes is the same Walsh", "the note says 'same Martin as on Leapblock'", "martin.walsh@harmonygames.co, ENG-2454"],
    ["Marcus (Eveline Art)", "Marcus Bennett, Marcus Lee, the Trello and GitHub Marcus", "ENG-2440's note, 'Marcus’s company'; bare name, resolved only by the issue", "ENG-2440"],
    ["Lauren Brooks", "Oliver Brooks", "the contact row 564155d70112411151e512a6 is Lauren", "lauren@harmonygames.co"],
    ["Nathan Price", "Calvin Price", "ENG-2453 is Nathan", "nathan@harmonygames.co"],
    ["Lucas", "—", "ENG-2447's token [PERSON_NAME_36400] is on all five receipts", "lucas@harmonygames.co"],
    ["Graham Porter", "no entity record (resolve: no exact match)", "appears by name on the notice and issue only", "ENG-2449"],
    ["Oleg", "no entity record (resolve: no exact match)", "appears in the ENG-2459 note", "ENG-2459"],
    ["Dixelar", "no entity record (resolve: no exact match)", "the name on the payment requests in Robert's mail, which the notes call Oleg", "ENG-2459"],
    ["Deel, Inc. ***8380", "[ORG_NAME_0057], Inc. ***8380", "two spellings, one account (NB-12)", "ENG-2438"],
    ["Singular Labs Inc ***4015", "[SOURCE_ORG_0351] Labs Inc ***4015", "two spellings, one account (NB-12)", "ENG-2443"],
    ["the Payee history project", "base projects on team_ENG", "the only project of that name", "ENG-2438"],
    ["Angel note: how to count the money", "Angel note working; Angel note money page", "the doc is the method; the others are the layout and the replaced plan", METHOD],
])

# ---------------------------------------------------------------- 11
P("## 11 · Pre-submit checklist")
P("")
for x in ["Reads like Robert: first person, plain, no spec-sheet layout", "Names only the two anchors (§6); nothing from §9", "Names no tool, server or parameter", "States no root cause",
          "Every sentence is needed; deleting one changes something", "Every date sits before the clock or is a real future date; Thursday and Tuesday checked against §7",
          "Carries the three deliverables and their destinations: the sheet in his Drive, shared with Leonard and Blake; the project worked through; the reply in #winddown with the link",
          "No hint, riddle, hedge, if-chain or audit wording", "Keeps 'angel calls' and 'bet', which hold the investor framing; no 'payee by payee'; not the LLC prompt's sentence", "Asks for investigation and action across at least two services", "Every fair reading in §4b is still fair against the final text",
          "20 to 4,000 words", "Run `/create-prompt-writing check` before `/prompt`"]:
    P(f"- [ ] {x}")
P("")

# ---------------------------------------------------------------- 12
P("## 12 · Blockers and routed defects")
P("")
P(("No blocker in this brief." if INJ_OK and ERR_OK else "The chain is open until the upstream gates are re-run on this SQL; nothing in this brief is blocked otherwise.") + f" Error/async: the requester skipped the stage; friction is none and 03_Error_Async_Config.txt records that (digest {h03}). Reference files: none exist.")
P("")
P("Routed to /create-injection for the requester's decision. My read is that neither needs a change, because no graded figure rests on them:")
P("")
P("- F21 Arthur's 'Done!' corroborates only: F3's closing-file sentence with F19 and F20 settles Leapblock.")
P("- F26 the post naming Node Media gives a display name: F27 settles the bucket, and §4b leaves the Payee label free. The surface's X6 keys its row on the name 'Node Media', so the rubric must key on ***0115 instead.")
P("")
P(f"The platform /prompt review of rev4 ({PLAT}, attempt {ATTEMPT}) failed at 2 on two record gaps. Rev6 closes both, verified on disk this run: Leonard's third note on ENG-2455 settles Lauren Brooks's bucket (F39; its I1 and I2), and the method now holds Combo Fighter's revenue off the page, the deck and the reply (F3, F32; its I3, NB-26). The prompt is unchanged. ENG-2459 stays zero, Marketing, reason first (F36, F37; its fork F5).")
P("")
P("Two facts pass only through a read around the hit, which runs rarely do (sc4 §3): F13 and F16. They stay YES because a natural query lands inside the right exchange. Martin's bucket no longer needs one: the ENG-2454 note now names the laptop (F31).")
P("")
P("For /create-rubric-writing: 01_Gradable_Surface.json is narrower than §4b or misses a graded fact in these slots, which the rubric must widen or add to rather than copy:")
P("")
for x in [f"D4 reads a thread on {ASK1.split('/')[1]} only; §4b accepts either post or top-level.",
          f"D1 reads the parent {ROOT} only; §4b accepts any folder Robert owns.",
          "X9 reads the Company cell; §4b also accepts the row's Note.",
          "The ledger's name_regex needs a word like angel, seed, bet, money or payee in the title; §4b accepts any title.",
          "X6 and the other field slots key on truth names; NB-12 says key on account endings.",
          "C1 to C4 cover four reason comments; no slot covers ENG-2459, the fifth.",
          "R2 matches only the word 'deck'; plan a real row for the three cost figures and the brought-in line, with Combo Fighter left off (pw1_prompt_lessons.md).",
          "V3 is gone (29 slots, weight 91), so no slot grades Combo Fighter's revenue, which matches the method's hold; no rubric row may grade a Combo Fighter figure."]:
    P(f"- {x}")
P("")
P("Unverified: the Leapblock invoice PDFs (f_06f42106818045db3b7d0d and siblings) can't be read through hg.py, so nothing here confirms they total the Sep 2023 wire; the Chase top-up reason in F22 is seeded and no base record states it; live search ranking and matching differ from persona_view (§5a), so findability is proven for this tool only; the off-bank census covers the routes in the VERIFY lines, and hits were judged by subject except the four 'Payment Receipt' threads, which were read (a registered-agent receipt, an ad prepayment and two inbound deposit notices, none a contractor payment).")
P("")
P(f"Folded in: plan/research/pw1_prompt_lessons.md, which reviewed an earlier 115-word candidate; the platform /prompt report {PLAT}; and the cold reviews listed in §13.")
P("")

# ---------------------------------------------------------------- 13
P("## 13 · Self-review")
P("")
P("Walked Evals/1_Prompt_Eval.md Phases 1 to 3 against this brief. 04_Prompt.txt exists and is the text the platform reviewed; check mode re-runs every C-check on it. The rows below cover every area the brief can settle.")
P("")
table(["Area", "Counter-reading (strongest argument it fails)", "Evidence that resolves it", "Verdict"], [
    ["Fair readings (C6)", "Leapblock stays at $374,654: 'what the banks say is our ground source of truth', and a payee's statement is not a bank.", f"{METHOD} says 'If someone we paid closes out their file with us and tells us what they received, that beats the notices for them', and {STATEMENT} is that closing post. It ties to the notices in every year once F20's wire is added (VERIFY lines, §5a). A newer source settles it: case K49-newer-source.", "settled"],
    ["Fair readings (C6)", "ENG-2459 stays at $125: the notice says Processed, and Robert's mail holds Dixelar's requests for that amount, so a receipt reached him.", f"Leonard's note on ENG-2459 says the wire came back, which meets {METHOD} 'unless one of us has said the money came back'. {A}1798239548116390324 and {A}1811158112675912556 are payment requests. 'Thanks for your payment' returns 0 as Robert and sits only in Leonard's mailbox (positive control, VERIFY lines), and the method counts what 'reached your mail'. Zero, Marketing, reason first.", "settled"],
    ["Fair readings (C6)", "Lucas should carry the fees, $7,528.96 on 'money that left', or $8,600 if every receipt mail is summed.", f"{METHOD} says 'at the amount sent, not the fee'. VERIFY shows 5 tracking numbers and 1 forwarded copy in {RECEIPTS[1]}, so $7,525.00.", "settled"],
    ["Fair readings (C6)", "Lauren Brooks is Build by date, as a monthly contractor on the team, or Company: the platform found no record deciding it.", f"That was rev4 ({PLAT} I1, attempt {ATTEMPT}). Rev6 adds Leonard's note on ENG-2455, 'her contract had her running our paid UA on telegram, so she’s marketing, not build' (F39), which agrees with f_20a0df3860bb5731d22f07 Exhibit A and C05KNDCHAAG/1760125440.959149. A record by the payee's own approver now names the bucket.", "settled"],
    ["Fair readings (C6)", "Martin's 1,999 BGN is Build, ZM by date, as the platform read it.", f"ENG-2454's note now reads 'paid him direct for his laptop, not through Leapblock' (F31), {ADM}1761844454.096829 asks about the laptop, and {METHOD} puts equipment in Company.", "settled"],
    ["Fair readings (C6)", "The reply must give Combo Fighter's revenue, because the prompt asks what each bet brought in.", f"{METHOD} says 'Leave Combo Fighter’s revenue off for now, on the page, on the deck and when you tell me'. The prompt hands the counting to Leonard ('how he wants it counted'), and an incorporated source governs the decisions it covers (playbook fair-reading step 2). §4b accepts the figure left blank, held or 'to come'; it closes the platform's I3 (NB-26).", "settled"],
    ["Fair readings (C6)", "The traps the platform called settled could still fork on rev6.", f"{PLAT} forks F2 to F7 settle MotMot, Leapblock, JPMorgan, Oleg, the Western Union receipts and Node Media on records Robert can see. Rev6 changes none of those records apart from Oleg's note wording, which still says the wire came back (F36).", "settled"],
    ["Fair readings (C6)", "Singular is Marketing, since attribution serves ads, or splits across the games.", f"ENG-2443's note says 'attribution tool, not one game', and {METHOD} puts 'tools' and anything not for one game in Company.", "settled"],
    ["Fair readings (C6)", "The reply belongs only under the post that says 'tell me here'.", f"{ASK2} says it, but the draft wording says 'in #winddown', and Eval 1 §2.1 fails only materially incompatible outcomes. All three placements reach Leonard with the same content, so §4b accepts them. Surface D4 is flagged in §12.", "accepted outcomes"],
    ["Fair readings (C6)", "Brought-in figures can sit in the reply alone, since the layout has no column for them.", f"{ASK1} defines the page as cost and brought in, and the draft wording says 'Build that page as a sheet', so they belong on the sheet. {SHEET} has no column, so §4b takes any row or tab.", "settled"],
    ["Fair readings (C6)", "The run should edit the deck, since it is told what changes.", f"{ASK2} ends 'I’ll update it myself', so the deck is his edit. §4b keeps an edit unpenalised because {DECK} is shared with Robert.", "accepted outcomes"],
    ["Assignment fit (C4)", "Reconciling payees is bookkeeping, so Business Function scores 3 as it did on the winddown task.", f"The platform scored Business Function 5 on this exact prompt ({PLAT}, Phase 1: 'a founder deliverable for the angel calls'). It keeps 'angel calls', 'bet' and the draft deck, which pw1_prompt_lessons.md row 3 named as the guard.", "settled on the platform"],
    ["Clarity (C7)", "'work through the project the way he wants' is a vague verb with no stated write.", f"{METHOD} states the writes, and Eval 1 §2.6 treats a vague verb as Minor when records hold the rule. Two competing named writes are absent.", "Minor at most"],
    ["Clarity (C7)", "'one straight page' could mean a document, not the sheet.", f"The draft wording says 'Build that page as a sheet', and {ASK2} sets the layout. A doc beside it changes no graded write.", "settled"],
    ["Incorporation (C8)", "'He laid out how he wants it counted' could lead to the Trello plan instead of the doc.", f"{ASK1} names the doc by title, F3's search has one hit, and {METHOD} says it replaces the plan on {CARD}.", "unique"],
    ["Incorporation (C8)", "The method might hand over the answer.", f"{METHOD} states tests and dates and no payee or total. The closing-file sentence names no payee. {'fact_check --no-leak passed in the dossier (01_Grounding_Dossier.md).' if INJ_OK else 'The fact_check for this SQL is pending with the injection re-run.'}", "instructions only"],
    ["Truthfulness (C17)", "'On Thursday' is false: the ts falls on Friday in UTC.", f"{ASK1} is 2026-02-13T01:23:41Z, which is Thu Feb 12, 5:23 PM PT; persona dates are Pacific (§7).", "true"],
    ["Truthfulness (C17)", "'Blake' could be someone else, and 'angel calls on Tuesday' could be loose.", f"entity.py resolve 'Blake' gives one candidate, {ART} (§10). {EVT} is Tue Feb 17, 2026.", "true"],
    ["Feasibility / ACL (C18–C19)", "Robert may not read a deciding record, or the Done state may not exist.", "check-sql verdict PASS with 0 load-bearing rows hidden (§5a), and Done is a state on team_ENG issues (hg.py search linear, 1,944 base issues). All six writes are in catalog.json.", "feasible"],
    ["Feasibility / ACL (C18–C19)", "Exact revenue may not survive the tool path.", "snowflake.ANALYTICS.MONETIZATION.REVENUE_DAILY sums to the cent through hg.py; V2 agrees. Combo Fighter's is held by the method and graded nowhere (NB-26).", "feasible"],
    ["Feasibility / ACL (C18–C19)", "The prompt asks what each bet brought in while the method withholds one, which is conflicting instructions.", f"The prompt incorporates the method ('He laid out how he wants it counted'), and {METHOD} narrows Leonard's own ask; a reply that says Combo Fighter's figure is held answers each bet. No write becomes impossible. Check mode should re-test this on the final text.", "feasible; watch at check"],
    ["Contrived register (C15–C16)", "'how it should look' hides a layout the persona knows, which is the hidden-destination pattern.", f"The destination is named ('in my Drive'), and the clause only points at {ASK2}: pw1_prompt_lessons.md §1b shows 'His email lays out what he's after.' rejected as a defect, and control-named-destination passes, unlike K42-hidden-destination.", "ordinary"],
    ["Contrived register (C15–C16)", "Three deliverables in order could read as a command list.", "Deliverables and who to tell are not sequenced method steps (Eval 1 §1.3.1): control-plain-request, unlike K1-audit-form.", "ordinary"],
])
P("Fair readings, clarity, incorporation, truthfulness, feasibility / ACL and the contrived register are each addressed above. Facts were re-read in this run, not carried from notes: 132 notices, 23 account endings, Leapblock by year, 5 receipts, the off-bank census, both revenue tables, and every §5a query. "
  "The root cause appears only in §5; assemble_brief.py stops if a cause word reaches §1 to §4.")
P("")
P(f"Independent reviews. The platform /prompt review of rev4 ({PLAT}, attempt {ATTEMPT}, SQL 872bbb307710) is on disk and was read in this run: it failed at 2 on Lauren Brooks's bucket (UGT 2, Clarity 1) and Combo Fighter's revenue (Cross-Service Coherence 1), scored every other dimension 5, and settled the Leapblock close-out, JPMorgan, the Western Union receipts, Oleg, MotMot and Node Media. The others were reported to me by the coordinator in this session; none is saved as a file and I have not seen their text, so these are the coordinator's summaries, not findings I checked: a rev1 blind sweep (36 forks, 18 open); a rev2 sweep in which a keyless reviewer reproduced the three build totals, Company 49,625.00 plus BGN 1,999 and that revision's revenue figures, with prompt findings none; a cold Eval 1 review (NON-FAIL on Clarity and Coherence, both reported fixed on the record in rev3); a fourth cold reviewer on the rev3 wording, whose two small findings went into rev4; and a cold reviewer on rev5 who found the reply gap and the Martin reading, both reported fixed in rev6. I verified the Martin fix (F31). For the reply gap I can only say the rev6 change that touches the reply is the method's 'and when you tell me' clause on Combo Fighter; Leonard's two posts are unchanged since rev3. No cold review has covered rev6 itself.")
P("")
P("Unresolved: F21 and F26 are routed for the requester's decision (§12); the surface slots listed in §12 need widening at the rubric stage; the items marked Unverified in §12 stand; no cold review has covered rev6; the prompt/method split on Combo Fighter's revenue should be re-tested in check mode; check mode re-tests every point on 04_Prompt.txt.")
P("")

text = "\n".join(L) + "\n"
head = text[:text.index("## 5 · Discovery map")]
head = head[head.index("## 1 · Assignment fit"):]
BANNED = r"returned|bounced|came back|bad account|wrong account|Western Union|receipt|Chase|own account|laptop|statement|Telegram|ad.spend|company card|re-sent|resubmitted"
hits = sorted({m.group(0) for m in re.finditer(BANNED, head, re.I)})
if hits:
    sys.exit(f"STOP: cause words in §1-§4: {hits}")
if "11.75" in text or "11,75" in text:
    sys.exit("STOP: a Combo Fighter revenue value reached the brief")
if "1770858495" in text or "1770858501" in text:
    sys.exit("STOP: excluded ts in the brief")
open(os.path.join(WF, "04_Prompt_Writing_Brief.md"), "w").write(text)
print("wrote 04_Prompt_Writing_Brief.md", len(text), "chars; NO rows", NOS)
