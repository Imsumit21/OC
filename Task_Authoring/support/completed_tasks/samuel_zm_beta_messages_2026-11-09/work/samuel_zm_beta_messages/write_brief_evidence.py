#!/usr/bin/env python3
"""Record the prompt-writing outcome review in 00_V3_Authoring_Evidence.json, bound to the brief's artifact hash."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
env = {**os.environ, "TASK_AUTHORING_TASK_DIR": "Task_Authoring/task_inputsK"}
h = subprocess.run(["python3", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", "Task_Authoring/task_inputsK/Working_Files/04_Prompt_Writing_Brief.md"],
                   cwd=WS, capture_output=True, text=True, env=env).stdout.strip().split()[-1]
P = json.load(open(os.path.join(HERE, "ids.json")))
EX = json.load(open(os.path.join(HERE, "brief_extra.json"))) if os.path.exists(os.path.join(HERE, "brief_extra.json")) else {}
path = os.path.join(WF, "00_V3_Authoring_Evidence.json")
ev = json.load(open(path))
ev.setdefault("outcome_reviews", {})["prompt-writing"] = {
    "artifact": "04_Prompt_Writing_Brief.md", "artifact_hash": h,
    "reviewer": "Claude (Opus 5.5), self-review plus independent blind fork sweeps by fresh agents that saw only the SQL and the base (plan/sweep_fork.md on rev1, plan/sweep_fork_rev2.md on rev2, its forks settled in rev3; an independent read of the prompt settled in rev4); no independent human reviewer (REDTEAM_* unset)",
    "rationale": EX.get("rationale", "Brief §4b gives one value or a closed accepted set for every graded field of rev6. Every fork the first sweep found that could move a Call was settled in a record, not in acceptance."),
    "accepted_outcomes": [
        "W1: one native sheet whose final parent is d_caafeec2804b3a67ce46aa, header Message, Ticket, Call, What's missing, Audience, Final headline, String change, 36 rows",
        "W1 calls: Go 2 (Lapsed 1 day, Lapsed 7 days), Drop 6 (Hourly Coins, Nathan's Treasure Hunt, Streak Fever, Axe Arena, Lapsed 14 days, Comeback gift), Hold 28",
        "W1 headlines on Go rows with or without emoji; String change Yes only on Lapsed 7 days with " + P["new_line"],
        "W1 What's missing in any wording naming the gap, with or without the test number; Audience in the asker's words or a plain rewording, narrowing to asked players also fair on Go rows",
        "W2: a Google Doc with the same final parent: iOS D1 31.65 D7 9.28, Android D1 37.86 D7 10.68, rounded to one decimal also fine; reminders on days 1, 7, 14, 21, 28; players who stop before level 20 hear nothing unless they switched messages on from settings",
        "W3: the call as a comment on the 32 message tickets; W4: Drop to Canceled, Hold to Backlog unassigned, Go unchanged; on the four Done Holds, Todo still shows the call was found",
        "W5: four new tickets for the asks with no ticket (team DES or ZOM, any title) and one string ticket under DES-314 carrying the new line",
        "W6: a checklist with the two Go messages on 6851a769c65dc0017a227bb7, any checklist name",
        "W7: one email to each of Brian, Calvin, Douglas, Julia, Martin, Oliver, Owen and Robert with their asks and calls; none needed to Leonard",
        "W8: Go 2, Hold 28, Drop 6 in Leonard's DM"],
    "alternatives_considered": [
        "Hold on the Go rows because players below the ask can't be reached: rejected, the rule says test 4 fails only if none of them count",
        "Hold on the lapsed rows because a moved phone date isn't seen: rejected, the QA note says it is fine on a store build",
        "Go on Lives recharged because Vincent passed it on 0.3.40: rejected, his Sep 30 post takes his tick off it after 0.3.49",
        "Go on Plague Race because the sheet and ticket show a pass: rejected, his Sep 29 reply says that iPhone was on the timers build",
        "Hold on the two lapsed rows because they were passed on 0.3.40: rejected, Vincent's Sep 30 post says they are still coming through",
        "Your Squad Needs You Back as the final line: rejected, Leonard's Sep 30 note on the copy check replaces it and says so",
        "Go on Finish first mission because iOS prompts at launch: rejected, Arthur's reply says that popup switches nothing on and the rule says our own ask",
        "Todo for Hold tickets: rejected, the doc defers to the roadmap and Leonard's later card note says Backlog",
        "A new ticket for Win & Collect: rejected, the hub says under whatever name and the live-ops page maps the names",
        "An email to Leonard for his own asks: rejected, the hub says apart from me"] + EX.get("alternatives", []),
}
json.dump(ev, open(path, "w"), indent=1, ensure_ascii=False)
print("evidence bound to", h)
