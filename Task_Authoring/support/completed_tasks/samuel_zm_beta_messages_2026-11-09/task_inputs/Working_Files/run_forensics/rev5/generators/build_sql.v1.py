#!/usr/bin/env python3
"""Builds task_inputsK/01_Universe_Inject.sql for samuel_zm_beta_messages.
Read-only on the base; writes only under the task folder; never executes SQL. Ids, times and planned wording come from
plan/ids.json (the scenario builder's output); this file is not allowed to import build_scenario, which rewrites the
draft manifest and the gradable surface on import. Row shapes follow base records and the bridge and Q4 tasks' SQL."""
import base64, datetime as D, email.utils, hashlib, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
TI = HERE.parents[1]
P = json.load(open(HERE / 'ids.json'))
ROWS_PN = {int(k): v for k, v in json.load(open(HERE / 'pn_rows.json')).items()}
HUNK = (HERE / 'rc18_hunk.txt').read_text()
I, BASE, T, Q, M, TK, PARENT = P['ids'], P['base'], P['times'], P['quotes'], P['members'], P['tickets'], P['parent']
SALT = "hg-samuel-zm-beta-messages|"

SAM, LEO, VIN, ROB, ART = ('samuel.turner@harmonygames.co', 'leonard.hayes@harmonygames.co', 'vincent.parker@harmonygames.co',
                           'robert@harmonygames.co', 'arthur.blake@harmonygames.co')
OLI, OWE = 'oliver.brooks@harmonygames.co', 'owen.baker@harmonygames.co'
NAMES = {SAM: 'Samuel Turner', LEO: 'Leonard Hayes', VIN: 'Vincent Parker', OLI: 'Oliver Brooks', OWE: 'Owen Baker'}
SLACK_U = {'leonard': 'EMPLOYEE_0038_SLACK_ID', 'vincent': 'EMPLOYEE_0012_SLACK_ID', 'robert': 'EMPLOYEE_0016_SLACK_ID',
           'brian': 'EMPLOYEE_0026_SLACK_ID'}
LIN = {'samuel': 'usr_caafeec2804b3a67', 'leonard': 'usr_63fffeb4fab5233e', 'vincent': 'usr_65c76e0b87aa7e9b',
       'oliver.brooks': 'usr_bdf01b53c6a92c5e', 'arthur': 'usr_cc3e90160f490686', 'brian.foster': 'usr_fc22d5941b2aeb5c',
       'calvin.price': 'usr_49b9dfa5208d400d', 'owen.baker': 'usr_4e13bd40cc73d0fc', 'julia.lawson': 'usr_8140f09bf9f1b94c',
       'martin.walsh': 'usr_51f5f16d46e8cf55', 'robert': 'usr_Robert'}
TR_LEO = 'PERSON_6094_TRELLO_USER_ID'
ROOT_LEO, ROOT_VIN = 'd_63fffeb4fab5233ed5bb73', 'd_65c76e0b87aa7e9b84d1df'
BOARD = {'id': '6851a6569f3bf818760632ab', 'name': 'ZM ROADMAP', 'shortLink': 'HSqnngwQ'}


def h(seed, n):
    return hashlib.sha256((SALT + seed).encode()).hexdigest()[:n]


def dt(iso):
    return D.datetime.fromisoformat(iso.replace('Z', '+00:00'))


def plus(iso, **kw):
    return (dt(iso) + D.timedelta(**kw)).strftime('%Y-%m-%dT%H:%M:%SZ')


def q(v):
    if v is None:
        return 'NULL'
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, (int, float)):
        return repr(v)
    s = str(v)
    if '\n' in s or '\\' in s or '\r' in s:
        return "E'" + s.replace('\\', '\\\\').replace("'", "''").replace('\r', '\\r').replace('\n', '\\n') + "'"
    return "'" + s.replace("'", "''") + "'"


def js(x):
    return json.dumps(x, ensure_ascii=False)


OUT, ROWS, IDS = {}, {}, {}


def ins(table, cols, vals, key):
    OUT.setdefault(table.split('.')[0], []).append(f"INSERT INTO {table} ({', '.join(cols)})\nVALUES ({', '.join(q(v) for v in vals)});")
    ROWS.setdefault(table, []).append(key)


def upd(table, sets, key_col, key):
    OUT.setdefault(table.split('.')[0], []).append(f"UPDATE {table} SET {', '.join(f'{k} = {q(v)}' for k, v in sets.items())} "
                                                   f"WHERE {key_col} = {q(key)};")
    ROWS.setdefault(table + ' (UPDATE)', []).append(key)


def thread_num(at, seed):
    return str((int(dt(at).timestamp() * 1000) << 20) + (int(h(seed, 8), 16) & 0xFFFFF))


# ============================================================ Drive / Docs / Sheets / Slides
DF_COLS = ['id', 'name', 'mime_type', 'parents_json', 'owner_email', 'shared_with_emails_json', 'shared_roles_json',
           'visibility', 'owners_json', 'modified_time', 'created_time', 'trashed', 'starred']
DOC_MT, SLIDE_MT, SHEET_MT = ('application/vnd.google-apps.document', 'application/vnd.google-apps.presentation',
                              'application/vnd.google-apps.spreadsheet')


def drive(fid, name, mime, parent, owner, shares, created, modified):
    ins('gdrive.drive_files', DF_COLS,
        [fid, name, mime, js([parent]), owner, js([e for e, _ in shares]), js([{'email': e, 'role': r} for e, r in shares]),
         'private', js([owner]), modified, created, False, False], fid)


def doc(fid, title, body, parent, owner, shares, created, modified):
    drive(fid, title, DOC_MT, parent, owner, shares, created, modified)
    first = len(body.split('\n', 1)[0])
    runs = [{'start': 0, 'end': first + 1, 'named_style': 'TITLE', 'list_id': None, 'list_nesting': 0},
            {'start': first + 1, 'end': len(body), 'named_style': 'NORMAL_TEXT', 'list_id': None, 'list_nesting': 0}]
    ins('gdocs.docs_documents', ['document_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility', 'body_text',
                                 'style_runs_json', 'revision_id', 'drive_file_id', 'created_time', 'modified_time'],
        [fid, title, owner, js([e for e, _ in shares]), 'private', body, js(runs), h('rev' + fid, 10), fid, created, modified], fid)


def sheet(fid, title, grid, tab, parent, owner, shares, created, modified):
    drive(fid, title, SHEET_MT, parent, owner, shares, created, modified)
    ins('gsheets.sheets_spreadsheets', ['spreadsheet_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility',
                                        'drive_file_id', 'created_time', 'modified_time'],
        [fid, title, owner, js([e for e, _ in shares]), 'private', fid, created, modified], fid)
    ins('gsheets.sheets_sheets', ['spreadsheet_id', 'sheet_id', 'title', '"index"', 'row_count', 'column_count', 'grid_json'],
        [fid, 0, tab, 0, 1000, 26, js(grid)], f"{fid}#0")


def deck(fid, title, slides, parent, owner, shares, created, modified):
    drive(fid, title, SLIDE_MT, parent, owner, shares, created, modified)
    ins('gslides.slides_presentations', ['presentation_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility',
                                         'drive_file_id', 'revision_id', 'created_time', 'modified_time'],
        [fid, title, owner, js([e for e, _ in shares]), 'private', fid, h('rev' + fid, 10), created, modified], fid)
    for i, (head, body) in enumerate(slides):
        sid = 'slide_' + h(fid + 's' + str(i), 12)
        ins('gslides.slides_pages', ['presentation_id', 'object_id', '"index"', 'layout', 'notes'], [fid, sid, i, 'TITLE_AND_BODY', None], f"{fid}#{sid}")
        for oid, ph, text, ordn, y, hgt in [('el_' + h(fid + 'e' + str(i), 12), 'TITLE', head, 0, 457200, 1143000),
                                             ('el_' + h(fid + 'b' + str(i), 12), 'BODY', body, 1, 1600200, 3200400)]:
            ins('gslides.slides_page_elements', ['presentation_id', 'page_object_id', 'object_id', 'kind', 'text',
                                                 'placeholder_type', 'x_emu', 'y_emu', 'width_emu', 'height_emu', 'table_json', 'ordinal'],
                [fid, sid, oid, 'SHAPE', text, ph, 457200, y, 8229600, hgt, None, ordn], f"{fid}#{oid}")


TEAM = [(SAM, 'reader'), (VIN, 'reader'), (ROB, 'reader'), (ART, 'reader')]
RULE_BODY = Q['rule'].replace('Beta message rule. A message', 'Beta message rule\nA message', 1)
for mark in ('Run these tests', '1. The feature', '2. The client can', '3. The client already', '4. It can reach', '5. It fires',
             '6. Vincent has', 'Go: it passes', 'In the beta means', 'Neither status', 'What Vincent counts', 'The final headline',
             'Drop tickets go'):
    RULE_BODY = RULE_BODY.replace(' ' + mark, '\n' + mark, 1)
doc(I['rule_doc'], 'Beta message rule', RULE_BODY, ROOT_LEO, LEO, TEAM, T['rule_doc'], T['rule_doc'])
deck(I['deck'], 'Beta readiness', [('Beta readiness', Q['deck'].split('. ', 1)[1])], ROOT_LEO, LEO, TEAM, T['deck'], T['deck'])

# Vincent's running pass log: the build each pass was made on, named in his QA note. Same words as his ticket comments.
QA_SHEET = 'f_' + h('qa-sheet', 22)
QA_DATE = '2025-09-24T15:00:00Z'
B_A, B_I = '0.3.127', '0.3.40'
sheet(QA_SHEET, 'Phone message checks',
      [['Message', 'Android', 'iOS', 'Checked', 'Notes'],
       ['Lives recharged', B_A, B_I, 'Sep 24', ''],
       ['Lapsed 1 day', B_A, B_I, 'Sep 24', 'phone date moved forward'],
       ['Lapsed 7 days', B_A, B_I, 'Sep 24', 'phone date moved forward'],
       ['Finish first mission', B_A, B_I, 'Sep 24', 'notifications switched on from settings'],
       ['Plague Race', B_A, 'iPhone', 'Sep 24', ''],
       ['Weekly Leaderboard reset', B_A, B_I, 'Sep 24', 'phone date moved forward']],
      'Beta', ROOT_VIN, VIN, [(SAM, 'reader'), (OLI, 'reader'), (OWE, 'reader'), (LEO, 'reader')], '2025-09-15T12:50:00Z', QA_DATE)
IDS['qa_sheet'] = QA_SHEET

# ============================================================ Slack
SL_COLS = ['id', 'ts', 'channel_id', 'type', 'user_id', 'text', 'thread_parent_id', 'thread_ts_legacy', 'reply_count',
           'reply_users_count', 'latest_reply', 'is_activity_message', 'subtype', 'reactions_json', 'files_json',
           'attachments_json', 'created_at', 'metadata_json']


def slack(chan_ts, user, text, parent=None):
    ch, ts = chan_ts.split('/')
    mid = hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]
    ins('slack.slack_messages', SL_COLS, [mid, ts, ch, 'message', user, text, parent[0] if parent else None, parent[1] if parent else None,
                                          0, 0, None, False, None, '[]', '[]', '[]',
                                          D.datetime.fromtimestamp(float(ts), D.UTC).strftime('%Y-%m-%dT%H:%M:%S.%fZ'), '{}'], chan_ts)
    return mid


IDS['slack_mid'] = {}
IDS['slack_mid']['brian_opinion'] = slack(I['brian_opinion'], SLACK_U['brian'], Q['brian_opinion'])
IDS['slack_mid']['ask_decision'] = slack(I['ask_decision'], SLACK_U['robert'], Q['ask_decision'])
ZART_ROOT = ('a3e78e820b9f880ef4e3d941562110df', '1759159849.386619')   # base: Martin, Sep 29, desert theme (3 replies, 3 people)
IDS['slack_mid']['corr_reply'] = slack(I['corr_reply'], SLACK_U['leonard'], Q['corr_reply'], parent=ZART_ROOT)
upd('slack.slack_messages', {'reply_count': 4, 'reply_users_count': 4, 'latest_reply': I['corr_reply'].split('/')[1]}, 'id', ZART_ROOT[0])
DMV_ROOT = ('c42902df5f54c75c1a6e3529cd25121c', '1759163970.141449')    # base: Samuel to Vincent, Sep 29, Android 2007 (no replies)
IDS['slack_mid']['qa_reply'] = slack(I['qa_reply'], SLACK_U['vincent'], Q['qa_reply'], parent=DMV_ROOT)
upd('slack.slack_messages', {'reply_count': 1, 'reply_users_count': 1, 'latest_reply': I['qa_reply'].split('/')[1],
                             'thread_ts_legacy': DMV_ROOT[1]}, 'id', DMV_ROOT[0])
IDS['slack_mid']['hub'] = slack(I['hub'], SLACK_U['leonard'], Q['hub'])

# ============================================================ Trello (two comments on ZM ROADMAP cards)
TA_COLS = ['id', 'type', 'date', '"idMemberCreator"', '"idBoard"', '"idCard"', 'data_json']


def badges(comments, due_complete=False):
    return {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0, "checkItemsChecked": 0,
            "checkItemsEarliestDue": None, "comments": comments, "description": False, "due": None, "dueComplete": due_complete,
            "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False, "location": False, "maliciousAttachments": 0,
            "start": None, "votes": 0}


def trello_comment(aid, at, card, lst, text, comments, due_complete=False):
    ins('trello.trello_actions', TA_COLS,
        [aid, 'commentCard', at, TR_LEO, BOARD['id'], card['id'],
         js({"board": BOARD, "card": card, "idCard": card['id'], "list": lst, "text": text, "textData": {"emoji": {}}})], aid)
    upd('trello.trello_cards', {'badges_json': js(badges(comments, due_complete)), '"dateLastActivity"': at}, 'id', card['id'])


CARD_NOTE_AT = '2025-09-24T16:00:00Z'
IDS['card_comment'] = f"{int(dt(CARD_NOTE_AT).timestamp()):08x}" + h('pn-card-comment', 16)
CARD_NOTE = "The beta list goes on this card as a checklist. " + Q['card']
trello_comment(IDS['card_comment'], CARD_NOTE_AT,
               {'id': BASE['pn_card'], 'idShort': 7, 'name': '[Feature] Push Notifications - Samuel + Leonard', 'shortLink': 'ADparqb9'},
               {'id': '6851a6608b76856437112e45', 'name': 'Jun 30th'}, CARD_NOTE, 2, True)
trello_comment(I['freeze_comment'], T['freeze'],
               {'id': BASE['tech_card'], 'idShort': 79, 'name': 'Fix TECH ISSUES', 'shortLink': 'pTbZYXdb'},
               {'id': '6851a674975da1fe76e70d93', 'name': 'BETA: Oct 10'}, Q['freeze'], 1)

# ============================================================ Gmail
GM_COLS = ['id', 'thread_id', 'user_email', 'label_ids_json', 'snippet', 'internal_date', 'date', 'size_estimate', 'subject',
           'from_email', 'from_name', 'to_json', 'cc_json', 'bcc_json', 'reply_to_json', 'body_text', 'body_html',
           'headers_json', 'in_reply_to', '"references"', 'mbox_from', 'attachments_meta_json']


def addr(e):
    return f"{NAMES[e]} <{e}>"


def msgid_for(key):
    return '<CA' + base64.b64encode(hashlib.sha256((SALT + key).encode()).digest()).decode()[:38].replace('/', '_').replace('+', '-') + '@mail.gmail.com>'


def mail(key, at, subject, body, frm, to, boxes, tid):
    d0, msgid = dt(at), msgid_for(key)
    ms = int(d0.timestamp() * 1000)
    body_r = body.replace('\n', '\r\n')
    snippet = ' '.join(body.split())[:140]
    hdrs = [{"name": "Message-ID", "value": msgid}, {"name": "Date", "value": email.utils.format_datetime(d0)},
            {"name": "Subject", "value": subject}, {"name": "From", "value": addr(frm)},
            {"name": "To", "value": ', '.join(addr(x) for x in to)}]
    ids = {}
    for box in boxes:
        tref = tid if box == SAM else f"{box}/{thread_num(at, key + box)}"
        ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [tref, box, snippet, None], tref)
        ins('gmail.gmail_messages', GM_COLS,
            [f"{box}/{msgid}", tref, box, js(["SENT"] if box == frm else ["INBOX", "CATEGORY_PERSONAL"]), snippet, ms, at, len(body_r) + 900,
             subject, frm, NAMES[frm], js([addr(x) for x in to]), '[]', '[]', '[]', body_r, None, js(hdrs), None, None, None, '[]'],
            f"{box}/{msgid}")
        ids[box] = f"{box}/{msgid}"
    return ids


QA_BODY = f"Hi all,\n\n{Q['qa']}\n\nPasses go in the Phone message checks sheet.\n\nVincent"
IDS['qa_msg'] = mail('qa-note', T['qa_note'], 'Phone messages for beta', QA_BODY, VIN, [SAM, OLI, OWE], [SAM, VIN], I['qa_thread'])[SAM]

# GitHub's mail for Arthur's inline comment joins the base notification thread for the PR (INT-12)
PR_SUBJ = 'Re: [[SOURCE_ORG_0001]-Games/match3d] Push notification (PR #248)'
PR_ROOT = '<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963243580@github.com>'   # the review mail before it in the base thread
GH_MSGID = '<[SOURCE_ORG_0001]-Games/match3d/pull/248/review/2963610417@github.com>'
GH_BODY = (f"@arthur.blake commented on this pull request.\r\n\r\n> +                DateTime fireTime = referenceDate.AddDays(i * 7);\r\n\r\n"
           f"{Q['arthur_inline']}\r\n\r\n-- \r\nReply to this email directly or view it on github:\r\n"
           f"https://github.com/[SOURCE_ORG_0001]-Games/match3d/pull/248#discussion_r2169904417\r\n"
           f"You are receiving this because you authored the thread.\r\n\r\nMessage ID: {GH_MSGID}")
d0 = dt(T['arthur_inline'])
IDS['arthur_mail'] = f"{SAM}/{GH_MSGID}"
ins('gmail.gmail_messages', GM_COLS,
    [IDS['arthur_mail'], BASE['pr248_mail'], SAM, js(["INBOX", "IMPORTANT", "CATEGORY_PERSONAL"]), ' '.join(GH_BODY.split())[:140],
     int(d0.timestamp() * 1000), T['arthur_inline'], len(GH_BODY) + 3000, PR_SUBJ, 'SVC_0248_EMAIL', 'SVC_0248_NAME',
     js(["SVC_3649_NAME <SVC_3649_EMAIL>"]), js([addr(SAM), "SVC_0613_NAME <SVC_0613_EMAIL>"]), '[]',
     js(["SVC_5111_NAME <SVC_5111_EMAIL_PLUS_ALIAS_2595>"]), GH_BODY, None,
     js([{"name": "Message-ID", "value": GH_MSGID}, {"name": "Date", "value": email.utils.format_datetime(d0)},
         {"name": "Subject", "value": PR_SUBJ}, {"name": "From", "value": "SVC_0248_NAME <SVC_0248_EMAIL>"},
         {"name": "To", "value": "SVC_3649_NAME <SVC_3649_EMAIL>"}, {"name": "In-Reply-To", "value": PR_ROOT},
         {"name": "References", "value": PR_ROOT}]), PR_ROOT, PR_ROOT, None, '[]'], IDS['arthur_mail'])

# ============================================================ Calendar (+ INT-11 mails)
GC_COLS = ['event_id', 'calendar_id', 'summary', 'description', 'location', 'start_ts', 'end_ts', 'start_json', 'end_json',
           'organizer_email', 'creator_email', 'attendees_json', 'status', 'visibility', 'transparency', 'rrule_json',
           'recurring_event_id', 'original_start_json', 'sequence', 'created', 'updated', 'hangout_link', 'ical_uid']
LADDER_START, LADDER_END, LADDER_MADE = '2025-09-26T16:00:00Z', '2025-09-26T16:30:00Z', '2025-09-23T18:10:00Z'
MEET = 'https://meet.google.com/rvq-hkzt-mbn?hs=224'
UID = h('uid-ladder', 32) + '@hg4'
IDS['evt'] = {}
for cal in (SAM, LEO):
    eid = I['ladder_review'] if cal == SAM else 'evt_' + h('ladder' + cal, 22)
    att = []
    for e in (LEO, SAM):
        a = {"email": e, "organizer": e == LEO, "responseStatus": 'accepted' if e == LEO else 'needsAction'}
        if e == cal:
            a["self"] = True
        att.append(a)
    ins('gcal.gcal_events', GC_COLS, [eid, cal, 'Lapsed ladder review', Q['ladder_review'], None, LADDER_START, LADDER_END,
                                      js({"dateTime": LADDER_START}), js({"dateTime": LADDER_END}), LEO, LEO, js(att), 'cancelled', None,
                                      'opaque', '[]', None, None, 1, LADDER_MADE, T['ladder_review'], MEET, UID], eid)
    IDS['evt'][cal] = eid


def cal_mail(key, at, subject, lead):
    d0 = dt(at)
    mid = f"<calendar-{h(key, 8)}-{h(key + '1', 4)}-{h(key + '2', 4)}-{h(key + '3', 4)}-{h(key + '4', 12)}@google.com>"
    who = f"leonard hayes <{LEO}>"
    body = (f"{lead}Lapsed ladder review\r\nFriday Sep 26, 2025 \u22c5 10am \u2013 10:30am\r\nCentral Standard Time - El Salvador\r\n\r\n"
            f"Join with Google Meet\r\n{MEET}\r\n\r\nOrganizer\r\nLeonard Hayes\r\n{LEO}\r\n\r\nGuests\r\nLeonard Hayes - organizer\r\n{SAM}\r\n")
    tref = f"{SAM}/{thread_num(at, key)}"
    snippet = ' '.join(body.split())[:140]
    ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [tref, SAM, snippet, None], tref)
    hdrs = [{"name": "Reply-To", "value": who}, {"name": "Sender", "value": "Google Calendar <SVC_0842_EMAIL>"},
            {"name": "Message-ID", "value": mid}, {"name": "Date", "value": email.utils.format_datetime(d0)},
            {"name": "Subject", "value": subject}, {"name": "From", "value": who}, {"name": "To", "value": SAM}]
    ins('gmail.gmail_messages', GM_COLS,
        [f"{SAM}/{mid}", tref, SAM, js(["INBOX", "CATEGORY_PERSONAL"]), snippet, int(d0.timestamp() * 1000), at, len(body) + 3000, subject,
         LEO, 'leonard hayes', js([SAM]), '[]', '[]', js([who]), body, None, js(hdrs), None, None, None, '[]'], f"{SAM}/{mid}")
    return f"{SAM}/{mid}"


WHEN = 'Lapsed ladder review @ Fri Sep 26, 2025 10am - 10:30am (CST) (samuel.turner@harmonygames.co)'
IDS['invite_mail'] = cal_mail('ladder-invite', LADDER_MADE, 'Invitation: ' + WHEN, '')
IDS['cancel_mail'] = cal_mail('ladder-cancel', T['ladder_review'], 'Canceled event with note: ' + WHEN,
                              f'This event has been canceled and removed from your calendar with a note:\r\n"{Q["ladder_review"]}"\r\n\r\n')

# ============================================================ GitHub (Arthur's inline comment, before his approval rev_6)
ins('github.github_review_comments', ['id', 'pr_id', 'author_login', 'body', 'path', 'diff_hunk', 'line', 'position', 'commit_id',
                                      'in_reply_to_id', 'created_at', 'seq'],
    [I['arthur_inline'], BASE['pr248'], 'EMPLOYEE_0025_GITHUB_USERNAME', Q['arthur_inline'],
     'Assets/Scripts/Notifications/NotificationManager.cs', HUNK, None, None, None, None, T['arthur_inline'], 18], I['arthur_inline'])

# ============================================================ Linear
ins('linear.linear_team_memberships', ['id', 'team_id', 'user_id', 'created_at'],
    ['tmem_team_DES_' + LIN['samuel'], 'team_DES', LIN['samuel'], '2025-09-23T16:00:00Z'], 'tmem_team_DES_' + LIN['samuel'])

BUILT_NOTE = "Built in match3d #248."
LIVE_NOTE = {'Quests rollover': 'Quests are already in production.', 'Login Calendar update': 'Daily login is already in the game.'}
ASK = {  # key: (filed at, description)
    'Endless entries back': ('2025-09-24T09:12:00Z', "Endless players run out of entries and leave. Tell them when entries are back so they come back for another run."),
    'Endless weekly result': ('2025-09-24T09:31:00Z', "When the Endless week closes, tell players where they finished."),
    'Boss Arena open': ('2025-09-24T12:58:00Z', "Let players know when Boss Arena is open."),
    'Boss Arena last hours': ('2025-09-24T13:03:00Z', "Reminder a few hours before Boss Arena closes."),
    'Season Pass last 48 hours': ('2025-09-24T14:05:00Z', "Two days before the season ends, so nobody loses tiers they already earned."),
    'Season Pass premium nudge': ('2025-09-24T15:40:00Z', "When a free-track player gets close to a premium reward, show them what they'd get."),
    'Plague Race last hour': ('2025-09-24T16:22:00Z', "Race players drop off near the end. One hour left in the race."),
    'Plague Race result': ('2025-09-24T16:27:00Z', "Tell players where they placed when a race ends."),
    'Zombie Lane reward ready': ('2025-09-25T09:14:00Z', "Ping the moment a reward on Zombie Lane is ready."),
    'Trophy Path reward waiting': ('2025-09-25T09:18:00Z', "Second ping, two days after a Trophy Path reward was left unclaimed. Separate from the ready ping on DES-336."),
    'Daily chest ready': ('2025-09-25T10:08:00Z', "Ping when today's daily gift chest is ready to open. This is the chest itself, not the calendar refresh on DES-322."),
    'Free shop coins ready': ('2025-09-25T13:44:00Z', "We already give free coins in the shop. Ping when the next ones can be taken."),
    'Support reply waiting': ('2025-09-25T14:26:00Z', "Tell a player when Helpshift support has answered them."),
    'New levels added': ('2025-09-25T15:50:00Z', "Tell players who finished the last handmade level that new ones are in."),
    'Lapsed 3 days': ('2025-09-25T17:05:00Z', "Could we add a reminder on day 3 between the 1 day and 7 day ones."),
    'Lapsed 30 days': ('2025-09-25T17:09:00Z', "Could we add a last reminder at 30 days."),
    'Lapsed 14 days': ('2025-09-26T14:22:00Z', "A reminder at two weeks for anyone who still hasn't come back."),
    'Comeback gift': ('2025-09-26T15:31:00Z', "Lapsed players tap the message and get a gift when they open the game."),
    'Rewarded ad ready': ('2025-09-29T12:10:00Z', "Ping when a rewarded ad is ready to watch for a bonus."),
}
AUD_STYLE = {'brian.foster': "for {a}", 'robert': "{a}", 'oliver.brooks': "who it's for: {a}", 'julia.lawson': "this is for {a}",
             'owen.baker': "for {a}", 'calvin.price': "for {a}", 'martin.walsh': "it's for {a}", 'leonard': "Who it's for: {a}"}
ARTHUR = {  # his pass over everything unbuilt on Sep 25: one line each, in his own words for that ticket
    'Win & Collect start': "not in NotificationManager yet. windows are fixed so a local timer can do it",
    'Quests rollover': "not in NotificationManager yet. client knows the rollover time, local timer is enough",
    'Login Calendar update': "nothing for this in NotificationManager. it's just the daily reset, local timer works",
    'Season Pass start': "not scheduled anywhere yet. client has the season dates so a local timer can do it",
    'Hourly Coins': "not in NotificationManager",
    "Nathan's Treasure Hunt": "nothing in NotificationManager for this",
    'Streak Fever': "nothing in NotificationManager for this one either",
    'Axe Arena': "not in NotificationManager",
    'Endless entries back': "not in NotificationManager yet. entries come back on a timer so local works",
    'Endless weekly result': "not in NotificationManager. this needs a server send, the phone doesn't know the final standings",
    'Boss Arena open': "not scheduled yet. local timer can do it",
    'Boss Arena last hours': "not in NotificationManager yet, local timer off the end time",
    'Season Pass last 48 hours': "not in NotificationManager yet. client has the end date, local timer",
    'Season Pass premium nudge': "not in NotificationManager. needs a server send, it's picked per player from server data",
    'Plague Race last hour': "not in NotificationManager yet. race end is known, local timer is fine",
    'Plague Race result': "needs a server send, the final placing only exists on the server",
    'Zombie Lane reward ready': "not in NotificationManager yet. local timer can do it",
    'Trophy Path reward waiting': "same as the lane one, not scheduled, local timer is enough",
    'Daily chest ready': "not in NotificationManager yet. the chest timer is local",
    'Free shop coins ready': "not scheduled yet, local timer is enough",
    'Support reply waiting': "needs a server send, the reply comes from Helpshift",
    'New levels added': "needs a server send, nothing on the phone knows we shipped levels",
    'Lapsed 3 days': "not in NotificationManager yet. local timer, same as the other lapsed ones",
    'Lapsed 30 days': "not in NotificationManager yet. local timer can do it",
}
ARTHUR_FROM = '2025-09-25T20:30:00Z'          # after the last ask of that day, before Lapsed 14 days was filed
SAME_BUILD = "arrived on both on store builds, Android 0.3.127 and iOS 0.3.40"
VINCENT = {'Lives recharged': ('2025-09-24T14:10:00Z', SAME_BUILD, 'qa-lives'), 'Lapsed 1 day': ('2025-09-24T14:16:00Z', SAME_BUILD, 'qa-l1'),
           'Lapsed 7 days': ('2025-09-24T14:22:00Z', SAME_BUILD, 'qa-l7'),
           'Plague Race': ('2025-09-24T14:30:00Z', "arrived on Android 0.3.127 and on iPhone", 'race-qa'),
           'Weekly Leaderboard reset': ('2025-09-24T14:40:00Z', SAME_BUILD, 'weekly-qa'),
           'Finish first mission': ('2025-09-24T14:50:00Z', "arrives on both when notifications are switched on from settings", 'ftue-qa')}


def cid(label):
    return 'cmt_' + h(label, 20)


COMMENTS = {}     # issue id -> [(at, author, body, comment id)]


def comment(issue, at, who, body, label):
    COMMENTS.setdefault(issue, []).append((at, LIN[who], body, cid(label)))


ISSUES = []
LI_COLS = ['id', 'project_id', 'team_id', 'parent_id', 'assignee_id', 'creator_id', 'state_id', 'cycle_id', 'identifier', 'number', 'title',
           'description', 'priority', 'estimate', 'due_date', 'started_at', 'completed_at', 'canceled_at', 'archived_at',
           'time_in_status_minutes', 'labels_json', 'links_json', 'relations_json', 'state_history_json', 'is_archived', 'created_at', 'updated_at']


def issue(key, parent, assignee, creator, state, title, desc, prio, started, completed, created, relations=()):
    ISSUES.append(dict(id=key, parent=parent, assignee=assignee, creator=creator, state=state, title=title, desc=desc, prio=prio,
                       started=started, completed=completed, created=created, relations=list(relations)))


issue(PARENT, None, LIN['samuel'], LIN['leonard'], 'In Progress', 'Beta player messages', Q['parent'], 2, plus(T['parent'], minutes=1), None, T['parent'])

n_row, n_arthur, arthur_at = 0, 0, 0
for m in M:
    if not m['ticket']:
        continue
    k, tkt, who = m['key'], m['ticket'], m['asker']
    aud = AUD_STYLE[who].format(a=m['note'])
    built = m['built']
    if k == 'Win & Collect start':
        created = T['wc_ticket']
        desc = "Players should get a ping when a Collect & Win window opens. Three windows a week."
        issue(tkt, None, LIN['calvin.price'], LIN[who], 'In Review', m['title'], desc, 3, plus(created, minutes=30), None, created)
        comment(tkt, plus(created, minutes=4), who, aud, 'aud-' + tkt)
    elif m['source'].startswith('PNs Beta'):
        r = ROWS_PN[int(m['source'].rsplit(' ', 1)[1])]
        created = plus(T['parent'], minutes=1 + n_row)
        desc = f"{r['details'].rstrip('.')}. Fires: {r['when']}. Headline: {r['headline']}"
        if built:
            desc += ' ' + BUILT_NOTE
        if k in LIVE_NOTE:
            desc += ' ' + LIVE_NOTE[k]
        started = plus(created, minutes=5)
        completed = None
        if built:
            at, text, label = VINCENT[k]
            completed = plus(at, minutes=20) if k != 'Plague Race' else '2025-09-24T15:30:00Z'   # after Leonard's 15:10 comment
        issue(tkt, PARENT, LIN['samuel'], LIN['leonard'], 'Done' if built else 'In Review', m['title'], desc, 2, started, completed, created)
        if k == 'Lives recharged':
            aud += ". Rollover on the sheet is wrong for this one, it goes when lives are full"
        comment(tkt, plus(T['parent'], minutes=22 + n_row), 'leonard', aud, 'aud-' + tkt)
        if built:
            comment(tkt, at, 'vincent', text, label)
        n_row += 1
    else:
        created, desc = ASK[k]
        rel = {'Boss Arena open': ['ZOM-542'], 'Daily chest ready': ['ZOM-556']}.get(k, [])
        issue(tkt, PARENT, LIN['samuel'], LIN[who], 'In Review', m['title'], desc, 3, plus(created, minutes=8), None, created,
              [{"target": x, "type": "relates"} for x in rel])
        comment(tkt, plus(created, minutes=3), who, aud, 'aud-' + tkt)
    # Arthur's pass over everything unbuilt that existed on Sep 25
    if not built and created < ARTHUR_FROM:
        arthur_at += 1 + int(h('gap-' + tkt, 4), 16) % 7          # uneven gaps: one person working down a list
        comment(tkt, plus(ARTHUR_FROM, minutes=arthur_at), 'arthur', ARTHUR[k], 'arthur-' + tkt)
        n_arthur += 1

comment(TK['Plague Race'], T.get('race_daily', '2025-09-24T15:10:00Z'), 'leonard', Q['race_daily'], 'race-daily')
comment(TK['Comeback gift'], T.get('gift_note', '2025-09-26T16:00:00Z'), 'leonard', Q['gift_note'], 'gift-v2-note')

comment('ZOM-542', T['boss_ask'], 'brian.foster', Q['boss_ask'], 'boss-ask')
comment('ZOM-556', T['gift_ask'], 'julia.lawson', Q['gift_ask'], 'gift-ask')
for a, b in (('race-qa', I['race_qa']), ('weekly-qa', I['weekly_qa']), ('ftue-qa', I['ftue_qa']), ('gift-v2-note', I['gift_note']),
             ('race-daily', I['race_daily']), ('boss-ask', I['boss_ask']), ('gift-ask', I['gift_ask'])):
    assert cid(a) == b, (a, b, cid(a))

for it in sorted(ISSUES, key=lambda x: int(x['id'].split('-')[1])):
    cs = sorted(COMMENTS.get(it['id'], []))
    last = max([it['created'], it['started'] or '', it['completed'] or ''] + [c[0] for c in cs])
    n = int(it['id'].split('-')[1])
    ins('linear.linear_issues', LI_COLS,
        [it['id'], None, 'team_DES', it['parent'], it['assignee'], it['creator'], it['state'], None, it['id'], n, it['title'], it['desc'],
         it['prio'], None, None, it['started'], it['completed'], None, None, None, '[]', '[]', js(it['relations']), '[]', False, it['created'], last],
        it['id'])
for iss in sorted(COMMENTS, key=lambda x: (x.split('-')[0], int(x.split('-')[1]))):
    for i, (at, author, body, c) in enumerate(sorted(COMMENTS[iss]), 1):
        ins('linear.linear_comments', ['id', 'issue_id', 'author_id', 'parent_id', 'body', 'is_edited', 'created_at', 'updated_at', 'sequence'],
            [c, iss, author, None, body, False, at, at, i], c)
upd('linear.linear_issues', {'relations_json': js([{"target": TK['Boss Arena open'], "type": "relates"}]), 'updated_at': T['boss_ask']}, 'id', 'ZOM-542')
upd('linear.linear_issues', {'relations_json': js([{"target": TK['Daily chest ready'], "type": "relates"}]), 'updated_at': T['gift_ask']}, 'id', 'ZOM-556')
upd('linear.linear_teams', {'issue_counter': P['last_ticket']}, 'id', 'team_DES')
IDS['comments'] = {k: [c[3] for c in sorted(v)] for k, v in COMMENTS.items()}
IDS['aud'] = {k: cid('aud-' + k) for k in COMMENTS if k.startswith('DES-')}
IDS['issues'] = {it['id']: {k: it[k] for k in ('state', 'title', 'created', 'started', 'completed')} for it in ISSUES}

# ============================================================ write
order_s = ['gdrive', 'gdocs', 'gsheets', 'gslides', 'slack', 'trello', 'gmail', 'gcal', 'github', 'linear']
n_ins = sum(1 for s in OUT for x in OUT[s] if x.startswith('INSERT'))
n_upd = sum(1 for s in OUT for x in OUT[s] if x.startswith('UPDATE'))
head = ['-- Are you planning to inject? Yes',
        f'-- HarmonyGames injection - persona Samuel Turner <{SAM}> (Game Designer), Long Horizon, Oct 1, 2025 universe.',
        f'-- Services: {", ".join(order_s)}. Statements: {n_ins} INSERT (one row each), {n_upd} UPDATE.',
        '-- Literal values only; parents before children; re-apply this exact SQL before every agent run.', 'BEGIN;']
body = []
for s in order_s:
    body.append(f'-- {s}')
    body += OUT.get(s, [])
(TI / '01_Universe_Inject.sql').write_text('\n'.join(head + body + ['COMMIT;']) + '\n')
json.dump({'ids': IDS, 'rows': ROWS}, open(HERE / 'sql_ids.json', 'w'), indent=1, ensure_ascii=False)
print(n_ins, 'INSERT', n_upd, 'UPDATE', {k: len(v) for k, v in ROWS.items()})
print('comments', sum(len(v) for v in COMMENTS.values()), 'arthur', n_arthur)
