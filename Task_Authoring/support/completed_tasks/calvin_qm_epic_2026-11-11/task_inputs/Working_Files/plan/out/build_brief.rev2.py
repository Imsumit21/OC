#!/usr/bin/env python3
"""Assembles Working_Files/04_Prompt_Writing_Brief.md (brief mode) from the dossier facts, solver/truth.json and the
persona_view search outputs in plan/out/brief/. Facts only; no prompt wording."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TD = os.path.dirname(WF)
sys.path.insert(0, HERE)
import reports as RP
SEED = json.load(open(os.path.join(HERE, "seed_text.json")))
TRUTH = json.load(open(os.path.join(WF, "solver", "truth.json")))
SQL = open(os.path.join(TD, "01_Universe_Inject.sql")).read()
sid = lambda k: SEED[k]["id"]
HUB, NOTE, SHEET, LEG, RULE, DD = sid("hub"), sid("epic_note"), sid("sheet"), sid("legend"), sid("rule_doc"), sid("dd_doc")
CARD, CARDUPD, INV1, INV2, EVT = sid("rev_card"), sid("rev_card_update"), sid("invite_v1"), sid("invite_v2"), sid("event")
IN1, IN2, REOPEN, BACK, ELSE, FILT = sid("inline"), sid("inline2"), sid("reopen"), sid("back"), sid("else_pr"), sid("filt_dm")
AG, AS, DECK, FOLDER, OLD = sid("alias_gift"), sid("alias_streak"), sid("deck"), sid("folder"), sid("gate_old")
NOTEZ = NOTE + " on ZOM-543"
PEOPLE = "brian.foster@harmonygames.co, leonard.hayes@harmonygames.co, arthur.blake@harmonygames.co, julia.lawson@harmonygames.co, vincent.parker@harmonygames.co"

def table(head, rows):
    out = ["| " + " | ".join(head) + " |", "|" + "---|" * len(head)]
    for r in rows:
        out.append("| " + " | ".join(str(c).replace("|", "/").replace("\n", " ") for c in r) + " |")
    return "\n".join(out)

reps = [v for v in TRUTH.values() if "report" in v.get("groups", [])]
assert len(reps) == 39, len(reps)
cnt = lambda s: sum(r["Status"] == s for r in reps)
NP, NQ, NF = cnt("Passed"), cnt("Waiting on QA"), cnt("Waiting on a fix")
NREV = sum(r["Review list"] == "Yes" for r in reps)
NEW = [r for r in reps if not r["Ticket"]]; OLDT = [r for r in reps if r["Ticket"]]
CHG = [r for r in OLDT if r["Ticket state"] != r["Ticket state as found"]]
areas = []
for a in RP.AREAS:
    rs = [r for r in reps if r["Area"] == a]; op = sum(r["Status"] != "Passed" for r in rs)
    areas.append((a, len(rs), op, "Clear" if op == 0 else "Open"))
NCLEAR = sum(a[3] == "Clear" for a in areas)
assert (NP, NQ, NF, NCLEAR, NREV, len(NEW), len(OLDT), len(CHG)) == (12, 6, 21, 1, 6, 19, 20, 3)
rownum = {r[2]: r[0] for r in RP.R}

L = []
A = L.append
A("# Prompt Brief — calvin_qm_epic · prep")
A("> Built 2026-11-10 from 00_Assigments.md, Working_Files/00_Task_Context.json, 01_Grounding_Dossier.md (injection rev2, sha256 ee46405a157d, built after the platform /hardness FAIL 2 on rev1; rev1 passed the platform /injection and /prompt, rev2 has not been reviewed there yet), 01_Scenario_Design.md, 01_Hardness_Manifest.json, solver/truth.json, 03_Error_Async_Config.txt (Friction: none) · Persona view verified: all (check-sql PASS, §5a)")
A("> 04_Prompt.txt may be drafted by Claude or Codex (`/create-prompt-writing draft`) or written by the human. No 02_Reference_Files: the scenario needs no attachment.")
A("> Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)\n")

A("## 1 · Assignment fit\n")
A(table(["Axis", "Assigned value", "What it requires here (cited)"], [
 ["Business function", "Engineering", "Engineering & Live-Ops in `Evals/references/rules/task_categories.md` (engineering delivery, releases, incidents, live game operations): the ZM home screen queue manager and the QA reports against it."],
 ["Persona", "Calvin Price · calvin.price@harmonygames.co · Game Engineer (Unity VFX) (roster.json persona_key calvin_price, department Engineering)", "Voice: a working engineer writing to his assistant, first person, short and plain; judged against the role only. Remit: he is the assignee of ZOM-543 (Queue Manager, In Progress), opened harmonygames-Games/match3d#465 and #472, Brian asked him to take the queue manager on (D0770ET6WBW/1758730948.999939) and QA reports to him directly (D06UPGF5PQV/1758806199.381319). Read scope: his DMs D0770ET6WBW (Brian), D06UPGF5PQV (Vincent), D05U73FNDDL (Marcus), D05HYDTG5TJ (Julia), channels C08R27X0EAH (#zombie-bugs), C0880U9751A (#zombie-match3d), C093LEZGF6J (#zombie-prs), C05433XK267 (#builds), his mailbox, calendar and Drive."],
 ["Competency", "Engineering Ops", "Epic and task management: one ticket becomes an epic with a child per area, every QA report gets its line under the right child, and ticket states are brought in line. Brian asks him because the ticket is his (hub " + HUB + ")."],
 ["Task skill", "Analysis and synthesis", "Exercised by deciding the status of 39 reports from the pass sheet, build posts, PR reviews and later chat reports, and by the stock-take sheet, the slide and the five numbers that sum it up. Retrieval and the Linear writes stack under it."],
 ["Task type", "long-horizon (Long Horizon; difficulty mode hard, V3 cap < 70 %; requester targets: average < 60 %, > 130 counted calls per run, largest failure pattern < 50 %)", "Services carrying weight: Linear (ZOM-543, 20 existing tickets, 27 notes, about 70 writes), Sheets (38 rows of " + SHEET + "), Slack (4 DMs, 4 channels, 15 build posts), GitHub (4 PRs, 2 review comments, 1 PR comment), Docs (legend, rule doc, decoy), Trello (the review card and its 4 actions), Gmail (2 invitations, 2 review mails), Calendar (1 event, 6 attendees), Drive (folder, shares), Slides (deck). Call budget floor 180 (01_Hardness_Manifest.json); the prompt states no count."],
]))

A("\n## 2 · Situation\n")
A(table(["Symptom", "Seen by", "Where it shows (locator)", "Relevant records the persona cannot see"], [
 ["The queue manager is one ticket while QA's home screen flow pass lives in a sheet of its own; Brian wants it turned into a real epic before Thursday's flow review.", "Calvin (DM recipient)", HUB, "—"],
 ["Brian left a note on the ticket saying how he wants the epic.", "Calvin (Linear, unscoped)", NOTE + " on ZOM-543", "—"],
 ["Vincent's flow pass sheet has 38 rows with tickets, fixes and re-tests as he knew them.", "Calvin (sheet shared with him)", SHEET, "—"],
 ["Brian also wants a stock-take sheet in Calvin's folder, shared with the review's people, one slide in Calvin's deck and five numbers back in the DM.", "Calvin", FOLDER + "; " + DECK + "; " + EVT, "the other attendees' calendar copies and invitation mails (not needed: Calvin's own copy " + EVT + " lists every attendee)"],
]))

A("\n## 3 · Investigation → action\n")
A("Questions to resolve (no answers here):")
for q in ["How does Brian want the epic laid out, and which areas get a child?",
          "Which reports are in the list, and which things stay out of it?",
          "What does each re-test code in the pass sheet mean, and on which build was each re-test done?",
          "Which builds count for a QA pass on this game?",
          "Did anyone say later that something came back, and on which build?",
          "For each report that is not passed, is its fix really merged?",
          "Does a ticket already hold the report, perhaps under another name?",
          "Does each ticket's state match where its report stands?",
          "Which areas does the review cover now, and who is on it?",
          "Where do the stock-take sheet and the slide go?"]:
    A("- " + q)
A("\nWrites those answers feed: ten child issues under the epic, a sub-issue for every report with no ticket, a move, a note and where needed a state change on every existing ticket, the stock-take sheet and its sharing, one slide, and the reply to Brian. Every write depends on the investigation.")

A("\n## 4 · Pinned final state (UGT anchor)\n")
A(table(["Deliverable", "Required contents", "Destination", "Recipients", "Catalog write", "Fed by"], [
 ["Area children", "one child per area named in Brian's note " + NOTE + ", state by whether the area is clear", "Linear team ZOM, parent ZOM-543", "—", "linear_create_issue", "the areas and each area's reports"],
 ["New sub-issues", "one per report no ticket holds, title the report, state by status, no priority, no assignee (" + NOTE + ")", "under the area's child of ZOM-543", "—", "linear_create_issue", "status of each report; ticket lookup"],
 ["Existing tickets", "moved under the area's child, a note with the status and why, state changed where it does not match (" + NOTE + ")", "ZOM-556, ZOM-560, ZOM-567 to ZOM-584", "—", "linear_update_issue, linear_create_comment", "status of each report; ticket lookup"],
 ["Stock-take sheet", "tab Reports (Report, Area, Status, Ticket, Review list, Why) and tab Areas (Area, Status, Open reports), per " + NOTE, "Calvin's folder " + FOLDER, PEOPLE + " (attendees of " + EVT + ")", "gsheets_create_spreadsheet, gsheets_batch_update, gsheets_values_update, gdrive_move_file, gdrive_share_file", "every status"],
 ["Slide", "the five numbers", "Calvin's deck " + DECK, "—", "gslides_batch_update", "the five counts"],
 ["Reply to Brian", "reports passed, waiting on QA, waiting on a fix, areas clear, reports on the review list", "Brian's DM D0770ET6WBW (hub " + HUB + ")", "brian.foster@harmonygames.co", "slack_send_message", "the five counts"],
]))
A("\nAlternatives a careful run could defend are settled or accepted in §4b. The forks two blind sweeps found, and how each was closed, are in plan/sweeps/fork_sweep_inj.md and the dossier's Self-review; the design's two-reading table (01_Scenario_Design.md §10) lists the record that settles each one.")

A("\n### 4b · Canonical outcome (all fair outcomes)\n")
A(table(["Deliverable", "Field", "Fixed value (or closed accepted set, with sources)", "Delegated by (quoted span, or —)", "Allowed equivalence class", "Material / representational", "Source"], [
 ["Area children", "count and names", "10: " + ", ".join(RP.AREAS), "—", "title is the area name; a prefix such as 'Queue Manager:' is fine", "material (areas) / representational (prefix)", NOTEZ],
 ["Area children", "team, parent, assignee", "ZOM, ZOM-543, none", "—", "—", "material", NOTEZ],
 ["Area children", "state", "Done for Zombie Lane; Todo for the other nine", "—", "—", "material", NOTEZ],
 ["Reports", "population", "39: the 38 rows of the pass sheet plus the pass icon glow Marcus reported", "—", "—", "material", SHEET + "; " + FILT],
 ["Reports", "status", f"{NP} Passed, {NQ} Waiting on QA, {NF} Waiting on a fix; per report in the table below", "—", "—", "material", NOTEZ + "; " + RULE],
 ["New sub-issues", "count and parent", f"{len(NEW)}, each under its area's child", "—", "—", "material", NOTEZ],
 ["New sub-issues", "title", "the report as the pass sheet words it; for Marcus's report, wording that names the pass icon glow staying on", "note: 'make a sub-issue under the child with the report as the title'", "case and end punctuation free; Marcus's line may be reworded", "material (which report) / representational (wording)", NOTEZ + "; " + FILT],
 ["New sub-issues", "state", "Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix", "—", "—", "material", NOTEZ],
 ["New sub-issues", "priority and assignee", "none", "—", "—", "material", NOTEZ],
 ["Existing tickets", "which", f"{len(OLDT)}: ZOM-567 to ZOM-584, plus ZOM-556 for the day counter row and ZOM-560 for the freezer row", "—", "—", "material", AG + "; " + AS],
 ["Existing tickets", "parent", "the child of the report's area", "—", "—", "material", NOTEZ],
 ["Existing tickets", "state", "ZOM-571 to Todo, ZOM-581 to Todo, ZOM-572 to In Validation; the other 17 keep their state", "—", "—", "material", IN1 + "; " + IN2 + "; " + ELSE],
 ["Existing tickets", "note", "one on each of the 20, giving the status and why", "note: 'leave a note with the status and why'", "wording free", "material (presence, status) / representational (wording)", NOTEZ],
 ["Existing tickets", "priority and assignee", "left as found", "—", "—", "representational", NOTEZ],
 ["Sheet", "location", "in " + FOLDER, "—", "—", "material", HUB],
 ["Sheet", "title", "—", "hub: 'put a stock-take sheet in your ZM queue manager folder'", "any title", "representational", HUB],
 ["Sheet", "tab Reports", "columns Report, Area, Status, Ticket, Review list, Why; 39 rows", "—", "column order free; Ticket holds the key of the existing ticket or of the new sub-issue; Review list as Yes/No or the like", "material", NOTEZ],
 ["Sheet", "tab Areas", "columns Area, Status, Open reports; 10 rows; Zombie Lane Clear, nine Open; open counts per the area table below", "—", "column order free", "material", NOTEZ],
 ["Sheet", "sharing", "Brian, Leonard, Arthur, Julia, Vincent", "hub: 'share it with everyone on the review invite, Leonard too'", "any role", "material (people) / representational (role)", EVT],
 ["Slide", "location and count", "one new slide in " + DECK, "—", "any layout, any position", "material (deck, one slide) / representational (layout)", HUB],
 ["Slide", "numbers", f"{NP} passed, {NQ} waiting on QA, {NF} waiting on a fix, {NCLEAR} area clear, {NREV} on the review list", "—", "labels free; '1 of 10' is fine", "material", NOTEZ],
 ["Reply", "destination", "Brian's DM D0770ET6WBW", "hub: 'tell me here'", "a new message in the DM or a reply in the thread of " + HUB, "material (the DM) / representational (thread or not)", HUB],
 ["Reply", "numbers", f"{NP}, {NQ}, {NF}, {NCLEAR}, {NREV}", "—", "extra detail may be added", "material", HUB],
 ["Review list", "membership", f"{NREV} reports: those not Passed in Collect & Win or Level-end rewards", "—", "—", "material", CARD + " (changed by " + CARDUPD + ")"],
]))
A("\nAreas (solver/truth.json):\n")
A(table(["Area", "Reports", "Open reports", "Status", "Source"], [[a, n, o, s, SHEET] for a, n, o, s in areas]))
A("\nReports (solver/truth.json; the row number is the pass sheet's # column):\n")
rr = []
for r in reps:
    n = rownum.get(r["Report"])
    src = f"{SHEET} row {n}" if n else FILT
    rr.append([r["Report"], r["Area"], r["Status"], r["Ticket"] or "new sub-issue", r["Review list"],
               f"{r['Ticket state as found'] or '—'} → {r['Ticket state']}", src])
A(table(["Report", "Area", "Status", "Ticket", "Review list", "Ticket state (as found → to set)", "Source"], rr))

# ---------------- discovery map
F = [
 ("F1", "Brian's ask", "the epic, the stock-take sheet, the share, the slide, five numbers back", HUB, "YES (DM member)", "met first (the anchor)", "—", "Yes (anchor AN1)", "slack", "flow review"),
 ("F2", "Brian's note on the ticket", "areas, what counts as a report, the three statuses, the ticket rule, states, Clear and Open, the review list, the tabs", NOTE + " on ZOM-543", "YES (Linear unscoped)", "named by the hub ('I left a note on the ticket')", "comments need their own read", "Yes for the ticket (anchor AN2); the note's content No", "linear", "Queue Manager"),
 ("F3", "Vincent's flow pass sheet", "38 rows: #, Area, What happens, Found on, Ticket, Fix, Re-test", SHEET, "YES (shared with Calvin)", "named by the hub and the note; its cells are the claims met first", "a sheet, not a chat", "No", "gsheets", "flow pass"),
 ("F4", "pass sheet legend", "ok, nr, again, 'ok, chat'; Fix is the PR he was told", LEG, "YES (shared with Calvin)", "the sheet's own note points at it", "a second doc to open", "No", "gdocs", "pass sheets"),
 ("F5", "Arthur's rule for QA passes", "a pass only counts on a build of the main branch", RULE, "YES (shared with Calvin)", "named by role in the note ('Arthur's rule for QA passes'); the decoy " + DD + " sits beside it", "a search for QA passes also returns the other game's doc", "No", "gdocs", "QA passes"),
 ("F6", "DD hotfix doc (decoy)", "a branch-build pass is enough, for DD hotfixes", DD, "YES (shared with Calvin)", "decoy for F5", "title names DD", "No", "gdocs", "hotfix builds"),
 ("F7", "Leonard's review card", "Thu Oct 2; Collect & Win and Level-end rewards", CARD + " (changed by " + CARDUPD + ")", "YES (Trello unscoped)", "Brian's earlier line " + OLD + " and the first invitation first; overturned by the changed card", "the card is off the DM path", "No", "trello", "flow review"),
 ("F8", "Brian's earlier line", "Friday; collect&win and daily gift first", OLD, "YES (DM member)", "met first, in the same DM as the hub", "reads as the agenda", "No", "slack", "daily gift first"),
 ("F9", "first invitation", "Fri Oct 3; Collect & Win and Daily Gift", INV1, "YES (Calvin's mailbox)", "met first", "older mail on the same meeting", "No", "gmail", "flow review"),
 ("F10", "updated invitation", "Thu Oct 2; agenda changed on the card", INV2, "YES (Calvin's mailbox)", "after F9", "says the card changed, not what to", "No", "gmail", "Updated invitation"),
 ("F11", "the review event", "Thu Oct 2 18:00 UTC; Leonard, Brian, Arthur, Julia, Vincent, Calvin", EVT, "YES (Calvin's calendar)", "named by the hub ('everyone on the review invite')", "—", "No", "gcal", "flow review"),
 ("F12", "review comment on #472", "the season pass icon restart is not in that diff", IN1, "YES (GitHub unscoped)", "the sheet's Fix cell and ZOM-571 In Validation first; overturned by Arthur's comment", "the review body is empty; the comment is inline", "No", "github", "Win&Collect into Queue Manager"),
 ("F13", "review comment on #475", "the pack sound stop is not in it", IN2, "YES (GitHub unscoped)", "the sheet's Fix cell and ZOM-581 In Validation first; overturned by Arthur's comment", "same", "No", "github", "animated icons"),
 ("F14", "Oliver's comment on his PR", "#473 also has the pass start popup fix and the bar fill fix", ELSE, "YES (GitHub unscoped)", "blank Fix cells and ZOM-572 Todo first; overturned by the comment", "no sheet cell points at #473", "No", "github", "Addressables/sp"),
 ("F15", "GitHub app copies in #zombie-prs", "the same three comments", "8e02c1142dfdd380c577a14bc366ee1d; 69700214ac2e727feec1d08d2b873218; 66dd5332dde5b7312c0ae201c285a323", "YES (channel member)", "a second route to F12 to F14", "thread replies under bot posts", "No", "slack", "season pass icon"),
 ("F16", "pass popup came back", "on Android Submission 135 the pass popup came up on top of the gift again", REOPEN, "YES (channel member)", "nr on row 9 first; overturned by Vincent's later reply", "a reply under a Sep 15 thread; the root is outside a recent-history read", "No", "slack", "pass popup"),
 ("F17", "home intro came back", "on Android Submission 135 the home intro played again after Endless", BACK, "YES (channel member)", "ok on row 29 first; overturned by Robert's reply under his Sep 10 endless thread", "a reply under a three-week-old thread; the root is outside a recent-history read", "No", "slack", "home intro"),
 ("F18", "Marcus's report", "the pass icon glow stays on after everything is claimed", FILT, "YES (DM member)", "the sheet reads as the whole list first", "a DM no anchor names", "No", "slack", "icon glow"),
 ("F19", "day counter row's ticket", "ZOM-556", AG + " on ZOM-556", "YES (Linear unscoped)", "no key in the sheet first; the tie is Vincent's note", "the ticket's title uses other words", "No", "linear", "daily gift is skipped"),
 ("F20", "freezer row's ticket", "ZOM-560", AS + " on ZOM-560", "YES (Linear unscoped)", "no key in the sheet first; the tie is Vincent's note", "the ticket's title uses other words", "No", "linear", "win streak freezer"),
 ("F21", "Vincent's 18 tickets", "ZOM-567 to ZOM-584; ZOM-571, ZOM-576, ZOM-581 In Validation, the rest Todo", "ZOM-567", "YES (Linear unscoped)", "keys are in the sheet", "states are claims, not facts", "No", "linear", "Season pass icon"),
 ("F22", "Calvin's folder", "ZM queue manager", FOLDER, "YES (Calvin owns it)", "named by the hub", "—", "Yes, by its plain name if needed", "gdrive", "queue manager"),
 ("F23", "Calvin's deck", "ZM queue manager, four slides", DECK, "YES (Calvin owns it)", "named by the hub", "—", "Yes, by its plain name if needed", "gslides", "queue manager"),
 ("F24", "which build 'ok, chat' was on", "Calvin's line naming iOS Internal #1718", "D06UPGF5PQV/1758817744.353289", "YES (DM member)", "Vincent's ok D06UPGF5PQV/1758820544.160399 first", "the build number is in the line before the ok", "No", "slack", "already tested"),
 ("F25", "where #1718 was built from", "Calvin's QueueManager branch", "C05433XK267/1758817549.151639", "YES (channel member)", "overturns 'ok, chat' on rows 1, 2 and 25", "the branch is in the bot post's text", "No", "slack", "Internal - #1718"),
 ("F26", "Android Submission #135", "a main build, Sep 30 20:13 UTC", "C05433XK267/1759263189.219529", "YES (channel member)", "dates F16 and F17 after the passes", "a busy channel", "No", "slack", "Android Submission"),
 ("F27", "PR #465", "merged Sep 25; coin replay and queued tutorials", "harmonygames-Games/match3d#465", "YES (GitHub unscoped)", "the Fix cell of rows 1, 2, 5, 25", "—", "No", "github", "queue manager"),
 ("F28", "the parked input blocker", "Brian: not a problem right now", "D0770ET6WBW/1758808795.588519", "YES (DM member)", "could read as a report; the note keeps it off", "—", "No", "slack", "input blocker"),
 ("F29", "Julia's point about Calvin's tickets", "why no priority or assignee on the new ones", "D05HYDTG5TJ/1756838837.147599", "YES (DM member)", "the note states the rule itself", "—", "No", "slack", "tickets"),
 ("F30", "Vincent's Bug Checklist canvas", "left as it is", "C08R27X0EAH/1755139050.519009", "YES (channel member)", "could read as more reports; the note keeps it out", "a canvas next to the list", "No", "slack", "Bug Checklist"),
 ("F31", "Oliver's skip tutorial exceptions", "stay off the list", "C08R27X0EAH/1758903616.346579", "YES (channel member)", "could read as reports; the note keeps them off", "—", "No", "slack", "skip tutorial"),
]
A("\n## 5 · Discovery map\n")
A("Root causes and findings appear only here and never in the prompt.\n")
A(table(["Fact", "Value", "Locator", "Persona-readable", "Met first / overturned by", "Search risk", "Name in prompt?"],
        [[f"{f[0]} {f[1]}", f[2], f[3], f[4], f[5], f[6], f[7]] for f in F]))

A("\n## 5a · Search-as-persona proof\n")
A("`persona_view.py search calvin_price <service> \"<query>\" --limit 3 --no-hidden` reads base data; seeded rows Calvin can see are counted from the SQL overlay (check-sql PASS for every scoped seeded record, dossier 1.E). For a base fact the hit id is the target record among the visible hits. Outputs verbatim below the table.\n")
rows, outs = [], []
BASEF = {"F24", "F25", "F26", "F27", "F28", "F29", "F30", "F31"}
SCOPED = {"slack", "gmail", "gcal", "gdrive", "gdocs", "gsheets", "gslides"}
for f in F:
    out = open(os.path.join(HERE, "out", "brief", f[0] + ".txt")).read().rstrip()
    outs.append(out)
    m = re.search(r"visible hits=(\d+)", out); base = int(m.group(1))
    hid = "n/a (--no-hidden)" if f[8] in ("slack", "gmail") else "0"
    q = f[9]
    seeded = sum(1 for ch in SQL.split('INSERT INTO ')[1:] if ch.startswith(f[8] + '.') and q.lower() in ch.lower())
    first = f[3].split(" ")[0].rstrip(";")
    if f[0] in BASEF:
        found = "YES (base hit)"
    elif f[0] in {"F2", "F12", "F13", "F14", "F19", "F20"}:
        found = "YES (base hit on the parent record; the seeded comment sits on it, unscoped)"
    else:
        found = "YES (seeded; " + ("check-sql YES" if f[8] in SCOPED else "unscoped") + ")"
    rows.append([f[0], f[8], q, f"{base} base + {seeded} seeded", hid, first, found])
A(table(["Fact (§5 row)", "Service", "Natural query", "Visible hits", "Hidden by ACL", "First visible hit (id)", "Found?"], rows))
A("\n```\n" + "\n".join(outs) + "\n```")

A("\n## 6 · Triggers, incorporation and implicit requirements\n")
A(table(["Graded requirement", "Seeded where", "Trigger category the prompt must carry", "Incorporating source (locator · persona-readable · unique · instructions-not-answer)", "Inferable"], [
 ["ten area children under the epic", NOTE, "deliverable (Brian's ask)", "hub " + HUB + " 'I left a note on the ticket about how I want it' · YES · one note by Brian on ZOM-543 · rules, no answers", "yes, once the hub is followed"],
 ["which reports are in the list", NOTE, "scope", NOTE + " · YES · unique · a scope sentence, no list", "yes"],
 ["status of each report", NOTE, "scope", NOTE + " names 'Arthur's rule for QA passes' · YES · " + RULE + " is the one ZM doc with that subject · rule, no answers", "yes, through the note"],
 ["ticket reuse, move, note and state", NOTE, "none", NOTE + " · YES · unique · instruction", "gotcha with a record trigger"],
 ["no priority and no assignee on new ones", NOTE, "none", NOTE + " · YES · unique · instruction", "gotcha with a record trigger"],
 ["review list", NOTE, "none", NOTE + " 'in an area on the agenda of Thursday's review' · YES · one card " + CARD + " · names areas, not reports", "gotcha with a record trigger"],
 ["stock-take sheet in the folder, shared with the review's people", HUB, "destination + recipients", "hub 'share it with everyone on the review invite, Leonard too' · YES · one event " + EVT + " · names people, no answers", "yes"],
 ["tabs and columns", NOTE, "none", NOTE + " · YES · unique · instruction", "gotcha with a record trigger"],
 ["one slide with the numbers", HUB, "deliverable", "hub · YES · one deck " + DECK + " in Calvin's Drive · instruction", "yes"],
 ["five numbers back to Brian", HUB, "deliverable", "hub 'tell me here' · YES · DM D0770ET6WBW · instruction", "yes"],
]))
A("\nAnchor-name table (noun phrases of at most 6 words; `;` separates synonyms):\n")
A(table(["Anchor", "May be named"], [["AN1", "Brian's message from yesterday; Brian's DM"], ["AN2", "the Queue Manager ticket; ZOM-543"]]))

A("\n## 7 · Dates and constraints\n")
A(table(["Item", "Absolute date or value", "Source", "Past fact or deadline"], [
 ["Calvin's today", "Wednesday Oct 1, 2025 (clock 2025-10-01 00:00 PT = 07:00 UTC)", "00_Task_Context.json universe.persona_today; last hub record " + HUB, "—"],
 ["Brian's ask", "Tue Sep 30, 2025 13:40 PT (20:40 UTC): 'yesterday' for Calvin", HUB, "past fact"],
 ["Brian's note on the ticket", "Tue Sep 30, 2025 13:25 PT (20:25 UTC)", NOTEZ, "past fact"],
 ["Vincent's pass started", "Fri Sep 26, 2025 (sheet created 03:12 PT, 10:12 UTC)", SHEET, "past fact"],
 ["pass sheet last changed", "Tue Sep 30, 2025 12:30 PT (19:30 UTC)", SHEET, "past fact"],
 ["review card changed", "Tue Sep 30, 2025 10:22 PT (17:22 UTC)", CARDUPD, "past fact"],
 ["first invitation", "Mon Sep 29, 2025 09:05 PT (16:05 UTC), for Fri Oct 3", INV1, "past fact"],
 ["updated invitation", "Tue Sep 30, 2025 10:24 PT (17:24 UTC), for Thu Oct 2", INV2, "past fact"],
 ["the flow review", "Thu Oct 2, 2025 11:00 to 11:30 PT (18:00 to 18:30 UTC; 12pm CST on Calvin's invitation): 'Thursday' or 'tomorrow'", EVT, "deadline (future event); no deadline is graded"],
 ["Android Submission #135", "Tue Sep 30, 2025 13:13 PT (20:13 UTC)", "C05433XK267/1759263189.219529", "past fact"],
 ["latest seeded record", "Tue Sep 30, 2025 14:44 PT (21:44 UTC), before the clock", BACK, "past fact"],
]))

A("\n## 8 · Difficulty levers\n")
A(table(["Lever", "Used", "Load-bearing", "Where it lives", "Prompt-side condition"], [
 ["Ambiguity", "yes", "yes", "what decides a report's status is spread over the note, the legend, the rule doc, build posts and PRs (F2 to F5, F24 to F27)", "the prompt names the two anchors only, never where an answer lives"],
 ["Dynamic change", "yes", "yes", "sheet cells, ticket states and the first invitation are met first and overturned later (F7, F12 to F14, F16, F17)", "the prompt names neither a first reading nor what corrects it"],
 ["Multi-source", "yes", "yes", "Linear, Sheets, Slack, GitHub, Docs, Trello, Gmail, Calendar, Drive, Slides", "no source named as an exact artifact beyond the two anchors"],
 ["Async", "no", "no", "Friction: none (03_Error_Async_Config.txt)", "—"],
 ["Error recovery", "no", "no", "Friction: none", "—"],
 ["Access control", "no", "no", "every load-bearing record is Calvin-visible (check-sql PASS)", "no ask to read someone else's scoped data"],
]))

A("\n## 9 · Must not appear in the prompt\n")
A("- **Tool and server names (catalog.json):** linear_create_issue, linear_update_issue, linear_create_comment, linear_list_issues, linear_list_comments, slack_send_message, slack_read_thread, slack_search_public_and_private, slack_conversations_history, github_get_pull_request_comments, github_get_pull_request_reviews, gsheets_create_spreadsheet, gsheets_values_update, gsheets_batch_update, gdrive_share_file, gdrive_move_file, gslides_batch_update, gmail_search_messages, gcal_list_events, trello_search, any MCP server name.")
A("- **Opaque ids and filenames:** " + ", ".join([SHEET, LEG, RULE, DD, FOLDER, DECK, EVT, CARD]) + ", D0770ET6WBW, D06UPGF5PQV, D05U73FNDDL, C08R27X0EAH, C0880U9751A, C093LEZGF6J, C05433XK267, every ZOM key other than ZOM-543.")
A(f"- **Findings and root causes:** any status, any count ({NP}, {NQ}, {NF}, {NCLEAR}, {NREV}, 39, 38, 19, 20, 10), any area name, #builds or any build number (#1718, 135), the QueueManager branch, any PR number (#465, #472, #473, #475) or review comment, Vincent's thread reply, Robert's post, Oliver's comment, Marcus or his report, ZOM-556, ZOM-560, ZOM-571, ZOM-572, ZOM-581.")
A("- **Hidden authorities and rules:** Brian's note's content or any of its sentences, the three statuses, the state mapping, Clear and Open, the review list rule, the tabs and columns, the pass sheet's legend, Arthur's doc or its rule, the DD doc, Leonard's card or Trello, the invitation mails, the review having moved, Julia's point.")
A("- **Format and choreography:** markdown, numbered steps, a per-column content list, a service list, a call count, 'first … then …'.")
A("- **Friction and files:** none configured; no reference files or /app/artifact paths.")

A("\n## 10 · Entity traps\n")
A("`entity.py collisions` and `entity.py resolve` for every name the prompt could use, verbatim:\n```")
A(open(os.path.join(HERE, "out", "brief", "collisions.txt")).read().rstrip())
A(open(os.path.join(HERE, "out", "brief", "resolve.txt")).read().rstrip())
A("```\n")
A(table(["Correct entity (exact)", "Lookalike(s)", "How they differ", "Locator (email or record id)"], [
 ["Brian Foster", "none by first name", "the requester; Calvin's DM partner in D0770ET6WBW", "brian.foster@harmonygames.co"],
 ["Vincent Parker", "none by first name", "QA; owner of the pass sheet", "vincent.parker@harmonygames.co"],
 ["Arthur Blake", "'Blake' in base talk; mail thread files named blake@", "one person", "arthur.blake@harmonygames.co"],
 ["Leonard Hayes", "none", "organizer of the review", "leonard.hayes@harmonygames.co"],
 ["Julia Lawson", "Peter Lawson", "Julia is on the invite", "julia.lawson@harmonygames.co"],
 ["Marcus Bennett", "Marcus Lee, Oscar Bennett, github and trello 'Marcus'", "Calvin's DM partner is Bennett; the prompt must not name him", "marcus.bennett@harmonygames.co"],
 ["Robert (one name)", "none", "co-founder; posts in #zombie-match3d and #zombie-bugs", "robert@harmonygames.co"],
 ["Oliver Brooks", "Lauren Brooks", "Oliver wrote and merged #473", "oliver.brooks@harmonygames.co"],
 ["Calvin Price", "Nathan Price; two GitHub identities for Calvin", "the persona", "calvin.price@harmonygames.co"],
 ["ZOM tickets", "ENG tickets (DD)", "ZM is on ZOM; the decoy doc " + DD + " is about DD", "ZOM-543"],
 ["the Queue Manager ticket", "'Reward animation and queue manager issues' and other tickets that mention a queue manager", "ZOM-543 is titled Queue Manager and is Calvin's", "ZOM-543"],
]))

A("\n## 11 · Pre-submit checklist\n")
for c in ["Persona voice: Calvin, first person, plain; no spec-sheet layout",
          "Names only the two anchors (§6 table); no §9 item",
          "States the deliverables at the level Brian's DM does, or simply points at it; destination named",
          "No tool or server name; no step list; no count; no area name",
          "No word that the review moved, that a pass may not count, or that something came back",
          "'yesterday' for Brian's message and 'Thursday' for the review are the only dates, if any",
          "Clean spelling and punctuation; no riddle, hint, hedge or if-chain",
          "20–4,000 words",
          "Run `/create-prompt-writing check` before `/prompt`"]:
    A("- [ ] " + c)

A("\n## 12 · Blockers and routed defects\n")
A("None blocking. No fact is routed to /create-injection: every §5 fact is found by a natural search or reached by reading an anchor's DM, ticket, sheet or card (§5a). rev2 (sha256 ee46405a157d) needs its own platform /injection before /prompt; the prompt text is the one /prompt scored 5 on rev1.\n")
A("Open, not blocking: the fixes made after the two blind sweeps of the SQL were not swept again; the pre-check must confirm that Slack tools return the attachment text of the #builds posts (C05433XK267/1758817549.151639) and of the #zombie-prs copies; no independent red team ran (fallback recorded in the scenario design, section 13). The under-60 % requester target stays at risk until the pre-check run.")

A("\n## 13 · Self-review\n")
A(table(["Area", "Counter-reading (strongest argument it fails)", "Evidence that resolves it", "Verdict"], [
 ["Fair readings (C6)", "Rows 1, 2 and 25 are Passed: Vincent said ok in the chat.", RULE + " counts only main builds; C05433XK267/1758817549.151639 shows #1718 came from Calvin's QueueManager branch; harmonygames-Games/match3d#465 is merged, so Waiting on QA", "settled"],
 ["Fair readings (C6)", "Row 12 is Waiting on QA: #472 is merged and ZOM-571 is In Validation.", NOTE + " 'a fix for it is in main'; " + IN1, "settled"],
 ["Fair readings (C6)", "Rows 13 and 38 are Waiting on a fix: the sheet names no PR.", NOTE + " 'a fix for it is in main that QA has not tried on a main build yet'; " + ELSE, "settled"],
 ["Fair readings (C6)", "Row 9 stays Passed: Vincent's reply is about another thread's topic.", RULE + " 'A pass stands until somebody sees the bug again on a main build made after the one it passed on'; " + REOPEN + " names Android Submission 135, C05433XK267/1759263189.219529", "settled"],
 ["Fair readings (C6)", "Row 29 stays Passed: Robert is not QA.", "the note says 'somebody'; " + BACK, "settled"],
 ["Fair readings (C6)", "Daily Gift is on the review list: Brian said so on Sep 29.", "the note names the review's agenda and the updated invitation puts it on the roadmap card; " + CARDUPD + " is later than " + OLD + " and " + INV1, "settled"],
 ["Fair readings (C6)", "Marcus's line is not a report: it is a chat remark.", NOTE + " 'any bug somebody else on the team saw in a build and told you about in a DM since Vincent started his pass on the 26th'; " + FILT, "settled"],
 ["Fair readings (C6)", "Rows 11 and 20 get new sub-issues: the sheet has no key.", NOTE + " 'if a ticket already has the report, move that ticket'; " + AG + "; " + AS, "settled"],
 ["Clarity (C7)", "'tell me here' could be a thread reply or a new DM message.", "§4b accepts both, in D0770ET6WBW (" + HUB + ")", "accepted outcomes"],
 ["Clarity (C7)", "The share leaves the role open, and the sheet's title is not given.", "§4b accepts any role for the five attendees of " + EVT + " and any title", "accepted outcomes"],
 ["Incorporation (C8)", "The note might not be reached: the prompt names only the DM.", "hub " + HUB + " says 'I left a note on the ticket about how I want it'; " + NOTE + " is Brian's only note on ZOM-543 and Linear is unscoped", "incorporated"],
 ["Incorporation (C8)", "'Arthur's rule for QA passes' could be the DD doc.", RULE + " is titled 'ZM builds and QA passes'; " + DD + " is titled for DD hotfixes", "unique"],
 ["Truthfulness (C17)", "'yesterday' could be the wrong day for Brian's message.", HUB + " is Tue Sep 30 13:40 PT and Calvin's today is Wed Oct 1 (00_Task_Context.json)", "true"],
 ["Truthfulness (C17)", "Calvin might not own the ticket or the folder.", "ZOM-543 is assigned to Calvin (base); " + FOLDER + " and " + DECK + " are owned by calvin.price@harmonygames.co in the SQL", "true"],
 ["Feasibility / ACL (C18–C19)", "The sheet must sit in Calvin's folder with two tabs and be shared; a new sheet lands in his root with one tab.", "gsheets_create_spreadsheet, gsheets_batch_update to add the tab, gdrive_move_file to " + FOLDER + ", gdrive_share_file; Calvin owns the folder", "feasible"],
 ["Feasibility / ACL (C18–C19)", "Calvin cannot read the other attendees' invitations.", "his own event copy " + EVT + " lists all six attendees, and " + INV2 + " is in his mailbox", "feasible"],
 ["Feasibility / ACL (C18–C19)", "States or parents might not be settable.", "Todo, In Validation and Done are states on base ZOM tickets (ZOM-556 Todo); linear_create_issue and linear_update_issue take state and parentId", "feasible"],
 ["Contrived register (C15–C16)", "Pointing at Brian's DM could read as hiding the destination.", "the prompt names the DM and the ticket, and the DM itself names the folder, the deck and where to answer (" + HUB + "); prompt_qc_cases hidden_destination", "ordinary"],
 ["Contrived register (C15–C16)", "Listing what Brian wants could read as a command list.", "deliverables and who to tell are the screen-24 skeleton, not sequenced method steps; ZOM-543 stays named as an anchor only", "ordinary"],
]))
A("\nFair readings, clarity, incorporation, truthfulness, feasibility / ACL and the contrived register are each addressed above with evidence. Unresolved: the prompt is not yet written, and check mode re-tests every point on the actual text.\n")
open(os.path.join(WF, "04_Prompt_Writing_Brief.md"), "w").write("\n".join(L) + "\n")
print("brief written", len("\n".join(L)))
