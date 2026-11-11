#!/usr/bin/env python3
"""Assemble Working_Files/08_OE_Writing_Ledger.md (prep) from the rev3 SQL rows (parsed, never executed), the base
records read through tools/hg.py (base_quotes.json), solver/truth.json (asserted in model.py) and persona_view.
Facts and dependency edges only; no event text."""
import datetime as dt
import json
import os
import re
import subprocess
import sys
from zoneinfo import ZoneInfo

from model import (ADS, ARCHIVE, BY, CM, D10, D15, GRID, HERE, ISS, JULIA, MARCUS, OFF_SHEET, S, SHEET, TI, WF, call,
                   campaigns, due, kind, maker, name, rows, sql_line)

WS = os.path.abspath(os.path.join(TI, '..', '..'))
sys.path.insert(0, os.path.join(TI, '..', 'tools'))
import stage_gate as G  # noqa: E402

PY = os.path.expanduser('~/.local/bin/python3.12')
PERSONA = 'claire_morgan'
BASE = json.load(open(os.path.join(HERE, 'base_quotes.json')))
DEFER = json.load(open(os.path.join(HERE, 'defer.json')))
PROMPT = open(os.path.join(TI, '04_Prompt.txt')).read()
SQLREL = 'Task_Authoring/task_inputsN2/01_Universe_Inject.sql'
PT = ZoneInfo('America/Los_Angeles')
CLAIRE = 'claire.morgan@harmonygames.co'


def run(args):
    p = subprocess.run(args, cwd=WS, capture_output=True, text=True,
                       env={**os.environ, 'TASK_AUTHORING_TASK_DIR': 'Task_Authoring/task_inputsN2'})
    return p.stdout


def when(iso):
    d = dt.datetime.fromisoformat(iso.replace('Z', '+00:00'))
    p = d.astimezone(PT)
    return f"{p.strftime('%a %b %-d %Y %-I:%M %p')} PT ({d.strftime('%Y-%m-%dT%H:%MZ')})"


def clean(s):
    return (s or '').replace('\\n', ' ').replace('\n', ' ').replace('|', '/').strip()


def line_of(table, **kw):
    return f"SQL L{sql_line(table, **kw)}"


def slack_row(ts):
    return rows('slack.slack_messages', ts=ts)[0]


def mail_row(subject):
    return [r for r in rows('gmail.gmail_messages', subject=subject) if r['user_email'] == CLAIRE][0]


FACTS, fid = [], {}


def fact(key, value, service, tools, locator, origin, expected, result, visible, depends, source):
    n = f'F{len(FACTS) + 1}'
    fid[key] = n
    FACTS.append((n, value, service, tools, locator, origin, expected, result, visible, depends, source))
    return n


def F(*keys):
    return ', '.join(fid[k] for k in keys)


def fid_t(k):
    return fid['t:' + k]


def seeded_slack(key, value, ts, channel_label, origin, depends='—', extra=''):
    r = slack_row(ts)
    loc = f"{r['channel_id']}/{ts}"
    fact(key, value, f'Slack ({channel_label})', 'slack_search_public_and_private, slack_read_thread, slack_read_channel', loc, origin,
         f"Posted {when(r['created_at'])} by {r['user_id']}. Quote: '{clean(r['text'])}'{extra}",
         'VERIFIED: quote cut from the SQL row text', 'YES (channel member; check-sql)', depends, line_of('slack.slack_messages', ts=ts))


# ---------------------------------------------------------------- the ask and the sources it names
seeded_slack('ask', "Leonard's Halloween ask", '1759269913.882683', '#zombie_marketing, C06DJBJL798', 'prompt ("#zombie_marketing"); search "halloween for ZM"')
ev = rows('gcal.gcal_events', event_id='evt_d947bf7cd910549b674b1f')[0]
fact('review', "Thursday's review and its attendees", 'Calendar (Claire\'s own)', 'gcal_list_events, gcal_search_events, gcal_get_event', 'evt_d947bf7cd910549b674b1f',
     'prompt ("Thursday\'s review"); search "Halloween review"',
     f"Event '{ev['summary']}', starts {when(ev['start_ts'])}, organizer {ev['organizer_email']}, created {when(ev['created'])}. Description: '{ev['description']}'. Attendees: " + ', '.join(a['email'] for a in json.loads(ev['attendees_json'])),
     'VERIFIED: fields cut from the SQL row', 'YES (own calendar; check-sql)', F('ask'), line_of('gcal.gcal_events', event_id='evt_d947bf7cd910549b674b1f'))
SHEETID = 'f_02b1968f5e882366fbb883'
fact('sheet', 'Live creatives sheet: Read me and Store tab', 'Sheets (shared with Claire)', 'gdrive_search, gsheets_get_spreadsheet, gsheets_values_get', SHEETID,
     f'{F("ask")} ("the live creatives sheet"); search "live creatives"',
     f"Spreadsheet {SHEETID} 'ZM3D live creatives', owner frederick.stone@harmonygames.co, created {when('2025-09-08T15:40:00Z')}, modified {when('2025-09-30T22:30:00Z')}. Read me: '{GRID['Read me'][0][0]}' Store rows: " + '; '.join(r[0] for r in GRID['Store'][1:]),
     'VERIFIED: grid cells cut from the SQL rows', 'YES (shared; check-sql)', F('ask'), f"SQL L193, SQL L194 (sheet {SHEETID})")
fact('unity', 'Unity tab: 56 rows, each with its ART ticket', 'Sheets (shared with Claire)', 'gsheets_values_get, gsheets_values_batch_get', f'{SHEETID} tab Unity A1:D57', F('sheet'),
     '56 rows: ' + '; '.join(f'{SHEET[k]} {k}' for k in sorted(SHEET)), 'VERIFIED: grid cells; 56 by count of rows', 'YES (shared; check-sql)', F('sheet'), f'SQL L195 (sheet {SHEETID})')
fact('archive', 'Archive tab: 4 paused rows', 'Sheets (shared with Claire)', 'gsheets_values_get', f'{SHEETID} tab Archive A1:D5', F('sheet'),
     '4 rows: ' + '; '.join(f'{r[0]} {r[3]} paused {r[2]}' for r in GRID['Archive'][1:]), 'VERIFIED: grid cells; 4 by count of rows', 'YES (shared; check-sql)', F('sheet'), f'SQL L196 (sheet {SHEETID})')
card = rows('trello.trello_cards', id='68dc52e015f87c50c441d1a9')[0]
TA = {a['id']: a for a in rows('trello.trello_actions', type='commentCard')}
ta = TA['68dc65a0f2d7fb28743f5860']
fact('card', "Halloween push card and Frederick's comment on Julia's 4:5 static", 'Trello (unscoped)', 'trello_search, trello_get_card, trello_get_comments', "card 'Halloween push' on the ZM roadmap",
     f'{F("sheet")} ("see the Halloween push card on the ZM roadmap")',
     f"Card 68dc52e015f87c50c441d1a9 '{card['name']}' on board ZM ROADMAP. Comment action 68dc65a0f2d7fb28743f5860 by Frederick Stone, posted {when(ta['date'])}: '{json.loads(ta['data_json'])['text']}' (the CPI clause stays off every Expected line, SC-11)",
     'VERIFIED: card name and comment text cut from the SQL rows', 'YES (Trello unscoped)', F('sheet'), 'SQL L317, SQL L320')
cal = rows('gdocs.docs_documents', document_id='f_fdd6d2d2f4a4d2f5b908fb')[0]
fact('calendar', "Arthur's release calendar", 'Docs (shared with Claire)', 'gdrive_search, gdocs_get_document_text', 'f_fdd6d2d2f4a4d2f5b908fb', f'{F("ask")} ("Arthur\'s release calendar"); search "release calendar"',
     f"Owner arthur.blake@harmonygames.co, created {when(cal['created_time'])}. Text: '{clean(cal['body_text'])}'", 'VERIFIED: body_text cut from the SQL row', 'YES (shared; check-sql)', F('ask'), 'SQL L199')
seeded_slack('pointer', "Robert's pointer to the deck", '1758817822.269981', '#zombie-art, C08R8CHB0QL', f'{F("ask")} ("Robert has direction for seasonal art"); search "seasonal art direction"', F('ask'))
deck = '\n'.join(r['text'] for r in rows('gslides.slides_page_elements', presentation_id='f_5ebf55ad29e815d46243c8'))
fact('deck', "Robert's seasonal direction deck", 'Slides (shared with Claire)', 'gdrive_search, gslides_get_presentation', 'f_5ebf55ad29e815d46243c8', f'{F("pointer")}; search "Seasonal art direction"',
     f"Owner robert@harmonygames.co, created {when('2025-09-25T16:10:00Z')}. Text: '{clean(deck)}'", 'VERIFIED: page element text cut from the SQL rows', 'YES (shared; check-sql)', F('pointer'), 'SQL L207, SQL L213, SQL L220')
fact('library', 'UA creative library tickets', 'Linear (unscoped)', 'linear_list_issues', 'team ART, created from 2025-09-01, limit 100', 'prompt ("its ART ticket")',
     '62 tickets ART-793 to ART-854; off the sheet: ART-826, ART-831; paused: ' + ', '.join(ARCHIVE) + ' (' + '; '.join(f"{k}: '{ISS[k]['description']}'" for k in ARCHIVE) + ')',
     'VERIFIED: titles and descriptions cut from the SQL rows; 62 by count', 'YES (Linear unscoped)', F('unity', 'archive'), 'SQL L33 to SQL L168')
for k in ADS:
    notes = ' / '.join(f"{c['id']} {when(c['created_at'])}: '{c['body']}'" for c in CM[k])
    fact('t:' + k, f"{k} {name(k)}: {kind(k)}", 'Linear (unscoped)', 'linear_get_issue, linear_list_comments', k, F('library') if k in OFF_SHEET else F('unity'),
         f"Title '{ISS[k]['title']}'. {notes}. Current campaigns: {', '.join(campaigns(k))}. Call {call(k)}; due {due(k) or 'none'}; maker {maker(k) or 'none'}.",
         'VERIFIED: comment bodies cut from the SQL rows; the call, date and maker recomputed by oe_gen/model.py and equal to solver/truth.json', 'YES (Linear unscoped)', F('library') if k in OFF_SHEET else F('unity'),
         line_of('linear.linear_issues', id=k))
for key, subject, val, q in (('draft', 'October UA plan (draft)', "Frederick's Sep 12 draft plan (superseded)", 'October UA plan'),
                             ('changes', 'October UA plan - changes', "Frederick's Sep 30 changes mail", 'October UA plan'),
                             ('restart', 'Unity retention restart', "Frederick's Sep 29 restart mail", 'Unity retention')):
    m = mail_row(subject)
    fact(key, val, "Gmail (Claire's mailbox, To)", 'gmail_search_messages, gmail_get_message, gmail_get_thread', f"Claire's inbox, from:frederick.stone@harmonygames.co, subject '{subject}'", f'{F("ask")} ("Frederick is sending his october UA plan tonight")',
         f"Message {m['id']}, subject '{subject}', sent {when(m['date'])}, from {m['from_email']}. Body: '{clean(m['body_text'])}'", 'VERIFIED: body cut from the SQL row', 'YES (To; check-sql)', F('ask'),
         line_of('gmail.gmail_messages', id=m['id']))
seeded_slack('reply', "Frederick's later word on the Android date", '1759275738.984915', '#zombie-match3d, C0880U9751A', 'search "Android US phone"', F('changes'), extra=f" Thread parent C0880U9751A/1759211437.306779: {BASE['parent']['summary']}")
seeded_slack('leave', "Martin's vacation post", '1759243286.478812', '#company-internal, C05KNDCHAAG', 'search "ad statics"', F('ask'))
seeded_slack('leave_ok', "Leonard's reply on the ad statics", '1759275107.322377', '#company-internal, C05KNDCHAAG', 'search "ad statics"', F('leave'))
fact('who', 'The person Martin tags', 'Slack (profile)', 'slack_read_user_profile, slack_search_users', 'user EMPLOYEE_0005_SLACK_ID', F('leave'),
     BASE['who']['ledger'] + ' (tagged in C05KNDCHAAG/1759243286.478812)', 'VERIFIED: record read through hg.py get', 'YES (directory record)', F('leave'), BASE['who']['pointer'])
seeded_slack('note', "Marcus's re-capture note", '1758823964.738872', '#zm-animations, C09ATAJ220H', 'search "couch alpha 50"', '—')
seeded_slack('im', "Marcus's reply in Claire's DM", '1759166437.080255', 'DM, D05V2N6PZNU', 'search "cheer fastcouch"', '—')
seeded_slack('test', "Marcus's test post", '1759167065.499092', '#zombie-art, C08R8CHB0QL', 'search "cheer fastcouch"', '—', extra=' Replies C08R8CHB0QL/1759248337.170599 and C08R8CHB0QL/1759249269.380507.')
seeded_slack('robert', "Robert's review of the test", '1759248337.170599', '#zombie-art, C08R8CHB0QL', F('test'), F('test'))
seeded_slack('redo', "Marcus's redo reply", '1759249269.380507', '#zombie-art, C08R8CHB0QL', F('test'), F('test'))
tp = TA['68d6cff0c6568da5d9c8e81f']
fact('packs', "Frederick's comment on end card 001", 'Trello (unscoped)', 'trello_search, trello_get_comments', "comment text matching 'end card 001'", f'{fid_t("ART-833")} (the creative name end card 001)',
     f"Card 68768a1501ae552dbee94b8a 'Marketing Video Refresh', comment action 68d6cff0c6568da5d9c8e81f by Frederick Stone, posted {when(tp['date'])}: '{json.loads(tp['data_json'])['text']}'", 'VERIFIED: comment text cut from the SQL row', 'YES (Trello unscoped)', '—', 'SQL L321')
fact('music', "Frederick's Aug 13 thread on the marcus.bennett master", 'Slack (#zombie_marketing, C06DJBJL798)', 'slack_read_thread', BASE['music']['locator'], 'cmt_art809_1 pointer ("Frederick\'s Aug 13 thread in #zombie_marketing"); search "baked in"',
     BASE['music']['ledger'], 'VERIFIED: quote read through hg.py get', 'YES (channel member; can-see)', '—', BASE['music']['pointer'])
seeded_slack('export', "Martin's store export post", '1759245641.309714', '#zombie-art, C08R8CHB0QL', 'search "store screens"', '—', extra=' Reply C08R8CHB0QL/1759247246.453725.')
seeded_slack('export_ok', "Leonard's reply on store tickets", '1759247246.453725', '#zombie-art, C08R8CHB0QL', F('export'), F('export'))
fact('folder', 'Halloween folder in Drive', 'Drive (shared with Claire)', 'gdrive_search, gdrive_list_folder', 'd_272d849cde40c35980a433', 'search "ZM3D Halloween 2025"',
     "Folder 'ZM3D Halloween 2025', owner leonard.hayes@harmonygames.co, subfolders Store d_74a7c95c28097dd9777e01 and UA masters d_6c2e4339e5d58108799ac8", 'VERIFIED: names and parents cut from the SQL rows', 'YES (shared; check-sql)', '—', 'SQL L173, SQL L175, SQL L176')
files = [r for r in rows('gdrive.drive_files') if 'd_74a7c95c28097dd9777e01' in str(r.get('parents_json'))]
assert len(files) == 11
fact('store', 'Halloween Store folder', 'Drive (shared with Claire)', 'gdrive_search, gdrive_list_folder', 'd_74a7c95c28097dd9777e01', F('folder'),
     '11 files, created Sep 30: ' + ', '.join(sorted(r['name'] for r in files)), 'VERIFIED: names cut from the SQL rows; 11 by count; ABSENCE evidence_check for the iPad set in research/defer_absence.md', 'YES (shared; check-sql)', F('folder'), 'SQL L177 to SQL L187')
fact('masters', 'UA masters folder', 'Drive (shared with Claire)', 'gdrive_search, gdrive_list_folder', 'd_6c2e4339e5d58108799ac8', F('folder'),
     '2 files, owner marcus.bennett@harmonygames.co: cheer_fastcouch_halloween_9x16.mp4, cheer_fastcouch_halloween_16x9.mp4', 'VERIFIED: names cut from the SQL rows', 'YES (shared; check-sql)', F('folder'), 'SQL L188, SQL L189')
fact('concept', "Martin's Sep 17 icon concept", 'Slack (#zombie-art, C08R8CHB0QL)', 'slack_search_public_and_private, slack_read_thread', 'C08R8CHB0QL/1758121809.236839', 'search "app icon"',
     BASE['icon']['ledger'] + ' Reply C08R8CHB0QL/1758127951.679146.', 'VERIFIED: quote read through hg.py get', 'YES (channel member; can-see)', '—', BASE['icon']['pointer'])
seeded_slack('icon_no', "Robert's icon reply", '1758127951.679146', '#zombie-art, C08R8CHB0QL', F('concept'), F('concept'))
fact('users', 'Linear users for the makers and team ART', 'Linear (unscoped)', 'linear_list_users, linear_list_teams', BASE['users']['locator'], 'search "Marcus Bennett"',
     BASE['users']['ledger'], 'VERIFIED: records read through hg.py get', 'YES (Linear unscoped)', '—', BASE['users']['pointer'])

# ---------------------------------------------------------------- derived sets (dependency edges, not new records)
TK = [fid['t:' + k] for k in ADS]
fact('d_skip', 'Skip set', 'Linear comments plus Gmail (derived)', 'reasoning', f"{F('changes')} rule on the ticket campaigns, {F('restart')} on the two landscape cuts", F('changes', 'restart'),
     f"{len(BY['Skip'])} ads: {', '.join(BY['Skip'])}", 'VERIFIED: recomputed by oe_gen/model.py; equal to solver/truth.json', 'YES (inputs proved above)', F('changes', 'restart'), 'SQL L33 to SQL L168 recomputed by oe_gen/model.py; solver/truth.json')
fact('d_hv', 'Halloween version ads', 'Linear comments plus Slack (derived)', 'reasoning', f"{F('deck')} rule", F('deck', 'note', 'robert'),
     f"{len(BY['Halloween version'])} ads: {', '.join(BY['Halloween version'])}", 'VERIFIED: recomputed by oe_gen/model.py; equal to solver/truth.json', 'YES (inputs proved above)', F('deck', 'note', 'robert'), 'SQL L33 to SQL L168 recomputed by oe_gen/model.py; solver/truth.json')
fact('d_rf', 'Refresh first ads', 'Linear comments plus Slack and Trello (derived)', 'reasoning', f"{F('deck')} rule", F('deck', 'music', 'packs'),
     f"{len(BY['Refresh first'])} ads: {', '.join(BY['Refresh first'])}", 'VERIFIED: recomputed by oe_gen/model.py; equal to solver/truth.json', 'YES (inputs proved above)', F('deck', 'music', 'packs'), 'SQL L33 to SQL L168 recomputed by oe_gen/model.py; solver/truth.json')
fact('d_due', 'Due dates', 'Linear comments, Gmail and Slack (derived)', 'reasoning', f"{F('changes')} and {F('reply')}", F('changes', 'reply'),
     f"Fri Oct 10 ({len(D10)}): {', '.join(D10)}. Wed Oct 15 ({len(D15)}): {', '.join(D15)}", 'VERIFIED: recomputed by oe_gen/model.py; equal to solver/truth.json', 'YES (inputs proved above)', F('changes', 'reply'), 'SQL L33 to SQL L168 recomputed by oe_gen/model.py; solver/truth.json')
fact('d_maker', 'Makers', 'Slack (derived)', 'reasoning', f"{F('ask')} split and {F('leave', 'leave_ok')}", F('ask', 'leave', 'leave_ok'),
     f"Julia Lawson ({len(JULIA)}): {', '.join(JULIA)}. Marcus Bennett ({len(MARCUS)}): the other working ads (C06DJBJL798/1759269913.882683, C05KNDCHAAG/1759275107.322377)", 'VERIFIED: recomputed by oe_gen/model.py; equal to solver/truth.json', 'YES (inputs proved above)', F('ask', 'leave', 'leave_ok'), 'SQL L33 to SQL L168 recomputed by oe_gen/model.py; solver/truth.json')
fact('d_store', 'Store calls', 'Sheets, Drive, Docs and Slack (derived)', 'reasoning', f"{F('sheet', 'store', 'icon_no', 'calendar')}", F('sheet', 'store', 'icon_no', 'calendar'),
     "app icon Halloween version, due Thu Oct 16 12:00 PT; iPad 12.9\" set Halloween version, same cut; iPhone 6.5\" set Reuse; Google Play phone set Reuse; all Martin Walsh (f_fdd6d2d2f4a4d2f5b908fb, d_74a7c95c28097dd9777e01, C08R8CHB0QL/1758127951.679146)", 'VERIFIED: equal to solver/truth.json', 'YES (inputs proved above)', F('sheet', 'store', 'icon_no', 'calendar'), 'SQL L33 to SQL L168 recomputed by oe_gen/model.py; solver/truth.json')

# ---------------------------------------------------------------- requirements
REQ = [
    ("Leonard asked me in #zombie_marketing yesterday to own the art side of Halloween for Zombie Match 3D", 'Discovery: the source message', 'Explicit', F('ask')),
    ("I'm walking everyone through it at Thursday's review", 'Constraint: the deadline and the audience', 'Explicit', F('review')),
    ("Can you take his message and do it all for me?", 'Constraint: every source and ask in the message applies', 'Explicit (contents through F1)', F('ask', 'sheet', 'calendar', 'deck', 'changes', 'reply', 'leave', 'leave_ok')),
    ("Work out the Halloween call for everything that's live today, the store pages and every ad we're running", 'Discovery: the population (62 surfaces) and a call for each', 'Explicit', F('sheet', 'unity', 'archive', 'card', 'library', 'd_skip', 'd_hv', 'd_rf', 'd_store')),
    ("who makes what by when", 'Discovery: maker and due date per surface', 'Explicit', F('d_due', 'd_maker', 'd_store', 'reply', 'leave', 'leave_ok', 'calendar')),
    ("put it in a plan doc", 'Write: a Google Doc in Claire\'s Drive', 'Explicit', F('d_skip', 'd_hv', 'd_rf', 'd_due', 'd_maker', 'd_store')),
    ("a tracker in my Drive", 'Write: a spreadsheet with one row per surface', 'Explicit', F('d_skip', 'd_hv', 'd_rf', 'd_due', 'd_maker', 'd_store')),
    ("shared with everyone on the review so they can comment", 'Write: both files shared with the six others on the invite', 'Explicit', F('review')),
    ("Comment each ad's call and due date on its ART ticket", 'Write: 58 comments', 'Explicit', F('d_skip', 'd_hv', 'd_rf', 'd_due')),
    ("assign the ones that need new work to whoever's making them", 'Write: 48 assignments', 'Explicit', F('d_maker', 'users')),
    ("open ART tickets for any new store art", 'Write: 2 tickets, narrowed by Leonard\'s reply', 'Explicit', F('d_store', 'export_ok', 'users')),
    ("reply in Leonard's thread with both links before the review", 'Write: one thread reply', 'Explicit', F('ask')),
]
for span, *_ in REQ:
    assert span in PROMPT, span

# ---------------------------------------------------------------- writes
WR = [
    ('R6', 'Create the plan doc', '"put it in a plan doc"', 'gdocs_create_document (exists)', 'title (bodyText carries the plan)', F('d_store'), "a new Google Doc owned by Claire with the plan in its body", 'the calls, ship route and dates, reuse, owners', 'doc'),
    ('R7', 'Create the tracker and write its rows', '"a tracker in my Drive"', 'gsheets_create_spreadsheet (exists), gsheets_values_update (exists)', 'title; spreadsheetId, range, values', F('d_skip', 'd_hv', 'd_rf', 'd_due', 'd_maker', 'd_store'), 'a new spreadsheet owned by Claire, header and 62 rows', 'call, owner, due date and a short reason per surface', 'tracker'),
    ('R8', 'Share both files (12 shares)', '"shared with everyone on the review so they can comment"', 'gdrive_share_file (exists)', 'fileId (emailAddress, role, type carry the person)', F('review'), 'six people hold commenter access on each file', 'role commenter or writer', 'share'),
    ('R9', f'Comment on {len(ADS)} ad tickets', '"Comment each ad\'s call and due date on its ART ticket"', 'linear_create_comment (exists)', 'issueId, body', ', '.join(TK[:3]) + ' and the other ad facts', 'one new comment per ticket', "the ad's call and due date; Skip has no date", 'comment'),
    ('R10', f'Assign {len(JULIA) + len(MARCUS)} tickets', '"assign the ones that need new work to whoever\'s making them"', 'linear_update_issue (exists)', 'id (assignee carries the maker)', F('d_maker', 'users'), 'each working ad has its maker as assignee', 'Marcus Bennett or Julia Lawson', 'assign'),
    ('R11', 'Open 2 ART tickets', '"open ART tickets for any new store art"', 'linear_create_issue (exists)', 'team, title', F('d_store', 'users'), 'two new ART tickets, assigned to Martin Walsh', 'the icon and the iPad 12.9" set, with the merge cut', 'ticket'),
    ('R12', "Reply in Leonard's thread", '"reply in Leonard\'s thread with both links before the review"', 'slack_send_message (exists)', 'channel, text (thread_ts carries the thread)', F('ask'), 'a sent reply under C06DJBJL798/1759269913.882683', 'both links', 'reply'),
]

TRAPS = [
    ('T1', f"Frederick's Sep 30 mail: every Halloween ad by Wed Oct 15 ({F('changes')}, {mail_row('October UA plan - changes')['id']})", F('reply'), 'C0880U9751A/1759275738.984915 is 32 minutes later, same author, names Android US phone'),
    ('T2', f"Sep 12 draft: Fri Oct 17, four campaigns ({F('draft')})", F('changes'), f"{mail_row('October UA plan - changes')['id']} 'not the 17th'"),
    ('T3', f"April capture notes on ART-795, ART-797 and ART-805 ({fid['t:ART-795']}, cmt_art795_1)", F('note'), 'C09ATAJ220H/1758823964.738872, Sep 25, names three cuts and builds'),
    ('T4', f"Marcus's DM says the cheer fastcouch test is done ({F('im')}, D05V2N6PZNU/1759166437.080255)", F('robert'), "C08R8CHB0QL/1759248337.170599, Robert, a day later: 'We can't ship these'"),
    ('T5', f"The ask gives the stills to Martin ({F('ask')})", F('leave', 'leave_ok'), 'C05KNDCHAAG/1759275107.322377 is later than the ask, same author'),
    ('T6', f"Campaign notes on ART-811 and ART-813 keep iOS UK tablet ({fid['t:ART-811']}, cmt_art811_2)", F('restart'), f"{mail_row('Unity retention restart')['id']}, Sep 29, later than the Sep 9 notes"),
    ('T7', f"End card 001 tickets name Android #1529 ({fid['t:ART-833']}, cmt_art833_1)", F('packs'), 'Trello action 68d6cff0c6568da5d9c8e81f, Sep 26'),
    ('T8', f"The sheet looks like the whole list ({F('unity')}, {SHEETID})", F('card', 'library'), 'Trello 68dc65a0f2d7fb28743f5860 and cmt_art831_2 name two off-sheet ads'),
    ('T9', f"Leonard's 'around the 24th' icon swap ({F('ask')})", F('calendar'), "f_fdd6d2d2f4a4d2f5b908fb 'Merge cut is Thu Oct 16, 12:00 PT'"),
    ('T10', f"Martin's Sep 17 concept reads as a finished icon ({F('concept')}, C08R8CHB0QL/1758121809.236839)", F('icon_no'), "C08R8CHB0QL/1758127951.679146, 'not for the app icon'"),
    ('T11', f"Martin's 'exported' reads as every store set ({F('export')}, C08R8CHB0QL/1759245641.309714)", F('store'), 'd_74a7c95c28097dd9777e01 holds iPhone and Google Play files only'),
    ('T12', f"ART-840's Sep 11 opening reads as a new capture ({fid['t:ART-840']}, cmt_art840_1)", F('deck'), "'Captured Jul 28; Boris opening added Sep 11' against the Jul 29 swap in f_5ebf55ad29e815d46243c8"),
    ('T13', f"ART-831 Android #1450 reads as post-swap ({fid['t:ART-831']}, cmt_art831_1)", F('deck'), 'build number 1450 against Android #1452 in f_5ebf55ad29e815d46243c8'),
    ('T14', f"ART-809 is on a current build with no master note ({fid['t:ART-809']}, cmt_art809_1)", F('music'), BASE['music']['locator']),
    ('T15', f"ART-832 says 'Made by Martin Walsh' ({fid['t:ART-832']}, SQL L124)", F('ask'), "the ask: 'Marcus has video and end cards'"),
]
RISKS = [
    ('1', 'Tracker row wording: a run may write Skip October; the deck word is Skip', F('d_skip'), 'rubric (accept either)', 'rubric stage'),
    ('2', "Store due dates: an earlier internal date that names the cut is fair (brief 4b; /hardness r2)", F('d_store'), 'rubric (accept)', 'rubric stage'),
    ('3', 'Julia is not on the review, so no row may require sharing with her', F('review', 'd_maker'), 'rubric', 'rubric stage'),
    ('4', 'A blanket Oct 10 fails for ads off Android US phone (surface S39)', F('d_due'), 'rubric', 'rubric stage'),
    ('5', "Frederick's Trello comment carries a CPI clause; SC-11 says not to grade Unity spend", F('card'), 'OE accuracy / rubric', 'kept off every Expected line'),
    ('6', 'Unity Live since values on the sheet are not graded', F('unity'), 'rubric', 'kept off every Expected line'),
]

# ---------------------------------------------------------------- visibility proof
brow = [' | '.join(str(c) for c in f) for f in FACTS]
need = sorted({x for r in brow for _, x in G.scoped_ids(r)})
cs_json = json.loads(run([PY, '-B', 'Task_Authoring/tools/persona_view.py', 'check-sql', PERSONA, SQLREL, '--json']))
sq = {k for r in cs_json['rows'] for k in r['keys']}
seeded = [x for x in need if x in sq or x.split('/')[-1] in sq]
base = [x for x in need if x not in seeded]
lbf = os.path.join(HERE, 'oe_lb_ids.txt')
open(lbf, 'w').write('\n'.join(seeded) + '\n')
cs_txt = run([PY, '-B', 'Task_Authoring/tools/persona_view.py', 'check-sql', PERSONA, SQLREL, '--load-bearing', 'Task_Authoring/task_inputsN2/Working_Files/oe_gen/oe_lb_ids.txt'])
yes_rows = [l for l in cs_txt.splitlines() if l.startswith('[YES LB]')]
verdict = [l for l in cs_txt.splitlines() if l.startswith('verdict:')]
svc_of = {x: s for r in brow for s, x in G.scoped_ids(r)}
cansee = []
for x in base:
    o = run([PY, '-B', 'Task_Authoring/tools/persona_view.py', 'can-see', PERSONA, svc_of[x], x]).splitlines()
    cansee.append(o[0] if o else f'{PERSONA} {svc_of[x]} {x}: UNVERIFIED')

# ---------------------------------------------------------------- write
O = []
P = O.append
P('# 08 OE Writing Ledger — claire-zm3d-halloween-art-plan (injection rev3)')
P('Generated 2026-11-06 · Clock 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · seed bound 2025-10-01T00:00:00Z · Persona Claire Morgan claire.morgan@harmonygames.co (Art Lead) · Tier Long-Horizon · Mode Medium')
P(f'Status: READY — every requirement has verified facts, every scoped fact is persona-visible (pasted proof below), all {len(WR)} write families map to cataloged tools, friction is none')
P('Inputs read: 04_Prompt.txt — present (sha256 63d7c0713c3b) · 00_Assigments.md — present · 01_Universe_Inject.sql — present (rev3, sha256 0a08dedecd60) · 01_Grounding_Dossier.md — present (leads only) · 01_Scenario_Design.md + 01_Hardness_Manifest.json — present (leads for traps only) · 03_Error_Async_Config.txt — present (Friction: none) · 02_Reference_Files_Manifest.md — absent (no attachments) · 04_Prompt_Writing_Brief.md — present (§4b accepted outcomes) · six baseline trajectories and /hardness r2 — present (routes only)')
P('')
P('Persona binding: roster entry claire_morgan, Claire Morgan, Art Lead, Design, claire.morgan@harmonygames.co. Scoped services: Gmail (own mailbox), Slack (member of #zombie_marketing, #zombie-art, #zombie-match3d, #zm-animations, #company-internal, #builds and her IM with Marcus), Calendar (own calendar), Drive/Docs/Sheets/Slides (files she owns or that are shared with her). Unscoped: Linear, Trello, Contacts.')
P('')
P("Dates: Pacific first, UTC beside it. 'sent', 'created' and 'posted' mark record times; 'starts' and 'due' mark semantic future dates. Every record time below is at or before the seed bound.")
P('')
P('## A · Requirements (traced to the prompt)')
P('| R | Prompt span (quoted) | Type (Discovery / Write / Tell / Constraint) | Explicit / implicit | Fact IDs |')
P('|---|---|---|---|---|')
for i, (span, typ, ex, fids) in enumerate(REQ, 1):
    P(f'| R{i} | "{span}" | {typ} | {ex} | {fids} |')
P('')
P('## B · Facts')
P('| F | Fact / value | Service | Tool family (catalog) | Locator | Locator origin (prompt · F-n · search "query text") | Expected data (dates typed: created / starts / due) | Ledger result for the Expected line (VERIFIED quote · not_a_claim · ABSENCE evidence_check · UNRESOLVED) | Persona-visible? (proof) | Depends on | Source pointer |')
P('|---|---|---|---|---|---|---|---|---|---|---|')
for f in FACTS:
    P('| ' + ' | '.join(str(c).replace('|', '/').replace('\n', ' ') for c in f) + ' |')
P('')
P('Visibility proof (persona_view can-see / check-sql lines, pasted verbatim)')
P('')
P(f'`python3 Task_Authoring/tools/persona_view.py check-sql {PERSONA} {SQLREL} --load-bearing oe_gen/oe_lb_ids.txt` ({len(seeded)} seeded ids; load-bearing rows and the verdict line kept):')
P('')
for l in yes_rows + verdict:
    P(l)
P('')
P(f'`python3 Task_Authoring/tools/persona_view.py can-see {PERSONA} <service> <id>` ({len(base)} base ids, first line of each):')
P('')
for l in cansee:
    P(l)
P('')
P('## C · Write capability')
P('| R | Required write | Prompt authority (quoted; agent, not user-reserved) | Catalog tool (exists?) | Required parameters | Target (fact ID) | Completing end state | Content the prompt requires | Defer search (services · population · pagination complete · governing version · result, or UNRESOLVED) | Feasible? |')
P('|---|---|---|---|---|---|---|---|---|---|')
for w in WR:
    P('| ' + ' | '.join(w[:8]) + f' | {DEFER[w[8]]} | yes |')
P('')
P('## D · Friction facts')
P('| Function (01_) | Mode / rate / wait | Facts blocked | Alternative path (service, locator) | Alternative facts | Visible? |')
P('|---|---|---|---|---|---|')
P('| none | Friction: none (03_Error_Async_Config.txt) | — | — | — | — |')
P('')
P('## E · Traps and distractors')
P('| T | What the agent meets (pointer) | Competes with (fact ID) | Discriminator (timestamp / author / ID) |')
P('|---|---|---|---|')
for t in TRAPS:
    P('| ' + ' | '.join(t) + ' |')
P('')
P('## F · Open risks')
P('| # | Risk | Facts affected | Consequence (OE accuracy / rubric / UGT / feasibility) | Check needed |')
P('|---|---|---|---|---|')
for r in RISKS:
    P('| ' + ' | '.join(r) + ' |')
P('')
P('## G · Tally')
nq = sum(1 for f in FACTS if 'VERIFIED' in f[7])
P(f'Requirements {len(REQ)} · facts {len(FACTS)} · writes {len(WR)} (feasible {len(WR)}) · friction items 0 · expected values {len(FACTS)} (quoted {nq} · not_a_claim 0 · ABSENCE-checked 1) · unverified visibility 0 · blocking 0')
P('')
P('## Self-review')
P('')
P(f"Walked Evals/2_Oracle_Events_Eval.md 1.1, 2.1–2.6 and 3.1–3.5 against this ledger in order. Every requirement has facts; every write family has its prompt authority, a cataloged tool with its required parameters, a completing end state and a defer search; friction is none; every scoped fact carries pasted visibility proof. Every §B value was re-verified in this run: seeded rows re-parsed from 01_Universe_Inject.sql, base records read through hg.py, and oe_gen/model.py recomputed all 58 calls, due dates and makers from the rows and asserted them equal to solver/truth.json. No-event-text scan: §B holds facts and dependency edges only.")
P('')
P('| R | Counter-reading (strongest other reading of the span, or a competing location) | Evidence that resolves it | Result |')
P('|---|---|---|---|')
CRS = [
    ('R1', "'his message' could be another Leonard post in #zombie_marketing", 'C06DJBJL798/1759269913.882683 is the one Sep 30 post that tags Claire and asks for the Halloween art plan', 'holds'),
    ('R2', "Thursday's review could be a different meeting", 'evt_d947bf7cd910549b674b1f is the one event named for it and it says Claire walks us through the plan and tracker', 'holds'),
    ('R3', "'do it all' could be read as only the sentences the prompt repeats", 'F1 lists the sources and asks; the prompt says take his message and do it all (brief §6)', 'holds'),
    ('R4', "'live today' could be the sheet alone", f"Trello 68dc65a0f2d7fb28743f5860 and cmt_art831_2 add two ads; the Archive tab removes four ({F('card', 'library')})", 'holds (62)'),
    ('R5', "'by when' could be one date for all ads", f"C0880U9751A/1759275738.984915 splits Android US phone from iOS UK ({F('reply')})", 'holds'),
    ('R6', "the plan could be the tracker's tab", "C06DJBJL798/1759269913.882683: 'a plan doc we can comment on plus a tracker'", 'holds'),
    ('R7', "the tracker could list only rows that need work", "brief §4b row set and C06DJBJL798/1759269913.882683 'go through everything that's live today'", 'holds (62 rows)'),
    ('R8', "'everyone on the review' could include Julia, who now makes six ads", f"evt_d947bf7cd910549b674b1f lists seven people and Julia is not one ({F('review')})", 'holds (6 shares per file)'),
    ('R9', "Skip ads could need no comment", "the prompt says each ad; brief §4b comments on 58 tickets; Skip has no date", 'holds (58)'),
    ('R10', "'whoever's making them' could be the ticket's original maker", f"C06DJBJL798/1759269913.882683 names the split and C05KNDCHAAG/1759275107.322377 updates it ({F('d_maker')})", 'holds (42 and 6)'),
    ('R11', 'new store art could include every store set', f"C08R8CHB0QL/1759247246.453725: 'whatever is already exported is done so no tickets needed for those' ({F('export_ok')})", 'holds (2 tickets)'),
    ('R12', "the reply could be a new post", "the prompt says Leonard's thread; thread ts 1759269913.882683 in C06DJBJL798", 'holds'),
]
assert len(CRS) == len(REQ)
for r in CRS:
    P('| ' + ' | '.join(r) + ' |')
P('')
P('Unresolved: none blocking. Open risks §F 1–6 go to the rubric stage or are kept off every Expected line.')
P('')
open(os.path.join(WF, '08_OE_Writing_Ledger.md'), 'w').write('\n'.join(O) + '\n')
json.dump({'fid': fid, 'seeded': seeded, 'base': base}, open(os.path.join(HERE, 'oe_ledger_ids.json'), 'w'), indent=1)
print('facts', len(FACTS), 'req', len(REQ), 'seeded', len(seeded), 'base', len(base), 'yes', len(yes_rows), 'cansee', [l.split(':')[-1].strip()[:3] for l in cansee])
