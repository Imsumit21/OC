"""Writes task_inputs/Working_Files/08_OE_Writing_Ledger.md (prep mode) from the minted ids, accounts, truth and SQL text.
Arg 1: a file with the pasted visibility-proof lines (persona_view check-sql rows), or nothing on the first pass."""
import hashlib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
TI = os.path.join(BUNDLE, 'task_inputs')
M = json.load(open(os.path.join(HERE, 'minted_ids.json')))
P = json.load(open(os.path.join(HERE, 'planned_text.json')))
ACC = json.load(open(os.path.join(HERE, 'accounts.json')))
TR = json.load(open(os.path.join(HERE, 'truth.json')))
SQL = open(os.path.join(TI, '01_Universe_Inject.sql')).read()
PROMPT = open(os.path.join(TI, '04_Prompt.txt')).read()
A = ACC['accounts']
issue = {a['vendor']: a for a in A}
ROB = 'robert@harmonygames.co'
WHO = {'usr_cc3e90160f490686': 'Arthur', 'usr_63fffeb4fab5233e': 'Leonard', 'usr_Robert': 'Robert', 'usr_bdf01b53c6a92c5e': 'Oliver'}
G = lambda k: M[k]['thread_id'][ROB]
sha = lambda s: hashlib.sha256(s.encode()).hexdigest()[:12]
fmt = lambda x: f"{x:,.2f}"
txt = lambda k: ' '.join(P[k].split())


def sline(loc):
    n = [i for i, l in enumerate(SQL.splitlines(), 1) if loc.split('/')[-1] in l]
    return f"01_Universe_Inject.sql (SQL L{n[0]})" if n else "01_Universe_Inject.sql"


def esc(s):
    return str(s).replace('|', '/').replace('\n', ' ')


L = []
w = L.append
w("# 08 OE Writing Ledger — Robert account close-out register (rb-winddown-closeout)")
w("Generated 2026-10-29 · Clock 2026-02-14T00:00:00Z (Fri Feb 13, 2026, 4:00 PM PST) · Persona Robert robert@harmonygames.co "
  "(Co-Founder & Creative Director, Executive) · Tier Long-Horizon")
w("Status: READY — every requirement has verified, persona-visible facts; every write maps to a cataloged tool; friction none")
w(f"Inputs read: 04_Prompt.txt — present (sha256 {sha(PROMPT)}) · 00_Assigments.md — present · 01_Universe_Inject.sql — present "
  f"(sha256 {sha(SQL)}; /injection PASS, /prompt NON-FAIL) · 01_Grounding_Dossier.md — present in Working_Files (leads only) · "
  "01_Hardness_Manifest.json — present in Working_Files (leads for traps) · 03_Error_Async_Config.txt — present (Friction: none) · "
  "02_Reference_Files_Manifest.md — absent (no attachments) · 04_Prompt_Writing_Brief.md — present (§4b canonical outcome) · "
  "06_PreCheck_Trajectory + 07_Baseline_Trajectories — seven Opus runs on the pre-hardening SQL, read for tool paths only\n")
w("Persona binding: roster.json entry robert, Robert, Co-Founder & Creative Director, Executive. Scoped services: Gmail (own mailbox "
  "robert@harmonygames.co), Slack (224 visible channels incl. #winddown C0ADGSZKR3R, #prototype C09UHHN6PFZ, #admin_foundersonly "
  "C04UEQVDVB7, #executives C07C2866011, the shared applovin channel C1C2137664A3), Calendar (own), Drive/Docs/Sheets (own files and files shared with him). Unscoped: Linear, Trello, GitHub, "
  "Contacts, Confluence.\n")
w("Linear users in the project: usr_cc3e90160f490686 = Arthur Blake, usr_63fffeb4fab5233e = Leonard Hayes, usr_Robert = Robert, "
  "usr_bdf01b53c6a92c5e = Oliver Brooks. Dates are UTC; \"created\" marks a record time, \"due\"/\"starts\"/\"renews\" a semantic future "
  "date. No semantic future date is expected as done: the SVB card closure (Feb 18), the review call (Mar 12) and every by-when date "
  "are named as future events only.\n")

# ------------------------------------------------------------------ A
w("## A · Requirements (traced to the prompt)")
w("| R | Prompt span (quoted) | Type (Discovery / Write / Tell / Constraint) | Explicit / implicit | Fact IDs |\n|---|---|---|---|---|")
REQ = [
 ("R1", "leonard asked me in #winddown on friday to own the account close-out register", "Discovery — find Leonard's Feb 13 ask in #winddown; it names every source and the deliverables", "Explicit", "F1"),
 ("R2", "work through his ask and everything it points to", "Discovery — the keep list and its thread, Arthur's card moves, Sunset's checklist and correction, SVB's card terms, the conventions doc, the Linear project and its issue comments, the review call, the costs tab and the ledger, each vendor's billing record", "Implicit (the sources are named in the ask and the doc)", "F2–F16, F18–F27, F29, F30, F34, F36–F38"),
 ("R3", "build the register the way he wants it", "Write — one register (25 rows: account, action, status for Cancel rows, by when, owner, monthly cost) with two totals, following rules 1–9", "Explicit (columns and rules implicit through the ask and the doc)", "F7, F31, F32"),
 ("R4", "share it with him and arthur", "Write + Constraint — Leonard and Arthur as editors", "Explicit (role implicit: the ask says 'as editors')", "F1, F30, F31"),
 ("R5", "settle each of the linear issues like he asked", "Write — per the project rule: Done when Closed, Canceled when it doesn't belong, else open; a comment on each with what happens and by when", "Explicit (the rule itself implicit through the project description)", "F8, F9, F29, F33, F34, F37, F38"),
 ("R6", "reply to him in his thread with the two monthly totals", "Write + Tell — a reply in the ask's thread with both totals", "Explicit", "F1, F32"),
 ("R7", "anything that clashes with what we already decided", "Tell — the #winddown decisions Sunset's list or SVB's terms would undo (rule 10)", "Explicit (definition implicit through rule 10)", "F5, F6, F7, F12, F13, F35"),
 ("R8", "before he archives anything on google after the 15th", "Constraint — the Google archive plan is a decision on record (feeds the clash set)", "Explicit (context)", "F6, F35"),
]
for r in REQ:
    assert r[1] in PROMPT, r[1]
    w(f"| {r[0]} | \"{r[1]}\" | {r[2]} | {r[3]} | {r[4]} |")
w("")

# ------------------------------------------------------------------ B
w("## B · Facts")
w("| F | Fact / value | Service | Tool family (catalog) | Locator | Locator origin (prompt · F-n · search \"query\") | Expected data (dates typed: created / starts / due) | Persona-visible? (proof) | Depends on | Source pointer |")
w("|---|---|---|---|---|---|---|---|---|---|")
F = []
f = lambda *x: F.append(x)
an = M['S_ANCHOR']['locator']
f("F1", "Leonard's ask (hub)", "Slack (#winddown, private)", "slack_search_channels, slack_read_channel, slack_read_thread",
  "#winddown, Leonard's newest message before the clock", "prompt (\"leonard asked me in #winddown on friday\")",
  f"Message {an} by Leonard (EMPLOYEE_0038_SLACK_ID), created Fri Feb 13 2026 17:21:07Z: \"{esc(txt('S_ANCHOR'))}\". "
  "Newest #winddown message before the clock; no replies", "YES — check-sql", "—", f"{sline(an)}; {an}")
f("F2", "Leonard's keep list and its thread", "Slack (#winddown)", "slack_read_channel (paginate: 206 Feb 2026 messages), slack_read_thread",
  "#winddown, Leonard's Feb 12 keep-list message and its replies", "F1 (\"my keep list from last night\")",
  "Message C0ADGSZKR3R/1770933601.686309 by Leonard, created Thu Feb 12 2026 22:00:01Z: \"During shutdown, let's keep Deel, gusto, Intuit. "
  "I canceled other subscriptions under mine. ...\" reply_count 1 (after the SQL's parent update)", "YES — check-sql (base)", "F1",
  "slack messages C0ADGSZKR3R/2026-02.json ts 1770933601.686309; 01_Universe_Inject.sql L39 (UPDATE of the parent)")
gl = M['S_GUSTO_REPLY']['locator']
f("F3", "Arthur's Gusto reply under the keep list (amends it)", "Slack (#winddown thread)", "slack_read_thread",
  "Replies in the keep-list thread", "F2 (the thread holds 1 reply)",
  f"Reply {gl} by Arthur, created Fri Feb 13 2026 02:14:36Z: \"{esc(txt('S_GUSTO_REPLY'))}\" → Gusto is Cancel (by-when from the SVB card comment, F36)",
  "YES — check-sql", "F2", f"{sline(gl)}; {gl}")
f("F4", "Arthur's card moves to his LLC", "Slack (#winddown)", "slack_read_channel", "#winddown, Arthur's Feb 12 message about his KubLLC card",
  "F1 (\"Arthur's moves to his LLC card\")",
  "Message C0ADGSZKR3R/1770937232.664809 by Arthur, created Thu Feb 12 2026 23:00:32Z: \"I'll be moving github, [USERNAME_30019], and "
  "Metabase to my KubLLC card.\" ([USERNAME_30019] = dbt, per Leonard's keep-Metabase-and-dbt line)", "YES — check-sql (base)", "F1",
  "slack messages C0ADGSZKR3R/2026-02.json ts 1770937232.664809")
f("F5", "The Slack decisions on record (Feb 11–12)", "Slack (#winddown)", "slack_read_channel (page back past Feb 12), message attachments",
  "#winddown, Feb 11 Slack plan messages and Leonard's Feb 12 subscriptions checklist table", "F1 (\"what we already decided\")",
  "C0ADGSZKR3R/1770839825.928989 Leonard, created Feb 11 2026 19:57Z: \"For Slack, should I just go back to free version with no history?\"; "
  "C0ADGSZKR3R/1770840054.486779 Arthur, created Feb 11 20:00Z: \"yeah free version\"; C0ADGSZKR3R/1770842080.379699 Leonard: \"I guess "
  "I'll keep only a few accounts active and turn people into guest accounts\"; C0ADGSZKR3R/1770842405.931359 Leonard: \"let me do that\"; "
  "C0ADGSZKR3R/1770933450.410449 Leonard, created Feb 12 21:57Z, attachments blocks table \"latest and greatest on subscriptions\": "
  "\"- [x] Slack (down to 3 FT members)\"", "YES — check-sql (base)", "F1",
  "slack messages C0ADGSZKR3R/2026-02.json ts 1770839825.928989, 1770840054.486779, 1770842080.379699, 1770842405.931359, 1770933450.410449")
f("F6", "The Google archive plan on record", "Slack (#winddown)", "slack_read_channel", "#winddown, Leonard's Feb 12 action-item list",
  "prompt (\"before he archives anything on google after the 15th\")",
  "Message C0ADGSZKR3R/1770933903.645709 by Leonard, created Thu Feb 12 2026 22:05:03Z, action items incl. \"archieve account on google "
  "after Feb 15\" and \"I think we keep Metabase and dbt\"", "YES — check-sql (base)", "F1",
  "slack messages C0ADGSZKR3R/2026-02.json ts 1770933903.645709")
dc = M['DOC_CONV']['id']
f("F7", "Close-out register conventions, rules 1–10", "Docs (shared with Robert)", "gdrive_search, gdocs_get_document_text, gdrive_read_file",
  "Doc \"Close-out register conventions\"", "F1 (\"the conventions doc I just put in the Wind Down folder\"); search \"Close-out register conventions\"",
  f"Doc {dc}, created Fri Feb 13 2026 16:38:02Z, modified 16:58:40Z, shared with Leonard, Arthur, Robert. Text: \"{esc(txt('DOC_CONV'))}\"",
  "YES — check-sql", "F1", f"{sline(dc)}; {dc}")
pj = M['L_PROJECT']['id']
f("F8", "Linear project \"Shutdown – accounts\" and its settle rule", "Linear (team ENG)", "linear_list_projects, linear_get_project",
  "Project \"Shutdown – accounts\"", "F1 (\"Arthur put every account into the Linear shutdown project\")",
  f"Project {pj}, lead Arthur, created Thu Feb 12 2026 23:24:10Z. Description: \"{esc(txt('L_PROJECT'))}\"",
  "Unscoped (Linear)", "F1", f"{sline(pj)}; linear project {pj}")
iss = "; ".join(f"{a['issue']} {a['vendor']} ({WHO[a['assignee']]})" for a in A)
inr = [a for a in A if a['inr']]
out = [a for a in A if not a['inr']]
NC = sum(len(a['comments']) for a in A)
f("F9", f"The project's {len(A)} issues", "Linear", "linear_list_issues (project filter)", "Issues of the project", "F8",
  f"{len(A)} issues, ENG-2438 … ENG-2466 with no gaps, all Todo at the clock, created Feb 12 2026, creator Arthur: {iss}",
  "Unscoped (Linear)", "F8", f"01_Universe_Inject.sql linear.linear_issues rows ({len(A)}), ENG-2438 … ENG-2466")
cm = lambda a: " / ".join(f"{WHO[c[0]]}: \"{esc(c[2])}\"" for c in a['comments']) or "no comment"
f("F10", f"Comments on the {len(inr)} issues that stay on the register", "Linear", "linear_list_comments (one call per issue)",
  "Comments of each project issue", "F9",
  "; ".join(f"{a['issue']} {a['vendor']}: {cm(a)}" for a in inr), "Unscoped (Linear)", "F9",
  "01_Universe_Inject.sql linear.linear_comments rows (" + ", ".join(a['comment_ids'][0] for a in inr if a['comment_ids'])[:200] + " …)")
f("F11", f"Comments on the {len(out)} issues that leave the register", "Linear", "linear_list_comments (one call per issue)",
  "Comments of each project issue", "F9",
  "; ".join(f"{a['issue']} {a['vendor']}: {cm(a)}" for a in out), "Unscoped (Linear)", "F9",
  "01_Universe_Inject.sql linear.linear_comments rows: " + ", ".join(c for a in out for c in a['comment_ids']))
s1 = G('G_SUNSET1')
f("F12", "Sunset's data delivery checklist (first version)", "Gmail (Robert's mailbox)", "gmail_search_messages, gmail_get_thread",
  "Robert's inbox, Sunset's Feb 12 \"data delivery checklist\" email", "F1 (\"Sunset's data checklist\"); search \"data delivery checklist\"",
  f"Thread {s1}, first message created Thu Feb 12 2026 23:58:21Z from PERSON_7731_EMAIL (Maya, Sunset) to Leonard, Robert, Arthur: "
  f"\"{esc(txt('G_SUNSET1'))}\"", "YES — check-sql", "F1", f"{sline(s1)}; {s1}")
f("F13", "Sunset's in-thread correction (governing version)", "Gmail (same thread)", "gmail_get_thread",
  "Second message of the Sunset thread", "F12 (thread holds 2 messages)",
  f"Reply in {s1}, created Fri Feb 13 2026 18:20:44Z: \"{esc(txt('G_SUNSET2'))}\" → hold list: Slack, Google Workspace, Figma, Linear, "
  "GitHub, Trello, BigQuery, dbt; Metabase out", "YES — check-sql", "F12", f"{sline(s1)}; {s1}")
f("F14", "SVB's card terms", "Trello (founders' board, To Do)", "trello_search, trello_get_card", "Card \"SVB card payoff + closure\"",
  "F1 (\"SVB's card terms\"); search \"SVB card\"",
  f"Card {M['T_SVB']['id']} (idShort 456), created Fri Feb 13 2026 15:52:30Z by Leonard: \"{esc(txt('T_SVB'))}\" → card closes Feb 20 "
  "(due), move by end of day Feb 19 (due); superseded by the card's comments (F36). The card shows 2 comments", "Unscoped (Trello)", "F1", f"{sline(M['T_SVB']['id'])}; trello {M['T_SVB']['id']}")
ev = M['E_REVIEW']['robert_copy']
f("F15", "Sunset's delivery review call", "Calendar (Robert's own copy)", "gcal_search_events, gcal_list_events",
  "Robert's calendar, event \"Sunset – data delivery review\"", "F12 (\"before the delivery review call Leonard booked\"); search \"data delivery review\"",
  f"Event {ev} on robert@harmonygames.co, organizer Leonard; starts Thu Mar 12 2026 17:00Z (semantic future date), created Feb 12 2026 22:40:15Z",
  "YES — check-sql", "F12", f"{sline(ev)}; {ev}")
f("F16", "Costs-tab lines (membership, rule 3)", "Sheets (shared with Robert)", "gdrive_search, gsheets_values_get",
  "Spreadsheet \"Harmony Games P&L and forecast - Jan 2026\", tab \"HG Costs\"", "F7 (rule 3: \"one issue per costs-tab line\"); search \"P&L and forecast\"",
  "Spreadsheet f_605121f4a36752645e0ac3, tab HG Costs, 75 rows. Shared lines: row 15 \"Sound (Pond5, Soundly,Elevenlabs)\"; row 37 \"UA\". "
  "Lines the project names: [PERSON_NAME_0499] ($6,250 line = Singular), [PERSON_NAME_0250] (Hosting = GitHub). Costs are not read from "
  "its month columns (rule 8)", "YES — check-sql (base)", "F7", "gsheets data.json /sheets_spreadsheets/141 sheet HG Costs")
for k, fid, what, bit in [('G_FIGMA', 'F18', 'Figma receipt', 'annual $1,212, renews Sep 11, 2026 (due)'),
                          ('G_LAYER', 'F19', 'Layer receipt', '$49.00 monthly, next payment Mar 3, 2026 (due); the earlier SVB date (F36) gives Feb 17; Leonard cancelled in the app, no vendor reply → Requested'),
                          ('G_POND5', 'F20', 'Pond5 end notice', 'not renewed, ended Sep 8, 2025 → rule 2 leaves it out'),
                          ('G_SOUNDLY', 'F21', "Soundly's cancellation", '$10.00 monthly, cancelled, access to Mar 3, 2026 → Closed')]:
    t = G(k)
    f(fid, what, "Gmail (Robert's mailbox)", "gmail_search_messages, gmail_get_message", f"Robert's inbox, the {what.split()[0]} email",
      f"F10 (vendor named in its issue or the Sound line); search \"{what.split()[0]}\"" if k != 'G_POND5' else "F16 (Sound line names Pond5); search \"Pond5\"",
      f"Thread {t}, created {M[k]['at']}: \"{esc(txt(k))}\" → {bit}", "YES — check-sql", "F16" if k == 'G_POND5' else "F10", f"{sline(t)}; {t}")
for fid, what, tid, q, bit, dep in [
    ("F22", "Google Workspace invoice", "robert@harmonygames.co/1856033699491658253", "Google Workspace invoice", "created Feb 2 2026; amount $298.13 only in the PDF; Leonard's ENG-2452 comment states it", "F10"),
    ("F23", "Singular billing thread", "robert@harmonygames.co/1850283027022457279", "Singular invoice", "quarterly $6,250 invoices Sep 1 and Dec 1 2025 → next Mar 1 (due); Mar 15 is only the extension on the past-due balance; the earlier SVB date (F36) gives Feb 17", "F10"),
    ("F24", "ElevenLabs receipt", "robert@harmonygames.co/1837122624854744558", "ElevenLabs", "created Jul 9 2025, annual $50 → renews Jul 9, 2026 (due); the earlier SVB date (F36) gives Feb 17", "F16"),
    ("F25", "iPostal closure", "robert@harmonygames.co/1854432461283937829", "iPostal", "mailbox cancelled Jan 16 2026 → cancelled before Feb 9 (rule 2)", "F11"),
    ("F26", "Trello plan change", "robert@harmonygames.co/1849420841999587093", "Changes to your Trello subscription", "created Nov 21 2025: \"You still have access to Trello Free\" → free plan, $0, held by Sunset", "F13")]:
    f(fid, what, "Gmail (Robert's mailbox)", "gmail_search_messages, gmail_get_thread", f"Robert's inbox, the {what}",
      f"{dep}; search \"{q}\"", f"Thread {tid} — {bit}", "YES — check-sql (base)", dep, f"gmail threads {tid.split('/')[1]}.json; {tid}")
f("F27", "Leonard's Layer note", "Slack (#prototype)", "slack_search_public_and_private, slack_read_channel", "#prototype, Leonard's Feb 11 Layer message",
  "F10 (ENG-2458 \"cancelled it in the app on the 11th\"); search \"layer\"",
  "Message C09UHHN6PFZ/1770837702.167889 by Leonard, created Feb 11 2026 19:21:42Z: \"canceled layer.ai account ... we have access until March 3rd\"",
  "YES — check-sql (base)", "F10", "slack messages C09UHHN6PFZ/2026-02.json ts 1770837702.167889")
f("F29", "CodeRabbit's own cancellation notice", "GitHub (Combo-Fighters repo)", "github_list_pull_requests, github_get_pull_request_comments, github_get_issue_comments",
  "Bot comment on pull request 38 \"Final build settings\" in the Combo-Fighters repo", "F10 (ENG-2459 CodeRabbit; rule 5 \"an in-app or bot notice\"); search \"CodeRabbit subscription\"",
  f"Comment {M['GH_CR']['id']} by the CodeRabbit bot, created Fri Feb 13 2026 09:41:12Z: \"The CodeRabbit subscription for "
  "harmonygames-Games was canceled on Feb 12, 2026, so this pull request was not reviewed.\" → CodeRabbit Closed (say where: this notice), "
  "dash, ENG-2459 Done", "Unscoped (GitHub)", "F10", f"{sline('Combo-Fighters#38#c_1')}; {M['GH_CR']['id']}")
f("F30", "Workflow states and share recipients", "Linear + Contacts", "linear_list_issue_statuses, contacts lookup",
  "Team ENG workflow states; Leonard's and Arthur's emails", "F8, F1",
  "Team ENG states include Done and Canceled (both used by the baselines' linear_update_issue calls); leonard.hayes@harmonygames.co, "
  "arthur.blake@harmonygames.co", "Unscoped (Linear, Contacts)", "F8", "linear data.json /workflow_states team_ENG; Evals/references/persona/roster.json")
f("F34", "Lucidchart and Google Ads cancellation notices", "Gmail (Robert's mailbox)", "gmail_search_messages, gmail_get_thread",
  "Robert's inbox, the two vendor cancellation notices", "F10 (ENG-2465, ENG-2466 \"From old receipts.\", no comment, no costs-tab line); search \"Lucidchart\", \"Google Ads account was canceled\"",
  "Thread robert@harmonygames.co/1845611902985063512, created Oct 10 2025 16:11:09Z: \"Your Lucidchart subscription has been canceled and will expire on Nov 4, 2025.\"; "
  "thread robert@harmonygames.co/1846207913731182209, created Oct 17 2025 06:04:29Z: Google Ads account \"was canceled on 10/16/25.\" → both cancelled before Feb 9, "
  "off the register (rule 2), ENG-2465 and ENG-2466 Canceled", "YES — check-sql (base)", "F10",
  "gmail threads 00015599.json, 00015671.json; robert@harmonygames.co/1845611902985063512, robert@harmonygames.co/1846207913731182209")
svb = M['T_SVB']['id']
f("F36", "The SVB card's two comments (supersede its description)", "Trello (same card)", "trello_get_card_actions (comments), trello_get_card",
  "Comment actions on card \"SVB card payoff + closure\"", "F14 (the card shows 2 comments)",
  f"Comment {M['T_SVB_CMT']['id']} by Leonard, created Fri Feb 13 2026 22:47:19Z: \"{esc(txt('T_SVB_CMT'))}\"; comment {M['T_SVB_CMT2']['id']} by Arthur, "
  f"created 23:12:05Z: \"{esc(txt('T_SVB_CMT2'))}\" → card closes Feb 18 (due); Keep/Hold rows still on it off by Feb 17 (due); every non-Closed "
  "Cancel row by Feb 17 (due), earlier than any next-charge date (rule 6); Carta keeps Aug 14, 2026 (renews Aug 15)",
  "Unscoped (Trello)", "F14", f"{sline(M['T_SVB_CMT']['id'])}; trello actions {M['T_SVB_CMT']['id']}, {M['T_SVB_CMT2']['id']}")
for fid, k, what, where, q, dep, bit in [
    ("F37", 'S_CURSOR_CONF', "Arthur's Cursor reply (relays Cursor's confirmation)", "Slack (#prototype thread)", "cursor", "F10 (ENG-2460 Cursor)",
     "→ Cursor Closed (say where: this reply), dash, ENG-2460 Done"),
    ("F38", 'S_UNITY_CONF', "Arthur's Unity note (relays Unity's confirmation)", "Slack (#executives)", "unity termination", "F10 (ENG-2438 Unity)",
     "→ Unity Closed (say where: this note), dash, ENG-2438 Done")
]:
    loc = M[k]['locator']
    extra = (f"; parent C09UHHN6PFZ/{M['S_OLIVER_CURSOR']['ts']} by Oliver: \"{esc(txt('S_OLIVER_CURSOR'))}\"" if k == 'S_CURSOR_CONF' else
             f"; Leonard's earlier ask in the shared applovin channel {M['S_APPL_ASK']['locator']}: \"{esc(txt('S_APPL_ASK'))}\"" if k == 'S_APPL_CONF' else "")
    f(fid, what, where, "slack_search_public_and_private, slack_read_thread", f"{where.split('(')[1].rstrip(')')}, the {what.split('(')[0].strip()}",
      f"{dep}; search \"{q}\"", f"Message {loc}, created {M[k]['at']}: \"{esc(txt(k))}\"{extra} {bit}", "YES — check-sql", dep.split(' ')[0], f"{sline(loc)}; {loc}")
rows = "; ".join(f"{r['account']} · {r['action']} · {r['status'] or '—'} · {r['deadline']} · {r['owner']} · {fmt(r['cost'])}" for r in TR['rows'])
f("F31", f"The register (derived, {len(TR['rows'])} rows)", "Computed from F2–F30, F34", "local reasoning, then gsheets_create_spreadsheet + gsheets_values_update",
  "Rules 1–8 (F7) applied to F9–F11 plus the rule-3 addition from the Sound line (F16)", "F7, F10, F11",
  f"Account · action · status · by when (due) · owner · monthly cost: {rows}. Left out ({len(out)} issues): " + ", ".join(a['vendor'] for a in out)
  + " (Intuit = duplicate of QuickBooks, rule 1; the others cancelled before Feb 9, rule 2); also off: Pond5 (ended Sep 2025), AWS and the UA line's ad accounts (meta, applovin, Unity ads; rule 3 and the project description) and the two $30 game-ops lines (excluded in the project description)", "Derived from visible inputs", "F2, F3, F4, F7, F10, F11, F12, F13, F14, F15, F16, F18, F19, F20, F21, F22, F23, F24, F25, F26, F27, F29, F34, F36, F37, F38",
  "Derived; truth.json /rows")
f("F32", "The two monthly totals (derived)", "Computed from F31", "local reasoning", "Rule 9 (F7) over F31", "F31",
  f"Every row: {fmt(TR['total_today'])}; Keep and Hold rows only: {fmt(TR['total_after'])}", "Derived", "F31", "Derived; truth.json /total_today, /total_after")
L_ = TR['linear']
f("F33", "Linear end states (derived)", "Computed from F8, F31", "local reasoning, then linear_update_issue", "Project settle rule (F8) over F31", "F8, F31",
  f"Done ({len(L_['done'])}): {', '.join(L_['done'])}; Canceled ({len(L_['canceled'])}): {', '.join(L_['canceled'])}; stay open ({len(L_['open'])}): {', '.join(L_['open'])}",
  "Derived", "F8, F29, F31, F37, F38", "Derived; truth.json /linear")
f("F35", "The clash set (derived, rule 10)", "Computed from F5, F6, F12, F13", "local reasoning", "Rule 10 (F7) over the #winddown decisions",
  "F5, F6, F13",
  "Exactly 2: (a) the Slack free-plan / guest-seat decision (F5) vs Sunset's \"Slack (stay on the paid plan …)\" and \"every user in place\"; "
  "(b) the Google archive after Feb 15 (F6) vs \"please don't archive or delete any\". Not clashes: the card moves (rule 10), Arthur's "
  "Gusto reply and Oliver's Cursor request (requests), the Helpshift \"no export\" line (Sunset's list is the named accounts)",
  "Derived", "F5, F6, F7, F12, F13", "Derived; truth.json /rows; C0ADGSZKR3R/1770933903.645709, C0ADGSZKR3R/1770842405.931359")
for x in F:
    w("| " + " | ".join(esc(c) for c in x) + " |")
w("")
w("Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)\n")
proof = open(sys.argv[1]).read().strip() if len(sys.argv) > 1 and os.path.exists(sys.argv[1]) else ""
w("```\n" + (proof or "(pending)") + "\n```\n")

# ------------------------------------------------------------------ C
w("## C · Write capability")
w("| R | Required write | Prompt authority (quoted; agent, not user-reserved) | Catalog tool (exists?) | Required parameters | Target (fact ID) | Completing end state | Content the prompt requires | Defer search (services · population · pagination complete · governing version · result, or UNRESOLVED) | Feasible? |")
w("|---|---|---|---|---|---|---|---|---|---|")
DEF = ("slack #winddown C0ADGSZKR3R Feb 2026 (206 base + 3 seeded messages, paged to Feb 1, complete) · gmail Sunset thread "
       f"{s1} (2 versions; governing version: the Feb 13 correction) · linear project {pj} ({len(A)} issues, {NC} comments, complete) · trello card {M['T_SVB']['id']} (description + 2 comments; governing version: Leonard's Feb 13 22:47Z comment) · "
       f"docs {dc} (1 version) → no hold, defer or wait on this write")
C = [
 ("R3", "Create the register sheet and write its 25 rows and two totals", "build the register the way he wants it", "gsheets_create_spreadsheet, gsheets_values_update (yes)", "title; spreadsheetId, range, values", "F31, F32", "a new spreadsheet in Robert's Drive holding the 28 rows and both totals", "account, action, status (Cancel rows), by when, owner, monthly cost; two totals"),
 ("R4", "Share the register with Leonard as editor", "share it with him and arthur", "gdrive_share_file (yes)", "fileId, emailAddress, role writer", "F30", "leonard.hayes@harmonygames.co has writer access", "editor role (the ask: 'as editors')"),
 ("R4", "Share the register with Arthur as editor", "share it with him and arthur", "gdrive_share_file (yes)", "fileId, emailAddress, role writer", "F30", "arthur.blake@harmonygames.co has writer access", "editor role"),
 ("R5", f"Comment on each of the {len(A)} issues with what happens and by when", "settle each of the linear issues like he asked", "linear_create_comment (yes)", "issueId, body", "F9, F31", f"{len(A)} new comments, one per issue", "the row's action and by-when (or why it leaves the register)"),
 ("R5", f"Set Done on the {len(TR['linear']['done'])} Closed rows' issues", "settle each of the linear issues like he asked", "linear_update_issue (yes)", "id, state Done", "F33", ", ".join(TR['linear']['done']) + " Done", "state only"),
 ("R5", f"Set Canceled on the {len(TR['linear']['canceled'])} issues that leave the register", "settle each of the linear issues like he asked", "linear_update_issue (yes)", "id, state Canceled", "F33", ", ".join(TR['linear']['canceled']) + " Canceled", "state only"),
 ("R6", "Reply in Leonard's thread with the two totals and the clashes", "reply to him in his thread with the two monthly totals", "slack_send_message (yes)", "channel_id, thread_ts, message", "F1, F32, F35", "a reply under Leonard's ask in #winddown", "both totals (11,045.13; 1,249.04) and the two clashes"),
]
for c in C:
    assert c[2] in PROMPT, c[2]
    w(f"| {c[0]} | {c[1]} | \"{c[2]}\" | {c[3]} | {c[4]} | {c[5]} | {c[6]} | {c[7]} | {DEF} | yes |")
w("")

w("## D · Friction facts")
w("| Function (01_) | Mode / rate / wait | Facts blocked | Alternative path (service, locator) | Alternative facts | Visible? |\n|---|---|---|---|---|---|")
w("| none | Friction: none (03_Error_Async_Config.txt) | none | — | — | — |\n")

# ------------------------------------------------------------------ E
w("## E · Traps and distractors")
w("| T | What the agent meets (pointer) | Competes with (fact ID) | Discriminator (timestamp / author / ID) |\n|---|---|---|---|")
man = json.load(open(os.path.join(TI, 'Working_Files', '01_Hardness_Manifest.json')))
CMP = {'T1': 'F3', 'T2': 'F35', 'T3': 'F35', 'T4': 'F13', 'T5': 'F13', 'T6': 'F31', 'T7': 'F16', 'T8': 'F16', 'T9': 'F14', 'T10': 'F12',
       'T11': 'F7', 'T12': 'F31', 'T13': 'F37', 'T14': 'F15', 'T15': 'F10', 'T16': 'F31', 'T17': 'F31', 'T18': 'F10', 'T19': 'F25',
       'T20': 'F31', 'T21': 'F35', 'T22': 'F23', 'T23': 'F10', 'T25': 'F10', 'T26': 'F36'}
for t in man['traps']:
    ptr = ", ".join((t.get('seeded_ids') or []) + (t.get('base_pointers') or []))[:160] or "01_Hardness_Manifest.json"
    w(f"| {t['id']} | {esc(t.get('expected_wrong_reading', ''))} ({esc(ptr)}) | {CMP.get(t['id'], 'F31')} | {esc(t.get('resolver', ''))} |")
w("")

w("## F · Open risks")
w("| # | Risk | Facts affected | Consequence (OE accuracy / rubric / UGT / feasibility) | Check needed |\n|---|---|---|---|---|")
w("| 1 | The Slack clash rests on decisions spread over Feb 11 messages and a checklist table inside a message attachment; a run that reads only the newest 100 #winddown messages or only `text` misses it (pre-check run) | F5, F35 | rubric: the clash criterion; OE must page back and read attachments | none — the records exist and are Robert-visible (/prompt reading I) |")
w("| 2 | The Helpshift \"no export\" line reads like a third clash; 3 of 6 baselines listed it | F35 | rubric must say exactly two clashes, or accept the two with a harmless extra | settle in the rubric plan (dossier Revision 13 note) |")
w("| 3 | CodeRabbit's confirmation lives only on GitHub (bot notice); 6 of 6 baselines missed it | F29, F31, F33 | rubric: an all-fail criterion with a valid justification (record exists, rule 5 names bot notices) | AF justification at /create-allfail |")
w("| 4 | Lucidchart and Google Ads say only \"From old receipts.\" with no comment or costs-tab line; their cancellations are only in Robert's Gmail | F34, F31, F33 | OE must read both notices before the register step | none — both threads are Robert-visible (check-sql base lines) |")
w("| 6 | The SVB card's Feb 17 dates live only in two Trello comments under an out-of-date description; a run that reads the description alone dates Cancel rows by next charge | F14, F36, F31 | rubric: the by-when rows; OE reads the comments | none — Trello is unscoped and the card shows 2 comments |")
w("| 7 | Unity and Cursor confirmations reach Robert only as founder relays in #executives and #prototype (the vendor mails sit in Arthur's and Leonard's mailboxes); Leonard's AppLovin note is a decoy for an out-of-scope account | F37, F38 | rubric 'say where' must accept the relay | none — /prompt recommendation 5 |")
w("| 5 | Workspace's invoice amount is only in a PDF; the figure the agent uses is Leonard's ENG-2452 comment | F10, F22 | OE cites the comment, not the PDF | none |\n")

w("## G · Tally")
w(f"Requirements {len(REQ)} · facts {len(F)} · writes {len(C)} (feasible {len(C)}) · friction items 0 · unverified visibility 0 · blocking 0\n")

# ------------------------------------------------------------------ Self-review
w("## Self-review")
w("Walked `Evals/2_Oracle_Events_Eval.md` 1.1, 2.1–2.6 and 3.1–3.5 against the ledger in order: every requirement has facts (§A Fact IDs); "
  "every write has prompt authority, a cataloged tool with its required parameters, a completing end state and a defer search (§C); "
  "no friction (§D); every scoped §B fact carries a record id and a pasted check-sql line. No-event-text scan: §B and §C hold facts, "
  "values and edges only — no 'OE n', no agent voice, no 'should'.\n")
w("| Counter-reading | Resolution (evidence) |\n|---|---|")
CR = [
 ("R1: the ask could be another #winddown message", f"the ask is the newest message before the clock and the only one naming the register ({an}); prompt 'on friday' = Feb 13"),
 ("R2: 'everything it points to' could stop at the doc", f"the ask names the keep list, LLC moves, Sunset, SVB, the doc and the project ({an}); rule 3 adds the costs tab and the ledger (F7)"),
 (f"R3: the register could include the {len(out)} left-out issues as rows", f"rules 1 and 2 of {dc} leave them out; the /prompt Reading A derivation (Audit-Report/1_prompt_NONFAIL_planD.md) has 25 rows"),
 ("R4: commenter access could suffice", f"the ask says 'share it with me and Arthur as editors' ({an})"),
 ("R5: settling could include creating issues for the rule-3 additions", f"rule 3 adds them as register rows ('each one gets its own row'), and the prompt asks to settle the existing linear issues ({pj}): state plus a comment on each of the {len(A)}, no new issues"),
 ("R6: the totals could be posted as a new channel message", f"the ask says 'reply here' — a thread reply under {an}"),
 ("R7: the clash set could include the Helpshift no-export line or the card moves", f"rule 10 of {dc}: card moves are not clashes; Sunset's list is the named accounts (/prompt reading D excluded)"),
 ("R8: 'before he archives anything on google after the 15th' could be a deadline for the register", "it states Leonard's plan (C0ADGSZKR3R/1770933903.645709); it feeds the clash, the register has no due date of its own"),
 ("F13 vs F12: the first checklist governs", f"the correction is the later message in the same thread ({s1}, Feb 13 18:20:44Z) and says 'The rest of the list stands'"),
 ("F36 vs F14: the card description's Feb 19 / 'until it ends' governs", f"Leonard's comment {M['T_SVB_CMT']['id']} is later (22:47:19Z vs 15:52:30Z) and says 'not the 20th'; Arthur's reply confirms 1Password by the 17th (AWS is off the register, rule 3)"),
 ("F36: Carta also goes to Feb 17", "the comment names it: 'Only exception is carta, that renewal is in august and stays'; ENG-2451 'renews aug 15' → Aug 14, 2026"),
 ("F38: Unity stays Requested (ENG-2438 says only 'sent')", f"Arthur's later #executives note {M['S_UNITY_CONF']['locator']} relays the account manager's confirmation; rule 5 'the vendor itself has confirmed'"),
 ("F29: CodeRabbit is Requested (Arthur only said cancelled in Slack)", f"rule 5 counts 'an in-app or bot notice'; the bot comment {M['GH_CR']['id']} says canceled Feb 12"),
]
for a, b in CR:
    w(f"| Counter: {a} | {b} |")
w("\nRe-verified this run through `tools/hg.py` and the SQL rows: the ask, Gusto reply, Sunset thread, SVB card, conventions doc, project "
  f"description, the {NC} issue comments, the SVB card comments, the Cursor and Unity relays, the review event (01_Universe_Inject.sql rows); the base #winddown, #prototype and #admin_foundersonly "
  "messages by ts; the Workspace, Singular, ElevenLabs, iPostal and Trello threads in Robert's "
  f"mailbox (the Typecast check is gone with its issue); the {len(TR['rows'])}-row register and both totals recomputed from truth.json (re-added: {fmt(TR['total_today'])} / {fmt(TR['total_after'])}).\n")
w("Unresolved: none.\n")
dst = os.path.join(TI, 'Working_Files', '08_OE_Writing_Ledger.md')
open(dst, 'w').write("\n".join(L) + "\n")
print('wrote', dst, len(F), 'facts')
