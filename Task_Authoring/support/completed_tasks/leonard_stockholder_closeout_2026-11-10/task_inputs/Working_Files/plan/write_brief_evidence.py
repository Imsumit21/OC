#!/usr/bin/env python3
"""Record the prompt-writing outcome review in Working_Files/00_V3_Authoring_Evidence.json, bound to the brief's digest."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__)); WF = os.path.dirname(HERE); WS = os.path.abspath(os.path.join(WF, "..", "..", ".."))
PY = os.path.expanduser("~/.local/bin/python3.12")
h = subprocess.run([PY, "-B", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", "Task_Authoring/task_inputs/Working_Files/04_Prompt_Writing_Brief.md"],
                   cwd=WS, capture_output=True, text=True, env=dict(os.environ, TASK_AUTHORING_TASK_DIR="Task_Authoring/task_inputs")).stdout.strip().splitlines()[-1].split()[-1]
p = os.path.join(WF, "00_V3_Authoring_Evidence.json"); d = json.load(open(p))
d.setdefault("outcome_reviews", {})["prompt-writing"] = {
    "artifact": "04_Prompt_Writing_Brief.md", "artifact_hash": h,
    "reviewer": "Claude (Opus 5.5), with a blind fork sweep (research/sweeps/rev1_fork_sweep.md) that reproduced the solver's totals and labels without the answer key, a coherence audit, a run simulation and two delta reviews",
    "rationale": ("Brief §4b fixes every material field from dated records: the close-out notes f_a37b403d5200d4f0a31d31 (rows, labels, told, owed, route, drafts), the reply under the Feb 12 list "
                  "C0ADGSZKR3R/1770949310.220519 (family rule, Covered, sharing), the project description ec2ea957-fc8e-4958-b809-0fb735b1e916 (states, reason comments, KPMG sent), KPMG's request and follow-up "
                  "(as-of date, boundary) and Sunset's list (sheet contents). Representational variants (column order, label synonyms, date zone, editing the draft sheet) are accepted."),
    "accepted_outcomes": [
        "holder sheet in the close-out folder d_601064334a0b493022fe83 (new sheet or the draft sheet updated), shared with Robert and Arthur, one row per issue ENG-2438 to ENG-2463",
        "labels Nothing 6, Already told 4, Closing 6, Covered 2, Last day 6, Closing and last day 2 (First note / Date note / Full note accepted as synonyms)",
        "Series Seed 3,051,879; common 6,000,000; options now 164,114; directors Leonard Hayes and Robert; Griffin 90.0 % of the preferred",
        "14 Gmail drafts: Closing to Schaeppi, Bergmann, Enes (covering three lines), TOR, Deepak; Last day to ES-1, ES-4, ES-7, ES-13, ES-15; Closing and last day to ES-3, ES-12, ES-14 and ES-18; Claire's answers her equity question",
        "Linear: Canceled 5, Todo 14, Done 7; a reason comment on each of the 12 issues with no note of its own",
        "letter as a Google Doc in the folder, shared with Robert, updated from C0ADGSZKR3R/1770664700.848759",
        "KPMG reply to all on leonard.hayes@harmonygames.co/1857029474983245439: options at Dec 31, 2025 243,757; shares plus options 9,295,636; each fund's holding; the closing as a later event",
        "Griffin heads-up sent on leonard.hayes@harmonygames.co/1856958794180374704 naming the preferred vote",
        "thread reply under C0ADGSZKR3R/1770934638.035469 naming ES-14 (Feb 21) first",
    ],
    "alternatives_considered": [
        "three messages for the Disli family (rejected: the reply under the list says one note covers the family's lines)",
        "Segerstrale and Nebojsa owed the closing (rejected: Leonard's Feb 9 DM and Robert's Feb 12 reply are written messages about the closing sent and delivered to them directly)",
        "ES-14 and ES-18 as already told (rejected: neither has a Feb 11 letter; a channel post is not sent to them directly)",
        "owner-list lines as stock (rejected: the advisor table and the term sheet tie only after the grants come out)",
        "KPMG at today's 164,114 or the term sheet's 268,772 (rejected: KPMG fixes December 31, 2025 and effective dates as Carta shows them)",
        "266,436 at Dec 31 (rejected: the follow-up says a termination effective on the as-of date counts as of that date)",
        "the KPMG reply or the Griffin heads-up as drafts (rejected: the project says send; the notes say it can go out once the sheet is done)",
        "editing the draft sheet instead of a new sheet (accepted: same folder, contents and sharing)",
        "Tor already told by the Nov 4 DM (rejected: the DM never says the company is closing)",
        "the side letter for Tor alone (rejected: the signed chain adds Segerstrale)",
        "a new top-level #winddown post (rejected: 'reply under my list')",
    ],
}
json.dump(d, open(p, "w"), indent=1, ensure_ascii=False); open(p, "a").write("\n")
print("prompt-writing outcome review bound to", h)
