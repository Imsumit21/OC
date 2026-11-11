#!/usr/bin/env python3
"""Read the base records the Oracle Events quote through tools/hg.py and write base_quotes.json."""
import json, os, subprocess
HERE = os.path.dirname(os.path.abspath(__file__))
WS = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
PY = os.path.expanduser('~/.local/bin/python3.12')
def get(svc, f, ptr):
    p = subprocess.run([PY, '-B', 'Task_Authoring/tools/hg.py', 'search', 'get', svc, '--file', f, '--pointer', ptr], cwd=WS, capture_output=True, text=True,
                       env={**os.environ, 'TASK_AUTHORING_TASK_DIR': 'Task_Authoring/task_inputsN2'})
    return json.loads(json.loads(p.stdout)['text'])
parent = get('slack', 'messages/C06DJBJL798/2025-08.json', '/22')
var = get('slack', 'messages/C06DJBJL798/2025-08.json', '/33')
icon = get('slack', 'messages/C08R8CHB0QL/2025-09.json', '/121')
fp = get('slack', 'messages/C0880U9751A/2025-09.json', '/467')
assert parent['ts'] == '1755114007.441789' and var['thread_ts'] == parent['ts'] and icon['ts'] == '1758121809.236839' and fp['ts'] == '1759211437.306779'
pf = parent['files'][0]['name']; vf = [x['name'] for x in var['files']]
print(pf, vf)
music_text = ' '.join([parent['text'], var['text'], pf] + vf)
users = {k: get('linear', 'data.json', p) for k, p in (('marcus', '/users/33'), ('julia', '/users/18'), ('martin', '/users/9'), ('lee', '/users/28'))}
team = get('linear', 'data.json', '/teams/0')
utext = ' '.join(f"{u['email']} {u['id']}" for u in users.values()) + f" {team['name']} {team['key']} {team['id']}"
print(utext)
jl = get('slack', 'users.json', '/3')
assert jl['id'] == 'EMPLOYEE_0005_SLACK_ID', jl
print(jl['name'], jl['email'])
B = {
 'who': {'text': f"{jl['name']} {jl['email']}", 'ledger': f"{jl['id']}: name '{jl['name']}', email {jl['email']}", 'pointer': 'slack users.json /3'},
 'music': {
  'text': music_text,
  'expected': f'Frederick Stone, Wed Aug 13 2025 12:40 PM PT, posting {pf}: "Here\'s a 30 second cut for UA. I can\'t really cut and paste different video segments as the background music is baked in." Marcus Bennett\'s reply: "Two variants, one with no music but with sfx, and another one with no music but with sfx and no video transitions (just cuts between the scenes)", with files {vf[0]} and {vf[1]}. Those files are no-music exports of the investor video. ART-809\'s master is the music-baked cut Frederick posted, so under the deck in {{deck}} it is re-cut first from a master without music: Refresh first.',
  'locator': 'C06DJBJL798/1755114007.441789',
  'ledger': f"Posted Wed Aug 13 2025 12:40 PM PT (2025-08-13T19:40Z) by EMPLOYEE_0008_SLACK_ID with file {pf}. Quote: '{parent['text']}' Reply C06DJBJL798/1755118817.302199 by EMPLOYEE_0002_SLACK_ID: '{var['text']}' Files: {', '.join(vf)}",
  'pointer': 'slack messages/C06DJBJL798/2025-08.json /22 and /33'},
 'icon': {
  'text': icon['text'] + ' ' + ' '.join(x['name'] for x in icon['files']),
  'expected': 'Martin Walsh, Wed Sep 17 2025 8:10 AM PT, with file AppIconHalloween.png: "*Halloween theme* for an app icon or an event". Robert\'s reply, 9:52 AM PT: "Nice for an event, but not for the app icon, it gets too busy at that size. A Halloween icon should stay as simple as the one we have". So the concept is not the icon, and the app icon needs a new Halloween version.',
  'ledger': f"Posted Wed Sep 17 2025 8:10 AM PT (2025-09-17T15:10Z) by EMPLOYEE_0033_SLACK_ID. Quote: '{icon['text']}' Files: {', '.join(x['name'] for x in icon['files'])}",
  'pointer': 'slack messages/C08R8CHB0QL/2025-09.json /121'},
 'users': {
  'text': utext,
  'expected': 'marcus.bennett@harmonygames.co (usr_c77c50cc15c5342d), julia.lawson@harmonygames.co (usr_8140f09bf9f1b94c) and martin.walsh@harmonygames.co (usr_51f5f16d46e8cf55); team Art, key ART, id team_ART. marcus.lee@harmonygames.co is a different person.',
  'locator': 'users marcus.bennett, julia.lawson, martin.walsh; team Art',
  'ledger': utext,
  'pointer': 'linear data.json /users/33, /users/18, /users/9, /users/28, /teams/0'},
 'parent': {'summary': f"'{fp['text']}' by {fp['user']}", 'text': fp['text']},
}
json.dump(B, open(os.path.join(HERE, 'base_quotes.json'), 'w'), indent=1)
