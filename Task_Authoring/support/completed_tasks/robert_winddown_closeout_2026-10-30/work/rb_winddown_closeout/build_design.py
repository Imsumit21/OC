"""Writes task_inputs/Working_Files/01_Scenario_Design.md from the minted ids, planned text, truth and pasted tool outputs.

Tool outputs (reach, collisions, resolve, hardness gate) are read from files captured by the caller (argv[1] = dir).
Sections 12 (self-review) and 13 (red team) are appended from review_sections.md when it exists.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUNDLE = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
CAP = sys.argv[1]
M = json.load(open(os.path.join(HERE, 'minted_ids.json')))
T = json.load(open(os.path.join(HERE, 'planned_text.json')))
ACC = json.load(open(os.path.join(HERE, 'accounts.json')))
TR = json.load(open(os.path.join(HERE, 'truth.json')))
MAN = json.load(open(os.path.join(BUNDLE, 'task_inputs', 'Working_Files', '01_Hardness_Manifest.draft.json')))
A, ADDED = ACC['accounts'], ACC['added']
cap = lambda n: open(os.path.join(CAP, n)).read().rstrip()
G = lambda k: M[k]['robert_message']
GT = lambda k: M[k]['robert_thread']
WD = 'C0ADGSZKR3R'
issue = {a['vendor']: a for a in A}
fmt = lambda x: f"{x:,.2f}"
L = []
w = L.append

w("# Scenario Design — rb-winddown-closeout · design only · contains no prompt, OE or criterion text\n")
w("Persona Robert (Co-Founder & Creative Director, Executive) · competency Corporate Ops · task skill Planning and Decision "
  "Support · horizon Long (platform \"Task Type\": long-horizon) · difficulty mode easy · universe date February 14, 2026 "
  "00:00 UTC (Saturday). Author targets (`00_Assigments.md`, chat 2026-10-28): **more than 150 tool calls in every run** and "
  "an average **under 80%**; the Evals line is under 75% (strictest governs), so the design aims at ~62–68%. Builder scripts: "
  "`support/task_work/rb_winddown_closeout/` (`mint_ids.py` mints every id, the seeded wording `planned_text.json` and the "
  "emitted ground truth `truth.json`; `build_manifest.py` writes the draft manifest; `build_design.py` writes this file). "
  "Reference designs: the three tasks in `support/completed_tasks/` (Frederick ×2 missed 75% at 78.3% / 80.8%; Douglas "
  "landed 56.3% after three hardening rounds — its lessons are applied in §6).\n")

# ------------------------------------------------------------------ 0
w("## 0 Assignment, persona census and horizon note\n")
w("| Field | Assigned (verbatim, `00_Assigments.md`) | Resolution |\n|---|---|---|")
w("| persona | Robert | roster `robert`, robert@harmonygames.co, Executive (`Evals/references/persona/roster.json`) |")
w("| role | Co-founder & Creative Director | co-founder; member of #winddown (C0ADGSZKR3R) with Leonard and Arthur; holds the creative-tool logins (Soundly cancelled by him, C0ADGSZKR3R/1770839322.836779; Figma admin, C0ADGSZKR3R/1770859313.592649) |")
w("| business function | Executive | Evals category Founders / Exec / Strategy (`Evals/references/rules/task_categories.md`) |")
w("| competency | Corporate Ops | wind-down account and subscription close-out (timeline 2026-02-09 \"Vendor terminations\" beat) |")
w("| task skill | Planning and decision support | a close-out plan: per account an action, status, deadline, owner and monthly cost, decided by four rule sources, plus the clashes with earlier decisions |")
w("| horizon | long-horizon | manifest `horizon: Long Horizon`, `effective_profile: long` with `profile_exception` (author's >150-call band) |")
w("| universe date | February 14, 2026 00:00 | clock 2026-02-14T00:00:00Z (`tools/hg_clock.py`); latest seed 2026-02-13T20:49:58Z |")
w("| difficulty mode | easy | recorded; author target under 80%, Evals gate under 75%, pass@1 ≤ 3 of 6, SD 0.1–0.3, ≥ 2 failure patterns |\n")
w("**Remit argument.** On Feb 9 the founders decided to shut down (C0ADGSZKR3R/1770663250.160009). Leonard ran the vendor "
  "terminations (Helpshift C0ADGSZKR3R/1770673717.808759, Singular C0ADGSZKR3R/1770674268.840059), asked Robert to cancel "
  "Soundly or move it to his personal card (C0ADGSZKR3R/1770837766.132019), posted a keep list (C0ADGSZKR3R/1770933601.686309) "
  "and action items (C0ADGSZKR3R/1770933903.645709), and said the P&L covered everything (C0ADGSZKR3R/1770933999.157259). "
  "His own plate (C0ADGSZKR3R/1770934638.035469) is Carta, the angels and Sunset onboarding; Arthur took the data hand-off "
  "(C0ADGSZKR3R/1770935695.500189). The base Task List in the Wind Down folder has \"Cancel or move all software "
  "subscriptions\" open with no owner (f_31115ddb6ed866f2b10d60). Pulling the third co-founder in to own the close-out "
  "register before the Google accounts are archived is the Corporate Ops planning work Robert would plausibly get on Feb 13.\n")
w("**Effective profile.** Long Horizon normally maps to `extreme` (≥ 500 calls). The author asked for more than 150 calls "
  "in every run, not a ~600-call design, so the manifest uses the gate's `long` profile (extreme breadth, authorities, "
  f"chains and traps; 100-call floor) with `profile_exception` quoting the author. Necessary budget: **{sum(b['calls'] for b in MAN['call_budget'])} "
  "unconditional calls** (§9). Douglas's 139-call budget measured 163–238 counted calls, so this budget should put the "
  "leanest correct run above 150.\n")
w("Persona reach census (`python3 Task_Authoring/tools/persona_view.py reach robert --top 10`, verbatim):\n")
w("```\n" + cap('reach.txt') + "\n```\n")
w("Linear / GitHub / Trello identities (`entity.py resolve`, §1c): Robert Linear `usr_Robert`, Trello `3d06b73654d0c8940792514c`, "
  "Slack `EMPLOYEE_0016_SLACK_ID`, Confluence `user_EMPLOYEE_0016`. Leonard: Linear `usr_63fffeb4fab5233e`, Trello "
  "`PERSON_6094_TRELLO_USER_ID`, Confluence `user_EMPLOYEE_0038`. Arthur: Linear `usr_cc3e90160f490686`, Trello "
  "`2162c1ba310341bf318f48b7`. Oliver: Linear `usr_bdf01b53c6a92c5e`, Confluence `user_EMPLOYEE_0003`, GitHub "
  "`EMPLOYEE_0003_GITHUB_USERNAME`.\n")

# ------------------------------------------------------------------ 1
w("## 1 Storyline\n")
w("**Arc.** Shutdown was decided on Feb 9 (timeline 2026-02-09, `slack:C0ADGSZKR3R:1770663250.160009`). Over Feb 9–12 the "
  "founders cancel or keep vendors one message at a time in #winddown, sign the wind-down and data agreements with Sunset "
  "(Feb 12 21:29Z, C0ADGSZKR3R/1770931777.561519; signed SOW forwarded to Robert, robert@harmonygames.co/1856956532017091340) "
  "and plan to pay off and close the SVB card once the data money lands (C0ADGSZKR3R/1770927223.969899). At 23:24Z Arthur "
  "turns the costs tab and the #winddown lists into a Linear project, \"Shutdown – accounts\" (47 issues, ENG-2438…ENG-2484). "
  "Leonard books the delivery review with Sunset for Mar 12 (event created 22:40Z) and Sunset's onboarding lead mails the data delivery checklist (23:58Z). "
  "On Feb 13 Arthur amends the keep list in its thread (Gusto), Leonard puts SVB's card terms on the founders' Trello "
  "board, writes the register conventions into a doc in the Wind Down folder, comments on his issues, and at 17:21Z asks "
  "Robert in #winddown to own the register. Sunset corrects its list in the same mail thread at 18:20Z.\n")
w("**Timeline placement** (`references/universe_kb/timeline.md`, clock 2026-02-14): the 2026-02-09 \"wind-down\" and \"vendor\" "
  "beats (Helpshift/Singular Feb 9, Unity Feb 12), 2026-02-11 (termination letters, Google accounts to be archived after "
  "Feb 15, Sunset call `gcal:evt_212e50fb5a53ea8016ce29`), 2026-02-12 (agreements signed, `snowflake:FINANCE_LEDGER/FIN-000702` "
  "Sunset fee), 2026-02-13 (work continues; Combo-Fighters#37 merged) and 2026-01-13 (Combo Fighter monetisation; Meta UA "
  "spend Dec–Feb — the ledger's meta rows). No seed is after 2026-02-13T20:49:58Z.\n")
w("**Anchors per service.**\n")
w("| Service | Record | Role |\n|---|---|---|")
w(f"| slack | {M['S_ANCHOR']['locator']} (seed) | anchor A1, Leonard → Robert, {M['S_ANCHOR']['at']} |")
w("| slack | C0ADGSZKR3R/1770933601.686309, /1770933903.645709, /1770933999.157259, /1770937232.664809, /1770936655.574079, /1770937188.477219, /1770839729.441789, /1770839825.928989, /1770840054.486779, /1770927223.969899 (base) | keep list, action items, 'covers everything', LLC moves, 'cancelled' claims, Gusto/Slack-plan history, card closure |")
w(f"| slack | {M['S_GUSTO_REPLY']['locator']} (seed, thread of 1770933601.686309) | Arthur's Gusto amendment |")
w(f"| slack | {M['S_OLIVER_CURSOR']['locator']} (seed, #prototype) | Oliver asks to keep Cursor (distractor) |")
w(f"| linear | project {M['L_PROJECT']['id']} 'Shutdown – accounts' (seed), ENG-2438…ENG-2484 + {sum(len(a['comment_ids']) for a in A)} comments | cohort; write targets |")
w(f"| gmail | {GT('G_SUNSET1')} (seed thread: {G('G_SUNSET1')} + {G('G_SUNSET2')}) | H1 Sunset's checklist and its correction |")
w(f"| gmail | {GT('G_SHERWOOD')} (seed) | Sherwood checklist decoy |")
w("| gmail | robert@harmonygames.co/1853470745017478863, robert@harmonygames.co/1850283027022457279, robert@harmonygames.co/1854432461283937829, robert@harmonygames.co/1849420841999587093 (base) | Singular billing thread (termination asks for written confirmation), Singular Dec 1 invoice, iPostal1 mailbox closed Jan 16, Trello Standard ended Nov 21 |")
w(f"| gmail | {len([k for k in M if k.startswith('G_') and k not in ('G_SUNSET1','G_SUNSET2','G_SHERWOOD')])} vendor billing mails (seed; §11) | next charge dates, card, Soundly/Kapwing confirmations, Pond5/ElevenLabs |")
w(f"| trello | {M['T_SVB']['id']} (seed, board 640643a3fd8f3ca308d9318e list To Do) | H2 'SVB card payoff + closure' |")
w("| trello | 64de736c2b10abdbda220c1b (base #170, same board, Done 2024) | decoy: the 2023 move of subscriptions onto the SVB card |")
w(f"| gdocs | {M['DOC_CONV']['id']} (seed, parent d_e5caf6a8c630421942ee59 'Wind Down') | H3 'Close-out register conventions' |")
w(f"| gdrive | {M['SHEET_SUBS']['id']} (seed) | Arthur's superseded 'Subscriptions' sheet |")
w("| gsheets | f_605121f4a36752645e0ac3 'HG Costs' (base) | cost lines (rule 3 membership); 'Sound (Pond5, Soundly,Elevenlabs)' and 'UA' shared lines; stale December figures (cost decoy) |")
w("| snowflake | FINANCE.EXPENSES.FINANCE_LEDGER FIN-000687…FIN-000700 (base) | AWS 1,485; meta −2,843.84/−956.45; applovin −9.80/−9.83 |")
w(f"| gcal | {M['E_REVIEW']['robert_copy']} (seed, Robert's copy of 3; ical {M['E_REVIEW']['ical_uid']}) | review call 2026-03-12 17:00Z |")
w(f"| linear | {issue['Helpshift']['comment_ids'][0]} (Oliver's ENG-2439 comment) + drive helpshift_export_2026-02-13.zip | Helpshift export done Feb 13 |")
w(f"| confluence | {M['CONF_UA']['id']} (seed, 2025-03-18) | Growth/UA conventions decoy |")
w(f"| github | {M['GH_PR']['id']} + {M['GH_CR']['id']} (seed) | CodeRabbit's own cancellation notice |\n")
w("**Cohort.** `cohorts.json: no fit — the cohort is the seeded Linear project (45 issues, created Feb 12) plus four accounts "
  "the project lacks; the nearest base cohort, LIN-OPEN-ENG (115 open ENG issues), holds none of them and is not touched` "
  "— the seeded issues take ENG-2438… after the base maximum ENG-2437; LIN-CQ11 (ENG created 2025-Q4, 61) ends before them. "
  "SF-LEDGER (FINANCE_LEDGER rows by category, 704) is the ledger population rule 3 points into; its `hazards_inside` "
  "(Q05 burn vs ledger) are not read by the task (only Jan/Feb rows by counterparty).\n")
w("**Natural traps used** (`references/universe_kb/trap_catalog.json`): X03 (the costs tab's blanked '[PERSON_NAME_0499]' is "
  "Singular — named in Arthur's description), D04/D08 (P&L workbook versions; only the January workbook's costs tab is "
  "named), D07 (the founders' Trello board is stale since Nov 2025 — H2 revives it with one card), C01 (a reply that "
  "corrects — Arthur's Gusto reply, Sunset's correction), B03 (CodeRabbit bot activity — its notice is the confirmation), "
  "B05 (Zapier pipes Helpshift into #issuefeed — Oliver's note), K02 (app-name lineage, not used), P02 (Brooks: Oliver "
  "vs Lauren).\n")
w("**Originality.** Not the Combo Fighters launch record, the 133-PR residue register, the RC-flag gate or the art-canon "
  "handoff; not the Frederick card-spend or account-handover tasks (Frederick's reconciled card charges to receipts; this "
  "task decides an action per vendor account under four rule sources) and not Douglas's beta sign-off (tickets × deploys).\n")

# ------------------------------------------------------------------ 1a
w("## 1a Coherence audit\n")
w("Scope = every record a correct run opens: the #winddown history Feb 9–13, the keep-list thread, #prototype's Cursor "
  "message, the 47 issues and their comments, Sunset's and Sherwood's mails, the 18 seeded billing mails, the base Workspace and ElevenLabs receipts and the base Singular, "
  "iPostal and Trello mails, the two Trello cards, the conventions doc, Arthur's sheet, the January P&L costs tab, the "
  "Jan/Feb ledger rows, the review event, the UA page, page_aws_infra and "
  "Combo-Fighters#38. Known hazards walked from `references/universe_kb/coherence_hazards.json` (all six categories).\n")
w("| Record | Category | Fields | Evidence pointer | Hazard id | Disposition |\n|---|---|---|---|---|---|")
rows1a = [
 ("Seeded mail threads (Sunset checklist + correction)", "temporal", "message dates in thread order", f"{GT('G_SUNSET1')}", "hazard T02", "avoid: both messages in ISO date order, the correction 18h after the checklist"),
 ("Base support playbook page contradicts itself", "semantic", "page body vs comments", "page_support_playbook (base)", "hazard S08", "avoid: the Helpshift export is logged on a seeded page (page_support_after_helpshift), so page_support_playbook is neither modified nor cited"),
 ("Storyline YAML artifacts dated 2026-02-13", "temporal", "artifacts absent from base", "slack:C0ADGSZKR3R (Feb 13 base posts: none)", "hazard T07", "avoid: no seed references a YAML artifact; seeds carry their own ids"),
 ("Contacts job titles (Robert 'CPO', Leonard 'CEO')", "semantic", "job", "contacts.json /contacts/108, contacts.json /contacts/170", "hazard S06", "avoid: no seed or graded value uses a Contacts title"),
 ("Gemini notes misname the entity", "semantic", "entity name", "f_0c37bb7235683d73569903", "hazard S07", "avoid: Leonard-private; not cited or read"),
 ("Slack links to native Google ids", "cross-service referential", "folder link", "C0ADGSZKR3R/1770673821.508389", "hazard R04", "avoid: seeds name the Wind Down folder and every file by title"),
 ("Calendar invitations with no GCal instance", "cross-service referential", "invitation mails", M['E_REVIEW']['robert_copy'], "hazard R08", "fold in: the review event is seeded on all three calendars with no invitation mails (integration_exceptions no_notify), so no orphan mail and no orphan event"),
 ("Helpshift balance quoted three ways", "quantitative", "$1,500 / $150×8 / $300", "C0ADGSZKR3R/1770673467.186629, C07C2866011/1770765511.243329, C04UEQVDVB7/1770765910.100299", "hazard Q07", "fold in: balances owed, not the monthly cost; the register uses the costs tab 150 and Leonard's comment quotes Helpshift's final $300 invoice — consistent with the last of the three"),
 ("Keep-list parent counters after the Gusto reply", "quantitative", "reply_count / latest_reply", "C0ADGSZKR3R/1770933601.686309", "hazard Q01", "fold in: UPDATE companion sets reply_count 1, reply_users_count 1, latest_reply = the reply ts"),
 ("P&L vs Snowflake cash", "quantitative", "month-end cash", "f_605121f4a36752645e0ac3, CASH_BALANCE", "hazard Q06", "avoid: only the HG Costs tab is used; no cash figure is graded"),
 ("Combo-Fighters#37 merged after the announcement; CodeRabbit comment", "state/lifecycle", "merge vs shutdown", "harmonygames-Games/Combo-Fighters#37", "hazard L13", "avoid: the CodeRabbit notice is seeded on a new open PR #38; #37 is not modified or cited"),
 ("Open issues assigned to quiet people", "state/lifecycle", "assignee", "ART-384", "hazard L08", "avoid: every seeded issue is assigned to Leonard, Arthur or Robert (active_feb_2026)"),
 ("Linear ids not usr_ + 16 hex", "identifier/format", "assignee_id", "usr_Robert on ART-100 (base)", "hazard I10", "fold in: Robert's base id usr_Robert is used verbatim on his issues"),
 ("Drive owner is a Resource token", "identifier/format", "owner_email", "f_31115ddb6ed866f2b10d60", "hazard I14", "fold in: the conventions doc copies the Wind Down siblings' owner 'Resource: 7240535625619857401' and share list"),
 ("Mailbox file aliases", "identifier/format", "thread file names", "blake@harmonygames.co_1856689465050769375.json", "hazard I03", "fold in: copies of Sunset/Sherwood mails filed under the base aliases (leonard@, blake@)"),
 ("Token-owned billing mailboxes / senders", "identifier/format", "sender tokens", "SVC_5771_EMAIL (Unity), SVC_0019_EMAIL (Singular, robert@harmonygames.co/1850283027022457279)", "hazard I05", "fold in: seeded billing mails reuse the vendor's base sender token where one exists; new vendors get new SVC_77nn tokens"),
 ("'Sunset' counterparty redacted in Slack", "other", "[USERNAME_26907]", "C0ADGSZKR3R/1770931777.561519", "none (other)", "fold in: the signed SOW mail (robert@harmonygames.co/1856956532017091340) names Sunset; the checklist thanks them 'for signing today'"),
]
for r in rows1a:
    w("| " + " | ".join(r) + " |")
w("")
w("**Sibling-defect sweep.** For each designed defect, other records with the same kind in scope:\n")
w("- *Stale costs-tab forecast:* iPostal (tab 34.79 in Dec-25; closed Jan 16, robert@harmonygames.co/1854432461283937829) is designed. "
  "Siblings: Trello (tab 0 since its Standard plan ended Nov 21 — consistent), AWS (tab 0 while the ledger shows 1,485/month, "
  "FIN-000687), UA (tab 0 while meta/applovin charge, FIN-000689/FIN-000688), Kling (tab 9 in Sep-25, 0 since — consistent with "
  "Robert's 'dropped after the september trial'). AWS, meta and applovin take their own January ledger line under rule 8 (the costs-tab AWS/UA values decide nothing); UA membership is rule 3; none is left as a silent second answer.")
w("- *'Cancelled' said in Slack without the vendor's word:* Layer (C0ADGSZKR3R/1770837793.168589), CodeRabbit "
  "(C0ADGSZKR3R/1770936655.574079), Cursor and Kapwing (C0ADGSZKR3R/1770937188.477219), Zapier (Leonard's list C0ADGSZKR3R/1770933450.410449), Soundly (C0ADGSZKR3R/1770839322.836779), "
  "Helpshift (C0ADGSZKR3R/1770789534.434749). Every one is a cohort issue with a designed status; Soundly, Kapwing, Helpshift and "
  "CodeRabbit have a vendor confirmation, Layer, Cursor and Zapier do not, Singular's own thread asks for one that never came "
  "(robert@harmonygames.co/1853470745017478863, Feb 12 21:43Z).")
w("- *Blanked vendor names:* '[PERSON_NAME_0499]' (Singular, X03), the hosting line '[PERSON_NAME_0250]' (GitHub: its Sep–Dec values 165/169/105/86 are Arthur's GitHub receipts), '[PERSON_NAME_20852]' "
  "(Kapwing per C0ADGSZKR3R/1770933450.410449) and '[USERNAME_30019]' (dbt in base Slack, C0ADGSZKR3R/1770937232.664809) are resolved by base records, not "
  "Arthur's project description; the two $30 game-ops lines are named as stipends. The redacted names in #winddown are not relabelled (injection review F2): Leonard's subscriptions table (C0ADGSZKR3R/1770933450.410449) names Kapwing outright, and Arthur's own comment on the dbt issue says dbt is on his KubLLC card.")
w("- *Accounts on Leonard's own card ('I canceled other subscriptions under mine', C0ADGSZKR3R/1770933601.686309):* "
  "no seeded receipt names a card number; which card an account bills is stated by its holder in the issue (Intuit on the SVB card per its receipts, Deel by bank transfer; base: the SVB card is a "
  "MasterCard, leonard.hayes@harmonygames.co/1846148320251001978), so no hidden personal-card account exists.\n")

# ------------------------------------------------------------------ 1b
w("## 1b Active speakers\n")
w("Every person given a seeded voice, with `status_at_clock` from `references/universe_kb/activity.json` (clock 2026-02-14).\n")
w("| Person | Email | status_at_clock (activity.json) | Seeding role |\n|---|---|---|---|")
w("| Leonard Hayes | leonard.hayes@harmonygames.co | active_feb_2026 | anchor; conventions doc; SVB card; comments on his issues; review event organizer |")
w("| Arthur Blake | arthur.blake@harmonygames.co | active_feb_2026 | Linear project and 47 issues; Gusto reply; comments on his issues; 'Subscriptions' sheet |")
w("| Robert | robert@harmonygames.co | active_feb_2026 | persona; comments on his own issues (Feb 13 20:41–20:49Z) |")
w("| Oliver Brooks | oliver.brooks@harmonygames.co | active_feb_2026 | Cursor request in #prototype; Zapier note; Helpshift export comment; PR #38 author |")
w("| Frederick Stone | frederick.stone@harmonygames.co | quiet_since_2025-10 | author of the 2025-03-18 UA conventions page only (he was active then) |\n")
w("Vendors write only billing mail through the billing group (base precedent robert@harmonygames.co/1850283027022457279); "
  "CodeRabbit (`PERSON_6026_GITHUB_USERNAME`) writes only its PR notice; Sunset's onboarding lead and Sherwood write one "
  "mail thread each. Seeded text follows `references/universe_kb/conventions.json` (Arthur lowercase and short, Leonard "
  "plain sentences, Linear comments one line).\n")

# ------------------------------------------------------------------ 1c
w("## 1c Identity traps\n")
w("`python3 Task_Authoring/tools/entity.py collisions` (verbatim, first sections) and `resolve` for every person the design names:\n")
w("```\n" + cap('coll.txt') + "\n" + cap('resolve.txt') + "\n```\n")
w("Correct entity vs lookalikes: Oliver Brooks is oliver.brooks@harmonygames.co (not Lauren Brooks, lauren@harmonygames.co, "
  "active_jan_2026_quiet_in_feb); Arthur's mailbox files are `blake@…`, Leonard's `leonard@…`. 'Sunset' is the wind-down "
  "provider (signed SOW robert@harmonygames.co/1856956532017091340), not the 'Sunset of Creative Reporting' notices "
  "(robert@harmonygames.co mail 00014921) or Sunset's platform invite sender SVC_0210 (robert@harmonygames.co/1856871927204514890). "
  "'Intuit' and 'QuickBooks' are one vendor (rule 1). 'Meta' appears as ad spend (ledger marketing_ua) and as Audience Network "
  "self-billing (robert@harmonygames.co mail 00016816, revenue) — only the spend account is a register row. 'AppLovin' is UA "
  "spend (marketing_ua) and MAX ad revenue (FIN-000697) — only the UA account is a row.\n")

# ------------------------------------------------------------------ 2
w("## 2 Cohort spine\n")
w("**Rule (K2 + H3).** Every issue of the Linear project 'Shutdown – accounts' (47, ENG-2438…ENG-2484), plus accounts the "
  "project lacks that (a) still charge us in the January/February ledger lines, (b) share a costs-tab line with an account "
  "in the project, or (c) are on Sunset's corrected list. Then rule 1 (one row per vendor account; the newer of two issues "
  "for one vendor is the duplicate) and rule 2 (exclusions; Sunset's list overrides them). Candidates **52**; register rows "
  f"**{TR['counts']['rows']}**; excluded issues **{TR['counts']['excluded']}**.\n")
w("**Per-account truth** (emitted by `mint_ids.py` → `truth.json`; deadlines are the conventions' rule 6, costs rule 8):\n")
w("| Issue | Account | Action | Status | Deadline | Owner | Monthly cost | Cost source | Decisive evidence |\n|---|---|---|---|---|---|---|---|---|")
ev = lambda e: ", ".join(G(x) if x.startswith('G_') else (M[x]['robert_copy'] if x == 'E_REVIEW' else (M[x]['id'] if x in M else x)) for x in e) or "comments / tab"
for r in TR['rows']:
    w(f"| {r['issue']} | {r['account']} | {r['action']} | {r['status'] or '—'} | {r['deadline']} | {r['owner']} | {fmt(r['cost'])} | {r['cost_src']} | {ev(r['evidence'])} |")
w(f"\nTotals: every row today **{fmt(TR['total_today'])}**; Keep + Hold after the plan **{fmt(TR['total_after'])}**. "
  f"Actions: {dict(TR['counts']['by_action'])}; Cancel statuses: {dict(TR['counts']['by_status'])}.\n")
w("**Excluded issues → Canceled** (rule 2 / rule 1):\n")
w("| Issue | Vendor | Why out |\n|---|---|---|")
for o in TR['excluded']:
    w(f"| {o['issue']} | {o['vendor']} | {o['why']} |")
w("")
w("**Surfaces and shortcut audit.**\n")
w("| Surface | Tool | Records | What it decides | Bulk call that does not cover it |\n|---|---|---|---|---|")
for s in MAN['cohort']['evidence_surfaces']:
    w(f"| {s['service']} | {s['tool']} | {s['records']} | {s['requirement']} · {s['decides']} | {s['why_no_bulk']} |")
w("")
dec = [a for a in A if any(c[3] for c in a['comments'])]
w(f"**Necessity rule.** Comments sit on {sum(1 for a in A if a['comments'])} of {len(A)} issues; {len(dec)} are decisive "
  f"({', '.join(a['issue'] for a in dec)}), the rest neutral ('we went to basic at the renewal', 'robert cancelled this on the "
  "11th per #winddown', 'same account as the quickbooks issue', 'cancelled. lite plan, 3 seats at $15' — CodeRabbit's status comes from GitHub, not this "
  f"comment). {sum(1 for a in A if not a['comments'])} issues have no comment, so having a comment reveals nothing; the decisive subset (~40%) is not "
  "predictable from title, state, assignee or description. Billing mails exist for 21 accounts, including Keep/Hold ones, "
  "so finding a receipt does not flag a Cancel row.\n")
w("**Short-circuit audit.** Linear comments: the status, owner and in/out columns are written per issue whatever Gmail "
  "says; a run that reads only descriptions gets Docusign's owner, Unity/Layer/Singular's status, OpenAI/Typecast/Adobe/"
  "Solsten/JetBrains's exclusion and Metabase/dbt/GitHub's card wrong. Gmail: the deadline column for 14 Cancel rows "
  "and the move/no-move decision for 6 Keep/Hold rows need the next charge date; no comment carries it. One filtered "
  "search cannot sweep it: the senders are 12 different tokens, and a 'receipt' search returns hundreds of Google Play, "
  "SVB and Bizxpress mails (robert@harmonygames.co mail 00016326, 00016329) — each vendor has to be found by name.\n")
w("**House rule overriding the natural reading (A15).** Rule 5: an account is Closed only when the vendor itself has "
  "confirmed. Arthur's and Leonard's 'cancelled' messages (C0ADGSZKR3R/1770936655.574079, /1770937188.477219, "
  "/1770837793.168589) read as closed; under rule 5 Layer, Cursor and Zapier are Requested, CodeRabbit and Kapwing Closed (bot "
  "notice, cancellation mail).\n")
w("**Dual regime.** Not used — one rule set applies to every account; the time element is the supersession chain "
  "(keep list → thread reply; checklist → correction).\n")
w("**Boundary records (A17).** Inside: Pond5 and ElevenLabs (share the Sound line), Meta Ads and AppLovin (UA) (ledger "
  "only), Trello (excluded by its Nov downgrade but held by Sunset). Outside: iPostal "
  "(tab still forecasts it), Intuit (duplicate), Arthur's 18-row sheet (stale shorter list), Legal & accounting and Sunset "
  "in the ledger (professional firms, rule 2).\n")

# ------------------------------------------------------------------ 3
w("## 3 Hidden authorities\n")
w("| Id | Name (as the hub names it) | Home | Governs | Decoy (scope) | Findability proof |\n|---|---|---|---|---|---|")
w(f"| H1 | Sunset's data checklist | gmail {GT('G_SUNSET1')} (checklist {G('G_SUNSET1')} + correction {G('G_SUNSET2')}) | R2, R7 | gmail {G('G_SHERWOOD')} Sherwood's checklist (issuer: Sherwood, not engaged) | `hg.py search search gmail \"data delivery checklist\"` returns the seeded thread (planned; base has no hit for the phrase) |")
w(f"| H2 | SVB's card terms | trello {M['T_SVB']['id']} 'SVB card payoff + closure' (founders' board, To Do) | R4 | trello 64de736c2b10abdbda220c1b base card #170 'move subscriptions to SVB credit card' (Done, 2023–24) on the same board | `trello_search` 'SVB card' / board card list returns both cards |")
w(f"| H3 | the conventions doc in the Wind Down folder | gdocs {M['DOC_CONV']['id']} 'Close-out register conventions' | R1, R3, R6 | confluence {M['CONF_UA']['id']} 'Vendor close-out conventions (Growth/UA)' (team: Growth/UA tracker, 2025) | `gdocs` search 'close-out register conventions' returns the doc; a Confluence search for 'close-out conventions' returns the decoy |\n")
w("`governs` lists do not overlap. H1's correction is A14 (a reply inside the thread). H2 is A12 (Trello, opened in 50/131 runs) "
  "with a same-board decoy; Gmail has 162 SVB notification threads (`references/Scenario_Atlas.md` §1) and none of them "
  "dates the closure. H3's decoy carries the same search terms ('close-out conventions') and differs on cost and closed "
  "rules for another team's tracker.\n")

# ------------------------------------------------------------------ 4
w("## 4 Delegation lattice\n")
w("| Anchor | Anchor name (noun phrase, ≤ 6 words) | Record |\n|---|---|---|")
w(f"| A1 | Leonard's close-out register ask | {M['S_ANCHOR']['locator']} |\n")
w("**Hub.** A1 is Leonard's message in #winddown: it names the deliverable columns, the destination (a sheet shared with "
  "him and Arthur as editors), the Linear write and the reply, and delegates by name to the project, the keep list and "
  "its replies, Arthur's LLC moves, Sunset's checklist, SVB's card terms and the conventions doc.\n")
w("| Fragment | Service | Container | Record | Kind | Delegated by | Delegation quote (verbatim) | Requirements |\n|---|---|---|---|---|---|---|---|")
for f in MAN['ask_fragments']:
    rec = (f['seeded_ids'] or f['base_pointers'])[0]
    w(f"| {f['id']} | {f['service']} | {f['container']} | {rec} | {f['kind']} | {f['delegated_by_record']} | \"{f['delegation_quote']}\" | {', '.join(f['requirement_ids'])} |")
w("")
w("**Amendments.** K9 (Slack thread reply, Feb 13 02:14Z) changes Gusto from Keep to Cancel and leaves the rest of the keep "
  "list standing; K4 (Gmail reply, Feb 13 18:20Z) adds Trello, BigQuery and dbt and removes Metabase ('The rest of the list "
  "stands'). No later record re-asserts either amended clause (searched 'gusto' and 'metabase' over the seeded rows in "
  "`planned_text.json`).\n")
w(f"**Distractors outside the chain.** Oliver's request to keep Cursor ({M['S_OLIVER_CURSOR']['locator']}), Sherwood's checklist, "
  f"Arthur's 'Subscriptions' sheet ({M['SHEET_SUBS']['id']}), the 2023 SVB-move card, the UA conventions page, page_aws_infra's ~$1,550, "
  "the Helpshift balance messages and the Singular Mar 15 extension.\n")

# ------------------------------------------------------------------ 5
w("## 5 Chains and trap register\n")
w("| Chain | Mechanism | Hops (service · record · finding) | Ends in |\n|---|---|---|---|")
for c in MAN['chains']:
    hops = " → ".join(f"{h['service']} {h['record']}: {h['finding']}" for h in c['hops'])
    w(f"| {c['id']} | {c['root_cause']} | {hops} | {c['ends_in']} |")
w("")
w("| Trap | Family | Records | Requirement | Expected wrong reading | Resolver | Discovery order |\n|---|---|---|---|---|---|---|")
for t in MAN['traps']:
    recs = ", ".join((t.get('seeded_ids') or []) + (t.get('base_pointers') or []))
    fam = t['family'] + (f" ({t['distractor_type']})" if t.get('distractor_type') else '')
    w(f"| {t['id']} | {fam} | {recs} | {t['requirement']} | {t['expected_wrong_reading']} | {t['resolver']} | {t.get('discovery_order', '—')} |")
w("")
w("**Trap independence.** T1 (thread reply), T5/T4 (mail-thread correction), T8 (ledger), T9 (Trello), T13 (GitHub notice), "
  "T14 (calendar), T15 (Confluence comments) and T7 (shared costs line) each need a different read; a run that has beaten "
  "all the others still fails each one it skips. T4 and T5 fall to the same reply and are counted as one discovery in §6. "
  "No record states a conclusion: the SVB card never lists accounts, the checklist never names a deadline, the review "
  "event never mentions holds, and no comment says 'Closed' or 'Requested'.\n")

# ------------------------------------------------------------------ 6
w("## 6 Failure-diversity plan\n")
w("Douglas's lessons (memory, 2026-10-27): every hidden fact must decide two or more rubric rows; levers must be "
  "independent ~50% habits, not one 'deep reader' trait; never hide a fact on the ask itself; project with "
  "`difficulty_stats.py` on an atomic, work-weighted rubric.\n")
w("| Discovery (lever) | Habit it tests | Rows it decides | Expected find rate |\n|---|---|---|---|")
w("| D1 Sunset's correction (K4, in-thread reply) | opening the second message of a mail thread | Trello, dbt, BigQuery, Metabase action; dbt/BigQuery deadline; T2 | ~0.5 (Gmail get_thread 1/6–5/6 in Douglas) |")
w("| D2 Gusto reply (K9, Slack thread) | opening a thread on a message the run already read | Gusto action, status, deadline; total after | ~0.5–0.7 (reply_count 1 on a key message) |")
w("| D3 ledger UA lines (T8) | opening Snowflake on a doc's instruction | Meta Ads and AppLovin rows (membership, cost, deadline); total today | ~0.4 (Snowflake 46/131) |")
w("| D4 SVB card on Trello (H2) | searching Trello for a named rule | six Keep/Hold Feb 19 deadlines | ~0.5 (Trello 50/131) |")
w("| D5 review call date (K5, GCal) | opening Calendar for a referenced meeting | five Hold deadlines (Mar 12) | ~0.3–0.5 (Calendar 5/131, but the mail names the call) |")
w("| D6 CodeRabbit notice (GitHub) | looking for a bot confirmation outside mail | CodeRabbit status/deadline; Done vs open | ~0.3 |")
w("| D7 Confluence comments (T15) | listing page comments | Helpshift deadline | ~0.25 (Douglas: 2/6, 1/6) |")
w("| D8 Sound line split (T7) + Pond5/ElevenLabs mail | reading a costs line as several accounts | two rows, Soundly cost, total today | ~0.5 |")
w("| D9 rule 5 per record (A15) | applying a house rule against 'cancelled' claims | Layer, Cursor, Unity, Singular status | ~0.6 |\n")
w("No single discovery decides more than ~15% of the register's cells; D1 and D3 each touch both totals, so the totals rows "
  "fail for different reasons in different runs. Expected shape: no run finds all nine; typical runs find 4–6, so the "
  "failing sets differ on several rows (≥ 2 failure patterns, largest ≤ 50%). Predicted average ~62–70% before the "
  "rubric exists; the rubric stage must replay `difficulty_stats.py` against this lever table, as Douglas round 3 showed.\n")

# ------------------------------------------------------------------ 7
w("## 7 Deliverables and dependent writes\n")
w("| Write | Service · tool | Content depends on | Requirements |\n|---|---|---|---|")
for i, x in enumerate(MAN['writes'], 1):
    w(f"| W{i} | {x['service']} · {x['tool']} ×{x['count']} | {', '.join(x['depends_on'][:12])}{' …' if len(x['depends_on']) > 12 else ''} | {', '.join(x['requirements'])} |")
w("")
w(f"- W1: one register sheet in Robert's Drive ({TR['counts']['rows']} rows: account, action, status, deadline, owner, monthly "
  f"cost) with the two totals ({fmt(TR['total_today'])} / {fmt(TR['total_after'])}). The Wind Down folder is not writable "
  "or readable for Robert (owner 'Resource: …', empty share list), so A1 asks for sharing, not a folder.")
w(f"- W2: shared with leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co as writers.")
w(f"- W3: Done on {', '.join(TR['linear']['done'])}; Canceled on the {len(TR['linear']['canceled'])} excluded issues; the "
  f"{len(TR['linear']['open'])} other issues stay open; one comment on each of the 47 (what happens, by when).")
w(f"- W4 (reuse vs create, A8): new issues in the project for {', '.join(TR['linear']['new_issues'])} — Soundly's issue is "
  "not reused for Pond5/ElevenLabs (one issue per vendor).")
w("- W5: a reply in Leonard's thread with both totals and the three clashes (Slack downgrade to free; cutting Slack to three paid seats and guests; archiving Google "
  "accounts after Feb 15) against Sunset's hold until Mar 12.\n")

# ------------------------------------------------------------------ 8
w("## 8 Service role map\n")
w("| Service | Role | Load-bearing fact / write | Carrier |\n|---|---|---|---|")
for svc, v in MAN['services'].items():
    w(f"| {svc} | {v['role']} | {v['weight_reason']} | ● |")
w("| contacts | not used | no vendor contacts exist; no write needs an address beyond the two founders | — |")
w("| gslides | not used | the BoD Jan 14 deck (f_65ada5e24989d256cabdfa) has no vendor list; nothing graded | — |\n")
w("Carriers: Linear comments ● (Ask_Carriers §6b), Gmail bodies ●, Trello card desc ●, Docs body ●, Slack messages ●, "
  "Confluence comments ●, GitHub PR comments ●, Sheets cells ●, Snowflake rows ●. No load-bearing fact sits in a GCal "
  "description, Slides notes or Drive `content_text` (○): the review event's load-bearing field is its start time.\n")

# ------------------------------------------------------------------ 9
w("## 9 Call budget\n")
w("| Phase | Service | Calls | Necessity |\n|---|---|---|---|")
for b in MAN['call_budget']:
    w(f"| {b['phase']} | {b['service']} | {b['calls']} | {b['reason']} |")
tot = sum(b['calls'] for b in MAN['call_budget'])
w(f"\n**Total {tot}**, all unconditional; 11 services; largest share outside the per-record phase 25% (Linear). Golden-run "
  "rule: a correct run must open each issue's comments, settle each issue and find each billing account's receipt; "
  "decoy reads, read-backs and repeated searches are not counted. Measured runs add discovery searches on top (Douglas: "
  "+17% to +71% over budget).\n")

# ------------------------------------------------------------------ 10
w("## 10 QC rails\n")
w("### Two-reading table\n")
w("| Decision point | Best reading | Strongest alternative | Resolved by |\n|---|---|---|---|")
tr_rows = [
 ("Trello: excluded (paid plan ended Nov 21) or held", "Hold for Sunset, cost 0, Mar 12", "out: cancelled before Feb 9 (robert@harmonygames.co/1849420841999587093)", f"rule 2 exception + correction {G('G_SUNSET2')} (newer, names Trello)"),
 ("Metabase: Hold (first checklist) or Move", "Move to Arthur's LLC, dash", f"Hold for Sunset ({G('G_SUNSET1')})", f"correction {G('G_SUNSET2')} removes it; Arthur's comment on ENG-2456 confirms the KubLLC card"),
 ("GitHub: Move (Arthur's LLC message) or Hold", "Hold for Sunset, Mar 12 (already off the SVB card)", "Move to Arthur's LLC (C0ADGSZKR3R/1770937232.664809)", "rule 4: Sunset's list wins over everything above"),
 ("Gusto: Keep or Cancel", "Cancel, Open, Feb 28", "Keep (C0ADGSZKR3R/1770933601.686309)", f"newer reply in that thread ({M['S_GUSTO_REPLY']['locator']}) incorporated by A1 'the replies under it'"),
 ("CodeRabbit: Closed or Requested", "Closed (vendor's notice)", "Requested (only Arthur's word in Slack)", f"{M['GH_CR']['id']} is CodeRabbit's own notice; rule 5 lists 'an in-app or bot notice'"),
 ("Singular deadline: Feb 28 or Mar 14", "Feb 28 (next quarterly invoice Mar 1)", "Mar 14 (extension to Mar 15)", "Mar 15 is the overdue balance's due date (robert@harmonygames.co/1853470745017478863); invoices Sep 1 and Dec 1 (robert@harmonygames.co/1850283027022457279) fix the quarterly cycle"),
 ("Helpshift deadline: dash or Feb 27", "dash (export done)", "Feb 27 (export pending before Feb 28)", f"{issue['Helpshift']['comment_ids'][0]} (Oliver, Feb 13) logs the export; rule 6 dash"),
 ("Figma deadline: Feb 19 or Mar 12", "Mar 12", "Feb 19 (card on file is the SVB card)", f"{G('G_FIGMA')}: next charge Sep 11, 2026 ($1,212 annual, tab Sep-25) — after the review call; rule 6 'won't charge it again before Sunset's review call'"),
 ("Meta Ads cost: Jan 2,843.84, Feb 956.45, the UA line 610 or 30-day spend", "2,843.84", "610 (UA line on the costs tab) / 956.45 (last ledger line) / trailing 30-day (UA page)", "rule 8: the UA line is shared by two accounts → own last full month (January) in the ledger; UA page scoped to the Growth/UA tracker"),
 ("Docusign owner: Leonard or Robert", "Robert", "Leonard (assignee)", f"rule 7 + Leonard's comment {issue['Docusign']['comment_ids'][0]} handing it over"),
 ("Clashes to report: which", "Slack free plan; Slack cut to three paid seats + guests; Google archiving after Feb 15", "also Metabase/GitHub moves, Gusto", "the three decided steps Sunset's hold forbids (C0ADGSZKR3R/1770840054.486779, /1770842405.931359, /1770933903.645709); card moves close nothing; extras are accepted, the three are the minimum"),
 ("Confluence: on the register", "Hold for Sunset, cost 0, owner Robert", "out (never billed; not in the project)", f"Sunset's list ({G('G_SUNSET1')}) + rule 2 exception; rule 8 'accounts that have never charged us are 0' (no Atlassian charge in Robert's mail); rule 7 'anything you add is yours'"),
]
for r in tr_rows:
    w("| " + " | ".join(r) + " |")
w("")
w("### Reach table (load-bearing records)\n")
w("`python3 Task_Authoring/tools/persona_view.py can-see robert <service> <id>` for every scoped base record the design "
  "leans on (all YES); seeded records are planned in Robert's mailbox / calendar / shares and are checked by `check-sql` at "
  "the injection gate.\n")
w("| Record | Service | can-see robert | Reason |\n|---|---|---|---|")
for rec in ["C0ADGSZKR3R/1770933601.686309", "C0ADGSZKR3R/1770933903.645709", "C0ADGSZKR3R/1770933999.157259",
            "C0ADGSZKR3R/1770937232.664809", "C0ADGSZKR3R/1770936655.574079", "C0ADGSZKR3R/1770937188.477219",
            "C0ADGSZKR3R/1770839729.441789", "C0ADGSZKR3R/1770839825.928989", "C0ADGSZKR3R/1770840054.486779",
            "C0ADGSZKR3R/1770927223.969899", "C0ADGSZKR3R/1770673467.186629", "C0ADGSZKR3R/1770931777.561519"]:
    w(f"| {rec} | slack | YES | member of private #winddown |")
for rec in ["robert@harmonygames.co/1853470745017478863", "robert@harmonygames.co/1850283027022457279",
            "robert@harmonygames.co/1854432461283937829", "robert@harmonygames.co/1849420841999587093",
            "robert@harmonygames.co/1856956532017091340"]:
    w(f"| {rec} | gmail | YES | own mailbox |")
w("| f_605121f4a36752645e0ac3 | gsheets | YES | shared with robert@harmonygames.co |")
w("| evt_212e50fb5a53ea8016ce29 | gcal | YES | Robert's calendar (Sunset call context) |")
w(f"| {M['DOC_CONV']['id']} (planned) | gdocs | planned | shared with robert@harmonygames.co like its Wind Down siblings f_31115ddb6ed866f2b10d60 |")
w(f"| {M['E_REVIEW']['robert_copy']} (planned) | gcal | planned | Robert's own calendar copy |")
w(f"| {GT('G_SUNSET1')} (planned) | gmail | planned | Robert cc'd; copy in his mailbox |")
w("\nUnscoped and always readable: Linear, Trello, Confluence, GitHub, Snowflake. The Wind Down folder itself is not "
  "readable by Robert and is not load-bearing (the doc is found by title).\n")
w("**Feasibility.** Writes in `Evals/references/tools/catalog.json`: `gsheets_create_spreadsheet`, `gsheets_values_update`, "
  "`gdrive_share_file` (role writer), `linear_update_issue` (state), `linear_create_comment`, `linear_create_issue` "
  "(project), `slack_post_message` with `thread_ts`. Robert owns the sheet he creates; Linear is unscoped; he is a #winddown "
  "member. Values observable to the cent in the tab, the ledger and the receipts.\n")
w("**Explicit rules.** Temporal comparison: newer replies amend (A1 'the replies under it'; Sunset 'we'll reply on this "
  "thread'). Duplicates: rule 1 (newer issue). 'Now': clock Feb 14; deadlines are future dates. Write end states: "
  "Done / Canceled / open per K2. Every cross-reference postdates its target: A1 (Feb 13 17:21Z) after the doc (16:38Z), the card "
  "(15:52Z) and the project (Feb 12 23:24Z); the checklist (Feb 12 23:58Z) after the review event it calls booked "
  "(created Feb 12 22:40Z) and after the signing (21:29Z); the correction (Feb 13 18:20Z) after the checklist.\n")
w("**Precedence.** Every load-bearing fact is in a ● carrier (Ask_Carriers §5 as amended by §6b).\n")
w("**Prompt naturalness.** The trigger names the anchor in plain words (Leonard's close-out register ask), the deadline "
  "(before Leonard archives the Google accounts) and the deliverables (register, Linear, reply). It must not name Sunset's "
  "list contents, the SVB date, the Trello board, the ledger, the Sound line, any account, the review date or the totals.\n")
w(f"**Grading devices.** Exact set of {TR['counts']['rows']} account rows; per-column spot checks (≤ 5 per group) + "
  "a volume row; the two totals; Linear exact sets (4 Done, 21 Canceled, 5 new); one row per share target; the reply's "
  "three clashes (extras such as the GitHub card move accepted). Hidden-fact rows at weight 5; avoid always-pass per-issue rows (Douglas round 3).\n")

# ------------------------------------------------------------------ 11
w("## 11 Record plan for /create-injection\n")
w("| Table | Rows | Ids | Notes |\n|---|---|---|---|")
w(f"| slack.slack_messages | 3 (+1 UPDATE parent counters) | {M['S_GUSTO_REPLY']['id']}, {M['S_OLIVER_CURSOR']['id']}, {M['S_ANCHOR']['id']} | ts {M['S_GUSTO_REPLY']['ts']}, {M['S_OLIVER_CURSOR']['ts']}, {M['S_ANCHOR']['ts']}; reply thread_ts 1770933601.686309 |")
nmail = sum(len(M[k]['mailboxes']) for k in M if k.startswith('G_'))
w(f"| gmail.gmail_threads / gmail_messages | {nmail} messages | Robert copies e.g. {G('G_SUNSET1')}; Leonard/Arthur copies of Sunset ×2 and Sherwood | sender tokens PERSON_7731 (Sunset), PERSON_0728 (Sherwood), SVC_77nn new vendors |")
w(f"| linear.linear_projects (+project_teams) | 1 | {M['L_PROJECT']['id']} | team_ENG, lead usr_cc3e90160f490686, created {M['L_PROJECT']['at']} |")
w(f"| linear.linear_issues | 47 | ENG-2438…ENG-2484 | creator Arthur, created 2026-02-12T23:24:13Z… (17 s apart), states Todo |")
w(f"| linear.linear_comments | {sum(len(a['comment_ids']) for a in A)} | cmt_ + 20 hex (`minted_ids.json` L_ISSUES) | authors Arthur, Leonard, Robert, Oliver at their Feb 12–13 times |")
w(f"| trello.trello_cards + actions | 1 + 1 | {M['T_SVB']['id']} | createCard action {M['T_SVB']['create_action']} |")
w(f"| gdrive.drive_files + gdocs.docs_documents | 1 | {M['DOC_CONV']['id']} | parent d_e5caf6a8c630421942ee59, owner Resource token, shared with the three founders |")
w(f"| gdrive.drive_files + gsheets.sheets_spreadsheets | 1 | {M['SHEET_SUBS']['id']} | Arthur's 'Subscriptions' (Feb 10), shared with Leonard and Robert |")
w(f"| gcal.gcal_events | 3 | {', '.join(M['E_REVIEW']['copies'].values())} | ical {M['E_REVIEW']['ical_uid']}, 2026-03-12 17:00–17:45Z |")
w(f"| confluence.confluence_pages (+versions) | 1 + 1 | {M['CONF_UA']['id']} | UA page by user_EMPLOYEE_0008 2025-03-18 (before the Oct 2025 deactivation notice; decoy only) |")
w(f"| github.github_pull_requests / pr_comments | 1 + 1 | {M['GH_PR']['id']}, {M['GH_CR']['id']} | open PR by Oliver Feb 13 09:38Z; CodeRabbit notice 09:41Z |\n")
w("### Integrations and companions\n")
w("| Service | INT id | Companion | Decision |\n|---|---|---|---|")
w("| github | INT-01 | Slack mirror of PR comments | none: Combo-Fighters is not a mirrored repo (INT-01 covers GameOfDominoes, game-of-dominoes-backend, match3d) |")
w("| github | INT-23 | CodeRabbit comment author PERSON_6026_GITHUB_USERNAME + timeline actor SVC_0321 | seeded with the base author token; no review row (review skipped) |")
w("| github | INT-12 | GitHub notification mail per PR | none: Robert is not a Combo-Fighters participant; no mail seeded (integration_exceptions at injection if base_check asks) |")
w("| linear | INT-03 | linear[bot] PR comment | none: no PR names an ENG-24xx key |")
w("| linear | INT-04 | Linear Slack app posts | none: the ENG team posts to no Slack channel in 2026 |")
w("| linear | INT-05 | Linear e-mail digests | none: digests are not seeded for one day of activity |")
w("| gcal | INT-11 | invitation mails | none: no_notify (integration_exceptions) |")
w("| slack | INT-22 | Slack e-mail notifications | none: Robert is active in Slack; no notification mail |")
w("| gmail | none | — | gmail: no integration sources from Gmail; seeded threads get gmail_label_user_counters bumps |")
w("| trello | INT-21 | Trello → Slack | none: no integration exists |")
w("| gdrive | INT-13 | Drive Slack app DMs | none: the doc is shared without a Slack notification |")
w("| confluence | none | — | confluence: no integration; page version row seeded with the page |")
w("| gsheets / gdocs | none | — | gsheets: the decoy sheet and the doc get drive_files rows with the same sharing |\n")

body = "\n".join(L) + "\n"
rs = os.path.join(HERE, 'review_sections.md')
if os.path.exists(rs):
    sec = open(rs).read()
    rt = os.path.join(HERE, 'redteam_section.md')
    subs = {'@@HARDNESS@@': cap('hardness.txt'), '@@GUSTO@@': M['S_GUSTO_REPLY']['locator'], '@@SVB@@': M['T_SVB']['id'],
            '@@SUNSET1@@': G('G_SUNSET1'), '@@SUNSET2@@': G('G_SUNSET2'), '@@FIGMA@@': G('G_FIGMA'), '@@BUDGET@@': str(sum(b['calls'] for b in MAN['call_budget'])),
            '@@REDTEAM@@': open(rt).read() if os.path.exists(rt) else ''}
    for k, v in subs.items():
        sec = sec.replace(k, v)
    body += sec
dst = os.path.join(BUNDLE, 'task_inputs', 'Working_Files', '01_Scenario_Design.md')
open(dst, 'w').write(body)
print('wrote', dst, len(body))
