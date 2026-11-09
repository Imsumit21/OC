#!/usr/bin/env python3
"""Write selfreview.md (the plan's Self-review) from rows.json and the local baseline grade."""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
rows = json.loads((HERE / "rows.json").read_text())
TAG = {r["tag"]: f"P{i + 1}" for i, r in enumerate(rows)}
grade = subprocess.run([sys.executable, "-B", str(HERE / "grade_baselines.py")], capture_output=True, text=True).stdout
g = {k: v for k, v in (l.split(" ", 1) for l in grade.splitlines() if l.startswith(("scores", "precheck", "all-fail", "patterns")))}
keep = [l for l in grade.splitlines() if l.startswith(("rows ", "scores", "precheck", "patterns", "varying"))]
m = re.search(r"mean (\S+) popSD (\S+)", grade)
MEAN, SD = m.group(1), m.group(2)
AF = re.search(r"all-fail rows (\d+) weight (\d+)", grade)

SPEC = {
    "sheet_folder": "(a) a sheet created in the root and moved in passes, the title says so · (b) a sheet left outside d_caafeec2804b3a67ce46aa fails on its final parent",
    "sheet_header": "(a) another letter case or column order passes · (b) a dropped What's missing fails against D06L58XCVKK/1759264851.763895",
    "sheet_rows": "(a) a row named by the sheet's or the ticket's name counts once · (b) 32 rows (no comment asks) fail, and a 37th for a red dot fails; the rule doc f_dc45e0e5a8b8635c1b82b2 defines a message as what reaches a closed phone",
    "call_lives_recharged": "(a) none: test 6 fails once Vincent's tick is off, and the row's name 'Full Ammo' is the same message · (b) Go from the Sep 24 pass fails against C0880U9751A/1759245146.720608",
    "call_plague_race": "(a) none: Vincent scratched iOS, so test 6 fails · (b) Go from the checks sheet's Sep 24 pass fails against D06UFE81RF0/1759174846.723833",
    "call_weekly_leaderboard_reset": "(a) none: test 5 fails on Arthur's comment · (b) Go from Ready, Done and Vincent's pass fails against harmonygames-Games/match3d#248#rc_18",
    "call_finish_first_mission": "(a) none: 'It fails only if none of them count', and none do · (b) Go from the settings-toggle pass fails against C0880U9751A/1759167608.326578",
    "call_lapsed_1_day": "(a) none: all six tests pass · (b) Hold because Full Ammo went missing on 0.3.49 fails: Vincent says 'the lapsed ones are still coming through' (C0880U9751A/1759245146.720608)",
    "call_lapsed_7_days": "(a) none: a line change is a String change, not a Hold · (b) Hold for the new line fails against rule doc f_dc45e0e5a8b8635c1b82b2",
    "head_l7": "(a) with or without an emoji passes · (b) 'Your Squad Needs You Back' fails: evt_f2c03e69f50acf62c9d1c3 says it replaces the art-thread line",
    "head_l1": "(a) with or without its emoji passes (rule doc: emoji don't count) · (b) another line fails against f_a325dd4af80afc5994d5dc row 4",
    "str_l7": "(a) 'Yes - DES-346', or the key alone, passes: the DM names the column but sets no Yes/No form · (b) No fails: the client ships a different line (harmonygames-Games/match3d#248)",
    "str_l1": "(a) 'None - client already ships this line' passes, as in run-4 · (b) Yes fails: emoji don't count (f_dc45e0e5a8b8635c1b82b2)",
    "head_count": "(a) n/a or a dash on the other rows passes, and the row reads the sheet's own Go rows, so a wrong Go is judged on its own call row · (b) a headline on a Hold row fails against rule doc f_dc45e0e5a8b8635c1b82b2 ('only for Go rows')",
    "str_count": "(a) n/a or a dash on the other rows passes · (b) 'No' down all 36 rows fails against rule doc f_dc45e0e5a8b8635c1b82b2 ('only for Go rows')",
    "msg_lapsed_1_day": "(a) either name passes, in any wording · (b) a blank Message cell fails; PN sheet f_a325dd4af80afc5994d5dc row 4 and DES-316",
    "tally_go": "(a) any row order passes · (b) run-3's four Go fail; the rule doc f_dc45e0e5a8b8635c1b82b2 sets a Go at all six tests",
    "call_lapsed_14_days": "(a) none: the weekly batch covers day 14, so the rule makes it a Drop · (b) Hold as new work fails against the cancellation mail and DES-344 (rule doc f_dc45e0e5a8b8635c1b82b2)",
    "new_unassigned": "(a) a ticket created with no assignee passes · (b) that ticket assigned to Samuel fails; card 68d1eb90bef538c7c5c5599d ('unassigned')",
    "ticket_teammate_sent_lives": "(a) the new key alone or with a title passes · (b) ZOM-563 in the cell fails: the comment's ticket is not the message's ticket (OE 58)",
    "ticket_wc": "(a) 'DES-313 Ping when a Collect & Win window opens' passes · (b) a new key fails: DES-313 exists (Confluence page_liveops_calendar)",
    "note_folder": "(a) a note moved in passes · (b) a note left elsewhere fails on d_caafeec2804b3a67ce46aa",
    "note_page": "(a) any layout passes; all seven runs wrote 364 to 711 words · (b) a multi-page note fails; the prompt says 'the one-page note' (D06L58XCVKK/1759264851.763895 repeats it)",
    "note_first": "(a) a title or lead-in first passes, as in run-5 · (b) Holds before the lapsed reminders fail against D06L58XCVKK/1759264851.763895 ('start with D1 and D7', 'then the lapsed reminders')",
    "note_ladder": "(a) 'Day 1, then days 7, 14, 21 and 28' in any layout passes, and the race and leaderboard may sit beside them · (b) stopping at day 7 fails against harmonygames-Games/match3d#248",
    "note_count": "(a) the four named in any order pass, a caveat beside them is harmless · (b) three, with Plague Race passed as Go, fail; solver/truth.json holds four",
    "cm_count": "(a) a comment pointing to a new ticket is no call comment · (b) a call left on ZOM-542 instead of the new ticket fails (brief §4 risk 'base tickets holding the asks')",
    "mv_total": "(a) moves in any order pass, and its new tickets don't count · (b) DES-317 moved to In Progress, or DES-314 closed, makes 31; rule doc f_dc45e0e5a8b8635c1b82b2 ('Go tickets stay as they are')",
    "mv_unassign": "(a) unassigning in the same update or a later one passes · (b) a state-only move leaves Samuel assigned and fails, and a Todo run that unassigns nothing can't pass; card 68d1eb90bef538c7c5c5599d ('unassigned')",
    "new_state": "(a) a state set at creation or by a later update passes · (b) that ticket in Todo fails; card 68d1eb90bef538c7c5c5599d ('Held tickets sit in Backlog, unassigned.')",
    "new_string": "(a) any title, state or assignee passes (brief §4b) · (b) 'Your Squad Needs You Back' fails against evt_f2c03e69f50acf62c9d1c3",
    "new_count": "(a) the four asks and one string ticket in any team pass · (b) a second Win & Collect ticket makes six, against D06L58XCVKK/1759264851.763895 ('don't make a second one')",
    "chk_count": "(a) any checklist name passes · (b) run-3's four items fail: a Hold is on the list; card 6851a769c65dc0017a227bb7",
    "em_count": "(a) a second mail to one person counts once · (b) nine with Leonard fails, and seven with Douglas missing fails; D06L58XCVKK/1759264851.763895 ('apart from me')",
    "order_dm": "(a) a read after the post is harmless; only the listed writes count · (b) a late email fails; the prompt says 'When it's all finished' (D06L58XCVKK/1759264851.763895)",
}


def cr(r):
    t = r["tag"]
    if t in SPEC:
        return SPEC[t]
    src = re.search(r"(DES-\d+|ZOM-\d+|cmt_[0-9a-f]+|[CD]0[0-9A-Z]+/\d+\.\d+|f_[0-9a-f]+|page_liveops_calendar|\b[0-9a-f]{24}\b)", r["ev"])
    rec = src.group(1) if src else "D06L58XCVKK/1759264851.763895"
    if t.startswith("call_"):
        return f"(a) the row may use the sheet's or the ticket's name, so it is found by its Ticket cell · (b) {r['alt']} Record: {rec}"
    if t.startswith("miss_"):
        return f"(a) any wording naming that gap passes, with or without the test number · (b) {r['alt']} Record: {rec}"
    if t.startswith("aud_"):
        return f"(a) a plain rewording passes (brief §4b) · (b) {r['alt']} Record: {rec}"
    if t.startswith("ticket_"):
        return f"(a) a key with a title passes · (b) {r['alt']} Record: {rec}"
    if t.startswith("un_"):
        return f"(a) unassigning in the same update as the move or a later one passes · (b) {r['alt']} Record: 68d1eb90bef538c7c5c5599d"
    if t.startswith("note_"):
        return f"(a) rounded to one decimal, with or without %, passes (brief §4b) · (b) {r['alt']} Record: wh_USER_COHORT_RETENTION rows 236 and 237"
    if t.startswith("nh_"):
        return f"(a) any wording naming the gap passes, with or without the test number · (b) {r['alt']} Record: {rec}"
    if t.startswith("cm_"):
        return f"(a) any wording carrying the call passes, a reason beside it is free · (b) {r['alt']} Record: {rec}"
    if t.startswith("mv_"):
        return f"(a) a move in any order among the writes passes · (b) {r['alt']} Record: {rec}"
    if t.startswith(("newb_", "newu_")):
        return f"(a) set at creation or by a later update passes · (b) {r['alt']} Record: 68d1eb90bef538c7c5c5599d"
    if t.startswith("nhn_"):
        return f"(a) any of the listed names passes, in any layout · (b) {r['alt']} Record: {rec}"
    if t.startswith("new_"):
        return f"(a) any title in Design or Zombie Match 3D passes (brief §4b) · (b) {r['alt']} Record: {rec}"
    if t.startswith("chk_"):
        return f"(a) any checklist name, and an item that adds the headline, passes · (b) {r['alt']} Record: 6851a769c65dc0017a227bb7"
    if t.startswith("em_"):
        return f"(a) the ticket key or the name passes, in any wording, in one mail or two · (b) {r['alt']} Record: {rec}"
    if t.startswith("dm_"):
        return f"(a) any order and wording with the number passes · (b) {r['alt']} Record: D06L58XCVKK/1759264851.763895"
    raise KeyError(t)


L = ["## Self-review", ""]
A = L.append
A("Re-read as /rubric: walked Evals/3_Rubrics_Eval.md 1.4 and 3.1 against the plan in order. Every prompt requirement (ledger R1–R13), every write family (sheet, note, comments, moves, new tickets, checklist, emails, DM), the three told counts, "
  "every exclusion (the decoys and second tickets, as exact counts on the required writes; Leonard, as the count of people emailed) and the ordering ask ('When it's all finished') has a row on the correct artifact. No row grades the final response; the DM is the deliverable the prompt names. "
  "The /oe report's 'No Process row is needed' speaks to reads; the prompt's ordering ask still needs its one row, which no Outcome can show.")
A("")
A("Re-verified: every source value in 00_V3_Authoring_Evidence.json was read in this run by plan/rubric/build_rubric.py: seeded rows by parsing 01_Universe_Inject.sql (never executed), base records through hg.py get-many (GitHub review comment 599, Trello cards 705 and 802, "
  "Confluence page 27, Contacts, Snowflake table 10 rows 236 and 237). Every quote in a row's evidence is asserted against its record at build time. Counts were recomputed from solver/truth.json (36 rows, 32 existing tickets, 24 Backlog, 6 Canceled, 5 new tickets, 2 Go items, 8 people, Go 2, Hold 28, Drop 6). "
  "Limits of the V3 sidecar, not of the rows: the gate's lookup for unscoped services reads base data only, so seeded Linear tickets (DES-313 to DES-345) are named in each row's evidence text and the sidecar cites the rule doc, the DM or a base ZOM ticket; the Snowflake rows have no timezone-aware field, so the sidecar cites the DM, and the build asserts the four values on rows 236 and 237.")
A("")
A("Predicted all-fail re-check: for every row the persona reaches the value through a cataloged tool (Gmail, Slack, Calendar and Drive records pasted YES under Visibility proof; Linear, Trello, GitHub, Confluence, Snowflake and Contacts unscoped), each write exists in the catalog (ledger §C), no row needs a rate-1.0 retry and no evidence sits outside Samuel's view. "
  f"Count on the four bases: 0. The local grade below shows {AF.group(1)} rows ({AF.group(2)} weight) failing all six baselines: all rest on the four comment asks, each reachable through OE 9 to OE 13 (updatedAt, then each ticket's comments). They are discovery failures, not impossible targets, and /create-allfail must prove that route (ledger §F 1 and §F 3).")
A("")
A("Local baseline grade (plan/rubric/grade_baselines.py over the six rev6 trajectories; a local estimate of the verifier, not its result):")
A("")
A("```text")
for l in keep:
    A(l)
A("```")
A("")
A("Shortcut and diversity: the §F probe hits are dispositioned below the paste. The largest units of discovery are the rule doc (F2) and the parent DES-314 (F4), upstream of every call by construction — see Unresolved.")
A("")
A("Surface dispositions: ten slots are dispositioned. X2b, X6b, X8b and X21b are reasons on ticket comments: the DM asks to 'Leave the call as a comment', and the reason is already graded in the sheet and the note. X11, X12, X11b and X12b are sheet Call cells whose call is graded on the ticket and in the email; their rows are graded by What's missing. X18 and X19 are per-ticket moves the round-1 Fix List cut to keep the Backlog samples at five.")
A("")
A("Brief §4b: two acceptances are narrowed. §4b lets Todo pass on the four Done Holds; the rows require Backlog, because OE 98 to OE 101 say so, /oe passed that reading, and a row accepting Todo would pass a wrong state (overly_broad). §4b and ledger §F 6 let the call sit in a new ticket's description; the rows require a comment, because the DM says 'Leave the call as a comment on each ticket' and OE 50, 52, 54 and 56 are comments. No run is affected: all seven moved those tickets to Backlog when they held them, and none reached the new tickets.")
A("")
A("Platform /rubric round 2 (2026-11-06, FAIL 1, reviewed sha d1cbadf710e9, coverage 153/153): every checked fix is copied word for word, by assertion. R21 is the author's rewrite the report asks for: the cell must identify Lapsed 7 days, the bare name passes, the client's and Leonard's names and any other wording that identifies it pass, and a cell naming only the Weekly Leaderboard batch fails, because that batch also fires on day 14 and is a Hold. The code call site was re-read in the PR #248 hunk and in run-5's file read. R121 is left locked, though its name list lacks the client's 'Lapsed last session reminder' (the report's note for QM): editing it would unlock a row that passed.")
A("")
A("Platform /rubric round 1 (2026-11-06, FAIL 1, reviewed sha 3911b7d5f4de, coverage 154/156): every Fix List item is applied word for word, checked by an assertion that each title sits in the report and that each row lands at its 'cand.' number. 113 of the 149 rows are byte-identical to the reviewed JSON, so DELTA keeps them locked. Local edits made after that build (sha 6dc1d728a183, from two blind reviews) were set aside, so no row changes that the report did not name; they are stored in run_forensics/rev6/rubric_r1/. The five 'not scored, worth doing' items are applied to supporting fields only.")
A("")
A("Counter-readings, one per section A row:")
A("")
A("| P | Counter-reading (a valid answer that could fail · a wrong answer that could pass) and resolution (evidence) |")
A("|---|---|")
for i, r in enumerate(rows):
    A(f"| P{i + 1} | Counter-reading — {cr(r).replace('|', '/')} |")
A("")
DIV = json.loads((HERE / "diversity.json").read_text()) if (HERE / "diversity.json").exists() else {}
A(f"Unresolved: (1) diversity.authority_share, the one structural gate check: {DIV.get('units', 'the rule doc and DES-314')} sit upstream of most of the weight. Leonard's DM names both as the rule and the ticket list, and no honest rubric can grade a call without them. A design finding for the human to accept, as on the archived bridge and Q4 tasks. "
  f"(2) The local grade estimates mean {MEAN} and population SD {SD} on the rev6 baselines (retained band 0.10–0.30): the SD check is expected to fail on this batch; the requester has not ruled on it. Trimming or re-weighting rows to reach the band is forbidden. "
  "(3) If the comment-ask rows were ruled invalid, the average would rise above the 85% cap, so /create-allfail must prove the updatedAt route. "
  "(4) The Fix List adds a sheet Call row for DES-344 beside its comment and email rows, so that call sits on three artifacts. The platform asked for it; the email row's fact is declared told:Lapsed 14 days, so v3.fact_duplication passes on the declared ids only. (5) Ledger §F 2 says relations are seeded on the ZOM side only. That is out of date: the SQL inserts relations_json on DES-315, DES-330 and DES-338 as well (SQL L111, L141, L157), a second route to the asks. No OE or row relies on it and no run saw a non-empty relatedTo, so the ledger is left as sealed, and /create-allfail can cite the route once it is proven.")
(HERE / "selfreview.md").write_text("\n".join(L) + "\n")
print("selfreview written:", len(rows), "counter-readings; mean", MEAN, "SD", SD)
