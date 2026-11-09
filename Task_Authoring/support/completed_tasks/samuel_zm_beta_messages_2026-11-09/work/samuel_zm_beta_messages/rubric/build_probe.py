#!/usr/bin/env python3
"""Turn probe_raw.txt into probe.txt: the output pasted verbatim in a fence, then one SHORTCUT-OK line per reported item."""
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
raw = (HERE / "probe_raw.txt").read_text().rstrip()
REASON = [
    (r"^gmail samuel\.turner@harmonygames\.co/1836006988541924555", "the GitHub notification thread for PR #248 in Samuel's mailbox: it carries the same code hunk and the client's titles, and no call on any message"),
    (r"^github data\.json/review_comments/", "a review comment on PR #248 whose hunk shows NotificationManager.cs, the designed source for the schedule: it holds the code and the title, and no call on any message"),
    (r"^sql:github\.github_review_comments", "Arthur's rc_18 comment, the designed authority for test 5: its hunk shows the same code, and it decides one message only"),
    (r"^sql:slack\.slack_messages L45:", "Leonard's DM itself, the record the prompt names: it holds the column names and the job, and no call, count or line, so no row is answered from it"),
    (r"^sql:gdocs\.docs_documents L13:", "the rule doc, the designed authority the DM names: it holds the column names and the tests, and no call on any message"),
    (r"^sql:linear\.linear_issues .*DES-316", "DES-316's own ticket: it holds its key, name and shipped line, and the call still needs all six tests across the code, the QA note, the checks sheet and Slack"),
    (r"^sql:linear\.linear_issues .*DES-317", "DES-317's own ticket: it holds its key, name and shipped line, and the call still needs all six tests"),
    (r"^sql:linear\.linear_issues .*DES-315", "DES-315's own ticket: its relations name ZOM-483 and ZOM-563, a pointer to two comment asks, and it holds no call, so reading it answers no row; the asks still have to be opened"),
    (r"^sql:linear\.linear_issues .*DES-338", "DES-338's own ticket: its relation names ZOM-556, a pointer to one comment ask, and it holds no call, so reading it answers no row"),
    (r"^sql:linear\.linear_issues .*DES-330", "DES-330's own ticket: its relation names ZOM-542, a pointer to one comment ask, and it holds no call, so reading it answers no row"),
    (r"^sql:linear\.linear_issues ", "one ticket's own row: it holds its key and name, and no call on any other message"),
    (r"^gsheets f_a325dd4af80afc5994d5dc", "the PN sheet the prompt names: it lists the 14 row names, which the job starts from; its status columns decide nothing (rule doc f_dc45e0e5a8b8635c1b82b2)"),
    (r"^gsheets ", "another sheet that happens to repeat row names or headlines, with no call, test or ticket key"),
    (r"^sql:gsheets", "Vincent's checks log: the six passes it records are half the evidence for test 6, and two are later withdrawn, so it answers no call alone"),
]


def reason(key):
    for rx, why in REASON:
        if re.search(rx, key):
            return why
    return None


lines = raw.split("\n")
out = ["```text"] + lines + ["```", ""]
seen, missing = set(), []
for l in lines:
    m = re.match(r"^HIT (\S+) (\S+) ", l) or re.match(r'^INCOMPLETE (\S+) (value:".*") \(', l)
    if not m or (m.group(1), m.group(2)) in seen:
        continue
    seen.add((m.group(1), m.group(2)))
    why = reason(f"{m.group(1)} {m.group(2)}")
    if why is None:
        missing.append(l[:220])
        continue
    out.append(f"SHORTCUT-OK: {m.group(1)} {m.group(2)} — {why}")
(HERE / "probe.txt").write_text("\n".join(out) + "\n")
print(len(seen), "items;", len(missing), "without a reason")
for x in missing:
    print(x)
