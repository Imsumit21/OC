#!/usr/bin/env python3
"""Builds task_inputs/01_Universe_Inject.sql for calvin_qm_epic from plan/seed_text.json and plan/reports.py.
Read-only on the base; writes only under the task folder; never executes SQL. Row shapes follow base records read
through tools/hg.py at this stage and the archived tasks' SQL."""
import datetime as D, email.utils, hashlib, json, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TI = HERE.parents[1]
sys.path.insert(0, str(HERE))
import reports as RP
SEED = json.load(open(HERE / 'seed_text.json'))
SALT = 'calvin_qm:'
ID = {k: v['id'] for k, v in SEED.items()}
AT = {k: v['at'] for k, v in SEED.items()}
TX = {k: v['text'] for k, v in SEED.items()}

CAL, BRI, VIN, ART, LEO, JUL, MAR, OLI, OWE, SAM, ROB = [x + '@harmonygames.co' for x in (
    'calvin.price', 'brian.foster', 'vincent.parker', 'arthur.blake', 'leonard.hayes', 'julia.lawson', 'marcus.bennett',
    'oliver.brooks', 'owen.baker', 'samuel.turner', 'robert')]
SLACK_U = {'calvin': 'EMPLOYEE_0006_SLACK_ID', 'brian': 'EMPLOYEE_0026_SLACK_ID', 'vincent': 'EMPLOYEE_0012_SLACK_ID',
           'marcus': 'EMPLOYEE_0002_SLACK_ID', 'robert': 'EMPLOYEE_0016_SLACK_ID', 'bot': 'SLACK_BOT_0004_SLACK_ID'}
LIN = {'calvin': 'usr_49b9dfa5208d400d', 'brian': 'usr_fc22d5941b2aeb5c', 'vincent': 'usr_65c76e0b87aa7e9b',
       'oliver': 'usr_bdf01b53c6a92c5e', 'owen': 'usr_4e13bd40cc73d0fc', 'samuel': 'usr_caafeec2804b3a67'}
GH = {'arthur': 'EMPLOYEE_0025_GITHUB_USERNAME', 'oliver': 'EMPLOYEE_0003_GITHUB_USERNAME'}
TR_LEO = 'PERSON_6094_TRELLO_USER_ID'
ROOT = {CAL: 'd_49b9dfa5208d400d9b3937', VIN: 'd_65c76e0b87aa7e9b84d1df', ART: 'd_cc3e90160f490686039986'}
BOARD = {'id': '6851a6569f3bf818760632ab', 'name': 'ZM ROADMAP', 'shortLink': 'HSqnngwQ'}
BACKLOG = {'id': '68c451221ebabaf255a7d16b', 'name': 'Backlog'}


def h(seed, n):
    return hashlib.sha256((SALT + seed).encode()).hexdigest()[:n]


def dt(iso):
    return D.datetime.fromisoformat(iso.replace('Z', '+00:00'))


def plus(iso, **kw):
    return (dt(iso) + D.timedelta(**kw)).strftime('%Y-%m-%dT%H:%M:%SZ')


def ep(iso):
    return int(dt(iso).timestamp())


def q(v):
    if v is None:
        return 'NULL'
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, (int, float)):
        return repr(v)
    s = str(v)
    if '\n' in s or '\\' in s or '\r' in s or '\t' in s:
        return "E'" + s.replace('\\', '\\\\').replace("'", "''").replace('\r', '\\r').replace('\n', '\\n').replace('\t', '\\t') + "'"
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


# ============================================================ Drive / Docs / Sheets / Slides
DF_COLS = ['id', 'name', 'mime_type', 'parents_json', 'owner_email', 'shared_with_emails_json', 'shared_roles_json',
           'visibility', 'owners_json', 'modified_time', 'created_time', 'trashed', 'starred']
DOC_MT, SLIDE_MT, SHEET_MT, FOLDER_MT = ('application/vnd.google-apps.document', 'application/vnd.google-apps.presentation',
                                         'application/vnd.google-apps.spreadsheet', 'application/vnd.google-apps.folder')


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
        ins('gslides.slides_pages', ['presentation_id', 'object_id', '"index"', 'layout', 'notes'], [fid, sid, i, 'BLANK', None], f"{fid}#{sid}")
        for oid, ph, text, ordn, y, hgt in [('el_' + h(fid + 'e' + str(i), 12), 'TITLE', head, 0, 457200, 1143000),
                                             ('el_' + h(fid + 'b' + str(i), 12), 'BODY', body, 1, 1600200, 3200400)]:
            ins('gslides.slides_page_elements', ['presentation_id', 'page_object_id', 'object_id', 'kind', 'text',
                                                 'placeholder_type', 'x_emu', 'y_emu', 'width_emu', 'height_emu', 'table_json', 'ordinal'],
                [fid, sid, oid, 'TEXT_BOX', text, None, 457200, y, 8229600, hgt, None, ordn], f"{fid}#{oid}")


R = lambda *e: [(x, 'reader') for x in e]
# Vincent's flow pass sheet and its legend
GRID = [['#', 'Area', 'What happens', 'Found on', 'Ticket', 'Fix', 'Re-test']]
for n, area, what, found, tk, fix, rt, *_ in RP.R:
    GRID.append([str(n), area, what, found, tk, fix, rt])
SHEET_NOTE = TX['sheet'].split('Note under the table: ', 1)[1]
GRID += [[''] * 7, [SHEET_NOTE] + [''] * 6]
SHEET_SHARES = R(BRI, CAL, LEO, ART)
sheet(ID['sheet'], 'ZM home screen flow pass', GRID, 'Flow pass', ROOT[VIN], VIN, SHEET_SHARES, '2025-09-26T10:12:44Z', AT['sheet'])
doc(ID['legend'], 'How to read my pass sheets', TX['legend'], ROOT[VIN], VIN, SHEET_SHARES, '2025-09-26T10:24:10Z', AT['legend'])
# Arthur's two notes on builds and QA passes
ENG = R(CAL, VIN, OLI, OWE, SAM, BRI, LEO, ROB)
doc(ID['rule_doc'], 'ZM builds and QA passes', TX['rule_doc'], ROOT[ART], ART, ENG, '2025-09-12T22:21:36Z', AT['rule_doc'])
doc(ID['dd_doc'], 'DD hotfix builds and QA passes', TX['dd_doc'], ROOT[ART], ART, ENG, '2025-07-10T15:43:02Z', AT['dd_doc'])
# Calvin's folder and deck
ins('gdrive.drive_files', DF_COLS, [ID['folder'], 'ZM queue manager', FOLDER_MT, js([ROOT[CAL]]), CAL, '[]', '[]', 'private', js([CAL]),
                                    AT['folder'], AT['folder'], False, False], ID['folder'])
DECK = [('ZM queue manager', 'Home screen flow after a level'),
        ('What it orders', 'Tutorials\nLevel-end animations\nTrash in/out animations\nClaimed reward animations\nLive-Ops token animations\nThe order of opening Live-Ops panels'),
        ('Order of events', 'One event at a time. The next one starts when the one before reports it is done.\nTutorials stay blocked until the level-end animations finish.'),
        ('Adding a Live-Op', 'A new Live-Op adds its own order to the queue with EnqueueEvent. Collect & Win is next.')]
deck(ID['deck'], 'ZM queue manager', DECK, ID['folder'], CAL, R(BRI), AT['deck'], AT['deck'])

# ============================================================ Slack
SL_COLS = ['id', 'ts', 'channel_id', 'type', 'user_id', 'text', 'thread_parent_id', 'thread_ts_legacy', 'reply_count',
           'reply_users_count', 'latest_reply', 'is_activity_message', 'subtype', 'reactions_json', 'files_json',
           'attachments_json', 'created_at', 'metadata_json']


def slack(chan_ts, user, text, parent=None, attachments=None):
    ch, ts = chan_ts.split('/')
    mid = hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]
    ins('slack.slack_messages', SL_COLS, [mid, ts, ch, 'message', user, text, parent[0] if parent else None, parent[1] if parent else None,
                                          0, 0, None, False, None, '[]', '[]', js(attachments) if attachments else '[]',
                                          D.datetime.fromtimestamp(float(ts), D.UTC).strftime('%Y-%m-%dT%H:%M:%S.%fZ'), '{}'], chan_ts)
    return mid


amp = lambda s: s.replace('&', '&amp;')
IDS['slack_mid'] = M = {}
BDM, VDM, MDM = 'D0770ET6WBW', 'D06UPGF5PQV', 'D05U73FNDDL'
M['gate_old'] = slack(ID['gate_old'], SLACK_U['brian'], amp(TX['gate_old']))
M['hub_hello'] = slack(f"{BDM}/{ep('2025-09-30T20:39:44Z')}.871309", SLACK_U['brian'], 'Hello!')
M['hub'] = slack(ID['hub'], SLACK_U['brian'], amp(TX['hub']))
# Vincent tells Calvin when the pass starts and when the tickets are in
M['pass_start'] = slack(f"{VDM}/{ep('2025-09-26T10:41:17Z')}.402889", SLACK_U['vincent'],
                        "Brian asked me to do a full pass on the home screen flow after a level. I started a sheet for it today, everything goes in there")
M['pass_tickets'] = slack(f"{VDM}/{ep('2025-09-30T19:33:26Z')}.118549", SLACK_U['vincent'],
                          "flow sheet is up to date. the ticket keys are in it where I opened one")
# Marcus writes in short bursts
f1, f2 = TX['filt_dm'].split(', saw it ', 1)
M['filt_dm'] = slack(ID['filt_dm'], SLACK_U['marcus'], f1)
M['filt_dm2'] = slack(f"{MDM}/{ep(AT['filt_dm']) + 19}.208739", SLACK_U['marcus'], 'saw it ' + f2)
SHADER = ('d0dd5d3ad4658add1f79802e2aa60e48', '1759249488.495439')     # base: Vincent's shader thread, 4 replies by 3 people (Vincent among them)
M['reopen'] = slack(ID['reopen'], SLACK_U['vincent'], TX['reopen'], parent=SHADER)
upd('slack.slack_messages', {'reply_count': 5, 'reply_users_count': 3, 'latest_reply': ID['reopen'].split('/')[1]}, 'id', SHADER[0])
M['back'] = slack(ID['back'], SLACK_U['robert'], TX['back'])

# GitHub app copies in #zombie-prs, under each PR's opened message
PRS = 'C093LEZGF6J'
REPO = 'harmonygames-Games/match3d'
PR_TITLE = {472: '#472 Implement Win&amp;Collect into Queue Manager', 473: '#473 Addressables/sp', 475: '#475 [PERSON_NAME_0029]/animated icons'}
PR_PARENT = {472: ('61f686b8a8b6c164b14aff6b5b1897bf', '1759185399.395419', 3, '1759247586.958099'),
             473: ('d05a2f8a3c4ada2d6b91c809e04222dc', '1759246868.802449', 2, '1759246882.921709'),
             475: ('1389e3c51eeac40d0019f335f34550e4', '1759247948.371729', 3, '1759248557.911919')}


def mirror(key, n, at, frac, login, anchor, body):
    par = PR_PARENT[n]
    ts = f"{ep(at) + 2}.{frac}"
    att = [{"color": "24292f", "fallback": f"[{REPO}] Comment on #{n}", "footer": f"<https://github.com/{REPO}|{REPO}>",
            "footer_icon": "https://slack.github.com/static/img/favicon-neutral.png", "id": 1, "mrkdwn_in": ["text"],
            "pretext": f"<https://github.com/{REPO}/pull/{n}#{anchor}|Comment> on pull request by <https://github.com/{login}|{login}>",
            "text": amp(body), "title": f"<https://github.com/{REPO}/pull/{n}|{PR_TITLE[n]}>", "ts": ep(at)}]
    M[key] = slack(f"{PRS}/{ts}", SLACK_U['bot'], '', parent=(par[0], par[1]), attachments=att)
    upd('slack.slack_messages', {'reply_count': par[2] + 1, 'reply_users_count': 1, 'latest_reply': max(par[3], ts)}, 'id', par[0])


DISC = {472: 'discussion_r2391840517', 475: 'discussion_r2391889164', 473: 'issuecomment-3352803412'}
mirror('mirror_else', 473, AT['else_pr'], '447309', 'oliver.brooks', DISC[473], TX['else_pr'])
mirror('mirror_inline', 472, AT['inline'], '208419', 'arthur.blake', DISC[472], TX['inline'])
mirror('mirror_inline2', 475, AT['inline2'], '611579', 'arthur.blake', DISC[475], TX['inline2'])

# ============================================================ Trello: Leonard's review card on ZM ROADMAP
TA_COLS = ['id', 'type', 'date', '"idMemberCreator"', '"idBoard"', '"idCard"', 'data_json']
V1_NAME, V1_DESC = TX['rev_card_v1'].split('\n\n', 1)
V2_NAME, V2_DESC = TX['rev_card'].split('\n\n', 1)
CARD_ID, SHORT = ID['rev_card'], 'q' + h('card-short', 7)
tid = lambda iso, salt: format(ep(iso), '08x') + hashlib.sha256(('tr:' + salt).encode()).hexdigest()[:16]
T_C, T_U = AT['rev_card_v1'], AT['rev_card_update']
T_D1, T_N2 = plus(T_C, seconds=51), plus(T_U, seconds=-31)
card = lambda **kw: {**kw, "id": CARD_ID, "idShort": 80, "shortLink": SHORT}
BADGES = {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0, "checkItemsChecked": 0,
          "checkItemsEarliestDue": None, "comments": 0, "description": True, "due": None, "dueComplete": False,
          "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False, "location": False, "maliciousAttachments": 0,
          "start": None, "votes": 0}
ins('trello.trello_cards', ['id', 'name', '"idBoard"', '"idList"', '"desc"', 'pos', 'closed', 'due', '"dueComplete"', '"idMembers_json"',
                            '"idLabels_json"', '"idShort"', '"shortLink"', '"shortUrl"', 'url', '"dateLastActivity"', 'cover_json', 'badges_json'],
    [CARD_ID, V2_NAME, BOARD['id'], BACKLOG['id'], V2_DESC, 140737488502784.0, False, None, False, '[]', '[]', 80, None, None,
     f"https://PERSON_6092_TRELLO_USERNAME.com/c/{SHORT}/80-zm-home-screen-flow-review-thu-oct-2", T_U, None, js(BADGES)], CARD_ID)
IDS['trello'] = {'create': ID['rev_card_v1'], 'desc1': tid(T_D1, 'desc1'), 'name2': tid(T_N2, 'name2'), 'update': ID['rev_card_update']}
for aid, typ, at, data in [
    (IDS['trello']['create'], 'createCard', T_C, {"board": BOARD, "card": card(name=V1_NAME), "list": BACKLOG}),
    (IDS['trello']['desc1'], 'updateCard', T_D1, {"board": BOARD, "card": card(desc=V1_DESC, name=V1_NAME), "list": BACKLOG, "old": {"desc": ""}}),
    (IDS['trello']['name2'], 'updateCard', T_N2, {"board": BOARD, "card": card(name=V2_NAME), "list": BACKLOG, "old": {"name": V1_NAME}}),
    (IDS['trello']['update'], 'updateCard', T_U, {"board": BOARD, "card": card(desc=V2_DESC, name=V2_NAME), "list": BACKLOG, "old": {"desc": V1_DESC}}),
]:
    ins('trello.trello_actions', TA_COLS, [aid, typ, at, TR_LEO, BOARD['id'], CARD_ID, js(data)], aid)
upd('trello.trello_boards', {'"dateLastActivity"': T_U}, 'id', BOARD['id'])

# ============================================================ Calendar + invitation mails (INT-11)
GC_COLS = ['event_id', 'calendar_id', 'summary', 'description', 'location', 'start_ts', 'end_ts', 'start_json', 'end_json',
           'organizer_email', 'creator_email', 'attendees_json', 'status', 'visibility', 'transparency', 'rrule_json',
           'recurring_event_id', 'original_start_json', 'sequence', 'created', 'updated', 'hangout_link', 'ical_uid']
EV_SUM = 'ZM home screen flow review'
EV_START, EV_END = '2025-10-02T18:00:00Z', '2025-10-02T18:30:00Z'
EV_DESC1 = 'Agenda is on the roadmap card: Collect & Win and Daily Gift this time.'
EV_DESC2 = 'Agenda is on the roadmap card.'
EV_NOTE = 'Moved up a day. Agenda is on the roadmap card, I changed it, daily gift waits until next week.'
MEET = 'https://meet.google.com/' + '-'.join(''.join('abcdefghijkmnopqrstuvwxyz'[int(h('meet' + str(i) + str(j), 2), 16) % 25] for j in range(k)) for i, k in enumerate((3, 4, 3))) + '?hs=224'
UID = h('uid-review', 32) + '@hg4'
GUESTS = [LEO, BRI, ART, JUL, VIN, CAL]
T_INV1, T_INV2 = AT['invite_v1'], AT['invite_v2']
IDS['evt'] = {}
for cal in GUESTS:
    eid = ID['event'] if cal == CAL else 'evt_' + h('review' + cal, 22)
    att = []
    for e in sorted(GUESTS):
        a = {"email": e, "organizer": e == LEO, "responseStatus": 'accepted' if e == LEO else 'needsAction'}
        if e == cal:
            a["self"] = True
        att.append(a)
    ins('gcal.gcal_events', GC_COLS, [eid, cal, EV_SUM, EV_DESC2, None, EV_START, EV_END, js({"dateTime": EV_START}), js({"dateTime": EV_END}),
                                      LEO, LEO, js(att), 'confirmed', None, 'opaque', '[]', None, None, 1,
                                      plus(T_INV1, seconds=-9), plus(T_INV2, seconds=-6), MEET, UID], eid)
    IDS['evt'][cal] = eid

GM_COLS = ['id', 'thread_id', 'user_email', 'label_ids_json', 'snippet', 'internal_date', 'date', 'size_estimate', 'subject',
           'from_email', 'from_name', 'to_json', 'cc_json', 'bcc_json', 'reply_to_json', 'body_text', 'body_html',
           'headers_json', 'in_reply_to', '"references"', 'mbox_from', 'attachments_meta_json']
# per mailbox: local time zone label, zone line of the mail body, hour offset from UTC, subject suffix (as base invitations in that mailbox end)
BOX = {CAL: ('CST', 'Central Standard Time - El Salvador', -6, CAL), VIN: ('GMT+3', 'Türkiye Time', 3, VIN), BRI: ('GMT+3', 'Türkiye Time', 3, BRI),
       JUL: ('GMT+3', 'Türkiye Time', 3, '[PERSON_NAME_0043]'), ART: ('EDT', 'Eastern Time - New York', -4, ART)}
TO_LINE = [BRI, ART, 'julia <' + JUL + '>', VIN, CAL]
WHO = f"leonard hayes <{LEO}>"


def when(start_iso, off, long):
    s = dt(start_iso) + D.timedelta(hours=off)
    e = s + D.timedelta(minutes=30)
    hm = lambda t: (t.strftime('%I').lstrip('0') + (t.strftime(':%M') if t.minute else '') + t.strftime('%p').lower())
    if long:
        return f"{s.strftime('%A %b')} {s.day}, {s.year} \u22c5 {hm(s)} \u2013 {hm(e)}"
    return f"{s.strftime('%a %b')} {s.day}, {s.year} {hm(s)} - {hm(e)}"


def cal_mail(key, box, at, kind, start_iso, lead, desc):
    tz, zone, off, suffix = BOX[box]
    d0 = dt(at)
    hk = key if box == CAL else key + box
    h0 = lambda x, n: hashlib.sha256(x.encode()).hexdigest()[:n]      # same derivation as plan/build_scenario.py
    mid = "<calendar-%s-%s-%s-%s-%s@google.com>" % (h0('cal:' + hk, 8), h0('cal1:' + hk, 4), h0('cal2:' + hk, 4), h0('cal3:' + hk, 4), h0('cal4:' + hk, 12))
    subject = f"{kind}: {EV_SUM} @ {when(start_iso, off, False)} ({tz}) ({suffix})"
    guests = ''.join(f"{e}\r\n" for e in (BRI, ART, '[PERSON_NAME_0043]', VIN, CAL))
    body = (f"{lead}{EV_SUM}\r\n{when(start_iso, off, True)}\r\n{zone}\r\n\r\nJoin with Google Meet\r\n{MEET}\r\n\r\n{desc}\r\n\r\n"
            f"Organizer\r\nLeonard Hayes\r\n{LEO}\r\n\r\nGuests\r\nLeonard Hayes - organizer\r\n{guests}")
    tnum = str((int(d0.timestamp() * 1000) << 20) | (int(hashlib.sha256(('gm:' + hk).encode()).hexdigest()[:5], 16) & 0xFFFFF))
    tref = f"{box}/{tnum}"
    snippet = ' '.join(body.split())[:140]
    ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [tref, box, snippet, None], tref)
    hdrs = [{"name": "Reply-To", "value": WHO}, {"name": "Sender", "value": "Google Calendar <SVC_0842_EMAIL>"},
            {"name": "Message-ID", "value": mid}, {"name": "Date", "value": email.utils.format_datetime(d0)},
            {"name": "Subject", "value": subject}, {"name": "From", "value": WHO}, {"name": "To", "value": ', '.join(TO_LINE)}]
    ins('gmail.gmail_messages', GM_COLS,
        [f"{box}/{mid}", tref, box, js(["INBOX", "CATEGORY_PERSONAL"]), snippet, int(d0.timestamp() * 1000), at, len(body) + 3000, subject,
         LEO, 'leonard hayes', js(TO_LINE), '[]', '[]', js([WHO]), body, None, js(hdrs), None, None, None, '[]'], f"{box}/{mid}")
    return f"{box}/{mid}", tref


IDS['mail'] = {}
for box in (CAL, VIN, BRI, JUL, ART):
    a = cal_mail('inv1', box, T_INV1, 'Invitation', '2025-10-03T18:00:00Z', '', EV_DESC1)
    b = cal_mail('inv2', box, T_INV2, 'Updated invitation with note', EV_START,
                 f'This event has been updated with a note:\r\n"{EV_NOTE}"\r\nChanged: time, description\r\n\r\n\r\n', EV_DESC2)
    IDS['mail'][box] = {'inv1': a[0], 'inv1_thread': a[1], 'inv2': b[0], 'inv2_thread': b[1]}
assert IDS['mail'][CAL]['inv1'] == ID['invite_v1'] and IDS['mail'][CAL]['inv2'] == ID['invite_v2'], (IDS['mail'][CAL], ID['invite_v1'])

# ============================================================ GitHub: Arthur's two inline comments, Oliver's comment on his own PR
HUNK = {472: ("Assets/RewardVFXManager.cs",
              "@@ -142,11 +146,18 @@ private IEnumerator PlayVFX(RewardVFXRequest req)\n         yield return new WaitForSeconds(0.2f);\n \n"
              "+        if (_collectAndWinProgressController != null)\n+        {\n"
              "+            yield return _collectAndWinProgressController.GetCollectAndWinStatusRoutine();\n+        }\n+\n"
              "+        float waited = 0f;\n+        yield return new WaitUntil(() => _activeVFX == 0 || (waited += Time.deltaTime) > _vfxTimeout);\n"
              "         yield return new WaitForSeconds(0.3f);",
              "+        yield return new WaitUntil(() => _activeVFX == 0 || (waited += Time.deltaTime) > _vfxTimeout);"),
        475: ("Assets/Scripts/Object/Effects/Upgrades/CardPackOpenScreen.cs",
              "@@ -88,6 +96,24 @@ public void CloseScreen()\n+        closeButton.interactable = false;\n+        StartCoroutine(CloseAfterAnimations());\n+    }\n+\n"
              "+    private IEnumerator CloseAfterAnimations()\n+    {\n+        foreach (var card in _cards)\n+        {\n"
              "+            card.GetComponent<TokenTweenPath>().Restart();\n+        }\n+\n"
              "+        tapAnywhereToCollect.SetActive(false);\n+        cardBackground.SetActive(false);\n+        title.SetActive(false);",
              "+        title.SetActive(false);")}
GH_THREAD = {472: ('calvin.price@harmonygames.co/1844639618018823785', 'Implement Win&Collect into Queue Manager', '0476', '3285698310'),
             475: ('calvin.price@harmonygames.co/1844705205220700048', '[PERSON_NAME_0029]/animated icons', '1254', '3285755391')}
IDS['gh'] = {}
for n, key in ((472, 'inline'), (475, 'inline2')):
    pr = f"{REPO}#{n}"
    path, hunk, last = HUNK[n]
    at = AT[key]
    rev = f"{pr}#rev_2"
    ins('github.github_reviews', ['id', 'pr_id', 'author_login', 'state', 'body', 'submitted_at', 'commit_id', 'seq'],
        [rev, pr, GH['arthur'], 'COMMENTED', '', at, None, 2], rev)
    ins('github.github_review_comments', ['id', 'pr_id', 'author_login', 'body', 'path', 'diff_hunk', 'line', 'position', 'commit_id',
                                          'in_reply_to_id', 'created_at', 'seq'],
        [ID[key], pr, GH['arthur'], TX[key], path, hunk, None, None, None, None, at, 1], ID[key])
    # GitHub's mail to the PR author joins the base notification thread for the PR (INT-12)
    thread, title, alias, revno = GH_THREAD[n]
    root = f"<[SOURCE_ORG_0001]-Games/match3d/pull/{n}@github.com>"
    msgid = f"<[SOURCE_ORG_0001]-Games/match3d/pull/{n}/review/{revno}@github.com>"
    subj = f"Re: [[SOURCE_ORG_0001]-Games/match3d] {title} (PR #{n})"
    body = (f"@arthur.blake commented on this pull request.\r\n\r\n\r\n\r\n> {last}\r\n\r\n{TX[key]}\r\n\r\n-- \r\n"
            f"Reply to this email directly or view it on github:\r\nhttps://github.com/[SOURCE_ORG_0001]-Games/match3d/pull/{n}#{DISC[n]}\r\n"
            f"You are receiving this because you authored the thread.\r\n\r\nMessage ID: {msgid}")
    sent = plus(at, seconds=19)   # base: approval 15:52:58Z, its mail 15:53:19Z
    d0 = dt(sent)
    mail_id = f"{CAL}/{msgid}"
    ins('gmail.gmail_messages', GM_COLS,
        [mail_id, thread, CAL, js(["INBOX", "IMPORTANT", "CATEGORY_PERSONAL", "UNREAD"]), ' '.join(body.split())[:140],
         int(d0.timestamp() * 1000), sent, len(body) + 3000, subj, 'SVC_0248_EMAIL', 'SVC_0248_NAME',
         js(["SVC_3649_NAME <SVC_3649_EMAIL>"]), js([f"calvin <{CAL}>", "SVC_0613_NAME <SVC_0613_EMAIL>"]), '[]',
         js([f"SVC_5111_NAME <SVC_5111_EMAIL_PLUS_ALIAS_{alias}>"]), body, None,
         js([{"name": "Message-ID", "value": msgid}, {"name": "Date", "value": email.utils.format_datetime(d0)},
             {"name": "Subject", "value": subj}, {"name": "From", "value": "SVC_0248_NAME <SVC_0248_EMAIL>"},
             {"name": "To", "value": "SVC_3649_NAME <SVC_3649_EMAIL>"},
             {"name": "Cc", "value": f"calvin <{CAL}>, SVC_0613_NAME <SVC_0613_EMAIL>"},
             {"name": "In-Reply-To", "value": root}, {"name": "References", "value": root}]), None, None, None, '[]'], mail_id)   # the PR's root mail is not in the export, so the two columns stay NULL as on no base row they could point at
    IDS['gh'][key] = {'review': rev, 'comment': ID[key], 'mail': mail_id}
    upd('github.github_pull_requests', {'updated_at': at}, 'id', pr)     # the comment is later than the merge that last touched the PR
PR473 = f"{REPO}#473"
ins('github.github_pr_comments', ['id', 'pr_id', 'author_login', 'body', 'created_at', 'updated_at'],
    [ID['else_pr'], PR473, GH['oliver'], TX['else_pr'], AT['else_pr'], None], ID['else_pr'])
ins('github.github_timeline_events', ['id', 'pr_id', 'event', 'actor_login', 'created_at', 'data_json'],
    [PR473 + '#ev_5', PR473, 'commented', GH['oliver'], AT['else_pr'], '{}'], PR473 + '#ev_5')

# ============================================================ Linear
LI_COLS = ['id', 'project_id', 'team_id', 'parent_id', 'assignee_id', 'creator_id', 'state_id', 'cycle_id', 'identifier', 'number', 'title',
           'description', 'priority', 'estimate', 'due_date', 'started_at', 'completed_at', 'canceled_at', 'archived_at',
           'time_in_status_minutes', 'labels_json', 'links_json', 'relations_json', 'state_history_json', 'is_archived', 'created_at', 'updated_at']
ROWTXT = {r[0]: r for r in RP.R}
# ticket: (sheet row, assignee, priority, filed at, description, [(minutes after filing, who, comment)])
TICKETS = {
 'ZOM-567': (4, 'oliver', 1, '2025-09-30T16:43:18Z', "At level 20 the win streak tutorial starts and the home screen stops taking taps. I have to kill the app.\n\nSeen on Android 1974.",
             [(3, 'vincent', "Happens every time on a fresh account for me."), (58, 'oliver', "can't get it on my phone yet, I'll try with a fresh account tomorrow")]),
 'ZOM-568': (6, 'calvin', 2, '2025-09-30T16:49:52Z', "If I tap play right after a level, the pre-level panel is open and the level-end coins are still flying over it.\n\nSeen on Android 1974.",
             [(2, 'vincent', "Only when I tap play really fast after the level.")]),
 'ZOM-569': (8, 'calvin', 3, '2025-09-30T16:55:07Z', "On tablets the stars from the level fly to the top left corner, not to the star counter.\n\nSeen on Android Submission 129.",
             [(4, 'vincent', "Tab S7 and the old iPad both. Phones are fine.")]),
 'ZOM-570': (10, 'calvin', 2, '2025-09-30T17:01:33Z', "The daily gift calendar opens while the level-end coins are still playing. It should wait for them.\n\nSeen on Android 1984.",
             [(2, 'vincent', "Still the same on Android 2013 today.")]),
 'ZOM-571': (12, 'calvin', 3, '2025-09-30T17:06:41Z', "Every time a panel closes on the home screen, the season pass icon plays its animation from the start.\n\nSeen on Android 1984.",
             [(1, 'vincent', "I was told this went into #472. Not re-tested yet.")]),
 'ZOM-572': (13, 'oliver', 2, '2025-09-30T17:13:09Z', "The season pass start popup comes again after every level until I claim it. It should show once.\n\nSeen on iOS Internal 1727.",
             [(3, 'vincent', "It stops once you claim. Until then it is after every single level.")]),
 'ZOM-573': (14, 'oliver', 3, '2025-09-30T17:18:46Z', "After I come back from the shop, the reward claim animation of the season pass plays two times.\n\nSeen on iOS Internal 1745.",
             [(2, 'vincent', "Only when coming back from the shop, not from a level."), (47, 'oliver', "I have this one on my branch, no PR for it yet")]),
 'ZOM-574': (15, 'owen', 2, '2025-09-30T17:26:12Z', "The Collect & Win bar starts filling while the daily gift popup is still open on top of it.\n\nSeen on Android 2013.",
             [(2, 'vincent', "The bar should wait until the gift popup is closed."), (39, 'owen', "ok, I'll look at it after the analytics ticket")]),
 'ZOM-575': (16, None, 3, '2025-09-30T17:31:58Z', "The Endless unlock banner shows again when I come back from a level. It should show one time.\n\nSeen on Android 2006.",
             [(2, 'vincent', "Every time I come back, not only the first one.")]),
 'ZOM-576': (18, 'calvin', 2, '2025-09-30T17:38:24Z', "On the first unlock, the Collect & Win panel opens on top of the level-end rewards.\n\nSeen on iOS Internal 1750.",
             [(1, 'vincent', "I was told #472 has this. Not re-tested yet.")]),
 'ZOM-577': (19, 'owen', 2, '2025-09-30T17:44:37Z', "The Collect & Win progress popup opens before the level-end coins finish.\n\nSeen on Android 2013.",
             [(3, 'vincent', "Same level every time, the popup is early."), (41, 'owen', "I have a fix locally, need to test it before I open the PR")]),
 'ZOM-578': (21, 'samuel', 2, '2025-09-30T17:52:03Z', "After a win the streak counter goes up by two when other panels are waiting to open.\n\nSeen on iOS Internal 1745.",
             [(2, 'vincent', "For example from 3 to 5. After a restart the number is right."), (64, 'samuel', "looks like the counter runs twice when the queue plays, checking")]),
 'ZOM-579': (28, None, 3, '2025-09-30T17:58:29Z', "The Endless unlock banner and the daily gift open on top of each other.\n\nSeen on Android 1984.",
             [(2, 'vincent', "You can't tap the gift until the banner goes away.")]),
 'ZOM-580': (30, None, 2, '2025-09-30T18:14:51Z', "The Endless reward chest opens while the coins are still flying.\n\nSeen on Android 2006.",
             [(2, 'vincent', "The chest should wait for the coins to land.")]),
 'ZOM-581': (32, 'calvin', 3, '2025-09-30T18:21:16Z', "When a pack closes, the pack opening sound keeps playing on the home screen.\n\nSeen on iOS Internal 1746.",
             [(1, 'vincent', "I was told #475 has it. Not re-tested yet.")]),
 'ZOM-582': (34, 'calvin', 3, '2025-09-30T18:27:44Z', "The pack count on the home button does not change after opening packs. It is right after a restart.\n\nSeen on Android 2006.",
             [(2, 'vincent', "Opened 2 packs and the button still said 3 until I restarted.")]),
 'ZOM-583': (36, 'calvin', 1, '2025-09-30T18:36:02Z', "Right after an app update, the first level I finish shows no level-end rewards at all.\n\nSeen on Android Submission 129.",
             [(3, 'vincent', "Only the first level after the update. After that it is fine."), (52, 'brian', "This one is important for the store update, please look at it first")]),
 'ZOM-584': (37, 'calvin', 2, '2025-09-30T18:44:35Z', "The win streak freezer popup opens behind the season pass popup.\n\nSeen on iOS Internal 1745.",
             [(2, 'vincent', "The freezer popup is there, you only see it after you close the pass one.")]),
}
assert {k: ROWTXT[v[0]][4] for k, v in TICKETS.items()} == {k: k for k in TICKETS}, 'ticket keys must match the sheet rows'
cid = lambda label: 'comment_' + h(label, 32)
COMMENTS = {}


def comment(issue, at, who, body, c):
    COMMENTS.setdefault(issue, []).append((at, LIN[who], body, c))


for key, (row, who, prio, at, desc, cs) in TICKETS.items():
    state = RP.SEEDED_STATE.get(key, 'Todo')
    for i, (mins, author, body) in enumerate(cs):
        comment(key, plus(at, minutes=mins, seconds=7 + int(h('cs' + key + str(i), 4), 16) % 50), author, body, cid(f'c-{key}-{i}'))
    last = max(c[0] for c in COMMENTS[key])
    ins('linear.linear_issues', LI_COLS,
        [key, None, 'team_ZOM', None, LIN[who] if who else None, LIN['vincent'], state, None, key, int(key.split('-')[1]), ROWTXT[row][2], desc,
         prio, None, None, at if state == 'In Validation' else None, None, None, None, None, '["Bug"]', '[]', '[]', '[]', False, at, last], key)
comment('ZOM-543', AT['epic_note'], 'brian', TX['epic_note'], ID['epic_note'])
comment('ZOM-556', AT['alias_gift'], 'vincent', TX['alias_gift'], ID['alias_gift'])
comment('ZOM-560', AT['alias_streak'], 'vincent', TX['alias_streak'], ID['alias_streak'])
for iss in sorted(COMMENTS, key=lambda x: int(x.split('-')[1])):
    for i, (at, author, body, c) in enumerate(sorted(COMMENTS[iss]), 1):
        ins('linear.linear_comments', ['id', 'issue_id', 'author_id', 'parent_id', 'body', 'is_edited', 'created_at', 'updated_at', 'sequence'],
            [c, iss, author, None, body, False, at, at, i], c)
for k, key in (('ZOM-543', 'epic_note'), ('ZOM-556', 'alias_gift'), ('ZOM-560', 'alias_streak')):
    upd('linear.linear_issues', {'updated_at': AT[key]}, 'id', k)
IDS['comments'] = {k: [c[3] for c in sorted(v)] for k, v in COMMENTS.items()}
IDS['tickets'] = {k: {'row': v[0], 'assignee': v[1], 'state': RP.SEEDED_STATE.get(k, 'Todo'), 'created': v[3]} for k, v in TICKETS.items()}

# ============================================================ write
order_s = ['gdrive', 'gdocs', 'gsheets', 'gslides', 'slack', 'trello', 'gcal', 'gmail', 'github', 'linear']
n_ins = sum(1 for s in OUT for x in OUT[s] if x.startswith('INSERT'))
n_upd = sum(1 for s in OUT for x in OUT[s] if x.startswith('UPDATE'))
head = ['-- Are you planning to inject? Yes',
        f'-- HarmonyGames injection - persona Calvin Price <{CAL}> (Game Engineer (Unity VFX)), Long Horizon, Oct 1, 2025 universe.',
        f'-- Services: {", ".join(order_s)}. Statements: {n_ins} INSERT (one row each), {n_upd} UPDATE.',
        '-- Literal values only; parents before children; re-apply this exact SQL before every agent run.', 'BEGIN;']
body = []
for s in order_s:
    body.append(f'-- {s}')
    body += OUT.get(s, [])
(TI / '01_Universe_Inject.sql').write_text('\n'.join(head + body + ['COMMIT;']) + '\n')
json.dump({'ids': IDS, 'rows': ROWS}, open(HERE / 'sql_ids.json', 'w'), indent=1, ensure_ascii=False)
print(n_ins, 'INSERT', n_upd, 'UPDATE', {k: len(v) for k, v in ROWS.items()})
print('comments', sum(len(v) for v in COMMENTS.values()))
