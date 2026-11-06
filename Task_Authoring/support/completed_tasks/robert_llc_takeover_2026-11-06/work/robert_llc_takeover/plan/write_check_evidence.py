#!/usr/bin/env python3
"""Record the prompt-check outcome review and the assigned-role review in Working_Files/00_V3_Authoring_Evidence.json,
both bound to the digest of 04_Prompt.txt (the artifact /prompt reads)."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
h = subprocess.run(["python3", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", "Task_Authoring/task_inputs/04_Prompt.txt"],
                   cwd=WS, capture_output=True, text=True, env=dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")).stdout.strip().splitlines()[-1]
p = os.path.join(WF, "00_V3_Authoring_Evidence.json"); d = json.load(open(p))
REVIEWER = "Claude (Opus 5.5), prompt check C1-C24 on rev4 (Working_Files/04_Prompt_Check.md), with four blind fork sweeps of the data and a fifth, focused re-sweep of the rev4 forks (plan/sweep_dispositions.md)"
d.setdefault("outcome_reviews", {})["prompt-check"] = {
    "artifact": "04_Prompt.txt", "artifact_hash": h, "reviewer": REVIEWER,
    "rationale": ("The prompt pins every destination (Robert's Drive, the LLC project, the thread of Leonard's DM D04UP2L3E3S/1770961200.890407) "
                  "and the two readers (Leonard, Blake), and points at Leonard's DM for the rules; the DM in turn names the ground rules doc "
                  "f_1e468a9d69ea0f0a2001f5, the draft f_d996e4c434ce160dc52596 and the split email. Every material field of brief §4b is settled "
                  "by a dated record; the open fields (sheet title, share role, owner, wording, link vs name, third vs cash framing of each "
                  "founder's monthly cost) are representational or both-correct readings of the same split rule, and each is accepted."),
    "accepted_outcomes": [
        "plan sheet in Robert's Drive root d_9f7ba94f7526d54d8482ba, any title, the draft's eight columns (order free, extra columns allowed), one row per item (37 issues + the CF VO campaign; Metabase + dbt as one or two rows), shared with leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co as writer, commenter or reader",
        "decisions LLC 7 / Founder 3 / HG 28 with costs DD prod 140, CF stacks 62 (Arthur's jenkins email over his $95 ENG-2445 note), VO campaign 3,000, Metabase 100, dbt 100, GitHub 48 and every other row 0; Paid by the LLC for DD prod, CF stacks and the campaign (the new company's card from March), Arthur for Metabase, dbt, GitHub",
        "steps: DD support build by Feb 28 (any Feb 15-28 date); layer.ai art pulled out by Robert by/before Mar 3; CF and DD when the sale closes; LLC billing moves by Mar 1",
        "per-month shares on the sheet: total 3,450, a third 1,150 each, cash 1,150 / 1,150 / 902 (Leonard / Robert / Arthur); optional Mar-May totals x3",
        "a comment with the call on each of ENG-2438..ENG-2474 and the state from the rev4 project description: the LLC rows Todo (CF Robert, DD Leonard, DD prod / CF stacks / DD support Arthur, AppsFlyer Leonard), ENG-2462 Todo not Done, Metabase / dbt / GitHub Done, the HG rows Canceled (layer.ai, Calm Play and Google Analytics included)",
        "a new issue for the CF VO campaign in project 0fa95761-d59b-4ff4-a8a3-15df3210ca6e, Todo and assigned to Leonard, so the project matches the sheet",
        "a reply in the thread of D04UP2L3E3S/1770961200.890407 with what Robert would do and each founder's monthly cost, $1,150 each (a third of $3,450), optionally with Arthur's $902 cash after his carried $248 (platform rev3 DR1: $902 is his cash, not his cost), plus the sheet's link (its name also accepted)",
    ],
    "alternatives_considered": [
        "each founder's monthly cost as the even third vs '$902' as Arthur's cost (settled by the split email robert@harmonygames.co/1856989298688559716: each carries a third and puts the difference in as cash, so his cost is $1,150 and $902 is his cash)",
        "CF stacks at $95 (rejected: Arthur's later jenkins email robert@harmonygames.co/1856982378087295205 says it bills $62 a month now)",
        "ENG-2462 to Done on Arthur's 'done' note (rejected: the later App Review notice robert@harmonygames.co/1856994331853686118 leaves the support build to ship)",
        "layer.ai owned by Leonard or moved to Todo for the art export (rejected: Leonard's reply C09UHHN6PFZ/1770923700.470906 asks Robert to pull it out himself and says there's nothing on the layer account for our new company to take, it just lapses; Todo is only for what the LLC takes; a fresh blind re-check rated it SETTLED)",
        "the layer.ai export step on the Combo Fighter row instead of the layer.ai row (accepted: same step, owner and date on the same sheet)",
        "the VO campaign kept on Leonard's card as his carried cost (rejected: C09UHHN6PFZ/1770938400.370665 says it moves to our new company's card from March and to count it as its own line)",
        "a Jenkins line or issue (rejected: the jobs run on Arthur's own machine with no bill, and the email says the build boxes are HG's)",
        "a new top-level DM message instead of a thread reply (settled by the prompt: 'in that DM thread')",
        "the call written in the issue description or as a label instead of a comment (settled by the project description: 'Leave your call on each one as a comment and move it')",
        "the sheet left in a subfolder or in a shared drive (settled by the prompt and the hub: 'in my Drive' / 'keep it in your drive')",
        "no new issue because the project holds only things from HG (rejected: the project description covers what the LLC might take from HG or pay for, the campaign moves to the new company's card from March per C09UHHN6PFZ/1770938400.370665, and the prompt says the project should match the sheet)",
        "AppsFlyer (ENG-2451) assigned to Arthur, who did attribution work (rejected: Leonard's note 'I'll set CF up on it')",
        "Google Analytics (ENG-2452) to Todo at $0 after the data is out (rejected: Leonard's note 'nothing for the LLC to take or pay' and Arthur's mail 'nothing there for the LLC')",
        "GitHub (ENG-2449) Canceled because HG still owns the org (rejected: the rev4 Done test 'if one of us pays it himself through May (even if HG still owns it)' and Arthur's mail 'count it as mine like the other two')",
        "the draft's figures (~$1k DD, ~$300 Metabase/dbt) copied as truth (rejected: later records by the item owners, D04V95AAAHW/1770952200.665739 and robert@harmonygames.co/1856975772058401508)",
        "the LLC takes the build boxes (ENG-2446) if Sunset can't sell them (rejected: Arthur's note 'so the LLC doesn't need them')",
        "a separate CF player-support line and issue (rejected: Leonard's Helpshift note 'CF was never on it, its support is the contact on its store listing and that moves with the game')",
        "share role writer vs commenter or reader (accepted: representational, the hub says only 'share it')",
    ],
}
d.setdefault("role_reviews", {})["prompt-check"] = {
    "artifact": "04_Prompt.txt", "artifact_hash": h, "reviewer": REVIEWER,
    "persona_role": "Co-founder & Creative Director",
    "rationale": ("Robert is one of the three co-founders running the wind-down (#winddown C0ADGSZKR3R; Soundly cancellation "
                  "C0ADGSZKR3R/1770839322.836779) and Combo Fighter is his game, which he wants to keep self-sustaining "
                  "(C07C2866011/1770084297.911029). Leonard asks him directly, in their DM D04UP2L3E3S/1770961200.890407, to make the call on "
                  "each item the founders' LLC might take, cost it March-May and say what each founder pays, before the three founders' "
                  "Monday decision call (evt_f5f279f282d20ec86bb8e5, attendees Leonard, Robert, Arthur). Preparing that plan and recommending "
                  "it to his co-founders is inside a co-founder's remit (prepare and recommend; the decision is taken jointly on Monday). "
                  "Creative Director is no obstacle: the ask is a founder's, not a department's, and the V3 rule judges role plausibility only."),
    "source_ids": ["D04UP2L3E3S/1770961200.890407", "C0ADGSZKR3R/1770839322.836779", "C07C2866011/1770084297.911029",
                   "evt_f5f279f282d20ec86bb8e5", "C07C2866011/1770612982.268919", "d_9f7ba94f7526d54d8482ba"],
}
json.dump(d, open(p, "w"), indent=1); open(p, "a").write("\n")
print("prompt-check outcome + role reviews bound to", h)
