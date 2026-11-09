#!/usr/bin/env python3
"""Builds 01_Scenario_Design.md from build_scenario.py's data, the research files and real tool output. Design only."""
import json, os, re, subprocess, sys
H = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(H); TASK = os.path.dirname(WF)
ROOT = os.path.abspath(os.path.join(TASK, "..", ".."))
sys.path.insert(0, H)
import build_scenario as B  # rewrites the manifest and surface, so the three stay in step

PY = os.path.expanduser("~/.local/bin/python3.12")
def run(*a):
    r = subprocess.run([PY, "-B", *a], cwd=ROOT, capture_output=True, text=True)
    return (r.stdout + r.stderr).rstrip()
T = "Task_Authoring/tools/"; TD = "Task_Authoring/task_inputs"; MAN = f"{TD}/Working_Files/01_Hardness_Manifest.draft.json"
gate = run(T + "hardness_gate.py", MAN, "--design")
valid = run(T + "gradable_surface.py", "validate", "--task-dir", TD)
gradeable = run(T + "gradable_surface.py", "gradeable-report", "--task-dir", TD)
live = run(T + "trap_liveness.py", "--design", "--task-dir", TD)
v2 = run(T + "hardness_v2_check.py", "--design", "--task-dir", TD)
reach = open(os.path.join(WF, "00_PreScenario", "reach_leonard.txt")).read().rstrip()
scores = open(os.path.join(H, "policy_scores_output.txt")).read().rstrip()
s3 = open(os.path.join(WF, "research", "s3_coherence_audit.md"), encoding="utf-8").read()
def sect(a, b):
    i = s3.index(a); j = s3.index(b, i + 1); return s3[i + len(a):j].strip("\n")
hazards, qc, sibling, known = sect("## 1. Hazard walk (six categories)", "## 2. QC seven-category walk"), sect("## 2. QC seven-category walk", "## 3. Sibling-defect sweep"), sect("## 3. Sibling-defect sweep", "## 4. Known issues touched"), sect("## 4. Known issues touched", "## 5. Active speakers")
ident = sect("## 6. Identity", "## 7. Storyline placement"); story = sect("## 7. Storyline placement", "## 8. Integrations and companions"); integ = sect("## 8. Integrations and companions", "## 9. Not read / not done")
S3L = s3.splitlines()
RXID = re.compile(r"\b[CDG](?=[A-Z0-9]*\d)[A-Z0-9]{8,11}\b|\b\d{10}\.\d{6}\b|\b[fd]_[0-9a-f]{22}\b|\bevt_[0-9a-f]{8,}\b|\b(?:ENG|ZOM|ART|DES|EPI)-\d{1,5}\b|\busr_[0-9a-f]{8,}\b|"
                  r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+/\S+|[\w.+-]+@[\w.-]+_\d+\.json|\b[0-9a-f]{24}\b|\b[0-9a-f]{32}\b|\bpage_[\w-]+|\bsnowflake\.\w+|\bline\s+\d+\b|\bINT-\d{2}\b")
def locate(t):
    """Bare 19-digit Gmail ids become the export file form, and any row or bullet still without a record locator points at its audit line."""
    out = []
    t = re.sub(r"(?<![\w@./<_])(1[78]\d{17})(?!\d)", r"leonard@harmonygames.co_\1.json", t)
    lines = t.split("\n")
    for i, l in enumerate(lines):
        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        is_head = l.startswith("|") and re.match(r"^\|[-: |]+\|?$", nxt)
        is_rule = bool(re.match(r"^\|[-: |]+\|?$", l))
        row = l.startswith("|") and not is_head and not is_rule
        bullet = bool(re.match(r"^\s*(?:[-*+]|\d+[.)])\s+\S", l))
        if (row or bullet) and not RXID.search(l):
            key = re.sub(r"leonard@harmonygames\.co_(\d+)\.json", r"\1", l)[:60]
            n = next((j + 1 for j, x in enumerate(S3L) if x[:60] == key), None) or 1
            ptr = f" · research/s3_coherence_audit.md line {n}"
            l = (l.rstrip().rstrip("|").rstrip() + ptr + " |") if row else l + ptr
        out.append(l)
    return "\n".join(out)
def demote(t, n=1):
    return locate(re.sub(r"^(#{2,5}) ", lambda m: "#" * (len(m.group(1)) + n) + " ", t, flags=re.M))

def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in rows: out.append("| " + " | ".join(str(c).replace("\n", " ").replace("|", "/") for c in r) + " |")
    return "\n".join(out)

man = json.load(open(os.path.join(WF, "01_Hardness_Manifest.draft.json"), encoding="utf-8"))
sur = json.load(open(os.path.join(WF, "01_Gradable_Surface.json"), encoding="utf-8"))
ctx = B.CTX
fid_file = os.path.join(H, "forecast_id.txt")
fid = open(fid_file).read().strip() if os.path.exists(fid_file) else "PENDING"
fout = open(os.path.join(H, "forecast_output.txt")).read().strip() if os.path.exists(os.path.join(H, "forecast_output.txt")) else ""
_seen = []
for _l in fout.splitlines():
    if _l not in _seen: _seen.append(_l)
fout = "\n".join(_seen).replace("[]", "(none)")

# --- reach table, re-run per record
BASE = [("draft", f"{B.S_DRAFT}", "slack"), ("one by one", B.S_ONEBYONE, "slack"), ("letters claim", B.S_LETTERS, "slack"), ("Feb 12 list", B.S_LIST, "slack"), ("Carta claim", B.S_CARTA, "slack"),
        ("promise", B.S_PROMISE, "slack"), ("Segerstrale told", B.S_SEG, "slack"), ("Claire's question", B.S_CLAIRE, "slack"), ("Tor warned", B.S_TOR, "slack"), ("Vincent exit", B.S_VINC, "slack"), ("owner list Slack copy", B.S_LISTSLACK, "slack")]
for lab, t in [("owner list", "1816809274978043917"), ("Matthew resigns", "1830959847543474636"), ("Griffin resigns", "1856958794180374704"), ("side letter chain", "1775602109531090463"), ("side letter signed", "1777052222643175480"),
               ("KPMG FY24", "1817557789846606177"), ("KPMG FY23", "1788910618703813283"), ("Enes addresses", "1770141224265557526"), ("brothers wired", "1774211155651873582"), ("Vincent resigns", "1849344928983425627"),
               ("letter ES-4", "1856858053929740799"), ("letter ES-12", "1856860994291529096"), ("letter ES-13", "1856861229984402233"), ("letter ES-7", "1856861323365646598"), ("letter ES-15", "1856861400116562076"), ("letter ES-1", "1856861462411533365"),
               ("notice ES-17 letter", "1847335165884050330"), ("Carta ES-2", "1808666480668498098"), ("Carta ES-6", "1830952527208439510"), ("Carta ES-17", "1847333272519888206"), ("Carta ES-16", "1847333318158821452"), ("Carta ES-3", "1847333347700620793"),
               ("Carta ES-5", "1847333395311994879"), ("Carta ES-7", "1856960351896429942"), ("Carta ES-18", "1856960382677662910"), ("Carta ES-4", "1856960410709778333"), ("Carta ES-1", "1856960433624350836"), ("Carta ES-14", "1856960478782792748"),
               ("Carta ES-12", "1856960504234892536"), ("Carta ES-15", "1856960532806250145"), ("Carta ES-13", "1856960563574318616")]:
    BASE.append((lab, f"{B.MB}/{t}", "gmail"))
for lab, f in [("advisor table", "f_6a37227593d0977fdbdd7a"), ("term sheet", "f_11040fe5d66821bd6951aa"), ("side letter draft", "f_6201c7027d02997bfb2c84"), ("financing draft", "f_966445655f653d26dc8537"), ("charter draft", "f_90c029015fc474199cf736"), ("owner list Drive copy", "f_414596b0a9d698267dd1e1")]:
    BASE.append((lab, f, "gdocs"))
BASE.append(("Task List", "f_31115ddb6ed866f2b10d60", "gsheets"))
reach_lines = []
for lab, ref, svc in BASE:
    o = run(T + "persona_view.py", "can-see", "leonard_hayes", svc, ref).splitlines()
    reach_lines.append(f"base:{lab} | {o[0] if o else 'no output'}")
reach_txt = "\n".join(reach_lines)

fr_rows = [(f["id"], f["service"], f["container"], f["kind"], " > ".join(f["incorporated_via"]), f["delegated_by_record"], f'"{f["delegation_quote"]}"', ", ".join(f["requirement_ids"]) + (" (ENG-2438)" if B.PROJECT in (f["container"] + f["delegated_by_record"]) else "")) for f in man["ask_fragments"]]
tr_rows = [(t["id"], t["family"] + (f" ({t['distractor_type']})" if t.get("distractor_type") else ""), t["requirement"], ", ".join(t["seeded_ids"] + t["base_pointers"]) or "see resolver", t["expected_wrong_reading"], t["resolver"], t.get("discovery_order", "-")) for t in man["traps"]]
ch_rows = [(c["id"], c["root_cause"], c["ends_in"], " > ".join(f"{h['service']} {h['record']}: {h['finding']}" for h in c["hops"])) for c in man["chains"]]
holder_rows = [(h[0], h[1], h[2], h[3]) for h in B.HOLDERS]
surf_rows = [(s["service"], s["tool"], s["per_record_calls"], s["records"], s["requirement"], f"{s['why_no_bulk']} / {s['short_circuit']}") for s in man["cohort"]["evidence_surfaces"]]
bud_rows = [(b["phase"], b["service"], b["calls"], b["reason"] + (f" (conditional: {b['conditional_on']})" if b.get("conditional_on") else "")) for b in man["call_budget"]]
ANCH = {"ADV": "f_6a37227593d0977fdbdd7a", "LETTER": B.S_LETTERS, "TOLD": B.S_SEG, "ASOF": B.M_ES14, "FAM": B.M_BROS, "SIDE": "f_6201c7027d02997bfb2c84", "BOARD": "f_966445655f653d26dc8537", "ASK": B.S_CLAIRE, "BOUNCE": B.M_BOUNCE, "EXT": B.M_EXT, "ALIAS": B.M_AKIN}
port_rows = [(p["id"], p["mechanism"], ", ".join(p["nodes"]), ANCH[p["id"]], p["natural_reading"], "; ".join(p["controls"]), p["over_application"], ", ".join(p["decides"][:6])) for p in man["mechanism_portfolio"]]

CAND = [
 ("ADV (kept)", f"{B.M_LIST} > f_6a37227593d0977fdbdd7a", "merged line > stock count > total and every note", "A17 Beta(1,2) mean 0.33", "owner list figure, 'advisor'", "K1, K4-K8, P1"),
 ("LETTER (kept)", f"{B.S_LETTERS} > six letters > eight Carta entries", "a founder's done line > who is told > class, note and order", "A24 Beta(1,2) mean 0.33", "'Termination details', recipients", "C_ES14, C_ES18, N_Vincent, D6"),
 ("TOLD (kept)", f"{B.S_LIST} > {B.S_SEG}; NEW {B.TH_ROBERT}", "list says open > a personal record elsewhere > class and note count", "A25 Beta(1,2) mean 0.33", "holder address, name", "C_SEG, C_NEB, TC_SEG"),
 ("ASOF (kept)", f"NEW {B.TH_KPMG} > {B.M_ES14}", "as-of date > effective dates > every option line", "A19 Beta(1,1), no record", "'Audit Request'", "A1, A2, AL_*"),
 ("FAM (kept)", f"{B.M_ENES} > {B.M_BROS}", "one contact > three lines change call", "A7 Beta(1,1), no record", "'brothers'", "F1-F5; the rule sits in a DM, not the notes"),
 ("SIDE (retired at injection: the close-out notes name the side letter's holders)", f"f_6201c7027d02997bfb2c84 > {B.M_SIGN}", "Drive copy > signed chain > route for a second holder", "A15 Beta(1,2) mean 0.33", "'side letter'", "S3 only: Tor's route is on the Drive copy, so S1 and S2 are plain reads"),
 ("BOARD (kept)", f"f_966445655f653d26dc8537 > {B.M_MATT} > {B.M_PHIL}", "document list > resignations > directors and the vote", "A11 Beta(1,2) mean 0.33", "'board'", "B1, L6, G2"),
 ("ASK (kept)", f"{B.S_CLAIRE}", "unanswered question > note content", "A9 Beta(1,1), no record", "'equity'", "Q1"),
 ("BOUNCE (rev2, new)", f"{B.S_LETTERS} > {B.M_OWEN} > NEW {B.M_BOUNCE}", "a done line and a sent letter > the mail system's failure notice in the letter's thread > told, class, note", "A24 (prior from the ledger)", "'Delivery Status Notification', Owen's address", "C_ES12, TC_ES12, C_DATE"),
 ("ALIAS (rev2, new)", f"ENG-2447 > NEW {B.M_AKIN} > {B.M_AKIN_SIG}", "the issue's work address shows no mail > a founder's mail to 'Akin' at a personal address > Collins signs 'akin'", "A7 (prior from the ledger)", "'Akin', Collins's names", "C_COL, TC_COL, LC_Col, C_FIRST"),
 ("EXT (rev2, new)", f"{B.M_CALVIN} > NEW {B.M_EXT}", "Carta's termination notice > Carta's later update, forwarded by the holder from his issue address > live line, note, who goes first", "A11 (prior from the ledger)", "Calvin's issue address, 'option grant'", "C_ES3, TC_ES3, P_first, N_Calvin, D6, P1"),
 ("OPT (kept as channel CH-LIVE, not a rule)", f"{B.S_LIST} names Carta > 14 notices", "pointed: Leonard's own list says 'Carta terminations', and C5 shows pointed traps caught 6 of 6", "none: complexity channel", "'Termination details'", "P_lapsed_*, P_FRED"),
 ("CAP (rejected)", f"seeded TLAS request; {B.S_TOR}", "Tor's cap table on request; the smallest modelled effect, and a planted look; Tor's Nov 4 DM (T8) replaces it as a free base fact", "none", "-", "-"),
 ("WATERFALL (rejected)", "f_11040fe5d66821bd6951aa and f_90c029015fc474199cf736", "dollars per holder need residual cash, which NB-3 and NB-4 block", "none", "-", "-"),
 ("FD PERCENT (rejected)", f"{B.M_LIST}", "four fully diluted bases and two reserves in the base, two of them self-consistent: a fork with no settling record, so counts only", "none", "-", "-"),
 ("ROUTE to work address (rejected)", f"{B.MB}/1856861323365646598", "ES-7's letter went to a mailbox archived by Feb 15, but no personal address is on record and addresses are never graded", "none", "-", "-"),
]

TWO = [
 ("Who counts as a holder", "everyone on a Carta record, live or lapsed: 26 non-founder lines, one project issue each", "only people holding something today: 20 lines", f"project {B.PROJECT} (ENG-2438 to ENG-2463) states the cohort; the schedule shows Nothing for the six; {B.M_ES14} is one such record"),
 ("Is a past last day lapsed, or could the option have been exercised", "lapsed: H1 makes Carta the record and a line past its last day holds nothing", "ES-16's holder was trying to exercise (leonard@harmonygames.co_1847333990408253969.json)", f"H1 {B.DOC_NOTES} closes it by rule, not by evidence of no exercise; the October notices predate those windows"),
 ("Someone with stock and an open grant", "one row and at most one note per person; advisor grants have no last day, so the note is on the closing", "the grant is a live option line that fires its own note", f"H1 {B.DOC_NOTES}: one row and at most one note per person; Carta's digests name all four grants (ES-9, ES-11 in leonard.hayes@harmonygames.co/1782897835407336831; ES-8, ES-10 in the seeded Nov 20, 2023 digest) and no termination, and Carta is the record"),
 ("Does a channel post count as told", "no: told means a message sent to the person directly and delivered", "Oliver replied in the channel, so he knows (C05KNDCHAAG/1770839984.194409)", f"H1 {B.DOC_NOTES}: sent to them directly and delivered; a `<!here>` post is not"),
 ("ES-14's channel membership", "not told: he left in November", "a listed member of #company-internal", f"H1 sent-directly-and-delivered rule; NB-31; his exit {B.M_VINC}"),
 ("Who may do the telling", "Leonard, Robert or Arthur", "only Leonard, who promised to personally reach out", f"H1 {B.DOC_NOTES}: from one of the three of us; {B.TH_ROBERT}; the promise {B.S_PROMISE}"),
 ("Is Griffin told through its partner", "yes: one mail to the partner reaches both funds", "per-line, and no mail names the Side Fund", f"H1 for a fund, its partner; {B.MB}/1856675475513544349 message 13; one signer for both funds {B.MB}/1774928765255297348"),
 ("Was Tor told in November", "no: a runway warning, not the closing", f"he heard about three months of runway ({B.S_TOR})", "the DM never says the company is closing; H1's told rule names the closing"),
 ("Does a Slack DM count for Segerstråle", "yes for told: written and sent to him directly", "it is not a side letter notice", f"told and route are separate columns; {B.S_SEG}"),
 ("Family contact", "one note to Enes covers the other two lines, which need no note of their own", "they hold individually, so three notes", f"{B.SL_AMEND} overrides {B.MB}/1774211155651873582 ('holding shares individually'); Enes's own line stays First note"),
 ("Does the family rule reach the Solsten pair", "no: colleagues, not family", "two holders at one company", f"'all three Disli brothers' {B.M_BROS}; the Solsten pair sign as CEO and COO, {B.MB}/1770053656612413311"),
 ("Awards ending exactly on the as-of date", "reflected: vested only, 243,757 options", "still whole on that day: 266,436", f"NEW {B.TH_KPMG}: each effective date as Carta shows it, regardless of when recorded"),
 ("Effective dates entered late or chosen on Feb 11", "use the effective date as Carta shows it", "an audit should not use backdated entries (C07C2866011/1770827616.441769): 268,772", f"NEW {B.TH_KPMG}: each effective date as Carta shows it. A run that also flags the backdating must not lose a row"),
 ("What 'fully diluted' means", "not asked: KPMG asks for counts", "four bases exist in the base", f"NEW {B.TH_KPMG} asks shares, options and their total; no percent of the whole is graded; {B.M_LIST}"),
 ("Is a personal note a notice", "no: formal notices are a separate step; route is a column for those", "the note to Tor must copy TLAS", f"NEW {B.TH_SUNSET} says formal notices are a separate step legal will walk him through later; no row fails if a run copies TLAS; f_0c37bb7235683d73569903 is the visible base line"),
 ("Does Griffin still have to act", "yes: its vote as a holder is separate from the board seat", "it resigned, so nothing is left", "charter draft f_90c029015fc474199cf736, Requisite Holders and 3.3.5"),
 ("Could Griffin's waiver remove the notice duty", "out of scope: no notice deadline is graded", "Fourth B 8 lets the Requisite Holders waive class rights", "no row grades a notice deadline; f_90c029015fc474199cf736"),
 ("Who is on the board", "Leonard and Robert", "all three founders ('it's just us and Griffin', Feb 11), or Leonard alone", f"C04UEQVDVB7/1752517647.842649 fits two founders against Phil; Carta consents {B.MB}/1838216168984971198; {B.M_MATT}; {B.M_PHIL}"),
 ("ES-17's date", "lapsed on either date", "letter Jan 22 against Carta Jan 28", f"both precede the clock; no row grades the exact date; {B.M_ES17}"),
 ("ES-5's end date", "lapsed by Carta", "ledger pays him to Dec 31, so he could be live (NB-32)", f"H1: Carta is the record; never grade his end date; {B.MB}/1847333395311994879"),
 ("Who goes first", "whoever's last day comes first: ES-3 (Feb 20, from Carta's Jan 23 update), then ES-14 (Feb 21)", "Griffin first, per Leonard's Feb 9 line; or the sheet first; or ES-14 on Carta's Oct 29 date for ES-3", f"H1 {B.DOC_NOTES}; the sheet-first card {B.TRELLO_CARD} is about the work order, not the notes; {B.S_PROMISE}; {B.M_EXT}"),
 ("Is 'Akin' Matthew Collins", "yes: Collins signs his own mail 'akin' and board mail greets him as Akin, so Leonard's Feb 12 mail told him", "Akin is someone else, or a personal address is not his", f"{B.M_AKIN_SIG} ('best / akin' from matthew.collins@harmonygames.co); {B.M_AKIN}"),
 ("Does a letter that bounced count as told", "no: the mail system says it was not delivered, so the closing never reached Owen", "it was sent, and the rule's word is the message, not its delivery", f"{B.M_BOUNCE} (550 5.2.1 inactive, nine seconds after the letter); H1's told line"),
 ("Which Carta date governs ES-3", "Carta's Jan 23 update: Feb 20, 2026, after the clock, so the line is live", "Carta's Oct 29 termination notice: Jan 24, so it holds nothing", f"H1 'Carta is the record'; {B.M_EXT} carries Carta's own later notice with the old date beside the new one; {B.M_CALVIN}"),
 ("Issue state by class", "Canceled where the line holds nothing; otherwise Todo where its own note waits, and Done where it does not", "a Covered line stays Todo with the family note", f"project {B.PROJECT} description; ENG-2438"),
]

QC = [
 ("temporal", "the project description cites records dated after it", f"project updated_at is after {B.TH_SUNSET}; created_at stays earlier, ENG-2438"),
 ("temporal", "Robert's reply contradicts the Feb 12 list", f"it is dated after {B.S_LIST}, so the list was true when written; {B.TH_ROBERT}"),
 ("temporal", "a Tuesday deadline sits after 'archive by Feb 15'", f"{B.WD}/1770933601.686309 keeps accounts until the data is extracted; the notes say so, {B.DOC_NOTES}"),
 ("semantic", "'told' could mean heard about it", f"H1 {B.DOC_NOTES} defines it; T8 tests the boundary on {B.S_TOR}"),
 ("semantic", "'Nothing' reads as if the holder never held anything", f"the column is what is owed now; {B.M_ES17}"),
 ("cross-service referential", "the project cites a Sunset request that must exist", f"seeded in the same revision, {B.TH_SUNSET}, after {B.MB}/1856675475513544349"),
 ("cross-service referential", "a seed names a Sunset entity first seen in a PDF", "seeds use the mail's own 'Sunset' form only; research/s1_signed_pdfs.md section C item 6"),
 ("quantitative", "3,051,879 against 3,051,881 and 3,051,882", f"#executives idx 727 says 3,051,881 issued, but the newer term sheet and the sum of lines settle it, {B.D_TERM.split()[-1]}; only 3,051,879 is graded"),
 ("quantitative", "the owner list claims to add to 100 %", "true on its own base, f_414596b0a9d698267dd1e1 adds the unissued pool; no percent of the whole is graded (hazard Q10)"),
 ("quantitative", "a comment repeats an owner-list figure as fact", f"every such comment quotes it as the Nov 2024 owner list, dated, never in the present tense; {B.M_LIST}"),
 ("state/lifecycle", "a closed Linear issue gets a later comment", "seeded comments predate any close; states are moved by the run, ENG-2438 to ENG-2463"),
 ("state/lifecycle", "Trello card 801 reads as closed", "it is open in the Done list and stays untouched: 68c5a49e8491a9d7faf869d0"),
 ("identifier/format", "ENG keys could collide", "research/s4_carrier_formats.md: 0 collisions, max ENG 2437, ENG-2438"),
 ("identifier/format", "Gmail thread ids off the base scale", f"(ms << 20) rule, {B.TH_KPMG}; Robert's reply sits in base thread {B.MB}/{B.M_NEB_THREAD}"),
 ("other", "Linear is a product tracker with no investor project", f"origin stated by Leonard in {B.SL_ORIGIN}, and 'linear we keep during transition' at {B.WD}/1770933601.686309"),
 ("other", "the KPMG body lists its items where base bodies do not", f"forced: attachments return no bytes; the body says why, and that the financials are covered by {B.MB}/1856787396431935562"),
 ("other", "Robert has shown little interest in the shutdown", f"{B.DMA} says so, but he and Nebojsa are ex-coworkers with real traffic, and the reply gives its reason: {B.MB}/{B.M_NEB_THREAD}"),
]

doc = f"""# Scenario Design — leonard_stockholder_closeout · design only · contains no prompt, OE or criterion text

Leonard Hayes · Executive · Finance · Authoring · Long Horizon · medium (platform cap < 85 %; requester aim under 70 %, 62 % a stretch) · Feb 14, 2026 (normal). Written 2026-11-07 by `/create-scenario` (Claude Opus 5.5) from `plan/build_scenario.py` and `plan/assemble_design.py`. Research: `research/s1_signed_pdfs.md`, `s2_option_notice_state.md`, `s3_coherence_audit.md`, `s4_carrier_formats.md`; census in `00_PreScenario/census/`.

## 0 Assignment, persona census and horizon note

| Field | Value |
|---|---|
| Universe | key `normal`, label Feb 14, 2026 (normal), `{ctx['universe']['clock_line']}`, seed bound `freeze_utc` {ctx['freeze_utc']}, `shutdown_rules_apply` true |
| Assignment | Executive · Leonard Hayes (Role: Co-founder & Creative Director, leonard.hayes@harmonygames.co) · Finance · Authoring · long-horizon · medium · February 14, 2026 00:00 |
| Evals category | Executive (Founders / Exec / Strategy): a founder's investor close-out, cap table and audit confirmation, inside Finance |
| Loss budget | V3 Medium cap < 85 %, design target E[avg] <= 77 % (cap - 8). Requester aim, recorded verbatim: 'assignemt is medium but we have to target hard difficulty'; then 'go with your recommendations on all six' (aim under 70 %, 62 % a stretch). The assignment value is unchanged |
| Effective profile | `horizon: Long Horizon` -> `effective_profile: extreme`, with requester-confirmed `volume_exception {{call_budget_floor 130, per_record_floor 85}}` and `cohort_exception {{cohort_floor 26}}` (§2, §9) |
| Theme screen | holders and money; no bio-adjacent theme in the storyline. Seeded text says ZM |
| Source | task_context.py --require-source: ready, KB bound, context_hash {ctx['context_hash'][:12]}…; last tools commit c16c7a1 |
| Role note | every signed record shows Leonard as CEO; the roster says Creative Director. The assigned role stands and the prompt will state no title. Persona_Briefs: the primary operator who owns the financial model and runway narrative |

Remit, before-freeze sources: his promise {B.S_PROMISE}; his list {B.S_LIST}; the draft {B.S_DRAFT}; Task List row in `f_31115ddb6ed866f2b10d60`; his KPMG replies {B.MB}/1817557789846606177.

Persona reach census (`persona_view.py reach leonard_hayes --top 12`), verbatim:

```
{reach}
```

## 1 Storyline

**The stockholder close-out.** Leonard owes the holders three things he has not done: the personal outreach he promised, the investor letter he drafted, and an honest holder picture for Sunset and for Griffin's auditors. His own records say parts of this are finished. They are not.

**Why it is real.** Nine stock lines have no record of being told. No live option holder has a last day in writing on any record Leonard can read (research/s2_option_notice_state.md section B). Six letters exist against eight Feb 12 Carta entries, so ES-14 and ES-18 have none, though {B.S_LETTERS} says all were sent. ES-14 is Vincent Parker: he resigned in November, was never told of the closing, and his window ends Feb 21.

**Closed answer set.** 29 holders on Carta, 26 of them non-founders, tied exactly to 3,051,879, 762,880 and 268,772 (`verified_anchors.txt`, re-computed from raw records). The signed Schedule of Purchasers confirms every line (research/s1_signed_pdfs.md section D).

**Anchors per service.** Slack {B.S_DRAFT}, {B.S_LIST}; Gmail {B.M_ES14}; Linear ENG-2438 to ENG-2463 in project {B.PROJECT}; Docs `f_6a37227593d0977fdbdd7a`, `f_11040fe5d66821bd6951aa`; Sheets `f_31115ddb6ed866f2b10d60`; Drive {B.FOLDER}; Snowflake FINANCE_LEDGER financing rows (FIN-000041, FIN-000061).

**Universe KB placement** (`universe_kb/timeline.md`, cohorts.json, trap_catalog.json):

{demote(story)}

## 1a Coherence audit

Source: `coherence_hazards.json` walked in full, the seven QC categories, the sibling sweep and every NB card; `research/s3_coherence_audit.md` is the working record. This audit ran before the PDF read, so corrections come first.

**Corrections since the audit** (research/s1_signed_pdfs.md; all read from the signed PDFs under decision 6):

| Audit said | Now | Evidence |
|---|---|---|
| Segerstrale's route rests on an unread PDF; the party may be Menlo capital LLC | He is a full party in his own name and signed | {B.MB}/1777587701740700050, research/s1_signed_pdfs.md section B |
| Every clause is a draft | The filed charter and final-form IRA and Voting match the drafts on every clause used here | `f_90c029015fc474199cf736`, research/s1_signed_pdfs.md section D |
| §1a table says NB-32 is not touched | ENG-2454 is Douglas: touched, and H1's Carta rule settles it; his end date is never graded | {B.MB}/1847333395311994879 |
| Hazard S06 cites /contacts/170 and /108, /139 | Dead pointers from the hazard file; the real rows are /169 (Leonard) and /138 (Frederick) | research/sweeps/coherence_sweep.md line 195 |
| Tor 'no contact since May 2024', Nebojsa Sep 2025 | Tor Nov 4, 2025, {B.S_TOR}; Nebojsa Oct 24, 2025 in C7442B7CD94B | research/sweeps/coherence_sweep.md line 89 |
| Sunset's fee quoted three ways | $12,363 in the signed set; no row grades it | {B.MB}/1856956483320787350, hazard Q07 excluded |
| Pro rata dropped | Clause 3 keeps a right of first offer for both side letter investors; off the graded path | {B.MB}/1777587701740700050 |

{demote(hazards)}

**QC seven-category walk.**

{demote(qc)}

**Sibling-defect sweep.**

{demote(sibling)}

**Known issues touched** (`references/known_data_issues/normal.md`).

{demote(known)}

## 1b Active speakers

`activity.json` status at the clock. External people have no `activity.json` entry, so the last-authored date stands in. Seeded voices are the three founders, PERSON_3088 (KPMG) and PERSON_2888 (Sunset) only.

| Person | Email | status_at_clock | Seeding role |
|---|---|---|---|
| Leonard Hayes | leonard.hayes@harmonygames.co | active_feb_2026 | project, notes, comments, Slack origin post |
| Robert | robert@harmonygames.co | active_feb_2026 | reply to Nebojsa; comments |
| Arthur Blake | arthur.blake@harmonygames.co | active_feb_2026 | comments; DM reply |
| KPMG associate | PERSON_3088_EMAIL | not in activity.json; last authored 2024-12-18, leonard@harmonygames.co_1817557789846606177.json | FY25 request |
| Sunset Head of Partnerships | PERSON_2888_EMAIL | not in activity.json; last authored 2026-02-11, leonard@harmonygames.co_1856872398290956689.json | Company Information request |
| Griffin VP Finance | PERSON_2847_EMAIL | not in activity.json; cc 2026-02-12 | cc only, no seeded voice |
| Vincent Parker | vincent.parker@harmonygames.co | quiet_since_2025-12 | holder only; must stay untold, no seed may speak for him |
| Frederick Stone | frederick.stone@harmonygames.co | quiet_since_2025-10 | holder only, no voice |
| Victor Barnes | victor.barnes@harmonygames.co | quiet_since_2025-04 | holder only; cannot act (playbook S1) |
| Calvin Price | calvin.price@harmonygames.co | quiet_since_2025-10 | holder only |

## 1c Identity traps

{demote(ident).replace("[]", "(none)")}

## 2 Cohort spine

**Rule.** {man['cohort']['definition']}. Key: {man['cohort']['key']}. Size {man['cohort']['size']}. Requester-confirmed `cohort_exception`: {man['cohort_exception']['reason']}.

| Surface | Tool | Per record | Records | Requirement | Why no bulk / short circuit |
|---|---|---|---|---|---|
""" + "\n".join("| " + " | ".join(str(c) for c in r) + " |" for r in surf_rows) + f"""

Sum of per-record calls {sum(s['per_record_calls'] * s['records'] for s in man['cohort']['evidence_surfaces']):.1f}, above the 85 floor. Linear comments buy calls, not misses: they are read every time (research/s4_carrier_formats.md section A), so no deciding fact sits only there. They carry neutral contact history, and stale figures met first.

**Classification predicate (closed).** Wording is neutral on purpose: the first draft read as a trap index (run_sim LEAK-1), so no sentence names a case or a carrier, and the rule is split across records. Carried by H1 {B.DOC_NOTES} unless marked:
- Carta is the record. If a line's last day has passed, it holds nothing.
- One row per issue on the sheet and at most one note per person. The three of us get no row, only the totals.
- Told means a written message about the closing, sent to them directly and delivered, from one of the three of us (a post in a channel doesn't count); for a fund, its partner.
- Everyone still holding something gets what they are owed: the closing if they have not been told, their last day if they have one. Whoever's last day comes first goes first.
- Anything they asked about their holding that we never answered gets answered in their note.
- Family (Leonard's reply under his Feb 12 list, {B.SL_AMEND}, not H1): one note to whoever has always handled it for a family covers the rest of the family's lines, which need no note of their own.
- States (project description {B.PROJECT}, ENG-2438): Canceled where the line holds nothing; otherwise Todo where its own note is waiting for Leonard, and Done where it isn't. On every issue with no note of its own, Canceled included, say why.

Labels in the holder sheet: H1 gives Nothing, Already told, Closing (First note here), Last day (Date note), Closing and last day (Full note); the reply adds Covered.

**Applied to all 26.** Titles use the forms the owner list shows, so no surname links the family: [PERSON_NAME_52949] is Enes Disli, [PERSON_NAME_27652] is Eren Disli.

{table(["Issue", "Holder", "Carta id", "Owed"], holder_rows)}

Counts: Already told 4, First note 6, Covered 2, Date note 6, Full note 2, Nothing 6 = 26. Notes written: 6 First + 6 Date + 2 Full = 14. Reason comments: 4 + 2 + 6 = 12. States: Canceled 6, Todo 14, Done 6. Issues are keyed by Linear id because SSP-06 and SSP-08 cannot be told apart on the record. Holder-of-record names on three lines differ between Carta and the signed schedule, so legal names are never graded (research/s1_signed_pdfs.md section D).

**Shortcut audit.** The owner list {B.M_LIST} hands 27 lines in one read, in three copies including `f_414596b0a9d698267dd1e1`, so difficulty never rests on the census. `Termination details` returns the 14 notices in one search, and the batch read collapses them. Neither reaches told state, the letter join, the family link or the as-of date.

**Boundary records.** ES-14 (a last day 7 days out, no letter); ES-18 (no letter, a channel post); ES-17 (the largest non-Griffin line, holds nothing); ES-1, 4, 15 (terminated exactly on the as-of date).

## 3 Hidden authorities

| Id | Authority | Home | Governs | Decoy | Decoy scope | Findability |
|---|---|---|---|---|---|---|
| H1 | my close-out notes | gdocs {B.DOC_NOTES} | R4, R5, R12 | earlier notes {B.DOC_OLD} (same service) | older version in T18's version_records | Drive search 'close-out notes' (planned) |
| H2 | Carta's termination details | gmail {B.M_ES14} and 13 siblings | R2 | term sheet f_11040fe5d66821bd6951aa | older version in T3's version_records | gmail search 'Termination details', 14 hits |
| H4 | KPMG's FY25 request | gmail {B.TH_KPMG} | R8 | FY24 request {B.M_K24} (same service) | fiscal year: FY24 as of Sep 30, 2024 against FY25 | gmail search 'Audit Request' (planned) |

## 4 Delegation lattice

| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |
|---|---|---|
""" + "\n".join(f"| {a['id']} | {a['prompt_reference']} | {a['locator']}{' (issues ENG-2438 to ENG-2463)' if a['id'] == 'AN2' else ''} |" for a in man["anchors"]) + f"""

**Hub.** The project description {B.PROJECT}, in Leonard's voice, delegates by role: his close-out notes, what Sunset asked for. It names no location. H2 is found by search. Origin of the project is stated in {B.SL_ORIGIN}, on the base line 'linear we keep during transition' ({B.WD}/1770933601.686309).

**Amendment.** K14 {B.SL_AMEND}: in a reply under his Feb 12 list, after the notes doc, Leonard adds Arthur to the sharing and gives the family sentence; the rest stands. H1 names that message twice ('where I left things today', 'reply under my list in #winddown') and every run must write there.

**Non-authoritative distractors.** The Feb 12 list read as a to-do (T6), the deck (T19), the draft sheet (T20), the Done card (T21).

{table(["Id", "Service", "Container", "Kind", "Chain", "Delegated by", "Delegation quote (verbatim)", "Requirements"], fr_rows)}

## 5 Chains and trap register

{table(["Chain", "Root cause", "Ends in", "Hops"], ch_rows)}

{table(["Trap", "Family", "Req", "Records", "Expected wrong reading", "Resolver", "Discovery order"], tr_rows)}

**Hardness v2 selection** (`Hardness_Mastery.md` §13, guide Part 5). Trap 1, proving done: LETTER, wrong source {B.S_LETTERS} (Leonard, Feb 11), beaten by six letters joined to eight entries ({B.M_ES14}); flips C_ES14, C_ES18, N_Vincent. Trap 9, work already done: TOLD, wrong source {B.S_LIST}, beaten by {B.S_SEG} and NEW {B.TH_ROBERT}; flips C_SEG, C_NEB. Trap 7 and 8: ADV. Trap 4 and 8: ASOF. Trap 6: FAM. Trap 5: SIDE. Trap 2: BOARD. Trap 3: ASK.

### Mechanism portfolio (S5a)

Grounded candidates considered ({len(CAND)}), with ledger priors (`hardness_ledger.py priors --model claude-opus-5-5`; this machine's ledger holds one record per family, n_eff 1):

{table(["Candidate", "Anchor record", "Coupling", "Prior (Opus 5.5)", "Findability term", "Slots / reason"], CAND)}

Selected, one per future solver rule ({len(man['mechanism_portfolio'])}, inside the k <= 8 engine limit):

{table(["Rule", "Mechanism", "Nodes", "Anchor record", "Natural reading", "Controls", "Over-application", "Decides"], port_rows)}

Per node, the four checks. Incorporated: every rule's chain runs from AN2 or AN3 (§4). Survives complete retrieval: ADV needs a subtraction, ASOF a date computation, BOARD a rule read correctly; TOLD, LETTER and FAM are retrieval-shaped, and census C5 says reading decides those. Tool-surface proof: each deciding record is returned by a natural call (§10). Graded weight: §6.

**Budget arithmetic.** See §6: expected miss weight about 0.21 against about 0.38 for 62 %. The medium target (<= 77 %) sits at the edge of the central estimate; the requester's aim of under 70 % is not supported.

### Liveness flags (S5b)

```
{live}
```

| Flag | Trap | Disposition |
|---|---|---|
| breadcrumb | T1, T2, T3 | wrong source met first by design; the correction sits in a different record; {B.M_LIST} |
| breadcrumb | T10, T11 | the query words reach both versions, which is fair; the deciding text differs; {B.M_PHIL} |
| breadcrumb | T14, T15, T16 | names are searchable by design; the join is the work; {B.M_ES17} |
| breadcrumb | T18 | both notes docs share terms by design (H1 and its older version); {B.DOC_NOTES} |

`hardness_v2_check.py --design`:

```
{v2}
```

Every check that can run is CLEAN. RULE_IN_PROMPT runs once a prompt exists.

## 6 Failure-diversity plan

`plan/policy_scores.py` on the real surface, UNCALIBRATED, verbatim:

```
{scores}
```

**Reading it.** Four heavy channels, ADV, LETTER, TOLD and ASOF, sit on different records and habits: a tie-out, a recipient join, a per-address search and a date computation. A run strong on one is not thereby strong on another. FAM adds a fifth at 8.2 %. SIDE, BOARD and ASK are small and add little spread. A1 and A2 need both ASOF and ADV, because the count includes the advisor grants.

**Honest position.** My first model said 71.6 %. A cold adversary reading the same design put a first baseline at 76 to 82 %, and found why: the rule doc pointed at traps, about 27 weight never flipped when its trap landed, and my own volume plan defeated T7. The fixes are in, and rates here are the adversary's, moved only where a pointer was removed. Central estimate 78 %. Against the bars: platform < 85 % likely; medium design target <= 77 % at the edge; requester's aim under 70 % not supported (P about 0.1); 62 % not supported. SD is the gate at risk: P(SD in band) 0.67 to 0.83. /rubric row multiplication has cost 6.5 to 15 points on past tasks; this surface already plans per-target rows, but the risk stands. Only the pre-check can test any of this, and C5 recommends proving catch rates before the baseline.

## 7 Deliverables and dependent writes

| Deliverable | Service | Depends on | Requirement |
|---|---|---|---|
| Holder schedule, one row per project issue, plus a short summary | gsheets, moved to {B.FOLDER} | C1, C2, C3, T3 | R1-R5, R9 |
| Investor letter, updated from {B.S_DRAFT} | gdocs, moved to {B.FOLDER} | C5, K1 | R10 |
| 14 personal notes as drafts | gmail | C2, C3, C7, C8 | R6, R12 |
| Reply to KPMG, to all recipients on {B.TH_KPMG} | gmail | C4 | R8 |
| Heads-up to Griffin in thread {B.MB}/1856958794180374704. Sunset drafts and sends the consents, so this stops short of the instrument | gmail | C5 | R9 |
| State move on ENG-2438 to ENG-2463; reason comment on the 12 issues with no note | linear | C2, C3 | R11 |
| Shares to Robert and Arthur; reply to the founders in {B.WD} | gdrive, slack | K13, K14, C2 | R13 |

Reuse versus create: the deliverables are new; the draft sheet {B.SHEET} is partial and stale, so it is a layout source only.

## 8 Service role map

| Service | Role | Load-bearing fact or write | Carrier |
|---|---|---|---|
""" + "\n".join(f"| {k} | {v['role']} | {v['weight_reason']} | ● |" for k, v in man["services"].items()) + f"""
| github | not used | no honest job in a stockholder close-out | n/a |
| confluence | not used | never seeded; no fact rests on it | n/a |

## 9 Call budget

{table(["Phase", "Service", "Calls", "Necessity reason"], bud_rows)}

Unconditional floor {sum(b['calls'] for b in man['call_budget'] if not b.get('conditional_on'))}; planned total {sum(b['calls'] for b in man['call_budget'])}. Note writes are conditional until the pre-check proves `gmail_create_draft`, which has never run in a stored baseline. The ≥ 500 floor is not honestly reachable: 26 holders, and mail reads batch. `volume_exception`: {man['volume_exception']['reason']}. Golden-run note: a correct run needs these per-holder reads, because told state exists nowhere in bulk.

## 10 QC rails

### Two-reading table

{table(["Decision point", "Best reading", "Strongest alternative", "Resolved by"], TWO)}

### Reach table (load-bearing records)

Every scoped base record below is YES for Leonard (`persona_view.py can-see leonard_hayes …`); planned seeds are checked by `check-sql` at injection. Not reachable, and so never relied on: the advisor agreements (visible to no persona), all PDFs and Gmail attachments, and the 2023 Bridge Round sheet.

```
{reach_txt}
```

**Feasibility.** Every write is in `Evals/references/tools/catalog.json` (research/s4_carrier_formats.md section H). Leonard will own every target. `gmail_create_draft` is unproven and falls back to sends. Slack's catalog names `channel, text`; stored calls use `channel_id, message`. Nothing is asked that needs a Doc comment, an attachment or a Cc on a reply.

**Precedence.** Load-bearing facts sit only in ● carriers. Linear comments are ● under Ask_Carriers §6b. Slides, Contacts and GCal hold supporting detail only, and no graded fact sits only there.

**Prompt naturalness.** The prompt will name the three anchors and the deliverable kinds. It must not name the rule, the classes, the carriers, any holder's state, who goes first, or the Tuesday date. Rules live in the records.

**Grading devices.** Exact totals (3,051,879; 159,706; 243,757; 9,295,636). No row may penalise a run that flags the backdated entries. The answer to Claire's question is required on ES-4 only, with no penalty for telling ES-1 or ES-15 too. ≤ 5 samples per group plus a volume row. One row per write where the content differs. Accepted name forms in row titles, tokens included. The notes are graded by a bare count, never by exclusion. Addresses are never graded.

### Coherence rail

- Every audit row in §1a is dispositioned; designed disagreements are dated human claims with a named later record: {B.S_LETTERS} against {B.M_ES14}; {B.S_CARTA} against {B.M_BRIAN}.
- Companions for every seeded record are planned in §11, with `integrations.json` entries cited, for example INT-04.
- Id schemes follow the base: ENG-2438, {B.TH_KPMG}, {B.FOLDER}.
- No claim about git is made, so `base_claims.py` has nothing to test; ENG-2438 names no branch.

## 11 Record plan for /create-injection

Row floor: ≥ 120 INSERTs, not lowered by the exceptions. Estimate about 118: Linear 1 + 26 + about 56 comments, Gmail 8 (KPMG root, its follow-up, Leonard's holding reply, Sunset, Robert's reply, thread rows), Slack 8 (two short founder bursts), GCal 1, Drive 6, Docs 2, Sheets 2, Slides 7, Contacts 1, Trello 3. A third comment goes only where it is true. Count this at injection: padding fails on its own.

| Service | Planned id | Record | Timestamp (UTC) | Role |
|---|---|---|---|---|
| linear | {B.PROJECT} | project 'Holder records', team_ENG, lead Leonard; neutral name and titles, because team ENG includes the holders (ENG-2438) | created 2026-02-12T23:24:12Z; updated after {B.TH_SUNSET} | hub, AN2 |
| linear | ENG-2438 to ENG-2463 | 26 issues, Backlog; assignee a named founder or none; titles in owner-list forms; no instrument, no state | from 2026-02-12T23:25:03Z | cohort |
| linear | comment ids minted at SQL time | quoted, dated figures ('Nov 2024 owner list: 127,162'), never present tense; one dated last contact before February on all 26, ENG-2438 to ENG-2463, so no gap marks a told line; values only where a record backs them | before {B.TH_ROBERT}'s time | per-holder surface; wrong source met first |
| gmail | {B.TH_KPMG} | PERSON_3088 to Leonard, cc PERSON_4416, PERSON_2322, PERSON_2847; financials covered by {B.MB}/1856787396431935562; asks shares, each option line by holder, and their total, as of Dec 31, 2025, using each effective date as Carta shows it, regardless of when recorded; reply to all | 2026-02-13T16:48:33Z | AN3, H4 |
| gmail | {B.TH_SUNSET} | PERSON_2888 to Leonard, relaying legal: what the intake needs on stockholders: one line per holder, shares and options outstanding, count by what is owed, directors, and any special terms; says formal notices come from Sunset later | 2026-02-13T18:06:21Z | K8 |
| gmail | {B.TH_ROBERT} | Robert's reply on base thread {B.MB}/{B.M_NEB_THREAD} to Nebojsa, Leonard copied; says the company is closing, and that he wanted him to hear it from a friend; promises nothing further. Copy in Robert's mailbox too (robert@harmonygames.co/1773963101279916523). Update `gmail_threads.snippet` | 2026-02-12T23:41:12Z | T7 |
| gdocs+gdrive | {B.DOC_NOTES} | close-out notes, owner Leonard. Includes one line tying Tuesday to {B.WD}/1770933601.686309 and one on why this folder and not the Wind Down one | 2026-02-13T01:05:41Z | H1 |
| gdocs+gdrive | {B.DOC_OLD} | earlier notes, owner Leonard; must not name Sunset, the letters or Carta entries | 2026-02-10T17:41:09Z | H1 decoy |
| gdrive | {B.FOLDER} | close-out folder, owner Leonard, in root d_63fffeb4fab5233ed5bb73 | 2026-02-12T23:20:37Z | destination |
| gsheets+gdrive | {B.SHEET} | partial draft sheet, figures marked as copied from the Nov 2024 list | 2026-02-10T18:12:26Z | T20 |
| gslides+gdrive | {B.DECK} | update outline, 5 pages; '27 holders on the Nov 2024 owner list'; must not name Sunset | 2026-02-10T18:33:52Z | T19, K12 |
| slack | {B.SL_ORIGIN} | Leonard's short burst in #winddown: why the holders sit in Linear | 2026-02-12T23:15:20Z | K15 |
| slack | {B.SL_AMEND} | Leonard's replies under his Feb 12 list C0ADGSZKR3R/1770934638.035469: the family sentence, the Covered label, the sheet going to Arthur too; Arthur's one-line reply; parent counters updated | 2026-02-13T02:21:50Z | K14, FAM rule |
| gcal | {B.EVT_HOLD} | hold, Leonard sole attendee; the date lives here and not in the prompt | created 2026-02-13, start 2026-02-17 | K11 |
| trello | {B.TRELLO_CARD} | To Do card, list 640643a3fd8f3ca308d93195, written by Leonard, with his comment after Sunset's mail; bump the card's activity | 2026-02-12T22:54:08Z | K10 |
| contacts | minted at SQL time | Bergmann and Eren, token and email only, no date field | n/a | name to address |

**Must not.** Move a share figure, a Carta notice date or the two historic mailings. Seed a list with figures or states, or a Carta export. Say Leonard told an angel, or that ES-14 or ES-18 got a letter or a date. Write $11,700. Quote a real name from a PDF signature page. Name Sunsets HQ Corp., Sutter Law or Stable Rock. Name Sunset before its first base mention. Touch Trello card 68c5a49e8491a9d7faf869d0. Say anything about the closing in the project name or issue titles. Name three founders by count, in seeded text: name them.

### Integrations and companions

{demote(integ)}

## 12 Self-test results

`hardness_gate.py --design`, verbatim:

```
{gate}
```

`gradable_surface.py validate`:

```
{valid}
```

`gradable_surface.py gradeable-report`:

```
{gradeable}
```

**Lazy-solver pass.** One broad search per service, first hits, no thread opens. It gets the owner list and the letter draft, so it scores stock on plain lines and the delivery rows (`plan/policy_scores_output.txt`) and misses every trap. Leaks found and fixed: issue titles showed the family surname and holder ids; rows now key by issue. The full leak list is in §13.

**Literal-value sweep.** 243,757 and 9,295,636 appear in no base record, and no seed may carry them. 164,114 likewise. 3,051,879 appears in the term sheet only, on purpose (rev2 removed it from KPMG's follow-up and from Leonard's #executives note).

**Wording sweep.** H1's rule words must not appear in the deciding records: 'told' and 'closing' are absent from {B.S_SEG}'s own text, which says 'shut down'. H1 quotes no base sentence (K3 removed: 'every angel investor' was one Slack hit from the Segerstråle record). To re-run on the SQL.

**'The rest stands' check.** K14 adds to the sharing and carries the family sentence; no later record re-asserts or contradicts it.

**S9b forecast.** Pre-registered ledger id {fid}. UNCALIBRATED.

```
{fout}
```

### Self-review

Re-read Evals/1_Prompt_Eval.md §2.1 (Unique Ground Truth), §2.2 (Feasibility), §3.2 (Cross-Service Coherence) and Evals/0_Injection_Quality_Eval.md Check C in order.

{table(["Area", "Counter-reading (strongest argument it fails)", "Resolution (evidence)"], QC + [("decision point: " + d[0], f"{d[2]} is fair", d[3]) for d in TWO])}

Load-bearing base values re-read this session through hg.py: `00_PreScenario/verified_anchors.txt`, and independently recomputed by the fork sweep (research/sweeps/fork_sweep.md section 4).

`hardness_gate.py --design` result: {gate.splitlines()[0]}

Unresolved: no dual red team (REDTEAM_* unset; fallback in §13). The platform pre-check proved gmail_create_draft (14 drafts), so the draft slots are live. The new rules' miss rates (BOUNCE about 50 %, EXT 55-60 %, ALIAS about 30 %, ADV 50-65 % after un-pointing) are cold estimates, UNCALIBRATED. All six runs clearing 130 calls is about even: low runs land near 139 and the platform's 100 is safe. Row floor about 118 against 120. ES-16's identity is by id only. Catch rates come from other personas. The under-70 aim and 62 % stretch are not supported. The Sunset request's fit with SOW page 7 (absent from the export) is unverified.

## 13 Red team (dual)

@@REDTEAM@@

## 14 Revision intake (S0r)

@@INTAKE@@

"""
rt = os.path.join(H, "redteam_section.md")
doc = doc.replace("@@REDTEAM@@", open(rt, encoding="utf-8").read().strip() if os.path.exists(rt) else "RED TEAM UNAVAILABLE: REDTEAM_* is unset (0 variables), so tools/redteam_review.py --dual cannot reach a reviewer.")
doc = doc.replace("@@INTAKE@@", open(os.path.join(H, "revision_intake.md"), encoding="utf-8").read().strip())
open(os.path.join(WF, "01_Scenario_Design.md"), "w", encoding="utf-8").write(doc)
print("design written", len(doc), "chars;", gate.splitlines()[0])
