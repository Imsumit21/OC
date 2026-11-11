#!/usr/bin/env python3
"""Record the prompt-writing outcome review in Working_Files/00_V3_Authoring_Evidence.json, bound to the brief's digest.
Touches outcome_reviews["prompt-writing"] only; every other key is kept as it stands. Run after assemble_brief.py."""
import json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
TASK = "Task_Authoring/task_inputsS2"
ENV = dict(os.environ, TASK_AUTHORING_TASK_DIR=TASK, PYTHONDONTWRITEBYTECODE="1")
h = subprocess.run([sys.executable, "-B", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", f"{TASK}/Working_Files/04_Prompt_Writing_Brief.md"],
                   cwd=WS, capture_output=True, text=True, env=ENV).stdout.strip().splitlines()[-1]
p = os.path.join(WF, "00_V3_Authoring_Evidence.json")
d = json.load(open(p))
before = {k: v for k, v in d.items() if k != "outcome_reviews"}
others = {k: v for k, v in d.get("outcome_reviews", {}).items() if k != "prompt-writing"}
d.setdefault("outcome_reviews", {})["prompt-writing"] = {
    "artifact": "04_Prompt_Writing_Brief.md", "artifact_hash": h,
    "reviewer": ("Claude (Opus 5.5), self-review of the brief, with plan/research/pw1_prompt_lessons.md, plan/research/sw1_forks.md and the platform /prompt report "
                 "plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md read (attempt 6aeed82596dcfe103f9f74d9, rev4 SQL 872bbb307710, FAIL 2 on Lauren Brooks's bucket and Combo Fighter's revenue, both closed in rev6). "
                 "Other cold reviews were reported to Claude by the coordinator in this session and are recorded as reported: none is saved as a file and Claude has not seen their text. "
                 "They are a rev1 blind sweep (36 forks, 18 open), a rev2 sweep where a keyless reviewer reproduced the bet totals, Company line and revenue with prompt findings none, "
                 "a cold Eval 1 review (NON-FAIL on Clarity and Coherence, reported fixed in rev3), a fourth reviewer on the rev3 wording whose two findings went into rev4, "
                 "and a reviewer on rev5 who found the reply gap and the Martin reading, reported fixed in rev6. No cold review has covered rev6 itself."),
    "rationale": ("Brief §4b fixes each material field from dated records: the method f_6feda53b2382c63bf47b25, the ask C0ADGSZKR3R/1770945821.640039 and C0ADGSZKR3R/1770945859.212469, "
                  "the 132 notices, Leapblock's statement, Arthur's mail, Leonard's notes on ENG-2454, ENG-2455 and ENG-2459, and the warehouse table. It accepts every representational or delegated field. Figures were re-derived in this run through hg.py: "
                  "all 23 account endings, the three by-date sums, Leapblock by year, five receipts by tracking number and both revenue tables agree with solver/truth.json, and the absence of a Payoneer or Upwork receipt in Robert's mail was searched with a positive control. "
                  "This records a review of supplied evidence, not proof of semantic fairness."),
    "accepted_outcomes": [
        "a sheet owned by Robert in his Drive, at his root d_9f7ba94f7526d54d8482ba or any folder he owns, any title, in the layout of f_3304033843904a426f3c00, shared with Leonard and Arthur Blake as editor, viewer or commenter",
        "22 rows, matched on account endings (NB-12), with the zero rows kept: Build 9, Marketing 6, Company 6, Not a cost 1",
        "build cost Domino Delights 959,342.64, ZM 544,433.44, Combo Fighter 72,685.61; brought in Domino Delights 12,331.25 and ZM 11.99 as table totals, anywhere on the sheet",
        "Combo Fighter's brought-in left blank, marked held or 'to come', on the sheet and in the reply, as the method says; nothing grades a Combo Fighter figure (NB-26)",
        "reply figures exact, whole-dollar or rounded ($959K, $544K, $73K; $12.3K, $12)",
        "Company dollars in the Company column, with or without the same amount in a bet column; Company total 49,625.00 plus 1,999 BGN",
        "1,999 BGN in the Company cell or that row's Note, never in a dollar total",
        "Marketing dollars in or out of the bet columns, outside every build total; Marketing total 73,965.63 if shown",
        "ENG-2450's zero row under any bucket label that marks it as no cost",
        "ENG-2459 at zero, Marketing, with a reason first",
        "ENG-2438 to ENG-2459 all Done, with a reason comment first on ENG-2439, ENG-2442, ENG-2447, ENG-2450 and ENG-2459; extra comments, such as on ENG-2454, not penalised",
        "one reply in #winddown as a thread under either of Leonard's two posts or a top-level post, giving what each bet cost and brought in, what changes on the deck, and the sheet link",
        "deck left unchanged, with a deck edit not penalised; Trello card left untouched",
    ],
    "alternatives_considered": [
        "Leapblock at the notices' 374,654 on 'ground source of truth' (rejected: 'that beats the notices for them', the Awaiting notice shows the wire and the statement ties out by year; case K49-newer-source)",
        "MotMot at the notices' 41,088 (rejected: the founders said the money came back, which the method's test names)",
        "Lucas at the notices' 6,450 (rejected: the method admits a receipted contractor at the amount sent)",
        "Lucas with fees at 13,978.96 (rejected: 'at the amount sent, not the fee')",
        "Lucas at 15,050 by summing every receipt mail (rejected: one is a forwarded copy with the same tracking number)",
        "JPMorgan as a cost, or as a 4,000 row marked not spending (rejected: Arthur's mail, and 'Every payee keeps its line, even at zero')",
        "ENG-2459 at 125 because the notice says Processed and Dixelar's requests reached Robert (rejected: Leonard's note says the wire came back, and a request is not a receipt)",
        "Node Media as Build by date (rejected: the invoice mail's ad-spend clause, under the method's Marketing sentence)",
        "Lauren Brooks as Build or Company (rejected: Leonard's ENG-2455 note 'so she\u2019s marketing, not build', with her Agreement's Exhibit A and the #company-internal post)",
        "Singular as Marketing or split by game (rejected: ENG-2443 'attribution tool, not one game' and the method's 'tools')",
        "Martin Walsh as Build (rejected: the ENG-2454 note 'paid him direct for his laptop' and the Oct 30, 2025 exchange make it equipment, so Company)",
        "Combo Fighter's revenue reported on the sheet or in the reply (outside acceptance: the method says leave it off; nothing grades it)",
        "the P&L or the Trello quick plan as the counting method (rejected: the method says go by the notices and that it replaces the plan)",
        "a one-page doc instead of the sheet (rejected as a replacement: the draft wording builds the page as a sheet; accepted as an extra)",
        "a sheet edited inside Leonard's file (rejected: 'keep yours in your drive')",
        "brought-in figures in the reply alone (rejected: the page covers cost and brought in, and that page is the sheet; any place on the sheet is accepted)",
        "the run editing the deck as the required outcome (rejected: 'I'll update it myself'; an edit is not penalised)",
        "a thread under the first post only (rejected as a restriction: all three placements reach Leonard in #winddown with the same content)",
    ],
}
after = {k: v for k, v in d.items() if k != "outcome_reviews"}
assert after == before and {k: v for k, v in d["outcome_reviews"].items() if k != "prompt-writing"} == others
json.dump(d, open(p, "w"), indent=2)
print("prompt-writing outcome review bound to", h)
