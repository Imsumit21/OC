"""Round 7 rubric: the /rubric r3 PASS rubric (68 rows) brought to SQL b64bc2f2c6dc.

Changes: 23 tickets / 15 Live (ZOM-295 off by Blake's 'not tiers' on PR 271); ZOM-281 Live replaces the ZOM-246 spot check;
the seven Editor only / Not shipped comment rows also need both builds (Leonard's thread reply); Blake's editor/debug rule
now cites his reply (its own thread); Robert's three columns (header row + 3 spot checks, Pacific or UTC day accepted
per /prompt r14); an exact-key row for the DM's Editor only list; Brian's role weight 5 (multi-source supersession);
starting tier also accepts '10 levels played' (/prompt r14).
Writes task_inputs/09_Rubrics.json and Working_Files/09_Rubrics.draft_with_plan_ids.json. Run from Task_Authoring-2.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import truth7 as T  # noqa: E402

S = os.environ.get('R3_DIR', '/tmp/claude-1000/-home-sumit-Downloads-OC-OC/d90c98e9-996d-4e3a-824a-b4d92e5eb889/scratchpad/r7oebak')
BASE = json.load(open(os.path.join(S, '09_Rubrics.json')))
DRAFT = json.load(open(os.path.join(S, '09_Rubrics.draft_with_plan_ids.json')))
assert len(BASE) == 68 and len(DRAFT) == 68

MAIL = "Blake's 'store builds for monday' mail julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com>"
BREPLY_ID = "julia.lawson@harmonygames.co/<CA5_F2rDr1wRIt9hs5OQOh24VwdKeAGryNjbRuXV@mail.gmail.com>"
REPLY = f"Blake's reply 'editor stuff and ZOM-199, before Monday' {BREPLY_ID}"
PR271 = "Blake's review comment harmonygames-Games/match3d#271#rc_1"
PR265 = "Blake's review comment harmonygames-Games/match3d#265#rc_7"
ASKR = "Leonard's reply under the ask, D05HB64NMQU/1759262838.442871"
ROBERT = "Robert's reply in the group chat, CAFC495E4006/1759229513.774912"
CARD2 = "Trello card 'Difficulty baseline (Julia)' 68daca5871dba40417a00383, rule 2"
T_ = "on the Tickets tab of the ZM difficulty baseline register"


def fix_text(x):
    x = x.replace(f"the store builds mail julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> strips only editor and debug folders",
                  f"Blake's reply {BREPLY_ID} says only level editor, Editor-folder and debug tooling is stripped")
    x = x.replace("read against Blake's mail. Blake's mail: 'A ticket whose changes", "read against Blake's reply. Blake's reply: 'A ticket whose changes")
    x = x.replace("the store builds mail julia.lawson@harmonygames.co/<CAAMNAwYx-0CiDbK185Gu5MJ7tQOQpotFjqOw79t@mail.gmail.com> decides the status",
                  f"Blake's reply {BREPLY_ID} decides the status")
    if MAIL in x and BREPLY_ID not in x:
        x = x.replace(MAIL, f"{MAIL}; {REPLY}")
    if PR265 in x and PR271 not in x:
        x = x.replace(PR265, f"{PR265}; {PR271}")
    x = x.replace("'after the first 10 levels', 'after the first 10 levels played', 'after 10 levels'", "'after the first 10 levels', 'after 10 levels'")
    x = x.replace("passes: wording that counts 10 games, attempts or plays,", "passes: wording that counts 10 games, attempts, plays or levels played,")
    return x


rows = []
for i, (b, d) in enumerate(zip(BASE, DRAFT), 1):
    r = {k: b[k] for k in ('title', 'category', 'weight', 'justification', 'evidence')}
    meta = {k: d[k] for k in ('plan_row', 'r1', 'cr')}
    for k in ('title', 'justification', 'evidence'):
        r[k] = fix_text(r[k])
    rows.append((i, r, meta))


def get(i):
    return next(r for j, r, m in rows if j == i)


def setmeta(i, cr):
    next(m for j, r, m in rows if j == i)['cr'] = cr


# counts
r = get(5)
r['title'] = r['title'].replace("exactly 24 ticket rows", "exactly 23 ticket rows")
r['justification'] = r['justification'].replace("the notes doc and the PR 265 review.", "the notes doc and the PR 265 and PR 271 reviews.")
r['evidence'] = r['evidence'].replace("Accept: exactly 24 rows", "Accept: exactly 23 rows")
r = get(6)
r['title'] = r['title'].replace("exactly 16 tickets with the status Live", "exactly 15 tickets with the status Live")
r['justification'] = ("Multi-source: needs every scope cut and every status call; Leonard's reply D05HB64NMQU/1759262838.442871 drops the six analytics "
                      "and tutorial tickets and Blake's 'not tiers' comment harmonygames-Games/match3d#271#rc_1 drops ZOM-295, which leaves 15 Live.")
r['evidence'] = r['evidence'].replace("Accept: exactly 16 rows", "Accept: exactly 15 rows")
setmeta(6, "a run that keeps ZOM-295 (24 rows, 16 Live) fails; the PR 271 inline comment is the deciding record")
r = get(53)
r['title'] = r['title'].replace("that 24 tickets made the list", "that 23 tickets made the list")
r['evidence'] = r['evidence'].replace("Accept: 24", "Accept: 23")
r = get(54)
r['title'] = r['title'].replace("that 16 tickets are Live", "that 15 tickets are Live")
r['evidence'] = r['evidence'].replace("Accept: 16 Live.", "Accept: 15 Live.")
# ZOM-281 replaces the ZOM-246 spot check (Live group stays at 5)
r = get(10)
r['title'] = f"The Agent records the status Live for ZOM-281 {T_}"
r['justification'] = ("Interpretation: member only through Blake's 'tiers:' closing note cmt_df69e4a92767cbff0000 on a ticket assigned to someone else, "
                      f"with no title keyword; Blake's reply {BREPLY_ID} says only level editor, Editor-folder and debug tooling is stripped.")
r['evidence'] = (f"Sources: ZOM-281's closing note cmt_df69e4a92767cbff0000 ('tiers: closing. checked on the dev build'); Trello card 'Difficulty baseline (Julia)' "
                 f"68daca5871dba40417a00383, rule 1; {REPLY}. Accept: 'ZOM-281' Live.")
setmeta(10, "a run that scans only Blake's own tickets for 'tiers:' misses ZOM-281 (/hardness r6 F1)")
# comments name the builds
for i in range(45, 52):
    r = get(i)
    k = r['title'].split('Linear issue ')[1].split(' ')[0]
    r['title'] = (f"The Agent adds a new comment on Linear issue {k} saying its change is not in the store builds iOS 0.3.49 and Android 0.3.133 "
                  "(any wording that names both builds as lacking the change passes)")
    r['justification'] = ("Multi-source: the checklist's rule 6 change ('the Editor only and Not shipped tickets get a comment too', 68dc033bf7d24e86b8a9cc67) "
                          f"plus {ASKR}: 'put the two builds in the comment (ios 0.3.49 and android 0.3.133)'.")
    r['evidence'] = (f"Sources: the card's 'Before Monday' checklist 68dc033bf7d24e86b8a9cc67; {ASKR}; {MAIL}. "
                     f"Accept: a new '{k}' comment that names iOS 0.3.49 and Android 0.3.133 as the store builds without the change, any wording.")
    setmeta(i, "a comment that says 'not in the store builds' without the two build numbers fails")
# Brian: multi-source supersession
r = get(39)
r['weight'] = 5
r['justification'] = ("Multi-source: rule 7 says everyone else comments, the checklist's rule 7 change gives Brian edit, and Leonard's later reply "
                      "D05HB64NMQU/1759267002.665190 (Sep 30 21:16Z) takes that back; the latest of the three decides the role.")
r['evidence'] = ("Sources: the tuning invite evt_91674a9c23d012a9ac34da; the card's 'Before Monday' checklist 68dc033bf7d24e86b8a9cc67; "
                 "Leonard's reply under Julia's Sep 29 question, D05HB64NMQU/1759267002.665190. Accept: brian.foster@harmonygames.co commenter.")

out = [(r, m) for j, r, m in rows]
# exact Editor only keys in the DM (after the four per-key rows)
pos = next(n for n, (r, m) in enumerate(out) if r['title'].startswith("The Agent names ZOM-315 in its DM reply")) + 1
out.insert(pos, (dict(title="The Agent names exactly ZOM-173, ZOM-200, ZOM-277 and ZOM-315 as the Editor only tickets in its DM reply to Leonard",
                      category="Outcome", weight=3,
                      justification=("Multi-source: Leonard asks for 'the keys of the not shipped ones and the editor only ones so i know who to chase' "
                                      "(D05HB64NMQU/1759262838.442871); his later reply D05HB64NMQU/1759267002.665190 takes ZOM-162, 163, 201 and 250 off "
                                      "and Blake's review comment harmonygames-Games/match3d#265#rc_7 keeps ZOM-312 off, so the chase list is these four."),
                      evidence=(f"Sources: {ASKR}; Leonard's reply under Julia's Sep 29 question, D05HB64NMQU/1759267002.665190; {PR265}; {REPLY}. "
                                "Accept: the reply's Editor only keys are exactly ZOM-173, ZOM-200, ZOM-277 and ZOM-315.")),
                 dict(plan_row='new', r1='added', cr="a reply listing ZOM-162, 163, 201, 250 or 312 as Editor only fails")))
# Robert's three columns: header row + three spot checks (Pacific or UTC day accepted, /prompt r14)
pos = next(n for n, (r, m) in enumerate(out) if r['title'].startswith("The Agent records ZOM-280's Linear state")) + 1
R293 = next(x for x in T.ROWS if x['id'] == 'ZOM-293')
R200 = next(x for x in T.ROWS if x['id'] == 'ZOM-200')
assert R293['assignee'] == 'Robert' and R293['priority'] == 4 and R200['done_pt'] == '2025-06-12'
NEW = [
    (f"The Agent gives the Tickets tab of the ZM difficulty baseline register a column each for the ticket's Linear assignee, the day it was marked done and its Linear priority", 1,
     f"Lookup: card rule 2 adds 'the three things Robert asked for' to the agenda layout; {ROBERT} names them.",
     f"Sources: {CARD2}; {ROBERT}. Accept: three columns holding assignee, done day and priority, in any order and position.",
     "a run that never opens the group chat thread has the agenda's columns only"),
    (f"The Agent records Robert as the Linear assignee of ZOM-293 {T_}", 1,
     f"Lookup: ZOM-293's Linear assignee, asked for in {ROBERT}.",
     f"Sources: {ROBERT}; ZOM-293 in Linear (assignee Robert). Accept: Robert or robert@harmonygames.co.",
     "assignee cells copied from the creator field fail"),
    (f"The Agent records ZOM-293's Linear priority as Low {T_} (Low or the number 4 passes)", 1,
     f"Lookup: ZOM-293's Linear priority, asked for in {ROBERT}.",
     f"Sources: {ROBERT}; ZOM-293 in Linear (priority 4, Low). Accept: Low or 4.",
     "a priority taken from a label or a guess fails"),
    (f"The Agent records 2025-06-12 as the day ZOM-200 was marked done {T_} (Robert asked for Pacific time; the UTC day 2025-06-13 also passes)", 1,
     f"Lookup: ZOM-200's completed_at 2025-06-13T01:17:38Z is June 12 in Pacific time, which {ROBERT} asks for.",
     f"Sources: {ROBERT}; ZOM-200 in Linear (completed_at 2025-06-13T01:17:38Z). Accept: 2025-06-12 or 2025-06-13, any date format.",
     "a blank done day for a Done ticket fails"),
]
for n, (title, w, j, e, cr) in enumerate(NEW):
    out.insert(pos + n, (dict(title=title, category="Outcome", weight=w, justification=j, evidence=e),
                         dict(plan_row='new', r1='added', cr=cr)))

for r, m in out:
    for k in ('title', 'justification', 'evidence'):
        assert '—' not in r[k] and '\r' not in r[k], (k, r['title'][:60])
json.dump([r for r, m in out], open('task_inputs/09_Rubrics.json', 'w'), indent=2, ensure_ascii=False)
json.dump([{**r, **m} for r, m in out], open('task_inputs/Working_Files/09_Rubrics.draft_with_plan_ids.json', 'w'), indent=2, ensure_ascii=False)
print('rows', len(out), 'weight', sum(r['weight'] for r, m in out))
