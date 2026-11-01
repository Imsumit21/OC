"""Round 5 dossier update: text edits for the moved reply + fresh verbatim tool blocks.

Usage (from Task_Authoring-2): python3 support/task_work/jl_difficulty/dossier_r5.py
"""
import re
import subprocess

D = 'task_inputs/Working_Files/01_Grounding_Dossier.md'
SQL = 'task_inputs/01_Universe_Inject.sql'
MAN = 'task_inputs/Working_Files/01_Hardness_Manifest.json'
s = open(D).read()
REPLY = "julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>"
NEWT = "julia.lawson@harmonygames.co/1844695547248825769"


def rep(old, new, n=1):
    global s
    c = s.count(old)
    assert c == n, (c, n, old[:90])
    s = s.replace(old, new)


def run(args):
    p = subprocess.run(['python3'] + args, capture_output=True, text=True)
    return (p.stdout + p.stderr).rstrip('\n')


# --- text edits
rep("| julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> | gmail | Julia's own mailbox copy (INBOX), thread julia.lawson@harmonygames.co/1844679607844896665 | LB H2 reply |",
    f"| julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com> | gmail | Julia's own mailbox copy (INBOX), own thread {NEWT} (round 5: Blake changed the subject) | LB H2 reply |")
rep("| 12 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844679607844896665 | H2 thread | ● | Julia's mailbox | container |",
    "| 12 | gmail.gmail_threads | julia.lawson@harmonygames.co/1844679607844896665 | H2 thread (first mail only) | ● | Julia's mailbox | container |\n"
    f"| 12b | gmail.gmail_threads | {NEWT} | H2 reply thread (round 5) | ● | Julia's mailbox | container |")
rep("""Record:              gmail.gmail_messages · julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>
Agent's likely query: "Re: store builds for monday" via the same thread""",
    """Record:              gmail.gmail_messages · julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>
Agent's likely query: card rules 3 and 6 name "his reply to it"; gmail search "from:arthur.blake@harmonygames.co" or "ZOM-199" (own thread, subject "editor stuff and ZOM-199, before Monday"; the "store builds" search does not return it)""")
rep("Chain position:      terminal (reply under the first message)", "Chain position:      terminal (reply to the first message, own Gmail conversation)")
rep("Blake 2025-09-30T09:12:44Z: store builds iOS 0.3.49 / Android 0.3.133, cut Sep 26; level editor, Editor folders and debug menu stripped | Julia's mailbox | authority |",
    "Blake 2025-09-30T09:12:44Z: store builds iOS 0.3.49 / Android 0.3.133, cut Sep 26 (round 5: the stripping rule moved to his reply) | Julia's mailbox | authority |")
rep("Blake 2025-09-30T13:26:05Z: the build checks cpm > 90, not >= 90; ZOM-199 is wrong | Julia's mailbox | overturning evidence |",
    f"Blake 2025-09-30T13:26:05Z, reply in its own thread {NEWT} (subject 'editor stuff and ZOM-199, before Monday'): level editor (Assets/Scripts/LevelEditor, LevelDesigner panels), Editor folders and the debug menu (Assets/Scripts/Debug) are stripped before shipping, so editor-only tickets never reached players; the code checks cpm > 90 when the 10th game ends (wins and losses), ZOM-199's '>= 90 after the first 10 levels' is wrong | Julia's mailbox | authority + overturning evidence (hardening round 5) |")
rep("| D05HB64NMQU/1759262838.442871 | seeded | Leonard 2025-09-30T20:07:18Z, thread reply under the ask: drop ZOM-30, ZOM-49, ZOM-50, ZOM-161 (analytics) and ZOM-262, ZOM-275 (tutorial); the reply also lists the Not shipped and Editor only keys | DM | amendment (hardening L1) |",
    "| D05HB64NMQU/1759262838.442871 | seeded | Leonard 2025-09-30T20:07:18Z, thread reply under the ask: drop ZOM-30, ZOM-49, ZOM-50, ZOM-161 (analytics) and ZOM-262, ZOM-275 (tutorial); the reply also lists the Not shipped and Editor only keys; round 5: the Editor only and Not shipped comments name the two builds (ios 0.3.49, android 0.3.133) | DM | amendment (hardening L1, round 5 L9) |")
rep("| trello:68daca5871dba40417a00383 | seeded | rules 1–7 (Leonard 2025-09-29T18:05:12Z);",
    "| trello:68daca5871dba40417a00383 | seeded | rules 1–7 (Leonard 2025-09-29T18:05:12Z; round 5: rule 3 reads 'Blake's store builds mail and his reply to it', in the desc and the 14:04Z updateCard action);")

if '## Round 5 hardening' not in s:
    s = s.replace("## Record ledger", """## Round 5 hardening (failure-pattern gate)

| Change | Records | Why |
|---|---|---|
| Blake's reply moves to its own Gmail conversation (he changed the subject to 'editor stuff and ZOM-199, before Monday'; In-Reply-To/References kept) and now carries the level editor / Editor folder / debug menu stripping rule and both ZOM-199 corrections (> 90; checked when the 10th game ends, wins and losses) | 5 mailbox copies of julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>; 5 new gmail_threads rows (id = date ms << 20 + random bits, Gmail's format) | a second carrier independent of Slack threads (A14 Gmail reply): baseline round 5, runs 1/4/6 failed identically (pattern 60%) |
| The first mail keeps only the builds and the Sep 26 cut; its thread snippets now show the first mail | 5 copies of <CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> and their thread rows | the stripping rule lives in one place |
| Card rule 3: 'Blake's store builds mail and his reply to it' | card 68daca5871dba40417a00383 desc and its updateCard action 68dbe36f4b2b4fffb7525fde | incorporates the reply (rule 6 already names it) |
| Leonard's thread reply under the ask adds: name the two builds in the Editor only / Not shipped comments | D05HB64NMQU/1759262838.442871 | per-comment output rule (A21) on the thread carrier |

Code check of every new claim (match3d at the Sep 26 cut): TierManager.cs `totalGames == 10`, `cpm > 90.0f`; WinHistory.cs GetTotalGames = wins + losses; Assets/Scripts/LevelEditor and Assets/Scripts/Debug exist as named. The reply never uses the words 'store' or 'builds', so the 'store builds' search returns only the first mail's thread.

## Record ledger""", 1)

# --- fresh verbatim blocks
lb = set()
for line in re.findall(r"\[YES LB\] L\d+ \S+ \S+ (.*?) - ", s):
    lb |= {x.strip() for x in line.split(',') if len(x.strip()) > 6 and not x.strip().endswith('…')}
lb = sorted(lb | {NEWT})
LBF = 'support/task_work/jl_difficulty/lb_ids_r5.txt'
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
