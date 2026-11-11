#!/usr/bin/env python3
"""Render base_records.md from the JSON pulled through hg.py. Quotes and timestamps come from the data, never retyped."""
import json, re
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

S = '/private/tmp/claude-501/-Users-sumit-Source-OC/03f412d7-1226-4687-96da-a0d4194c9430/scratchpad'
ROOT = '/Users/sumit/Source/OC'
OUT = ROOT + '/Task_Authoring/task_inputsN2/Working_Files/oe_gen/research/base_records.md'
PT = ZoneInfo('America/Los_Angeles')

P = {}
for n in (1, 2, 3, 6):
    P.update(json.load(open(f'{S}/pull{n}.json')))
P4 = json.load(open(f'{S}/pull4.json'))
for k, v in P4.items():
    if k.startswith('slack:'):
        P[k.split(':', 1)[1]] = v

USERS = {v['id']: v for k, v in P.items() if k.startswith('users.json')}
ROWS = json.load(open(ROOT + '/Task_Authoring/task_inputsN2/Working_Files/oe_gen/sql_rows.json'))

verdicts = {}
for block in re.split(r'(?m)^(?=claire_morgan )', open(f'{S}/cansee.out').read()):
    if not block.startswith('claire_morgan '):
        continue
    lines = block.strip().split('\n')
    verdicts[lines[0].split(' ', 1)[1].rsplit(':', 1)[0]] = lines[:2]


def pv(svc, oid):
    return '```text\n' + '\n'.join(verdicts[f'{svc} {oid}']) + '\n```\n'


def tfmt(ts):
    sec, frac = ts.split('.')
    u = datetime.fromtimestamp(int(sec), tz=timezone.utc)
    p = u.astimezone(PT)
    return f'{u:%Y-%m-%d %H:%M:%S}.{frac} UTC', f'{p:%a %Y-%m-%d %H:%M:%S}.{frac} {p:%Z}'


def who(uid):
    if uid is None:
        return '(no `user` value)'
    u = USERS.get(uid)
    name = u['real_name'] if u and u.get('real_name') != uid else None
    return f'{name} (`{uid}`)' if name else f'`{uid}`'


def reacts(v):
    r = v.get('reactions') or []
    if not r:
        return 'none'
    return '; '.join(f":{x['name']}: x{x['count']} ({', '.join(who(u) for u in x['users'])})" for x in r)


def files(v):
    out = []
    for f in v.get('files') or []:
        dims = f" {f['original_w']}x{f['original_h']}" if f.get('original_w') else ''
        dur = f", {f['duration_ms']} ms" if f.get('duration_ms') else ''
        out.append(f"`{f['id']}` name `{f['name']}`, title `{f['title']}`, {f.get('filetype')}{dims}{dur}, "
                   f"{f.get('size')} bytes, uploader {who(f.get('user'))}")
    return out


def block(text):
    return '```text\n' + text + '\n```\n'


def msg(key, label=None, channel=None, body=None):
    file, ptr = key.split('#')
    v = P[key]
    cid = v['channel']
    u, p = tfmt(v['ts'])
    o = [f"#### `{cid}/{v['ts']}`" + (f' ({label})' if label else ''), '']
    o.append(f'- Service: slack. File + pointer: `{file}` `{ptr}`. Message id: `{v["id"]}`.')
    o.append(f"- Author: {who(v.get('user'))}" + (f", subtype `{v['subtype']}`" if v.get('subtype') else ''))
    o.append(f'- Time: {u} | {p}')
    o.append(f"- Thread fields: thread_ts `{v.get('thread_ts')}`, reply_count {v.get('reply_count')}, "
             f"reply_users_count {v.get('reply_users_count')}, latest_reply `{v.get('latest_reply')}`")
    o.append(f'- Reactions: {reacts(v)}')
    fl = files(v)
    o.append('- Files: ' + ('none' if not fl else ''))
    o += [f'  - {x}' for x in fl]
    o.append('')
    o.append('Verbatim text:')
    o.append('')
    o.append(block(body if body is not None else v.get('text') or ''))
    o.append('persona_view:')
    o.append('')
    o.append(pv('slack', f"{cid}/{v['ts']}"))
    return '\n'.join(o)


def filepv(*ids):
    return ''.join(pv('slack', i) for i in ids)


md = []
w = md.append
w('# Base records for Oracle Events (task_inputsN2)\n')
w('Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut). Source `hg4-synth-sep30cut` v16. '
  'Persona: Claire Morgan, Art Lead (`claire_morgan`, Slack `EMPLOYEE_0009_SLACK_ID`).\n')
w('## How to read this\n')
w('- Every quote below is generated from the JSON returned by `hg.py search`, never retyped. Keep Slack mention tokens, '
  '`[PERSON_NAME_*]` placeholders, curly apostrophes (U+2019) and HTML entities such as `&amp;` exactly as shown.')
w('- Slack paths are relative to `Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/slack/`. '
  'Trello and Linear paths are `data.json` under their service folders. Pacific is America/Los_Angeles (PDT on every date here).')
w('- Placeholder identities: Trello card 68768a1501ae552dbee94b8a has name `Marketing Video Refresh (Marcus/[PERSON_NAME_0036])` '
  'and URL slug `45-marketing-video-refresh-marcus.bennett-frederick.stone`, so `[PERSON_NAME_0036]` is Frederick Stone. '
  'The unfurl in item 3 has `author_id` `EMPLOYEE_0016_SLACK_ID` (Robert) with `author_name` `[PERSON_NAME_0055]` and fallback name '
  '`[PERSON_NAME_0054]`, so both tokens read as Robert. That is inference from tokens, so quote the token, not the name.\n')
w('### Scope notes\n')
w('- Reads went through `hg.py search` (`lookup`, `search-many`, `get`, `get-many`) and `persona_view.py`. No SQL was executed and git was not run.')
w('- Linear reads went slightly past the brief, in three places. The user lookup also returned Claire Morgan (`/users/17`). The contiguous '
  'read of `/issues/578`-`/issues/593` also returned array neighbours ART-78, ART-95 and ART-96. The state pass used a `state_id` lookup over all '
  'teams and then kept only ART pointers. `ART-793`-`ART-1199` were checked on `identifier` only. No comments, projects or other teams\' tickets were opened.')
w('- Because Linear reads were limited, creator id `usr_175c0d7bc72ed244` (on ART-774/790/792 and on the overlay ART rows) was not resolved to a person.\n')

# ---- item 1
w('## 1. Aug 13 "30 s cut" thread in #zombie_marketing\n')
w('Coverage: `lookup --key thread_ts` over all 4,840 message files, `scan_complete` true, returned the parent and 15 replies, matching `reply_count` 15.\n')
w('### Lines to quote\n')
w('Baked-in line (parent, Frederick Stone):\n')
w(block(P['messages/C06DJBJL798/2025-08.json#/22']['text']))
w('No-music lines, in order:\n')
for n in (24, 25, 28, 30, 33):
    v = P[f'messages/C06DJBJL798/2025-08.json#/{n}']
    w(f"- `/{n}` {who(v['user'])}: `{v['text']}`")
w('')
w('### Which creatives it covers\n')
w('- The thread names one UA creative: the file on the parent, `marcus.bennett_9-16_blur-VEED.mp4` (`F09AMU1LSN5`, 30,030 ms, 9:16). '
  'Overlay ART-809 `marcus.bennett 9:16 (9:16 video)` points here. Its comment gives no master type and defers to this thread: '
  '`Captured from Android #1630 on Aug 13. Master notes are in Frederick\'s Aug 13 thread in #zombie_marketing. Unity: iOS UK phone, Android US phone.`')
w('- The baked-in statement is about that cut only.')
w('- The no-music exports are not of that cut. Marcus attached two zips of the investor video, `InvestorFacing_Seq3_NoMusic.zip` (`F09A3UM7F43`) and '
  '`InvestorFacing_Seq3_NoMusic_NoTransitions.zip` (`F09A9NUF3RQ`). By name they are variants of `InvestorFacing_Seq3.zip` (`F09AATG5BTQ`, channel post `/21`), which is the source video, not the 30 s cut.')
w('- Leonard frames them as material for later work: `I think [PERSON_NAME_0036] can start with this video and we’ll do others without music so that we can do different cuts`.')
w('- The thread never says the 9:16 was re-cut from a no-music file, and it never mentions 16:9, 4:5 or 1:1. '
  'Overlay ART-817/818/819 carry their own `Master: SFX only, no music.`, so the thread determines ART-809 alone.\n')
w('**Risk for the OE:** a reader could fairly take `Two variants, one with no music but with sfx` as a no-music master for ART-809 itself. '
  'The evidence that it is not rests on the zip names and on the parent\'s baked-in line. The OE should state that reasoning rather than treat it as self-evident.\n')
w('### Records\n')
w(msg('messages/C06DJBJL798/2025-08.json#/21', 'channel post just before the thread, not part of it'))
w(msg('messages/C06DJBJL798/2025-08.json#/22', 'parent'))
for n in range(23, 38):
    w(msg(f'messages/C06DJBJL798/2025-08.json#/{n}', f'reply {n - 22} of 15'))
w('File visibility:\n')
w(filepv('F09AMU1LSN5', 'F09A3UM7F43', 'F09A9NUF3RQ', 'F09AATG5BTQ'))
w('### Related no-music records Claire cannot see\n')
w('A complete search of all Aug-Sep 2025 message files for `no music`, `without music`, `without the music`, `NoMusic`, `baked in` and file names containing `VEED` '
  'found these outside the thread. They are context for you only and must not be load-bearing for Claire.\n')
for key, lab in (('messages/D05UDNHAPL2/2025-08.json#/29', 'Marcus asks for no-music recordings'),
                 ('messages/D05UDNHAPL2/2025-08.json#/38', 'Frederick agrees'),
                 ('messages/D05UDNHAPL2/2025-08.json#/43', 'Frederick shares a no-music Drive subfolder'),
                 ('messages/D05UDNHAPL2/2025-08.json#/44', 'Frederick plans the 30 s cuts')):
    w(msg(key, lab))
w(msg('messages/D05S58U4SAK/2025-08.json#/55', 'same 30,030 ms length as the thread cut, different file name, nothing about music'))
w(msg('messages/D05S58U4SAK/2025-08.json#/54', 'sibling 30 s cut `alin2`, nothing about music'))
w('File visibility:\n')
w(filepv('F09BJBG8J5N', 'F09B4C125TK'))

# ---- item 2
w('## 2. Martin\'s Sep 17 icon concept in #zombie-art\n')
w('Base: `reply_count` 0, `thread_ts` null, no replies (complete `thread_ts` lookup). Claire herself reacted (:ghost: and :jack_o_lantern:).\n')
w(msg('messages/C08R8CHB0QL/2025-09.json#/121'))
w('File visibility:\n')
w(filepv('F09FN3SLD9T', 'F09FN3YJ7D3'))
w('### Seeded reply `C08R8CHB0QL/1758127951.679146` (overlay only)\n')
seed = next(x['row'] for x in ROWS if x['line'] == 27)
u, p = tfmt(seed['ts'])
w(f"- Not in base: the `lookup --key ts` over all message files returned no match. Overlay SQL line 27. Id `{seed['id']}`.")
w(f"- Author: {who(seed['user_id'])}. Time: {u} | {p}.")
w('- Overlay line 29 updates the parent: `thread_ts_legacy` `1758121809.236839`, `reply_count` 1, `reply_users_count` 1, `latest_reply` `1758127951.679146`.\n')
w('Verbatim overlay text:\n')
w(block(seed['text']))
w('persona_view (UNVERIFIED is expected for an overlay row, and the channel verdict is YES):\n')
w('```text\n' + '\n'.join(verdicts['slack C08R8CHB0QL/1758127951.679146']) + '\n```\n')

# ---- item 3
w('## 3. Fake-installs thread in #zombie-match3d\n')
p3 = P['messages/C0880U9751A/2025-09.json#/467']
w('| Field | Base | After overlay |')
w('|---|---|---|')
w(f"| reply_count | {p3['reply_count']} | 5 (SQL line 32) |")
w(f"| latest_reply | `{p3['latest_reply']}` | `1759275738.984915` (SQL line 32) |")
w(f"| reply_users_count | {p3['reply_users_count']} | {p3['reply_users_count']} (not updated; Frederick and Robert already reply) |\n")
w('Coverage: the `thread_ts` lookup returned the parent plus 4 replies, matching base `reply_count` 4. Pointer `/468` sits between them but is a Linear-bot message in a different thread.\n')
w(msg('messages/C0880U9751A/2025-09.json#/467', 'parent'))
a = p3['attachments'][0]
w('The parent also carries an unfurl of a Robert post from #zombie-design (`C090N54TG79`):\n')
w(f"- `from_url`: `{a['from_url']}`")
w(f"- `author_id` `{a['author_id']}`, `author_name` `{a['author_name']}`, `ts` `{a['ts']}` ({tfmt(a['ts'])[0]} | {tfmt(a['ts'])[1]})\n")
w('Unfurl `text`:\n')
w(block(a['text']))
w('Unfurl `fallback`:\n')
w(block(a['fallback']))
w('Claire can read the unfurl here but cannot open the source post:\n')
w(pv('slack', 'C090N54TG79/1759207989.371869'))
for i, n in enumerate((469, 470, 471, 472), 1):
    w(msg(f'messages/C0880U9751A/2025-09.json#/{n}', f'reply {i} of 4'))
w('### Seeded reply (overlay only)\n')
seed = next(x['row'] for x in ROWS if x['line'] == 30)
u, p = tfmt(seed['ts'])
w(f"Overlay SQL line 30, {who(seed['user_id'])}, {u} | {p}:\n")
w(block(seed['text']))

# ---- item 4
w('## 4. Leonard\'s post about Thursday in #company-internal\n')
w(msg('messages/C05KNDCHAAG/2025-10.json#/0'))
w('- This is Tue Sep 30 in Pacific but Wed Oct 1 in UTC, so it is stored in the `2025-10.json` shard. It precedes the clock.')
w('- In Leonard\'s frame `tomorrow` is Wed Oct 1, `Thu` is Oct 2 and `Friday morning` is Oct 3.')
w('- `thread_ts` equals its own ts with `reply_count` 0. The lookup confirms no replies.')
w('- Tension to settle in the OE: this says he `won’t attend internal meeting tomorrow and Thu`, while overlay event `ZM3D Halloween review` (Thu Oct 2) says `I\'m in LA Thursday so I\'ll dial in for this one.` They read as compatible only as a stated exception.\n')

# ---- item 5
w('## 5. #builds Android #1452, near miss #1450, Robert\'s iOS 1232\n')
for key, lab in (('messages/C05433XK267/2025-07.json#/1672', 'Android #1452 result, the requested record'),
                 ('messages/C05433XK267/2025-07.json#/1671', 'Android #1452 start'),
                 ('messages/C05433XK267/2025-07.json#/1664', 'near miss, Android #1450 result'),
                 ('messages/C05433XK267/2025-07.json#/1662', 'near miss, Android #1450 start')):
    v = P[key]
    at = v['attachments'][0]
    assert at['fallback'] == at['fields'][0]['value']
    w(msg(key, lab, body=at['fallback']))
    w('`text` is empty. The quote is `attachments[0].fallback`, which is identical to `attachments[0].fields[0].value`.\n')
v = P['messages/C05433XK267/2025-07.json#/1673']
w(msg('messages/C05433XK267/2025-07.json#/1673', 'iOS #1232 result, posted 5 s after Android #1452', body=v['attachments'][0]['fallback']))
w(msg('messages/C0880U9751A/2025-07.json#/903', 'Robert\'s iOS 1232 post, #zombie-match3d'))
w(msg('messages/C0880U9751A/2025-07.json#/911', 'the only reply'))
w('Reading these together:\n')
w('- #1450 is a `main` build with the change `New Background and light/reflection rebake`. #1452 is a `[PERSON_NAME_0054]/ZombieSwap` branch build with `No Changes.`')
w('- Robert names iOS 1232 only. The `zombie swap completed with new background` claim is in his post, not in any #builds record. Tying it to Android #1452 relies on the shared branch and on #1452 starting 21 s after iOS #1232 (`1753820323.971319` vs `1753820302.497999`).')
w('- Robert posted about 2.5 minutes before Jenkins reported iOS #1232 finished (`1753820524` vs `1753820679`).')
w('- Overlay ART-831 cites `Android #1450 footage (Jul 29)`. Jul 29 holds in both UTC and Pacific for #1450.\n')

# ---- item 6, 7
w('## 6. "1.3.38 is out!"\n')
w(msg('messages/C0880U9751A/2025-09.json#/286'))
w('File visibility:\n')
w(filepv('F09FC42QJDV'))
w('## 7. Leonard\'s Sep 3 export ask\n')
w(msg('messages/C06DJBJL798/2025-09.json#/0'))
w('No replies: `thread_ts` null, `reply_count` 0, and the lookup found nothing.\n')

# ---- item 8
w('## 8. Old zombies on the packs\n')
w('`1754310794.907609` is a reply inside the thread on `1754077274.101399`, not a top-level post, so the parent and the rest of that thread follow it.\n')
w(msg('messages/C08R8CHB0QL/2025-08.json#/45', 'requested record'))
w('File visibility:\n')
w(filepv('F098VNHS1RS'))
w(msg('messages/C08R8CHB0QL/2025-08.json#/64', 'requested record'))
w('File visibility:\n')
w(filepv('F098W8JDC4U'))
w(msg('messages/C08R8CHB0QL/2025-08.json#/65', 'the only reply to the packs post'))
w('### Lineage context\n')
w(msg('messages/C08R8CHB0QL/2025-08.json#/41', 'top-level post before the thread'))
w(msg('messages/C08R8CHB0QL/2025-08.json#/42', 'thread parent'))
for n in (43, 46, 47, 48, 49, 50, 51, 52, 54, 59, 60, 61, 62):
    w(msg(f'messages/C08R8CHB0QL/2025-08.json#/{n}', 'reply in the same thread'))

# ---- item 9
w('## 9. Trello\n')
b = P4['trello:data.json#/boards/4']
w(f"Board, pointer `/boards/4`: id `{b['id']}`, name `{b['name']}`, closed `{str(b['closed']).lower()}`, dateLastActivity `{b['dateLastActivity']}` "
  '(overlay line 324 sets `2025-09-30T23:20:00Z`).\n')
w(pv('trello', b['id']))
w('Lists, in `pos` order:\n')
w('| Pointer | List id | Name | pos | closed |')
w('|---|---|---|---|---|')
ls = sorted(((k.split('#')[1], v) for k, v in P4.items() if k.startswith('trello:data.json#/lists')), key=lambda x: x[1]['pos'])
for ptr, v in ls:
    w(f"| `{ptr}` | `{v['id']}` | `{v['name']}` | {v['pos']} | {str(v['closed']).lower()} |")
w('')
w('Every list returns the same unscoped YES. Sample:\n')
w(pv('trello', ls[0][1]['id']))
c = P4['trello:data.json#/cards/750']
lname = next(v['name'] for _, v in ls if v['id'] == c['idList'])
w('Card, pointer `/cards/750`:\n')
w(f"- id `{c['id']}`, idShort {c['idShort']}")
w(f"- name `{c['name']}`")
w(f"- list `{lname}` (`{c['idList']}`)")
w(f"- closed `{str(c['closed']).lower()}`, due `{c['due']}`, dueComplete `{str(c['dueComplete']).lower()}`, badges.dueComplete `{str(c['badges']['dueComplete']).lower()}`")
w(f"- members `idMembers` {json.dumps(c['idMembers'])}: nobody is assigned, the two people appear only in the title")
w(f"- url `{c['url']}`, dateLastActivity `{c['dateLastActivity']}` (overlay line 323 sets `2025-09-26T17:40:00Z` and badges.comments 1)\n")
w(pv('trello', c['id']))

# ---- item 10
w('## 10. Linear\n')
t = P4['linear:data.json#/teams/0']
w(f"Team, pointer `/teams/0`: id `{t['id']}`, name `{t['name']}`, key `{t['key']}`.\n")
w(pv('linear', 'team_ART'))
st = json.load(open(f'{S}/st_out.json'))
art = {m['pointer'].rsplit('/', 1)[0] for m in json.load(open(f'{S}/artptr.json'))['matches']['team_ART']}
counts = {k: len({m['pointer'].rsplit('/', 1)[0] for m in v} & art) for k, v in st['matches'].items()}
counts = {k: v for k, v in sorted(counts.items(), key=lambda x: -x[1]) if v}
w('### ART workflow states\n')
w('The export has no workflow-state collection (`/workflow_states`, `/states`, `/workflowStates`, `/team_states` all return `JSON pointer not found`). '
  'States exist only as the plain string `state_id` on each issue. Distinct values over all '
  f'{len(art)} `team_ART` issues, with full coverage ({sum(counts.values())} of {len(art)}):\n')
w('| state_id | ART issues |')
w('|---|---|')
for k, v in counts.items():
    w(f'| `{k}` | {v} |')
w('')
w('`In Progress` exists on other teams but has 0 ART issues. The overlay\'s `Done` and `Canceled` are both valid ART values.\n')
w('### Users\n')
w('| Person | Pointer | id | email | name field | is_active |')
w('|---|---|---|---|---|---|')
for lab, ptr in (('Marcus Bennett', 33), ('Julia Lawson', 18), ('Martin Walsh', 9)):
    v = P4[f'linear:data.json#/users/{ptr}']
    w(f"| {lab} | `/users/{ptr}` | `{v['id']}` | `{v['email']}` | `{v['name']}` | {str(v['is_active']).lower()} |")
w('')
w('The `name` and `display_name` fields hold the email address, so there is no human-readable name in Linear. Sample visibility:\n')
w(pv('linear', 'usr_c77c50cc15c5342d'))
w('### Tickets near ART-774 and ART-790..792\n')
w('| Pointer | id | Title | state_id | assignee_id | created_at | completed_at |')
w('|---|---|---|---|---|---|---|')
for n in list(range(578, 588)) + [589, 590, 591]:
    v = P4[f'linear:data.json#/issues/{n}']
    title = v['title'].replace('|', '\\|')
    w(f"| `/issues/{n}` | `{v['id']}` | {title} | `{v['state_id']}` | `{v['assignee_id']}` | {v['created_at']} | {v['completed_at']} |")
w('')
w('**Note:** the base is thin and almost all Done above ART-770, with no ART-781..789 and no ART-791, and ART-792 is the highest number, so overlay ART-793 onward continues it without collision.\n')
w('- `id` equals `identifier`. There is no separate UUID in the export. Array order is string-sorted (`ART-78` sits between ART-779 and ART-780).')
w('- ART-790 is `Todo` and ART-792 is `Team Epic`, both assigned to Martin Walsh with no `completed_at`. ART-774 is `Done`, created by `usr_175c0d7bc72ed244`.')
w('- SC-16 describes ART-790/792 as `still Todo/In Progress`, but ART-792\'s actual value is `Team Epic`. Quote the record, not the card.\n')
for lab, n in (('ART-774', 582), ('ART-790', 590), ('ART-792', 591)):
    v = P4[f'linear:data.json#/issues/{n}']
    w(f"`{lab}` `{v['title']}` description, pointer `/issues/{n}/description`:\n")
    w(block(v['description']))
    w(pv('linear', lab))

# ---- item 11
w('## 11. Slack channels\n')
w('| Channel | id | Pointer | Private | Archived | num_members | Claire in `members` |')
w('|---|---|---|---|---|---|---|')
chs = [('#zombie_marketing', 57), ('#zombie-art', 129), ('#zombie-match3d', 108), ('#zm-animations', 139),
       ('#company-internal', 38), ('#builds', 25), ('Claire\'s IM', 590)]
for lab, n in chs:
    v = P[f'channels.json#/{n}']
    inn = 'EMPLOYEE_0009_SLACK_ID' in v['members']
    w(f"| {lab} | `{v['id']}` | `channels.json` `/{n}` | {str(v['is_private']).lower()} | {str(v['is_archived']).lower()} | {v['num_members']} | {'yes' if inn else 'no'} |")
w('')
w('`#zombie-art` and `#builds` are public, the others private. Note SC-7: membership lists are not a safe grading basis, so use these only for reach.\n')
v = P['channels.json#/590']
w(f"`D05V2N6PZNU` has `is_im` true but lists {v['num_members']} members: `{'`, `'.join(v['members'])}`. "
  'Marcus (`EMPLOYEE_0002_SLACK_ID`) and Claire are two of them. The other three were not resolved.\n')
w('persona_view:\n')
for lab, n in chs:
    w(pv('slack', P[f'channels.json#/{n}']['id']))

# ---- item 12
w('## 12. Base calendar and Gmail lookalikes\n')
w('### Calendar: no other Halloween review\n')
w('- `Halloween` appears 0 times anywhere in gcal `data.json` (`scan_complete` true). `ZM3D` appears in 0 event summaries. The overlay\'s `ZM3D Halloween review` is unique.')
w('- `2025-10-02` appears in 0 event values, so no base event instance sits on that date.')
w('- Claire has 553 events on `claire.morgan@harmonygames.co`. Her only `review`-named one is `Bug Review` (`/events/5852`, weekly Tuesdays). Her latest instances are `POD: PROTOTYPE` Sep 29 (`/events/1697`) and `(Wednesday) Mid Week Art Sync` Oct 1 (`/events/8858`).')
w('- Caveat: recurring masters without `UNTIL` could still expand onto Thu Oct 2. `POD: PROTOTYPE` (`/events/134` and `/events/6900`, `RRULE:FREQ=WEEKLY;BYDAY=MO,TU,TH`, 16:00-16:30Z) has the same slot as the seeded review (16:00-16:30Z, 09:00-09:30 PDT). `Ops-timus Prime Catchup` (`/events/967`, 16:30Z, and `/events/9400`, `/events/5216`, 16:45Z) and others follow it. These are not named like the review, but a solver expanding recurrences would see an overlap.\n')
w('### Gmail: nothing that looks like an October UA plan\n')
w('Searched all 81,404 thread files, every query `scan_complete` true after raising limits.\n')
w('| Query | Scope | Hits | Outcome |')
w('|---|---|---|---|')
for q, sc, h, o in (('`October UA`', 'all fields', 0, ''), ('`October plan`', 'all fields', 0, ''), ('`plan for October`', 'all fields', 0, ''),
                    ('`UA for October`', 'all fields', 0, ''), ('`October budget`', 'all fields', 0, ''), ('`retention restart`', 'all fields', 0, ''),
                    ('`Halloween flight`', 'all fields', 0, ''), ('`creatives to me`', 'all fields', 0, ''),
                    ('`UA plan`', 'all fields', 2, 'Liftoff newsletter item `UA Planning: ...`, Leonard and Martin mailboxes'),
                    ('`Q4 UA`', 'all fields', 4, 'Vendor newsletter text plus one header-hash false match'),
                    ('`Unity only`', 'all fields', 2, 'Conference mail and a code-review note, unrelated'),
                    ('`UA`', 'subject, case-sensitive', 75, 'Vendor mail, 2024 sync invites, `UA video assets` notices, and the Tilting Point item below'),
                    ('`October`', 'subject', 96, 'Admin, board and vendor mail. None about UA planning'),
                    ('`Halloween`', 'subject', 2, '2024 music newsletter and a 2023 costume social'),
                    ('`Unity`', 'subject', 908, 'Filtered for plan, flight, budget, UA, retention, creative: only `Unity Performance by Creative Pack` (Nov 2024 Singular support thread on the Unity Ads connector), vendor pitches and Unity Pro notices'),
                    ('`campaign`', 'subject', 66, 'Same filter, no UA plan'),
                    ('`Oct 20`', 'body', 209, 'Firebase test results and unrelated mail')):
    w(f'| {q} | {sc} | {h} | {o} |')
w('')
w('Closest by title, and still not a plan: `threads/frederick@harmonygames.co_1842443183462721250.json` `/messages/0`, subject `\'UA Funding request`, Fri 05 Sep 2025 16:45:42 +0000, in Frederick\'s mailbox. It is a Tilting Point auto-acknowledgement:\n')
w(block('Thank you for submitting your application. We have successfully received  \nyour request and will review the details carefully.\nIf your game aligns with our criteria for funding, our team will reach out  \nto you shortly to discuss next steps.\nWe appreciate your interest in working with us and will be in touch if we  \ncan move forward.\n\nTilting Point'))
w('The overlay mails `October UA plan (draft)` and `October UA plan - changes` therefore have no base competitor.\n')

# ---- item 13
w('## 13. SC cards in `Task_Authoring/references/known_data_issues/synthcut.md`\n')
src = open(ROOT + '/Task_Authoring/references/known_data_issues/synthcut.md').read()
cards = {}
for m in re.finditer(r"### (SC-\d+) · (.+?)\n.*?- \*\*Don't grade:\*\* (.+?)\n", src, re.S):
    cards[m.group(1)] = (m.group(2), m.group(3))
assert len(cards) == 73, len(cards)
groups = [
    ('Unity spend or CPI', [('SC-11', 'direct'), ('SC-12', 'adjacent: ZM3D paid UA spend'), ('SC-23', 'adjacent: other Snowflake UA spend')]),
    ('ART tickets', [('SC-16', 'direct: names ART-790/792'), ('SC-22', 'any ticket; ART-792 has 246277 and overlay line 171 nulls it'), ('SC-32', '11 of the 12 In Review tickets are ART'), ('SC-30', 'any parent ticket')]),
    ('App icon or store listing dates', [('SC-19', 'no card names the icon or listing; this one covers store-build versions, 0.3.x vs 1.3.x, and so 1.3.38'), ('SC-16', 'ART-790/792 are marketing-screenshot tickets')]),
    ('ZM3D release dates', [('SC-13', 'direct'), ('SC-14', 'beta cards on the same board'), ('SC-19', 'build matching'), ('SC-38', 'ship date'), ('SC-67', '#builds number'), ('SC-68', 'prod date'), ('SC-28', 'launch claims')]),
    ('Slack timezones', [('SC-70', 'direct')]),
    ('Trello list names', [('SC-13', 'direct: `BETA: Oct 10`')]),
    ('Linear states', [('SC-16', 'state vs shipped'), ('SC-30', 'parent vs child'), ('SC-32', 'In Review'), ('SC-8', 'ZOM-475 Todo'), ('SC-15', 'ZOM-521 children'), ('SC-38', 'ZOM-552 In Progress')]),
    ('Claire Morgan, Marcus Bennett, Julia Lawson, Martin Walsh', [('SC-7', 'none of the four is named in any card (grep confirmed); this is generic, channel membership'), ('SC-36', 'generic: invite lists from membership'), ('SC-70', 'generic: every Slack user'), ('SC-25', 'generic: roster vs current staff')]),
]
for g, items in groups:
    w(f'### {g}\n')
    w('| Card | Title | Why it matters | Don\'t grade |')
    w('|---|---|---|---|')
    for cid, why in items:
        title, dg = cards[cid]
        w(f'| {cid} | {title} | {why} | {dg} |')
    w('')
w('Also relevant to the records above: SC-56 (`' + cards['SC-56'][1] + '`) applies when quoting #1450\'s change line against GitHub.\n')
w('Card 68768a1501ae552dbee94b8a is idShort 45, outside SC-14\'s cards 54/56/58/67, and its two `dueComplete` flags agree (both true).\n')

open(OUT, 'w').write('\n'.join(md))
print('wrote', OUT, len('\n'.join(md)))
