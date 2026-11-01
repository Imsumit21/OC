"""Writes task_inputs/Working_Files/01_Grounding_Dossier.md. argv[1] = capture dir with the tool outputs
(sql_lint.txt, base_check.txt, hardness_sql.txt, checksql.txt, fact_check.txt, collisions.txt)."""
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
SQ = json.load(open(os.path.join(HERE, 'sql_ids.json')))
MAN = json.load(open(os.path.join(BUNDLE, 'task_inputs', 'Working_Files', '01_Hardness_Manifest.json')))
A, ADDED = ACC['accounts'], ACC['added']
cap = lambda n: open(os.path.join(CAP, n)).read().rstrip()
G = lambda k: M[k]['robert_message']
GT = lambda k: M[k]['robert_thread']
fmt = lambda x: f"{x:,.2f}"
issue = {a['vendor']: a for a in A}
L = []
w = L.append

w("# Grounding Dossier — rb-winddown-closeout (persona Robert, robert@harmonygames.co)\n")
w("Implements `01_Scenario_Design.md` (review-fixed design, §13) as `task_inputs/01_Universe_Inject.sql`. Builder: "
  "`support/task_work/rb_winddown_closeout/build_sql.py` (ids, wording and truth from `mint_ids.py`; row map "
  "`sql_ids.json`). Clock 2026-02-14T00:00:00Z; latest seeded timestamp 2026-02-13T22:47:19Z. Profile `long` "
  f"(manifest `effective_profile`, author's >150-call band). Statement counts are in the sql_lint output (§13).\n")

# ------------------------------------------------------------------ 1.A
w("## 1.A Structural\n")
w("| Table | Rows (INSERT/UPDATE) | Base sample ids (verbatim) | Notes |\n|---|---|---|---|")
rows = SQ['rows']
cnt = lambda t: f"{len(rows.get(t, []))}/{len(rows.get(t + ' (UPDATE)', []))}"
w(f"| slack.slack_messages | {cnt('slack.slack_messages')} | C0ADGSZKR3R/1770933601.686309 (id 6d8c8d8affd1255b13d8d875f1547e70), C0ADGSZKR3R/1770936725.388049 | id = sha256(channel\\|ts)[:32]; the keep-list parent gets thread_ts_legacy, reply_count 1, reply_users_count 1, latest_reply |")
w(f"| gmail.gmail_threads / gmail_messages | {cnt('gmail.gmail_threads')} · {cnt('gmail.gmail_messages')} | robert@harmonygames.co/1853470745017478863, robert@harmonygames.co/1850283027022457279 | ids `<mailbox>/<Message-ID>`, thread `<mailbox>/<19 digits>`; internal_date = date (ms); reply carries in_reply_to + references |")
w(f"| linear.linear_projects / _project_teams / _project_members | {cnt('linear.linear_projects')} · {cnt('linear.linear_project_teams')} · {cnt('linear.linear_project_members')} | project 1061a4f4-bc6a-45ca-a5b6-7f73d5e0abe2 (GoD - Beta, team_ENG) | uuid-shaped id; team_ENG; lead usr_cc3e90160f490686 |")
w(f"| linear.linear_issues | {cnt('linear.linear_issues')} | ENG-2405 (Todo), ENG-990 (Canceled) | ENG-2438…ENG-2466 after the base maximum ENG-2437; state Todo, no lifecycle stamps; labels/links/relations/state_history `[]` |")
w(f"| linear.linear_comments | {cnt('linear.linear_comments')} | none in base (0 rows; Ask_Carriers §6b verifies injected comments render) | cmt_ + 20 hex; authors usr_cc3e90160f490686, usr_63fffeb4fab5233e, usr_Robert, usr_bdf01b53c6a92c5e |")
w(f"| trello.trello_cards / trello_actions | {cnt('trello.trello_cards')} · {cnt('trello.trello_actions')} | 68c5a49e8491a9d7faf869d0 (idShort 455), createCard 68c5a49e8491a9d7faf869eb | id = 8 hex unix seconds + 16 hex; full badges shape; idShort 456 (SVB, next after the board's last card 455) |")
w(f"| gdrive.drive_files + gdocs.docs_documents | {cnt('gdrive.drive_files')} · {cnt('gdocs.docs_documents')} | f_31115ddb6ed866f2b10d60 (Wind Down Task List, owner 'Resource: 7240535625619857401') | the doc copies the Wind Down siblings' owner and share list |")
w(f"| gsheets.sheets_spreadsheets / sheets_sheets | {cnt('gsheets.sheets_spreadsheets')} · {cnt('gsheets.sheets_sheets')} | f_605121f4a36752645e0ac3 | Arthur's sheet in his root d_cc3e90160f490686039986 |")
w(f"| gcal.gcal_events | {cnt('gcal.gcal_events')} | evt_212e50fb5a53ea8016ce29 (Sunset call, on the three founders' calendars) | one copy per attendee calendar, self:true on the owner's copy, ical 32hex@hg4 |")
w(f"| confluence.confluence_pages / page_versions / comments | {cnt('confluence.confluence_pages')} · {cnt('confluence.confluence_page_versions')} · {cnt('confluence.confluence_comments')} | page_ops_home (parent), comment_analytics_integration_c1 | version 1 rows; space_OPS |")
w(f"| github.github_pull_requests (+branch, commit, pr_commit, pr_comment, timeline) | {cnt('github.github_pull_requests')} … | harmonygames-Games/Combo-Fighters#37, harmonygames-Games/Combo-Fighters#36#c_1 (CodeRabbit skip notice) | #38 open, base develop; CodeRabbit author PERSON_6026_GITHUB_USERNAME, timeline actor SVC_0321_GITHUB_USERNAME (hazard I07 convention) |\n")

# ------------------------------------------------------------------ 1.B
w("## 1.B Entity table\n")
w("| Entity | Canonical | Where it appears (cited) | Agreement |\n|---|---|---|---|")
w("| Robert | robert@harmonygames.co, Slack EMPLOYEE_0016_SLACK_ID, Linear usr_Robert | C0ADGSZKR3R/1770839322.836779; ENG-2440 assignee | AGREE |")
w("| Leonard Hayes | leonard.hayes@harmonygames.co, EMPLOYEE_0038_SLACK_ID, usr_63fffeb4fab5233e, Trello PERSON_6094_TRELLO_USER_ID | C0ADGSZKR3R/1770933601.686309 | AGREE |")
w("| Arthur Blake | arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID, usr_cc3e90160f490686 | C0ADGSZKR3R/1770937232.664809 | AGREE |")
w("| Oliver Brooks | oliver.brooks@harmonygames.co, EMPLOYEE_0003_SLACK_ID, usr_bdf01b53c6a92c5e, EMPLOYEE_0003_GITHUB_USERNAME | harmonygames-Games/Combo-Fighters#37 (merged_by) | AGREE (not Lauren Brooks) |")
w("| Sunset | the wind-down provider signed Feb 12 | robert@harmonygames.co/1856956532017091340 (signed SOW); C0ADGSZKR3R/1770931777.561519 | AGREE; sender token PERSON_7731_EMAIL is new (0 hits) |")
w("| Sherwood Partners | ABC firm consulted, not engaged | robert@harmonygames.co/1856689465442954434 (base thread, PERSON_0728) | AGREE; decoy reuses PERSON_0728_EMAIL |")
w("| SVB card | company card, never given digits in seeds | leonard.hayes@harmonygames.co/1846148320251001978 ('Silicon Valley Bank MasterCard') | AGREE (review A #2 fix) |")
w("| Singular | '[PERSON_NAME_0499]' on the costs tab | f_605121f4a36752645e0ac3 row 36; robert@harmonygames.co/1850283027022457279 | AGREE (trap_catalog X03) |")
w("| Kapwing / dbt | '[PERSON_NAME_20852]' and '[USERNAME_30019]' in #winddown | C0ADGSZKR3R/1770933450.410449 (Leonard's table: 'Kapwing (Blake)', '[USERNAME_30019] (keep it until … stops caring about data)'); C0ADGSZKR3R/1770937232.664809 | AGREE: no relabelling; Kapwing is ENG-2478, dbt's KubLLC move is stated in Arthur's comment on ENG-2457 |")
w("| QuickBooks / Intuit | one vendor | ENG-2460, ENG-2461; costs tab 'Quickbooks'; keep list 'Intuit' | DISAGREE (designed duplicate, rule 1) |")
w("| ElevenLabs | annual Starter, Jul 9 2025–Jul 9 2026, $50 | robert@harmonygames.co/1837122624854744558 | AGREE (base receipt governs; no seeded ElevenLabs mail) |")
w("| Linear plan | Basic annual from the Feb 1 renewal | robert@harmonygames.co/1850617582652876839 (Standard → Basic notice); seeded receipt | AGREE |\n")

# ------------------------------------------------------------------ 1.C
w("## 1.C Voice and realism (speakers, activity, conventions)\n")
w("Lengths, hours and styles from `references/universe_kb/conventions.json` (`slack.per_person_hours_and_style`, "
  "`slack.length_chars_by_channel_type`, `gmail.internal_subject_len_chars`, `linear.title_prefixes_by_team` — ENG titles "
  "are plain nouns, so issues are titled by vendor). Seeded speakers with `status_at_clock` from "
  "`references/universe_kb/activity.json`:\n")
w("| Speaker | activity.json status | Where seeded | Voice evidence |\n|---|---|---|---|")
w("| Leonard Hayes leonard.hayes@harmonygames.co (EMPLOYEE_0038_SLACK_ID) | activity active_feb_2026 | anchor; SVB Trello card; Linear comments; review event organizer | full sentences, plain, long Slack asks (C0ADGSZKR3R/1770933601.686309, /1770934638.035469) |")
w("| Arthur Blake arthur.blake@harmonygames.co (EMPLOYEE_0025_SLACK_ID) | activity active_feb_2026 | Gusto reply; project + issues; Linear comments; 'Subscriptions' sheet | lowercase, short (C0ADGSZKR3R/1770936655.574079 'coderabbit is cancelled') |")
w("| Robert robert@harmonygames.co (EMPLOYEE_0016_SLACK_ID) | activity active_feb_2026 | Linear comments on his creative tools | short lowercase (C0ADGSZKR3R/1770859313.592649) |")
w("| Oliver Brooks oliver.brooks@harmonygames.co (EMPLOYEE_0003_SLACK_ID) | activity active_feb_2026 | #prototype message; Helpshift export comment; PR #38 | casual, lowercase in #prototype (C09UHHN6PFZ, SL-T09 thread roots) |")
w("| Frederick Stone frederick.stone@harmonygames.co | activity quiet_since_2025-10 | Confluence UA page dated 2025-03-18 only (active then) | Growth/UA voice, page_product_okrs owner |")
w("| CodeRabbit PERSON_6026_GITHUB_USERNAME | bot (not in activity.json) | PR #38 notice | base skip-notice shape harmonygames-Games/Combo-Fighters#36#c_1 |")
w("| Sunset PERSON_7731_EMAIL, Sherwood PERSON_0728_EMAIL, vendor senders SVC_* | external (not in activity.json) | mail only | vendor receipts mirror base receipts (robert@harmonygames.co/1849420841999587093) |\n")
w("Posting hours: Leonard 16:12–17:21Z and Arthur 23:52–02:14Z / 19:05Z match their base #winddown hours (Feb 12 "
  "21:00–23:00Z, Feb 11 19–20Z); Robert's comments 20:41–20:51Z sit in his Feb 11 posting window (19:48Z).\n")

# ------------------------------------------------------------------ 1.D
w("## 1.D Keyword / findability (base hit counts via `tools/hg.py search search <svc> <term>`)\n")
w("| Term | Base hits / pointer | Seeded home |\n|---|---|---|")
w(f"| 'data delivery checklist' | NEW TERM — introduced in {G('G_SUNSET1')}, reached via A1 \"Sunset's data checklist\" | Gmail thread {GT('G_SUNSET1')} |")
w(f"| 'checklist' (gmail) | base hits in Robert's mail are unrelated (QA checklists); the seeded Sherwood mail {G('G_SHERWOOD')} shares the word | decoy first by date |")
w(f"| 'SVB card' / 'payoff' | base: C0ADGSZKR3R/1770927223.969899 ('close the credit card'), 162 SVB notification threads (Scenario_Atlas §1) — none dated | Trello {M['T_SVB']['id']} |")
w(f"| 'close-out register conventions' | NEW TERM — introduced in {M['DOC_CONV']['id']}, reached via A1 'conventions doc … Wind Down folder' | Docs; decoy {M['CONF_UA']['id']} shares 'close-out conventions' |")
w(f"| 'Shutdown – accounts' | NEW TERM — introduced in project {M['L_PROJECT']['id']}, reached via A1 'Linear shutdown project' | Linear |")
w("| 'KubLLC' | base C0ADGSZKR3R/1770937232.664809 (1 hit) | Linear comments on ENG-2456, ENG-2477, ENG-2479 |")
w(f"| 'data delivery review' | NEW TERM — introduced in {M['E_REVIEW']['robert_copy']}, reached via the checklist 'delivery review call Leonard booked' | GCal |")
w(f"| 'Pond5' / 'Elevenlabs' | base: costs tab row 15 'Sound (Pond5, Soundly,Elevenlabs)'; robert@harmonygames.co/1837122624854744558 (ElevenLabs) | Pond5 end notice {G('G_POND5')} (ended Sep 8 2025) |")
w(f"| 'coderabbit' (github) | base B03: 417 PR comments by PERSON_6026, e.g. harmonygames-Games/Combo-Fighters#37#c_1 | notice {M['GH_CR']['id']} |\n")

# ------------------------------------------------------------------ 1.E
w("## 1.E Persona reach (scoped records)\n")
w("Every load-bearing seeded record is in Robert's mailbox (INBOX), on his calendar (self copy), shared with him (doc) or in a "
  "Slack channel he belongs to (#winddown C0ADGSZKR3R, #prototype C09UHHN6PFZ). Base Workspace invoice "
  "robert@harmonygames.co/1856033699491658253 sits in SPAM — not load-bearing (Workspace's monthly billing is visible on the "
  "costs tab). Load-bearing ids written one per line to `support/task_work/rb_winddown_closeout/lb_ids.txt`.\n")
w("| Record | Service | Visibility path |\n|---|---|---|")
for k in ('G_SUNSET1', 'G_SUNSET2'):
    w(f"| {G(k)} | gmail | Robert cc'd; own copy INBOX |")
for k in sorted(x for x in M if x.startswith('G_') and x not in ('G_SUNSET1', 'G_SUNSET2', 'G_SHERWOOD') and M[x].get('robert_message')):
    w(f"| {G(k)} | gmail | own copy INBOX (billing mail to robert@harmonygames.co) |")
w(f"| {M['E_REVIEW']['robert_copy']} | gcal | Robert's own calendar copy, self:true |")
w(f"| {M['DOC_CONV']['id']} | gdocs | shared_with robert@harmonygames.co |")
w(f"| {M['S_ANCHOR']['locator']} | slack | member of private #winddown |")
w(f"| {M['S_GUSTO_REPLY']['locator']} | slack | member of private #winddown |")
w("| robert@harmonygames.co/1853470745017478863, robert@harmonygames.co/1850283027022457279, robert@harmonygames.co/1854432461283937829, robert@harmonygames.co/1837122624854744558 | gmail | own mailbox (base) |")
w("| f_605121f4a36752645e0ac3 | gsheets | shared_with robert@harmonygames.co (base) |\n")
w("```\n" + cap('checksql.txt') + "\n```\n")

# ------------------------------------------------------------------ 1.F
w("## 1.F Collision checks\n")
w("Identity tokens: PERSON_7731 and SVC_7702–SVC_7712 have 0 hits across HarmonyGames_Gmail, HarmonyGames_Other_Services and "
  "HarmonyGames_GitHub (`grep -rhoE` over all three, run 2026-10-28); PERSON_0728 (Sherwood), SVC_5771 (Unity), SVC_1177 "
  "(Deel), SVC_0982 (Google Cloud), SVC_2600 (Docusign), SVC_3550 (Soundly), SVC_0124 (Slack), SVC_0251 (Linear) reuse the "
  "vendor's own base token. Minted ids (`hg.py search lookup`, full collections):\n")
w("```\n" + cap('collisions.txt') + "\n```\n")
w("Linear ENG-2438…ENG-2466 follow the base maximum ENG-2437; Gmail ids carry the persona prefix and new Message-IDs; Combo-Fighters #38 "
  "follows the base maximum #37.\n")

# ------------------------------------------------------------------ 2
w("## 2 Record ledger\n")
w("| # | Service · table | Id | Container | Manifest element | Carrier | Reach | Role |\n|---|---|---|---|---|---|---|---|")
n = 0


def led(svc, rid, cont, elem, reach, role):
    global n
    n += 1
    w(f"| {n} | {svc} | {rid} | {cont} | {elem} | ● | {reach} | {role} |")


led('slack.slack_messages', M['S_ANCHOR']['locator'], 'C0ADGSZKR3R', 'A1 anchor', '#winddown member', 'first link')
led('slack.slack_messages', M['S_GUSTO_REPLY']['locator'], 'C0ADGSZKR3R thread 1770933601.686309', 'K9 · T1', '#winddown member', 'overturning')
led('slack.slack_messages (UPDATE)', 'C0ADGSZKR3R/1770933601.686309', 'C0ADGSZKR3R', 'K8 counters', '#winddown member', 'companion')
led('slack.slack_messages', M['S_OLIVER_CURSOR']['locator'], 'C09UHHN6PFZ', 'T21 distractor', '#prototype member', 'decoy')
led('linear.linear_projects', M['L_PROJECT']['id'], 'team_ENG', 'K2 · cohort source', 'unscoped', 'first link')
for a in A:
    led('linear.linear_issues', a['issue'], 'project Shutdown – accounts', 'cohort', 'unscoped', 'write target')
for a in A:
    for cid in a['comment_ids']:
        led('linear.linear_comments', cid, a['issue'], 'cohort surface (linear_list_comments)', 'unscoped', 'evidence')
led('trello.trello_cards', M['T_SVB']['id'], 'board 640643a3fd8f3ca308d9318e To Do', 'H2 · K6', 'unscoped', 'authority')
led('gdocs.docs_documents', M['DOC_CONV']['id'], 'Wind Down d_e5caf6a8c630421942ee59', 'H3 · K7', 'shared', 'authority')
led('gsheets.sheets_spreadsheets', M['SHEET_SUBS']['id'], 'Arthur root d_cc3e90160f490686039986', 'T20 distractor', 'shared', 'decoy')
for k, el, role in (('G_SHERWOOD', 'H1 decoy · T10', 'decoy'), ('G_SUNSET1', 'H1 · K3', 'authority'), ('G_SUNSET2', 'K4 amendment · T4/T5', 'overturning')):
    led('gmail.gmail_messages', G(k), GT(k), el, 'own copy INBOX', role)
for k in sorted(x for x in M if x.startswith('G_') and x not in ('G_SUNSET1', 'G_SUNSET2', 'G_SHERWOOD') and M[x].get('robert_message')):
    led('gmail.gmail_messages', G(k), GT(k), 'cohort surface (billing mail)', 'own copy INBOX', 'evidence')
led('gcal.gcal_events', M['E_REVIEW']['robert_copy'], M['E_REVIEW']['ical_uid'], 'K5 · T14', 'own calendar', 'evidence')
led('confluence.confluence_pages', M['CONF_UA']['id'], 'space_OPS', 'H3 decoy · T11', 'unscoped', 'decoy')
led('github.github_pull_requests', M['GH_PR']['id'], 'harmonygames-Games/Combo-Fighters', 'C5 container', 'unscoped', 'evidence')
led('github.github_pr_comments', M['GH_CR']['id'], M['GH_PR']['id'], 'C5 · T13', 'unscoped', 'evidence')
w("\nCompanion rows (not separate elements): the doc's and sheet's drive_files rows, the sheet tab, page versions, the "
  "Leonard/Arthur mail copies (SENT/INBOX in their own mailboxes, not load-bearing), the PR branch, commit, pr_commit and "
  "timeline event, project team/members, Trello createCard actions.\n")

# ------------------------------------------------------------------ 3
w("## 3 Findability and discovery-order proofs\n")
proofs = [
 ("slack " + M['S_ANCHOR']['locator'], "anchor named by the prompt; #winddown history", "first link", "the prompt names it"),
 (f"linear project {M['L_PROJECT']['id']}", "'shutdown' via linear search / project list", "connecting", "named in A1"),
 (f"gmail {G('G_SUNSET1')}", "'checklist' / 'Sunset' in Gmail", "connecting", f"Sherwood's {G('G_SHERWOOD')} (Feb 12, 18:40Z) sorts before it in date order — decoy met first; Sunset signed Feb 12 decides"),
 (f"gmail {G('G_SUNSET2')}", "read the whole thread (gmail_get_thread)", "overturning", "the first message reads complete; the correction is message 2 (A14)"),
 (f"trello {M['T_SVB']['id']}", "'SVB' / 'card' in Trello", "connecting", "the board also holds base card #170 'move subscriptions to SVB credit card' (Done, 2023–24) — same words, older move"),
 (f"gdocs {M['DOC_CONV']['id']}", "'conventions' / 'close-out' in Docs", "connecting", f"a Confluence-first run meets {M['CONF_UA']['id']} (Growth/UA) first"),
 (f"gcal {M['E_REVIEW']['robert_copy']}", "'Sunset' / 'review' in Calendar", "terminal", "only reached through the checklist's 'review call Leonard booked'"),
 (f"linear ENG-2439 comment {issue['Helpshift']['comment_ids'][0]}", "'Helpshift' in Linear, then list comments", "terminal", "the export status is in Oliver's comment, not the issue"),
 (f"github {M['GH_CR']['id']}", "PRs/comments by CodeRabbit after Feb 12", "terminal", "Arthur's Slack 'coderabbit is cancelled' (C0ADGSZKR3R/1770936655.574079) is met first"),
 (f"slack {M['S_GUSTO_REPLY']['locator']}", "thread replies of the keep list", "overturning", "parent 1770933601.686309 reads conclusive; reply_count 1"),
]
w("| Record | Agent's likely query | Chain position | Discovery order / competing hits |\n|---|---|---|---|")
for p in proofs:
    w("| " + " | ".join(p) + " |")
w("\n**Hidden authorities.** H1 'Sunset's data checklist' → Gmail search 'data delivery checklist' returns only "
  f"{GT('G_SUNSET1')}; decoy Sherwood differs on 'cancel every subscription right away'. H2 'SVB's card terms' → Trello "
  f"search 'SVB card' returns {M['T_SVB']['id']}; decoy Chase card differs on the bank and date. H3 'the conventions doc' "
  f"→ Docs search 'close-out register conventions' returns {M['DOC_CONV']['id']}; decoy UA page differs on the cost and "
  "closed rules (Growth/UA tracker scope).\n")

# ------------------------------------------------------------------ 4
w("## 4 Self-validation\n")
w("| QC category | Tool-enforced (sql_lint / base_check) | Manual (evidence) |\n|---|---|---|")
w("| Missing Universe Data | — | every fact in §9 is in a Robert-readable record; no tool is killed (Friction: none planned) |")
w("| Temporal Field | PASS (base_check Check C) | dates in text agree: receipts' next dates follow their send dates; the checklist (23:58Z) after the event (22:40Z) it calls booked; A1 17:21Z after the doc/card/comments it names |")
w("| Cross-service Referential | PASS (Check A) | Kapwing and dbt follow Leonard's table C0ADGSZKR3R/1770933450.410449 and Arthur's KubLLC message; every PR/issue cited exists (ENG-24xx, Combo-Fighters#38) |")
w("| Quantitative / Reconciliation | PASS (keep-list counters) | every cost is the owner's figure in the issue or the account's own last invoice, each equal to its latest base charge (Unity Pro 2,348.50 Jan 19; Slack 87.22 Feb 3; GitHub 90 Feb 3; BigQuery 4.97 Feb 1; Workspace 298.13 Feb 2; Metabase 148; dbt 100; QuickBooks 115; Gusto 116; Helpshift 150); the costs tab is used for membership only, and no graded value reads the finance ledger or the costs tab's AWS/UA rows (AWS and the UA line are out of scope, rule 3); Arthur's sheet is deliberately stale (T20) |")
w("| State / Lifecycle | PASS (Linear issues Todo without stamps) | no status contradicts activity: issues stay Todo for the agent to settle; Singular's termination asks for confirmation that never came |")
w("| Identifier / Format | PASS (sha ids, Message-IDs, f_ ids, evt_/ical, cmt_, Trello timestamped ids) | sender tokens reused from the base where the vendor exists |")
w("| Semantic / Category | — | issue titles = vendor names; card/list names match content; page title matches its body |")
w("| Other | — | no seeded record states a register cell; voice per §1.C |\n")

# ------------------------------------------------------------------ 5
w("## 5 Lazy-solver pass on the implemented records\n")
w("A run that lists the project, reads #winddown and the first Gmail hit and stops: gets the Keep/Move actions and the tab "
  "costs (if it copies the costs tab's December figures), misses the Gusto reply, Sunset's correction (Trello/dbt/BigQuery/Metabase), the card "
  "deadline, the review date, CodeRabbit's notice, the Helpshift switch-over, the UA accounts, the Sound split and every "
  "per-issue status/owner/exclusion that only a comment carries. Implemented records add no shortcut: issue descriptions "
  "carry only the source ('From costs tab.'), the SVB card names no account, receipts vary their card wording, and Arthur's "
  "sheet holds stale figures.\n")

# ------------------------------------------------------------------ 6
w("## 6 Intended disagreements\n")
w("| Disagreement | Older claim | Overturning record | Why realistic |\n|---|---|---|---|")
w(f"| Gusto kept vs cancelled | C0ADGSZKR3R/1770933601.686309 (Feb 12 22:00Z) | {M['S_GUSTO_REPLY']['locator']} (Feb 13 02:14Z) | Arthur exports the docs that night and replies in the thread |")
w(f"| Slack downgrade / guest seats vs paid with every user | C0ADGSZKR3R/1770840054.486779, C0ADGSZKR3R/1770842405.931359 (Feb 11) | {G('G_SUNSET1')} (Feb 12 23:58Z) | the data deal came after; the founders haven't reconciled it — the reply must report it |")
w(f"| Google archive after Feb 15 vs no archiving | C0ADGSZKR3R/1770933903.645709 (Feb 12 22:05Z) | {G('G_SUNSET1')} | same; a clash to report |")
w(f"| Metabase held vs not in the bundle | {G('G_SUNSET1')} | {G('G_SUNSET2')} (Feb 13 18:20Z) | Sunset's engineers map the data a day later |")
w(f"| Sherwood's 'cancel everything' vs Sunset's list | {G('G_SHERWOOD')} (Feb 12) | {G('G_SUNSET1')} | different issuer; Sherwood not engaged |")
w(f"| Docusign owner Leonard vs Robert | ENG-2469 assignee | {issue['Docusign']['comment_ids'][0]} (Feb 13 16:33Z) | handover in a comment |")
w(f"| Arthur's 'Subscriptions' sheet vs the project | {M['SHEET_SUBS']['id']} (Feb 10) | project {M['L_PROJECT']['id']} (Feb 12, 'replaces my subscriptions sheet') | a rough first list, rounded |\n")

# ------------------------------------------------------------------ 7
w("## 7 Constraints for the prompt brief\n")
w("| Anchor | May be named (noun phrases only) | Record |\n|---|---|---|")
w(f"| A1 | Leonard's close-out register ask; Leonard's #winddown request | {M['S_ANCHOR']['locator']} |\n")
w("Never name: Sunset's list or its correction, the SVB date or the Trello board, the conventions doc's rules, the ledger, "
  "the Sound line, any account, the review date, the Helpshift page, CodeRabbit's notice, the totals, ids. Deadline: "
  "before Leonard archives the Google accounts (after Feb 15). Deliverables: the register sheet shared with Leonard and "
  "Arthur, the Linear issues settled, a reply in Leonard's thread.\n")

# ------------------------------------------------------------------ 8
w("## 8 Fact sheet\n")
w("| Key | Value | Kind | Home / must appear in |\n|---|---|---|---|")
for f in MAN['facts']:
    w(f"| {f['key']} | {f['value']} | {f['kind']} | {', '.join(f.get('must_appear_in', []))} |")
w("\n`fact_check.py --no-leak` (verbatim):\n")
w("```\n" + cap('fact_check.txt') + "\n```\n")
w("Warning dispositions (fact_check): the value_drift warnings pair different vendors' prices/dates under one common word "
  "('monthly', 'annual', 'invoice', 'payment') — distinct accounts, not drift.\n")

# ------------------------------------------------------------------ 9
w("## 9 Facts for the human\n")
w("### 9.1 Records\n")
w("| Locator | Base/seeded | Fact (UTC) | Reach | Role |\n|---|---|---|---|---|")
w(f"| {M['S_ANCHOR']['locator']} | seeded | Leonard → Robert {M['S_ANCHOR']['at']}: own the register; share with Leonard and Arthur as editors; settle each Linear issue with a line on each; reply with the two totals and the clashes | #winddown member | claim/ask (anchor) |")
w(f"| {M['S_GUSTO_REPLY']['locator']} | seeded | Arthur {M['S_GUSTO_REPLY']['at']}: Gusto: docs pulled, 'let's cancel before mar 3' | #winddown member | overturning evidence |")
w("| C0ADGSZKR3R/1770933601.686309 | base | Leonard Feb 12 22:00Z: keep Deel, gusto, Intuit; Figma won't charge before renewal; Linear kept | #winddown member | claim met first |")
w("| C0ADGSZKR3R/1770937232.664809 | base | Arthur Feb 12 23:00Z: moving github, dbt ([USERNAME_30019]) and Metabase to his KubLLC card | #winddown member | evidence |")
w("| C0ADGSZKR3R/1770840054.486779 | base | Arthur Feb 11: 'yeah free version' (Slack) | #winddown member | clash 1 |")
w("| C0ADGSZKR3R/1770842405.931359 | base | Leonard Feb 11: keep the three founders as paid Slack seats | #winddown member | clash 2 |")
w("| C0ADGSZKR3R/1770933903.645709 | base | Leonard Feb 12: archive Google accounts after Feb 15 | #winddown member | clash 3 |")
w(f"| {G('G_SUNSET1')} | seeded | Sunset {M['G_SUNSET1']['at']}: hold Slack (paid), Google Workspace (all users), Figma, Linear, GitHub, Metabase until the review call; export Helpshift | own INBOX | authority (H1) |")
w(f"| {G('G_SUNSET2')} | seeded | Sunset {M['G_SUNSET2']['at']}: Trello in, Metabase out, BigQuery and dbt in | own INBOX | overturning evidence |")
w(f"| {G('G_SHERWOOD')} | seeded | Sherwood Feb 12: cancel everything except payroll/accounting | own INBOX | decoy |")
w(f"| {M['E_REVIEW']['robert_copy']} | seeded | review call 2026-03-12 17:00–17:45Z (created Feb 12 22:40Z) | own calendar | evidence |")
w(f"| {M['DOC_CONV']['id']} | seeded | conventions rules 1–10 (membership, exclusions, statuses, deadlines, costs, totals, clashes) | shared | authority (H3) |")
w("| f_605121f4a36752645e0ac3 | base | HG Costs cost lines (membership; the Sound shared line; the UA line is out of scope) | shared | evidence |")
w("| robert@harmonygames.co/1850283027022457279 | base | Singular quarterly invoice Dec 1 (Sep 1 earlier) → next Mar 1 | own mailbox | evidence |")
w("| robert@harmonygames.co/1853470745017478863 | base | Leonard's Feb 12 21:43Z termination asks Singular to confirm in writing; no reply | own mailbox | evidence |")
w("| robert@harmonygames.co/1854432461283937829 | base | iPostal1 mailbox closed Jan 16 2026 | own mailbox | evidence (exclusion) |")
w("| robert@harmonygames.co/1837122624854744558 | base | ElevenLabs Starter annual $50, Jul 9 2025–Jul 9 2026 | own mailbox | evidence |")
for k in sorted(x for x in M if x.startswith('G_') and x not in ('G_SUNSET1', 'G_SUNSET2', 'G_SHERWOOD') and M[x].get('robert_message')):
    w(f"| {G(k)} | seeded | {M[k]['at']}: {P[k][:110]} | own INBOX | evidence |")
w(f"| {M['T_SVB']['id']} | seeded | card description {M['T_SVB']['at']}: SVB closes the card Feb 20; move kept charging accounts by Feb 19 | unscoped | authority (H2), superseded |")
w(f"| {M['T_SVB_CMT']['id']} (commentCard on the same card) | seeded | Leonard {M['T_SVB_CMT']['at']}: closes the 18th; keep-rows off it and every cancellation by end of day the 17th, Carta excepted (its August renewal stays) | unscoped | authority (H2), governing version |")
w(f"| {M['T_SVB_CMT2']['id']} (commentCard, Arthur) | seeded | Arthur {M['T_SVB_CMT2']['at']}: AWS and 1Password go by the 17th too (store transfer done; logins in his own vault) | unscoped | supersedes his ENG-2464 1Password comment; AWS is context (out of scope, rule 3) |")
w(f"| {M['S_CURSOR_CONF']['locator']} (#prototype, reply to Oliver's Cursor ask) | seeded | Arthur {M['S_CURSOR_CONF']['at']}: it's already gone, Cursor sent the cancellation confirmation, seats until Mar 5 | member | rule 5 vendor word → Cursor Closed |")
w(f"| {M['S_UNITY_CONF']['locator']} (#executives) | seeded | Arthur {M['S_UNITY_CONF']['at']}: Unity's account manager confirmed the termination, no invoice on the 19th | member | rule 5 vendor word → Unity Closed |")
w(f"| {M['S_APPL_ASK']['locator']} (applovin_ Slack Connect) | seeded | Leonard {M['S_APPL_ASK']['at']}: asks AppLovin to close the ad account after this week's spend | member | context |")
w(f"| {M['S_APPL_CONF']['locator']} (#admin_foundersonly) | seeded | Leonard {M['S_APPL_CONF']['at']}: AppLovin emailed back, the ad account is closed as of today's spend | member | decoy: the UA line's ad accounts stay off the register (rule 3) |")
w(f"| {M['GH_CR']['id']} | seeded | CodeRabbit {M['GH_CR']['at']}: subscription canceled on Feb 12 | unscoped | evidence |")
w(f"| {issue['Helpshift']['comment_ids'][0]} on ENG-2439 | seeded | Oliver 2026-02-13T15:12:18Z: Helpshift ticket history exported (helpshift_export_2026-02-13.zip) | unscoped | overturning evidence |")
w("\n### 9.2 Derived ground truth (from the records above; for the human's Oracle Events and rubric)\n")
w("| Account | Issue | Action | Status | Deadline | Owner | Monthly cost | Evidence |\n|---|---|---|---|---|---|---|---|")
for r in TR['rows']:
    ev = ', '.join(G(x) if x.startswith('G_') else (M[x]['robert_copy'] if x == 'E_REVIEW' else (M[x]['id'] if x in M else ('snowflake.wh_finance__expenses__finance_ledger ' + x if x.startswith('FIN-') else x))) for x in r['evidence']) or 'f_605121f4a36752645e0ac3 / comments'
    w(f"| {r['account']} | {r['issue']} | {r['action']} | {r['status'] or '—'} | {r['deadline']} | {r['owner']} | {fmt(r['cost'])} | {ev} |")
w(f"\nTotals: today **{fmt(TR['total_today'])}**, Keep + Hold **{fmt(TR['total_after'])}**. Linear: Done "
  f"{', '.join(TR['linear']['done'])}; Canceled {', '.join(TR['linear']['canceled'])}; "
  f"a comment on each of the {len(A)} issues (no new issues: rule 3 additions are register rows). Reply clashes: Slack free plan, "
  "Slack guest seats, Google archiving (extras accepted).\n")

# ------------------------------------------------------------------ 10
w("## 10 Integrations and companions\n")
w("| Service | INT id | Companion | Decision |\n|---|---|---|---|")
w("| github | INT-01 | Slack mirror | none: Combo-Fighters is outside INT-01's mirrored repos |")
w("| github | INT-23 | CodeRabbit author + SVC_0321 timeline actor | seeded (commented event #38#ev_1) |")
w("| github | INT-12 | notification mail | none: Robert is not a PR participant |")
w("| linear | INT-03 / INT-04 / INT-05 | linear[bot], Slack app, digests | none: no PR names an ENG-24xx key; the ENG team has no Slack feed in 2026; no digest seeded |")
w("| gcal | INT-11 | invitation mails | seeded: 'Invitation: Sunset – data delivery review @ Thu Mar 12, 2026 10am - 10:45am (PDT)' from Leonard in Robert's and Arthur's mailboxes (Feb 12 22:40Z) |")
w("| slack | INT-17 | Slack Connect | seeded message in the existing applovin_ shared channel (Leonard; the AppLovin side's last speaker went quiet Dec 2025, so its reply is by email) |")
w("| slack | INT-22 | email notification | none |")
w("| trello | INT-21 | Slack posts | none: no integration exists |")
w("| gdrive | INT-13 | Drive Slack DM | none |")
w("| gmail | none | — | gmail: no outbound integration |")
w("| confluence | none | — | confluence: version 1 rows seeded with each page |")
w("| gsheets / gdocs | none | — | gdocs: drive_files twin rows with identical sharing |\n")

# ------------------------------------------------------------------ 11
w("## 11 Touched-data census and coherence hazards\n")
w(f"Touched: #winddown Feb 9–13 (incl. the keep-list thread), #prototype's Oliver message, the {len(A)} issues and their comments, "
  "the project, Robert's billing mail (seeded + base Singular, iPostal, Trello, ElevenLabs, Linear notice), Sunset/Sherwood "
  "threads, the two Trello cards on board 640643a3fd8f3ca308d9318e, the conventions doc and Arthur's sheet, the costs tab "
  "f_605121f4a36752645e0ac3, the review event, the support handover page, the UA page, "
  "Combo-Fighters#38. Hazards from `references/universe_kb/coherence_hazards.json`:\n")
w("| Hazard id | Category | Disposition |\n|---|---|---|")
for hz, cat, d in [("T02", "temporal", "seeded threads in date order"), ("T08", "temporal", "Leonard/Oliver active_feb_2026"),
                   ("S08", "semantic", "page_support_playbook avoided (export logged on a seeded page)"),
                   ("S06", "semantic", "Contacts titles not used"),
                   ("R04", "referential", "folder named by title only"), ("R08", "referential", "event has its invitation mails (Robert, Arthur) and no orphan mail"),
                   ("Q07", "quantitative", "Helpshift balances are distractor text; cost from the tab"),
                   ("Q01", "quantitative", "keep-list parent counters updated with the reply"),
                   ("L13", "state/lifecycle", "Combo-Fighters#37 untouched; notice on #38 (hazard_acknowledgements excluded)"),
                   ("L08", "state/lifecycle", "issues assigned to active founders only"),
                   ("I10", "identifier/format", "usr_Robert used verbatim"), ("I14", "identifier/format", "doc owner = Wind Down siblings' Resource owner"),
                   ("I07", "identifier/format", "CodeRabbit comment author PERSON_6026 with SVC_0321 timeline actor, as in base")]:
    w(f"| hazard {hz} | {cat} | {d} |")
w("")

# ------------------------------------------------------------------ 12
w("## 12 Platform follow-ups\n")
w("- Linear comments are ● (Ask_Carriers §6b); confirm in the Opus pre-check that `linear_list_issues` returns no comments.")
w("- The review event's start time is its load-bearing field (no description used).")
w("- base_check patched locally to accept a Linear project inserted by the same SQL (it already accepted same-SQL "
  "issues); diff kept in `support/task_work/rb_winddown_closeout/base_check.orig.py`. The platform `/injection` has its "
  "own reference check — watch for a project-id finding there.")
w("- No graded value reads Snowflake: AWS and the UA line's ad accounts are out of scope (rule 3), so the base ledger vs P&L AWS/UA disagreement is not depended on.\n")

# ------------------------------------------------------------------ 13
w("## 13 Self-review\n")
w("### Tool outputs (verbatim, final run)\n")
for t, f in [('sql_lint.py', 'sql_lint.txt'), ('base_check.py', 'base_check.txt'), ('hardness_gate.py (SQL)', 'hardness_sql.txt')]:
    w(f"`{t}`:\n\n```\n" + cap(f) + "\n```\n")
w("**Warning dispositions.** sql_lint weekend warn ×4 (disposition): automated vendor receipts sent on their billing dates "
  "(Layer Jan 25, Deel/Linear Feb 1, 1Password Feb 8) — base vendor mail arrives on weekends too (robert@harmonygames.co "
  "Google Play receipts on Sat/Sun). sql_lint clock warn ×6 (disposition): the review call on 2026-03-12 is a not-yet-happened "
  "future event, scheduled before the clock. sql_lint confluence warn (disposition): both seeded pages are reached through "
  "a pointer (the UA page by a Confluence search for close-out conventions; the handover page through the checklist's "
  "'support handover page'). base_check INT-11: resolved — invitation mails seeded (no exception needed).\n")
w("### /injection Checks A–C walk (`Evals/0_Injection_Quality_Eval.md`)\n")
w("| Check | Verdict | Evidence |\n|---|---|---|")
w("| Inventory | PASS | 120 INSERT + 4 UPDATE, every statement keyed on a primary key; no upsert, no DELETE (sql_lint stats) |")
w("| Check A — references | PASS | channels C0ADGSZKR3R, C09UHHN6PFZ; users EMPLOYEE_00nn; Linear users/team_ENG; project inserted first; page_ops_home parent; Combo-Fighters repo; board 640643a3fd8f3ca308d9318e lists; collisions 0 (§1.F) |")
w("| Check B — structure | PASS | literal JSON in every *_json column; no generated column written; quoted camelCase (sql_lint 0 errors) |")
w("| Check C — dates/relations | PASS | all timestamps before the clock except the future event; reply after parent; comments after issues; in_reply_to in the same mailbox (base_check) |\n")
w("### Counter-readings\n")
w("| # | Category | Counter-reading (strongest case it FAILS) | Resolution with evidence | Verdict |\n|---|---|---|---|---|")
cr = [
 ("temporal", "a receipt dated before a change contradicts the later state (dbt receipt Feb 3 on the SVB card vs moved to KubLLC); Sherwood's 'as promised on our call'", "the move is Feb 12 23:00Z (C0ADGSZKR3R/1770937232.664809) and ENG-2457's comment Feb 13 01:29Z supersede the receipt; Sherwood's mail now follows the Feb 12 16:30Z call (robert@harmonygames.co/1856689465442954434, review F1)", "PASS"),
 ("semantic / category", "'Closed' in rule 5 vs Linear 'Done' in the project description could be read as two definitions", f"project {M['L_PROJECT']['id']} description (K2): 'Done once the account counts as closed in the register' — one definition, rule 5 of {M['DOC_CONV']['id']}", "PASS"),
 ("cross-service referential", "the injection could relabel base redaction tokens (review F2) or cite a file that does not exist (F3)", "no seeded text names a redacted vendor: Kapwing comes from Leonard's base table C0ADGSZKR3R/1770933450.410449, dbt's move from Arthur's own ENG-2457 comment; helpshift_export_2026-02-13.zip is now a drive_files row in d_e5caf6a8c630421942ee59", "PASS"),
 ("quantitative", "the costs tab's month labels (HG Costs a year behind HG P&L) and its December figures vs the latest receipts", f"rule 8 of {M['DOC_CONV']['id']} takes no cost from the tab: owner figures in the issues or own last invoices, matching the latest base charges", "PASS"),
 ("state/lifecycle", "Singular could be closed: Leonard terminated it", "robert@harmonygames.co/1853470745017478863 asks for written confirmation; no later Singular message exists before the clock", "PASS"),
 ("state/lifecycle (sibling)", "another base account might look still-active without an issue (Calendly charged Oct 2025, tab col AC)", "ENG-2463 exists; Robert's comment 'turned off auto-renew in october' → excluded (cancelled before Feb 9)", "PASS"),
 ("identifier/format", "new sender tokens could collide with existing identities", "PERSON_7731, SVC_7702–SVC_7712: 0 hits in all three data folders (§1.F, collide.sh lookups); vendor tokens reused: SVC_5771_EMAIL (Unity)", "PASS"),
 ("people status", "Frederick (quiet since Oct 2025) authors a page", f"{M['CONF_UA']['id']} is dated 2025-03-18, when he was active (page_product_okrs owner; frederick.stone@harmonygames.co quiet_since_2025-10)", "PASS"),
 ("other", "the Sunset correction could read as an unintended contradiction of the first checklist", f"same sender, same thread {GT('G_SUNSET1')}, later date, 'one change … The rest of the list stands' — a dated amendment ({G('G_SUNSET2')})", "PASS"),
 ("intended: Gusto", "Arthur's reply could be read as a suggestion, not a decision", f"A1 {M['S_ANCHOR']['locator']} tells Robert to go by the keep list 'and the replies under it'; rule 4 'my keep list, as amended in the thread'", "PASS"),
 ("intended: Slack/Google clashes", "the clashes could be read as Sunset overriding silently (no report needed)", f"A1 {M['S_ANCHOR']['locator']} asks to report 'anything in the plan that clashes with what we already decided'", "PASS"),
 ("intended: Metabase", "Arthur's LLC move could clash with Sunset's first list", f"the correction {G('G_SUNSET2')} removes Metabase; ENG-2456's comment confirms the KubLLC card", "PASS"),
 ("intended: Sherwood", "two checklists from two firms are two live answers", "decoy_scope issuer: Sherwood was not engaged (signed SOW robert@harmonygames.co/1856956532017091340 is Sunset's)", "PASS"),
 ("intended: Docusign", "a handover by comment without Robert's acceptance", f"Leonard's comment {issue['Docusign']['comment_ids'][0]} on ENG-2469 is a statement ('docusign goes to robert'); rule 7", "PASS"),
 ("intended: Arthur's sheet", "the sheet could be read as current costs", f"project {M['L_PROJECT']['id']} description 'replaces my subscriptions sheet from Tuesday' ({M['SHEET_SUBS']['id']} Feb 10)", "PASS"),
]
for i, (c, a, b, v) in enumerate(cr, 1):
    w(f"| {i} | {c} | {a} | {b} | {v} |")
w("\n### Revision 2 — /injection review 6adfee3f27ce6ca81b457137 (FAIL: F1–F3) and fixes\n")
w("| Finding | Fix | Evidence |\n|---|---|---|")
w(f"| F1 Sherwood mail cites a call before it happened | redated to 2026-02-12T18:40:12Z, after the Thu Feb 12 16:30Z call | robert@harmonygames.co/1856689465442954434 (base call booking); {G('G_SHERWOOD')} |")
w("| F2 project description relabelled redaction tokens (Notion, Sentry) | sentence removed; Notion issue is now Kapwing (Leonard's table C0ADGSZKR3R/1770933450.410449, closed by its cancellation mail); Sentry issue dropped; dbt's KubLLC move stated in Arthur's ENG-2457 comment, so dbt's deadline is Mar 12; Zapier is Requested (ticked by Leonard in the same table, comment on its issue) | C0ADGSZKR3R/1770937232.664809, C0ADGSZKR3R/1770933903.645709 |")
w(f"| F3 Confluence comment cites a missing Drive file | drive_files row {SQ['zip']} helpshift_export_2026-02-13.zip (application/zip) in d_e5caf6a8c630421942ee59, 15:04:51Z, before the comment | comment_support_after_helpshift_c1 (removed in Revision 8) |")
w("| A1 links_json / sequence not in the snapshot (provisional) | linear_comments.sequence dropped (nullable in the live schema); linear_projects.links_json kept: references/universe_schema_live.json (platform DB export 2026-10-04) marks it NOT NULL with no default, so omitting it fails the insert — the eval snapshot injection.json is the older 58-table cross-check | linear_projects, linear_comments |")
w("| A2 Chase card idShort NULL | card dated 2023-04-18T20:18:50Z between cards 67 and 69, idShort 68 (the free number there) | board 640643a3fd8f3ca308d9318e |")
w("| A3 Carta renewal 8/15 | comment and deadline aligned (renews Aug 15 → 2026-08-14) | C0ADGSZKR3R/1770933450.410449 |\n")
w("\n### Revision 3 — /injection review 6adfee3f27ce6ca81b457137 rerun (FAIL: F1–F3) and fixes\n")
w("Root cause: the seeded receipts in Robert's mailbox were never checked against the vendors' real billing mail in Leonard's and Arthur's mailboxes (their message dates are RFC-2822, which an ISO-only scan skipped). Every vendor was re-scanned across all mailboxes (Nov 2025–Feb 2026, and Sep 2024 onward for the rest).\n")
w("| Finding | Fix | Base evidence |\n|---|---|---|")
w("| F1a Kapwing | seeded cancellation mail removed; Arthur's comment relays Kapwing's own cancellation notice ($24/month; base notice: Pro until Feb 25) → Closed | blake@harmonygames.co_1856962040028188034.json, blake@harmonygames.co_1855319224557456875.json |")
w("| F1b CodeRabbit | bot notice now says canceled on Feb 12; comment 'lite plan, 3 seats at $15' (cost 45) | blake@harmonygames.co_1856750389874631062.json, blake@harmonygames.co_1854150876243727777.json |")
w("| F1c Slack | seeded invoice removed; Leonard's comment 'renews on the 3rd, svb card' (Feb 3 renewal, next 3/3) | leonard@harmonygames.co_1856103558554635848.json |")
w("| F1d QuickBooks | seeded receipt removed; Leonard's comment 'takes the $115 from my own card on the 4th, not the svb one' → Keep, dash | leonard@harmonygames.co_1856211152930380063.json |")
w("| F1e Google Cloud | seeded email removed; Arthur's comment 'charges the svb card on the 1st' | blake@harmonygames.co_1855947447649217022.json |")
w("| F1f dbt | seeded receipt removed (dbt is on the KubLLC card per Arthur's comment) | leonard@harmonygames.co_1855983949220444975.json |")
w("| F1g Zapier | seeded receipt removed; Leonard's comment quotes Zapier's own notice (plan runs until Feb 27) → Closed | leonard@harmonygames.co_1856958213684823393.json |")
w("| F1 sweep (same defect class) | removed seeded Deel, Cursor, Vercel, Docusign and 1Password mail; Deel is paid by bank transfer (Keep, dash); Docusign renews Apr 20 for $300 (deadline Apr 19); GitHub costs $52 + Copilot ($90 last invoice); Gusto pulls its invoice from the bank on the 3rd (deadline Mar 2); Helpshift comment no longer quotes a $300 figure; no seeded record carries a card number | blake@harmonygames.co_1856009246393472679.json (Deel transfer), leonard@harmonygames.co_1827068676034658582.json (Docusign 04/20, 300), blake@harmonygames.co_1856132203079406675.json (GitHub $52 + $38), blake@harmonygames.co_1856071940774386395.json (Gusto Feb 3) |")
w("| F2 'never paid' comments | Office 365, Typecast, Adobe, OpenAI comments now agree with the costs tab (stopped paying before Feb 9); Miro issue dropped (live base receipts to Brian, A2) | f_605121f4a36752645e0ac3 rows 8, 11, 26, 54; leonard@harmonygames.co_1841288941522824072.json (Typecast Aug 2025) |")
w("| F3 commit identity | author/committer 'Oliver Brooks' <oliver.brooks@harmonygames.co> | harmonygames-Games/Combo-Fighters#38 |")
w("| A3 / A7 | 1Password's description no longer claims #winddown; Chase card closed like its neighbours 67 and 69 | C0ADGSZKR3R/1770933450.410449 |\n")
w("\n### Revision 4 — /prompt review 6adfee3f27ce6ca81b457137 (FAIL 2: UGT, Clarity, Cross-Service Coherence) and fixes\n")
w("| Finding | Fix | Evidence |\n|---|---|---|")
w(f"| Sound-line accounts (Pond5, ElevenLabs) two readings of rule 3 | rule 3 now names two sources explicitly: ledger lines still charging, and every other account inside a costs-tab line that covers several vendors, each its own row with or without a ledger line | {M['DOC_CONV']['id']} rule 3; f_605121f4a36752645e0ac3 row 15 |")
w("| Hailuo.ai, Dailybot, UA Assets had no status record | assignee comments: Hailuo cancelled in October (tab AD 10, AE 0), Dailybot stopped early 2024 (tab C–L), UA Assets one-off campaign creative buys, last Apr 2025 (tab X) → all excluded, issues Canceled | ENG-2446, ENG-2452, ENG-2481 |")
w(f"| clash list undefined | rule 10: a clash is a #winddown decision that Sunset's list or SVB's terms would undo; card moves and requests are not decisions → exactly Slack free plan (C0ADGSZKR3R/1770840054.486779), Slack cut to three paid seats (C0ADGSZKR3R/1770842405.931359), Google archiving (C0ADGSZKR3R/1770933903.645709) | {M['DOC_CONV']['id']} rule 10 |")
w("| AWS: costs tab 0 vs ledger 1,485 | rule 8 no longer falls back to the ledger except for ad spend; Arthur's ENG-2455 comment gives all of AWS at $1,485 in January and says the P&L line was never kept up (a dated human explanation of the near-empty line) | ENG-2455; FIN-000687 |")
w("| Singular date both-fair (Feb 28 / Mar 14) | Leonard's ENG-2454 comment: the next quarterly invoice is Mar 1; Mar 15 is only the extension on the old one → Feb 28 | ENG-2454; robert@harmonygames.co/1850283027022457279 |")
w("| minor: Docusign / Linear charges missing from the P&L | owner comments say the P&L missed last April's Docusign charge and only caught Linear's 2024 payment | ENG-2469; ENG-2448 |")
w("| platform note: PR #38 base_sha not in the export | base_sha = 4e9e1e94d7d89fb7ef9985d1a6c271421129888a (Combo-Fighters#37's develop base) | harmonygames-Games/Combo-Fighters#38 |\n")
w("\n### Revision 5 — /injection review 6adfee3f27ce6ca81b457137 (FAIL: F1 Dailybot, F2 UA Assets) and fixes\n")
w("Root cause: the Revision-4 comments were checked against the recent costs-tab columns only. Every comment that states a payment history was then re-checked against its row's full history (C=Jul-23 … AF=Dec-25); one more defect of the same kind was found and fixed (Kling).\n")
w("| Finding | Fix | Costs-tab evidence (f_605121f4a36752645e0ac3) |\n|---|---|---|")
w("| F1 Dailybot 'cancelled after the first month' | 'we stopped paying for dailybot in early 2024, it's sat on the free plan since' (ENG-2452) | Dailybot C–I 25–34, J–L rolling averages to Apr-24; base Free-plan notices 2025 |")
w("| F2 UA Assets 'never spent on it' | 'that line was one-off creative buys for campaigns, the last one was last april' → excluded as one-off (ENG-2481) | UA Assets I, J, M, N, R, S, T, X (last Apr-25) |")
w("| sweep: Kling 'dropped after the september trial' | 'dropped kling after september' (ENG-2445) | Kling U–AC 9/month Jan–Sep 2025 |")
w("| A2 Linear / A3 AWS wording | 'the p&l stops after the 2024 payment' (ENG-2448); 'the p&l line for it was never kept up' (ENG-2455) | Linear D–Q (last Sep-24); Servers (AWS) AE 15 only |")
w("| sweep, held | OpenAI (last Apr-24), Typecast (last Jul-25), Veed (last Nov-25), Hailuo (last Oct-25), JetBrains (to Dec-25), Adobe (last Oct-24), Office 365 (last Dec-24), Calendly (Oct-25), Solsten (Jan-24), Notarize (Aug-23), Docusign (Apr-24 only), Carta (Aug-25 3,852) all agree with their comments | rows 8, 11, 19–22, 26, 51, 55, 64, 69, 32, 49 |\n")
w("\n### Revision 6 — /injection review 6adfee3f27ce6ca81b457137 (FAIL: F1 Dailybot still 'on the free plan') and fix\n")
w("| Finding | Fix | Evidence |\n|---|---|---|")
w("| F1 Dailybot comment implied the workspace still exists | 'we stopped paying for dailybot in early 2024, it sat on the free plan until they deleted the workspace last september' (ENG-2452) | blake@harmonygames.co_1842691964207508503.json (8 Sep 2025 'We deleted your organization'); blake@harmonygames.co_1839039701685601092.json (30 Jul 2025 removal notice); costs tab Dailybot C–L |")
w("| sweep: every comment's current-state claim vs vendor account-state mail in all mailboxes (full-body scan, 2025-01 → clock: deleted / deactivated / canceled / expired / downgraded / plan changed) | only Dailybot contradicted; Kapwing and Zapier notices already match their comments; Carta notices are contractor terminations (match ENG-2462); no notice exists for Typecast, Adobe, Office 365, Hailuo, Veed, Kling, OpenAI, Calendly, JetBrains, Solsten, Notarize, 1Password, Vercel, Cursor, Layer, Figma, Pond5, Soundly, ElevenLabs, Docusign or Linear | blake@harmonygames.co_1856962040028188034.json; leonard@harmonygames.co_1856958213684823393.json |\n")
w("\n### Revision 7 — /prompt review 6adfee3f27ce6ca81b457137_1_prompt (1) (FAIL: Cross-Service Coherence 2, AWS costs tab vs ledger) and fix\n")
w("| Finding | Fix | Evidence |\n|---|---|---|")
w("| Issue 1: the AWS cost was routed by the costs tab's 0 (rule 8 fallback) and ENG-2455 explained the tab/ledger gap, so the task depended on a base quantitative conflict | rule 8 now starts: 'A cloud or ad-spend account with its own line in the finance ledger uses its January line there, whatever the costs tab shows' — only AWS (FIN-000687 −1,485), applovin (FIN-000688 −9.80) and meta (FIN-000689 −2,843.84) have such lines in Jan 2026; BigQuery (inside 'SaaS vendors') keeps AF 14.33. ENG-2455 comment drops 'the p&l line for it was never kept up'. Costs and totals unchanged (10,916.98 / 1,206.39) | snowflake FINANCE_LEDGER 2026-01-31 rows FIN-000686…FIN-000696 (other lines: aggregates, salaries, revenue) |")
w("| Known base issue (not depended on): HG Costs 'Servers (AWS)' AC–AF vs ledger AWS Sep–Dec 2025, and 'UA' vs ledger marketing_ua | no graded value reads either side; rubric and OEs stay off monthly AWS and UA spend for 2025 | f_605121f4a36752645e0ac3 row 41; FIN-000672 |")
w("| Issue 2 (Business Function 3, NON-FAIL, optional) | not changed: any reframing risks a new fork; the reviewer marks it non-blocking | — |\n")
w("\n### Revision 8 — /prompt review 6adfee3f27ce6ca81b457137_1_prompt (2) (FAIL: Cross-Service Coherence 2) and fixes\n")
w("| Finding | Fix | Evidence |\n|---|---|---|")
w("| 1 Vercel label on GitHub's costs-tab line | project description now 'the hosting one is GitHub'; Vercel issue ENG-2459 and its comment removed (numbering kept, the gap is ENG-2459); ENG-2477 GitHub 'From costs tab (unlabeled hosting line).'; GitHub costed from AF = 86.00 (rule 8) and its comment no longer quotes $52/$90 (one route); 'Vercel 90' dropped from the stale Subscriptions sheet | HG Costs row 42 '[PERSON_NAME_0250]' AC–AF 165/169/105/86 = Arthur's GitHub receipts (2025-09-03 … 2025-12-03); Leonard's SVB feed −189.49 2025-04-04 = GitHub Apr receipt |")
w("| 2 Confluence deactivated (Vincent's mailbox, 2025-10-03) vs injected Confluence activity | Confluence removed from Sunset's list (all three copies); the 'support handover page' sentence dropped; page_support_after_helpshift, its version and comment deleted; register loses the Confluence Hold row ($0). Helpshift export now logged by Oliver on ENG-2439 (2026-02-13T15:12:18Z, after the zip's 15:04:51Z) | helpshift_export_2026-02-13.zip in the Wind Down folder, shared with Robert; the Growth/UA page (2025-03-18) predates the deactivation and stays a decoy |")
w("| 3 HG Costs header a year behind HG P&L from column V | UPDATE gsheets.sheets_sheets (f_605121f4a36752645e0ac3, sheet 2): header V…AR +1 year, so V–AL equal HG P&L's labels and AF reads 2025-12-25; values unchanged; spreadsheet and Drive modified_time 2026-02-13T16:31:07Z (before the conventions doc, 16:38); rule 8's 'off by a year, go by position' sentence removed | builder asserts costs header C–AL == HG P&L header C–AL; the early I/L–T labels are identical on both tabs (base, unchanged) |")
w("| 4 Chase-closure decoy card vs the Chase account opening in Apr 2023 | Trello card and its createCard action deleted; H2's decoy is now base card #170 'move subscriptions to SVB credit card' (Done, 2023–24) on the same board | #admin_foundersonly 2023-04-24/28 |")
w("| 5 (optional) AWS wording | 'whatever the costs tab shows' removed from rule 8 | FIN-000687 |")
w("| sweep: other unlabeled costs-tab lines | the '$30 game-ops lines are people's tool stipends' claim removed (Leonard's SVB feed books '[PERSON_NAME_5480]' as −29.99 Software & apps, 2025-03-27) → 'the two $30 game-ops lines I'm handling myself, so they're not in here' (a scope decision, no identity claim); '$6,250 one is Singular' kept: Singular invoices quarterly $6,250 in Robert's mailbox, and the same token reads 'Singular Fix' in the Android version tracker | HG Costs rows 11/18/36; SVB feed sheet |")
w("| totals (before Revision 9) | 29 rows: 10,826.98 / 1,202.39; 45 issues; 4 new issues | truth.json |\n")
w("\n### Revision 9 — independent coherence audit of the Revision-8 SQL (before resubmitting /injection and /prompt)\n")
w("| Finding | Fix | Evidence |\n|---|---|---|")
w("| Linear: seeded receipt 'Linear Basic (annual), 4 seats, $480, renews Feb 1 2027' contradicts the base Standard renewal | receipt removed; Arthur's ENG-2448 comment: 'linear is on standard, paid yearly. we paid $1,832.65 last august for the year to aug 21, it moves to basic at that renewal' → 1,832.65 / 12 = 152.72 (rule 8: tab AF 0 for Dec is a true no-charge month for an annual plan); 'the p&l stops after the 2024 payment' removed | leonard@harmonygames.co_1841095243838114182.json (Aug 21 2025, Standard ×22, Aug 21 2025 – Aug 21 2026, amount paid $1,832.65); leonard@harmonygames.co_1840819416447370635.json; 00016109.json (Robert, Dec 4 2025: Basic at the next renewal after Feb 1 2026) |")
w("| QuickBooks: 'from my own card, not the svb one' contradicts the Intuit receipts (MASTER 5348 = the SVB card) | comment: 'intuit takes the $115 off the svb card on the 4th' → Keep row still charging the SVB card → by when Feb 19 (rule 6 + SVB card terms); Revision-3 row F1d superseded | leonard@harmonygames.co_1856211152930380063.json (Feb 4 2026, MASTER ending in 5348); leonard@harmonygames.co_1787909925965085132.json ('Silicon Valley Bank Card ending in 5348') |")
w("| OpenAI: 'we stopped those in 2024' contradicts the May 2025 $50 API top-up | comment: 'prepaid api credits we topped up by hand now and then, the last one was $50 last may. nothing recurring' → left out as one-off purchases (rule 2); the ChatGPT Plus claim dropped | blake@harmonygames.co_1830989465254730549.json (2025-05-02, $50) |")
w("| Pond5: 'renews on March 2, 2026' implies a Mar 2025 $60 charge the Sound line never shows | seeded mail now an end notice dated 2025-09-08: not renewed, ended Sep 8 2025 → rule 2 leaves it out (no row, no new issue) | HG Costs row 15: Sep-24 70.5 (the annual), flat 15 after, no Sep-25 bump |")
w("| JetBrains: 'contractor who left' vs EMPLOYEE_0032 full_time | 'the engineer who left in october' | PAYROLL_ROSTER (last month Oct-25) |")
w("| checked clean by the audit | GitHub and Singular relabels match receipts; Figma, Kapwing, CodeRabbit, Zapier, Carta, Docusign, Calendly, AWS, Unity, Typecast/Veed/Kling/Hailuo/Adobe/Office 365/Dailybot/UA Assets/Solsten, Trello, Slack, KubLLC moves; mail dates and weekdays; authors' channel membership; header UPDATE changes only row 0 cols V–AR | — |")
w("| totals | 28 rows: 10,934.70 today / 1,315.11 after the plan; 45 issues; 3 new issues (ElevenLabs, Meta Ads, AppLovin UA) | truth.json |\n")
w("\n### Revision 10 — /injection review 6adfee3f27ce6ca81b457137_0_injection (6) (FAIL: F1 header UPDATE vs the Drive xlsx bytes) and fix\n")
w("The two reviews conflict: /prompt (run 3) failed a positional note around the HG Costs header year slip, and /injection (run 6) failed the header UPDATE because the same file's Drive xlsx bytes keep the old labels. The only route both accept is that no graded value reads the costs tab's month columns.\n")
w("| Finding | Fix | Evidence |\n|---|---|---|")
w("| F1 Sheets header vs Drive xlsx bytes | the three P&L statements removed (Drive modified_time, sheets_sheets header grid, spreadsheet modified_time); base file untouched | Audit-Report/0_injection_FAIL_r8.md |")
w("| rule 8 depended on the costs tab's month columns | rule 8: ledger line for cloud/ad-spend accounts with their own line; everything else the owner's monthly figure in its Linear issue, or its own last invoice brought to a month; the costs tab is now used only for membership (rule 3) | doc f_1326e66bcabfda8fd29e4a |")
w("| owner figures added (each = the latest base charge before the clock) | Unity 'unity pro is 11 seats at $2,348.50 a month with tax, next invoice is the 19th' → 2,348.50, by when Feb 18 | Arthur's mailbox INZ02468432/INZ02517133/INZ02565829/INZ02614348: UTY-PRO ×11 $2,200 + $148.50 tax, Oct 19 … Jan 19 |")
w("| | Slack 'it was $87.22 this month' | Leonard's mailbox 'your plan has renewed' 2026-02-03 Total $87.22 (Dec 129.50, Jan 121.10) |")
w("| | GitHub 'it was $90 this month all in' | GitHub receipt 2026-02-03: Team $52 + Copilot $38 = $90 |")
w("| | BigQuery 'it was $4.97 this month' | Google payment 2026-02-01 $4.97 |")
w("| | Metabase $148, dbt $100, Helpshift $150, Deel $300, Gusto 'january invoice was $116' | Metabase receipts Dec 21/Jan 21 $148; dbt Feb 1 $100; Helpshift INV/HSUS9879 (31/1/2026) $150; Gusto January 2026 invoice paid Feb 3, $116; Deel: costs tab Nov/Dec 300, no billing mail |")
w("| | Workspace: own last invoice in Robert's mailbox, Feb 2 2026, $298.13 | robert@harmonygames.co/1856033699491658253 att_0001.pdf |")
w("| seeded Unity 'CINV' invoice (Feb 10) removed | the base CINV invoices are Unity Ads (uAds per-game lines) and stop after Nov 10 2025; a Feb CINV was invented | 00015915.json CINV-00022209 (uAds 1 – 31/10/2025) |")
w("| decoy | T25: the costs tab's December figures (Unity 2,172, Workspace 316.56, Slack 129.50, BigQuery 14.33, GitHub 86) are now wrong answers | f_605121f4a36752645e0ac3 |")
w("| totals | 28 rows: 11,045.13 today / 1,249.04 after the plan | truth.json |\n")
w("\n### Revision 11 — second independent coherence audit of the Revision-10 SQL\n")
w("| Finding (verified both sides) | Fix | Evidence |\n|---|---|---|")
w("| BigQuery 'google cloud charges the svb card' vs Google payments on MasterCard x-2758 (the SVB card is 5348; 2758 also pays Arthur's GitHub and PayPal) | 'google cloud charges my card on the 1st, not the svb one. it was $4.97 this month' → Hold row already off the SVB card → by when = the review call (Mar 12) | blake@harmonygames.co_1855947447649217022.json (Feb 1 2026, $4.97, x-2758); leonard@harmonygames.co_1787909925965085132.json (SVB card 5348) |")
w("| OpenAI 'the last one was $50 last may' vs the costs tab (no OpenAI charge after Apr-24) — the mail (May 2 2025 $50) and the tab disagree in base | the comment no longer dates a top-up: 'prepaid api credits we topped up now and then, nothing recurring' (rule 2 one-off purchases) | HG Costs OpenAI row; blake@harmonygames.co_1830989465254730549.json |")
w("| rule 6 'ads, cloud — bill on the 1st' vs Meta's threshold billing (many receipts a month) | rule 6 now states a convention: 'for accounts billed on usage — ads, cloud — use Feb 28' | Leonard's mailbox: Meta ads receipts Jan 2026 ×26, Feb 2/3/5/8/12 |")
w("| 'unlabeled' costs-tab lines (labels are names in the tab) | project description 'A few costs-tab lines are filed under other names: the $6,250 one is Singular and the hosting one is GitHub'; issue descriptions '($6,250 line)', '(hosting line)' | Singular invoices $25,000 (Sep-24) / $6,250 (Sep-25) = tab Q/AC; GitHub receipts 169/105/86 = AD/AE/AF |")
w("| Docusign 'he used it for the art contracts' vs every envelope being Leonard's | 'docusign goes to robert from here. annual, $300, renews apr 20' | leonard@harmonygames.co_1827068676034658582.json |")
w("| Calendly auto-renew claim by Robert while renewals go to Leonard | Leonard's comment 'auto-renew has been off since october, right after it charged' | Calendly Oct 13 2025 charge (costs tab Oct-25 96) |")
w("| held: Soundly $10 notice vs the Aug 2025 'Monthly: $19.99' change | kept — the same Aug 2025 notice offers to lock the current rate; /prompt run 2 rejected this as a conflict (P2-DR9) | 00014928.json |")
w("| held: Slack and Workspace 'on the svb card' | kept — no base billing mail names their card | Slack renewal mails Jan 3 / Feb 3 2026; Workspace invoices Jan 1 / Feb 2 2026 |\n")
w("\n### Revision 12 — /prompt review 6adfee3f27ce6ca81b457137_1_prompt (3) (FAIL: Feasibility 2, UGT 2, Cross-Service Coherence 2) and fixes\n")
w("| Finding | Fix | Evidence |\n|---|---|---|")
w("| 1 Workspace cost only inside a PDF the Agent can't read | Leonard's ENG-2464 comment: 'workspace is on the svb card, this month's invoice was $298.13' | robert@harmonygames.co/1856033699491658253 att_0001.pdf: $298.13 (Jan 1–31 2026) |")
w("| 2 Unity Ads inside the UA line, no record of it ending | project description: 'we stopped the unity ads in the UA line after october, so they're not in here' (rule 2) | Unity Ads CINV invoices end with 'uAds 1 - 31/10/2025' (Nov 10 2025); no later Unity Ads invoice; ledger Jan/Feb has no Unity line |")
w("| 3 Zapier switch-over undecided (Oliver's #issuefeed pipe note) | Oliver's Zapier comment removed | — |")
w("| Helpshift by when (switch-over of both games off Helpshift not recorded) | Oliver's ENG-2439 comment: '... both games' support buttons now open email instead of helpshift' → export and switch-over done → Closed row, dash | Leonard #winddown 1770789534.434749 'We gotta move domino delights and zombie match off Helpshift before Feb 28th. We can just open up the email app' |")
w("| 4 Layer receipt 'next payment Feb 25' vs Leonard 'we have access until March 3rd' | receipt dated 2026-02-03, 'Your next payment is on March 3, 2026' → Requested row by when 2026-03-02 | #prototype C09UHHN6PFZ/1770837702.167889 |")
w("| 5 Linear and DocuSign 2025 charges missing from the costs tab | in-world lines restored as the reviewer recommends: ENG-2448 '... the p&l stops after the 2024 payment'; ENG-2469 '(the p&l missed last april's charge)' (accepted in /prompt run 2) | HG Costs Linear (last Aug-24 2403), Docusign (Apr-24 300) |")
w("| 6 HG Costs header years (minor) | no graded value reads the costs tab's month columns; OEs and rubric stay off them | — |")
w("| totals | unchanged: 28 rows, 11,045.13 / 1,249.04 | truth.json |\n")
w("\n### Revision 13 — blind unique-answer audit (register rebuilt from Robert-readable records only)\n")
w("| Finding | Fix |\n|---|---|")
w("| no fatal fork; required values all readable; totals re-added 11,045.13 / 1,249.04 | — |")
w("| Calendly 'auto-renew off' is not plainly 'cancelled' (rule 2) | Leonard: 'we cancelled calendly in october right after the annual charge, it just runs out' |")
w("| Unity Ads 'stopped' is not plainly 'cancelled' (rule 2) | project description: 'we cancelled the unity ads in the UA line after october' |")
w("| held as settled by /prompt run 4 | Layer/Cursor Requested (rule 5: nothing back from the vendor); Slack is a clash (reading I); Metabase Move (keep list = the thread parent and its reply) |")
w("| rubric note | the clash set is three (Slack free plan and guest seats, Google archive, plus the third in §9.2); the rubric accepts the two Slack items merged or listed apart |\n")
w("\n### Revision 14 — hardening r1 (`01a_Hardening_Report.md`, plan D)\n")
w("| Change | Records | Effect on the answer |\n|---|---|---|")
w("| 16 issues removed whose own comment stated the exclusion (OpenAI, Typecast, Unity Asset Store, Veed, Kling, Hailuo, JetBrains, Adobe, Dailybot, Solsten, Calendly, Fondo, Insurance, Office 365, Notarize, UA Assets) | project description: 'I skipped the costs-tab lines that were one-off buys, filings and insurance, or dead well before this year'; rule 3: 'he skipped one-off, filing and insurance lines and ones long gone' | 29 issues, renumbered ENG-2438…ENG-2466; register unchanged (28 rows) |")
w(f"| Cursor, Unity, AppLovin: vendor word relayed outside Linear | {M['S_CURSOR_CONF']['locator']}, {M['S_UNITY_CONF']['locator']}, {M['S_APPL_CONF']['locator']} (+ backing mail in Arthur's/Leonard's mailboxes) | Closed, dash; {issue['Cursor']['issue']} Cursor and {issue['Unity']['issue']} Unity → Done |")
w(f"| SVB card amended by Leonard's comment | {M['T_SVB_CMT']['id']} | Intuit, Workspace, Slack by Feb 17; every non-Closed Cancel row by Feb 17 except Carta (Aug 14, Leonard's exception) (rule 6: 'or the SVB card on the founders' board if it sets an earlier date'); Arthur's reply on the card moves AWS and 1Password to the 17th |")
w("| review-call invitation mails | Robert's and Arthur's mailboxes | none (resolves base_check INT-11) |")
w(f"| totals | unchanged: 28 rows, {fmt(TR['total_today'])} / {fmt(TR['total_after'])}; Linear Done {len(TR['linear']['done'])}, Canceled {len(TR['linear']['canceled'])}, open {len(TR['linear']['open'])} | truth.json |\n")
w("Coherence checks for this revision (independent audit, 2026-10-29): Arthur's AWS ('keeping dd prod up through the month') and 1Password ('cancel it last') comments are superseded by his later reply on the SVB card; Leonard's Feb 12 #winddown Carta decision ('we have time for Carta renewal so I'm not gonna really touch that') is kept by the exception in his comment, so it is no clash; the Cursor relay is a reply to Oliver's ask in #prototype (#engineering-bots is a bot channel since Nov 2025); "
  "Marcus Lee (AppLovin) is quiet since 2025-12 (activity.json), so AppLovin answers Leonard by email; no base message dates the card closure (#winddown 'pay SVB fully and close the credit card' has no date).\n")
w("\n### Revision 15 — /prompt review 6adfee3f27ce6ca81b457137_1_prompt (6) (FAIL: Cross-Service Coherence 2, ledger vs Cash P&L on AWS/UA) and fix\n")
w("| Change | Records | Effect on the answer |\n|---|---|---|")
w("| AWS issue removed (its number stays a gap); AWS and the UA line's ad accounts declared out of scope | project description ('AWS and the ad accounts in the UA line aren't in here either'); conventions rule 3 ('AWS and the ad accounts in the UA line stay off the register') | no AWS, Meta Ads or AppLovin row; no graded value reads the finance ledger, which the base Cash P&L contradicts for AWS and UA in nearly every month |")
w("| rule 3 ledger clause and rule 8 ledger sentence removed | conventions doc | costs come only from owner figures or the account's own receipt |")
w("| ask wording: 'yesterday', 'the reply under it' (/prompt advisory Issue 4) | anchor message | none |")
w(f"| totals | {len(TR['rows'])} rows, {fmt(TR['total_today'])} / {fmt(TR['total_after'])}; Linear {len(A)} issues: Done {len(TR['linear']['done'])}, Canceled {len(TR['linear']['canceled'])}, open {len(TR['linear']['open'])} | truth.json |\n")
w("Kept as context only: Arthur's SVB-card reply mentioning AWS, Leonard's two AppLovin messages and the AppLovin closure mail (now decoys for rule 3, traps T8 and T11).\n")
w("\n### Re-verified facts\n")
w("Re-read through the exports this session: costs tab line labels (f_605121f4a36752645e0ac3), "
  "#winddown timestamps (C0ADGSZKR3R/2026-02.json), Robert's mail 00016283 / 00016086 / 00016395 / 00016044 / ElevenLabs / "
  "Linear notice, Trello board 640643a3fd8f3ca308d9318e idShort range, Combo-Fighters#37 fields, Linear team memberships.\n")
w("Unresolved: (1) platform /injection may not resolve a Linear project inserted by the same SQL (local base_check patched, "
  "§12); (2) the difficulty projection waits for the Opus pre-check and the rubric (scenario §6, red team B3/B5).\n")

dst = os.path.join(BUNDLE, 'task_inputs', 'Working_Files', '01_Grounding_Dossier.md')
open(dst, 'w').write("\n".join(L) + "\n")
print('wrote', dst)
