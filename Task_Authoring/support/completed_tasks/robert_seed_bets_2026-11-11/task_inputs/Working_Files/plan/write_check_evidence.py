#!/usr/bin/env python3
"""Record the prompt-check outcome review and the assigned-role review in Working_Files/00_V3_Authoring_Evidence.json,
both bound to the digest of 04_Prompt.txt (the artifact /prompt reads). Only outcome_reviews["prompt-check"] and
role_reviews["prompt-check"] are written; every other key keeps its bytes (the file round-trips through json.dumps
with indent 2, checked before writing).

Run: ~/.local/bin/python3.12 -B Task_Authoring/task_inputsS2/Working_Files/plan/write_check_evidence.py
"""
import json
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
WS = os.path.abspath(os.path.join(TI, "..", ".."))
TASK = "Task_Authoring/task_inputsS2"
P = os.path.join(WF, "00_V3_Authoring_Evidence.json")

h = subprocess.run([sys.executable, "-B", "Task_Authoring/tools/stage_gate.py", "--artifact-hash", f"{TASK}/04_Prompt.txt"],
                   cwd=WS, capture_output=True, text=True,
                   env=dict(os.environ, TASK_AUTHORING_TASK_DIR=TASK)).stdout.strip().splitlines()[-1]
if h != "d0cb08476d23":
    sys.exit(f"STOP: 04_Prompt.txt digest is {h}, not the checked d0cb08476d23; re-run the check on the new text first")

raw = open(P).read()
d = json.loads(raw)
if json.dumps(d, indent=2) != raw:
    sys.exit("STOP: the evidence file does not round-trip byte for byte; refusing to rewrite other keys")
before = {k: json.dumps(v, sort_keys=True) for k, v in d.items() if k not in ("outcome_reviews", "role_reviews")}
before_o = {k: v for k, v in d.get("outcome_reviews", {}).items() if k != "prompt-check"}
before_r = {k: v for k, v in d.get("role_reviews", {}).items() if k != "prompt-check"}

REVIEWER = ("Claude (Opus 5.5), /create-prompt-writing check C1-C24 on 04_Prompt.txt d0cb08476d23 against SQL rev6 ad50f039b5c2 "
            "(Working_Files/04_Prompt_Check.md; lookups in plan/check_r1/), testing the platform /prompt report on rev4 "
            "(plateform_reports/6aeed82596dcfe103f9f74d9_1_prompt.md: UGT 2, Clarity 1, Cross-Service Coherence 1), with one "
            "blind subagent read of the same text and the rev6 SQL on UGT, Clarity, Cross-Service Coherence and Business "
            "Function (reported in the check's Self-review)")

d.setdefault("outcome_reviews", {})["prompt-check"] = {
    "artifact": "04_Prompt.txt",
    "artifact_hash": h,
    "reviewer": REVIEWER,
    "rationale": (
        "The prompt names every destination the persona knows: a sheet in Robert's Drive, shared with Leonard and Blake; the "
        "Payee history project in Linear; a reply to Leonard in #winddown. It points at Leonard's two #winddown posts "
        "(C0ADGSZKR3R/1770945821.640039, C0ADGSZKR3R/1770945859.212469) for the rules and the layout. Those posts name the method "
        "f_6feda53b2382c63bf47b25 and the working sheet f_3304033843904a426f3c00, and say 'I'll update it myself' about the deck "
        "f_a4b3c4287a4314d8e532e1. Every material field is settled by the prompt, the incorporated method or a dated record Robert "
        "can read: Leapblock's closing statement C05URGU759U/1770971846.479179, the returned-wire notes C04UEQVDVB7/1712901800.684259, "
        "five Western Union receipts, Arthur's Chase mail in Robert's INBOX, and Leonard's ENG-2459 note. The fields left open are "
        "representational and each is accepted: title, folder, share role, column order, where the brought-in figures and the "
        "Marketing dollars sit, thread or top-level placement in #winddown, rounding, and an extra comment or a deck edit. On "
        "rev6 the platform's two record gaps are closed: Leonard's own note on ENG-2455 "
        "(comment_990674712ad0127e26f780eadb5418ea) makes Lauren Brooks Marketing, and the method holds Combo Fighter's revenue "
        "'on the page, on the deck and when you tell me', so no Combo Fighter revenue figure is expected or graded. ENG-2454's "
        "note now names the laptop, so Martin is Company. No figure is left to a choice between sources, so no "
        "BOTH_FAIR_FIGURE is recorded."),
    "accepted_outcomes": [
        "a Google Sheet owned by Robert in his Drive (root d_9f7ba94f7526d54d8482ba or any folder he owns), any title, a copy of the working sheet's layout also fine, shared with leonard.hayes@harmonygames.co and arthur.blake@harmonygames.co as editor, commenter or viewer",
        "the layout of f_3304033843904a426f3c00: Payee, Name on the bank, Bucket, Domino Delights, ZM, Combo Fighter, Company, Note; extra columns, a totals row and any column order allowed",
        "22 payee rows (ENG-2438 to ENG-2459), matched on account endings, zero rows kept; Payee label free (bank spelling or the name the notes give)",
        "build cost per bet Domino Delights 959,342.64, ZM 544,433.44, Combo Fighter 72,685.61 (to the cent, whole dollars, or rounded in the reply: $959K / $544K / $73K, $0.96M / $0.54M, $72.7K)",
        "Marketing dollars (ENG-2441, ENG-2444, ENG-2448, ENG-2451, ENG-2455 Lauren Brooks per Leonard's note; ENG-2459 at zero) in the bet columns or in the row with the bet named, never inside a build total; Company 49,625.00 in the Company column (ENG-2443, ENG-2445, ENG-2446, ENG-2452, ENG-2458), with or without the same amount in a bet cell; ENG-2454 1,999.00 BGN on its line (Company cell or Note; 'paid him direct for his laptop'), never in a dollar total; ENG-2450 at zero with any no-cost label",
        "brought in, lifetime, from ANALYTICS.MONETIZATION.REVENUE_DAILY as recorded: Domino Delights 12,331.25 and ZM 11.99 (REVENUE_DAILY_V2 gives the same sums), anywhere on the sheet, exact or rounded in the reply; Combo Fighter's left off the sheet, the deck change and the reply (blank, omitted, or marked held until its first sales are checked), per the method's 'Leave Combo Fighter’s revenue off for now'",
        "all 22 issues ENG-2438 to ENG-2459 moved to Done, with a reason comment first on ENG-2439, ENG-2442, ENG-2447, ENG-2450 and ENG-2459; any assignee; an extra comment on another issue is not penalised",
        "one Slack message from Robert in #winddown C0ADGSZKR3R to Leonard: in the thread of C0ADGSZKR3R/1770945859.212469, in the thread of C0ADGSZKR3R/1770945821.640039, or top-level; with each bet's build cost, what Domino Delights and ZM brought in (Combo Fighter's held), what changes on the draft deck (the three cost figures $985K / $609K / $74K move to the new ones and the brought-in slide gets Domino Delights and ZM), and the sheet's link",
        "the draft deck f_a4b3c4287a4314d8e532e1 left for Leonard ('I'll update it myself'); an edit to it is not penalised",
        "the Trello card 698e55f9af74d68d679de7b3 left untouched",
    ],
    "alternatives_considered": [
        "edit Leonard's working sheet f_3304033843904a426f3c00 in place (rejected: the prompt says 'in my Drive' and C0ADGSZKR3R/1770945859.212469 says 'keep yours in your drive')",
        "a one-page doc instead of a sheet (rejected: 'Build that page as a sheet'); a doc beside the sheet changes no graded write",
        "the quick-pass figures 984,888.21 / 608,820.50 / 73,685.61 or the deck's $985K / $609K / $74K as the build cost (rejected: the method f_6feda53b2382c63bf47b25 says 'A notice is where you start, not the last word', keeps Marketing out of build cost, puts Company in its own column, and replaces the quick plan on 698e55f9af74d68d679de7b3)",
        "Leapblock at the notices' 374,654 (rejected: 'If someone we paid closes out their file with us and tells us what they received, that beats the notices for them' and the newer statement C05URGU759U/1770971846.479179: 30 wires, 407,944; case K49-newer-source)",
        "MotMot ***8605 kept at 4,032 (rejected: 'Take a notice as paid unless one of us has said the money came back' and C04UEQVDVB7/1712901800.684259 'bank returned our money')",
        "Lucas at the notices' 6,450 or with the forwarded receipt counted twice (rejected: the receipt sentence admits the five Western Union receipts 'at the amount sent, not the fee', 7,525.00 by tracking number, so 13,975.00)",
        "ENG-2450 JPMorgan ***3203 kept at 4,000 or booked to Company (rejected: Arthur's mail in Robert's INBOX says it went to the company's own Chase account, and the method says 'Money we moved between our own accounts isn't spending, no bucket for that')",
        "ENG-2459 kept at 125 or counted from the Payoneer re-send (rejected: Leonard's note 'that wire came back the same day, I'd already re-sent it through payoneer' takes the notice out, and Robert's mail holds two Dixelar payment requests but no receipt; the line is Marketing, so no build total moves)",
        "Lauren Brooks (ENG-2455) as Build by date, the platform's rev4 Reading B, on her 'Telegram Contractor' contact row 564155d70112411151e512a6 and her monthly contract, which would make ZM 544,933.44 and Combo Fighter 73,685.61 (rejected on rev6: Leonard's note on ENG-2455 comment_990674712ad0127e26f780eadb5418ea 'her contract had her running our paid UA on telegram, so she’s marketing, not build', borne out by the contract f_20a0df3860bb5731d22f07 'run and optimize paid UA for Telegram' and the method's 'Marketing is anything made or bought to get installs')",
        "Lauren Brooks as Company (rejected, as the platform did: her work was for the games, starting with a Domino Delights experiment, C05KNDCHAAG/1760125440.959149)",
        "Martin Walsh (ENG-2454) as Build, ZM by date, the platform's rev4 reading (rejected on rev6: the note reads 'paid him direct for his laptop, not through Leapblock', with C04UEQVDVB7/1761844454.096829, and the method puts equipment in Company)",
        "Combo Fighter's warehouse revenue reported on the sheet, the deck change or the reply because the prompt asks what each bet brought in (rejected: the incorporated method says 'Leave Combo Fighter’s revenue off for now, on the page, on the deck and when you tell me, until we’ve checked its first sales'; no rubric slot grades a Combo Fighter figure)",
        "ENG-2459 counted from Leonard's Payoneer receipt (rejected: it sits only in Leonard's mailbox, outside Robert's view, and the method counts a receipt that 'reached your mail')",
        "the brought-in figures only in the reply (rejected: the page is 'what each bet cost us to build and what it brought in' and the prompt says 'Build that page as a sheet')",
        "Marketing added into each bet's build cost (rejected: the method says 'keep it out of build cost')",
        "only the issues whose figure differs moved, or none moved (rejected: the method's last paragraph says to move each payee's issue to Done once its line is right)",
        "the reply only under the post that says 'tell me here', or only as a top-level post (accepted either way: same channel, recipient and contents)",
        "edit the deck as well as report the changes (accepted, not required: Leonard says 'I'll update it myself')",
        "REVENUE_DAILY_V2 instead of REVENUE_DAILY (accepted: the sums are equal)",
    ],
}

d.setdefault("role_reviews", {})["prompt-check"] = {
    "artifact": "04_Prompt.txt",
    "artifact_hash": h,
    "reviewer": REVIEWER,
    "persona_role": "Co-founder & Creative Director",
    "rationale": (
        "Robert is one of the three co-founders winding the company down: he is a member of the private #winddown channel "
        "C0ADGSZKR3R, where on Feb 12 Leonard lists 'Reaching out to our angels properly and let them know about the situation' as "
        "his next step (C0ADGSZKR3R/1770934638.035469). On Thursday Feb 12, 5:23 PM PT Leonard @-mentions Robert there and asks "
        "him to own one straight page on what each bet cost to build and brought in, before the angel calls on Tuesday Feb 17 "
        "(C0ADGSZKR3R/1770945821.640039; Robert is an attendee of evt_f21476dc404329f67fd60d). Leonard's reason is 'you know what "
        "each of these people did better than I do'. Robert handled contractor payments with his co-founders: he sent Lucas's "
        "payments 'via company card' (C04UEQVDVB7/1719603595.852129) and talked through how to book the returned wire with Leonard "
        "(C04UEQVDVB7/1712901837.860709). Preparing an investor-facing account of how the seed money was spent, and sending it "
        "back to his co-founder, is a founder's work: Robert prepares and Leonard presents. The Creative Director title is no "
        "obstacle. The ask is a founder's, not a department's, and the V3 rule judges role plausibility only. A better-fitting "
        "colleague, such as Leonard himself, would not make it a Fail."),
    "source_ids": ["C0ADGSZKR3R/1770945821.640039", "C0ADGSZKR3R/1770945859.212469", "C0ADGSZKR3R/1770934638.035469",
                   "evt_f21476dc404329f67fd60d", "C04UEQVDVB7/1719603595.852129", "C04UEQVDVB7/1712901837.860709",
                   "d_9f7ba94f7526d54d8482ba"],
}

after = {k: json.dumps(v, sort_keys=True) for k, v in d.items() if k not in ("outcome_reviews", "role_reviews")}
assert after == before, "a key other than the two prompt-check reviews changed"
assert {k: v for k, v in d["outcome_reviews"].items() if k != "prompt-check"} == before_o
assert {k: v for k, v in d["role_reviews"].items() if k != "prompt-check"} == before_r
with open(P, "w") as f:
    f.write(json.dumps(d, indent=2))
print("prompt-check outcome + role reviews bound to", h)
