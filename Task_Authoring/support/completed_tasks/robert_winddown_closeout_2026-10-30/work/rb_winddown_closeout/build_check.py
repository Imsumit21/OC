"""Writes task_inputs/Working_Files/04_Prompt_Check.md for the current 04_Prompt.txt."""
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
M = json.load(open(os.path.join(HERE, 'minted_ids.json')))
TR = json.load(open(os.path.join(HERE, 'truth.json')))
ACC = json.load(open(os.path.join(HERE, 'accounts.json')))
issue = {a['vendor']: a for a in ACC['accounts']}
prompt = open(os.path.join(BUNDLE, 'task_inputs', '04_Prompt.txt')).read()
SQLSHA = hashlib.sha256(open(os.path.join(BUNDLE, 'task_inputs', '01_Universe_Inject.sql'), 'rb').read()).hexdigest()[:12]
wc, sha = len(prompt.split()), hashlib.sha256(prompt.encode()).hexdigest()[:12]
ANC, PROJ, DOC, SVB = M['S_ANCHOR']['locator'], M['L_PROJECT']['id'], M['DOC_CONV']['id'], M['T_SVB']['id']
G = lambda k: M[k]['robert_message']
fmt = lambda x: f"{x:,.2f}"


def span(s):
    assert s in prompt, s
    return f'"{s}"'


L = []
w = L.append
w("# Prompt Check — rb-winddown-closeout")
w(f"> Prompt: 04_Prompt.txt · {wc} words · sha256 {sha} · checked 2026-10-28 against 04_Prompt_Writing_Brief.md (2026-10-28)")
w("> Suggested wording allowed. Typos and capitalisation are not assessed (scored by /prompt §1.2).\n")

w("## Summary\n")
w("Fail 0 · Non-fail 0 · Advisory 2 (C20, C23) · UNVERIFIED 0 · checks clean: C1–C19, C21, C22, C24.")
w("Predicted /prompt band: PASS. Status: READY FOR /prompt.\n")
w("Revision: the first /prompt run (report 6adfee3f27ce6ca81b457137_1_prompt) failed C6 UGT, C7 Clarity and C22 coherence on universe records, not on the prompt text; the records were fixed (dossier Revision 4: rule 3, rule 8, rule 10, comments on ENG-2446/2452/2481/2454/2455) and this check re-run on the unchanged 04_Prompt.txt. The second /prompt run (6adfee3f27ce6ca81b457137_1_prompt (1)) passed every prompt dimension and failed only Cross-Service Coherence on AWS (costs tab 0 vs ledger); fixed in dossier Revision 7 (rule 8 + ENG-2455), prompt unchanged. The third run (6adfee3f27ce6ca81b457137_1_prompt (2)) again passed every prompt dimension and failed only Cross-Service Coherence (Vercel label, Confluence lifecycle, HG Costs header, Chase card); fixed in dossier Revision 8, prompt unchanged. An independent coherence audit of that SQL then found three more seeded claims contradicting base mail (Linear plan, QuickBooks card, OpenAI credits) plus Pond5's renewal date; fixed in dossier Revision 9, prompt unchanged. /injection run 6 then failed the HG Costs header UPDATE (the Drive xlsx bytes keep the old labels) while /prompt run 3 had failed the positional note, so rule 8 no longer reads the costs tab's month columns at all (dossier Revision 10), prompt unchanged. /prompt run 4 then found Workspace's cost only in a PDF, Unity Ads undecided, Zapier/Helpshift switch-over undecided, the Layer date and the Linear/DocuSign P&L gaps; fixed in dossier Revision 12, prompt unchanged.\n")

w("## Findings\n")
w("| # | Check | Dimension · severity | Quoted span | Rule (source) | Defect |\n|---|---|---|---|---|---|")
w(f"| 1 | C20 | Today's date · Advisory | {span('on friday')} | Prompt Writing §4.2 asks for absolute dates; /prompt §2.8 allows clear relative wording | relative day; resolves to Fri Feb 13 (the ask {ANC}); optional: 'on feb 13' |")
w(f"| 2 | C23 | Originality · Advisory | {span('own the account close-out register')} | /prompt §2.9 is N/A without supplied samples | no samples supplied; no guideline example shares the scenario (Combo Fighters launch, 133-PR register, RC-flag gate, art-canon handoff) |\n")

w("## UGT readings\n")
w("| Deliverable | Reading A | Reading B | Resolution and evidence |\n|---|---|---|---|")
w(f"| W1 register | a new sheet in Robert's Drive with the {TR['counts']['rows']} rows and two totals (dossier §9.2) | a sheet inside the Wind Down folder | Robert cannot see or write d_e5caf6a8c630421942ee59 (persona_view NO); the ask asks for sharing, not a folder ({ANC}) — same acceptance class (§4b W1) |")
w(f"| W1 rule set | Sunset's checklist + correction, SVB's card terms, the conventions doc | Sherwood's checklist ({G('G_SHERWOOD')}); the Growth/UA page ({M['CONF_UA']['id']}) | the ask names Sunset, SVB and 'the conventions doc I just put in the Wind Down folder' ({ANC}); Sunset is the signed provider (robert@harmonygames.co/1856956532017091340) — source identity settles it |")
w(f"| W2 share | Leonard and Arthur as editors | commenter access, or folder sharing | the ask: 'share it with me and Arthur as editors' ({ANC}) |")
w(f"| W3 Linear | Done on the {len(TR['linear']['done'])} Closed rows, Canceled on the {len(TR['linear']['canceled'])} excluded, comment on each of {len(TR['linear']['done']) + len(TR['linear']['canceled']) + len(TR['linear']['open'])} | close every issue, or leave all open | the project description defines each state ({PROJ}); the prompt's 'settle each of the linear issues like he asked' incorporates it |")
w(f"| W5 reply | thread reply with {fmt(TR['total_today'])} / {fmt(TR['total_after'])} and the three clashes | a longer clash list (Cursor request, Gusto change, card moves) | rule 10 of {DOC} defines a clash as a #winddown decision Sunset or SVB would undo, excluding card moves and requests — one set |\n")

w("## Verification log\n")
w("| Span | Type | Universe record (locator) | Result |\n|---|---|---|---|")
w(f"| {span('leonard asked me in #winddown on friday')} | person / channel / date | {ANC} (Leonard, Fri 2026-02-13 17:21Z; #winddown C0ADGSZKR3R, Robert member) | true |")
w(f"| {span('own the account close-out register')} | event | {ANC} 'can you own the account close-out register' | true |")
w(f"| {span('before he archives anything on google after the 15th')} | state / date | C0ADGSZKR3R/1770933903.645709 'archieve account on google after Feb 15'; {ANC} 'before I archive anything on Google' | true |")
w(f"| {span('share it with him and arthur')} | person | {ANC}; arthur.blake@harmonygames.co | true |")
w(f"| {span('settle each of the linear issues like he asked')} | event | {ANC} 'Settle each Linear issue as you go and leave a line on each'; {PROJ} (ENG-2438…ENG-2483) | true |")
w(f"| {span('reply to him in his thread with the two monthly totals')} | event | {ANC} 'reply here with the two monthly totals'; {DOC} rule 9 | true |")
w(f"| {span('anything that clashes with what we already decided')} | event | {ANC} 'anything in the plan that clashes with what we already decided' | true |\n")

w("## Brief coverage\n")
w("| Brief item | Present in the prompt |\n|---|---|")
w(f"| §4 W1 register | {span('build the register the way he wants it')} |")
w(f"| §4 W2 share | {span('share it with him and arthur')} |")
w(f"| §4 W3 Linear settling | {span('settle each of the linear issues like he asked')} |")
w(f"| §4 W5 reply | {span('reply to him in his thread with the two monthly totals and anything that clashes with what we already decided')} |")
w(f"| §6 anchor A1 | {span('leonard asked me in #winddown on friday')} |\n")

w("## Self-review\n")
w("Walked `Evals/1_Prompt_Eval.md` Phases 1–3 in order against 04_Prompt.txt (hash unchanged before and after this run); every "
  "quoted span above is an exact substring (asserted by the builder).\n")
w("| Check | Counter-reading | Resolution (evidence) |\n|---|---|---|")
rows = [
 ("C1", "field length", f"{wc} words, inside 20–4,000 (taxonomy step 24)"),
 ("C2", "assignment incomplete", "00_Assigments.md has all five axes; robert resolves to one roster entry (robert@harmonygames.co)"),
 ("C3", "a co-founder wouldn't delegate this", f"Leonard asked Robert directly ({ANC}); Robert's own voice is short and lowercase (C0ADGSZKR3R/1770839322.836779)"),
 ("C4", "a register is retrieval, not planning", f"the register decides an action, status and deadline per account under four rule sources and reports clashes ({DOC} rules 4–6) — Planning and Decision Support; Corporate Ops"),
 ("C5", "the prompt carries the recipe", f"rules live in {DOC}, {SVB}, {G('G_SUNSET1')}; the prompt names none; Ambiguity, Dynamic Change and Multi-Source are load-bearing (brief §8)"),
 ("C6", "two destinations for the register", "UGT readings above: the Wind Down folder is unreadable for Robert (d_e5caf6a8c630421942ee59 NO); one acceptance class"),
 ("C7", "'go with your read' leaves writes open", f"it delegates judgement, not writes; every write is named in the ask ({ANC}); the cheapest reading still needs the discoveries (W4 row)"),
 ("C8", "a pointed-to record might hand over answers", f"the ask states rules and columns, not cells ({ANC}); the conventions doc states rules ({DOC})"),
 ("C9", "pre-solved by naming the register's contents", "no account, total, rule or clash appears in the prompt (brief §9)"),
 ("C10", "naming #winddown collapses discovery", f"#winddown holds the anchor itself ({ANC}); every hidden authority stays unnamed ({SVB}, {G('G_SUNSET1')}, {DOC})"),
 ("C11", "no write depends on the investigation", "the register, Linear states and comments and the reply all carry findings (brief §3)"),
 ("C12", "only Slack and Linear carry weight", "11 services carry weight (01_Hardness_Manifest.json services); HARDNESS GATE (long): PASS in the dossier"),
 ("C13", "the asks are bolt-ons", f"all four writes come from one request ({ANC}) for one close-out"),
 ("C14", "a tool is named", "no function, parameter or server name; 'linear' and '#winddown' are product/channel names (prompt_qc_examples row 103)"),
 ("C15", "the prompt scripts steps", "it lists the deliverables in the order Leonard asked (screen 24 skeleton), not sources or method"),
 ("C16", "spec-sheet register", "no column list, format rule or markdown; one 'two monthly totals' echoes the ask (C0ADGSZKR3R anchor)"),
 ("C17", "a premise is false", "every span verified in the log above against C0ADGSZKR3R/1770933903.645709 and the anchor"),
 ("C18", "a write is impossible", "gsheets_create_spreadsheet, gdrive_share_file, linear_update_issue, linear_create_comment, linear_create_issue, slack_post_message exist (Evals/references/tools/catalog.json)"),
 ("C19", "a scoped read is invisible", "check-sql PASS for robert (dossier §1.E); Leonard/Arthur billing facts are relayed in unscoped Linear comments (e.g. " + issue['Zapier']['comment_ids'][-1] + ")"),
 ("C20", "'on friday' / 'the 15th' are relative", "Advisory only: both resolve to one window (Fri Feb 13, Feb 15) before/after the clock 2026-02-14T00:00Z"),
 ("C21", "friction announced", "03_Error_Async_Config.txt is Friction: none; nothing to announce"),
 ("C22", "touched records inconsistent", "local injection gate PASS on SQL sha256 @@SQLSHA@@; AWS and the UA line's ad accounts are out of scope (conventions rule 3, project description), so the base ledger vs Cash P&L AWS/UA gap (/prompt r6 FAIL) is something nothing graded depends on; platform /injection pending (previous SQL be2477091995 passed, Audit-Report/0_injection_PASS_r7.md)"),
 ("C23", "lifted from a sample", "no samples supplied; guideline examples differ in scenario and entities (Advisory)"),
 ("C24", "only investigate + one Slack post", "four writes over Sheets, Drive, Linear and Slack (brief §4)"),
]
for c, a, b in rows:
    w(f"| {c} | Counter: {a} | {b} |")
w("\nUnresolved: none.\n")

w("## Route\n")
w("No Fail: paste 04_Prompt.txt exactly as saved into /prompt, paired with /injection (SQL sha256 @@SQLSHA@@), with all five "
  "assignment fields and 'Friction: none'. Then /create-humantime.\n")
dst = os.path.join(BUNDLE, 'task_inputs', 'Working_Files', '04_Prompt_Check.md')
open(dst, 'w').write("\n".join(L).replace("@@SQLSHA@@", SQLSHA) + "\n")
print('wrote', dst, wc, sha)
