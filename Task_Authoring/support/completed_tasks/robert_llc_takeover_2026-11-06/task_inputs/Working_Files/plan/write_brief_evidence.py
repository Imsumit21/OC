#!/usr/bin/env python3
"""Record the prompt-writing outcome review in Working_Files/00_V3_Authoring_Evidence.json, bound to the brief's digest."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
h = subprocess.run(["python3", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", "Task_Authoring/task_inputs/Working_Files/04_Prompt_Writing_Brief.md"],
                   cwd=WS, capture_output=True, text=True, env=dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")).stdout.strip().splitlines()[-1]
p = os.path.join(WF, "00_V3_Authoring_Evidence.json"); d = json.load(open(p))
d.setdefault("outcome_reviews", {})["prompt-writing"] = {
    "artifact": "04_Prompt_Writing_Brief.md", "artifact_hash": h,
    "reviewer": "Claude (Opus 5.5), with four blind fork sweeps by fresh agents, the latest on rev4 (Working_Files/plan/sweep_dispositions.md), and the rev4 red-team fallback (Working_Files/01b_Redteam_Fallback_rev4.md)",
    "rationale": ("Brief §4b fixes every material field from dated records (ground rules f_1e468a9d69ea0f0a2001f5, split email, Trello card, Arthur's DM and mail, "
                  "Leonard's #prototype status and layer.ai reply, Arthur's 'jenkins' email, the App Review notice, the project description's state tests) and accepts each representational or delegated field; "
                  "the rev4 blind sweep reproduced the solver's plan, states and totals ($3,450 a month, $1,150 a third, Arthur $902 cash, CF stacks $62, ENG-2462 Todo/Arthur) without the answer key."),
    "accepted_outcomes": [
        "plan sheet in Robert's Drive root d_9f7ba94f7526d54d8482ba with the draft's columns, one row per item (37 issues + the CF VO campaign), shared with Leonard and Arthur",
        "decisions LLC 7 / Founder 3 / HG 28; costs DD prod 140, CF stacks 62, VO campaign 3,000, Metabase 100, dbt 100, GitHub 48",
        "shares per month: total 3,450, third 1,150, cash 1,150 / 1,150 / 902 (Leonard / Robert / Arthur); LLC cash 3,202; the reply gives $1,150 each, optionally with Arthur's $902 cash (not $902 as his cost)",
        "a call and a state on each issue: the 7 LLC rows Todo (assignees CF Robert, DD Leonard, DD prod / CF stacks / DD support Arthur, AppsFlyer Leonard, VO campaign issue Leonard), the 3 Founder rows Done (GitHub included), the 28 HG rows Canceled (layer.ai, Calm Play and Google Analytics included); Metabase + dbt as one or two rows",
        "steps and dates: DD support build by Feb 28 (any Feb 15-28 date, by/before Feb 28); layer.ai art pulled out by Robert by/before Mar 3 (Mar 1-3 or an earlier date from Feb 20), on the layer.ai row or the Combo Fighter row; CF and DD when the sale closes; LLC billing moves by Mar 1",
        "Paid by: the LLC for DD prod, CF stacks and the VO campaign (the new company's card from March); Arthur for Metabase, dbt, GitHub; HG rows HG, none or blank",
        "a new issue for the CF VO campaign in the LLC project",
        "a thread reply under Leonard's DM D04UP2L3E3S/1770961200.890407 with the recommendation and each founder's monthly cost (third and/or cash) and the sheet's link or name",
    ],
    "alternatives_considered": [
        "campaign left off the plan, or kept on Leonard's card as his carried cost (rejected: his status says it moves to our new company's card from March and to count it as its own line)",
        "CF stacks at $95 from the ENG-2445 note (rejected: Arthur's later jenkins email, $62 a month now, under the costing rule)",
        "ENG-2462 to Done on Arthur's note under the project's Done test (rejected: the later App Review notice leaves the support build to ship, so Todo/Arthur)",
        "layer.ai owned by Leonard or set to Todo for the export (rejected: Leonard's reply asks Robert to pull the art out himself and says there's nothing on the layer account for our new company to take, it just lapses; Todo is only for what the LLC takes)",
        "the export step on the Combo Fighter row instead of the layer.ai row (accepted: same step, owner and date on the same sheet)",
        "DD stays with HG on the ~$1k / $300 figures (rejected: Arthur's later $140 under the costing rule)",
        "Metabase and dbt as LLC cash at ~$300 (rejected: Arthur's mail, $248 carried through May)",
        "Calm Play as the founders' own vehicle (rejected: 2023 subsidiary records and the ground rules' new LLC)",
        "DD player support done (rejected: the later App Review notice on #218)",
        "every step dated Mar 1 (rejected: the card's own-deadline rule; layer.ai Mar 3; Helpshift Feb 28)",
        "the LLC takes the build boxes (ENG-2446) if Sunset can't sell them (rejected: Arthur's note 'so the LLC doesn't need them')",
        "a separate CF player-support line and issue (rejected: Leonard's Helpshift note 'CF was never on it, its support is the contact on its store listing and that moves with the game')",
        "a new top-level DM message (settled by the prompt: in that thread)",
        "GitHub state Canceled instead of Done (rejected: the Done test comes first, 'even if HG still owns it', and Arthur's mail 'count it as mine like the other two')",
        "no new issue for the VO campaign (rejected: the project covers what the LLC might take from HG or pay for, and the prompt says the project should match the sheet)",
        "AppsFlyer assigned to Arthur (rejected: Leonard's ENG-2451 note 'I'll set CF up on it')",
        "Google Analytics to Todo at $0 (rejected: Leonard's ENG-2452 note 'nothing for the LLC to take or pay')",
    ],
}
json.dump(d, open(p, "w"), indent=1); open(p, "a").write("\n")
print("prompt-writing outcome review bound to", h)
