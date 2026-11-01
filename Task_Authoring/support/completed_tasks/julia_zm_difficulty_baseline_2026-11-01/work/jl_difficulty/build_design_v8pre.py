"""Julia Lawson - Zombie Match 3D difficulty baseline register (design builder; reads the base exports, never writes them).

Writes, next to this file:
  truth.json         candidates, membership, per-ticket status (the ground truth the dossier/rubric will reuse)
  minted_ids.json    every seeded id with its own timestamp (collision-checked against the base)
  planned_text.json  the wording /create-injection seeds verbatim (every delegation quote is a substring of one of these)
and the draft manifest Task_Authoring-2/task_inputs/Working_Files/01_Hardness_Manifest.draft.json.
"""
import datetime as D
import hashlib
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
B = '/home/sumit/Downloads/OC/OC/'
WF = B + 'Task_Authoring-2/task_inputs/Working_Files/'
LIN = json.load(open(B + 'HarmonyGames_Other_Services/Services_Data/linear/data.json'))
GH = json.load(open(B + 'HarmonyGames_GitHub/Services_Data/github/data.json'))


def ts(s):
    return D.datetime.fromisoformat(s.replace('Z', '+00:00')).timestamp()


def iso(t):
    return D.datetime.fromtimestamp(t, D.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


def h(seed, n):
    return hashlib.sha256(seed.encode()).hexdigest()[:n]


CLOCK = '2025-10-01T00:00:00Z'
users = {u['id']: u['email'] for u in LIN['users']}
uid = {u['email']: u['id'] for u in LIN['users']}
idmap = {i['id']: i['identifier'] for i in LIN['issues']}
ISS = {i['identifier']: i for i in LIN['issues']}
ARTHUR = 'arthur.blake@harmonygames.co'

# ------------------------------------------------------------------ cohort rule (card rule 1 + comment)
CARD = re.compile(r'\b(difficulty|difficult|tier|tiers|tiering|enrage|enraged|blunder|cpm)\b', re.I)
AMEND = re.compile(r'\battack power\b', re.I)


def in_window(i):
    return i['created_at'][:10] <= '2025-08-31'


cands = []
for i in LIN['issues']:
    if not i['identifier'].startswith('ZOM-') or not in_window(i) or i['state_id'] == 'Duplicate':
        continue
    t = i['title'] or ''
    reason = ('card' if CARD.search(t) else 'amend' if AMEND.search(t) else
              'arthur' if users.get(i['assignee_id']) == ARTHUR else None)
    if reason is None:
        continue
    if i['updated_at'] >= CLOCK and reason != 'arthur':
        raise SystemExit(f"title candidate touched after the clock: {i['identifier']}")
    cands.append(i)
cands.sort(key=lambda i: i['number'])

# ------------------------------------------------------------------ per-ticket files (Arthur's closing notes)
DD = 'Assets/Scripts/DynamicDifficulty/'
TAGGED = {  # Blake tickets he tagged "tiers:" in his closing note (human tag; no file claims)
    'ZOM-221': "spawn gaps are fixed on every tier version of the tracks",
    'ZOM-300': "how many sets come off now depends on the player's streak level",
    'ZOM-305': "a lost level costs one life again",
    'ZOM-378': "level 1 is back in the list so the first levels line up with their tier versions again",
}
NEAR = {  # Arthur tickets that sound like difficulty work but touched no tier-code file (no match3d PR)
    'ZOM-96': ['Assets/Scripts/Monster/MonsterSpawner.cs'],
    'ZOM-190': ['Assets/Scripts/LevelEditor/UI/StatsPanel.cs'],
    'ZOM-209': ['Assets/Match3D/Game/Levels/AlgoLevelSettings.cs'],
    'ZOM-257': ['Assets/Match3D/Game/Levels/LevelObjectHelpers.cs'],
    'ZOM-289': ['Assets/Match3D/Game/Levels/LevelObjectHelpers.cs', 'Assets/Match3D/Game/Levels/GameLoader.cs'],
    'ZOM-313': ['Assets/Scripts/LevelEditor/UI/MonsterTimeline/'],
    'ZOM-383': ['Assets/Match3D/Game/Levels/LevelObjectHelpers.cs'],
    'ZOM-392': ['Assets/Match3D/Game/Levels/AlgoLevelSettings.cs'],
}
# candidates with a linked match3d PR: the note cites the PR (its CodeRabbit file table is the file list)
LINKED = {'ZOM-173': ['243'], 'ZOM-244': ['258', '283'], 'ZOM-292': ['267'], 'ZOM-295': ['271'], 'ZOM-303': ['244'],
          'ZOM-307': ['243'], 'ZOM-312': ['265'], 'ZOM-345': ['289'], 'ZOM-352': ['282'], 'ZOM-370': ['296'],
          'ZOM-371': ['296'], 'ZOM-372': ['296'], 'ZOM-387': ['319']}
TITLE_FILES = {  # Arthur's title-matching tickets
    'ZOM-42': [DD + 'TierManager.cs', DD + 'WinRateRule.cs', 'Assets/Scripts/LevelEditor/UI/LevelDesignPanel.cs'],
    'ZOM-45': ['Assets/Scripts/LevelEditor/UI/LevelSettings.cs', 'Assets/Match3D/Game/Levels/GameLoader.cs'],
    'ZOM-50': ['Assets/Scripts/Utils/AnalyticsManager.cs'],
    'ZOM-162': ['Assets/Scripts/LevelEditor/UI/MonsterTimeline/'],
    'ZOM-163': ['Assets/Scripts/LevelEditor/UI/LevelPreviewPanel.cs'],
    'ZOM-173': ['Assets/Scripts/LevelEditor/UI/LevelObjectsPanel.cs', 'Assets/Scripts/LevelEditor/UI/LevelObjectItem.cs'],
    'ZOM-199': [DD + 'CPMTierManager.cs', 'Assets/Scripts/Debug/DebugDynamicDifficultyPanel.cs'],
    'ZOM-200': ['Assets/Scripts/Debug/DebugDynamicDifficultyPanel.cs'],
    'ZOM-201': ['Assets/Scripts/Debug/DebugDynamicDifficultyPanel.cs', 'Assets/Scripts/Debug/DebugPanel.cs'],
    'ZOM-202': [],
    'ZOM-250': ['Assets/Scripts/LevelEditor/UI/StatsPanel.cs', 'Assets/Scripts/LevelEditor/UI/LevelDesignPanel.cs'],
    'ZOM-277': ['Assets/Scripts/LevelEditor/UI/StatsPanel.cs'],
    'ZOM-282': ['Assets/Scripts/Monster/Monster.cs'],
    'ZOM-303': [DD + 'TierManager.cs', 'Assets/Match3D/Game/Levels/GameLoader.cs'],
    'ZOM-312': ['Assets/Scripts/LevelEditor/UI/LevelSettings.cs'],
    'ZOM-315': ['Assets/Scripts/LevelEditor/UI/StatsPanel.cs'],
}
AREA = [  # neutral notes for the rest of Arthur's tickets (real directories, by topic)
    (r'icon|sprite|border', 'Assets/Match3D/Game/Items/ItemIconGenerator.cs'),
    (r'level editor|editor|play button|multi edit|easy add|copy|migrat', 'Assets/Scripts/LevelEditor/UI/'),
    (r'quest|plague|race|economy|leaderboard', 'Assets/Scripts/LiveOps/'),
    (r'ipad|stretch|tablet|resolution|screen|overlay|ui|tool tip|hud|profile|items page', 'Assets/Scripts/UI/'),
    (r'algo', 'Assets/Match3D/Game/Levels/AlgoLevelSettings.cs'),
    (r'spawn|monster|zombie', 'Assets/Scripts/Monster/'),
    (r'drop|item|throw|matching|deck|grid|size|boss buster|null ref|artifact|orientation|insertion|card',
     'Assets/Match3D/Game/Items/'),
    (r'singular|analytics|event', 'Assets/Scripts/Utils/AnalyticsManager.cs'),
    (r'haptic', 'Assets/Scripts/Utils/HapticManager.cs'),
    (r'lives|life', 'Assets/Scripts/Player/LivesManager.cs'),
]

# ------------------------------------------------------------------ ground truth per member
REPLACED = {'ZOM-254': 'ZOM-282'}
EDITOR = {'ZOM-162', 'ZOM-163', 'ZOM-173', 'ZOM-200', 'ZOM-201', 'ZOM-250', 'ZOM-277', 'ZOM-312', 'ZOM-315'}
NOT_SHIPPED_DONE = set()   # Done in Linear; level demotion behind a flag that is off in the store builds
PRS = {'ZOM-173': 'match3d#243', 'ZOM-303': 'match3d#244', 'ZOM-312': 'match3d#265', 'ZOM-295': 'match3d#271'}

truth = []
for i in cands:
    k, t = i['identifier'], i['title']
    reason = 'card' if CARD.search(t) else 'amend' if AMEND.search(t) else 'arthur'
    member = reason in ('card', 'amend') or k in TAGGED
    if not member:
        status = None
    elif i['state_id'] != 'Done' or k in NOT_SHIPPED_DONE:
        status = 'Not shipped'
    elif k in REPLACED:
        status = 'Replaced'
    elif k in EDITOR:
        status = 'Editor only'
    else:
        status = 'Live'
    truth.append(dict(id=k, title=t, state=i['state_id'], assignee=users.get(i['assignee_id']), created=i['created_at'],
                      completed=i['completed_at'], canceled=i['canceled_at'], updated=i['updated_at'],
                      parent=idmap.get(i['parent_id']), reason=reason, member=member, status=status,
                      replaced_by=REPLACED.get(k) if status == 'Replaced' else None, pr=PRS.get(k),
                      decided_by_comment=k in TAGGED or k in ('ZOM-45', 'ZOM-277', 'ZOM-315', 'ZOM-173', 'ZOM-312', 'ZOM-254')))
members = [r for r in truth if r['member']]
counts = {}
for r in members:
    counts[r['status']] = counts.get(r['status'], 0) + 1
OUT_TRUTH = dict(clock=CLOCK, candidates=len(truth), members=len(members), counts=counts,
                 card_only=sum(r['reason'] == 'card' for r in members), amend=sum(r['reason'] == 'amend' for r in members),
                 tagged=sum(r['reason'] == 'arthur' for r in members), rows=truth)

# ------------------------------------------------------------------ minted ids
out = {}
DM_LEO = 'D05HB64NMQU'       # Leonard <-> Julia DM
ZD = 'C090N54TG79'           # #zombie-design (Julia, Robert, Leonard, Arthur are members)
ZPRS = 'C093LEZGF6J'         # #zombie-prs (GitHub app mirror of match3d; Julia is not a member)
slack = [
    ('S_ROBERT_SUM', ZD, '2025-09-29T22:31:17.402611Z'),     # wrong summary (A1) - Brian
    ('S_BRIAN_POST', ZD, '2025-09-30T16:12:40.118527Z'),     # non-authoritative: post the list here - Oliver
    ('S_MIRROR_401', ZPRS, '2025-08-25T17:02:31.508113Z'),   # GitHub-app mirror of the seeded #401 comment
    ('S_ASK', DM_LEO, '2025-09-30T19:48:26.530914Z'),        # anchor A1
]
for k, c, t in slack:
    tsv = f"{ts(t):.6f}"
    out[k] = {'channel': c, 'ts': tsv, 'id': h(f"{c}|{tsv}", 32), 'at': t}


def trello(seed, t):
    return format(int(ts(t)), '08x') + h('trello-jl-' + seed, 16)


for k, t in [('T_H1CARD', '2025-09-29T18:05:12Z'), ('T_H1CREATE', '2025-09-29T18:05:12Z'),
             ('T_H1UPD', '2025-09-30T14:04:31Z'), ('T_H1CMT', '2025-09-30T15:41:55Z'),
             ('T_DDCARD', '2025-06-02T15:10:44Z'), ('T_DDCREATE', '2025-06-02T15:10:44Z')]:
    out[k] = {'id': trello(k, t), 'at': t}


def f(seed):
    return 'f_' + h('drive-jl' + seed, 22)


def d(seed):
    return 'd_' + h('drive-jl' + seed, 22)


out['FOLDER_ZMDIFF'] = {'id': d('zm_difficulty'), 'at': '2025-06-13T15:02:11Z'}
out['SHEET_KNOBS'] = {'id': f('zm_monster_enrage'), 'created': '2025-08-26T17:40:12Z', 'at': '2025-09-02T19:12:40Z',
                      'owner': 'julia.lawson@harmonygames.co'}
out['DOC_AGENDA'] = {'id': f('zm_tuning_agenda_oct6'), 'created': '2025-09-29T18:31:09Z', 'at': '2025-09-30T11:04:37Z'}


def gid(t):
    return str(int(ts(t) * 1000) << 20 | int(h('g' + t, 5), 16) & 0xFFFFF)


def msgid(key):
    import base64
    return '<CA' + base64.b64encode(hashlib.sha256(key.encode()).digest()).decode()[:38].replace('/', '_').replace('+', '-') + '@mail.gmail.com>'


for k, t in [('G_BUILD', '2025-09-30T09:12:44Z'), ('G_BUILD_RE', '2025-09-30T13:26:05Z')]:
    out[k] = {'at': t, 'gmail_id': gid(t), 'message_id': msgid(k)}
out['G_BUILD']['thread_id'] = out['G_BUILD']['gmail_id']
out['G_BUILD_RE']['thread_id'] = out['G_BUILD']['gmail_id']
out['G_BUILD']['mailboxes'] = ['julia.lawson@harmonygames.co', 'leonard.hayes@harmonygames.co', 'robert@harmonygames.co',
                               'arthur.blake@harmonygames.co', 'brian.foster@harmonygames.co']

SESSION_CALS = ['leonard.hayes@harmonygames.co', 'julia.lawson@harmonygames.co', 'robert@harmonygames.co',
                'arthur.blake@harmonygames.co', 'brian.foster@harmonygames.co']
out['GCAL_TUNING'] = {'ical_uid': h('ical_zm_tuning_oct6', 32) + '@hg4', 'start': '2025-10-06T17:00:00Z',
                      'end': '2025-10-06T18:00:00Z', 'created': '2025-09-29T18:24:51Z', 'at': '2025-09-29T18:24:51Z',
                      'organizer': 'leonard.hayes@harmonygames.co',
                      'copies': {cal: 'evt_' + h('zmtuning' + cal, 22) for cal in SESSION_CALS}}

# /injection F1: injection SQL can't edit Confluence -> Robert's write-up is a Slides deck, Blake's correction a Slack message
out['CONF_DDA'] = {'id': f('zm_dynamic_difficulty_deck'), 'at': '2025-06-16T14:10:33Z', 'owner': 'robert@harmonygames.co',
                   'slides': ['slide_' + h('jl-deck-s' + str(i), 12) for i in range(3)],
                   'elements': ['el_' + h('jl-deck-e' + str(i), 12) for i in range(3)]}
_tcc = '2025-09-03T15:22:09.304417Z'
out['CC_ART'] = {'id': h(f"C090N54TG79|{ts(_tcc):.6f}", 32), 'channel': 'C090N54TG79', 'ts': f"{ts(_tcc):.6f}", 'at': _tcc}
out['PRC_244'] = {'id': 'harmonygames-Games/match3d#401#c_2', 'pr': 'harmonygames-Games/match3d#401',
                  'at': '2025-08-25T17:02:28Z', 'author': 'EMPLOYEE_0025_GITHUB_USERNAME',
                  'timeline_event': 'harmonygames-Games/match3d#401#ev_7'}

# Linear notes: Arthur's closing note on every Arthur candidate; owners' notes on the other title/amend candidates.
NOTE_AUTHOR = {'ZOM-23': 'robert@harmonygames.co', 'ZOM-30': 'leonard.hayes@harmonygames.co',
               'ZOM-49': 'oliver.brooks@harmonygames.co', 'ZOM-161': 'oliver.brooks@harmonygames.co',
               'ZOM-258': 'marcus.bennett@harmonygames.co', 'ZOM-262': 'oliver.brooks@harmonygames.co',
               'ZOM-275': 'oliver.brooks@harmonygames.co', 'ZOM-288': 'robert@harmonygames.co',
               'ZOM-293': 'robert@harmonygames.co', 'ZOM-295': 'owen.baker@harmonygames.co'}
# EMPLOYEE_0032 tickets (token person): the QA note is Vincent's (Douglas precedent: never voice the token)
for k in ('ZOM-246', 'ZOM-254', 'ZOM-263', 'ZOM-274', 'ZOM-280'):
    NOTE_AUTHOR[k] = 'vincent.parker@harmonygames.co'
EXTRA_NOTES = {}


def area(t):
    for rx, p in AREA:
        if re.search(rx, t, re.I):
            return p
    return 'Assets/Match3D/Game/'


def note_text(r):
    k, t = r['id'], r['title']
    if k in TAGGED:
        return "tiers: closing. " + TAGGED[k]
    if k == 'ZOM-45':
        return "closing. the label shows in the editor and the level carries it at runtime too, the game reads it when it loads the level"
    if k == 'ZOM-277':
        return "closing. this is the average in the editor's stats panel, nothing changes in the game itself"
    if k == 'ZOM-315':
        return ("closing. this is the total attack power in the editor's stats panel, items without cardData now count "
                "with their base damage. nothing changes in the game itself")
    if k == 'ZOM-282':
        return ("closing. this replaces the blunder 2.0 boost from ZOM-254: enrage only adds speed and damage now, the "
                "hp part was switched off on the 19th. speed and damage still share one value")
    if k == 'ZOM-173':
        return ("merged with match3d#243 together with ZOM-307. this one is the set count in the level objects panel; the "
                "slider removal and the level model changes in that PR are ZOM-307's")
    if k == 'ZOM-312':
        return "merged with match3d#265. delete and reassign live in the level settings panel, the new events are the ones the editor listens to"
    if k == 'ZOM-292':
        return "keeping this open as the umbrella for the rest of the 2.0 list. copy monsters went in with match3d#267"
    if k in LINKED:
        prs = ' and '.join('match3d#' + n for n in LINKED[k])
        if r['state'] in ('Todo', 'Backlog', 'In Progress'):
            return f"keeping this open for the rest of it, the first part went in with {prs}"
        return f"merged with {prs}"
    if r['assignee'] == ARTHUR:
        if r['state'] == 'Canceled':
            return "dropping this one, nothing merged"
        if r['state'] in ('Todo', 'Backlog'):
            return "parking this, nothing merged yet"
        if r['state'] == 'In Progress':
            return "wip on a branch, nothing merged yet"
        return "closing. works on the dev build"
    owner = NOTE_AUTHOR.get(k)
    if owner == 'vincent.parker@harmonygames.co':
        if k == 'ZOM-254':
            return "checked on the dev build, blunder enrages the monsters on the board now"
        return "checked on the dev build, works as described" if r['state'] == 'Done' else "not reproducible anymore, closing"
    if r['state'] == 'Todo':
        return "still happens on the dev build, keeping it open"
    return "checked on the dev build, works as described"


notes = {}
for r in truth:
    k = r['id']
    i = ISS[k]
    author = ARTHUR if r['assignee'] == ARTHUR else NOTE_AUTHOR.get(k)
    if author is None:
        continue
    if i['updated_at'] >= CLOCK:          # open at the clock; changed only afterwards -> parking note before the clock
        at = iso(min(ts('2025-09-26T15:00:00Z'), ts(i['created_at']) + 86400 * 30) + 60 * (int(h('p' + k, 2), 16) % 50))
        notes[k] = {'id': 'cmt_' + h('jl-lin' + k, 20), 'issue': k, 'author': uid[author], 'author_email': author,
                    'at': at, 'text': "parking this, nothing merged yet", 'decisive': False, 'post_clock_issue': True}
        continue
    if k == 'ZOM-292':
        at = '2025-07-04T03:07:46Z'          # after match3d#267 merged (03:07:45Z), before the issue's updated_at 03:07:47Z
    if k != 'ZOM-292':
        anchor_t = i['completed_at'] or i['canceled_at'] or i['updated_at']
        at = iso(ts(anchor_t) - 60 * (4 + int(h('m' + k, 2), 16) % 20))
        if ts(at) < ts(i['created_at']):
            at = iso(ts(i['created_at']) + 300)
    notes[k] = {'id': 'cmt_' + h('jl-lin' + k, 20), 'issue': k, 'author': uid[author], 'author_email': author, 'at': at,
                'text': note_text(r), 'decisive': r['decided_by_comment']}
for k, (author, at) in EXTRA_NOTES.items():
    notes[k] = {'id': 'cmt_' + h('jl-lin' + k, 20), 'issue': k, 'author': uid[author], 'author_email': author, 'at': at,
                'text': note_text({'id': k, 'title': ISS[k]['title'], 'assignee': author, 'state': 'Done'}), 'decisive': True}
out['LIN_NOTES'] = notes

# ------------------------------------------------------------------ collision checks against the base
base_cmt = {c.get('id') for c in LIN.get('comments', [])}
assert not ({n['id'] for n in notes.values()} & base_cmt)
gh_pc = {c['id'] for c in GH['pull_request_comments']}
assert out['PRC_244']['id'] not in gh_pc
gh_ev = {e['id'] for e in GH['timeline_events']}
assert out['PRC_244']['timeline_event'] not in gh_ev
for k in ('S_ROBERT_SUM', 'S_BRIAN_POST', 'S_ASK', 'S_MIRROR_401', 'CC_ART'):
    p = B + f"HarmonyGames_Other_Services/Services_Data/slack/messages/{out[k]['channel']}/{out[k]['at'][:7]}.json"
    if os.path.exists(p):
        assert out[k]['ts'] not in {m['ts'] for m in json.load(open(p))}, k
for k, v in out.items():
    if isinstance(v, dict) and 'at' in v and isinstance(v['at'], str):
        assert v['at'] < CLOCK or k == 'GCAL_TUNING', (k, v['at'])

# ------------------------------------------------------------------ planned wording
P = {}
P['S_ASK'] = ("julia before monday's tuning session i want a baseline of the difficulty system from you, not from memory. "
              "every difficulty ticket since we started zm and whether players actually have it in the store builds right now, "
              "plus the tier and enrage numbers as they are today. the rules for the register are on the difficulty baseline "
              "card on the zm roadmap board. reply here when it's in the folder with how many tickets made the list and how many "
              "of each status")
P['S_ROBERT_SUM'] = ("for monday so we don't start from zero: everything from the june dynamic difficulty push is in the store "
                     "builds, the editor bits too (tier delete, the stats window, the debug menu). enrage is the same +50% "
                     "speed and damage for every monster like 282 says")
P['S_BRIAN_POST'] = "julia when you have the difficulty list can you drop it in here too so the rest of us can see it"
P['H1_TITLE'] = 'Difficulty baseline (Julia)'
P['H1_DESC'] = (
    "For the Oct 6 tuning session. Julia owns this one.\n"
    "1. Scope: every ZOM ticket created up to Aug 31 (so everything since we started ZM) that changed difficulty. That is any ticket with difficulty, "
    "difficult, tier, tiers, tiering, enrage, enraged, blunder or CPM as a whole word in the title, plus Blake's tickets "
    "that he counts as tier work even if the title doesn't say so: his closing note on those starts with 'tiers:'. "
    "Duplicates are out; open, cancelled and never-merged ones are in, as Not shipped.\n"
    "2. One row per ticket: ticket, title, Linear state (as you found it), status, and for Replaced the ticket or PR "
    "that replaced it. "
    "Layout as in the session agenda.\n"
    "3. Status is one of Live, Editor only, Replaced, Not shipped, judged against the store builds players have today. "
    "What is in the store builds and what counts as shipped: Blake's store builds mail.\n"
    "4. Replaced: only when a later ticket's closing note says it replaces this one. Name that ticket. Nothing else "
    "makes a ticket Replaced: bug fixes, follow-ups, later tuning and PRs that change or split its numbers don't, and a "
    "ticket players never had stays Editor only or Not shipped. ZOM-42 is the system itself: it stays Live and its rules "
    "go on the rules tab.\n"
    "5. Rules in force tab: starting tier, promotion, demotion (and whether the level drops after one) and enrage, as they "
    "work in the store builds today. "
    "Enrage is per monster: your monster enrage sheet has the numbers. The tier rules are written up in Robert's dynamic "
    "difficulty deck and in ZOM-42 itself.\n"
    "6. Ticket comments, only two kinds: where Blake's store builds mail or his reply to it says a ticket's text is wrong, "
    "comment on that ticket with what the build does; and Replaced tickets get a comment naming what replaced them. "
    "Every other ticket stays as it is, ZOM-42 and the Not shipped and Editor only ones included, even if its wording is "
    "a bit off. Same tickets, no new ones.\n"
    "7. The register goes in the ZM Difficulty folder. Share it with everyone on the tuning session invite: Robert can "
    "edit, everyone else comments.")
P['H1_DESC_OLD'] = ("For the Oct 6 tuning session. Julia owns this one. Rules go here once Blake has "
                     "confirmed what's in the store builds.")
P['H1_CMT'] = ("adding to rule 1: attack power in the title counts too, enrage tuning leans on those numbers. rest of the "
               "card stands.")
P['DD_TITLE'] = 'Difficulty baseline'
P['DD_DESC'] = (
    "For the spring difficulty pass on Domino Delights.\n"
    "1. Scope: ENG tickets from the #difficulty-optimization work (pity, bot balancing, level swaps).\n"
    "2. One row per ticket: ticket, status (Live / Not live).\n"
    "3. Live means merged to GameOfDominoes main.\n"
    "4. The list goes in the Difficulty Optimization sheet. Share it with Brian and Vincent, both can edit.")
P['DOC_AGENDA_TITLE'] = 'ZM difficulty tuning - Oct 6'
P['DOC_AGENDA_BODY'] = (
    "Agenda\n"
    "1. Baseline (Julia): the register from the difficulty baseline card. One sheet with two tabs, Tickets and Rules in "
    "force, so we tune from what players have and not from what we remember.\n"
    "2. Rage by level (Leonard): one enrage multiplier for every level is too blunt for the early funnel.\n"
    "3. Tier 0 versions (Robert): sign-off status per level band.\n"
    "4. What 0.3.22 had and what we keep (Robert).\n")
P['G_BUILD_SUBJECT'] = 'store builds for monday'
P['G_BUILD_BODY'] = (
    "Hi all,\n\nFor Monday, so we're talking about the same thing. The store builds players have today are iOS 0.3.49 "
    "(Leonard released it yesterday) and Android 0.3.133. Both were cut from main on Sep 26, and everything difficulty "
    "related was merged long before that.\n\nThe level editor (Assets/Scripts/LevelEditor and the LevelDesigner "
    "panels), anything in an Editor folder and the debug menu (Assets/Scripts/Debug) are stripped from store builds. "
    "A ticket whose changes are only level editor or debug tooling never reached players, Done or not.\n\nBlake")
P['G_BUILD_RE_BODY'] = (
    "One more, for the rules tab: the starting tier check in the build is cpm > 90, not >= 90. ZOM-199 says >= but the "
    "code never changed from the original spec, so 90 exactly stays on tier 0.\n\n"
    "Blake\n\nOn Tue, Sep 30, 2025 at 2:12 AM Arthur Blake <arthur.blake@harmonygames.co> wrote:\n"
    "> Hi all,\n>\n> For Monday, so we're talking about the same thing. The store builds players have today are iOS 0.3.49\n"
    "> (Leonard released it yesterday) and Android 0.3.133. ...")
P['GCAL_SUMMARY'] = 'ZM difficulty tuning'
P['SHEET_KNOBS_TITLE'] = 'ZM monster enrage'
MONSTERS = [("Bikekid", "0.25", "0.25"), ("Boxer", "0.5", "0.4"), ("Cheerleader", "0.6", "0.4"), ("Chef", "0.5", "0.5"),
            ("FootballPlayer", "0.6", "0.4"), ("Karen", "0.4", "0.4"), ("Magician (all three VarC versions)", "0.2", "0.2"),
            ("Mailman", "0.4", "0.4"), ("Mayor1", "0.5", "0.5"), ("Mayor2", "0.4", "0.6"),
            ("PartyGirl (both VarC versions)", "0.4", "0.3"), ("Plumber (both VarC versions)", "0.3", "0.3"),
            ("MonsterBase (default for any monster without its own value)", "0.8", "0.8")]
P['SHEET_KNOBS_TABS'] = {
    'Live': [["monster (VarC prefab)", "enrage speed", "enrage damage", "enrage hp"]]
            + [[m, sp, dm, "0"] for m, sp, dm in MONSTERS],
    'Next pass': [["proposal", "value", "who"],
                  ["enrage speed, levels 1-20, every monster", "0.3", "Leonard"],
                  ["enrage speed, levels 21+, every monster", "0.8", "Leonard"],
                  ["show the enrage boost on the monster", "yes", "Leonard"]],
    'History': [["date", "change", "ref"],
                ["2025-06-19", "enrage hp boost switched off", "Blake"],
                ["2025-08-09", "base enrage 0.6 -> 0.8 (MonsterBase)", "Robert"],
                ["2025-08-25", "speed and damage split into separate values", "match3d#401"],
                ["2025-09-02", "VarC values set (this tab: Live)", "Julia"]]}
P['CONF_DDA_TITLE'] = 'ZM dynamic difficulty - how tiers work'
P['CONF_DDA_BODY'] = (
    "Tiers -2 to +2 per level (ZOM-42); tier 0 is the default version of each level.\n"
    "Starting tier: average CPM over the first 10 levels; 90 or more starts you on tier 1, everyone else on tier 0.\n"
    "Promotion: win rate of 80% or more over the last 10 attempts moves you up one tier. On tier -2 one win promotes you.\n"
    "Demotion: 4 losses in a row moves you down one tier.\n"
    "Blunder: overfilling the match bar enrages every monster on the board: +25% walk speed, +25% damage, +25% max HP "
    "(ZOM-254, values per monster).")
P['CC_ART_BODY'] = ("fyi the blunder part of robert's tiers deck is old: enrage adds speed and damage only (split since "
                    "match3d#401), hp doesn't change, and the values are per monster. julia keeps the numbers")
P['PRC_244_BODY'] = ("this gives enrage speed and damage their own values, they shared one since ZOM-282. also drops the "
                     "old EnrageHealth method, nothing has called it since june")
P['FOLDER_ZMDIFF_NAME'] = 'ZM Difficulty'
P['NOTES'] = {k: v['text'] for k, v in notes.items()}

json.dump(OUT_TRUTH, open(os.path.join(HERE, 'truth.json'), 'w'), indent=1)
json.dump(out, open(os.path.join(HERE, 'minted_ids.json'), 'w'), indent=1)
json.dump(P, open(os.path.join(HERE, 'planned_text.json'), 'w'), indent=1, ensure_ascii=False)
print('candidates', len(truth), 'members', len(members), counts, 'card', OUT_TRUTH['card_only'], 'amend',
      OUT_TRUTH['amend'], 'tagged', OUT_TRUTH['tagged'], 'notes', len(notes),
      'decisive notes', sum(1 for n in notes.values() if n['decisive']))
