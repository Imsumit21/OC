"""Writes task_inputs/Working_Files/04_Prompt_Writing_Brief.md. argv[1] = capture dir (searches.txt, coll.txt, resolve.txt)."""
import hashlib
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
CAP = sys.argv[1]
M = json.load(open(os.path.join(HERE, 'minted_ids.json')))
P = json.load(open(os.path.join(HERE, 'planned_text.json')))
ACC = json.load(open(os.path.join(HERE, 'accounts.json')))
TR = json.load(open(os.path.join(HERE, 'truth.json')))
A = ACC['accounts']
issue = {a['vendor']: a for a in A}
cap = lambda n: open(os.path.join(CAP, n)).read().rstrip()
G = lambda k: M[k]['robert_message']
GT = lambda k: M[k]['robert_thread']
fmt = lambda x: f"{x:,.2f}"
sqlsha = hashlib.sha256(open(os.path.join(BUNDLE, 'task_inputs', '01_Universe_Inject.sql'), 'rb').read()).hexdigest()[:12]
ANC = M['S_ANCHOR']['locator']
L = []
w = L.append

w("# Prompt Brief — rb-winddown-closeout · prep")
w(f"> Built 2026-10-28 from 00_Assigments.md, 01_Universe_Inject.sql (sha256 {sqlsha}, /injection PASS — "
  "Audit-Report/0_injection_PASS.md), Working_Files/01_Grounding_Dossier.md, 01_Scenario_Design.md, 01_Hardness_Manifest.json · "
  "03_Error_Async_Config.txt is the blank template (Friction: none — no error-async stage run) · no 02_Reference_Files_Manifest.md "
  "(no attachments) · Persona view verified: all load-bearing records YES for robert (check-sql PASS, dossier §1.E); the "
  "Leonard/Arthur mailbox copies are not needed.")
w("> 04_Prompt.txt may be drafted by Claude (`/create-prompt-writing draft`) or written by the human.")
w("> **Clock:** 2026-02-14T00:00:00Z (Saturday). The latest seeded event is Robert's own Linear comment 2026-02-13T20:51Z; "
  "Leonard's ask is 2026-02-13T17:21Z (Fri 9:21 AM PT). The review call (Mar 12) and every deadline are future.\n")

# 1
w("## 1 · Assignment fit\n")
w("| Axis | Assigned value | What it requires here (cited) |\n|---|---|---|")
w("| Business function | Executive → Founders / Exec / Strategy (`Evals/references/rules/task_categories.md`) | a co-founder's wind-down decision work in the founders-only #winddown (C0ADGSZKR3R) |")
w("| Persona / role | Robert, robert@harmonygames.co, Co-Founder & Creative Director (roster `robert`, Executive) | Voice: short, lowercase, direct (C0ADGSZKR3R/1770839322.836779 'Soundly canceled'; C0ADGSZKR3R/1770859313.592649 'Our Figma is good until September 11th'). Read scope: #winddown, #executives, #admin_foundersonly member; own mailbox (billing mail); Wind Down files shared with him (f_31115ddb6ed866f2b10d60) |")
w(f"| Competency | Corporate Ops | account/subscription close-out during the shutdown; Leonard hands Robert the register ({ANC}); the Task List row 'Cancel or move all software subscriptions' is unowned (f_31115ddb6ed866f2b10d60) |")
w(f"| Task skill | Planning and decision support | decide per account what happens (Cancel / Keep / Move / Hold), where it stands, by when, who acts, what it costs, and surface the clashes with earlier decisions ({ANC}); stacked: Actions (Linear settling, sharing, the reply) |")
w("| Task type / tier | Long Horizon (100–500+; author target > 150 calls every run, average < 80%) | 11 services carry weight; 46 Linear issues × comments + settling; manifest budget 166; `HARDNESS GATE (long): PASS` in dossier §13 |")
w("| Difficulty mode / date | easy (recorded); Feb 14, 2026 | nothing on/after Sat Feb 14 00:00Z may be described as done |\n")

# 2
w("## 2 · Situation\n")
w("| Symptom | Seen by | Where it shows (locator) | Relevant records the persona cannot see |\n|---|---|---|---|")
w(f"| Leonard asks Robert to own the account close-out register before he archives anything on Google: one sheet of every account (what we do, where it stands, by when, who, monthly cost), shared with him and Arthur as editors; settle each Linear issue with a line on each; reply with the two monthly totals and any clashes | Robert, in #winddown | {ANC} (Fri Feb 13, 9:21 AM PT) | — |")
w("| Leonard said the P&L covers everything | Robert, #winddown | C0ADGSZKR3R/1770933999.157259 | — |")
w("| Arthur put the accounts into a Linear project | Robert (Linear, unscoped) | project " + M['L_PROJECT']['id'] + " 'Shutdown – accounts' (ENG-2438…ENG-2483) | — |")
w("| The vendors' own billing mail for Arthur's and Leonard's accounts | — | blake@harmonygames.co_1856962040028188034.json, leonard@harmonygames.co_1856958213684823393.json | Leonard's and Arthur's mailboxes; the account holders relay what matters in their Linear comments |\n")
w("No cause belongs in the situation. Why the obvious list is wrong (missing accounts, the Sunset hold and its correction, "
  "the card closure, the amended keep list, unconfirmed cancellations) is discovery-only (§5, never in the prompt).\n")

# 3
w("## 3 · Investigation → action\n")
w("Questions to resolve (no answers here):")
w("1. Which accounts belong on the register (the project, minus exclusions and the duplicate, plus accounts the project lacks)?")
w("2. What happens to each (Leonard's keep list as amended, Arthur's LLC moves, Sunset's list as corrected)?")
w("3. Where each Cancel account stands (vendor-confirmed or not) and by when each account needs action?")
w("4. Who owns each account and what it costs a month; the two totals?")
w("5. Which earlier decisions clash with the plan?\n")
w("Writes they feed: W1 register (1–4) → W2 share with Leonard and Arthur → W3 Linear settling of each issue (state + comment, "
  "from W1) → W4 new issues for added accounts (from 1) → W5 reply in Leonard's thread (totals from W1, clashes from 5). No "
  "write is a bolt-on: every one is named in the ask.\n")

# 4
w("## 4 · Pinned final state (UGT anchor)\n")
w("| Deliverable | Required contents (requirements) | Destination (exact) | Recipient(s) (exact) | Catalog write (reference only; never in the prompt) | Fed by |\n|---|---|---|---|---|---|")
w(f"| W1 register | one row per account ({TR['counts']['rows']}): action, status (Cancel rows), deadline, owner, monthly cost; totals {fmt(TR['total_today'])} and {fmt(TR['total_after'])} (dossier §9.2) | a new Google Sheet in Robert's Drive (the Wind Down folder d_e5caf6a8c630421942ee59 is not writable for him) | Leonard, Arthur (W2) | gsheets_create_spreadsheet + gsheets_values_update | {ANC}; {M['DOC_CONV']['id']} |")
w(f"| W2 share | Leonard and Arthur can edit the register | the register file | leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co (writer) | gdrive_share_file | {ANC} |")
w(f"| W3 Linear settling | Done: {', '.join(TR['linear']['done'])}; Canceled: the {len(TR['linear']['canceled'])} excluded issues; the rest stay open; a comment on each of the {len(A)} issues | project {M['L_PROJECT']['id']} | — | linear_update_issue + linear_create_comment | {M['L_PROJECT']['id']} description; {ANC} |")
w(f"| W4 new issues | one issue per added account: {', '.join(TR['linear']['new_issues'])} | project {M['L_PROJECT']['id']} (team_ENG) | — | linear_create_issue | {M['DOC_CONV']['id']} rule 3 |")
w(f"| W5 reply | the two monthly totals and the clashes: Slack downgrade to free (C0ADGSZKR3R/1770840054.486779), Slack cut to three paid seats (C0ADGSZKR3R/1770842405.931359), Google archiving after Feb 15 (C0ADGSZKR3R/1770933903.645709) vs Sunset's hold ({G('G_SUNSET1')}) | thread of {ANC} | Leonard (EMPLOYEE_0038_SLACK_ID) | slack_post_message (thread_ts) | W1; {G('G_SUNSET1')} |\n")
w("| Decision-ambiguity risk | Alternative a careful run could take | What pins it |\n|---|---|---|")
w(f"| register location | the Wind Down folder (d_e5caf6a8c630421942ee59) | Robert cannot see or write it (persona_view can-see NO); the ask says 'share it with me and Arthur as editors' ({ANC}), not a folder |")
w(f"| which rules | Sherwood's checklist ({G('G_SHERWOOD')}); the Growth/UA page ({M['CONF_UA']['id']}) | the ask names 'Sunset's data checklist' and 'the conventions doc I just put in the Wind Down folder' ({ANC}); Sunset is the signed provider (robert@harmonygames.co/1856956532017091340) |")
w(f"| reply place | a new #winddown message or a DM | the ask: 'reply here' ({ANC}); a thread reply or a channel message in #winddown both pass |")
w(f"| settle vs leave | leaving all issues open until accounts close | the project description: 'Done once the account counts as closed in the register …, Canceled if it doesn't belong on the list, everything else stays open' (project of ENG-2438…ENG-2483, {M['L_PROJECT']['id']}) |")
w(f"| act vs ask | cancelling accounts himself | the ask is the register, the issues and the reply; no rule asks Robert to cancel accounts on Feb 14 ({ANC}) |")
w(f"| persona vs agent | 'I'll share it' in the prompt | §11: every write is asked of the assistant ({ANC} asks Robert) |\n")
w("### 4b · Canonical outcome (one acceptance class)\n")
w("| Deliverable | Field | Fixed value (pinned, with locator) | Delegated by | Allowed equivalence class | Material / representational |\n|---|---|---|---|---|---|")
w(f"| W1 | kind/location | a spreadsheet Robert can share ({ANC} 'one sheet') | — | a Google Sheet (a Doc table also passes) in Robert's Drive | material |")
w(f"| W1 | title | — ({ANC} names none) | the ask names no title ({ANC}) | any title | representational |")
w(f"| W1 | row set | the {TR['counts']['rows']} accounts in dossier §9.2 (f_605121f4a36752645e0ac3; {M['L_PROJECT']['id']}) | — | any order; vendor-name variants (QuickBooks / Intuit QuickBooks; AppLovin / AppLovin UA; Meta / Meta Ads); excluded accounts listed separately are fine | material |")
w(f"| W1 | action | per dossier §9.2 ({M['DOC_CONV']['id']} rule 4) | — | the four words or clear synonyms (Cancel; Keep; Move to Arthur's LLC/KubLLC card; Hold for Sunset) | material |")
w(f"| W1 | status | Cancel rows only, per dossier §9.2 ({M['DOC_CONV']['id']} rule 5) | — | Closed/Requested/Open or synonyms; blank or n/a on other rows | material |")
w(f"| W1 | deadline | per dossier §9.2 ({M['DOC_CONV']['id']} rule 6) | — | any date format; dash/blank where §9.2 has '—' | material |")
w(f"| W1 | owner | per dossier §9.2 ({M['DOC_CONV']['id']} rule 7) | — | first name or full name | material |")
w(f"| W1 | monthly cost | per dossier §9.2 ({M['DOC_CONV']['id']} rule 8) | — | to the cent, with or without $ | material |")
w(f"| W1 | totals | {fmt(TR['total_today'])} and {fmt(TR['total_after'])} ({M['DOC_CONV']['id']} rule 9) | — | to the cent; anywhere in the sheet | material |")
w(f"| W1 | column order / formatting | — ({ANC}) | the ask lists the columns, not a layout ({ANC}) | any | representational |")
w(f"| W2 | grantees + role | leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co, editor ({ANC}) | — | direct share of the file | material |")
w(f"| W3 | states | Done {', '.join(TR['linear']['done'])}; Canceled {', '.join(TR['linear']['canceled'])}; others not Done/Canceled ({M['L_PROJECT']['id']}) | — | any open state (Todo, In Progress) for the rest | material |")
w(f"| W3 | comment | one per issue saying what happens and by when (project description, ENG-2438…ENG-2483) | — | any wording that carries the action and the deadline | material (presence, content) |")
w(f"| W4 | new issues | {', '.join(TR['linear']['new_issues'])} in the project of ENG-2438 ({M['L_PROJECT']['id']}) | — | any title naming the vendor; one per account | material |")
w(f"| W5 | contents | both totals ({fmt(TR['total_today'])}, {fmt(TR['total_after'])}) + exactly the three clashes under {M['DOC_CONV']['id']} rule 10 ({ANC}) | — | any wording per clash; card moves, Oliver's Cursor request and the Gusto change are not clashes (rule 10) | material |")
w(f"| W5 | wording | — ({ANC}) | the ask asks only for 'the two monthly totals and anything … that clashes' ({ANC}) | any wording | representational |\n")
w("Rule for 08/09: two runs reach the same final state when every material field matches within its class. Persona "
  "approximations flagged by /injection (Typecast 'after the summer', Gusto 'on the 3rd') are not graded beyond what §9.2 states.\n")

# 5
facts = [
 ("F1 the ask (LB)", "own the register; columns; share as editors; settle issues with a line on each; reply with totals + clashes", ANC, "YES (member)", "met first", "none", "Yes — as 'Leonard's close-out register ask' (anchor A1)"),
 ("F2 keep list (LB)", "keep Deel, gusto, Intuit; Figma; Linear", "C0ADGSZKR3R/1770933601.686309", "YES", "met first; amended by F3", "conclusive parent", "No"),
 ("F3 Gusto reply (LB)", "gusto pulls from the bank on the 3rd; cancel before Mar 3", M['S_GUSTO_REPLY']['locator'], "YES", "overturns F2 for Gusto", "replies rarely opened", "No"),
 ("F4 Leonard's subscriptions table", "Kapwing, Zapier ticked, Carta 8/15, Slack down to 3", "C0ADGSZKR3R/1770933450.410449", "YES", "context", "table in an attachment", "No"),
 ("F5 LLC moves", "github, dbt, Metabase to KubLLC", "C0ADGSZKR3R/1770937232.664809", "YES", "Hold wins for GitHub/dbt", "redacted dbt token; comments confirm", "No"),
 ("F6 'covers everything' (trap)", "P&L covers everything", "C0ADGSZKR3R/1770933999.157259", "YES", "overturned by F9/F12", "conclusion stop", "No"),
 ("F7 Sunset checklist (LB authority)", "hold list; review call; Helpshift export", G('G_SUNSET1'), "YES (own copy)", "decoy Sherwood met first by date", "Gmail rarely opened", "No — the ask names it"),
 ("F8 Sunset correction (LB)", "Trello in, Metabase out, BigQuery and dbt in", G('G_SUNSET2'), "YES", "overturns F7 in part", "second message of the thread", "No"),
 ("F9 conventions doc (LB authority)", "rules 1–9", M['DOC_CONV']['id'], "YES (shared)", "decoy UA page", "—", "No — the ask names it"),
 ("F10 SVB card (LB authority)", "card closes Feb 20; move kept charging accounts by Feb 19", M['T_SVB']['id'], "YES (unscoped)", "decoy Chase card", "Trello rarely opened", "No — the ask names 'SVB's card terms'"),
 ("F11 review call (LB)", "2026-03-12 17:00Z", M['E_REVIEW']['robert_copy'], "YES (own calendar)", "only via F7", "Calendar rarely opened", "No"),
 ("F12 costs tab (LB)", "column AF Dec-25 costs; Sound line", "f_605121f4a36752645e0ac3", "YES (shared)", "header dates a year off", "wrong column", "No"),
 ("F13 ledger UA lines (LB)", "meta 2,843.84 / applovin 9.80 (Jan)", "snowflake.wh_finance__expenses__finance_ledger FIN-000689 / FIN-000688", "YES (unscoped)", "only via F9 rule 3", "Snowflake rarely opened", "No"),
 ("F14 Linear comments (LB)", f"decisive on {sum(1 for a in A if any(c[3] for c in a['comments']))} of {len(A)} issues", f"{M['L_PROJECT']['id']} (e.g. {issue['Docusign']['comment_ids'][0]})", "YES (unscoped)", "titles/descriptions say nothing", "no list call returns comments", "No"),
 ("F15 CodeRabbit notice (LB)", "canceled Feb 12", M['GH_CR']['id'], "YES (unscoped)", "Arthur's 'cancelled' in Slack met first", "bot comment on a PR", "No"),
 ("F16 Helpshift export (LB)", "export done, buttons switched", M['CONF_C2']['id'] + ' on ' + M['CONF_C1']['id'], "YES (unscoped)", "only via F7", "page comments", "No"),
 ("F17 billing mail (LB)", "Figma Sep 11 2026, Layer Feb 25, Pond5 Mar 2, Linear Feb 1 2027, Soundly confirmation", f"{G('G_FIGMA')}; {G('G_POND5')}", "YES (own mailbox)", "—", "found by vendor name", "No"),
 ("F18 iPostal closed (trap)", "mailbox closed Jan 16", "robert@harmonygames.co/1854432461283937829", "YES", "tab still forecasts it", "—", "No"),
 ("F19 ElevenLabs annual", "$50, Jul 9 2025 – Jul 9 2026", "robert@harmonygames.co/1837122624854744558", "YES", "—", "—", "No"),
 ("F20 Singular cycle", "quarterly invoices Sep 1, Dec 1; termination asks for confirmation", "robert@harmonygames.co/1850283027022457279; robert@harmonygames.co/1853470745017478863", "YES", "Mar 15 extension decoy", "—", "No"),
]
w("## 5 · Discovery map\n")
w("| Fact | Value | Locator | Persona-readable | Met first / overturned by | Search risk | Name in prompt? |\n|---|---|---|---|---|---|---|")
for f in facts:
    w("| " + " | ".join(f) + " |")
w("")

# 5a
sap = [
 ("F1", "slack", "close-out register", "base 0; seeded 1", "0", ANC, "YES (seeded; check-sql YES)"),
 ("F2", "slack", "keep Deel", "1", "0", "C0ADGSZKR3R/1770933601.686309", "YES"),
 ("F3", "slack", "gusto (thread of the keep list)", "base 0; seeded 1", "0", M['S_GUSTO_REPLY']['locator'], "YES (seeded)"),
 ("F4", "slack", "latest and greatest on subscriptions", "1", "0", "C0ADGSZKR3R/1770933450.410449", "YES"),
 ("F5", "slack", "KubLLC", "2", "0", "C0ADGSZKR3R/1770937232.664809", "YES"),
 ("F6", "slack", "covers everything", "5", "0", "C0ADGSZKR3R/1770933999.157259 (among the 5)", "YES"),
 ("F7", "gmail", "data delivery checklist", "base 0; seeded 1 thread", "0", GT('G_SUNSET1'), "YES (seeded; own copy)"),
 ("F8", "gmail", "data delivery checklist (thread)", "base 0; seeded 2nd message", "0", G('G_SUNSET2'), "YES (seeded)"),
 ("F9", "gdocs", "close-out", "base 0; seeded 1", "0", M['DOC_CONV']['id'], "YES (seeded; shared)"),
 ("F10", "trello", "SVB", "3 base + seeded card", "0", M['T_SVB']['id'], "YES (unscoped)"),
 ("F11", "gcal", "Sunset", "base 0; seeded 1 (own copy)", "0", M['E_REVIEW']['robert_copy'], "YES (seeded)"),
 ("F12", "gsheets", "P&L and forecast", "7", "8", "f_605121f4a36752645e0ac3", "YES"),
 ("F13", "snowflake", "FINANCE_LEDGER (table read)", "unscoped table", "0", "snowflake.wh_finance__expenses__finance_ledger", "YES (unscoped)"),
 ("F14", "linear", "Shutdown", "base 0; seeded project", "0", M['L_PROJECT']['id'], "YES (seeded; unscoped)"),
 ("F15", "github", "coderabbit", "3 base + seeded PR comment", "0", M['GH_CR']['id'], "YES (unscoped)"),
 ("F16", "confluence", "Helpshift", "2 base + seeded page", "0", M['CONF_C1']['id'], "YES (unscoped)"),
 ("F17", "gmail", "Figma / Pond5", "Figma 78 base; Pond5 0 base + seeded", "0", G('G_POND5'), "YES (own mailbox)"),
 ("F18", "gmail", "Mailbox Has Been Cancelled", "1", "0", "robert@harmonygames.co/1854432461283937829", "YES"),
 ("F19", "gmail", "Eleven Labs", "3", "0", "robert@harmonygames.co/1837122624854744558", "YES"),
 ("F20", "gmail", "Singular", "203", "0", "robert@harmonygames.co/1853470745017478863", "YES"),
]
w("## 5a · Search-as-persona proof\n")
w("`persona_view.py search` reads only the base export, so seeded rows return 0 there; seeded reach is the dossier's "
  "check-sql PASS for robert (§1.E). Visible hits below are base counts.\n")
w("| Fact (§5 row) | Service | Natural query | Visible hits | Hidden by ACL | First visible hit (id) | Found? |\n|---|---|---|---|---|---|---|")
for r in sap:
    w("| " + " | ".join(r) + " |")
w("\n```\n" + cap('searches.txt') + "\n```\n")

# 6
w("## 6 · Triggers, incorporation and implicit requirements\n")
w("| Graded requirement | Seeded where | Trigger category the prompt must carry | Incorporating source (locator · readable · unique · instructions-not-answer) | Inferable |\n|---|---|---|---|---|")
w(f"| R1–R6 register contents and rules | {M['DOC_CONV']['id']}, {G('G_SUNSET1')}, {M['T_SVB']['id']} | deliverable: the register Leonard asked for | {ANC} · YES · names each rule source by issuer · states rules, not cells | no — needs the anchor |")
w(f"| R7 reply with totals + clashes | {ANC} | deliverable: Leonard's reply | {ANC} · YES · unique · asks, doesn't answer | no — needs the anchor |")
w(f"| R8 share as editors | {ANC} | recipients via the anchor | {ANC} · YES | no |")
w(f"| R9 Linear settling + new issues | {M['L_PROJECT']['id']}, {M['DOC_CONV']['id']} | scope: the Linear issues in the anchor | {ANC} 'Settle each Linear issue as you go and leave a line on each' · YES · unique | no |\n")
w("| Anchor | May be named |\n|---|---|")
w("| A1 | Leonard's close-out register ask; Leonard's #winddown request; the account close-out register |\n")

# 7
w("## 7 · Dates and constraints\n")
w("| Item | Absolute date or value | Source | Past fact or deadline |\n|---|---|---|---|")
w(f"| Leonard's ask | 2026-02-13T17:21Z | {ANC} | past |")
w("| Google accounts archived | after 2026-02-15 | C0ADGSZKR3R/1770933903.645709 | future (the register is due before it) |")
w(f"| SVB card closes | 2026-02-20; moves by 2026-02-19 | {M['T_SVB']['id']} | future |")
w(f"| Sunset review call | 2026-03-12 17:00Z | {M['E_REVIEW']['robert_copy']} | future |")
w("| Clock | 2026-02-14T00:00:00Z (Sat) | GEN_EXECUTION §3; latest seed ENG-2479 comment 2026-02-13T20:51Z | now |\n")

# 8
w("## 8 · Difficulty levers\n")
w("| Lever | Used | Load-bearing | Where it lives | Prompt-side condition |\n|---|---|---|---|---|")
w(f"| Ambiguity | yes | yes | which accounts are in, which rule governs (Sunset vs Sherwood, conventions vs UA page) | the prompt points at the ask only; destination pinned by the ask ({ANC}) |")
w(f"| Dynamic change | yes | yes | keep list → Gusto reply; checklist → correction; Slack 'cancelled' → vendor word | the prompt names neither the summary nor the correction |")
w("| Multi-source | yes | yes | 11 services (Slack, Linear, Gmail, Trello, Docs, Sheets, Snowflake, Calendar, Confluence, GitHub, Drive) | no source named as an exact artifact beyond the anchor |")
w("| Async | no | — | — | — |")
w("| Error recovery | no | — | Friction: none | — |")
w("| Access control | yes (minor) | no | the Wind Down folder (d_e5caf6a8c630421942ee59) is not visible; the register goes in Robert's Drive | the prompt does not ask for the folder |\n")

# 9
w("## 9 · Must not appear in the prompt\n")
w("- Tool / server names: gsheets_*, gdrive_share_file, linear_*, slack_*, gmail_*, trello_*, gcal_*, confluence_*, github_*, snowflake_*, any MCP server name.")
w(f"- Ids: {ANC}, {M['L_PROJECT']['id']}, ENG-24xx keys, {M['DOC_CONV']['id']}, {M['T_SVB']['id']}, {M['E_REVIEW']['robert_copy']}, {M['GH_CR']['id']}, f_605121f4a36752645e0ac3, FIN-000xxx.")
w("- Hidden authorities and their contents: Sunset's list or correction, the SVB dates, the conventions rules, the review date, the Helpshift page, CodeRabbit's notice.")
w("- Findings: any account name, action, status, deadline, owner, cost, either total, the missing accounts, the clashes.")
w("- Root causes: the P&L being incomplete, the Sound line, the ledger, the costs-tab column, the keep-list amendment.")
w("- Form: markdown, numbered steps, column lists beyond what Leonard asked, format rules.\n")

# 10
w("## 10 · Entity traps\n")
w("```\n" + cap('coll.txt') + "\n" + cap('resolve.txt') + "\n```\n")
w("| Correct entity (exact) | Lookalike(s) | How they differ | Locator (email or record id) |\n|---|---|---|---|")
w("| Leonard Hayes leonard.hayes@harmonygames.co | — (mailbox files `leonard@…`) | alias only | leonard.hayes@harmonygames.co |")
w("| Arthur Blake arthur.blake@harmonygames.co | 'Blake' in Leonard's table; mailbox files `blake@…` | same person | arthur.blake@harmonygames.co |")
w("| Oliver Brooks oliver.brooks@harmonygames.co | Lauren Brooks lauren@harmonygames.co | different person | oliver.brooks@harmonygames.co |")
w(f"| Sunset (provider, signed Feb 12) | Sherwood Partners (consulted); 'Sunset of Creative Reporting' mails | issuer | robert@harmonygames.co/1856956532017091340; {G('G_SHERWOOD')} |")
w("| Marcus Bennett marcus.bennett@harmonygames.co | Marcus Lee, marcus@harmonygames.co | three Marcuses | marcus.bennett@harmonygames.co |\n")

# 11
w("## 11 · Pre-submit checklist\n")
for x in ["Robert's voice: short, lowercase-ok, plain; no spec-sheet layout or markdown",
          "names the anchor in plain words (Leonard's close-out register ask in #winddown) and nothing else by exact title or id",
          "asks the assistant (not 'I'll') to do the register, the sharing, the Linear settling and the reply",
          "says it's due before Leonard archives the Google accounts (after Feb 15)",
          "no account, rule, date, total or clash from §9",
          "no tool or server name; no numbered steps",
          "20–4,000 words (aim 60–150)"]:
    w(f"- [ ] {x}")
w("")

# 12
w("## 12 · Blockers and routed defects\n")
w("None blocking. Advisories carried from /injection (Audit-Report/0_injection_PASS.md): comment-only vendor facts (Cursor, "
  "Zapier, 1Password, Vercel, 'which card') must be findable — they are, in Linear comments (F14); persona approximations "
  "(Typecast, Gusto day) are not graded beyond §9.2 of the dossier.\n")

# 13
w("## 13 · Self-review\n")
w("Walked `Evals/1_Prompt_Eval.md` Phases 1–3 against this brief (§1.1 persona, §1.5 competency/skill/complexity, §2.1 UGT, "
  "§2.2 feasibility/ACL, §2.3 truthfulness, §2.6 clarity, §2.7 contrived register, §3.2 coherence).\n")
w("| Area | Counter-reading | Resolution (evidence) |\n|---|---|---|")
w(f"| UGT | two destinations for the register (Wind Down folder vs own Drive) | Robert cannot see d_e5caf6a8c630421942ee59 (persona_view NO); the ask pins sharing, not a folder ({ANC}) — §4b W1 |")
w(f"| UGT | 'reply here' could be a thread reply or a channel message | both are in #winddown and carry the same contents; §4b W5 accepts either ({ANC}) |")
w(f"| Clarity | 'settle each Linear issue' could mean close every issue | the project description defines Done / Canceled / open ({M['L_PROJECT']['id']}) |")
w(f"| Incorporation | the rule sources might not be incorporated | the ask names Sunset's data checklist, SVB's card terms and the conventions doc ({ANC}); each is readable (check-sql YES) and states rules, not answers ({M['DOC_CONV']['id']}) |")
w("| Truthfulness | a prompt premise like 'Leonard asked me yesterday' could be off | the ask is Fri Feb 13 17:21Z; clock is Sat Feb 14 00:00Z — 'yesterday'/'today' both ambiguous across time zones, so the prompt should say Friday (C0ADGSZKR3R/1770933903.645709 dates the archive plan) |")
w("| Feasibility / ACL | the agent may need Leonard's/Arthur's billing mail | every needed fact is relayed in their Linear comments (unscoped; e.g. " + issue['Zapier']['comment_ids'][-1] + "); writes: gsheets create, gdrive share, linear update/comment/create, slack post exist in Evals/references/tools/catalog.json |")
w(f"| Contrived register | listing the register columns in the prompt reads as a spec sheet | the columns live in the ask ({ANC}); the prompt only points at it |\n")
w("Unresolved: none.\n")
dst = os.path.join(BUNDLE, 'task_inputs', 'Working_Files', '04_Prompt_Writing_Brief.md')
open(dst, 'w').write("\n".join(L) + "\n")
print('wrote', dst)
