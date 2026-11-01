"""Round 6 dossier update: Robert's thread reply in the group chat + fresh verbatim tool blocks.

Usage (from Task_Authoring-2): python3 support/task_work/jl_difficulty/dossier_r6.py
"""
import re
import subprocess

D = 'task_inputs/Working_Files/01_Grounding_Dossier.md'
SQL = 'task_inputs/01_Universe_Inject.sql'
MAN = 'task_inputs/Working_Files/01_Hardness_Manifest.json'
s = open(D).read()
CH = 'CAFC495E4006'
P_ID, R_ID = 'cec246a6e43158f200fe144f0dd7039c', 'abe096ff0b5d7216efbc889e91d6d13a'


def run(args):
    p = subprocess.run(['python3'] + args, capture_output=True, text=True)
    return (p.stdout + p.stderr).rstrip('\n')


ROW = "| 1 | slack.slack_messages | 6f77386571537f0bd88c959bdc216f94 | A1 / K1 | ● | DM member | first link |\n"
NEW = (f"| 1b | slack.slack_messages | {P_ID} | K19 / T32 (Leonard's question to Robert, group chat {CH}, reply_count 1) | ● | group chat member | container |\n"
       f"| 1c | slack.slack_messages | {R_ID} | K19 / T32 / C15 (Robert's thread reply: assignee, done day, priority) | ● | group chat member | amendment (round 6) |\n")
if R_ID not in s:
    assert s.count(ROW) == 1
    s = s.replace(ROW, ROW + NEW)

if '## Round 6 hardening' not in s:
    s = s.replace("## Round 5 hardening", f"""## Round 6 hardening (third hidden thread)

| Change | Records | Why |
|---|---|---|
| Leonard asks Robert in their group chat with Julia what he wants on Julia's list (top level, reply_count 1); Robert answers only in the thread: three Tickets-tab columns after status (Linear assignee, the day it got marked done or blank, Linear priority) | slack {CH}/1759226461.318204 ({P_ID}), {CH}/1759229513.774912 ({R_ID}); ids follow sha256(channel and ts) | 22 baseline and hardness runs: every judgement trap was resisted; only thread replies land (about 55% missed). A third thread in a different conversation spreads graded weight so failing runs split |
| Card rule 2: 'Layout as in the session agenda, plus the three things Robert asked for when I asked him in our group chat.' | card 68daca5871dba40417a00383 desc and updateCard action 68dbe36f4b2b4fffb7525fde | names the source (fair pointer); the content stays in the thread |
| Header comment counts updated (179 INSERT, 3 UPDATE) | line 3 | /injection advisory C-1 |

Base check of the new facts (Linear data.json, all 24 register tickets): every ticket has an assignee; completed_at is set for the 21 Done tickets and empty for ZOM-202 (In Progress), ZOM-280 (Canceled) and ZOM-293 (Todo); priority is 1 to 4 on all 24. Group chat {CH}: members Robert (EMPLOYEE_0016), Leonard (EMPLOYEE_0038), Julia (EMPLOYEE_0005) and PERSON_6089; base history Dec 2024 to Jul 2025, then Nov 2025, so no ts collision in Sep 2025. Robert's reply avoids the words register, column and baseline.

## Round 5 hardening""", 1)

lb = set()
for line in re.findall(r"\[YES LB\] L\d+ \S+ \S+ (.*?) - ", s):
    lb |= {x.strip() for x in line.split(',') if len(x.strip()) > 6 and not x.strip().endswith('…')}
lb = sorted(lb | {'julia.lawson@harmonygames.co/1844695547248825769', P_ID, R_ID})
LBF = 'support/task_work/jl_difficulty/lb_ids_r6.txt'
open(LBF, 'w').write('\n'.join(lb) + '\n')
blocks = {
    "`python3 Task_Authoring/tools/persona_view.py check-sql julia_lawson Task_Authoring/task_inputs/01_Universe_Inject.sql --load-bearing <lb ids>` (verbatim):":
        run(['tools/persona_view.py', 'check-sql', 'julia_lawson', SQL, '--load-bearing', LBF]),
    "`python3 Task_Authoring/tools/sql_lint.py Task_Authoring/task_inputs/01_Universe_Inject.sql` (verbatim):": run(['tools/sql_lint.py', SQL]),
    "`python3 Task_Authoring/tools/base_check.py Task_Authoring/task_inputs/01_Universe_Inject.sql` (verbatim):": run(['tools/base_check.py', SQL]),
    "`python3 Task_Authoring/tools/hardness_gate.py …/01_Hardness_Manifest.json …/01_Universe_Inject.sql` (verbatim):": run(['tools/hardness_gate.py', MAN, SQL]),
    "`python3 Task_Authoring/tools/fact_check.py … --no-leak` (verbatim):": run(['tools/fact_check.py', SQL, '--manifest', MAN, '--no-leak']),
}
for head, out in blocks.items():
    i = s.find(head)
    assert i >= 0, head
    a = s.find("```\n", i) + 4
    b = s.find("\n```", a)
    s = s[:a] + out + s[b:]
open(D, 'w').write(s)
print('ok; load-bearing ids', len(lb))
