#!/usr/bin/env python3
"""Builds 11_AF_Justification.md (workbook) and 11_Baseline_AllFail_Justifications.md (screen file) from the verifier
copy, the six trajectories and 09_Rubrics.json. Every per-run locator is re-extracted here, not carried from notes."""
import json, os, re, subprocess, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); TI = os.path.dirname(WF); WS = os.path.abspath(os.path.join(TI, "..", ".."))
RUB = json.load(open(os.path.join(TI, "09_Rubrics.json")))
T = lambda n: RUB[n - 1]["title"]
W = lambda n: RUB[n - 1]["weight"]

# ---- recompute the all-fail list from the raw verifier text (independent of the calculator)
vt = open(os.path.join(TI, "10_Baseline_Verifier_Results.md")).read()
parts = re.split(r"(?m)^Run\s*#\s*(\d+)\s*$", vt)
norm = lambda s: re.sub(r"\s+", " ", s).strip()
title_ix = {norm(c["title"]): i + 1 for i, c in enumerate(RUB)}
fails, heads = {}, {}
for k in range(1, len(parts), 2):
    n, block = int(parts[k]), parts[k + 1]
    heads[n] = int(re.search(r"(\d+)/184 criteria passed", block).group(1))
    rows = [l.split("\t") for l in block.splitlines() if "\t" in l and l.split("\t")[1].strip() in ("Pass", "Fail")]
    assert len(rows) == 184, (n, len(rows))
    assert sum(r[1].strip() == "Pass" for r in rows) == heads[n]
    for r in rows:
        if r[1].strip() == "Fail":
            fails.setdefault(title_ix[norm(r[0])], set()).add(n)
ALLFAIL = sorted(i for i, s in fails.items() if len(s) == 6)
calc = json.loads(subprocess.run(["python3", "Task_Authoring/tools/difficulty_stats.py", "--task-dir", "Task_Authoring/task_inputs",
                                  "Task_Authoring/task_inputs/Working_Files/12_difficulty_input.json", "--json"], cwd=WS, capture_output=True, text=True,
                                 env=dict(os.environ, TASK_AUTHORING_TASK_DIR=TI)).stdout)
assert sorted(int(x[1:]) for x in calc["all_fail_rubrics"]) == ALLFAIL, (calc["all_fail_rubrics"], ALLFAIL)
PARTIAL = {i: sorted(s) for i, s in fails.items() if len(s) < 6}

# ---- per-run facts from the trajectories (event = index in the export's event list)
TK = ["ZOM-571", "ZOM-572", "ZOM-573", "ZOM-574", "ZOM-581", "ZOM-584"]
F = {}
for n in range(1, 7):
    d = json.load(open(os.path.join(TI, "07_Baseline_Trajectories", f"trajectory-run-{n}.json")))
    R = {"gh": [], "upd": {}, "cmt": {}, "c38": None, "s38": None, "dm": None, "slide": None, "saw473": None}
    for i, e in enumerate(d):
        if e.get("type") == "user" and R["saw473"] is None and "Merge pull request #473" in json.dumps(e.get("message", {}).get("content", "")):
            R["saw473"] = i      # the #builds post of the main build that merged #473, returned to the run
        if e.get("type") != "assistant":
            continue
        for c in e["message"].get("content", []):
            if c.get("type") != "tool_use":
                continue
            nm, inp = c["name"].split("__")[-1], c["input"]; s = json.dumps(inp)
            if nm.startswith("github_"):
                arg = inp.get("pullNumber") or inp.get("pull_number") or inp.get("query") or inp.get("state") or ""
                R["gh"].append((i, nm, str(arg)))
            for k in TK:
                if re.search(k + r"\b", s):
                    if nm == "linear_update_issue":
                        assert not any(x in inp for x in ("state", "stateId", "status")), (n, k, inp)
                        R["upd"][k] = (i, inp.get("parentId"))
                    if nm == "linear_create_comment":
                        R["cmt"][k] = (i, inp["body"])
            if nm == "linear_create_issue" and "Pass progress bar" in s:
                R["c38"] = (i, inp.get("state"))
            if nm == "gsheets_values_update" and "Pass progress bar fills before the tokens arrive" in s:
                m = re.search(r'Pass progress bar fills before the tokens arrive", "Season Pass", "([^"]+)"', s); R["s38"] = (i, m.group(1))
            if nm == "slack_send_message" and R["dm"] is None:
                t = inp.get("message") or inp.get("text"); R["dm"] = (i, int(re.search(r"Waiting on QA:\W*(\d+)", t).group(1)), int(re.search(r"Waiting on a fix:\W*(\d+)", t).group(1)))
            if nm == "gslides_batch_update":
                R["slide"] = (i, int(re.search(r"aiting on QA: (\d+)", s).group(1)), int(re.search(r"aiting on a fix: (\d+)", s).group(1)))
    assert all(k in R["upd"] and k in R["cmt"] for k in TK) and R["c38"] and R["s38"] and R["dm"] and R["slide"] and R["saw473"] is not None, n
    assert not any(x in nm for _, nm, _ in R["gh"] for x in ("comments", "reviews")), n      # no run read a PR's review or conversation comments
    F[n] = R
SEEDED = {"ZOM-571": "In Validation", "ZOM-574": "In Validation", "ZOM-581": "In Validation", "ZOM-572": "Todo", "ZOM-573": "Todo", "ZOM-584": "Todo"}
def stat(body): return "Waiting on QA" if "Waiting on QA" in body else "Waiting on a fix"
def gh(n): return f"a #builds result it read shows 'Merge pull request #473' into main (event {F[n]['saw473']}); GitHub reads: " + ", ".join(f"{nm} {a} (event {i})".replace("  ", " ") for i, nm, a in F[n]["gh"]) + "; no review-comment or conversation-comment read"
def ev(n, text): return f"run-{n}: {text} (trajectory-run-{n}.json)"

NOTE = "comment_faaa792418a942cd40be046d8d217a7d"
A472, A475, O473 = "harmonygames-Games/match3d#472#rc_1", "harmonygames-Games/match3d#475#rc_1", "harmonygames-Games/match3d#473#c_2"
SRC = {
 "A": (A472, "Arthur Blake's review comment on pull request #472 (2025-09-30T15:53:40Z): 'Flow sheet has the season pass icon restart and the event bar starting under the gift popup against this PR. Neither is in this diff.'", "#472"),
 "B": (A475, "Arthur Blake's review comment on pull request #475 (2025-09-30T16:09:50Z): 'Don't see the pack sound stop anywhere in here. Still needs doing.'", "#475"),
 "C": (O473, "Oliver Brooks's comment on pull request #473 (2025-09-30T15:42:10Z), merged into main Sep 30 2025: 'this also has four fixes: the pass start popup coming back after every level, the pass bar filling before the tokens land, the claim animation playing twice after the shop, and the freezer popup opening behind the pass popup.'", "#473"),
}
HAND = "The prompt hands the set-up to Brian ('set it all up as he asked: the children and report lines in Linear'), his DM D0770ET6WBW/1759264805.214409 says 'I left a note on the ticket about how I want it', and the note " + NOTE + " on ZOM-543 sets the rule"
def tests(group, rule, dest):
    rid, quote, pr = SRC[group] if group in SRC else (None, None, None)
    src = (f"{quote} ({rid}), a seeded github row read as SQL text, dated before the freeze" if rid else
           "the counts follow from the 39 statuses; the three deciding comments are " + ", ".join((A472, A475, O473)) + ", seeded github rows read as SQL text, dated before the freeze")
    reach = ("GitHub is unscoped for Calvin; the sheet's Fix column names #472 and #475, and the note's 'a fix for it is in main' sends the reader to the pull requests merged into main, where #473 sits; "
             "the review comments and conversation comments are returned by the catalog's github_get_pull_request_comments, github_get_pull_request_reviews and github_get_issue_comments; deciding record PROMPT_LINKED (the /rubric review passed it)")
    return (f"Tests: authority: {HAND} ({rule}) · grounding: {src} · reachability: {reach} · capability: SUPPORTED, {dest} · "
            "atomicity/destination: one condition, graded on the artifact Brian asked for · precision/flexibility: a discrete value; any wording with the meaning passes; no format is demanded · "
            "phrasing: affirmative, Agent-centric, no tool name; an idle Agent fails it · friction: none configured (Friction: none)")

B = []   # (rid, per-run lines, tests, causation, shared, justification, counter)
def add(rid, runs, tst, shared, just, counter):
    assert T(rid) and len(just) <= 1400 and len(just) >= 200, (rid, len(just))
    first = re.split(r"(?<=[.!?])\s+", just)[0]
    assert len(first) <= 220 and re.search(r"\d", first), (rid, len(first))
    assert len(re.findall(r"[.!?](?:\s|$)", just)) <= 6 and "—" not in just and "–" not in just, rid
    B.append((rid, runs, tst, shared, just, counter))

RULE_STATE = "'If its state does not match the status, put Done for Passed, In Validation for Waiting on QA, Todo for Waiting on a fix'"
RULE_NOTE = "'move that ticket under the child and leave a note with the status and why'"
RULE_STATUS = "'Waiting on QA: not passed, and a fix for it is in main that QA has not tried on a main build yet. Waiting on a fix: everything else'"
INTRO = "Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', "
def not_in(pr, who, what): return f"{who}'s review comment on {pr} says {what}"
ROWS_A = {"ZOM-571": ("Season Pass", "the season pass icon restart is not in that diff", 34, 78, 79), "ZOM-574": ("Collect & Win", "the event bar start is not in that diff", 40, 84, 85)}
ROWS_B = {"ZOM-581": ("Card packs", "the pack sound stop is not anywhere in it", 58, 104, 105)}
ROWS_C = {"ZOM-572": ("Season Pass", "the pass start popup coming back after every level", 36, 80, 81), "ZOM-573": ("Season Pass", "the claim animation playing twice after the shop", 38, 82, 83),
          "ZOM-584": ("Win Streak", "the freezer popup opening behind the pass popup", 64, 110, 111)}
for group, rows in (("A", ROWS_A), ("B", ROWS_B)):
    pr = SRC[group][2]
    for k, (area, what, r_state, r_status, r_reason) in rows.items():
        miss = f"All 6 runs read {pr} only as a merged pull request named in the sheet's Fix column and never opened its review comments, so they took the fix as merged."
        runs_s = " · ".join(ev(n, f"linear_update_issue on {k} sets only parentId {F[n]['upd'][k][1]}, no state (event {F[n]['upd'][k][0]}), so {k} stays {SEEDED[k]}; {gh(n)}") for n in F)
        add(r_state, runs_s, tests(group, RULE_STATE, "linear_update_issue is in the catalog and every run used it"), f"{pr} review comment: " + ", ".join(f"R{x}" for x in (r_state, r_status, r_reason)) + ", and the counts R175, R176, R180, R181",
            f"{k} had to end in Todo, because its fix is not in pull request {pr}. {INTRO}sets Todo for a report waiting on a fix, and {not_in(pr, 'Arthur Blake', what)}. {miss} Each run moved {k} under the {area} child without changing its state, so it stayed In Validation.",
            f"could a correct run fail it? A run that reads the review comment sets Todo and passes; the row accepts the state however it is reached. Judge check: every run's linear_update_issue on {k} carries no state key (run-1 event {F[1]['upd'][k][0]} to run-6 event {F[6]['upd'][k][0]}), so no run set Todo.")
        runs_c = " · ".join(ev(n, f"linear_create_comment on {k} gives '{stat(F[n]['cmt'][k][1])}' and the reason that the fix went into main with {pr} (event {F[n]['cmt'][k][0]}): '{F[n]['cmt'][k][1][:110]}'; {gh(n)}") for n in F)
        assert all(stat(F[n]["cmt"][k][1]) == "Waiting on QA" for n in F)
        add(r_status, runs_c, tests(group, RULE_NOTE + "; " + RULE_STATUS, "linear_create_comment is in the catalog and every run used it"), f"{pr} review comment: " + ", ".join(f"R{x}" for x in (r_state, r_status, r_reason)),
            f"The comment on {k} had to give the status Waiting on a fix, because pull request {pr} does not hold its fix. {INTRO}asks for a note with the status and why on each moved ticket, and {not_in(pr, 'Arthur Blake', what)}. {miss} Each run's comment on {k} gives Waiting on QA.",
            f"could a correct run fail it? The row accepts any wording that means waiting on a fix. Judge check: all six comment bodies on {k} say Waiting on QA (run-1 event {F[1]['cmt'][k][0]} to run-6 event {F[6]['cmt'][k][0]}); none says a fix is still needed.")
        add(r_reason, runs_c, tests(group, RULE_NOTE, "linear_create_comment is in the catalog and every run used it"), f"{pr} review comment: " + ", ".join(f"R{x}" for x in (r_state, r_status, r_reason)),
            f"The comment on {k} had to say that pull request {pr} does not hold its fix. {INTRO}asks for a note with the status and why on each moved ticket, and {not_in(pr, 'Arthur Blake', what)}. {miss} Each run's comment on {k} gives the opposite reason, that the fix is in main through {pr}.",
            f"could a correct run fail it? Any wording that says {pr} lacks the fix passes. Judge check: the six bodies each say the fix is in main via {pr} (run-2 event {F[2]['cmt'][k][0]}), the opposite of the row; a separate status row (R{r_status}) grades the label, so this is one condition.")
pr = "#473"
MISS_C = "The sheet's Fix cell for the row is blank and the note asks whether a fix is in main, so the merged pull requests had to be checked. All 6 runs read the #builds post that shows #473 merged into main, but none opened the comments on #473, so each took the blank cell as no fix."
for k, (area, what, r_state, r_status, r_reason) in ROWS_C.items():
    runs_s = " · ".join(ev(n, f"linear_update_issue on {k} sets only parentId {F[n]['upd'][k][1]}, no state (event {F[n]['upd'][k][0]}), so {k} stays {SEEDED[k]}; {gh(n)}") for n in F)
    shared = "#473 comment: R36, R38, R64, R66, R80, R81, R82, R83, R110, R111, R141, and the counts R175, R176, R180, R181"
    add(r_state, runs_s, tests("C", RULE_STATE, "linear_update_issue is in the catalog and every run used it"), shared,
        f"{k} had to end in In Validation, because its fix is in pull request #473, merged into main on Sep 30 2025. {INTRO}sets In Validation for a report waiting on QA, and Oliver Brooks's comment on #473 lists four flow fixes, this one among them ({what}). {MISS_C} Each run moved {k} under the {area} child without changing its state, so it stayed Todo.",
        f"could a correct run fail it? A run that reads Oliver's comment sets In Validation and passes. Is #473 fairly reachable? The note's 'a fix for it is in main' covers every merged pull request, and every run was shown the merge of #473 into main in #builds (run-1 event {F[1]['saw473']} to run-6 event {F[6]['saw473']}) without opening its comments. Judge check: no state key in any run's update of {k}.")
    runs_c = " · ".join(ev(n, f"linear_create_comment on {k} gives '{stat(F[n]['cmt'][k][1])}' with the reason that no fix exists (event {F[n]['cmt'][k][0]}): '{F[n]['cmt'][k][1][:110]}'; {gh(n)}") for n in F)
    assert all(stat(F[n]["cmt"][k][1]) == "Waiting on a fix" and "473" not in F[n]["cmt"][k][1] for n in F)
    add(r_status, runs_c, tests("C", RULE_NOTE + "; " + RULE_STATUS, "linear_create_comment is in the catalog and every run used it"), shared,
        f"The comment on {k} had to give the status Waiting on QA, because its fix is in pull request #473, merged into main on Sep 30 2025. {INTRO}asks for a note with the status and why on each moved ticket, and Oliver Brooks's comment on #473 lists this fix ({what}). {MISS_C} Each run's comment on {k} gives Waiting on a fix.",
        f"could a correct run fail it? The row accepts waits on QA, ready for QA or to re-test. Judge check: all six bodies on {k} say Waiting on a fix (run-1 event {F[1]['cmt'][k][0]} to run-6 event {F[6]['cmt'][k][0]}).")
    add(r_reason, runs_c, tests("C", RULE_NOTE, "linear_create_comment is in the catalog and every run used it"), shared,
        f"The comment on {k} had to say that its fix is in pull request #473, which is merged into main. {INTRO}asks for a note with the status and why on each moved ticket, and Oliver Brooks's comment on #473 lists this fix ({what}). {MISS_C} Each run's comment on {k} says no fix is in main, and none names #473.",
        f"could a correct run fail it? Any wording that names the merged #473 as the fix passes. Judge check: '473' occurs in none of the six comment bodies on {k} (run-3 event {F[3]['cmt'][k][0]}).")
shared = "#473 comment: R36, R38, R64, R66, R80, R81, R82, R83, R110, R111, R141, and the counts R175, R176, R180, R181"
assert all(F[n]["c38"][1] == "Todo" and F[n]["s38"][1] == "Waiting on a fix" for n in F)
add(66, " · ".join(ev(n, f"linear_create_issue for 'Pass progress bar fills before the tokens arrive' with state Todo (event {F[n]['c38'][0]}); {gh(n)}") for n in F),
    tests("C", "'If no ticket has it, make a sub-issue under the child with the report as the title and the state the same way'", "linear_create_issue is in the catalog and every run used it"), shared,
    f"The sub-issue for the report had to be in In Validation, because its fix is in pull request #473, merged into main on Sep 30 2025. {INTRO}gives a new sub-issue the state that matches its status, and Oliver Brooks's comment on #473 lists this fix (the pass bar filling before the tokens land). {MISS_C} Each run created the sub-issue in Todo.",
    f"could a correct run fail it? In Validation set at creation or afterwards both pass. Judge check: each run's linear_create_issue for the report carries state Todo (run-1 event {F[1]['c38'][0]} to run-6 event {F[6]['c38'][0]}) and no later update changes it.")
add(141, " · ".join(ev(n, f"gsheets_values_update writes the row 'Pass progress bar fills before the tokens arrive', 'Season Pass', '{F[n]['s38'][1]}' (event {F[n]['s38'][0]}); {gh(n)}") for n in F),
    tests("C", "'Sheet: tab Reports with Report, Area, Status, Ticket, Review list, Why'; " + RULE_STATUS, "gsheets_values_update is in the catalog and every run used it"), shared,
    f"The Status cell of the report had to read Waiting on QA, because its fix is in pull request #473, merged into main on Sep 30 2025. {INTRO}asks for a Status on every report row of the stock-take sheet, and Oliver Brooks's comment on #473 lists this fix (the pass bar filling before the tokens land). {MISS_C} Each run wrote Waiting on a fix in that cell.",
    f"could a correct run fail it? The row accepts any wording that means waiting on QA. Judge check: the six sheet writes carry 'Waiting on a fix' for the report (run-1 event {F[1]['s38'][0]} to run-6 event {F[6]['s38'][0]}).")
dq, df = [F[n]["dm"][1] for n in F], [F[n]["dm"][2] for n in F]
sq, sf = [F[n]["slide"][1] for n in F], [F[n]["slide"][2] for n in F]
assert dq == sq and df == sf and 9 not in dq and 20 not in df
lst = lambda v: ", ".join(map(str, v[:-1])) + f" and {v[-1]}"
CNT = "The count runs over the 39 reports under Brian's note on ZOM-543, which the prompt hands over with 'set it all up as he asked', and Brian's message asks for it. It needs the three reports whose fix Arthur Blake's review comments on #472 and #475 say is not in those pull requests, and the four reports whose fix Oliver Brooks's comment lists in the merged #473. No run opened those comments"
CT = ("Tests: authority: the prompt's 'message him in our DM with the numbers he wants back' and 'a slide with the numbers in my queue manager deck'; Brian's DM D0770ET6WBW/1759264805.214409 asks 'how many wait on QA, how many wait on a fix'; "
      + tests("D", RULE_STATUS, "slack_send_message and gslides_batch_update are in the catalog and every run used them")[len("Tests: authority: "):])
shared_d = "all three comments (#472, #475, #473): R175, R176, R180, R181 follow from the seven statuses the runs got wrong (rows 12, 13, 14, 15, 32, 37, 38)"
for rid, what, exp, got, slot, key, where in ((175, "reports waiting on QA", 9, dq, "dm", 1, "message to Brian"), (176, "reports waiting on a fix", 20, df, "dm", 2, "message to Brian"),
                                              (180, "reports waiting on QA", 9, sq, "slide", 1, "new slide"), (181, "reports waiting on a fix", 20, sf, "slide", 2, "new slide")):
    tool = "slack_send_message in D0770ET6WBW" if slot == "dm" else "gslides_batch_update on the queue manager deck"
    add(rid, " · ".join(ev(n, f"{tool} gives {F[n][slot][key]} {what} (event {F[n][slot][0]}); {gh(n)}") for n in F), CT, shared_d,
        f"The {where} had to give {exp} {what}. {CNT}, so the six runs gave {lst(got)}.",
        f"could a correct run fail it? {exp} follows from the 39 statuses with no second fair reading: the platform /prompt and /oe reviews re-derived 10, 9, 20, 0 and 7. Judge check: run-2, the closest run, gives {F[2][slot][key]} (event {F[2][slot][0]}), off by the seven statuses the three comments decide.")
B.sort(key=lambda b: b[0])
assert [b[0] for b in B] == ALLFAIL, ([b[0] for b in B], ALLFAIL)

L = ["# 11 All-Fail Justification — calvin_qm_epic (rev3b, rubric b19500a5cc7b, /rubric PASS 5)", "",
     "Completed rollouts: 6/6 (excluded: none)   Rubric binding: ok — every verifier row binds to one criterion of 09_Rubrics.json by title; Run #N is bound to trajectory-run-N.json by the record ids each run created (Working_Files/12_Verifier_Binding_Receipt.json)",
     "Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)",
     "All-fail rubrics: " + ", ".join(f"R{i}" for i in ALLFAIL), "",
     "Verifier: 10_Baseline_Verifier_Results.md, six 'Run #N' blocks of 184 rows (" + ", ".join(f"run-{n} {heads[n]}/184" for n in sorted(heads)) + "); every header agrees with its rows. Trajectories: 07_Baseline_Trajectories/trajectory-run-1…6.json, all with a final result, all claude-opus-5-5. Event numbers are indexes into each trajectory's event list.",
     "", "One root cause in three places: no run read a pull request's review comments or conversation comments. The three deciding records are " + A472 + " (rows 12 and 15), " + A475 + " (row 32) and " + O473 + " (rows 13, 14, 37 and 38).", ""]
for rid, runs, tst, shared, just, counter in B:
    L += [f"### R{rid} — VALID   (weight {W(rid)})", f"Criterion: \"{T(rid)}\"", "Per-run evidence: " + runs, tst,
          "Causation: no test fails; the six runs share one omitted step (the pull request's comments were never opened), which is a model miss, not a rubric or environment defect",
          "Shared root cause: " + shared, "Justification (VALID only): " + just, ""]
L += [f"Screen file: task_inputs/11_Baseline_AllFail_Justifications.md ({len(B)} section(s), one paragraph each; Not justified: none)", "",
      f"Summary: valid {len(B)} · invalid 0 (rubric 0, environment 0; ≥ 2 = QC Fail, 1 = Non-fail) · judge errors 0 · unresolved 0 · non-causal defects to fix none",
      "Hand-off to /create-difficulty: --invalid none --judge-correction none", ""]
chk = [l for l in open(os.path.join(HERE, "out", "inj", "checksql.txt")).read().splitlines() if "#472#rc_1" in l or "#475#rc_1" in l or "#473#c_2" in l]
L += ["## Self-review", "",
      "**1. Re-read as the eval.** Walked Evals/references/rules/all_failing.md (the four classes and the Process test), the QC row 'Rubrics — All-Failing Rubrics' and screens 56/58. None of the four Evals bases applies: the three deciding comments are GitHub rows (unscoped for Calvin) on pull requests the sheet names or the note's 'a fix for it is in main' covers; every write tool is in the catalog and was used by the runs; no friction is configured; no row rejects a fair alternative or passes an idle Agent. 0 invalid all-fails, so the QC dimension is 5 if the 24 paragraphs are factual.", "",
      "**2. Recomputed the all-fail list independently.** plan/build_allfail.py counts the Fail decisions per criterion in the raw 10_Baseline_Verifier_Results.md text (split on 'Run #N', titles bound to 09_Rubrics.json): six of six for " + ", ".join(f"R{i}" for i in ALLFAIL)
      + ". This equals the calculator's 'All-fail rubrics' line, and each run's header equals its rows (" + ", ".join(str(heads[n]) for n in sorted(heads)) + " passed of 184). Rows failed by five runs, not six (run-2 passes them): "
      + ", ".join(f"R{i}" for i, s in sorted(PARTIAL.items()) if len(s) == 5) + "; they are not all-fails.", "",
      "**3. Re-verified the deciding records.** The three comments were re-read as SQL text in 01_Universe_Inject.sql (github.github_review_comments and github.github_pr_comments rows, created 2025-09-30T15:53:40Z, 16:09:50Z and 15:42:10Z, before the freeze); the base pull requests #472, #473 and #475 and their merge times were re-read through tools/hg.py (plan/oe_reads.py → plan/oe_base.json). Calvin's reach, from `persona_view.py check-sql calvin_price … --load-bearing`:", "", "```text"] + chk + ["```",
      "Every per-run locator above was re-extracted from the six trajectories by plan/build_allfail.py, which asserts that no run's linear_update_issue on the six tickets carries a state, that no run called a GitHub comments or reviews tool, and that the message and slide numbers agree in each run.", "",
      "**4. Counter-readings, one per block.**", "", "| Row | Verdict | Strongest counter-reading | Resolution | Unresolved |", "|---|---|---|---|---|"]
for rid, runs, tst, shared, just, counter in B:
    L.append(f"| R{rid} | VALID | {counter.split(' Judge check:')[0].replace('|', '/')} | Judge check:{counter.split(' Judge check:')[1].replace('|', '/')} | none |")
L += ["| All 24 | VALID | could the environment have blocked it? A forced error or a hidden record would make these invalid | 03_Error_Async_Config.txt is Friction: none; the three rows are [YES LB] in the check-sql lines above; run-3 opened #475 itself (github_get_pull_request, event " + str(next(i for i, nm, a in F[3]["gh"] if nm == "github_get_pull_request")) + ") and still did not ask for its comments | none |",
      "| All 24 | VALID | is one missed habit failing 24 rows a cascade defect? | Each row grades a separate write (a state, a status, a reason, a cell, a number); the /rubric review (rubric_r3_PASS.md) ruled that one missed record failing rows on separate deliverables is not a group, per R34 to R181 | none |", "",
      "Unresolved: none.", ""]
open(os.path.join(TI, "11_AF_Justification.md"), "w").write("\n".join(L))
S = ["# Baseline All-Fail Justifications", "", f"All 6 baseline rollouts completed, so an all-fail rubric is one that failed in all 6. {len(B)} rubrics failed in all 6, and {len(B)} are valid.", ""]
for rid, runs, tst, shared, just, counter in B:
    S += ["## " + T(rid), "", just, ""]
open(os.path.join(TI, "11_Baseline_AllFail_Justifications.md"), "w").write("\n".join(S))
print("all-fail", len(B), "paragraph chars", min(len(b[4]) for b in B), max(len(b[4]) for b in B), "partial5", [i for i, s in PARTIAL.items() if len(s) == 5][:40])
