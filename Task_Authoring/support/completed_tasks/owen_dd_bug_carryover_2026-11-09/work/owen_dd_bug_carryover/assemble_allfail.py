#!/usr/bin/env python3
"""Write task_inputs/11_AF_Justification.md (workbook) and 11_Baseline_AllFail_Justifications.md (screen file) from one
table, so the screen paragraph is the workbook's Justification line byte for byte. Evidence comes from the six trajectories
(event = index in the trajectory's event list, extracted by scratchpad af/extract.py) and the verifier copy."""
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
TI = os.path.dirname(os.path.dirname(HERE))
RUB = json.load(open(os.path.join(TI, "09_Rubrics.json")))
RAW = open(os.path.join(TI, "09_Rubrics.json")).read()
EV = {1: dict(apple=667, tav=779, c2363=811, sheet=937, reply=950, gm="events 457 and 490 (from:brian.foster@harmonygames.co; UI optimization OR \"close out\")"),
      2: dict(apple=681, tav=800, c2363=836, sheet=939, reply=951, gm="event 358 (from:brian.foster@harmonygames.co)"),
      3: dict(apple=723, tav=831, c2363=863, sheet=961, reply=973, gm="events 457 and 565 (from:brian.foster@harmonygames.co; thread 1832019221491068994, not Vincent's)"),
      4: dict(apple=598, tav=707, c2363=735, sheet=849, reply=864, gm="events 234 and 321 (from:brian.foster@harmonygames.co; \"0.3.310\")"),
      5: dict(apple=617, tav=729, c2363=762, sheet=873, reply=887, gm="events 131 and 386 (0.3.310; from:brian.foster@harmonygames.co)"),
      6: dict(apple=496, tav=608, c2363=640, sheet=748, reply=761, gm="events 119 and 275 (0.3.310; from:brian.foster@harmonygames.co)")}
APPLE_WHY = {1: "Unticked; QA said still cannot sign in (Nov 13). No later fix record. ENG-2073 is a different sync issue.",
             2: "Unticked; Vincent still couldn't sign in (Nov 13) and no later record of a fix",
             3: "Unticked; QA still could not sign in (Nov 13) and no later fix is recorded.",
             4: "Unticked; Vincent still could not sign in on 13 Nov and no later fix record. ENG-2073 is about quest sync, not this.",
             5: "Unticked; Vincent's thread says Apple sign-in still fails after the cache fix, no later record of a fix.",
             6: "Unticked; Vincent's last word (Nov 13) is still cannot sign in. No later fix record and no open ticket covers Apple sign-in (ENG-2280 is scoped to the iOS returning-player HUD case)."}
TAV_WHY = {1: "Ticked on the canvas and no later record says otherwise.", 2: "Ticked; Brian sent the fix", 3: "Ticked; Brian sent the fix (Nov 20).",
           4: "Ticked; Brian sent the fix (20 Nov).", 5: "Tick stands; Brian sent the fix 11/20.", 6: "Ticked; Brian sent the fix Nov 20."}
F = "trajectory-run-{n}.json"
VIN = "Vincent's email owen.baker@harmonygames.co/<CAK0a68e5711011904665cac8fb31fa@mail.gmail.com> (Thu Nov 20 2025 10:12 AM PT, 2025-11-20T18:12:00Z, subject 'sign in lines on my list': 'The Apple sync line on my Android list comes down to the same sync problem as ENG-2073, no need for anything new.')"
MAR = "Marcus Bennett's DM D05USBTQY1F/1765452012.418229 (Thu Dec 11 2025 3:20 AM PT, 2025-12-11T11:20:12Z: 'the Tavern buttons lost their frame again on last night's Android build, I looked at the prefab and Brian's fix didn't hold')"
NOTES = "the carry-over notes f_3ca9e15d7b20f4e681ad52"
AUTH = ("authority: the prompt asks for 'everything he asked for, the way he lays it out'; Arthur's DM D05S1S2AB5M/1770937805.214409 says "
        "'How we call each one is in the carry-over notes doc I shared with you', and " + NOTES + " set the rule quoted here")
REACH_V = ("reachability: " + VIN.split(' (')[0] + " is in Owen's own inbox (persona_view check-sql: '[YES LB] L284 … row user_email is the persona'); "
           "the notes' 'Vincent tied a few lines to tickets before he left' points to it, and the /oe-passed path reaches it with one Gmail search for Vincent's mail about signing in; deciding record PROMPT_LINKED")
REACH_M = ("reachability: " + MAR.split(' (')[0] + " is in Owen's own DM (persona_view check-sql: '[YES LB] L58 … persona EMPLOYEE_0021_SLACK_ID is in members of im D05USBTQY1F'); "
           "the notes' 'A tick on the canvas stands unless a later record about that bug says otherwise' sends the agent to later records, and the /oe-passed path reaches it with one Slack search for 'Tavern'; deciding record PROMPT_LINKED")
CAP = "capability: SUPPORTED (every run used the same catalog write tools for the other rows: linear_create_issue, linear_create_comment, gsheets_values_update, slack_send_message)"
PHR = "phrasing: affirmative, Agent-centric, no tool name; an idle Agent fails it (no write)"
FRI = "friction: none configured (03_Error_Async_Config.txt 'Friction: none'); no forced error or async wait in the runs"

ROWS = []


def row(rid, ev_fn, tests, cause, shared, just):
    ROWS.append(dict(rid=rid, ev=ev_fn, tests=tests, cause=cause, shared=shared, just=just))


row("R1", lambda n, e: f"run-{n}: 69 linear_create_issue calls (ENG-2438 to ENG-2506); the Apple sync line filed as '[2231] In general, I cannot sync and sign in with my Apple account. :warning: :warning:' in Bugs ({F.format(n=n)} event {e['apple']}); Gmail only {e['gm']}, Vincent's email never opened",
    f"{AUTH} ('One Linear record per canvas line and one per bug posted after it'; Covered: 'Don't file a new one, add a note on that ticket with the canvas wording'; the template 'Engineering team, Bug label, parent ENG-2401, … no assignee, nothing in the description'; Arthur's ENG-2401 comment 'put [2231] at the front of every title you file') · grounding: 63 canvas lines + 7 later posts − 2 Covered (Apple → ENG-2073 by {VIN.split(' (')[0]}, sign-in → ENG-2363 by comment_7ab5299cbb609d95ba12249d315daedc) = 68; ENG-2073 'Sign-In Account Synchronization Issues' is open in Bugs at the freeze · {REACH_V} · {CAP} · atomicity/destination: one volume row stating the template (rubric_sampling's volume control, kept by /rubric PASS 5); every run met each template field on all 69 issues (team Engineering, label Bug, parent ENG-2401, no assignee, no description, [2231] prefix), so only the count decides · precision/flexibility: an exact count the notes' scope produces; no wording or format imposed · {PHR} · {FRI}",
    "no test fails; the non-atomic reading (count plus template) is not causal, since every run met the template and failed only on the count 69", "R1, R77, R123, R128, R136 (the missed email: the Apple line filed as new); R135 shares it with the Tavern miss",
    "The expected count is exactly 68 new issues: 63 canvas lines plus 7 later bug posts, minus the 2 lines that open tickets already cover. The prompt asks for everything Arthur asked the way he lays it out, and his carry-over notes say a line an open ticket already covers gets a note on that ticket instead of a new one, and that Vincent tied a few lines to tickets before he left; Vincent's email in Owen's inbox (Nov 20, 2025) ties the Apple sync line to ENG-2073, which is still open in Bugs. All six runs found Vincent's other tie, a comment on ENG-2363, yet filed 69 issues (ENG-2438 to ENG-2506), adding ENG-2440 for the Apple sync line, because none of them opened Vincent's email: their only Gmail searches were for Brian's mail, the build number or the UI work. Every other part of the template held in all six runs, so the count of 69 alone fails the row.")
row("R15", lambda n, e: f"run-{n}: filed '[2231] Tavern buttons lost its frame.' in Done ({F.format(n=n)} event {e['tav']}); no Slack call on D05USBTQY1F and no search for 'Tavern' in the run",
    f"{AUTH} ('A tick on the canvas stands unless a later record about that bug says otherwise'; 'Broken: anything else. File it as Bugs.') · grounding: the line is ticked with Brian's Nov 20 fix in its thread; {MAR} is later and about this bug · {REACH_M} · {CAP} · atomicity/destination: one state on one issue, named by its line, any title accepted · precision/flexibility: Bugs is the notes' state for Broken; the row accepts the issue whatever its title · {PHR} · {FRI}",
    "no test fails", "R15, R122, R129 (the missed DM); R135 shares it with the Apple miss",
    "The expected state for the Tavern buttons issue is Bugs, because Marcus's Dec 11, 2025 DM to Owen says the frame was lost again on the Android build and Brian's fix didn't hold. The carry-over notes say a tick on the canvas stands unless a later record about that bug says otherwise, and anything not fixed, gone or covered is Broken and filed as Bugs; Marcus's message sits in Owen's own DMs and a Slack search for Tavern reaches it. All six runs filed the issue for the ticked Tavern line in Done, relying on the tick and Brian's Nov 20 fix in the line's thread, and none of them searched Slack for Tavern or opened the DM with Marcus.")
row("R77", lambda n, e: f"run-{n}: no linear_create_comment on ENG-2073; it filed a new issue for the Apple line instead ({F.format(n=n)} event {e['apple']}) and added the canvas wording only on ENG-2363 ({F.format(n=n)} event {e['c2363']})",
    f"{AUTH} (Covered: 'Don't file a new one, add a note on that ticket with the canvas wording'; 'Vincent tied a few lines to tickets before he left') · grounding: {VIN}; ENG-2073 open in Bugs at the freeze · {REACH_V} · {CAP} · atomicity/destination: one comment on one named ticket · precision/flexibility: the canvas wording the notes require; emoji codes free · {PHR} · {FRI}",
    "no test fails", "R1, R77, R123, R128, R136 (the missed email)",
    "The expected write is a new comment on ENG-2073 carrying the canvas line In general, I cannot sync and sign in with my Apple account. The carry-over notes say a line an open ticket already covers gets a note on that ticket with the canvas wording and no new ticket, and Vincent's Nov 20, 2025 email in Owen's inbox says the Apple sync line comes down to the same sync problem as ENG-2073, no need for anything new; ENG-2073 is still open in Bugs. No run left any comment on ENG-2073: all six filed a new issue for the line (ENG-2440) instead, and none opened Vincent's email. The same runs did add the canvas wording to ENG-2363 for the other line Vincent tied, so the miss is the email, not the comment step.")
row("R122", lambda n, e: f"run-{n}: sheet row ['Tavern buttons lost its frame. …', 'Fixed', 'ENG-2493', '{TAV_WHY[n]}'] ({F.format(n=n)} event {e['sheet']}); the DM with Marcus never opened",
    f"{AUTH} ('Sheet columns: Bug, Outcome, Ticket, Why.'; 'A tick on the canvas stands unless a later record about that bug says otherwise'; 'Broken: anything else') · grounding: {MAR} · {REACH_M} · {CAP} · atomicity/destination: one Outcome cell of one row in the DD carry-over sheet · precision/flexibility: Broken or the state Bugs both pass · {PHR} · {FRI}",
    "no test fails", "R15, R122, R129 (the missed DM)",
    "The expected Outcome for the Tavern buttons lost its frame row in the carry-over sheet is Broken (or Bugs), because Marcus's Dec 11, 2025 DM says Brian's fix didn't hold. The notes set the sheet columns Bug, Outcome, Ticket and Why and say a tick stands only until a later record about that bug says otherwise; Marcus's message sits in Owen's own DMs. All six runs wrote Fixed for the Tavern row, with a Why citing the tick or Brian's Nov 20 fix, because none of them opened the DM with Marcus or searched Slack for Tavern.")
row("R123", lambda n, e: f"run-{n}: sheet row ['In general, I cannot sync and sign in with my Apple account. …', 'Broken', 'ENG-2440', '{APPLE_WHY[n]}'] ({F.format(n=n)} event {e['sheet']}); Vincent's email never opened",
    f"{AUTH} (Covered: 'an open ticket already covers it. Don't file a new one'; 'Sheet columns: Bug, Outcome, Ticket, Why.') · grounding: {VIN}; ENG-2073 open in Bugs · {REACH_V} · {CAP} · atomicity/destination: one Ticket cell of one row · precision/flexibility: ENG-2073 in any rendering (a key or a link carrying it) · {PHR} · {FRI}",
    "no test fails", "R1, R77, R123, R128, R136 (the missed email)",
    "The expected Ticket for the Apple sync line in the carry-over sheet is ENG-2073, the open ticket Vincent tied the line to in his Nov 20, 2025 email. The notes say a covered line gets no new ticket, that Vincent tied a few lines to tickets before he left, and give the sheet a Ticket column, so the row should point at the ticket that covers it; Vincent's email is in Owen's inbox and ENG-2073, titled Sign-In Account Synchronization Issues, is open in Bugs. All six runs put ENG-2440, the new issue they had filed for the line, in the Ticket cell; two of them judged from ENG-2073's own description that it was a different issue, because none of them opened the email that ties the line to it.")
row("R128", lambda n, e: f"run-{n}: sheet row ['In general, I cannot sync and sign in with my Apple account. …', 'Broken', 'ENG-2440', …] ({F.format(n=n)} event {e['sheet']}); the only Covered line it found was ENG-2363 ({F.format(n=n)} event {e['c2363']})",
    f"{AUTH} ('Covered: it isn't fixed and an open ticket already covers it'; 'Vincent tied a few lines to tickets before he left') · grounding: {VIN}; ENG-2073 open in Bugs · {REACH_V} · {CAP} · atomicity/destination: one Outcome cell of one row · precision/flexibility: the notes' own outcome name · {PHR} · {FRI}",
    "no test fails", "R1, R77, R123, R128, R136 (the missed email)",
    "The expected Outcome for the Apple sync line in the carry-over sheet is Covered, because Vincent's Nov 20, 2025 email ties it to ENG-2073 (Sign-In Account Synchronization Issues), which is still open. The notes define Covered as a line that isn't fixed and that an open ticket already covers, and say Vincent tied a few lines to tickets before he left; his email is in Owen's inbox. All six runs recorded the line as Broken with their own new issue ENG-2440, since none of them opened the email; they found only the ENG-2363 tie, which Vincent left as a Linear comment.")
row("R129", lambda n, e: f"run-{n}: Tavern row Why '{TAV_WHY[n]}' ({F.format(n=n)} event {e['sheet']}); no call on D05USBTQY1F",
    f"{AUTH} ('Sheet columns: Bug, Outcome, Ticket, Why.'; 'A tick on the canvas stands unless a later record about that bug says otherwise') · grounding: {MAR} · {REACH_M} · {CAP} · atomicity/destination: one Why cell of one row · precision/flexibility: any wording saying the frame went again after Brian's fix · {PHR} · {FRI}",
    "no test fails", "R15, R122, R129 (the missed DM)",
    "The expected Why for the Tavern buttons lost its frame row is that the buttons lost their frame again after Brian's fix, as Marcus's Dec 11, 2025 DM to Owen says. The notes give the sheet a Why column and say a tick stands only until a later record about that bug says otherwise; the DM is in Owen's own messages and a Slack search for Tavern reaches it. All six runs gave a Why built on the stale record instead, either that the line is ticked with nothing later or that Brian sent the fix, because none of them opened the DM with Marcus.")
row("R135", lambda n, e: f"run-{n}: reply in the thread 1770937805.214409 says 'Still broken: 8', made of 7 in Bugs plus 1 Covered on ENG-2363 ({F.format(n=n)} event {e['reply']})",
    f"{AUTH} ('When you report back, Covered ones count as still broken'); Arthur's DM asks 'how many are still broken' · grounding: 7 Broken (shop icons, Tavern, train, team quit, backend errors, mega tile, tile dozer window) + 2 Covered (Apple → ENG-2073, sign-in → ENG-2363) = 9; the runs' 8 = 7 in Bugs (the Apple line in place of the Tavern line) + 1 Covered · {REACH_V}; {REACH_M} · {CAP} · atomicity/destination: one number in one reply · precision/flexibility: 9 in any rendering, with or without the 7 + 2 split · {PHR} · {FRI}",
    "no test fails", "R135 joins both misses: the Tavern DM (R15) and Vincent's email (R1)",
    "The expected figure is 9 still broken: 7 Broken items filed as Bugs plus the 2 Covered lines, which the notes say count as still broken when reporting back. Arthur's DM asks how many are still broken; the 7 Broken items include the Tavern line, which Marcus's Dec 11, 2025 DM reopens, while the Apple sync line is Covered by ENG-2073 per Vincent's Nov 20, 2025 email. Every run replied Still broken: 8, made of 7 issues in Bugs (with the Apple line in place of the Tavern line) plus 1 Covered line, ENG-2363, because each run missed both Marcus's DM and Vincent's email.")
row("R136", lambda n, e: f"run-{n}: reply in the thread 1770937805.214409 says 'New tickets filed: 69' ({F.format(n=n)} event {e['reply']}); it filed 69 issues including ENG-2440 for the Apple line ({F.format(n=n)} event {e['apple']})",
    f"{AUTH} (Covered: 'Don't file a new one'); Arthur's DM asks 'how many new tickets you filed' · grounding: 63 + 7 − 2 = 68; {VIN} · {REACH_V} · {CAP} · atomicity/destination: one number in one reply · precision/flexibility: 68 in any rendering · {PHR} · {FRI}",
    "no test fails", "R1, R77, R123, R128, R136 (the missed email)",
    "The expected figure is 68 new tickets: 63 canvas lines plus 7 later bug posts, minus the 2 lines that open tickets already cover. Arthur's DM asks how many new tickets were filed, and the notes say a covered line gets a note on its ticket, not a new one; Vincent's Nov 20, 2025 email ties the Apple sync line to ENG-2073. Every run replied New tickets filed: 69, counting the extra ENG-2440 it filed for the Apple sync line after missing Vincent's email, so the told figure is wrong by the same one ticket as the Linear count.")

for r in ROWS:
    p = r["just"]
    first = re.split(r"(?<=[.!?])\s+", p)[0]
    assert 200 <= len(p) <= 1400 and len(first) <= 220 and re.search(r"\d", first), (r["rid"], len(p), len(first))
    assert not re.search("[—–]", p) and len(re.findall(r"[.!?](?:\s|$)", p)) <= 6, r["rid"]


def crit(rid):
    t = RUB[int(rid[1:]) - 1]["title"]
    q = json.dumps(t, ensure_ascii=False)[1:-1]
    assert q in RAW
    return t, q


W = ["# 11 All-Fail Justification — owen_dd_bug_carryover (rev9, rubric 138f960e0b21, /rubric PASS 5)",
     "",
     "Completed rollouts: 6/6 (excluded: none)   Rubric binding: ok — bound through Working_Files/run_forensics/rev9/platform/09_Rubrics.verifier_titles.json, a copy of 09_Rubrics.json with the builder's escaped brackets in 9 titles (\\[2231\\], \\[PERSON_NAME_1711\\], \\[USERNAME_…\\]); no other field changed",
     "Clock: 2026-02-14 00:00 UTC, Feb 14, 2026 (normal)",
     "All-fail rubrics: " + ", ".join(r["rid"] for r in ROWS),
     "",
     "Verifier: 10_Baseline_Verifier_Results.md, six 'Run #N' blocks of 138 rows (run-1 125/138, run-2 125/138, run-3 129/138, run-4 129/138, run-5 129/138, run-6 125/138); every header agrees with its rows. Trajectories: 07_Baseline_Trajectories/trajectory-run-1…6.json, all with a final result, all claude-opus-5-5. Event numbers below are indexes into each trajectory's event list.",
     ""]
for r in ROWS:
    t, q = crit(r["rid"])
    w = RUB[int(r["rid"][1:]) - 1]["weight"]
    W.append(f"### {r['rid']} — VALID   (weight {w})")
    W.append(f"Criterion: \"{q}\"")
    W.append("Per-run evidence: " + " · ".join(r["ev"](n, EV[n]) for n in range(1, 7)))
    W.append("Tests: " + r["tests"])
    W.append("Causation: " + r["cause"])
    W.append("Shared root cause: " + r["shared"])
    W.append("Justification (VALID only): " + r["just"])
    W.append("")
W.append("Screen file: task_inputs/11_Baseline_AllFail_Justifications.md (9 sections, one paragraph each; Not justified: none)")
W.append("")
W.append("Summary: valid 9 · invalid 0 (rubric 0, environment 0) · judge errors 0 · unresolved 0 · non-causal defects to fix: none (R1's count-plus-template shape is the volume row /rubric kept; not causal, every run met the template)")
W.append("Hand-off to /create-difficulty: --invalid none --judge-correction none")
W.append("")
W.append("Note for /create-difficulty: the builder export (2026-11-09) has R108 (the 0.3.310 line on ENG-2423) at weight 1, not 3; R108 passed in all six runs, so it does not touch this list, but the platform's screen 60 uses the builder's weights.")
W.append("")
W.extend(open(os.path.join(HERE, "allfail_selfreview.md")).read().rstrip().splitlines())
open(os.path.join(TI, "11_AF_Justification.md"), "w").write("\n".join(W) + "\n")

S = ["# Baseline All-Fail Justifications", "",
     "All 6 baseline rollouts completed, so an all-fail rubric is one that failed in all 6. Nine rubrics failed in all 6, and all nine are valid.", ""]
for r in ROWS:
    t, _ = crit(r["rid"])
    S += [f"## {t}", "", r["just"], ""]
open(os.path.join(TI, "11_Baseline_AllFail_Justifications.md"), "w").write("\n".join(S).rstrip() + "\n")
print("wrote both files;", len(ROWS), "rows;", [(r["rid"], len(r["just"])) for r in ROWS])
