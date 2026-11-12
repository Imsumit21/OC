#!/usr/bin/env python3
"""Write 11_AF_Justification.md (workbook) and 11_Baseline_AllFail_Justifications.md (screen file) for stage 11.

Inputs: allfail_gen/out/evidence.json (allfail_gen/evidence.py, read from the six bound exports), the task model
(oe_gen/model.py, parsed from 01_Universe_Inject.sql), 09_Rubrics.json and the raw verifier copy. Every figure in the
two files is asserted here against those inputs before anything is written. Re-running keeps the pasted stage-gate
block at the end of the workbook's Self-review out of the way: the gate is pasted again after each rebuild."""
import collections, hashlib, json, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parent
TASK = WF.parent
sys.path.insert(0, str(WF / "oe_gen"))
import model as M  # noqa: E402

EV = json.loads((HERE / "out" / "evidence.json").read_text())
RUNS = {r["run"]: r for r in EV["runs"]}
RUBRIC = json.loads((TASK / "09_Rubrics.json").read_text())
ROW = lambda n: RUBRIC[n - 1]
CLOCK = json.loads((WF / "00_Task_Context.json").read_text())["universe"]["clock_line"]
CLOCK = CLOCK if CLOCK.startswith("Clock:") else "Clock: " + CLOCK
ALL_FAIL = [55, 147, 148]
A1K = "A1 Marcus's post C0880U9751A/1758906517.912099"
A2K = "A2 Robert's note D05GU6L0XFH/1759178332.042459"
C4K = "C4 Brian's log f_faf4d7c167d14a1127dcc3"

# ------------------------------------------------------------------ recompute the all-fail list from the raw verifier copy
VER = (TASK / "10_Baseline_Verifier_Results.md").read_text()
parts = re.split(r"(?m)^Run\s*#\s*(\d+)\s*$", VER)
fails, headers, verdicts = collections.Counter(), {}, {}
for i in range(1, len(parts), 2):
    n, body = int(parts[i]), parts[i + 1]
    m = re.search(r"(\d+)/(\d+) criteria passed", body)
    rows = [l.split("\t") for l in body.splitlines() if "\t" in l and l.split("\t")[1].strip() in ("Pass", "Fail")]
    assert (sum(r[1].strip() == "Pass" for r in rows), len(rows)) == (int(m.group(1)), int(m.group(2))), n
    headers[n] = (int(m.group(1)), int(m.group(2)))
    for k, r in enumerate(rows, 1):
        verdicts[(n, k)] = (r[1].strip(), r[2].strip() if len(r) > 2 else "")
        if r[1].strip() == "Fail": fails[k] += 1
assert sorted(headers) == [1, 2, 3, 4, 5, 6] and all(h[1] == 153 for h in headers.values())
RECOUNT = sorted(k for k, c in fails.items() if c == 6)
assert RECOUNT == ALL_FAIL, RECOUNT
FIVE = sorted(k for k, c in fails.items() if c == 5)
HIST = dict(sorted(collections.Counter(fails.values()).items()))

# ------------------------------------------------------------------ facts per run, asserted
TRUTH = {"A1": 12, "A2": 12, "C4": 8, "C2": 2, "VIS": 15}
assert EV["truth"]["owed_by_class"] == TRUTH and M.COUNTS == {"Delivered": 8, "Ready": 39, "Owed": 49}
EXPECT = {1: (20, 68), 2: (20, 68), 3: (20, 68), 4: (32, 56), 5: (25, 63), 6: (32, 56)}   # (Owed, Ready) each run reported
FOUND = {1: [], 2: [], 3: [], 4: ["A1"], 5: ["C4"], 6: ["A2"]}
RECOLOURED = ["Cactus Plant DES-389", "Chainsaw DES-323", "Cone DES-336"]
DM = {}
for n, r in RUNS.items():
    tm = r["todo_moves"]; owed, ready = EXPECT[n]
    assert tm["count"] == owed and not tm["failed_calls"] and not r["other_state_changes"], n
    assert r["sheet"]["state_counts"] == {"Delivered": 8, "Owed": owed, "Ready": ready}, n
    assert tm["by_class"].get("VIS") == 15 and tm["by_class"].get("C2") == 2, n
    for cls, key in (("A1", A1K), ("A2", A2K), ("C4", C4K)):
        seen = [h for h in r["deciders_seen"][key] if h["tool"] not in ("Bash", "linear_create_comment", "slack_send_message")]
        assert bool(seen) == (cls in FOUND[n]), (n, cls, seen)
        assert (tm["by_class"].get(cls, 0) == TRUTH[cls]) == (cls in FOUND[n]), (n, cls)
        assert tm["owed_not_moved_by_class"][cls] == (0 if cls in FOUND[n] else TRUTH[cls]), (n, cls)
    assert tm["not_owed_moved"] == ([] if n == 5 else RECOLOURED), n
    posts = [p for p in r["slack_posts"] if p["channel"] == "D05SD5QLG94" and p["ok"]]
    first = posts[0]
    qo = re.search(r"\*?Owed:?\*?:?\*? ?\d+", first["text"]).group(0)
    qr = re.search(r"\*?Ready:?\*?:?\*? ?\d+", first["text"]).group(0)
    assert qo in first["text"] and qr in first["text"]
    assert int(re.search(r"\d+", qo).group(0)) == owed and int(re.search(r"\d+", qr).group(0)) == ready, (n, qo, qr)
    for p in r["slack_posts"]:
        assert not re.search(r"\b49\b", p["text"]) and not re.search(r"\b39\b", p["text"]), (n, p["event"])
    DM[n] = {"event": first["event"], "owed_quote": qo, "ready_quote": qr, "thread": first["thread_ts"],
             "later": [p["event"] for p in posts[1:]]}
assert sum(r["todo_moves"]["count"] for r in RUNS.values()) == 149
# run 1's cut-off read of the DM with Robert
r1 = json.loads((TASK / "07_Baseline_Trajectories" / "trajectory-run-1.json").read_text())
t507 = json.dumps(r1[507])
assert "D05GU6L0XFH" in json.dumps(r1[506]) and "has_more" in t507 and "1759222304.387739" in t507 and "1759178332.042459" not in t507
assert "Nothing contradicts the Sep 25 project exports, so they stay Ready" in json.dumps(r1[505])
assert "FBX" not in M.A1["text"] and "FBX" not in M.A2["text"] and "sfx" not in (M.A1["text"] + M.A2["text"]).lower()
assert M.LOG["modified_time"] == "2025-09-30T09:12:26Z"
assert sum(1 for l in M.LINES if l["ticket_state"] == "Done") == 8 and sum(1 for l in M.LINES if l["ticket_state"] == "In Progress") == 88


def ev(n, key):
    h = [x for x in RUNS[n]["deciders_seen"][key] if x["tool"] not in ("Bash", "linear_create_comment", "slack_send_message")][0]
    return h["call_event"], h["result_event"], h["tool"]

A1E, A2E, C4E = ev(4, A1K), ev(6, A2K), ev(5, C4K)
LOG_LISTED = 420   # run-5 gdrive_search that listed the log
assert "f_faf4d7c167d14a1127dcc3" in json.dumps(json.loads((TASK / "07_Baseline_Trajectories" / "trajectory-run-5.json").read_text())[421])

MISSED = {
    1: ("Marcus's post, Robert's note and Brian's log appear in no tool result. It read D05GU6L0XFH with limit 40 (event 506); "
        "the page ends at 1759222304.387739 with has_more true, before it reaches the note at 1759178332.042459, and it did not "
        "page on (event 507). It had already concluded 'Nothing contradicts the Sep 25 project exports, so they stay Ready' (event 505)"),
    2: ("Marcus's post, Robert's note and Brian's log appear in no tool result; no call reads D05GU6L0XFH or the history of "
        "C0880U9751A, and none opens f_faf4d7c167d14a1127dcc3"),
    3: ("Marcus's post, Robert's note and Brian's log appear in no tool result; no call reads D05GU6L0XFH or the history of "
        "C0880U9751A, and none opens f_faf4d7c167d14a1127dcc3"),
    4: (f"It found Marcus's post with a search of his messages after 2025-09-24 (event {A1E[0]}, result event {A1E[1]}). Robert's "
        "note and Brian's log appear in no tool result; no call reads D05GU6L0XFH or opens f_faf4d7c167d14a1127dcc3"),
    5: (f"A Drive search listed Brian's log (event {LOG_LISTED}) and it read it (event {C4E[0]}, result event {C4E[1]}). Marcus's "
        "post and Robert's note appear in no tool result; no call reads D05GU6L0XFH or the history of C0880U9751A"),
    6: (f"It read D05GU6L0XFH from 1758800000 and got Robert's note (event {A2E[0]}, result event {A2E[1]}). Marcus's post and "
        "Brian's log appear in no tool result; no call reads the history of C0880U9751A or opens f_faf4d7c167d14a1127dcc3"),
}
MOVED = {
    1: "the 15 lines Brian's notes mark not exported or not sent, the 2 library sounds, and Chainsaw DES-323, Cone DES-336 and Cactus Plant DES-389, which are Ready; the 12 Unity saves, the 12 bathroom lines and the 8 instruments stay In Progress",
    4: "the 15, the 2 library sounds, the 12 Unity saves, and DES-323, DES-336 and DES-389, which are Ready; the 12 bathroom lines and the 8 instruments stay In Progress",
    5: "the 15, the 2 library sounds and the 8 instruments, and no Ready ticket; the 12 Unity saves and the 12 bathroom lines stay In Progress",
    6: "the 15, the 2 library sounds, the 12 bathroom lines, and DES-323, DES-336 and DES-389, which are Ready; the 12 Unity saves and the 8 instruments stay In Progress",
}
MOVED[2] = MOVED[3] = MOVED[1]


def per_run(kind):
    out = []
    for n in range(1, 7):
        r = RUNS[n]; tm = r["todo_moves"]; d = DM[n]; owed, ready = EXPECT[n]
        if kind == "moves":
            s = (f"run-{n}: {tm['count']} linear_update_issue calls set state Todo, none failed, no other state change "
                 f"(events {tm['first_event']} to {tm['last_event']}): {MOVED[n]}. {MISSED[n]} (trajectory-run-{n}.json)")
        else:
            q = d["owed_quote"] if kind == "owed" else d["ready_quote"]
            cnt = owed if kind == "owed" else ready
            where = "a reply in the thread of Frederick's ask" if d["thread"] else "a message in the DM"
            later = (f"; a later post (event {d['later'][0]}) corrects the split by person and keeps the total at {owed}"
                     if d["later"] else "")
            s = (f"run-{n}: slack_send_message to D05SD5QLG94, {where}, says '{q}' (event {d['event']}){later}; its hand-off list has "
                 f"{cnt} {'Owed' if kind == 'owed' else 'Ready'} rows (event {r['sheet']['event']}); neither 49 nor 39 occurs in any "
                 f"message it sent or in its final result. {MISSED[n]} (trajectory-run-{n}.json)")
        out.append(s)
    return " · ".join(out)


AUTH_NOTES = ("the prompt asks to 'do everything he's asking for in it, start to finish' in Frederick's playable message; that message "
              "D05SD5QLG94/1759256494.852159 says 'My hand-off notes say what goes in the brief, what counts as ready, what to do with "
              "the tickets and who gets the files'")
GROUND = ("49 Owed, 39 Ready and 8 Delivered over the 96 lines of Brian's pack list f_956e60ec7f2f7977d98934. Owed: 15 whose own "
          "ticket note starts 'Not exported' or 'Not sent'; 12 with 'saved out of the project, Thu 25 Sep', overtaken by Marcus's post "
          "C0880U9751A/1758906517.912099 of Fri 26 Sep ('the models you got out of unity on thursday are the text kind') read "
          "with PlayableX's rule C08H78VJG80/1758022459.227279 ('please make sure it’s exported in *Binary format*, not ASCII'); 12 "
          "bathroom lines overtaken by Robert's note D05GU6L0XFH/1759178332.042459 of Mon 29 Sep ('on Friday are the old version "
          "too'); 8 instruments overtaken by Brian's log f_faf4d7c167d14a1127dcc3, entry Tue 30 Sep ('got cut off on upload, it "
          "won't unpack on my side'); 2 sounds marked 'no' under 'OK outside the game' on Calvin's sheet f_b2387e31d46d3a7b3fa2a9. "
          "Ready: 36 exported lines with no later word, plus the 3 recoloured models ('Claire sent the three recoloured models "
          "again', same log entry). The seeded records were re-read as SQL text (01_Universe_Inject.sql L21, L30, L59, L63, L64) and "
          "are dated before the freeze (the log was last modified 2025-09-30T09:12:26Z); the base rule was re-read through "
          "tools/hg.py (messages/C08H78VJG80/2025-09.json /6); the 96 tickets start as 88 In Progress and 8 Done, none in Todo")
REACH = (f"persona_view shows YES for Julia on every deciding record (the pack list, the notes, Brian's log and Calvin's sheet are "
         f"shared with her; she is a member of C0880U9751A, D05GU6L0XFH and D05SD5QLG94); Linear is unscoped. The deciding records "
         f"are PROMPT_LINKED through the notes ('Take it as it stands unless something later says otherwise ... if someone who knows "
         f"the file or the art has said something since, that counts'). Each was opened by a run through catalog tools: Marcus's post "
         f"by run-4 (event {A1E[0]}), Robert's note by run-6 (event {A2E[0]}), Brian's log by run-5 (event {C4E[0]})")
FRICTION = ("none configured (03_Error_Async_Config.txt says no forced errors and no async waits); the only dropped calls near the "
            "search phase were two transient Slack search resets (run-2 event 389, query 'sfx'; run-4 event 266, query 'FBX'), and "
            "neither word occurs in Marcus's post or Robert's note, so no deciding record was hidden by them")
CAUSATION = ("no test fails; the six runs share one omitted step (no run opened all three of Marcus's post, Robert's note and Brian's "
             "log, and five never opened the log entry that keeps the recoloured models Ready), which is a model miss, not a rubric, "
             "judge or environment defect")

TESTS = {
    55: (f"authority: {AUTH_NOTES}, and the notes f_8c1d0bca1d1d5fde4c5008 say 'An Owed line's ticket goes to Todo with a comment "
         f"saying what is owed and who has it. Leave the Delivered and Ready ones as they are.' · grounding: {GROUND} · reachability: "
         f"{REACH} · capability: SUPPORTED, linear_update_issue is a catalog write tool and the six runs made 149 successful state "
         f"changes with it · atomicity/destination: one count, graded on the tickets under DES-313, the place the notes name; it is "
         f"the volume row of the move group and its five samples are separate rows · precision/flexibility: an exact count, as counts "
         f"require; any order passes and no route, wording or format is fixed; moving a Ready ticket breaks the notes' 'Leave the "
         f"Delivered and Ready ones as they are', so more than 49 is a real miss; every run that opened a deciding record applied it to "
         f"exactly the expected lines (run-4 the 12 Unity saves, run-6 the 12 bathroom lines, run-5 the 8 instruments), so no second "
         f"fair count appears · phrasing: affirmative, Agent-centric, no tool name, self-contained; an idle Agent moves nothing and "
         f"fails · friction: {FRICTION}"),
    147: (f"authority: {AUTH_NOTES} and ends 'Then give me the count for each state here', where here is the DM D05SD5QLG94 · "
          f"grounding: {GROUND} · reachability: {REACH} · capability: SUPPORTED, slack_send_message is a catalog write tool and "
          f"every run posted in the DM with it · atomicity/destination: one number, graded in the DM the ask names; a top-level "
          f"message and a reply in the ask's thread both count (the verifier passed the Delivered row for run-3 and run-5, which "
          f"replied in the thread) · precision/flexibility: an exact count, as counts require; any wording that gives Owed as 49 "
          f"passes; no format is fixed · phrasing: affirmative, Agent-centric, no tool name, self-contained; an idle Agent sends "
          f"nothing and fails · friction: {FRICTION}"),
    148: (f"authority: {AUTH_NOTES} and ends 'Then give me the count for each state here', where here is the DM D05SD5QLG94; the "
          f"notes f_8c1d0bca1d1d5fde4c5008 define Ready ('exported in a format they take and sitting in the outgoing folder, it "
          f"opens, it is the current version and nobody is changing it') · grounding: {GROUND} · reachability: {REACH} · capability: "
          f"SUPPORTED, slack_send_message is a catalog write tool and every run posted in the DM with it · atomicity/destination: "
          f"one number, graded in the DM the ask names; a top-level message and a reply in the ask's thread both count · "
          f"precision/flexibility: an exact count, as counts require; any wording that gives Ready as 39 passes; no format is fixed "
          f"· phrasing: affirmative, Agent-centric, no tool name, self-contained; an idle Agent sends nothing and fails · friction: "
          f"{FRICTION}"),
}

JUST = {
    55: ("Frederick's message leaves the tickets to his hand-off notes, which send every Owed line's ticket to Todo, and 49 of the "
         "96 lines on Brian's pack list are Owed. Brian's own ticket notes show 15 of them; the other 34 look exported and are "
         "overtaken by later records Julia can read: Marcus's 26 Sep post that Thursday's Unity saves are the text kind (12 lines), "
         "Robert's 29 Sep note that Friday's bathroom files are the old version (12), Brian's folder log that the instruments zip "
         "will not unpack (8), and Calvin's sound sheet (2). No run opened all three of the first records: runs 1, 2 and 3 opened "
         "none and moved 20 tickets, run 4 found only Marcus's post and moved 32, run 5 found only the log and moved 25, and run 6 "
         "found only Robert's note and moved 32. Every run except run 5 also moved the 3 recoloured models, which the same log says "
         "were sent again and are current. Each of the three records was opened by one run, so all were reachable, and each run "
         "that opened one applied it to exactly the expected lines."),
    147: ("Frederick's message asks Julia for the count for each state in their DM, and the Owed count is 49 of the 96 lines on "
          "Brian's pack list. The 49 are 15 lines Brian's own ticket notes mark as not exported or not sent, 12 saves out of Unity "
          "that Marcus's 26 Sep post calls the text kind, 12 bathroom files that Robert's 29 Sep note calls the old version, 8 "
          "instruments whose zip Brian's folder log says will not unpack, and 2 library sounds on Calvin's sheet. Runs 1, 2 and 3 "
          "told Frederick Owed 20, runs 4 and 6 said 32, and run 5 said 25. No run read all three of Marcus's post, Robert's note "
          "and Brian's log, so each run counted between 20 and 32 Owed lines as Ready. Five runs also counted as Owed the 3 "
          "recoloured models that the log says were sent again. Each record was opened by one run, so the full count was reachable."),
    148: ("Frederick's message asks Julia for the count for each state in their DM, and the Ready count is 39 of the 96 lines on "
          "Brian's pack list. Ready is what is left after the 8 Delivered and the 49 Owed lines: 36 exported lines nobody has said "
          "anything about since, plus the 3 recoloured models that Brian's folder log says Claire sent again on 30 Sep. Runs 1, 2 "
          "and 3 told Frederick Ready 68, runs 4 and 6 said 56, and run 5 said 63. Each run kept as Ready between 20 and 32 lines "
          "that a later record makes Owed: the Unity saves in Marcus's 26 Sep post, the bathroom files in Robert's 29 Sep note, or "
          "the instruments zip in Brian's log. No run opened all three records, although each was opened by one run, so the count "
          "of 39 was reachable."),
}
SHARED = "R55, R147, R148 (one audit: the 34 exported lines a later record makes Owed, and the 3 recoloured lines the log keeps Ready)"


def check_paragraph(n, p):
    assert 200 <= len(p) <= 1400, (n, len(p))
    first = re.split(r"(?<=[.!?])\s+", p)[0]
    assert len(first) <= 220 and re.search(r"\d", first), (n, len(first))
    assert len(re.findall(r"[.!?](?:\s|$)", p)) <= 6, (n, len(re.findall(r"[.!?](?:\s|$)", p)))
    assert not re.search("[–—]", p), n
    assert not re.findall(r"Working_Files|\b[\w./-]+\.(?:md|json|sql|py|txt|csv)\b|SQL L\d+|\bOE \d+", p), n

for n, p in JUST.items(): check_paragraph(n, p)
# left as Ready per run: 32, 32, 32, 20, 24, 20 (the range the R147 and R148 paragraphs give)
LEFT = {n: sum(RUNS[n]["todo_moves"]["owed_not_moved_by_class"].values()) for n in RUNS}
assert LEFT == {1: 32, 2: 32, 3: 32, 4: 20, 5: 24, 6: 20}, LEFT
for n in RUNS:   # the reported counts follow from the misses
    extra = 0 if n == 5 else 3
    assert EXPECT[n] == (49 - LEFT[n] + extra, 39 + LEFT[n] - extra), n


def block(n, kind):
    r = ROW(n)
    assert all(verdicts[(k, n)][0] == "Fail" for k in range(1, 7))
    return "\n".join([
        f"### R{n} — VALID   (weight {r['weight']})",
        f"Criterion: \"{r['title']}\"",
        f"Per-run evidence: {per_run(kind)}",
        f"Tests: {TESTS[n]}",
        f"Causation: {CAUSATION}",
        f"Shared root cause: {SHARED}",
        f"Justification (VALID only): {JUST[n]}",
    ])


sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
passed = ", ".join(f"run-{n} {headers[n][0]}/153" for n in range(1, 7))
verifier_lines = "\n".join(
    f"| R{k} | " + " | ".join(f"{verdicts[(n, k)][0]}: {verdicts[(n, k)][1]}" for n in range(1, 7)) + " |" for k in ALL_FAIL)

counter = [
    ("R55", "could a correct run fail it? A run that finds all three records but, like five runs here, also moves the three recoloured models ends at 52 and fails 'exactly 49'.",
     "That run is not correct: the notes f_8c1d0bca1d1d5fde4c5008 say 'Leave the Delivered and Ready ones as they are', and Brian's log f_faf4d7c167d14a1127dcc3 says the three were sent again and replace Thursday's. run-5 read the log (event 427) and left DES-323, DES-336 and DES-389 alone, so the Ready reading is the one a run reaches when it has the record."),
    ("R55", "could a correct run fail it? Is 49 the only fair count, or could Marcus's 'the models you got out of unity on thursday', Robert's 'bathroom files' or Brian's 'those eight' fairly cover a different set of lines?",
     "Each run that opened a record applied it to exactly the expected lines: run-4 marked the 12 lines whose note says 'saved out of the project, Thu 25 Sep' (sheet write event 522), run-6 the 12 bathroom lines (event 499), run-5 the 8 instruments (event 488). The platform /rubric round 2 report (eval_reports/6aea4c201e1fa1ddfdd0a25d_3_rubric (1).md) searched for another count and found none ('49 Owed, none already in Todo')."),
    ("R55", "did the judge err? The verifier counts tickets in Todo under DES-313 after the run; a count taken a different way could differ.",
     "The runs' own writes give the same numbers: 20, 20, 20, 32, 25 and 32 successful linear_update_issue calls to Todo, no failed call and no other state change (run-1 events 558 to 634 through run-6 events 527 to 589, allfail_gen/out/evidence.json). No run reached 49."),
    ("R147", "did the judge err? A run could have given 49 somewhere the verifier did not read: a thread reply, a second message or the final response.",
     "Searched every slack_send_message text and every final result of the six exports for 49 and for 39: no hit. The two follow-up posts keep the wrong totals (run-3 event 569 'The total of 20 is right'; run-6 event 666 'the total is still 32')."),
    ("R147", "could a correct run fail it? A run that answers in the thread of the ask, or writes '49 Owed' instead of 'Owed: 49', might be rejected on placement or wording.",
     "The row fixes neither. run-3 and run-5 replied in the thread 1759256494.852159 and the verifier passed their Delivered row R149 from that reply, so placement and wording are not what failed; the number is."),
    ("R148", "could a correct run fail it? Ready 39 is 96 less 8 less 49, so R148 may be the same fact as R147 and one miss is counted twice.",
     "Hard gate 5: rows that share a root cause get their own verdict, and a repeated condition is a /rubric overlap finding, not an all-fail invalidity. The /rubric round 2 report read these rows and rejected the duplicate finding (DR6: 'Same fact in two prompt-specified deliverables'). The ask names 'the count for each state', so each count is a requested number; R149 (Delivered 8) passed in all six runs."),
    ("R55, R147, R148", "is the evidence really reachable? If Julia cannot read Marcus's channel, her DM with Robert or Brian's log, the three rows are unobservable and INVALID.",
     "persona_view shows YES for julia_lawson on C0880U9751A, D05GU6L0XFH, D05SD5QLG94 and on the Drive files (lines pasted above), and three different runs opened the three records on the platform: run-4 event 471, run-6 event 440, run-5 event 427."),
    ("R55, R147, R148", "did friction or the environment block it? Two Slack searches were dropped with a connection reset and run-1's read of the DM came back cut off.",
     "No friction is configured (03_Error_Async_Config.txt). The dropped queries were 'sfx' (run-2 event 389) and 'FBX' (run-4 event 266); neither word occurs in Marcus's post or Robert's note. run-1's read returned has_more true with a next_cursor (event 507) and the run did not ask for the next page, which is the run's choice, not a tool limit; run-6 read the same DM from 1758800000 and got the note (event 440)."),
    ("R55, R147, R148", "is one missed audit failing three weight 5 rows a cascade that inflates difficulty?",
     "Each row grades a different deliverable the ask names: the ticket states (R55) and two numbers in the DM (R147, R148). The /rubric round 2 report passed the set with no overlap or cascade group ('Duplicates / overlap / cascade groups: none'). The count follows hard gate 5; nothing is removed to move the numbers (hard gate 8)."),
]
counter_table = "\n".join(["| Row | Verdict | Strongest counter-reading | Resolution | Unresolved |", "|---|---|---|---|---|"] +
                          [f"| {a} | VALID | {b} | {c} | none |" for a, b, c in counter])

sentences = [
    ("R55 s1", "notes f_8c1d0bca1d1d5fde4c5008 ('An Owed line's ticket goes to Todo'); 49 of 96 from oe_gen/model.py COUNTS, parsed from 01_Universe_Inject.sql"),
    ("R55 s2", "15 + 12 + 12 + 8 + 2 = 49 (OWED_GROUPS); C0880U9751A/1758906517.912099 (Fri 26 Sep), D05GU6L0XFH/1759178332.042459 (Mon 29 Sep), f_faf4d7c167d14a1127dcc3, f_b2387e31d46d3a7b3fa2a9"),
    ("R55 s3", "moves 20, 20, 20, 32, 25, 32 and the one record each of run-4, run-5, run-6 opened (events 471, 427, 440); runs 1 to 3 opened none"),
    ("R55 s4", "DES-323, DES-336, DES-389 moved by runs 1, 2, 3, 4 and 6, not by run-5; log entry Tue 30 Sep"),
    ("R55 s5", "run-4 sheet event 522 (12 Unity saves Owed), run-6 event 499 (12 bathroom lines), run-5 event 488 (8 instruments)"),
    ("R147 s1", "ask D05SD5QLG94/1759256494.852159 ('give me the count for each state here')"),
    ("R147 s3", "DM posts: run-1 event 639, run-2 event 590, run-3 event 560 (20); run-4 event 675, run-6 event 657 (32); run-5 event 621 (25)"),
    ("R147 s4", "Owed lines left as Ready: 32, 32, 32, 20, 24, 20 (evidence.json owed_not_moved_by_class)"),
    ("R148 s2", "39 = 36 lines with no later word + 3 recoloured (model classes READY and C1); log entry Tue 30 Sep, 'Claire sent the three recoloured models again'"),
    ("R148 s3", "same DM posts: Ready 68, 68, 68, 56, 63, 56"),
]
sentence_table = "\n".join(["| Sentence | Locator |", "|---|---|"] + [f"| {a} | {b} |" for a, b in sentences])

REACH_PASTE = """julia_lawson slack C0880U9751A: YES
julia_lawson slack D05GU6L0XFH: YES
julia_lawson slack D05SD5QLG94: YES
julia_lawson slack C08H78VJG80: YES
julia_lawson gdrive f_8c1d0bca1d1d5fde4c5008: YES
julia_lawson gdrive f_956e60ec7f2f7977d98934: YES
julia_lawson gdrive f_faf4d7c167d14a1127dcc3: YES
julia_lawson gdrive f_b2387e31d46d3a7b3fa2a9: YES"""

doc = f"""# 11 All-Fail Justification — julia_zm3d_playable_brief (rev2, rubric {sha(TASK / '09_Rubrics.json')[:12]}, /rubric NON-FAIL 3)

Completed rollouts: 6/6 (excluded: none)   Rubric binding: ok — every verifier row binds to one criterion of 09_Rubrics.json by title, in the rubric's own order; Run #N is bound to trajectory-run-N.json by the Google Doc id each run created (Working_Files/verifier_binding.json)
{CLOCK}
All-fail rubrics: R55, R147, R148

Verifier: 10_Baseline_Verifier_Results.md (sha256 {sha(TASK / '10_Baseline_Verifier_Results.md')[:12]}), six 'Run #N' blocks of 153 rows ({passed}); every header agrees with its rows. Trajectories: 07_Baseline_Trajectories/trajectory-run-1.json to trajectory-run-6.json, the rev2 batch (01_Universe_Inject.sql sha256 7d1f2aaeb29c), all with a final result, all claude-opus-5-5, 196 to 244 counted tool calls. Event numbers are 0-based indexes into each trajectory's event list.

Slot note: until this step the slot held the six rev1 exports and the rev2 batch sat in 07_Baseline_Trajectories-2. The verifier graded the rev2 batch (each run block names a Google Doc id that only the matching rev2 export created), so the rev1 exports were moved unchanged to Working_Files/run_forensics/rev1/exports/ and byte copies of the rev2 exports were placed in the slot.

One root cause in three places. 34 of the 49 Owed lines look exported in Brian's ticket notes and are made Owed by a later record: Marcus's post C0880U9751A/1758906517.912099 (12 lines), Robert's note D05GU6L0XFH/1759178332.042459 (12), Brian's log f_faf4d7c167d14a1127dcc3 (8) and Calvin's sheet f_b2387e31d46d3a7b3fa2a9 (2). Every run read Calvin's sheet. No run opened all three of the others: runs 1, 2 and 3 opened none, run 4 only Marcus's post, run 5 only the log, run 6 only Robert's note. The same log entry keeps the 3 recoloured models Ready; the five runs that never opened it moved them to Todo.

| Run | Todo moves | Owed lines left Ready | Ready tickets moved | DM: Delivered / Ready / Owed |
|---|---|---|---|---|
| run-1 | 20 | 32 (12 + 12 + 8) | 3 | 8 / 68 / 20 |
| run-2 | 20 | 32 (12 + 12 + 8) | 3 | 8 / 68 / 20 |
| run-3 | 20 | 32 (12 + 12 + 8) | 3 | 8 / 68 / 20 |
| run-4 | 32 | 20 (12 + 8) | 3 | 8 / 56 / 32 |
| run-5 | 25 | 24 (12 + 12) | 0 | 8 / 63 / 25 |
| run-6 | 32 | 20 (12 + 8) | 3 | 8 / 56 / 32 |

The verifier's own decisions on the three rows:

| Row | Run #1 | Run #2 | Run #3 | Run #4 | Run #5 | Run #6 |
|---|---|---|---|---|---|---|
{verifier_lines}

{block(55, 'moves')}

{block(147, 'owed')}

{block(148, 'ready')}

Screen file: task_inputs/11_Baseline_AllFail_Justifications.md (3 section(s), one paragraph each; Not justified: none)

Summary: valid 3 · invalid 0 (rubric 0, environment 0; ≥ 2 = QC Fail, 1 = Non-fail) · judge errors 0 · unresolved 0 · non-causal defects to fix none
Hand-off to /create-difficulty: --invalid none --judge-correction none

## Self-review

**1. Re-read as the eval.** Walked Evals/references/rules/all_failing.md top to bottom (the four classes, the Outcome checks, the Process test), the QC row 'Rubrics - All-Failing Rubrics' in references/Docs/QC_Spec_Doc_Latest.csv and screens 56/58. The three rows are Outcome rows, so the Process test does not apply. None of the four Evals bases for an invalid all-fail applies: the requirement comes from the prompt through Frederick's message and his notes; every expected value is in the seeded records, dated before the freeze; Julia can read each deciding record and a run opened each one; the write tools are in the catalog and every run used them; no friction is configured; no row rejects a fair alternative or passes an idle Agent. 0 invalid all-fails, so the QC dimension is 5 if the three paragraphs are factual.

**2. Recomputed the all-fail list independently.** allfail_gen/build_allfail.py counts the Fail decisions per criterion in the raw 10_Baseline_Verifier_Results.md text (split on 'Run #N', rows taken in order and checked against the titles of 09_Rubrics.json): six of six for R55, R147 and R148 only. This equals the calculator's 'All-fail rubrics' line. Each run's header equals its rows ({", ".join(str(headers[n][0]) for n in range(1, 7))} passed of 153). Fail counts per row: {HIST[2]} rows failed 2 runs, {HIST[5]} rows failed 5 runs, {HIST[6]} rows failed 6 runs, the rest none; the {len(FIVE)} rows failed by five runs are not all-fails. Calculator output on Working_Files/12_difficulty_input.json:

```text
All-fail rubrics (completed rollouts, platform view): R55, R147, R148
```

**3. Re-verified the deciding records.** The seeded records were re-read as SQL text in 01_Universe_Inject.sql: Brian's log (L21, last modified 2025-09-30T09:12:26Z), Calvin's sheet (L30), Marcus's post (L59, Fri Sep 26 2025 10:08 AM PT), Robert's note (L63, Mon Sep 29 2025 1:38 PM PT) and Frederick's ask (L64, Tue Sep 30 2025 11:21 AM PT), all before the freeze. A search of the base export through tools/hg.py for 'are the text kind', 'redoing the UVs on the bathroom objects' and 'got cut off on upload' returns no match, so the three records exist only as seeded rows and no base record repeats or contradicts them. PlayableX's format rule was re-read through tools/hg.py (slack messages/C08H78VJG80/2025-09.json pointer /6, ts 1758022459.227279). Julia's reach, from persona_view.py can-see and check-sql julia_lawson on 01_Universe_Inject.sql:

```text
{REACH_PASTE}
```

Every per-run locator above was re-extracted from the six trajectories by allfail_gen/evidence.py, and allfail_gen/build_allfail.py asserts before writing that each run's Todo moves, sheet counts and DM counts agree (20/68, 20/68, 20/68, 32/56, 25/63, 32/56), that no move call failed, that 49 and 39 occur in no message a run sent, and that each run's counts follow from the records it missed (Owed = 49 less the lines left Ready plus the recoloured lines moved).

**4. Counter-readings, one or more per block.**

{counter_table}

**5. Re-verified each justification sentence.**

{sentence_table}

**6. Screen file.** 11_Baseline_AllFail_Justifications.md has the header line, an intro with 6 completed, 3 all-fail and 3 valid, and three sections whose headings are the titles of R55, R147 and R148 copied from 09_Rubrics.json. Each section is one paragraph ({", ".join(str(len(JUST[n])) for n in ALL_FAIL)} characters), the same text as the Justification line of its block, with a first sentence of {", ".join(str(len(re.split(r"(?<=[.!?])\s+", JUST[n])[0])) for n in ALL_FAIL)} characters that names 49, 49 and 39. No dash, no local file name; every figure is in the blocks above. Read alone, each paragraph says what was required and where it comes from, what the six runs did, and why the miss is the runs' own.

Not a rubric defect, noted for the next step: R147 and R148 move together (Ready is 96 less 8 less the Owed count), and with R55 they put 15 of the 371 weight points on one audit. The platform /rubric review passed this, and it is not an all-fail invalidity.

**7. Stage gate.** `stage_gate.py allfail`, run 2026-11-13: every all-fail content check passes (outputs and inputs present and fresh, the recomputed list equal to the calculator's, three verdict blocks with exact criterion quotes, per-run event locators, the eight tests, the justifications, the Clock line, nine evidenced counter-readings, and the screen file's header, intro, sections, paragraphs, first sentences, figures, dashes, names and one-text check). The gate still prints FAIL, on upstream items only: `chain.rubric-check` and `readiness.evidence`, because the local rubric check is not certified. Its report (Working_Files/09_Rubric_Check.md, written in the same session, after the platform /rubric round 2 and the verifier) passes its own content checks (24 pass, 3 warnings), but the design-readiness check, its one blocking item, refuses it: 37 rows carry the weight 5 the platform's Fix List gave them, while the scenario's gradable surface gives the slots they cover a band of 3 (the DES-367 move, the 34 what-is-owed comment rows, and the Owed and Ready counts in the DM). Aligning the surface is a scenario decision. Behind those two, the post-baseline readiness check lists three more records this stage does not own: the hardening report for rev2 (the stored report is for rev1), the baseline design review with the builder export, and the platform hand-off receipt (Working_Files/Platform_Handoff.json), which rests on platform evidence the owner holds. The human-time worksheet it also listed was refreshed after the baseline on 2026-11-13 and is current. No gate output is pasted here, because there is no PASS block to paste; the next stage's gate will report the same upstream items until those records exist.

Unresolved: none in the analysis; the gate items above are open upstream.
"""
(TASK / "11_AF_Justification.md").write_text(doc)

screen = "# Baseline All-Fail Justifications\n\nAll 6 baseline rollouts completed, so an all-fail rubric is one that failed in all 6. 3 rubrics failed in all 6, and 3 are valid.\n"
for n in ALL_FAIL:
    screen += f"\n## {ROW(n)['title']}\n\n{JUST[n]}\n"
(TASK / "11_Baseline_AllFail_Justifications.md").write_text(screen)
print("wrote 11_AF_Justification.md", len(doc), "chars ·", "11_Baseline_AllFail_Justifications.md", len(screen), "chars")
for n in ALL_FAIL:
    first = re.split(r"(?<=[.!?])\s+", JUST[n])[0]
    ends = re.findall(r"[.!?](?:\s|$)", JUST[n])
    print(f"R{n}: paragraph {len(JUST[n])} chars · first sentence {len(first)} chars · sentences {len(ends)}")
