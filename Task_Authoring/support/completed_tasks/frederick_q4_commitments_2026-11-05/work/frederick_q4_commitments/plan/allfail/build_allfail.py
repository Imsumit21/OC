#!/usr/bin/env python3
"""Write 11_AF_Justification.md (workbook) and 11_Baseline_AllFail_Justifications.md (screen file) for
frederick_q4_commitments, rev4 baseline. The screen paragraphs are the workbook's Justification lines, rendered verbatim.
Evidence: run_forensics/rev4/baseline/run-*/calls.jsonl + writes.json (trajectory_ledger over 07_Baseline_Trajectories),
af_writes.json / af_verifier.json next to this script, and the probes in af_evidence.py (first result event that holds each
deciding record's text; NEVER SEEN in every run)."""
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WF = HERE.parents[1]
TI = WF.parent
WS = TI.parents[1]
RUB = json.loads((TI / "09_Rubrics.json").read_text())
RAW = (TI / "09_Rubrics.json").read_text()
CTX = json.loads((WF / "00_Task_Context.json").read_text())
CLOCK = CTX["universe"]["clock_line"]
F = {1: "trajectory-run-1 (2).json", 2: "trajectory-run-2.json", 3: "trajectory-run-3.json", 4: "trajectory-run-4.json",
     5: "trajectory-run-5.json", 6: "trajectory-run-6.json"}
LOG = {1: 409, 2: 406, 3: 680, 4: 376, 5: 316, 6: 386}
HUB = {1: 627, 2: 620, 3: 687, 4: 585, 5: 509, 6: 594}
EXEC = {1: (34, "Sep 26"), 2: (30, "Sep 26"), 3: (32, "Sep 28"), 4: (27, "Sep 26"), 5: (28, "Sep 26"), 6: (32, "Sep 28")}
FW_ANS = {1: 439, 2: 475, 3: 477, 4: 425, 5: 339, 6: 543}
LF_ANS = {1: 469, 2: 500, 3: 539, 4: 448, 5: 369, 6: 569}
SP_ANS = {1: 447, 3: 483, 4: 433, 5: 347, 6: 551}
CARDS = {1: (522, 534, 7), 2: (410, 422, 7), 3: (566, 576, 6), 4: (382, 394, 7), 5: (396, 406, 6), 6: (465, 477, 7)}
JAN5 = {1: (537, 557, 11), 2: (592, 612, 11), 3: (582, 606, 13), 4: (557, 577, 11), 5: (409, 433, 13), 6: (480, 498, 10)}
CONTACTS = {1: (621, 31), 2: (589, 30), 3: (674, 31), 4: (553, 31), 5: (506, 31), 6: (452, 30)}
ROWS = {1: 34, 2: 33, 3: 34, 4: 34, 5: 34, 6: 33}
LF_DEC = {1: "Sign", 2: "Sign", 3: "Park", 4: "Sign", 5: "Park", 6: "Sign"}
W = json.loads((HERE / "af_writes.json").read_text())


def title(r):
    return RUB[r - 1]["title"]


def quote(r):
    """The criterion exactly as it stands in the raw JSON text (escaped quotes kept), so the gate's substring test holds."""
    t = json.dumps(title(r), ensure_ascii=False)[1:-1]
    assert t in RAW, r
    return t


def ev(fn):
    return " · ".join(f"run-{k}: {fn(k)} ({F[k]} event {e})" for k, e in ((k, fn.ev(k)) for k in range(1, 7)))


class E:
    def __init__(self, text, event):
        self.text, self.event = text, event

    def __call__(self, k):
        return self.text(k)

    def ev(self, k):
        return self.event(k)


NIN_PROBE = ("never opened either Nintendo Developer Portal notice (threads 1842358947604469113 and 1842359398719557772) and "
             "made 0 Linear calls")
FW_PROBE = "read #executives top level only from {d} (event {e}), opened no Slack thread, never searched Maren"
LF_PROBE = "never read Leonard's DM reply D05S58U4SAK/1759174260.052645 (no result event holds its text)"
SP_PROBE = "read #executives only from {d} (event {e}); Robert's Sep 17 post C07C2866011/1758134460.899858 is in no result"
BAL_PROBE = {1: "Balancy only in a thread list (event 352)", 2: "opened thread 1840501641217286806 in minimal format, 100-character "
             "snippets (event 234)", 3: "Balancy only in a listing (event 74)", 4: "Balancy in no result", 5: "Balancy only in a "
             "listing (event 62)", 6: "Balancy in no result"}

TESTS_COMMON = ("capability SUPPORTED (the runs used the catalog write tools gsheets_values_append, gmail_reply_to_message, "
                "gmail_send_message, trello_create_card, contacts_add_new_contact and gcal_create_event) · phrasing affirmative, "
                "Agent-centric, no tool name; do-nothing case REJECT · friction none (03_Error_Async_Config.txt 'Friction: none'; "
                "no forced error or async wait in any run)")
AUTH_SCOPE = ("authority: prompt 'going by his email for what needs doing and how we decide each one'; Leonard's Sep 30 email "
              "incorporates the guardrails doc f_b98287f6f80fe431a71209, the folder README f_846ddc38b2aab3d2ed3fcb and ESG's note")

B = []  # (rid, weight, evidence, tests, causation, shared, justification)


def block(r, evidence, tests, causation, shared, just):
    B.append((r, evidence, tests, causation, shared, just))


# ---------------------------------------------------------------- R5 · 36 rows
block(5, ev(E(lambda k: f"log append writes {ROWS[k]} rows, no Nintendo or Balancy row"
              + {2: ", no Spotlight Fest row", 6: ", no Hootline row"}.get(k, "") + f"; {NIN_PROBE if k == 1 else 'no Nintendo notice opened'}; "
              + BAL_PROBE[k], lambda k: LOG[k])),
      f"{AUTH_SCOPE}; Leonard's scope sentence ('anyone outside the investor work who has an offer, a trial, a quote, terms or an "
      "ask in front of us and that one of us has actually engaged with') and README ('one row per company') · grounding: 36 = "
      "the 33 filed papers in d_ffa3e6e473da7e6523614f + Hootline thread frederick.stone@harmonygames.co/1839631800730308867 + "
      "Balancy thread frederick.stone@harmonygames.co/1840501641217286806 + Nintendo notices, all dated before 2025-10-01T00:00Z · "
      "reachability: PROMPT_LINKED (Leonard's email scopes Frederick's inbox); persona_view can-see YES for threads "
      "1840501641217286806, 1842358947604469113, 1842359398719557772 · atomicity/destination: one count on the log sheet the "
      "prompt names (volume control) · precision/flexibility: exact count, any order, duplicates count once; no rejected fair "
      "alternative (every run's shortfall is a missing in-scope company) · " + TESTS_COMMON,
      "no test fails", "Nintendo (R6, R18, R79, R96) and Balancy (R15, R82, R86)",
      "Leonard's Sep 30 email puts in scope everyone with an offer, a trial, a quote, terms or an ask that one of us engaged with, "
      "which is 36 companies, and every run logged 33 or 34. All six runs left off Nintendo, whose Developer Portal mail in "
      "Frederick's inbox includes 'Global Terms of Service & NDA Acceptance Required' (thread 1842358947604469113), and Balancy, "
      "whose thread 1840501641217286806 holds Leonard's Sep 11 reply to their ask to revisit implementing Balancy. No run opened "
      "either Nintendo notice, and no run read Leonard's Balancy reply in full; run 2 saw only its 100-character snippet. Runs 1, "
      "3, 4 and 5 wrote 34 rows, while run 2 also dropped Spotlight Fest and run 6 also dropped Hootline, for 33.")
NIN_TESTS = (f"{AUTH_SCOPE}; guardrails step 4 ('If it costs nothing before January but taking it means someone has to accept "
             "terms or sign for the company, it goes the way ESG's note says') · grounding: Linear ZOM-567 comment "
             "cmt_c9a6660d81e067ad1de7 by Arthur, 2025-09-25T18:20Z ('the Global ToS and NDA still needs our agreement approver "
             "to accept it'; 'It has to be accepted by Oct 15 or the request lapses'); notices 1842358947604469113 ('Global Terms "
             "of Service & NDA Acceptance Required') and 1842359398719557772 ('Registration Completed'), both 2025-09-04 · "
             "reachability: PROMPT_LINKED (Leonard's scope covers 'terms ... in front of us'; the notices are in Frederick's inbox, "
             "can-see YES; Linear is unscoped, and search 'Nintendo' finds ZOM-567 through its description 'Fred registered us on the "
             "Nintendo developer portal on Sep 4') · ")
# ---------------------------------------------------------------- R6 · Nintendo Sign
block(6, ev(E(lambda k: f"log append has no Nintendo row; {NIN_PROBE}", lambda k: LOG[k])),
      NIN_TESTS + "atomicity/destination: one Decision cell on the Nintendo row · precision/flexibility: 'Sign' is the README "
      "word, and 'Nintendo Developer Portal' is accepted; no run wrote any Nintendo row, so no alternative was rejected · "
      + TESTS_COMMON, "no test fails", "Nintendo (R5, R18, R79, R96)",
      "Nintendo needed the Decision Sign because Arthur's Sep 25 comment on Linear ZOM-567 says the Global ToS and NDA still "
      "needs a company officer to accept it by Oct 15, and none of the 6 runs logged Nintendo at all. Guardrails step 4 sends "
      "anything that costs nothing but needs someone to accept terms for the company to Sign, and Leonard's email brings terms in "
      "front of us into scope. Frederick's inbox holds the portal's 'Global Terms of Service & NDA Acceptance Required' notice "
      "(thread 1842358947604469113), and searching Linear for Nintendo finds ZOM-567, whose description says Fred registered "
      "on the Nintendo developer portal on Sep 4. No run opened either Nintendo notice or made a single Linear call, so no "
      "run's log has a Nintendo row.")
FW_TESTS = (f"{AUTH_SCOPE}; Leonard's email 'plus the one change I posted in #executives on Monday'; guardrails step 5 "
            "('Everything else that's free until January ... Tell them we'll pick it up in January') · grounding: Leonard's "
            "thread reply C07C2866011/1758920520.674991, 2025-09-26T21:02Z ('Maren called me back about the Pro plan. they'll hold "
            "it at no charge until Feb 1 with nothing to sign before then'), under the Sep 22 root 1758513190.847889 (reply_count 1, "
            "latest_reply 1758920520.674991); order form f_fba21c2d5d4bbb02983961 ('Billing starts: Nov 1, 2025') · reachability: "
            "PROMPT_LINKED (#executives is the channel Leonard's email points to; Frederick is a member, check-sql YES; Slack search "
            "'Maren', the sender of Framewell's own mail, returns the reply) · ")
# ---------------------------------------------------------------- R7 · Framewell Park
block(7, ev(E(lambda k: f"logs Framewell Decision 'End'; {FW_PROBE.format(d=EXEC[k][1], e=EXEC[k][0])}", lambda k: LOG[k])),
      FW_TESTS + "atomicity/destination: one Decision cell on the Framewell row · precision/flexibility: Park is the only fair "
      "Decision once the reply is read (End rests on the superseded order form) · " + TESTS_COMMON, "no test fails",
      "Framewell (R52, R86, R87)",
      "Framewell needed the Decision Park, because Leonard's Sep 26 reply in an #executives thread (C07C2866011/1758920520.674991) "
      "says Maren will hold the Pro plan at no charge until Feb 1, and all 6 runs logged End. Framewell's order form bills $149 a "
      "month from Nov 1, which fails the cash test on its own, but the reply says 'nothing from them lands before January. treat "
      "them like the other free ones', which is guardrails step 5, Park. Leonard's email points to #executives for the rules, and "
      "Frederick is a member of the channel. Every run read #executives only from Sep 26 or Sep 28 at the top level, opened no "
      "Slack thread and never searched for Maren, the sender of Framewell's mail, so no run saw the reply.")
LF_TESTS = (f"{AUTH_SCOPE}; guardrails step 1 ('If one of us has already given them an answer, don't write to them again. Note "
            "who answered and when. If the answer was \"later\", it comes back at the January commitments review'); README "
            "('Answered by: who on our side already answered them') · grounding: Leonard's DM reply D05S58U4SAK/1759174260.052645, "
            "2025-09-29T19:31Z ('I rang Wen back on Saturday about their Southeast Asia deal and let them know Southeast Asia has "
            "to wait until after the raise. we'll pick it up again in January'), under the Sep 17 root 1758151772.570449 "
            "(reply_count 1, latest_reply 1759174260.052645); Lanternfly thread frederick.stone@harmonygames.co/1842800807116855774 "
            "(Wen Halvorsen) · reachability: PROMPT_LINKED (Frederick's own DM with Leonard, check-sql YES; Slack search 'Wen' or "
            "'Southeast Asia', the contact and subject of Lanternfly's mail, returns the reply; run-3 event 352 shows that "
            "search returns DM thread replies) · ")
# ---------------------------------------------------------------- R8 · Lanternfly Answered
block(8, ev(E(lambda k: f"logs Lanternfly Publishing Decision '{LF_DEC[k]}'; {LF_PROBE}; replies to Wen again at event {LF_ANS[k]}",
              lambda k: LOG[k])),
      LF_TESTS + "atomicity/destination: one Decision cell on the Lanternfly row · precision/flexibility: step 1 is first-fit, "
      "so Answered is the only fair Decision; Sign and Park rest on the deck without the answer · " + TESTS_COMMON,
      "no test fails", "Lanternfly (R13, R24, R28, R86)",
      "Lanternfly Publishing needed the Decision Answered, because Leonard's Sep 29 reply in his DM with Frederick "
      "(D05S58U4SAK/1759174260.052645) says he rang Wen and told them Southeast Asia waits until after the raise. Guardrails step "
      "1 comes first: if one of us has already given them an answer, don't write to them again, and note who answered and when. "
      "The DM is Frederick's own, and the reply names Wen and their Southeast Asia deal, the contact and subject of Lanternfly's "
      "own thread. No run read that reply; runs 1, 2, 4 and 6 logged Sign from the deck's exclusive term, and runs 3 and 5 logged "
      "Park. All 6 runs then wrote to Wen again, which step 1 rules out.")
SP_TESTS = (f"{AUTH_SCOPE}; guardrails step 1 (as above); README Answered by · grounding: Robert's top-level #executives post "
            "C07C2866011/1758134460.899858, 2025-09-17T18:41Z ('had the call about the Dec 5 indie showcase. we're sitting this "
            "one out this year, I let Rina know'); Spotlight Fest thread frederick.stone@harmonygames.co/1842712097588195482 (Rina "
            "Takeda: 'showcase slot, Dec 5'; 'Could we set up a quick call?') · reachability: PROMPT_LINKED (#executives, "
            "check-sql YES; Slack search 'Rina' or 'showcase' returns the post) · ")
# ---------------------------------------------------------------- R9 · Spotlight Answered
block(9, ev(E(lambda k: ("has no Spotlight Fest row; " if k == 2 else "logs Spotlight Fest Decision 'End'; ")
              + SP_PROBE.format(d=EXEC[k][1], e=EXEC[k][0]) + (f"; replies to Rina at event {SP_ANS[k]}" if k in SP_ANS else ""),
              lambda k: LOG[k])),
      SP_TESTS + "atomicity/destination: one Decision cell on the Spotlight Fest row · precision/flexibility: Answered is the only "
      "fair Decision once the post is read · " + TESTS_COMMON, "no test fails", "Spotlight (R14, R28)",
      "Spotlight Fest needed the Decision Answered, because Robert's Sep 17 #executives post (C07C2866011/1758134460.899858) says "
      "he had the call about the Dec 5 indie showcase and let Rina know we're sitting it out. Guardrails step 1 says an answer "
      "already given by one of us settles the row, and Rina's Sep 8 mail asks for exactly that call about the Dec 5 showcase. "
      "Frederick is a member of #executives, but every run read the channel only from Sep 26 or Sep 28, and the five runs that "
      "searched Slack for it used Spotlight, a word the post never uses. Runs 1, 3, 4, 5 and 6 logged End and wrote to Rina again, and run 2 left Spotlight "
      "Fest off the log.")
# ---------------------------------------------------------------- R13 · Lanternfly Answered by Leonard
block(13, ev(E(lambda k: f"Lanternfly row has Answered by empty, Decision '{LF_DEC[k]}'; {LF_PROBE}", lambda k: LOG[k])),
      LF_TESTS + "atomicity/destination: one Answered by cell on the Lanternfly row · precision/flexibility: 'Leonard' or "
      "'Leonard Hayes', with or without the date · " + TESTS_COMMON, "no test fails", "Lanternfly (R8, R24, R28, R86)",
      "The Lanternfly Publishing row needed Leonard in Answered by, because only Leonard's Sep 29 DM reply "
      "(D05S58U4SAK/1759174260.052645) records that he rang Wen on Saturday, and all 6 runs left the cell empty. The README "
      "defines Answered by as who on our side already answered them, and guardrails step 1 says to note who answered and when. "
      "The reply sits in Frederick's own DM with Leonard and names Wen, Lanternfly's contact, and their Southeast Asia deal. No run "
      "read it, so none treated Lanternfly as answered: runs 1, 2, 4 and 6 logged Sign, runs 3 and 5 logged Park, and every run "
      "left Answered by blank.")
# ---------------------------------------------------------------- R14 · Spotlight Answered by Robert
block(14, ev(E(lambda k: ("has no Spotlight Fest row" if k == 2 else "Spotlight Fest row has Answered by empty")
               + ("; What's waiting reads 'call held with Robert, Sep 17'" if k == 1 else "") + "; "
               + SP_PROBE.format(d=EXEC[k][1], e=EXEC[k][0]), lambda k: LOG[k])),
      SP_TESTS + "atomicity/destination: one Answered by cell on the Spotlight Fest row · precision/flexibility: 'Robert', with "
      "or without the date · " + TESTS_COMMON, "no test fails", "Spotlight (R9, R28)",
      "The Spotlight Fest row needed Robert in Answered by, because Robert's Sep 17 #executives post "
      "(C07C2866011/1758134460.899858) says he let Rina know we're sitting out the Dec 5 showcase, and no run of 6 put him there. "
      "The README defines Answered by as who on our side already answered them, and Frederick is a member of #executives. No run "
      "opened the post: runs 1, 3, 4, 5 and 6 logged Spotlight Fest as End with Answered by empty, and run 2 had no Spotlight "
      "Fest row. Run 1 even noted 'call held with Robert, Sep 17' in What's waiting but never checked what Robert had told Rina.")
# ---------------------------------------------------------------- R15 · Balancy Answered by Leonard
block(15, ev(E(lambda k: f"log append has no Balancy row; {BAL_PROBE[k]}; no result holds Leonard's 'circle back with you as soon "
               "as we get some bandwidth'", lambda k: LOG[k])),
      f"{AUTH_SCOPE}; Leonard's scope sentence; guardrails step 1; README Answered by · grounding: base thread "
      "frederick.stone@harmonygames.co/1840501641217286806 (Balancy, Sep 11 14:54 MDT: 'revisit our conversation regarding the "
      "implementation of Balancy in Zombie Match 3D'; Leonard, Sep 11 17:21 PDT: 'we'll circle back with you as soon as we get "
      "some bandwidth'), read through hg.py get-many · reachability: PROMPT_LINKED (Frederick's own mailbox, can-see YES; Gmail "
      "search 'Balancy' finds it) · atomicity/destination: one Answered by cell on the Balancy row · precision/flexibility: "
      "'Leonard' or 'Leonard Hayes'; the date is not graded, so the Sep 11 PT / Sep 12 UTC split rejects nothing · " + TESTS_COMMON,
      "no test fails", "Balancy (R5, R82, R86)",
      "The Balancy row needed Leonard in Answered by, because his Sep 11 reply in thread 1840501641217286806 ('we'll circle "
      "back with you as soon as we get some bandwidth') says later, and no run of 6 logged Balancy. Balancy "
      "is in Leonard's scope: he held a call with them in August, and their Sep 11 mail asks to revisit implementing Balancy in "
      "Zombie Match 3D. The thread is in Frederick's own mailbox, and guardrails step 1 records an answer one of us already gave. "
      "Runs 1, 2, 3 and 5 saw Balancy in inbox listings, and run 2 opened the thread with only 100-character snippets, but no "
      "run read Leonard's reply or added a Balancy row.")
# ---------------------------------------------------------------- R18 · Nintendo Next date
block(18, ev(E(lambda k: f"log append has no Nintendo row and so no Oct 15 date; {NIN_PROBE}", lambda k: LOG[k])),
      NIN_TESTS + "atomicity/destination: one Next date cell on the Nintendo row · precision/flexibility: Oct 15, 2025 in any "
      "date form (a date-only deadline; no PT/UTC split) · " + TESTS_COMMON, "no test fails", "Nintendo (R5, R6, R79, R96)",
      "The Nintendo row needed the Next date Oct 15, 2025, the deadline in Arthur's Sep 25 Linear comment on ZOM-567 ('It has "
      "to be accepted by Oct 15 or the request lapses'), and none of the 6 runs logged Nintendo. The README gives Sign rows the "
      "date they need it by, and the comment is the only record that holds this date. Searching Linear for Nintendo finds "
      "ZOM-567, whose description says Fred registered on the Nintendo developer portal on Sep 4, and Frederick's inbox holds "
      "the portal's 'Global Terms of Service & NDA Acceptance Required' notice (thread 1842358947604469113). No run opened either Nintendo notice or made any Linear call, so no log has a "
      "Nintendo row or this date.")
# ---------------------------------------------------------------- R24 · Lanternfly told
TOLD = {1: "with our lawyers (ESG) first, then Leonard or Arthur to sign", 2: "with our lawyers (ESG) first, then Leonard or Arthur to sign",
        3: "won't make their Q4 slate; we'll pick it up in January", 4: "with ESG first, then Leonard to sign",
        5: "We'll pick it up in January.", 6: "With our lawyers first, then Leonard to sign"}
block(24, ev(E(lambda k: f"Lanternfly What we told them reads '{TOLD[k]}'; {LF_PROBE}", lambda k: LOG[k])),
      LF_TESTS + "atomicity/destination: one What we told them cell on the Lanternfly row · precision/flexibility: any wording "
      "that the deal waits until after the raise, with or without January · " + TESTS_COMMON, "no test fails",
      "Lanternfly (R8, R13, R28, R86)",
      "The Lanternfly Publishing row needed What we told them to say Southeast Asia waits until after the raise, Leonard's words in "
      "his Sep 29 DM reply (D05S58U4SAK/1759174260.052645), and all 6 runs wrote something else. The column records what we told "
      "them, and Leonard had already told Wen on Saturday, Sep 27. The reply is in Frederick's own DM with Leonard and names Wen "
      "and the Southeast Asia deal. No run read it: runs 1, 2, 4 and 6 wrote that the deal is with our lawyers and then Leonard or "
      "Arthur to sign, and runs 3 and 5 wrote that we'll pick it up in January.")
# ---------------------------------------------------------------- R28 · 31 answers
ANS_N = {1: 33, 2: 32, 3: 33, 4: 33, 5: 33, 6: 32}
block(28, ev(E(lambda k: f"answers reach {ANS_N[k]} companies: Wen at Lanternfly (event {LF_ANS[k]})"
               + (f" and Rina at Spotlight Fest (event {SP_ANS[k]})" if k in SP_ANS else "") + " were written to again"
               + ("; Hootline never answered" if k == 6 else ""), lambda k: LF_ANS[k])),
      f"{AUTH_SCOPE}; Leonard's email ('Everyone who is waiting to hear from us should get a written answer this week'); "
      "guardrails step 1 ('don't write to them again') and Answers ('Portals and no-reply notices don't need one') · grounding: "
      "31 = 36 companies less the four Answered (Lanternfly D05S58U4SAK/1759174260.052645, Spotlight "
      "C07C2866011/1758134460.899858, Balancy 1840501641217286806, Motive Forge 1843346276352084348) and the Nintendo portal · "
      "reachability: PROMPT_LINKED, as for R8 and R9 · atomicity/destination: one count over sent mail (volume control; each "
      "answer has its own row C29 to C63) · precision/flexibility: each company counted once however many emails; the "
      "billing@paylane.io cancellation counts as Clipforge's · " + TESTS_COMMON, "no test fails",
      "Lanternfly (R8, R13, R24, R86) and Spotlight (R9, R14)",
      "Exactly 31 companies were owed a written answer, and every run wrote to 32 or 33, because each wrote again to a company "
      "Leonard or Robert had already answered. Leonard's email asks for a written answer to everyone waiting, and guardrails step "
      "1 says that if one of us has already given them an answer, don't write to them again. Lanternfly Publishing was answered "
      "in Leonard's Sep 29 DM reply and Spotlight Fest in Robert's Sep 17 #executives post. All 6 runs replied to Wen at "
      "Lanternfly, and runs 1, 3, 4, 5 and 6 also replied to Rina at Spotlight Fest. That gives 33 companies in runs 1, 3, 4 and "
      "5, and 32 in run 2 and in run 6, which also never answered Hootline.")
# ---------------------------------------------------------------- R52 · Maren: January
FW_TXT = {1: "We've decided not to set up Pro", 2: "We won't be taking Pro", 3: "please don't set up Pro for Nov 1",
          4: "We won't be moving to Pro", 5: "We've decided not to take Framewell Pro", 6: "We won't be moving to Pro"}
block(52, ev(E(lambda k: f"only mail to PERSON_9701_EMAIL declines: '{FW_TXT[k]}'; {FW_PROBE.format(d=EXEC[k][1], e=EXEC[k][0])}",
               lambda k: FW_ANS[k])),
      FW_TESTS + "atomicity/destination: one answer to one recipient · precision/flexibility: picking it up, revisiting it or "
      "deciding in January, any wording; a decline is the wrong decision, not a fair alternative · " + TESTS_COMMON,
      "no test fails", "Framewell (R7, R86, R87)",
      "Maren Holt needed to hear that Harmony Games will pick Framewell up in January, the guardrails step 5 answer, and all 6 "
      "runs declined Pro instead. Leonard's Sep 26 reply in an #executives thread (C07C2866011/1758920520.674991) says Maren will "
      "hold Pro at no charge until Feb 1 with nothing to sign, which makes Framewell Park, and step 5 says to tell them we'll pick "
      "it up in January. Framewell's own order form bills $149 a month from Nov 1, and that is what every run acted on. No run "
      "read the reply, so each sent Maren a decline on the Framewell thread, such as run 1's 'We've decided not to set up Pro'.")
# ---------------------------------------------------------------- R79 · Nintendo card
block(79, ev(E(lambda k: f"creates {CARDS[k][2]} To Do cards (events {CARDS[k][0]} to {CARDS[k][1]}), none naming Nintendo; "
               + NIN_PROBE, lambda k: CARDS[k][0])),
      NIN_TESTS.replace(AUTH_SCOPE, AUTH_SCOPE + "; prompt 'the cards for anything that needs signing go on our Harmony Games "
                        "board'; Leonard's Sep 25 reply under ESG's note ('put it on our founders' board To Do list with the "
                        "company's name in the card title')") + "atomicity/destination: one card in list 640643a3fd8f3ca308d93195 "
      "· precision/flexibility: any title naming Nintendo (or Nintendo Developer Portal) and no other company waiting to sign · "
      + TESTS_COMMON, "no test fails", "Nintendo (R5, R6, R18, R96)",
      "A card of its own for Nintendo was needed in the To Do list, because Arthur's Sep 25 Linear comment on ZOM-567 says the "
      "portal's Global ToS and NDA waits on an officer to accept it, and none of 6 runs made one. Leonard's Sep 25 reply under "
      "ESG's note asks for anything waiting on Arthur or him to sign to go on the founders' board To Do list with the company's "
      "name in the card title. The comment leaves the acceptance for Leonard or Arthur, by Oct 15. No run opened either Nintendo "
      "notice in Frederick's inbox or searched Linear, where a search for Nintendo finds ZOM-567; runs 1, 2, 4 and 6 created seven signing cards and runs 3 and 5 six, "
      "none of them for Nintendo.")
# ---------------------------------------------------------------- R82 · 32 contacts
CT_MISS = {1: "Balancy", 2: "Balancy and Rina Takeda (Spotlight Fest)", 3: "Balancy", 4: "Balancy", 5: "Balancy",
           6: "Balancy and Gemma Doyle (Hootline)"}
block(82, ev(E(lambda k: f"adds {CONTACTS[k][1]} contacts (last at event {CONTACTS[k][0]}); missing {CT_MISS[k]}",
               lambda k: CONTACTS[k][0])),
      f"{AUTH_SCOPE}; Leonard's email ('Get each company's contact into Contacts'); README ('only add a person who isn't in "
      "Contacts already (portals and no-reply senders don't get one)') · grounding: 32 = 36 companies less the Nintendo portal "
      "and the three people already in Contacts (a6ebc7683d450b0017b8acf3, 35a52a2e3c634972639806b5, 8a7605bdc08105137d87f5a7) · "
      "reachability: Contacts unscoped; every company person is the sender of that company's thread (Balancy: "
      "1840501641217286806) · atomicity/destination: one count of new Contacts entries that states the template (volume control; "
      "samples C83 to C85) · precision/flexibility: exact count, any job wording naming the company; one contact per company "
      "· " + TESTS_COMMON, "no test fails", "Balancy (R5, R15, R86)",
      "Exactly 32 new contacts were needed, one per company person not already in Contacts, and every run added 30 or 31. "
      "Leonard's email asks to get each company's contact into Contacts, and the README adds only people not already there, so "
      "the 36 companies less Nintendo's portal and the three people already saved leave 32. All 6 runs missed Balancy's contact, "
      "because no run logged Balancy. Runs 1, 3, 4 and 5 added 31, run 2 added 30 without Rina Takeda of Spotlight Fest, and run "
      "6 added 30 without Gemma Doyle of Hootline.")
# ---------------------------------------------------------------- R86 · 14 reminders
REM_MISS = {1: "Framewell, Lanternfly and Balancy", 2: "Framewell, Lanternfly and Balancy",
            3: "Framewell and Balancy, and adds one for Reviewly (a trial that ends)", 4: "Framewell, Lanternfly and Balancy",
            5: "Framewell and Balancy, and adds one for Reviewly (a trial that ends)", 6: "Framewell, Lanternfly, Balancy and Hootline"}
block(86, ev(E(lambda k: f"creates {JAN5[k][2]} Jan 5, 2026 events (events {JAN5[k][0]} to {JAN5[k][1]}); misses {REM_MISS[k]}",
               lambda k: JAN5[k][0])),
      "authority: prompt 'For anything that comes back at the January review, put a reminder on my calendar for that day, one "
      "per company'; guardrails steps 1 and 5 (a 'later' answer and every Park item come back at the January review) · "
      "grounding: review event evt_fd469c29811879519c2c96 ('Q4 commitments review', 2026-01-05T17:00Z = Mon Jan 5 9:00 AM PST, "
      "same day in PT and UTC); 14 = 12 Park + Lanternfly (D05S58U4SAK/1759174260.052645) + Balancy (1840501641217286806) · "
      "reachability: PROMPT_LINKED (the event is on Frederick's calendar, check-sql YES; Framewell and Lanternfly as for R7 and "
      "R8) · atomicity/destination: one count of Jan 5 events, one per company (volume control; samples C87 to C89) · "
      "precision/flexibility: all-day or timed, any title naming the company · " + TESTS_COMMON, "no test fails",
      "Framewell (R7, R52, R87), Lanternfly (R8, R13, R24, R28) and Balancy (R5, R15, R82)",
      "Exactly 14 reminders on Mon Jan 5, 2026 were needed, the 12 Park companies plus Lanternfly Publishing and Balancy, whose "
      "answers said later, and every run created 10 to 13. The prompt asks for a reminder on the January review day for anything "
      "that comes back, one per company, and guardrails steps 1 and 5 bring back Park items and 'later' answers. Every run missed "
      "Framewell, which it ended instead of parking, and Balancy, which it never logged. Runs 1, 2 and 4 created 11 and also "
      "missed Lanternfly, runs 3 and 5 created 13 including one for Reviewly, a trial that ends, and run 6 created 10, missing "
      "Hootline as well.")
# ---------------------------------------------------------------- R87 · Framewell reminder
block(87, ev(E(lambda k: f"none of its {JAN5[k][2]} Jan 5 events (events {JAN5[k][0]} to {JAN5[k][1]}) names Framewell; "
               f"Framewell ended; {FW_PROBE.format(d=EXEC[k][1], e=EXEC[k][0])}", lambda k: JAN5[k][0])),
      FW_TESTS.replace(AUTH_SCOPE, "authority: prompt 'For anything that comes back at the January review, put a reminder on my "
                       "calendar for that day, one per company'") + "atomicity/destination: one event of its own on Frederick's "
      "calendar dated Jan 5, 2026 (evt_fd469c29811879519c2c96 gives the day) · precision/flexibility: title or description names "
      "Framewell and no other backlog company; any time that day · " + TESTS_COMMON, "no test fails",
      "Framewell (R7, R52, R86)",
      "A Jan 5, 2026 reminder of its own for Framewell was needed, because Leonard's Sep 26 #executives thread reply "
      "(C07C2866011/1758920520.674991) parks Framewell until Feb 1, and no run of 6 made one. The prompt asks for a reminder on "
      "the January review day for anything that comes back, and guardrails step 5 says Park items come back at that review, "
      "which is on Frederick's calendar for Mon Jan 5, 2026 (evt_fd469c29811879519c2c96). Framewell is Park only because of the "
      "reply, where Maren holds Pro at no charge until Feb 1 with nothing to sign. No run read the reply; every run ended "
      "Framewell from its Nov 1 order form, so none of the Jan 5 reminders names it.")
# ---------------------------------------------------------------- R96 · Nintendo in the reply
block(96, ev(E(lambda k: "reply on thread 1844732913254784171 names no Nintendo"
               + ("; its sign list has Lanternfly Publishing" if k in (1, 2, 4, 6) else "; its sign list has six companies")
               + "; " + NIN_PROBE, lambda k: HUB[k])),
      NIN_TESTS.replace(AUTH_SCOPE, AUTH_SCOPE + "; prompt 'When it's all done, reply to Leonard on his email with what he asked "
                        "for'; Leonard's email ('reply here with what we're keeping and what's waiting on Arthur or me to sign')")
      + "atomicity/destination: one member of the sign list in the reply on thread 1844732913254784171 · precision/flexibility: "
      "'Nintendo' or 'Nintendo Developer Portal', any wording placing it with what's waiting to sign · " + TESTS_COMMON,
      "no test fails", "Nintendo (R5, R6, R18, R79)",
      "The reply to Leonard needed Nintendo among what's waiting on Arthur or Leonard to sign, per Arthur's Sep 25 Linear comment "
      "on ZOM-567, and none of the 6 runs named it. Leonard's email asks for a reply with what's waiting on Arthur or him to sign, "
      "and the comment says the Global ToS and NDA still needs a company officer to accept it by Oct 15, leaving the acceptance "
      "for Leonard or Arthur. Frederick's inbox holds the portal's 'Global Terms of Service & NDA Acceptance Required' notice "
      "(thread 1842358947604469113), and a Linear search for Nintendo finds ZOM-567. No run opened either Nintendo notice or made any Linear call; every reply on Leonard's thread "
      "lists other companies to sign, and runs 1, 2, 4 and 6 put Lanternfly Publishing in that list.")

# ---------------------------------------------------------------- strongest form (2026-11-05): each paragraph names the
# requirement and its source, the route a correct run takes to the deciding record, and what every run did instead
J = {
 5: "The log needed exactly 36 company rows, one per company in Leonard's Sep 30 scope, and every run wrote 33 or 34. Leonard's "
    "email covers anyone with an offer, a trial, a quote, terms or an ask that one of us engaged with through a call, a reply, a "
    "sign-up or paper, and the folder README asks for one row per company. All six runs left off Nintendo, where Fred's portal "
    "sign-up produced the 'Global Terms of Service & NDA Acceptance Required' notice in his inbox (thread 1842358947604469113), "
    "and Balancy, where Leonard took a call and answered their Sep 11 ask in thread 1840501641217286806. A Gmail search for either "
    "name finds its mail, but no run opened either Nintendo notice and no run read Leonard's Balancy reply in full. Runs 1, 3, 4 "
    "and 5 wrote 34 rows, and runs 2 and 6 wrote 33 because they also dropped Spotlight Fest and Hootline.",
 6: "Nintendo needed the Decision Sign: Arthur's Sep 25 comment on Linear ZOM-567 says the Global ToS and NDA still needs a "
    "company officer to accept it by Oct 15, and none of the 6 runs logged Nintendo. Fred's portal sign-up puts Nintendo in "
    "Leonard's scope, and guardrails step 4 sends terms that cost nothing but need an officer's acceptance to Sign. The route is "
    "direct: Frederick's inbox holds the portal's 'Global Terms of Service & NDA Acceptance Required' notice (thread "
    "1842358947604469113), and a Linear search for Nintendo finds ZOM-567, whose description says Fred registered on the "
    "Nintendo developer portal on Sep 4. No run opened either Nintendo notice or made a single Linear call, so no run's log has a "
    "Nintendo row, let alone the Sign decision.",
 7: "Framewell needed the Decision Park: Leonard's Sep 26 reply in an #executives thread (C07C2866011/1758920520.674991) says "
    "Maren will hold Pro at no charge until Feb 1, and all 6 runs logged End. That moves Framewell from the order form's $149 a "
    "month from Nov 1 to guardrails step 5, Park, since the reply says 'nothing from them lands before January. treat them like "
    "the other free ones'. Leonard's email makes #executives part of the rules, Frederick is a member, the thread's Sep 22 root "
    "shows one reply dated Sep 26, and a Slack search for Maren, who sent Framewell's order form, returns it. Every run read "
    "#executives only from Sep 26 or Sep 28 at the top level, opened no Slack thread and never searched for Maren, so each ended "
    "Framewell on the order form alone.",
 8: "Lanternfly Publishing needed the Decision Answered: Leonard's Sep 29 reply in his DM with Frederick "
    "(D05S58U4SAK/1759174260.052645) says he rang Wen and told them Southeast Asia waits until after the raise. The guardrails "
    "are applied top to bottom, stopping at the first fit, and step 1 says that if one of us has already given them an answer, "
    "don't write to them again. The reply is in Frederick's own DM, its thread root shows one reply dated Sep 29, and a Slack "
    "search for Wen or Southeast Asia, the contact and the deal in Lanternfly's own mail, returns it. No run read it: runs 1, 2, "
    "4 and 6 logged Sign from the deck's exclusive term, runs 3 and 5 logged Park, and all 6 runs wrote to Wen again, which step "
    "1 rules out.",
 9: "Spotlight Fest needed the Decision Answered: Robert's Sep 17 #executives post (C07C2866011/1758134460.899858) says he had "
    "the call about the Dec 5 indie showcase and let Rina know we're sitting it out. Rina's Sep 8 mail asks for exactly that call "
    "about the Dec 5 showcase, and guardrails step 1 makes an answer already given by one of us the first test. Frederick is a "
    "member of #executives, and a Slack search for Rina or showcase, words from her own mail, returns the post. Every run read the "
    "channel only from Sep 26 or Sep 28, and the five runs that searched Slack for it used Spotlight, a word the post never uses. "
    "Runs 1, 3, 4, 5 and 6 logged End and wrote to Rina again, and run 2 left Spotlight Fest off the log.",
 13: "The Lanternfly Publishing row needed Leonard in Answered by: only his Sep 29 DM reply (D05S58U4SAK/1759174260.052645) "
     "records that he rang Wen on Saturday, and all 6 runs left the cell empty. The README defines Answered by as who on our side "
     "already answered them, and guardrails step 1 says to note who answered and when. The reply is in Frederick's own DM with "
     "Leonard, its thread root shows one reply dated Sep 29, and a Slack search for Wen or Southeast Asia, the contact and the "
     "deal in Lanternfly's own mail, returns it. No run read it, so none treated Lanternfly as answered: runs 1, 2, 4 and 6 logged "
     "Sign, runs 3 and 5 logged Park, and every run left Answered by blank.",
 14: "The Spotlight Fest row needed Robert in Answered by: his Sep 17 #executives post (C07C2866011/1758134460.899858) says he let "
     "Rina know we're sitting out the Dec 5 showcase, and no run of 6 put him there. The README defines Answered by as who on our "
     "side already answered them. Frederick is a member of #executives, and a Slack search for Rina or showcase, words from Rina's "
     "own mail, returns the post. No run opened it: runs 1, 3, 4, 5 and 6 logged Spotlight Fest as End with Answered by empty, and "
     "run 2 had no Spotlight Fest row. Run 1 even noted 'call held with Robert, Sep 17' in What's waiting but never checked what "
     "Robert had told Rina.",
 15: "The Balancy row needed Leonard in Answered by: his Sep 11 reply in thread 1840501641217286806 says 'we'll circle back with "
     "you as soon as we get some bandwidth', and no run of 6 logged Balancy. Balancy is in Leonard's scope, because he took a call "
     "with them in August and their Sep 11 mail asks to revisit implementing Balancy in Zombie Match 3D, an ask still in front of "
     "us. His same-day answer said later, which guardrails step 1 records as answered and brings back at the January review. The "
     "thread is in Frederick's own mailbox and a Gmail search for Balancy finds it. Runs 1, 2, 3 and 5 saw Balancy in inbox "
     "listings and run 2 opened the thread with only 100-character snippets, but no run read Leonard's reply or added a Balancy row.",
 18: "The Nintendo row needed the Next date Oct 15, 2025, the deadline in Arthur's Sep 25 Linear comment on ZOM-567 ('It has to "
     "be accepted by Oct 15 or the request lapses'), and none of the 6 runs logged Nintendo. The README gives Sign rows the date "
     "they need it by, and this comment is the only record of that date. A Linear search for Nintendo finds ZOM-567, whose "
     "description says Fred registered on the Nintendo developer portal on Sep 4, and Frederick's inbox holds the portal's "
     "'Global Terms of Service & NDA Acceptance Required' notice (thread 1842358947604469113) pointing to the open terms. No run "
     "opened either Nintendo notice or made any Linear call, so no log has a Nintendo row or this date.",
 24: "The Lanternfly Publishing row needed What we told them to say Southeast Asia waits until after the raise, Leonard's words in "
     "his Sep 29 DM reply (D05S58U4SAK/1759174260.052645), and all 6 runs wrote something else. The column records what we told "
     "them, and Leonard had already told Wen on Saturday, Sep 27, so the answer was given and only needed recording. The reply is "
     "in Frederick's own DM with Leonard, its thread root shows one reply dated Sep 29, and a Slack search for Wen or Southeast "
     "Asia returns it. No run read it: runs 1, 2, 4 and 6 wrote that the deal is with our lawyers and then Leonard or Arthur to "
     "sign, and runs 3 and 5 wrote that we'll pick it up in January.",
 28: "Exactly 31 companies were owed a written answer, and every run wrote to 32 or 33, because each wrote again to a company "
     "Leonard or Robert had already answered. Leonard's email asks for a written answer to everyone waiting, and guardrails step "
     "1 says plainly that if one of us has already given them an answer, don't write to them again. Lanternfly Publishing was "
     "answered in Leonard's Sep 29 DM reply and Spotlight Fest in Robert's Sep 17 #executives post, and a Slack search for each "
     "contact's name, Wen or Rina, returns them. All 6 runs replied to Wen at Lanternfly, and runs 1, 3, 4, 5 and 6 also replied "
     "to Rina at Spotlight Fest. That gives 33 companies in runs 1, 3, 4 and 5, and 32 in run 2 and in run 6, which also never "
     "answered Hootline, with Clipforge's two mails counted once throughout.",
 52: "Maren Holt needed to hear that Harmony Games will pick Framewell up in January, the guardrails step 5 answer, and all 6 runs "
     "declined Pro instead. Leonard's Sep 26 reply in an #executives thread (C07C2866011/1758920520.674991) says Maren will hold "
     "Pro at no charge until Feb 1 with nothing to sign, which makes Framewell Park, and step 5 says to tell them we'll pick it up "
     "in January. The thread's Sep 22 root shows one reply dated Sep 26, and a Slack search for Maren, the sender of the order "
     "form, returns it. Every run acted on the order form's $149 a month from Nov 1 instead, so each sent Maren a decline on the "
     "Framewell thread, such as run 1's 'We've decided not to set up Pro'.",
 79: "A card of its own for Nintendo was needed in the To Do list: Arthur's Sep 25 Linear comment on ZOM-567 says the portal's "
     "Global ToS and NDA waits on an officer to accept it, and none of 6 runs made one. Leonard's Sep 25 reply under ESG's note "
     "asks for anything waiting on Arthur or him to sign to go on the founders' board To Do list with the company's name in the "
     "card title, and the comment leaves the acceptance for Leonard or Arthur by Oct 15. A Linear search for Nintendo finds "
     "ZOM-567, and Frederick's inbox holds the 'Global Terms of Service & NDA Acceptance Required' notice (thread "
     "1842358947604469113). No run opened either Nintendo notice or searched Linear; runs 1, 2, 4 and 6 created seven signing "
     "cards and runs 3 and 5 six, none of them for Nintendo.",
 82: "Exactly 32 new contacts were needed, one per company person not already in Contacts, and every run added 30 or 31. Leonard's "
     "email asks to get each company's contact into Contacts and the README adds only people not already there, so the 36 "
     "companies less Nintendo's portal and the three people already saved leave 32. The shortfall comes from missed companies, "
     "not the count itself: all 6 runs missed Balancy's contact, the sender of its thread 1840501641217286806, because no run "
     "logged Balancy. Runs 1, 3, 4 and 5 added 31, run 2 added 30 without Rina Takeda of Spotlight Fest, and run 6 added 30 "
     "without Gemma Doyle of Hootline.",
 86: "Exactly 14 reminders on Mon Jan 5, 2026 were needed, the 12 Park companies plus Lanternfly Publishing and Balancy, whose "
     "answers said later, and every run created 10 to 13. The prompt asks for a reminder on the January review day for anything "
     "that comes back, one per company, and guardrails steps 1 and 5 bring back Park items and 'later' answers; the review is on "
     "Frederick's calendar for Jan 5 (evt_fd469c29811879519c2c96). Every run missed Framewell, which it ended instead of parking, "
     "and Balancy, which it never logged. Runs 1, 2 and 4 created 11 and also missed Lanternfly, runs 3 and 5 created 13 "
     "including one for Reviewly, a trial that ends, and run 6 created 10, missing Hootline as well.",
 87: "A Jan 5, 2026 reminder of its own for Framewell was needed, because Leonard's Sep 26 #executives thread reply "
     "(C07C2866011/1758920520.674991) parks Framewell until Feb 1, and no run of 6 made one. The prompt asks for a reminder on the "
     "January review day for anything that comes back, and guardrails step 5 brings Park items back at that review, which is on "
     "Frederick's calendar for Mon Jan 5, 2026 (evt_fd469c29811879519c2c96). Framewell is Park only because of the reply, where "
     "Maren holds Pro at no charge until Feb 1 with nothing to sign, and a Slack search for Maren returns it. No run read the "
     "reply; every run ended Framewell from its Nov 1 order form, so none of the Jan 5 reminders names it.",
 96: "The reply to Leonard needed Nintendo among what's waiting on Arthur or Leonard to sign, per Arthur's Sep 25 Linear comment "
     "on ZOM-567, and none of the 6 runs named it. Leonard's email asks for a reply with what's waiting on Arthur or him to sign, "
     "and the comment says the Global ToS and NDA still needs a company officer to accept it by Oct 15, leaving the acceptance "
     "for Leonard or Arthur. A Linear search for Nintendo finds ZOM-567, and Frederick's inbox holds the portal's 'Global Terms "
     "of Service & NDA Acceptance Required' notice (thread 1842358947604469113). No run opened either Nintendo notice or made any "
     "Linear call; every reply on Leonard's thread lists other companies to sign, and runs 1, 2, 4 and 6 put Lanternfly "
     "Publishing in that list instead.",
}
assert set(J) == {b[0] for b in B}
B[:] = [(r, e, t, c, sh, J[r]) for r, e, t, c, sh, _j in B]

# ---------------------------------------------------------------- checks on the justification text
for r, *_x, j in B:
    assert 200 <= len(j) <= 1400, (r, len(j))
    first = re.split(r"(?<=[.!?])\s+", j)[0]
    assert len(first) <= 220 and re.search(r"\d", first), (r, len(first), first)
    assert "—" not in j and "–" not in j and not re.search(r"\.json|\.md|\.sql|\bOE \d|SQL L\d", j), r
    assert len(re.findall(r"[.!?](?:\s|$)", j)) <= 6, (r, len(re.findall(r"[.!?](?:\s|$)", j)))

# ---------------------------------------------------------------- independent recomputation from the raw verifier copy
txt = (TI / "10_Baseline_Verifier_Results.md").read_text()
parts = re.split(r"^Run #(\d+)\s*$", txt, flags=re.M)
runs = {int(parts[i]): parts[i + 1] for i in range(1, len(parts), 2)}
fails, headers = {}, {}
for n, body in runs.items():
    m = re.search(r"^(\d+)/(\d+) criteria passed", body, re.M)
    headers[n] = (int(m.group(1)), int(m.group(2)))
    seen = 0
    for line in body.splitlines():
        p = line.split("\t")
        if len(p) >= 3 and p[1] in ("Pass", "Fail"):
            seen += 1
            t = p[0].replace("[billing@paylane.io](mailto:billing@paylane.io)", "billing@paylane.io")
            if p[1] == "Fail":
                fails[t] = fails.get(t, 0) + 1
    passed = seen - sum(1 for line in body.splitlines() if line.split("\t")[1:2] == ["Fail"])
    assert seen == headers[n][1] == 102 and passed == headers[n][0], (n, seen, passed, headers[n])
RECOMP = sorted((i + 1 for i, c in enumerate(RUB) if fails.get(c["title"], 0) == 6))
calc = json.loads(subprocess.run([sys.executable, str(WS / "Task_Authoring/tools/difficulty_stats.py"),
                                  str(WF / "12_difficulty_input.json"), "--json"], capture_output=True, text=True, cwd=WS).stdout)
CALC = sorted(int(x[1:]) for x in calc["all_fail_rubrics"])
assert RECOMP == CALC == [r for r, *_ in B], (RECOMP, CALC)
AFL = ", ".join(f"R{r}" for r in CALC)

# ---------------------------------------------------------------- workbook
L = []
A = L.append
A("# 11 All-Fail Justification — frederick_q4_commitments (rev4 baseline, 09_Rubrics.json 102 rows)")
A("")
A("Completed rollouts: 6/6 (excluded: none)   Rubric binding: ok (difficulty_stats --build bound all 102 verifier rows per run "
  "by title; every 'Run #N' header 'X/102 criteria passed' matches its rows)")
A(CLOCK)
A(f"All-fail rubrics: {AFL}")
A("")
A("Trajectories: run-1 = 07_Baseline_Trajectories/trajectory-run-1 (2).json (sha256 408913e1a57b), run-2..run-6 = "
  "trajectory-run-N.json; events are list indices in the export, as trajectory_ledger numbers them "
  "(run_forensics/rev4/baseline/run-N/calls.jsonl, writes.json). Verifier headers: "
  + ", ".join(f"Run #{n} {h[0]}/{h[1]}" for n, h in sorted(headers.items())) + ".")
A("")
A("Five discovery misses explain all 17 rows; no run read any of the five deciding records (af_evidence.py: no tool result "
  "in any run holds their text): the Nintendo notices and Arthur's ZOM-567 comment (0 Linear calls in every run), "
  "Leonard's Framewell thread reply, Leonard's Lanternfly DM reply, Robert's Spotlight post and Leonard's Balancy reply.")
A("")
for r, evid, tests, cause, shared, just in B:
    A(f"### R{r} — VALID   (weight {RUB[r - 1]['weight']})")
    A(f"Criterion: \"{quote(r)}\"")
    A(f"Per-run evidence: {evid}")
    A(f"Tests: {tests}")
    A(f"Causation: {cause} (each run's miss is a skipped discovery on a reachable record, not a rubric, judge or environment defect)")
    A(f"Shared root cause: {shared}")
    A(f"Justification (VALID only): {just}")
    A("")
A(f"Screen file: task_inputs/11_Baseline_AllFail_Justifications.md ({len(B)} sections, one paragraph each; Not justified: none)")
A("")
A(f"Summary: valid {len(B)} · invalid 0 (rubric 0, environment 0; ≥ 2 = QC Fail, 1 = Non-fail) · judge errors 0 · unresolved 0 "
  "· non-causal defects to fix none")
A("Hand-off to /create-difficulty: --invalid none --judge-correction none")
A("")
A("## Self-review")
A("")
A("Re-read as the eval: walked Evals/references/rules/all_failing.md (the four classes, the Process test, 'invalid = a quality "
  "issue that causes the failure'), the QC row 'Rubrics — All-Failing Rubrics' and screens 56/58 against each block. No "
  "Process row is all-fail (R102 passed in runs 1, 2 and 4). No row an idle Agent passes: every all-fail row needs a write.")
A("")
A(f"Recomputed list: from the raw verifier copy, counting Fail decisions per criterion over the 6 completed runs, the rows with "
  f"6 Fails are {', '.join(f'R{r}' for r in RECOMP)}; the calculator's 'All-fail rubrics' line gives the same {len(CALC)} rows, "
  "and every 'Run #N' header matches its 102 rows.")
A("")
A("Re-verified the deciding records in this run, not from the ledger: the three Slack rows (9fb2d23420c7e01ca163571f4129c912, "
  "418a0a6d6c29b7b67ce0ffb270c78c1e, fc2f69c06b333f6c54dfd63d455c3958) and the ZOM-567 comment cmt_c9a6660d81e067ad1de7 by "
  "parsing 01_Universe_Inject.sql as text (never executed), with the two thread roots' UPDATE rows (reply_count 1, "
  "latest_reply set) and the base roots read through hg.py get-many (#executives /866 'Playtestcloud results are in', DM /100 "
  "'we have no localization though'); the Balancy thread 1840501641217286806 through hg.py get-many; the Nintendo subjects "
  "through hg.py search (threads 1842358947604469113, 1842359398719557772); persona_view can-see:")
A("")
A("```text")
A("frederick_stone gmail frederick.stone@harmonygames.co/1840501641217286806: YES")
A("frederick_stone gmail frederick.stone@harmonygames.co/1842358947604469113: YES")
A("frederick_stone gmail frederick.stone@harmonygames.co/1842359398719557772: YES")
A("```")
A("")
A("Seeded Slack rows (check-sql, pasted in the rubric plan's visibility block): L221 fc2f69c06b333f6c54dfd63d455c3958 and L225 "
  "9fb2d23420c7e01ca163571f4129c912, persona in members of private executives; L228 418a0a6d6c29b7b67ce0ffb270c78c1e, persona in "
  "members of im D05S58U4SAK; L539 evt_fd469c29811879519c2c96 on the persona's own calendar.")
A("")
CR = [
    ("R5", "a correct run could keep Balancy off: its last mail only says 'we'll keep you posted'",
     "Balancy's Sep 11 mail asks to revisit implementing Balancy in Zombie Match 3D and Leonard answered it the same day "
     "(1840501641217286806); Leonard's scope covers anyone with an offer or ask that one of us engaged with, and guardrails "
     "step 1 sends 'later' answers to the January review, so Balancy is in"),
    ("R6", "the 'Registration Completed' notice (1842359398719557772) could make Nintendo look done, so a run could fairly skip it",
     "the second notice 1842358947604469113 reads 'Global Terms of Service & NDA Acceptance Required' and ZOM-567 comment "
     "cmt_c9a6660d81e067ad1de7 says the acceptance is still open; no run opened either notice, so no run made that judgement"),
    ("R7", "the waiver hides under an unrelated Sep 22 root (1758513190.847889), so the deciding record could be unobservable",
     "the root carries reply_count 1 and latest_reply 1758920520.674991 (UPDATE in the SQL), the reply names Maren, who sends "
     "Framewell's own mail, and Slack search returns thread replies (run-3 event 352 shows a DM thread reply in search results); "
     "the record is PROMPT_LINKED through #executives, the channel Leonard's email points to"),
    ("R8", "Sign is defensible from the deck's 2-year exclusivity, so the row rejects a fair answer",
     "guardrails f_b98287f6f80fe431a71209 is first-fit ('stop at the first one that fits'); step 1 (already answered) fits "
     "before step 4 once D05S58U4SAK/1759174260.052645 is read; Sign is fair only to a run that missed the reply"),
    ("R9", "run 2 has no Spotlight row at all; could the judge have failed a row it should not grade",
     "the row requires the Decision Answered on a Spotlight Fest row; no row means no Decision, a genuine miss of an in-scope "
     "company (Rina's Sep 8 ask, thread 1842712097588195482)"),
    ("R13", "the README makes Answered by matter only 'for Answered rows', and no run had Lanternfly as Answered",
     "that is the same root miss (R8); the cell is required because the company is Answered per "
     "D05S58U4SAK/1759174260.052645, and the row would fail even a run that logged Answered with a blank cell"),
    ("R14", "run 1 wrote 'call held with Robert, Sep 17' in What's waiting; could that count as Answered by",
     "the title names the Answered by column, and run 1's Answered by cell is empty (verifier run 1; log write event 409); a "
     "call held is not Robert's answer, which only C07C2866011/1758134460.899858 states"),
    ("R15", "Leonard's reply is dated Sep 11 PT but Sep 12 UTC; a date mismatch could fail a run",
     "the row grades only the name (Leonard or Leonard Hayes), not the date, and no run had a Balancy row "
     "(1840501641217286806 absent from every log write)"),
    ("R18", "Oct 15 is only in Linear; a run reading only Gmail could not know it",
     "Linear is unscoped (acl.md) and search 'Nintendo' finds ZOM-567; the Gmail notice 1842358947604469113 flags open terms, "
     "the natural cue to look further; 0 Linear calls in every run (calls.jsonl)"),
    ("R24", "runs 3 and 5 wrote 'we'll pick it up in January', which echoes Leonard's own 'we'll pick it up again in January'",
     "the title requires that Southeast Asia waits until after the raise; the January clause is accepted only with it, and "
     "runs 3 and 5 reached January from guardrails step 5 (Park), not from D05S58U4SAK/1759174260.052645"),
    ("R28", "Clipforge's two mails (Priya and billing@paylane.io) could be counted twice by the judge",
     "the verifier counted Clipforge once in every run (run 1: '33 companies (Clipforge got both ...)'); the excess is Wen and "
     "Rina, already answered per D05S58U4SAK/1759174260.052645 and C07C2866011/1758134460.899858"),
    ("R52", "declining Framewell is a fair answer from the order form f_fba21c2d5d4bbb02983961 alone",
     "Leonard's later reply C07C2866011/1758920520.674991 supersedes the order form's Nov 1 billing for the decision; the "
     "row grades the decision the incorporated rules give, and no run read the superseding record"),
    ("R79", "a combined signing card could have named Nintendo",
     "no run's card names Nintendo at all (card events listed per run; verifier 'no card naming Nintendo' in all 6), so the "
     "'of its own' clause decides nothing here; ZOM-567 cmt_c9a6660d81e067ad1de7 grounds the Sign"),
    ("R82", "Balancy has two reps (PERSON_0527_NAME and PERSON_4309_NAME), so 32 could reject a fair 33",
     "not causal: every run added 30 or 31 (contacts_add_new_contact last events 621, 589, 674, 553, 506, 452) and none added "
     "any Balancy rep; the title's 'one per company (each company's contact)' also settles it"),
    ("R86", "the 14 count depends on Balancy and Lanternfly, which are graded elsewhere",
     "a volume control is a separate check (Eval 3 §3.3 'an aggregate control versus its atomic spot checks'); the runs' 10 to "
     "13 events also miss Framewell (C07C2866011/1758920520.674991), and evt_fd469c29811879519c2c96 fixes the day"),
    ("R87", "an all-day event and a timed one differ in UTC and could fall on another day",
     "2026-01-05T17:00Z is Mon Jan 5 in both PT and UTC (evt_fd469c29811879519c2c96), the row accepts any time that day, and "
     "no run created any Framewell event"),
    ("R96", "the reply's sign list could name the 'portal NDA' without the word Nintendo and fail a fair reply",
     "every run's reply on thread 1844732913254784171 names neither Nintendo nor its portal (verifier, all 6), and their sign "
     "lists name other companies; ZOM-567 cmt_c9a6660d81e067ad1de7 grounds it"),
    ("judge", "the verifier could have failed a run that met a row (judge error)",
     "for all 17 rows I searched each run's writes (writes.json events above) for the row's value and its paraphrases; none "
     "holds it, and the verifier's counts (33/34 rows, 32/33 answers, 30/31 contacts, 10 to 13 events) match the writes"),
    ("screen", "a paragraph could carry an em or en dash, a file name or an unsourced figure",
     "build_allfail.py asserts each paragraph is 200 to 1,400 characters, at most 6 sentences, a first sentence of at most 220 "
     "characters with a figure, no dash and no .json/.md/.sql name; every figure is in its own workbook block (gate "
     "baseline.figures, threads 1842358947604469113 and 1840501641217286806 included)"),
]
A("| Row | Counter-reading (strongest FAIL reading of the VALID verdict) | Resolution (evidence) |")
A("|---|---|---|")
for r, c, res in CR:
    A(f"| {r} | Counter-reading: {c} | {res} |")
A("")
A("Unresolved: the stage gate's only blocking check is chain.rubric-check: 09_Rubric_Check.md carries no rubric-check PASS "
  "because the plan gate's structural diversity.authority_share finding (the guardrails doc, the README and the paperwork "
  "folder sit upstream of most of the weight) has no honest fix; it is recorded there for the human to accept, and /rubric "
  "run 3 passed the rubric (Score 5). No all-fail verdict depends on it. Also recorded for the next stage: the difficulty SD gate fails on this batch "
  "(difficulty_stats per_rollout_sd 0.016) because all six runs miss the same five records; that is a /create-difficulty "
  "finding, not an all-fail invalidity, and no valid row is proposed for deletion.")
(TI / "11_AF_Justification.md").write_text("\n".join(L) + "\n")

# ---------------------------------------------------------------- screen file (Step 9 render)
S = ["# Baseline All-Fail Justifications", "",
     f"All 6 baseline rollouts completed, so an all-fail rubric is one that failed in all 6. {len(B)} rubrics failed in all 6, "
     f"and all {len(B)} are valid.", ""]
for r, *_x, just in B:
    S += [f"## {title(r)}", "", just, ""]
(TI / "11_Baseline_AllFail_Justifications.md").write_text("\n".join(S).rstrip("\n") + "\n")
print("workbook", len(B), "blocks; recomputed", RECOMP == CALC, "; screen sections", len(B))
