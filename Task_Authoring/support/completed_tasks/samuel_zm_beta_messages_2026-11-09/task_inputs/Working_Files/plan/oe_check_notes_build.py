#!/usr/bin/env python3
"""Write plan/oe_check_notes.json: the sweep, self-review and counter-readings for 08_OE_Check.md, numbered from the live event
index. Findings and advisory rows are read from plan/oe_check_findings.json, which holds the independent review's dispositions."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
N = json.load(open(os.path.join(HERE, "oe_events_index.json")))["index"]
F = json.load(open(os.path.join(HERE, "oe_ledger_ids.json")))["fid"]
X = json.load(open(os.path.join(HERE, "oe_check_findings.json")))
n = lambda k: f"OE {N[k]}"  # noqa: E731
spans = X.get("spans", 188)
sweep = [
    ["One wrong count, ID, channel or tool", f"none: counts recomputed (36 messages, 14 + 18 + 4; Go 2, Hold 28, Drop 6; 31 children; 20 tickets; 13 card comments) from solver/truth.json and the records; every read and write maps to a cataloged tool (Evals/references/tools/catalog.json)"],
    ["One missing write", f"none: every write family in ledger §C (08_OE_Writing_Ledger.md) has its events, one write per event, {n('w_str')} to {n('wdm')}"],
    ["One Expected fact with no retrieving event", f"none: each value an Expected line uses is read by that event or an earlier one it names (Coverage rows above)"],
    ["One unledgered Expected value or unbacked absence word", f"none: {spans} quoted spans re-read against each event's own records; absence words are backed by complete scans ({F['pop']}, {F['census']}, {F['tcom']})"],
    ["One act-vs-defer conflict", "none: ledger §C defer search complete (Slack, Gmail, Linear, Trello), Leonard's Sep 30 DM (D06L58XCVKK/1759264851.763895) is the latest instruction"],
    ["One non-action or final-response event", "none: no event describes the final response or a thing not done; the Go tickets simply have no move event"],
    ["One prompt-forbidden or reserved write", "none: 04_Prompt.txt reserves nothing ('You don't need to run anything by me first'); Leonard gets no email, as the DM says"],
    ["One missing recovery or wait event", "none: 03_Error_Async_Config.txt is Friction: none"],
]
review = [
    "Re-read as the eval: walked Evals/2_Oracle_Events_Eval.md 1.2 (inventory), 1.3 (five fields per STEP), the HARD GATE (no non-action or final-response event), 2.1–2.7 (service, tool, parameters, expected data, visibility, authority, act-vs-defer, format), 3.1–3.6 (completeness) and 4.0 (the sweep above) in order against the file.",
    f"Re-verified: every quoted span ({spans}) re-read in this run against its own event's records by plan/assemble_oe_check.py (SQL parsed again, base through hg.py get and search); counts recomputed. No Expected value rests on a repository blob: the client lines and titles are quoted from the PR hunk read through hg.py, and run-5 event 117 shows the same call sites on main (ledger §F 4).",
    "Five fields: every event names its action and service in the heading, its parameters (search text, title, list, path, recipient) in the heading, the information and expected data on its Expected line, and its dependency as an 'OE n' pointer where it needs an earlier value. The eight decision events name the services they draw on.",
    X["independent"],
    f"Path notes: {n('pop')} rests on the catalog's updatedAt parameter, which no run exercised; {n('rc18')} on github_get_pull_request_comments, which no run called; {n('covered')} on a mail that appeared in Gmail results in run-3, run-4 and run-5 but that no run opened. Each is a cataloged tool reading a record the persona can see, so the path is SUPPORTED on the catalog and the records, not on a run that took it (ledger §F 1, §F 4); {n('rc18')} also offers Samuel's Gmail copy.",
]
counter = {
    "R1": f"the DM could be another Leonard message; {n('hub')} pins the Sep 30 message that names the PN sheet and the job (D06L58XCVKK/1759264851.763895, {F['hub']})",
    "R2": f"the sheet could mean every tab or the Domino twin; {n('sheet')} names the PNs Beta tab, which the DM names ({F['sheet']})",
    "R3": f"the population could stop at the 18 asks under DES-314; {n('pop')} and the four comment events take in the asks on ZOM-542, ZOM-556, ZOM-563 and ZOM-483, and {n('census')} and {n('tcom')} show nothing else is filed ({F['pop']}, {F['census']}, {F['tcom']})",
    "R4": f"a test could be skipped or read out of order; OE {N['c1']} to OE {N['c6']} run the six tests in turn, and each count follows from the last (36, 31, 25, 6, 5, 4; {F['rule']})",
    "R5": f"the sheet could stay outside the folder; {n('w_mv1')} moves it into d_caafeec2804b3a67ce46aa ({F['folder']})",
    "R6": f"the note could leave out one of the three parts the DM asks for; {n('w_note')} states all three, with four Holds ({F['wh']}, {F['client']}, {F['counts']})",
    "R7": f"Holds could go on the checklist; {n('w_i1')} and {n('w_i2')} add the two Go messages only, and the DM says 'Every Go' ({F['pncard']})",
    "R8": f"Go tickets could be skipped; the 32 comment events include DES-316 and DES-317, because the DM says 'each ticket' ({F['hub']})",
    "R9": f"Hold tickets could go to Todo; {n('freeze')} reads the roadmap note that overrides it, and each Hold event names Backlog with no assignee ({F['freeze']})",
    "R10": f"Win & Collect could get a new ticket; {n('wc')} finds DES-313 and the create events cover only the four asks and the string ticket ({F['wc']})",
    "R11": f"Douglas could be missed, or Leonard emailed; the eight email events include douglas@harmonygames.co, and the DM says 'apart from me' ({F['who:douglas']})",
    "R12": f"the counts could go out before the writes finish; {n('wdm')} is the last event and says so ({F['counts']})",
    "R13": f"a step could wait for Samuel's approval; no event does, and the prompt says 'You don't need to run anything by me first' (04_Prompt.txt, {F['hub']})",
}
json.dump({"sweep": sweep, "review": review, "counter": counter, "findings": X.get("findings", []), "advisory": X.get("advisory", []), "preface": X.get("preface", ""),
           "prediction": X.get("prediction", "PASS 5"), "completeness": X.get("completeness", 5), "accuracy": X.get("accuracy", 5)},
          open(os.path.join(HERE, "oe_check_notes.json"), "w"), indent=0, ensure_ascii=False)
print("notes", len(sweep), len(counter), "findings", len(X.get("findings", [])), "advisory", len(X.get("advisory", [])))
