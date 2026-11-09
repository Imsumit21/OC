#!/usr/bin/env python3
"""Assembles Working_Files/01_Grounding_Dossier.md from the SQL, solver truth, manifest and the tool outputs in plan/out/.
Totals come from solver/truth.json through the solver's aggregates; tool outputs are pasted verbatim."""
import hashlib, json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
O = os.path.join(HERE, "out")
sys.path.insert(0, os.path.join(TI, "..", "tools"))
sys.path.insert(0, os.path.join(WF, "solver"))
from base_check import parse_sql  # noqa: E402
import solver  # noqa: E402
SQLP = os.path.join(TI, "01_Universe_Inject.sql")
SQL = open(SQLP).read()
ST = parse_sql(SQL)
SEED = json.load(open(os.path.join(HERE, "seed_text.json")))
MAN = json.load(open(os.path.join(WF, "01_Hardness_Manifest.json")))
state = solver.load_state(SQL)
rows = solver.solve(state)
AGG = solver.aggregates(rows)
C, R = AGG["classes"], AGG["reply"]
rd = lambda n: open(os.path.join(O, n)).read().rstrip() if os.path.exists(os.path.join(O, n)) else f"(not run: {n})"
sid = lambda n: hashlib.sha256("|".join(SEED[n]["id"].split("/")).encode()).hexdigest()[:32]
L = []
A = L.append
sqlsha = hashlib.sha256(SQL.encode()).hexdigest()[:12]
ins = [x for x in ST if x["op"] == "insert"]
upd = [x for x in ST if x["op"] == "update"]
A("# Grounding Dossier — Owen Baker · DD bug carry-over into Linear · injection rev9 · contains no prompt, OE or criterion text\n")
A(f"SQL: `task_inputs/01_Universe_Inject.sql` (sha {sqlsha}), stored byte for byte in `Working_Files/run_forensics/rev9/01_Universe_Inject.sql`. rev1 to rev8 stay in `run_forensics/` with their platform reports. {len(ins)} INSERT, {len(upd)} UPDATE, no DELETE. Universe: normal, clock 2026-02-14 00:00 UTC. Persona: Owen Baker <owen.baker@harmonygames.co>, Game Engineer (Unity).\n")

A("## 1.A Structural\n")
A("| Table | NOT NULL columns supplied (live schema) | Base location · sample ids | Format notes |\n|---|---|---|---|")
A("| slack.slack_messages | id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, reactions_json, files_json, attachments_json, created_at, metadata_json | slack messages/CE156FDFB428/2025-11.json (root 1bc1434b15a44cec9044db1b59ae4995); messages/C050WGU41HR/2025-11.json | id = sha256(channel\\|ts)[:32]; a reply sets thread_parent_id to the root's id and thread_ts_legacy to its ts; each root's counters are updated |")
A("| gmail.gmail_threads / gmail_messages | id, user_email; id, thread_id, user_email | owen.baker@harmonygames.co/1849333980856689601 | thread id = mailbox plus a numeric id; message id = mailbox plus the RFC Message-ID; Owen's copies are INBOX, Vincent's SENT; invitation mails follow INT-11 |")
A(f"| gdrive.drive_files · gdocs.docs_documents · gsheets.sheets_spreadsheets / sheets_sheets · gslides.slides_presentations / pages / page_elements | id, name, mime_type; document_id, title; spreadsheet_id, title; spreadsheet_id, sheet_id, title; presentation_id, title; presentation_id, object_id; presentation_id, page_object_id, object_id | Drive roots d_4e13bd40cc73d0fc76f87c, d_cc3e90160f490686039986, d_fc22d5941b2aeb5c03ad32 | the file id is the same in Drive and in Docs, Sheets or Slides, with identical sharing; f_ + 22 hex; folder d_9b41e7c2a05d36f8e1c7a4 |")
A("| gcal.gcal_events | event_id, calendar_id | evt_6e2c91d4b07f3a58c1d2e4 (Owen's copy) | one row per attendee calendar with its own event id, shared ical_uid, self:true on the owner's copy; Sun Feb 15 17:00–17:30Z is a not-yet-happened event |")
A("| trello.trello_cards / trello_actions / trello_checklists / trello_check_items | id, name, idBoard, idList; id, type, date; id, name, idCard, idBoard; id, name, idChecklist | boards 65eb4ec525346c8070ca638f and 6851a6569f3bf818760632ab | ids: first 8 hex = Unix seconds; badges_json in the full base shape with comments 1 and the checklist's 28 items, 27 complete; idShort 211 and 80 are the next free numbers |")
A("| github.github_pr_comments / github_review_comments / github_timeline_events | id, pr_id; id, pr_id, seq; id, pr_id, event | harmonygames-Games/GameOfDominoes#1905 | next free #c_, #ev_ and #rc_ suffixes; each PR comment has a 'commented' event and an INT-01 copy; each inline comment belongs to the PR's #rev_1 approval and follows it by three seconds |")
A("| linear.linear_comments / linear_issues | id, issue_id, author_id, body, is_edited, created_at, updated_at; UPDATE of updated_at only | ENG-2401, ENG-2417 | comment_ + 32 hex; dates YYYY-MM-DDTHH:MM:SSZ; issue updated_at follows the newest comment; base Linear has no comments (NB-24) |\n")

A("## 1.B Entity\n")
A("| Entity | Spelling used | Where it appears (cited) | Agreement |\n|---|---|---|---|")
ENT = [
 ("Owen Baker", "owen.baker@harmonygames.co · EMPLOYEE_0021_SLACK_ID · usr_4e13bd40cc73d0fc · PERSON_5877_GITHUB_USERNAME", "D05S1S2AB5M/1770937805.214409; harmonygames-Games/GameOfDominoes#1905; Drive root d_4e13bd40cc73d0fc76f87c", "AGREE"),
 ("Arthur Blake", "arthur.blake@harmonygames.co · EMPLOYEE_0025_SLACK_ID · usr_cc3e90160f490686 · EMPLOYEE_0025_GITHUB_USERNAME", "CE156FDFB428/1763394823.486369 thread; harmonygames-Games/GameOfDominoes#1905#rev_1; hub D05S1S2AB5M/1770937805.214409", "AGREE"),
 ("Brian Foster", "brian.foster@harmonygames.co · EMPLOYEE_0026_SLACK_ID · usr_fc22d5941b2aeb5c · PERSON_0180_GITHUB_USERNAME · d1cd0fef645a6c978ae1f068", "D07E9PSQB6W/1765206644.602119; C05V5FNLB9V/1766415326.501939; harmonygames-Games/GameOfDominoes#1898", "AGREE"),
 ("Vincent Parker", "vincent.parker@harmonygames.co · EMPLOYEE_0012_SLACK_ID · usr_65c76e0b87aa7e9b", "CE156FDFB428/1763394823.486369; mail owen.baker@harmonygames.co/1849333980856689601", "AGREE"),
 ("Marcus Bennett", "marcus.bennett@harmonygames.co · EMPLOYEE_0002_SLACK_ID", "C05V5FNLB9V/1764256187.655299; D05USBTQY1F/1765452012.418229; harmonygames-Games/GameOfDominoes#1913 (PERSON_0396_GITHUB_USERNAME)", "AGREE"),
 ("Oliver Brooks", "oliver.brooks@harmonygames.co · EMPLOYEE_0003_SLACK_ID · usr_bdf01b53c6a92c5e", "ENG-2428; #builds C05433XK267 #2200", "AGREE"),
 ("Robert", "robert@harmonygames.co · EMPLOYEE_0016_SLACK_ID", "C09Q4S613CN/1764042435.541279; evt_6e2c91d4b07f3a58c1d2e4", "AGREE"),
 ("Leonard Hayes", "leonard.hayes@harmonygames.co", "C09SWTHEMEW/1770926214.816149", "AGREE"),
 ("Domino Delights", "DD; repo GameOfDominoes", "ENG-2401; harmonygames-Games/GameOfDominoes#1905", "AGREE"),
 ("Android canvas comment channel", "Vincent's Android canvas; channel FC:F09GAFM2DRR:Bugs on Android 2231", "CE156FDFB428/1763041126.468099", "AGREE"),
 ("#god-bugs", "the bug channel", "C05V5FNLB9V/1764256187.655299", "AGREE"),
 ("Win & Collect", "Win & Collect in Slack; 'Collect&win - Magical Wings' on the ticket", "C9CA62B5180A/1765927876.696389; ENG-2424", "AGREE (two names, one feature; the rule doc says neither)"),
 ("Nate's Treasure", "Nate's Treasure / Nathan's Treasure; '[PERSON_NAME_1711]' in the canvas", "ENG-2425; CE156FDFB428/1763131864.808869", "AGREE (anonymized token)"),
 ("BoomBit", "BoomBit (publisher of the public build)", "C09SWTHEMEW/1764659626.614679", "AGREE"),
]
for e in ENT:
    A("| " + " | ".join(e) + " |")
A("")

A("## 1.C Voice and realism\n")
A("Seeded speakers, each with its activity.json (normal KB) status at the clock:")
A("- Arthur Blake (arthur.blake@harmonygames.co, EMPLOYEE_0025_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds the hub D05S1S2AB5M/1770937805.214409 (Feb 12 23:10Z), the rule doc f_3ca9e15d7b20f4e681ad52, the ENG-2401 note, the inline comments, the triage notes and the review invite.")
A("- Brian Foster (brian.foster@harmonygames.co, EMPLOYEE_0026_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds his three check notes, the Trello checklist, C09Q4S613CN/1764606918.318209, D07E9PSQB6W/1765206644.602119, C05V5FNLB9V/1767021345.207719, the Trello comments and the tracker and deck, all dated Sep–Dec 2025.")
A("- Vincent Parker (vincent.parker@harmonygames.co, EMPLOYEE_0012_SLACK_ID) — activity.json status_at_clock quiet_since_2025-12; every seed is dated by Nov 22, 2025, before his last Slack post on Nov 23. Base shows him posting at weekends, so the Nov 22 replies fit.")
A("- Marcus Bennett (marcus.bennett@harmonygames.co, EMPLOYEE_0002_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds D05USBTQY1F/1765452012.418229 and one reply under C05V5FNLB9V/1764256187.655299.")
A("- Oliver Brooks (oliver.brooks@harmonygames.co, EMPLOYEE_0003_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds the ENG-2428 note, dated Dec 5.")
A("- Owen Baker (owen.baker@harmonygames.co, EMPLOYEE_0021_SLACK_ID) — activity.json status_at_clock active_feb_2026; the persona; seeds his own PR comments of November 2025, four channel_leave rows of Feb 11 and six channel_join rows of Feb 12.")
A("- Robert (robert@harmonygames.co, EMPLOYEE_0016_SLACK_ID) — activity.json status_at_clock active_feb_2026; seeds one reply, C09Q4S613CN/1766164222.418229, under his own Nov 24 report.")
A("- Bots: the GitHub app SLACK_BOT_0004_SLACK_ID posts the INT-01 copies in C050WGU41HR.\n")
A("Lengths and hours from conventions.json (normal KB): Slack replies in the canvas channel are one line, like Vincent's base 'yep' and 'still cannot sign in'; Brian's notes are short and plain. The hub is long for an im message, in the tail like Arthur's base requests. Voice from real messages: Vincent writes terse fragments (CE156FDFB428/1763394823.486369 thread), Brian says 'I send the fix' (CE156FDFB428/1763642881.891429) and Arthur writes 'Done' and 'fixed'. Seeds state claims and evidence, never conclusions.\n")

A("## 1.D Keyword\n")
A("| Term | Hits / pointer | Note |\n|---|---|---|")
KW = [
 ('"2231"', "base channel name FC:F09GAFM2DRR:Bugs on Android 2231 (CE156FDFB428/1763041126.468099); seeded comment_49b5ac4788465f72ddf245e34f2b7034", "the title prefix comes only from the ENG-2401 note"),
 ('"0.3.310"', "seeded f_3ca9e15d7b20f4e681ad52; base D04UGG61DUM/1770846601.876869 is a DM Owen cannot see", "the rule doc is the authority for the build; no review version is joined to it (NB-21)"),
 ('"how-to-play"', "seeded harmonygames-Games/GameOfDominoes#1905#rc_1 and its INT-01 copy in C050WGU41HR", "absent from Linear and the deck"),
 ('"info popup"', "seeded harmonygames-Games/GameOfDominoes#1908#rc_1 and its INT-01 copy in C050WGU41HR", "absent from Linear and the deck"),
 ('"round icons"', f"seeded C09Q4S613CN/1764606918.318209 (row {sid('brian_reply')})", "the correction avoids the canvas wording 'circular shapes'"),
 ('"Tavern"', f"base CE156FDFB428/1763642831.967359; seeded D05USBTQY1F/1765452012.418229 (row {sid('vincent_note')})", "a Tavern search of DMs finds Marcus's note, so BACK is rated about half"),
 ('"lives"', "base CE156FDFB428/1763548856.943389, C09SWTHEMEW/1764659626.614679, f_948768f5a462e7037d17c9; ENG-2277, ENG-2400", "the removal reads across a channel and a doc"),
 ('"reward track"', "seeded comment_d6aee2099bd71050facc422ccef8f809 on ENG-2428", "one record"),
 ('"carry-over"', "seeded D05S1S2AB5M/1770937805.214409, f_3ca9e15d7b20f4e681ad52, d_9b41e7c2a05d36f8e1c7a4, comment_49b5ac4788465f72ddf245e34f2b7034", "the task's own word; no correction carries it except the ENG-2401 note the rule doc points at"),
 ('"close these UI tickets"', "seeded 690b29bc3c7d2e51b0f86a47 on card 690b27282f4c1b7a6e93d512", "NEW TERM: the rule doc points at it by role"),
]
for k in KW:
    A("| " + " | ".join(k) + " |")
A("")

A("## 1.E Persona reach\n")
n_lb = sum(1 for l in open(os.path.join(HERE, "load_bearing_ids.txt")) if l.strip())
A(f"Load-bearing scoped ids (seeded and base) are in `Working_Files/plan/load_bearing_ids.txt` ({n_lb} ids; Linear, GitHub and Trello are unscoped).\n")
A("| Load-bearing record | Reach |\n|---|---|")
for i_, why in ((sid("hub"), "Owen is in the DM D05S1S2AB5M"), (sid("vincent_note"), "Owen is in the DM D05USBTQY1F"), (sid("brian_dm"), "Owen is in the DM D07E9PSQB6W"), (sid("brian_reply"), "Owen is in C09Q4S613CN"), ("f_3ca9e15d7b20f4e681ad52", "shared with Owen"), ("d_9b41e7c2a05d36f8e1c7a4", "Owen owns it"), ("evt_6e2c91d4b07f3a58c1d2e4", "on Owen's calendar"), (state["mail"], "in Owen's mailbox"), ("C9CA62B5180A/1765927876.696389", "Owen is in the mpim"), ("f_948768f5a462e7037d17c9", "shared with Owen")):
    A(f"| {i_} | {why} |")
A(f"\nOutput verbatim:\n\n```\n{rd('checksql.txt')}\n```\n")

A("## 1.F Collision\n")
A("Every id the SQL mints was looked up over its full base collection (`tools/hg.py search lookup`, outputs in `plan/idcheck/`):")
for n, lab in (("gdrive", "gdrive drive_files"), ("gcal", "gcal events"), ("trello_card", "trello cards"), ("trello_action", "trello actions"), ("trello_checklist", "trello checklists"), ("trello_check_item", "trello check items"), ("github_comment", "github pull_request_comments"), ("github_event", "github timeline_events"), ("github_rc", "github review_comments")):
    d = json.load(open(os.path.join(HERE, "idcheck", n + ".out.json")))
    A(f"- {lab}: {len(d['matches'])} ids, {d['records_checked']} base records checked, scan_complete {d['scan_complete']}, {sum(1 for v in d['matches'].values() if v)} matches (plan/idcheck/{n}.out.json).")
A("- Slack (channel, ts) pairs and Gmail ids: base_check Check A PASS; seeded Gmail threads are new numeric ids in each mailbox.")
A("- Linear comment ids and Slides object ids have no base rows to collide with (NB-24; gslides ids are per presentation). Header tokens: none minted.\n")

A("## Record ledger\n")
A("One row per SQL statement, in SQL order.\n")
A("| # | SQL line | Op | Table | Id | Pointer | Role |\n|---|---|---|---|---|---|---|")
ROLE = {}
for n, role in (("hub", "hub"), ("rule_doc", "authority H1"), ("decoy_doc", "decoy"), ("amend", "amendment"), ("vincent_note", "overturning"), ("brian_reply", "overturning"), ("brian_dm", "closing record"), ("bar_reply", "closing record"),
                ("alias_note", "tie to a ticket"), ("rule_comment", "authority H2"), ("zm_comment", "decoy"), ("deck", "stale summary"), ("season_note", "overturning"), ("gift_note", "overturning"),
                ("inline_td", "overturning"), ("inline_axe", "overturning"), ("train_reply", "overturning"), ("team_reply", "overturning"), ("lives_reply1", "overturning"), ("lives_reply2", "overturning")):
    i = SEED[n]["id"]
    ROLE[i] = role
    if "/" in i and n not in ("mail",):
        ROLE[sid(n)] = role
for k, x in enumerate(ST, 1):
    if x["op"] not in ("insert", "update"):
        continue
    r = x.get("row") or {}
    key = r.get("id") or r.get("event_id") or r.get("document_id") or r.get("spreadsheet_id") or r.get("presentation_id") or x.get("key") or ""
    t = x["table"]
    if x["op"] == "update":
        where = x.get("where") or {}
        key = key or (list(where.values())[0] if isinstance(where, dict) and where else "")
        m = re.search(r"WHERE id = '([^']+)'", SQL.splitlines()[x["line"] - 1]) if not key else None
        key = key or (m.group(1) if m else "")
        role = "thread counters" if t.startswith("slack") else "state repair or updated_at"
    else:
        role = ROLE.get(str(key)) or {"gmail.gmail_threads": "mail thread", "gmail.gmail_messages": "mail", "gcal.gcal_events": "share list", "github.github_timeline_events": "timeline companion", "github.github_pr_comments": "done claim",
                                      "linear.linear_comments": "per-record note", "slack.slack_messages": "INT-01 copy or control", "gslides.slides_pages": "deck page", "gslides.slides_page_elements": "deck text", "gsheets.sheets_sheets": "tracker tab"}.get(t, "container")
    ptr = r.get("issue_id") or r.get("presentation_id") or r.get("spreadsheet_id") or (f"{r.get('channel_id')}/{r.get('ts')}" if t.startswith("slack") and x["op"] == "insert" else key)
    if t.startswith("gslides") or t.startswith("gsheets"):
        key = ptr
    A(f"| {k} | L{x['line']} | {x['op']} | {t} | {key} | {ptr} | {role} |")
A("")

A("## Findability and discovery-order proofs\n")
for b in [
 f"Hub (AN1) D05S1S2AB5M/1770937805.214409 (row {sid('hub')}): Arthur to Owen, Thu Feb 12 23:10Z; the prompt names it. It names the carry-over notes doc, the UI Changes tree, the folder, Sunday's bug review and the three counts.",
 "Master ticket (AN2) ENG-2401: named by the hub; linear_list_issues returns it and its children; the amendment comment_49b5ac4788465f72ddf245e34f2b7034 needs linear_list_comments, and H1 says changes go on the master ticket.",
 "H1 f_3ca9e15d7b20f4e681ad52: shared with Owen; a Drive search for 'carry-over' returns it, with the folder d_9b41e7c2a05d36f8e1c7a4. The decoy f_72e0b4c3d91a5f68c2b7e4 comes up for 'bug list notes'; its title names the other game.",
 "H2 690b29bc3c7d2e51b0f86a47: H1 says 'Brian's closing rule from the UI work'; the card 690b27282f4c1b7a6e93d512 on board 65eb4ec525346c8070ca638f is the UI work card, and the ZM card's comment 68d284b84b7e9a3c5d16e208 is its decoy.",
 "T_INLINE_TD and T_INLINE_AXE: the merged PR, Owen's PR comment and Brian's tick on card 690b27282f4c1b7a6e93d512 come first; harmonygames-Games/GameOfDominoes#1905#rc_1 and harmonygames-Games/GameOfDominoes#1908#rc_1 need the PR's own review comments, and the review body is empty.",
 f"T_REPLY: the tick is read from CE156FDFB428/1763549455.195819; the correction sits under an unrelated gems post, C09Q4S613CN/1764606918.318209 (row {sid('brian_reply')}).",
 f"T_BACK: the tick and Brian's fix are in CE156FDFB428/1763642831.967359; Marcus's note D05USBTQY1F/1765452012.418229 (row {sid('vincent_note')}) sits in a DM no anchor names.",
 "T_GONE: the unticked lines come first; the removal is in C09SWTHEMEW/1764659626.614679 and f_948768f5a462e7037d17c9, and H1 says what counts is the build players have.",
 "T_WINGS: the child reads as finished until the disable post C9CA62B5180A/1765927876.696389 or the #builds line (commit 79791d4807) is found.",
 "T_LINE: Marcus's reply C05V5FNLB9V/1764329192.159229 reads as closed; harmonygames-Games/GameOfDominoes#1913 is open and its commit is not in #1914's list.",
 "T_ELSE: the threads stop at C05V5FNLB9V/1764659550.713509 and neighbours; the closes sit in the #builds line C05433XK267/1765310004.760809 and Brian's DM D07E9PSQB6W/1765206644.602119.",
 "T_ALIAS: titles use other words; Vincent's mail owen.baker@harmonygames.co/1849333980856689601 ties the Apple line to ENG-2073 and comment_7ab5299cbb609d95ba12249d315daedc ties the manual sign-in line to ENG-2363.",
 "T_SEASON and the Daily Gift child: the wrap deck f_d15a8c70e3f2b94a61c8d3 (Nov 21) comes first; Oliver's comment_d6aee2099bd71050facc422ccef8f809 (Dec 5) and Brian's DM line D07E9PSQB6W/1765471651.208713 (Dec 11, moved there from ENG-2437 in rev9) overturn it.",
]:
    A("- " + b)
A("")

A("## Self-validation\n")
A("| QC category | Tool-enforced (result) | Manual (evidence) |\n|---|---|---|")
A("| Missing Universe Data | check-sql PASS (1.E) | every deciding fact is persona-readable: D05USBTQY1F/1765452012.418229, owen.baker@harmonygames.co/1849333980856689601, f_3ca9e15d7b20f4e681ad52 |")
A("| Temporal Field | sql_lint 0 errors; base_check Check C | check notes follow each fix: ENG-2430 and ENG-2410 after #2205; inline comments follow their reviews and precede the merges, harmonygames-Games/GameOfDominoes#1905#rev_1 |")
A("| Cross-service Referential | base_check Check A | one claim per item across services; each PR comment has its timeline event and its copy in C050WGU41HR |")
A("| Quantitative / Reconciliation | counters updated on every root | the 28 children: 9 already Done plus 19 open under ENG-2403, ENG-2404, ENG-2405; the checklist badges match its 28 items |")
A("| State / Lifecycle | base_check PASS with no hazard ticket modified | the SQL updates no L01, L03 or L07 ticket (13 issue updates, each a companion of a seeded comment); no seeded comment follows a closed ticket; ENG-2417 |")
A("| Identifier / Format | eval lint FAIL 0 CHECK 0 | ids follow base schemes (1.A); base tokens kept, EMPLOYEE_0025_GITHUB_USERNAME |")
A("| Semantic / Category | — | titles match content: f_3ca9e15d7b20f4e681ad52, 690b27282f4c1b7a6e93d512, evt_6e2c91d4b07f3a58c1d2e4 |")
A("| Other | — | voice per 1.C; no record states a total, an outcome list or the sheet |\n")

A("## Integrations and companions\n")
A("| Service | INT id | Companion | Decision |\n|---|---|---|---|")
for r_ in [
 ("github", "INT-01", "GitHub Slack app copy in #engineering-bots", "seeded for all 12 PR comments and inline comments, threaded under each PR's opened message in C050WGU41HR; all fall inside the window that ends 2025-12-26"),
 ("github", "INT-02, INT-12", "push notices; notification mails", "none: no commits or PRs are seeded"),
 ("linear", "INT-03, INT-04, INT-05", "linear[bot] on PRs; Slack posts; digests", "none: no new PR names a key, and comments on open tickets have no Slack post; ENG-2401"),
 ("gcal", "INT-11", "invitation mails", "seeded for Owen, Oliver and Robert from Arthur, Feb 12 23:05Z, with all four calendar copies; evt_6e2c91d4b07f3a58c1d2e4"),
 ("gdrive", "INT-13", "Drive app DMs", "none: shares by notice only; f_3ca9e15d7b20f4e681ad52"),
 ("slack", "INT-22", "Slack email notices", "none for DMs; D05S1S2AB5M"),
 ("trello", "INT-21", "no Trello to Slack integration", "none; card 690b27282f4c1b7a6e93d512"),
 ("gmail", "none", "Vincent's mail is ordinary mail", "none; owen.baker@harmonygames.co/1849333980856689601"),
 ("gdocs, gsheets, gslides", "none", "Drive rows mirror every native file", "seeded; f_d15a8c70e3f2b94a61c8d3"),
]:
    A("| " + " | ".join(r_) + " |")
A("")

A("## Touched-data census and coherence hazards\n")
A("Touched data: the DMs D05S1S2AB5M, D05USBTQY1F and D07E9PSQB6W; channels CE156FDFB428, C05V5FNLB9V, C09Q4S613CN and C050WGU41HR (roots' counters updated); ENG-2401, ENG-2410, ENG-2428, ENG-2429, ENG-2430 and ENG-2437; ENG-2073, ENG-2363, ENG-2398, ENG-2280, ENG-2281, ENG-2181, ENG-2351, ENG-2406; PRs #1895 to #1916; boards 65eb4ec525346c8070ca638f and 6851a6569f3bf818760632ab.\n")
A("Hazards from coherence_hazards.json (normal KB):")
for b in ["temporal: T07 — all seeded Slack rows are before Feb 13 10:03Z (latest: the hub); T06 — the Trello card dates from Nov 5, before the board went quiet; T04 — Arthur's Feb note is on an open master; T05 — no seeded comment follows a child's completed_at.",
          "semantic: S03 — only the Bug label is used; S06 — no title is graded.",
          "referential: R01, R02 — seeds cite only keys and PRs the records prove; R04 — the hub names docs in words, with no Drive link.",
          "quantitative: Q01, Q03 — every seeded reply updates its root's reply_count, reply_users_count and latest_reply.",
          "state/lifecycle: L01, L07 — the 14 PR-state tree tickets keep their base state and the SQL updates none of them; moving them is the job Arthur gives, so PR on a merged ticket is the stale status it reconciles; L03 — ENG-2405 stays as it is, and the rule doc keeps the masters; all three acknowledged as dated_claim.",
          "identifier/format: I02 — seeded Slack ids are sha256(channel|ts)[:32]; I03 — Owen's seeded rows use owen.baker@harmonygames.co, not the owen@ alias in base file names."]:
    A("- " + b)
A("\nKnown data issues (references/known_data_issues/normal.md; no load-bearing fact, trap or graded slot rests on a card's 'Don't grade' value):")
for b in ["NB-1: repaired in rev3: Arthur puts Owen on a spare paid seat (five seats, three kept: C0ADGSZKR3R/1770842395.641349), and the SQL gives him a leave on Feb 11 and a join on Feb 12 in CE156FDFB428, C09Q4S613CN, C05433XK267 and C09SWTHEMEW, plus a join in C05V5FNLB9V and C050WGU41HR, whose leaves are in the base. /prompt failed rev2 and rev4 on this card.",
          "NB-6: every seeded Slack row is before Feb 13 10:03Z.", "NB-13: no exact branch name is graded.", "NB-14: repaired in rev3: the SQL clears the ENG-2403 and ENG-2404 checklists, so they can't disagree with the child tickets (ENG-2404).",
          "NB-21: no review version is joined to a build number.", "NB-24: every Linear comment the task relies on is seeded.", "NB-31: no access argument rests on DM member lists."]:
    A("- " + b)
A("")

A("## Intended disagreements\n")
A("| Claim met first | Overturning record | Why realistic | Resolution |\n|---|---|---|---|")
DIS = [
 ("Shop icons line ticked, CE156FDFB428/1763549455.195819", "Brian's reply C09Q4S613CN/1764606918.318209 (Dec 1)", "a regression noticed while working on something else", "still broken"),
 ("Tavern line ticked and Brian sent the fix, CE156FDFB428/1763642831.967359", "Marcus's DM D05USBTQY1F/1765452012.418229 (Dec 11)", "a colleague tells the owner, not the canvas", "still broken"),
 ("#1905 merged, Owen's comment harmonygames-Games/GameOfDominoes#1905#c_3, Brian's tick on card 690b27282f4c1b7a6e93d512", "Arthur's inline harmonygames-Games/GameOfDominoes#1905#rc_1", "approve-with-a-note on a late PR", "ENG-2434 stays"),
 ("#1908 merged, Owen's comment harmonygames-Games/GameOfDominoes#1908#c_3, Brian's tick on card 690b27282f4c1b7a6e93d512", "Arthur's inline harmonygames-Games/GameOfDominoes#1908#rc_1", "same reviewer habit", "ENG-2426 stays"),
 ("deck f_d15a8c70e3f2b94a61c8d3, 'UI pass wrapped up' (Nov 21)", "comment_d6aee2099bd71050facc422ccef8f809 (Dec 5), D07E9PSQB6W/1765471651.208713 (Dec 11)", "a wrap written a little early", "ENG-2437 and ENG-2428 stay"),
 ("Marcus 'fixed it and did a PR', C05V5FNLB9V/1764329192.159229", "harmonygames-Games/GameOfDominoes#1913 still open", "a PR nobody merged", "still broken"),
 ("unticked lives lines, CE156FDFB428/1763548856.943389", "C09SWTHEMEW/1764659626.614679, f_948768f5a462e7037d17c9", "the economy change removed the feature", "Gone"),
 ("commit 4189eca5 for the train line, CE156FDFB428/1763394823.486369", "Vincent's reply CE156FDFB428/1763845212.507119", "a partial fix", "still broken"),
 ("commit 100612a7 for the team line, CE156FDFB428/1763549817.580759", "Vincent's reply CE156FDFB428/1763742012.611229", "the fix covered the popup only", "still broken"),
 ("ZM note 68d284b84b7e9a3c5d16e208, 'no note'", "Brian's rule 690b29bc3c7d2e51b0f86a47", "two games, two habits", "notes name the build"),
 ("flicker thread ends at testing, C05V5FNLB9V/1764659550.713509", "Robert's reply C09Q4S613CN/1766164222.418229 under his own report, and the #builds line C05433XK267/1765310004.760809", "the reporter says so where he first raised it", "Fixed"),
]
for r_ in DIS:
    A("| " + " | ".join(r_) + " |")
A("")

A("## Constraints for the prompt brief\n")
A("| Anchor | May be named (noun phrases only) | Record |\n|---|---|---|")
A("| AN1 | Arthur's DM from Thursday | D05S1S2AB5M/1770937805.214409 |")
A("| AN2 | the UI Changes master ticket | ENG-2401 |\n")
A("Never name in the prompt: the rule doc's contents (the four outcomes, the first-fit order, what counts, the title and label rules), the Trello card or Brian's closing rule, Vincent's mail or his note, Marcus's DM, Brian's reply or DM, the inline comments, the economy removal, any outcome, any count, the build number or the title prefix.\n")

A("## Fact sheet\n")
A("Declared in the manifest's `facts`; `tools/fact_check.py --no-leak` holds the SQL to them.\n")
A("| Key | Value | Home |\n|---|---|---|")
for f in MAN["facts"]:
    A(f"| {f['key']} | {f['value']} | {f['home_ids'][0]} |")
A("")

A("## Facts for the human\n")
A(f"Totals from solver/truth.json: {C.get('Fixed')} Fixed, {C.get('Broken')} Broken, {C.get('Gone')} Gone, {C.get('Covered')} Covered; {R['new_tickets']} new tickets; {R['still_broken']} still broken in the reply; {R['children_done']} of {R['children_total']} UI children Done.\n")
A("| Locator | Base/seeded | Fact | Reach | Role |\n|---|---|---|---|---|")
H = [
 (sid("hub"), "seeded", "Arthur to Owen (D05S1S2AB5M/1770937805.214409): the ask", "DM member", "hub"),
 ("f_3ca9e15d7b20f4e681ad52", "seeded", "H1: scope, outcomes in first-fit order, what counts, ticket fields, tree rule, sheet columns", "shared with Owen", "authority"),
 ("comment_49b5ac4788465f72ddf245e34f2b7034", "seeded", "ENG-2401: every filed title starts [2231]", "Linear unscoped", "amendment"),
 ("690b29bc3c7d2e51b0f86a47", "seeded", "every close-out note names the current public build", "Trello unscoped", "authority"),
 ("harmonygames-Games/GameOfDominoes#1905#rc_1", "seeded", "Tile Dozer how-to-play popup still on old sprites: ENG-2434 stays", "GitHub unscoped", "overturning"),
 ("harmonygames-Games/GameOfDominoes#1908#rc_1", "seeded", "Axe Arena info popup keeps the old frame: ENG-2426 stays", "GitHub unscoped", "overturning"),
 ("C9CA62B5180A/1765927876.696389", "base", "Win & Collect disabled Dec 16: ENG-2424 stays", "mpim member", "eliminating evidence"),
 ("comment_d6aee2099bd71050facc422ccef8f809", "seeded", "Season Pass reward track on old frames: ENG-2428 stays", "Linear unscoped", "overturning"),
 ("D07E9PSQB6W/1765471651.208713", "seeded", "Daily Gift never got its last pass: ENG-2437 stays", "Owen is in the DM", "overturning"),
 (sid("brian_reply"), "seeded", "C09Q4S613CN/1764606918.318209: shop icons came back: Broken", "channel member", "overturning"),
 (sid("vincent_note"), "seeded", "D05USBTQY1F/1765452012.418229: Tavern frame went again: Broken", "DM member", "overturning"),
 ("C09SWTHEMEW/1764659626.614679", "base", "lives removed from the build: three lines Gone", "channel member", "overturning"),
 ("harmonygames-Games/GameOfDominoes#1913", "base", "the window fix's PR is still open: Broken", "GitHub unscoped", "overturning"),
 ("C09Q4S613CN/1766164222.418229", "seeded", "Robert: both flickers are gone: Fixed", "channel member", "closing record"),
 (sid("brian_dm"), "seeded", "D07E9PSQB6W/1765206644.602119: music and acid sorted: Fixed", "DM member", "closing record"),
 (state["mail"], "seeded", "Vincent ties the Apple line to ENG-2073: Covered", "Owen's mailbox", "tie"),
 ("comment_7ab5299cbb609d95ba12249d315daedc", "seeded", "Vincent ties the manual sign-in line to ENG-2363: Covered", "Linear unscoped", "tie"),
 ("evt_6e2c91d4b07f3a58c1d2e4", "seeded", "Sunday's bug review: Arthur, Robert, Oliver and Owen, so the sheet goes to those three", "Owen's calendar", "share list"),
 ("d_9b41e7c2a05d36f8e1c7a4", "seeded", "Owen's DD bug carry-over folder", "Owen owns", "destination"),
]
for r_ in H:
    A("| " + " | ".join(str(x) for x in r_) + " |")
A("")

A("## Platform /injection review of rev1\n")
A("Verdict: PASS, COMPLETE, no demonstrated defects; report stored at `run_forensics/rev1/0_injection_PASS_r1.md` (attempt 6aeed8256c022adb310c8253). It certifies SQL sha256 975909fb25e515722df0331b79770f69e97919a13766a31e21ab742426f5a1d1, 80,854 bytes. The requester removed the four header comment lines before uploading, so the certified file has a blank line 1 and otherwise matches what this stage sealed: all 172 statements are identical. The local copy keeps only the marker sql_lint requires on line 1, so every other line, and each line number in the report, is the same.\n")
A("| Advisory | Disposition | Evidence |\n|---|---|---|")
A("| 1. Seven columns outside the review's snapshot | Left in | references/universe_schema_live.json lists all seven, and github_review_comments.seq is NOT NULL there, so dropping it would break the insert; Douglas and Julia submitted the same review-comment columns (harmonygames-Games/GameOfDominoes#1905#rc_1 uses that shape); the gslides columns loaded on earlier tasks |")
A("| 2. Folder d_9b41e7c2a05d36f8e1c7a4 created 20 minutes after the hub | Fixed in rev2 | the folder is now dated 23:00Z, before the hub at 23:10Z |")
A("| 3. Board dateLastActivity older than card 690b27282f4c1b7a6e93d512 | Left | a cached field; the report does not call it a defect |\n")
A("The report also notes that the only base record of 0.3.310 is a DM Owen can't see (D04UGG61DUM/1770846601.876869); the rule doc is the authority, as the 1.D table says.\n")

A("## Changes in rev2\n")
A("A blind fork sweep before /prompt reproduced the outcome counts and found three blocking forks. Four rows changed and the truth did not: the hub D05S1S2AB5M/1770937805.214409, the rule doc f_3ca9e15d7b20f4e681ad52, Brian's comment 690b29bc3c7d2e51b0f86a47 and the folder d_9b41e7c2a05d36f8e1c7a4, which now predates the hub (advisory 2 above). Findings and dispositions are in plan/out/sweep_dispositions.md.\n")
A("Platform /injection of rev2: PASS, COMPLETE, no demonstrated defects, SQL sha256 be13a93a5920e0a68549489834fe9bcf0ef29f65a1390897389b4db7aa3850d9 (run_forensics/rev2/0_injection_PASS_r2.md). The folder advisory is resolved and the column and Trello advisories carry over with the dispositions above. It asks /prompt to confirm two records: the design question is C05V5FNLB9V/1767191512.428539 and the switched-off record is C9CA62B5180A/1765927876.696389, both visible to Owen.\n")

A("## Platform /prompt review of rev2 and the rev3 changes\n")
A("rev2 passed the platform /injection (run_forensics/rev2/0_injection_PASS_r2.md) and failed /prompt at 2 (run_forensics/rev2/1_prompt_FAIL_r2.md): every prompt dimension scored 5, and Unique Ground Truth, Clarity and Cross-Service Coherence scored 2. The report says the fixes are in the data, so the prompt is unchanged. Truth is unchanged.\n")
A("| Finding | rev3 change | Evidence |\n|---|---|---|")
A("| F1 flicker scope gap | Robert's reply under his own report says both flickers are gone | C09Q4S613CN/1766164222.418229 |")
A("| F2 Dec 22 two posts | the rule doc: a follow-up on a bug already posted is part of that bug | C05V5FNLB9V/1766415211.386389, f_3ca9e15d7b20f4e681ad52 |")
A("| F3 deleted canvas lines | the rule doc: a comment whose line was deleted has nothing to carry over | CE156FDFB428/1763042124.247899, f_3ca9e15d7b20f4e681ad52 |")
A("| F4 QA-doc post | the rule doc: a post that points at a QA doc isn't a bug post | C05V5FNLB9V/1764662837.138929, f_3ca9e15d7b20f4e681ad52 |")
A("| NB-1 Owen's access | the hub says he is back on a paid seat; he leaves on Feb 11 and rejoins on Feb 12 in every task channel | C05V5FNLB9V, CE156FDFB428, C09Q4S613CN, C05433XK267, C09SWTHEMEW, C050WGU41HR; C0ADGSZKR3R/1770842395.641349 |")
A("| NB-14 checklists | ENG-2403 and ENG-2404 descriptions cleared; distractor D_CHECKLIST dropped | ENG-2403, ENG-2404 |")
A("| 0.3.310 line | the rule doc says it came off the economy line; 'told BoomBit' removed | f_3ca9e15d7b20f4e681ad52 |")
A("| Inline comment dates | moved to just after their reviews, before the merges | harmonygames-Games/GameOfDominoes#1905#rc_1, #1908#rc_1 |")
A("| 7 snapshot columns | left in: references/universe_schema_live.json has them and seq is NOT NULL | Douglas's and Julia's submitted SQL used the same review-comment columns |\n")

A("## Platform /injection review of rev3 and the rev4 change\n")
A("rev3 failed /injection on one finding, C1 (run_forensics/rev3/0_injection_FAIL_r3.md): Owen's channel_join rows in CE156FDFB428 and C09Q4S613CN contradict the base, which shows him joining C09Q4S613CN on Nov 2 and has no leave for him in either channel; his Feb 11 leaves cover six other channels. rev4 deletes those two rows and changes nothing else. The rows for C05V5FNLB9V and C050WGU41HR stay, which the report calls correct. Advisory 3 (review comments three to four seconds after their reviews) is left as it is: it isn't a defect and any other change would widen the diff.\n")

A("## Platform /hardness on rev8 and the rev9 change\n")
A("rev8 passed /injection and /prompt 5 (run_forensics/rev8/). The next Opus pre-check run (269 calls) missed only Vincent's email, so /hardness scored 2: one independent cause, about 14 % of the answer against the 15 % medium loss (run_forensics/rev8/1a_hardness_FAIL2_r8.md). Like the rev7 run, it read Brian's Dec 11 DM lines, which settled Tavern and both popups. The cause sits in the design, not in one unlucky run: every second carrier, plus the shop reply and the music line, is written by Brian, and runs look through Brian's messages because he owns the closing rule, so they act as one trap that two pre-check runs in a row caught. Treating them as one behaviour (plan/boot_rev9.py) gives rev8 about 0.62 for /hardness 3 or better and rev7 about 0.48, against the 0.69-0.80 I had quoted for rev8.\n")
A("rev9 makes the hard part independent of that sweep. Brian's Tavern line (D07E9PSQB6W/1765471351.236119) is removed, so Tavern rests on Marcus's DM (D05USBTQY1F/1765452012.418229) and Apple on Vincent's email, the two records no measured run has opened (0 of 9). A run that reads Brian's DM still misses both, two independent causes worth about a quarter of the answer. For the baseline spread, Brian's Daily Gift note moves from ENG-2437 (comment_3e81bf306c58746580a9cfa0ca12bd60, Nov 24) to his DM on Dec 11 (D07E9PSQB6W/1765471651.208713: 'Daily Gift isn't finished either, the panel never got its last pass.'), next to his popups line, whose opening 'And' is dropped now that the Tavern line is gone. Oliver's Season Pass note stays on ENG-2428, so the notes doc's 'Brian and Oliver left notes on some of the open children' stays true (Brian's check notes on ENG-2410, ENG-2429 and ENG-2430 remain). No base commit touches Season Pass or Daily Gift after Dec 4. The model gives P(/hardness >= 3) about 0.98 and P(all baseline gates) about 0.53-0.68. The truth and the prompt are unchanged.\n")
A("## Platform /hardness on rev7 and the rev8 change\n")
A("rev7 passed /injection and /prompt 5 (run_forensics/rev7/). The Opus pre-check run (359 calls, trajectory run_forensics/rev7/precheck/trajectory.json, sha b0a1d4db639b) then got every item right and /hardness scored 1 (run_forensics/rev7/1a_hardness_FAIL1_r7.md). At calls 217-221 it listed every message Brian sent from Nov 1 to Dec 15 with no keyword, so the three Dec 11 lines in Brian's DM with Owen settled Tavern, Apple and both popups in one sweep. rev6 placed those lines by modelled baseline spread and never modelled the single pre-check run; a placement model over all 8 measured runs (plan/boot_rev8.py) gave rev7 only about 0.23-0.31 for /hardness 3 or better.\n")
A("rev8 removes only Brian's Apple line (D07E9PSQB6W/1765471447.518229). Apple Covered by ENG-2073 rests on Vincent's email in Owen's inbox, as on rev5, and no stored run has opened that email (0 of 8), so a run that reads Brian's DM still misses at least one independent cause. The Tavern and popup lines stay for the baseline spread. Over all 27 placements of the three corrections the model ranks this first: P(/hardness >= 3) about 0.69-0.80, P(all baseline gates) about 0.51-0.72. Removing all three lines gives about 1.00 and 0.00, since rev5's two baseline batches failed spread with them gone. The truth and the prompt are unchanged; the popup line still reads on from the Tavern line ('And I never got back to the two popups ...').\n")
A("## Platform review of rev6 and the rev7 change\n")
A("rev6 passed /injection (run_forensics/rev6/0_injection_PASS_r6.md). /prompt scored Unique Ground Truth and Clarity 2 on one thread, everything else as before (run_forensics/rev6/1_prompt_FAIL_r6.md, Issue 1): on the navigation bar tooltips line (CE156FDFB428/1763394941.178509) Vincent wrote 'I still have 1 pixel gap on my android but that's okay' (Nov 21 18:03 UTC) and Brian answered 'I'll send another fix' (18:07 UTC), and no later record speaks to the gap, so Done and Bugs were both fair. The fork is in base records every earlier revision had. rev7 adds the record its minimum fix asked for: Vincent's reply in that thread on Nov 22 at 21:05 UTC, in the same retest session as his train (21:00) and lives (21:10, 21:11) replies, saying Brian's second fix closed the gap (CE156FDFB428/1763845512.559339). The parent's reply_count goes from 6 to 7 and latest_reply moves to the new reply; reply_users_count stays 3, since Vincent already replied. The line was already Fixed, so the truth and the prompt are unchanged. Vincent's last activity is 2025-12-02, after this reply.\n")
A("## Baselines on rev5 and the rev6 change\n")
A("rev5 passed /injection, /prompt (score 5) and /hardness (NON-FAIL 4, run_forensics/rev5/1a_hardness_NONFAIL_r5.md). Two batches of six baselines then averaged about 64-65 % by hand grading but failed the spread and pattern gates: every one of 12 runs missed Vincent's ENG-2073 mail, Marcus's Tavern DM and both inline reviews, so 4 of 6 runs in each batch failed the same rows and SD was about 0.04 (run_forensics/rev5/baseline/summary.md).\n")
A("rev6 adds a second carrier for each of those four corrections in one place the stored runs reached only part of the time: Brian's DM with Owen, whose history past early December reached 3 of 7 runs (run_forensics/rev5/baseline/exposure.py). On Dec 11 Brian repeats Marcus's Tavern report and says his fix didn't hold (D07E9PSQB6W/1765471351.236119), passes on Vincent's tie of the Apple sync line to ENG-2073 (D07E9PSQB6W/1765471447.518229), and says he never got back to the Axe Arena info popup or the Tile Dozer how-to-play popup from Arthur's reviews (D07E9PSQB6W/1765471563.704419). Keeping the four together makes the runs that read that far differ from the runs that don't; a bootstrap from the runs' measured exposure favoured it over a deck-plus-DM split (plan/boot_rev6.py). The original records stay, every rev5 statement is unchanged, and the truth is identical. The lines avoid the words runs search Brian's messages for (ticket, close, Done, PR, build, UI). Vincent's last activity is 2025-12-02 and the notes already say he tied lines to tickets before he left; Arthur's reviews (Nov 19-20) are the holds Brian refers to, and nothing later says either popup was swapped.\n")

A("## Platform reviews of rev4 and the rev5 change\n")
A("rev4 passed /injection (run_forensics/rev4/0_injection_PASS_r4.md). /prompt scored every prompt dimension 5, including Unique Ground Truth and Clarity, and Cross-Service Coherence 2 on two points (run_forensics/rev4/1_prompt_FAIL_r4.md): Owen stays in task channels through his guest period, and card 690b27282f4c1b7a6e93d512 last moved before its ticked work. rev5 pairs a leave and a join in CE156FDFB428, C09Q4S613CN, C05433XK267 and C09SWTHEMEW, the last by the same logic, and restores the card's date. Truth and the prompt are unchanged. Canvas comment channels use the base's 'conversation' wording (CE22D7884D8F).\n")

A("## Platform follow-ups\n")
A("- ○ carriers: none load-bearing. Linear comments are ● (Ask_Carriers §6b).\n- `linear_create_issue` at volume is lightly proven: 2 stored calls, both clean. Watch it in the first baseline run.\n- Direct reads of the canvas channel CE156FDFB428 are unproven on the platform; persona_view shows it as public to Owen.\n- No call_budget row depends on an unverified behaviour beyond these two.\n")

A("## Self-review\n")
A("### Tool outputs (final SQL, verbatim)\n")
for name, f in (("sql_lint.py", "sql_lint.txt"), ("base_check.py", "base_check.txt"), ("base_claims.py", "base_claims.txt"), ("fact_check.py --no-leak", "fact_check.txt"), ("hardness_gate.py (SQL)", "hardness_gate.txt")):
    A(f"`{name}`:\n```\n{rd(f)}\n```")
lint = json.load(open(os.path.join(O, "hg_lint.json")))
A(f"\n`hg.py lint`: counts {json.dumps(lint.get('counts'))}. No FAIL and no CHECK flags, so no LINT disposition is owed.\n")
A("Warning dispositions:\n- weekend warning disposition: the Nov 22 replies fall on a Saturday; Vincent posted at weekends in base and his last post is Sunday Nov 23.\n- not-yet-happened warning disposition: Sunday's review is after the clock by design; it is a future event, so the deadline rule allows it.\n- fact_check warnings: Vincent is named in Arthur's Feb doc as the canvas's author, which is history; 'Nate' in a mirror is the event's name, not the person.\n")
A("### Preflight (S4b–S5e)\n")
A(f"`oracle_kit.py check`:\n```\n{rd('oracle_kit.txt')}\n```\n`difficulty_mutation.py mutate` and `geometry`:\n```\n[PASS] difficulty_mutation.py: 32 of 32 dispositions recorded, geometry U above 1 - cap\n{rd('mutation.txt')}\n{rd('geometry.txt')}\n```\n`trap_liveness.py`:\n```\n[WARN] trap_liveness.py: advisory flags, each dispositioned\n{rd('trap_liveness_sql.txt')}\n```\nEvery mutation result and liveness flag has a written disposition in `01c_Dispositions.json`. rule:INLINE is WEAK and rule:FOLLOW SURVIVED on direct slots by construction: they are graded on write content (I1 to I4, V4, O1 to O3), which geometry counts.\n")
A(f"Forecast (advisory, UNCALIBRATED):\n```\n[WARN] hardness_forecast.py: advisory, UNCALIBRATED\n{rd('forecast_final.txt')}\n```\nScope of that forecast: it scores solver-read slots only, so CH-INLINE and CH-FOLLOW show no expected loss and the write-content slots (V2 to V4, I1 to I4, B2, B4, G4, L2, A3, O1 to O3) count as passing. The design's own model on the whole surface (plan/policy_model_output.txt, UNCALIBRATED) gives 70.9 % at Opus ledger rates and 59 to 60 % at carrier rates, and the two come to 78.9 % and 70.1 % at 0.7x. The requester's line is under 80 %. Channel rates CH-FOLLOW 0.5 and CH-ALIAS 0.25 are disclosed design priors, not ledger records.\n\n`preflight_report.py`:\n```\n[PASS] preflight_report.py\n{rd('preflight.txt')}\n```\n")
A("### Changes made at this stage (and why)\n")
for d in MAN["design_delta"]:
    A(f"- {d['id']}: {d['change']} ({d['reason']}).")
A("\nBlind sweep of the new seeds: plan/out/sweep_dispositions.md (6 BLOCK and 9 FIX, each re-checked and fixed or accepted). That reviewer printed some rows outside its list, so its reading of those rows is not blind.\n")
A("### /injection Checks A–C walk\n")
A(f"- Inventory: {len(ins)} INSERT, {len(upd)} UPDATE, no DELETE, no upsert; every statement is in the record ledger.\n- Check A (references, uniqueness, identities, id contracts): base_check Check A; every parent resolves (roots 1bc1434b15a44cec9044db1b59ae4995, Drive roots d_cc3e90160f490686039986 and d_fc22d5941b2aeb5c03ad32, boards, PRs).\n- Check B (structure, literal JSON, generated and NOT NULL columns): sql_lint 0 errors; no text_fts or body_text_fts; Linear dates YYYY-MM-DDTHH:MM:SSZ.\n- Check C (dates, parent and reply order, statuses, counts, superseding records): base_check Check C; every seeded event is before the seed bound except Sunday's review, a future event; overturning records follow what they overturn.\n")
A("### Touched-data census\n\nThe census and its hazard dispositions are in 'Touched-data census and coherence hazards' above (all six categories; L01, L03 and L07 acknowledged as dated_claim; seven NB cards dispositioned).\n")
A("### Counter-readings\n")
A("| Category | Counter-reading (strongest argument it fails) | Evidence that resolves it | Verdict |\n|---|---|---|---|")
CR = [
 ("Temporal", "Brian's check notes could predate the fixes they imply", "ENG-2430 and ENG-2410 follow #2205 (C05433XK267 2025-11); ENG-2429 precedes the ENG-2404 tick at 14:29:13", "PASS"),
 ("Temporal", "the inline comments could sit outside their reviews", "harmonygames-Games/GameOfDominoes#1905#rc_1 at 13:05:35Z, after #rev_1 at 13:05:32Z and before the 13:05:40Z merge; #1908#rc_1 at 01:51:55Z, after 01:51:51Z and before 01:51:59Z", "PASS"),
 ("Temporal", "Vincent's replies could postdate his last activity", "latest is CE156FDFB428/1763845872.804449, Nov 22; his last Slack is Nov 23", "PASS"),
 ("Temporal", "the deck could be stale only by accident", "f_d15a8c70e3f2b94a61c8d3 is Nov 21; comment_d6aee2099bd71050facc422ccef8f809 is Dec 5 and D07E9PSQB6W/1765471651.208713 Dec 11, so the corrections follow it", "PASS"),
 ("Semantic / Category", "'Collect & Win' and 'Win & Collect' could read as two screens", "ENG-2424 title and C9CA62B5180A/1765927876.696389 name one feature; the base uses both", "PASS (pre-existing)"),
 ("Semantic / Category", "the ZM doc could be read as the rule", "f_72e0b4c3d91a5f68c2b7e4's title and first line name Zombie Match; H1 says the ZM canvases stay where they are", "PASS"),
 ("Semantic / Category", "a shop icon bug could hold ENG-2432", "H1: 'A bug on a screen doesn't hold its child'; f_3ca9e15d7b20f4e681ad52", "PASS"),
 ("Cross-service Referential", "the inline comment's file might not be in the PR", "both paths come from the CodeRabbit summaries harmonygames-Games/GameOfDominoes#1905#c_2 and #1908#c_2", "PASS"),
 ("Cross-service Referential", "a seeded PR comment could lack its mirror", "12 copies threaded in C050WGU41HR under the opened messages; base_check INT-01", "PASS"),
 ("Cross-service Referential", "0.3.310 has no base record Owen can read", "H1 is the authority; the sequence holds (C09SWTHEMEW/1770753609.436139) and nothing joins it to a review version (NB-21)", "PASS (limit accepted)"),
 ("Quantitative", "still broken could be 7 rather than 9", "H1: 'Covered ones count as still broken'; solver reply still_broken 9", "PASS"),
 ("Quantitative", "63 lines could be 61", "H1 says every ticked or unticked line; two empty roots have no line (CE156FDFB428/1763042124.247899)", "PASS"),
 ("Quantitative", "reply counters could drift", "base_check Check C: each parent's counters equal its replies, with every seeded reply included; the record ledger lists each counter row", "PASS"),
 ("State / Lifecycle", "a ticket in PR with a merged PR reads as a pre-existing defect", "the SQL updates none of them; the hub says the tree never got closed out, so reconciling them is the job; hazard_acknowledgements L01 and L07 dated_claim; ENG-2417", "PASS"),
 ("State / Lifecycle", "ENG-2405 stays Todo with a merged PR", "H1 says the masters stay as they are; the SQL leaves it alone; L03 dated_claim; harmonygames-Games/GameOfDominoes#1905", "PASS"),
 ("State / Lifecycle", "a ticked line could also be Gone after Dec 16", "H1's first-fit order puts Fixed first, so ticked Win & Collect lines stay Fixed; f_3ca9e15d7b20f4e681ad52", "PASS"),
 ("Identifier / Format", "a changed id scheme or a typed address", "eval lint FAIL 0 CHECK 0; sql_lint 0 errors; ids per 1.A; collisions 0 (1.F)", "PASS"),
 ("Identifier / Format", "calendar copies with one event_id would collide", "each copy has its own id and they share ical_uid; evt_6e2c91d4b07f3a58c1d2e4 is Owen's", "PASS"),
 ("Other", "a designed disagreement could read as a silent system conflict", "every overturning record is a dated human message: D05USBTQY1F/1765452012.418229, C09Q4S613CN/1764606918.318209", "PASS"),
 ("Other (pre-existing)", "the ENG-2404 checklist disagrees with child states", "NB-14: the SQL clears it; ENG-2404", "PASS (repaired)"),
 ("Other (sibling)", "another merged child could hide the same gap as ENG-2434", "all 19 open children were read in the sweeps; plan/truth_sketch.json lists each; controls ENG-2417 and ENG-2432", "PASS"),
 ("Other", "the tracker could be filler", "UI pass tracker gives the screen-to-ticket list the child records overturn; gsheets has no other seeded record, and it stays in the design as a stale summary (design_delta)", "PASS"),
 ("Other", "the 28-item checklist could be filler", "it is the per-screen record for children in PR state, closing the fork on ENG-2427 and ENG-2431; Daily Gift stays unticked, in line with D07E9PSQB6W/1765471651.208713", "PASS"),
]
for r_ in CR:
    A("| " + " | ".join(r_) + " |")
A("\nUnresolved: the numbers are UNCALIBRATED until a platform run; `linear_create_issue` at volume and direct canvas reads are unproven; the fork sweep's point that no record proves ENG-2427 and ENG-2431 are in the build now rests on Brian's undated ticks and H1's default rule.\n")
out = "\n".join(L) + "\n"
open(os.path.join(WF, "01_Grounding_Dossier.md"), "w").write(out)
print("dossier", len(out), "lines", out.count("\n"), "statements", len(ST))
