"""Round 7 dossier update: Blake's 'not tiers' on PR #271, Robert's pacific done day, fresh verbatim tool blocks.

Usage (from Task_Authoring-2): python3 support/task_work/jl_difficulty/dossier_r7.py
"""
import re
import subprocess

D = 'task_inputs/Working_Files/01_Grounding_Dossier.md'
SQL = 'task_inputs/01_Universe_Inject.sql'
MAN = 'task_inputs/Working_Files/01_Hardness_Manifest.json'
s = open(D).read()
PR = 'harmonygames-Games/match3d#271'
REV, RC = PR + '#rev_2', PR + '#rc_1'
MA, MC = '{MA}', 'e7977b0f608c8af00f33c4744ab7ea1f'
import hashlib
MA = hashlib.sha256(b'C093LEZGF6J|1751591124.205377').hexdigest()[:32]


def run(args):
    p = subprocess.run(['python3'] + args, capture_output=True, text=True)
    return (p.stdout + p.stderr).rstrip('\n')


ROW = next(l for l in s.splitlines(True) if l.startswith('| 19 | github.github_pr_comments | harmonygames-Games/match3d#401#c_2'))
NEW = (f"| 19b | github.github_reviews | {REV} | K20 / T33 (Blake's APPROVED review, empty body) | ● | unscoped | container (round 7) |\n"
       f"| 19c | github.github_review_comments | {RC} | K20 / T33 / C16 (inline 'not tiers' on MonsterSpawner.cs) | ● | unscoped | amendment (round 7) |\n"
       f"| 19d | slack.slack_messages | {MA} | INT-01 companion of {REV} (approval mirror) | ● | UNVERIFIED-OK | companion |\n"
       f"| 19e | slack.slack_messages | {MC} | INT-01 companion of {RC} (comment mirror) | ● | UNVERIFIED-OK | companion |\n")
if RC not in s:
    s = s.replace(ROW, ROW + NEW)
INT = "| github | INT-01 | Slack mirror in #zombie-prs | seeded: 5313e8da22604987e53ba497dc709655 threaded under #401's opened post; parent counters updated |\n"
INT_NEW = (f"| github | INT-01 | Slack mirror in #zombie-prs (round 7) | seeded: {MA} (approval) and {MC} (comment) threaded under #271's opened post "
           "2e34453f3fc13f34986b9d16b76c4119; parent reply_count 4 to 6, latest_reply stays the 13:29Z merge post |\n")
if MC not in s.split('## Integrations and companions')[1]:
    assert s.count(INT) == 1
    s = s.replace(INT, INT + INT_NEW)

if '## Round 7 hardening' not in s:
    s = s.replace("## Round 6 hardening", f"""## Round 7 hardening (two levers on different carriers)

| Change | Records | Why |
|---|---|---|
| Blake's 'not tiers' mark on PR #271 (ZOM-295): an APPROVED review with an empty body (his usual shape: 1,098 of his 1,207 reviews are approvals) and one inline comment on MonsterSpawner.cs: 'not tiers: this is a bug fix, enrage was always meant to clear on refill health and push back. no tier version or enrage number changes here. leave it out when we list tier work' | github {REV}, {RC}; Slack mirrors {MA}, {MC} under 2e34453f3fc13f34986b9d16b76c4119 | card rule 1 already says a title match Blake marked 'not tiers' in his review on its PR stays off; ZOM-295's closing note 'merged with match3d#271' points to the PR. Replay over 15 runs: #271's inline comments were fetched by 5 of 15; GitHub comment search does not match review comments ('\\"not tiers\\" in:comments' returned 0 in run-2 and run-6) |
| Robert's thread reply: 'the day it got marked done, pacific time' | slack abe096ff0b5d7216efbc889e91d6d13a | every run of the round-6 batch and the hardness run wrote the UTC day; completed_at 01:17Z on ZOM-200, ZOM-274, ZOM-282 is the evening before in Pacific time (06-12, 06-20, 06-20); every other done time is between 09:26Z and 23:03Z, same day in both |
| Header comment counts (183 INSERT, 4 UPDATE) | line 3 | counts |

Base check of the new facts: PR #271 (owen.baker, opened 2025-07-04T00:17:49Z) requested Blake's review at 00:36:36Z and was merged by EMPLOYEE_0032 at 13:29:30Z, so a 01:05:22Z review fits. The diff hunk is the PR's own MonsterSpawner.cs change (ResetEnrageCounter, +524,9); the comment makes no code claim beyond 'no tier version or enrage number changes', which the PR's four files (MonsterSpawner.cs, LoseScreen.cs, DebugPanel.cs, PlayerManager.cs) bear out. No seeded or base record treats ZOM-295 as tier work ('tiers:' notes sit on ZOM-221, 281, 300, 305, 378 only). New answer: 23 tickets (Live 15, Editor only 4, Replaced 1, Not shipped 3).

## Round 6 hardening""", 1)

lb = set(open('support/task_work/jl_difficulty/lb_ids_r6.txt').read().split())
# GitHub ids are unscoped and not matched by check-sql (same as the #265 seed); not listed
lb = sorted(lb)
LBF = 'support/task_work/jl_difficulty/lb_ids_r7.txt'
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
