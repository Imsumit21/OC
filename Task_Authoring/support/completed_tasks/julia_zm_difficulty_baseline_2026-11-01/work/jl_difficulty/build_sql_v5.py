"""Builds task_inputs/01_Universe_Inject.sql for the Julia difficulty baseline register (design v4).

Read-only on the base; writes only under Task_Authoring-2/. Never executes SQL. Every id and planned wording comes from
minted_ids.json / planned_text.json / truth.json (build_design.py).
"""
import base64
import datetime as D
import email.utils
import hashlib
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WS = ROOT.parent
P = json.load(open(HERE / 'planned_text.json'))
M = json.load(open(HERE / 'minted_ids.json'))
T = json.load(open(HERE / 'truth.json'))
LIN = json.load(open(WS / 'HarmonyGames_Other_Services/Services_Data/linear/data.json'))
ISSUES = {i['identifier']: i for i in LIN['issues']}

JL, LEO, ROB, ART, BRI, OLI = ('julia.lawson@harmonygames.co', 'leonard.hayes@harmonygames.co', 'robert@harmonygames.co',
                               'arthur.blake@harmonygames.co', 'brian.foster@harmonygames.co', 'oliver.brooks@harmonygames.co')
NAMES = {JL: 'Julia Lawson', LEO: 'Leonard Hayes', ROB: 'Robert', ART: 'Arthur Blake', BRI: 'Brian Foster', OLI: 'Oliver Brooks'}
VIN = 'vincent.parker@harmonygames.co'
SLACK_U = {LEO: 'EMPLOYEE_0038_SLACK_ID', BRI: 'EMPLOYEE_0026_SLACK_ID', VIN: 'EMPLOYEE_0012_SLACK_ID', ART: 'EMPLOYEE_0025_SLACK_ID'}
ROOTS = {LEO: 'd_63fffeb4fab5233ed5bb73', JL: 'd_8140f09bf9f1b94cb8ee2d', ROB: 'd_9f7ba94f7526d54d8482ba'}
TR_LEO = 'PERSON_6094_TRELLO_USER_ID'
ZM_BOARD = {'id': '6851a6569f3bf818760632ab', 'name': 'ZM ROADMAP', 'shortLink': 'HSqnngwQ'}
OCT21 = {'id': '6851a677e090018224fb8c7f', 'name': 'Oct 21'}
DD_BOARD = {'id': '65eb4ec525346c8070ca638f', 'name': 'Product Roadmap', 'shortLink': 'Yg3yTuCR'}
MARAPR = {'id': '65eb4f4e26cfce07d665a38e', 'name': 'Rebirth (June)'}
CLOCK = '2025-10-01T00:00:00Z'


def h(seed, n):
    return hashlib.sha256(seed.encode()).hexdigest()[:n]


def ts_of(s):
    return D.datetime.fromisoformat(s.replace('Z', '+00:00')).timestamp()


def q(v):
    if v is None:
        return 'NULL'
    if isinstance(v, bool):
        return 'true' if v else 'false'
    if isinstance(v, (int, float)):
        return repr(v)
    s = str(v)
    if '\n' in s or '\\' in s:
        return "E'" + s.replace('\\', '\\\\').replace("'", "''").replace('\n', '\\n') + "'"
    return "'" + s.replace("'", "''") + "'"


def js(x):
    return json.dumps(x, ensure_ascii=False)


OUT, ROWS = {}, {}


def ins(table, cols, vals, key):
    OUT.setdefault(table.split('.')[0], []).append(f"INSERT INTO {table} ({', '.join(cols)})\nVALUES ({', '.join(q(v) for v in vals)});")
    ROWS.setdefault(table, []).append(key)


def upd(table, sets, key_col, key):
    s = ', '.join(f"{c} = {q(v)}" for c, v in sets.items())
    OUT.setdefault(table.split('.')[0], []).append(f"UPDATE {table} SET {s} WHERE {key_col} = {q(key)};")
    ROWS.setdefault(table + ' (UPDATE)', []).append(key)


# =========================================================== Drive / Docs / Sheets
DF_COLS = ['id', 'name', 'mime_type', 'parents_json', 'owner_email', 'shared_with_emails_json', 'shared_roles_json',
           'visibility', 'owners_json', 'modified_time', 'created_time', 'trashed', 'starred']
FOLDER, SHEET, DOC = 'application/vnd.google-apps.folder', 'application/vnd.google-apps.spreadsheet', 'application/vnd.google-apps.document'


def drive(fid, name, mime, parent, owner, shares, created, modified):
    ins('gdrive.drive_files', DF_COLS, [fid, name, mime, js([parent]), owner, js([e for e, _ in shares]),
                                        js([{'email': e, 'role': r} for e, r in shares]), 'private', js([owner]),
                                        modified, created, False, False], fid)


FID = M['FOLDER_ZMDIFF']['id']
drive(FID, P['FOLDER_ZMDIFF_NAME'], FOLDER, ROOTS[LEO], LEO, [(JL, 'writer')], M['FOLDER_ZMDIFF']['at'], M['FOLDER_ZMDIFF']['at'])

# --- agenda doc (Leonard; shared with the session attendees)
AG = M['DOC_AGENDA']
AG_TEXT = P['DOC_AGENDA_TITLE'] + '\n' + P['DOC_AGENDA_BODY']
ag_shares = [(JL, 'reader'), (ROB, 'reader'), (ART, 'reader'), (BRI, 'reader')]
drive(AG['id'], P['DOC_AGENDA_TITLE'], DOC, FID, LEO, ag_shares, AG['created'], AG['at'])
tl = len(P['DOC_AGENDA_TITLE']) + 1
runs = [{'start': 0, 'end': tl, 'named_style': 'TITLE', 'list_id': None, 'list_nesting': 0},
        {'start': tl, 'end': len(AG_TEXT), 'named_style': 'NORMAL_TEXT', 'list_id': None, 'list_nesting': 0}]
ins('gdocs.docs_documents', ['document_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility', 'body_text',
                             'style_runs_json', 'revision_id', 'drive_file_id', 'created_time', 'modified_time'],
    [AG['id'], P['DOC_AGENDA_TITLE'], LEO, js([e for e, _ in ag_shares]), 'private', AG_TEXT, js(runs), h('rev' + AG['id'], 10),
     AG['id'], AG['created'], AG['at']], AG['id'])

# --- monster enrage sheet (Julia's; three tabs)
SH = M['SHEET_KNOBS']
sh_shares = [(ART, 'reader'), (ROB, 'reader'), (LEO, 'reader')]
drive(SH['id'], P['SHEET_KNOBS_TITLE'], SHEET, FID, JL, sh_shares, SH['created'], SH['at'])
ins('gsheets.sheets_spreadsheets', ['spreadsheet_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility',
                                    'drive_file_id', 'created_time', 'modified_time'],
    [SH['id'], P['SHEET_KNOBS_TITLE'], JL, js([e for e, _ in sh_shares]), 'private', SH['id'], SH['created'], SH['at']], SH['id'])
for i, tname in enumerate(['Live', 'Next pass', 'History']):
    grid = P['SHEET_KNOBS_TABS'][tname]
    ins('gsheets.sheets_sheets', ['spreadsheet_id', 'sheet_id', 'title', '"index"', 'row_count', 'column_count', 'grid_json'],
        [SH['id'], i, tname, i, 1000, 26, js(grid)], f"{SH['id']}#{i}")

# =========================================================== Slides (Robert's tier write-up; /injection F1: no Confluence)
C = M['CONF_DDA']
DECK_SHARES = [(JL, 'reader'), (LEO, 'reader'), (ART, 'reader'), (BRI, 'reader')]
drive(C['id'], P['CONF_DDA_TITLE'], 'application/vnd.google-apps.presentation', ROOTS[ROB], ROB, DECK_SHARES, C['at'], C['at'])
ins('gslides.slides_presentations', ['presentation_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility',
                                     'drive_file_id', 'revision_id', 'created_time', 'modified_time'],
    [C['id'], P['CONF_DDA_TITLE'], ROB, js([e for e, _ in DECK_SHARES]), 'private', C['id'], C['id'][2:12], C['at'], C['at']], C['id'])
lines = P['CONF_DDA_BODY'].split('\n')
slide_text = [P['CONF_DDA_TITLE'] + '\n' + lines[0], '\n'.join(lines[1:4]), lines[4] if len(lines) > 4 else '']
for i, (sid, eid, txt) in enumerate(zip(C['slides'], C['elements'], slide_text)):
    ins('gslides.slides_pages', ['presentation_id', 'object_id', '"index"', 'layout', 'notes'], [C['id'], sid, i, 'BLANK', None], f"{C['id']}#{sid}")
    ins('gslides.slides_page_elements', ['presentation_id', 'page_object_id', 'object_id', 'kind', 'text', 'placeholder_type',
                                         'x_emu', 'y_emu', 'width_emu', 'height_emu', 'table_json', 'ordinal'],
        [C['id'], sid, eid, 'TEXT_BOX', txt, None, 0, 0, 9144000, 5143500, None, 0], f"{C['id']}#{eid}")

# =========================================================== Slack
SL_COLS = ['id', 'ts', 'channel_id', 'type', 'user_id', 'text', 'thread_parent_id', 'thread_ts_legacy', 'reply_count',
           'reply_users_count', 'latest_reply', 'is_activity_message', 'subtype', 'reactions_json', 'files_json',
           'attachments_json', 'created_at', 'metadata_json']


def slack(mid, ts, ch, user, text, at, parent=None, attachments='[]'):
    ins('slack.slack_messages', SL_COLS, [mid, ts, ch, 'message', user, text, parent[0] if parent else None,
                                          parent[1] if parent else None, 0, 0, None, False, None, '[]', '[]', attachments,
                                          at, '{}'], f'{ch}/{ts}')


for k, who in [('S_ASK', LEO), ('S_ROBERT_SUM', BRI), ('S_BRIAN_POST', VIN)]:
    m = M[k]
    slack(m['id'], m['ts'], m['channel'], SLACK_U[who], P[k], m['at'])
cc = M['CC_ART']
slack(cc['id'], cc['ts'], cc['channel'], SLACK_U[ART], P['CC_ART_BODY'], cc['at'])

# GitHub-app mirror of Blake's #401 comment (INT-01), threaded under #401's opened post
PARENT_401 = ('1c181040768a5650a30ad1e68cf1b9b4', '1756140111.461039')
mm = M['S_MIRROR_401']
c401 = M['PRC_244']
att = [{"color": "24292f", "fallback": "[harmonygames-Games/match3d] Comment on #401",
        "footer": "<https://github.com/harmonygames-Games/match3d|harmonygames-Games/match3d>",
        "footer_icon": "https://slack.github.com/static/img/favicon-neutral.png", "id": 1, "mrkdwn_in": ["text"],
        "pretext": "<https://github.com/harmonygames-Games/match3d/pull/401#issuecomment-3221048112|Comment> on pull request by "
                   "<https://github.com/arthur.blake|arthur.blake>",
        "text": P['PRC_244_BODY'],
        "title": "<https://github.com/harmonygames-Games/match3d/pull/401|#401 Split enrage parameter into separate ones>",
        "ts": int(ts_of(c401['at']))}]
slack(mm['id'], mm['ts'], 'C093LEZGF6J', 'SLACK_BOT_0004_SLACK_ID', '', mm['at'], parent=PARENT_401, attachments=js(att))
upd('slack.slack_messages', {'reply_count': 3, 'reply_users_count': 1, 'latest_reply': mm['ts']}, 'id', PARENT_401[0])

# =========================================================== Trello
TC_COLS = ['id', 'name', '"idBoard"', '"idList"', '"desc"', 'pos', 'closed', 'due', '"dueComplete"', '"idMembers_json"',
           '"idLabels_json"', '"idShort"', '"shortLink"', '"shortUrl"', 'url', '"dateLastActivity"', 'cover_json', 'badges_json']
TA_COLS = ['id', 'type', 'date', '"idMemberCreator"', '"idBoard"', '"idCard"', 'data_json']


def badges(comments):
    return {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0,
            "checkItemsChecked": 0, "checkItemsEarliestDue": None, "comments": comments, "description": True,
            "due": None, "dueComplete": False, "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False,
            "location": False, "maliciousAttachments": 0, "start": None, "votes": 0}


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def shortlink(seed):
    return base64.b64encode(hashlib.sha256(seed.encode()).digest()).decode().replace('+', 'x').replace('/', 'Q')[:8]


CARDINFO = {}
for ck, ak, name, desc, board, lst, short, pos, last, ncom in [
        ('T_H1CARD', 'T_H1CREATE', P['H1_TITLE'], P['H1_DESC'], ZM_BOARD, OCT21, 80, 140737488486400.0, M['T_H1CMT']['at'], 1),
        ('T_DDCARD', 'T_DDCREATE', P['DD_TITLE'], P['DD_DESC'], DD_BOARD, MARAPR, 211, 98400.0, M['T_DDCARD']['at'], 0)]:
    cid = M[ck]['id']
    sl = shortlink(cid)
    CARDINFO[ck] = (cid, short, name, sl, board, lst)
    url = f"https://PERSON_6092_TRELLO_USERNAME.com/c/{sl}/{short}-{slug(name)}"
    ins('trello.trello_cards', TC_COLS, [cid, name, board['id'], lst['id'], desc, pos, False, None, False, '[]', '[]',
                                         short, None, None, url, last, None, js(badges(ncom))], cid)
    ins('trello.trello_actions', TA_COLS, [M[ak]['id'], 'createCard', M[ak]['at'], TR_LEO, board['id'], cid, js(
        {"board": board, "card": {"id": cid, "idShort": short, "name": name, "shortLink": sl}, "list": lst})], M[ak]['id'])
cid, short, name, sl, board, lst = CARDINFO['T_H1CARD']
ins('trello.trello_actions', TA_COLS, [M['T_H1CMT']['id'], 'commentCard', M['T_H1CMT']['at'], TR_LEO, board['id'], cid,
                                       js({"board": board, "card": {"id": cid, "idShort": short, "name": name, "shortLink": sl},
                                           "idCard": cid, "list": lst, "text": P['H1_CMT'], "textData": {"emoji": {}}})],
    M['T_H1CMT']['id'])

# =========================================================== Gmail (Blake -> Julia, Leonard, Robert, Brian; copy per mailbox)
GM_COLS = ['id', 'thread_id', 'user_email', 'label_ids_json', 'snippet', 'internal_date', 'date', 'size_estimate', 'subject',
           'from_email', 'from_name', 'to_json', 'cc_json', 'bcc_json', 'reply_to_json', 'body_text', 'body_html',
           'headers_json', 'in_reply_to', '"references"', 'mbox_from', 'attachments_meta_json']
TO = [JL, LEO, ROB, BRI]
BOXES = [JL, LEO, ROB, BRI, ART]
INBOX = ["INBOX", "IMPORTANT", "CATEGORY_PERSONAL"]
GTHREADS = {}


def mail(key, subject, body_text, reply_to_key=None, thread_snippet=None):
    at = M[key]['at']
    dt = D.datetime.fromisoformat(at.replace('Z', '+00:00'))
    ms = int(dt.timestamp() * 1000)
    msgid = M[key]['message_id']
    parent_id = M[reply_to_key]['message_id'] if reply_to_key else None
    body = body_text.replace('\n', '\r\n')
    snippet = ' '.join(body_text.split())[:140]
    to_hdr = ', '.join(f"{NAMES[e]} <{e}>" for e in TO)
    hdrs = [{"name": "Message-ID", "value": msgid}, {"name": "Date", "value": email.utils.format_datetime(dt)},
            {"name": "Subject", "value": subject}, {"name": "From", "value": f"{NAMES[ART]} <{ART}>"},
            {"name": "To", "value": to_hdr}]
    if parent_id:
        hdrs += [{"name": "In-Reply-To", "value": parent_id}, {"name": "References", "value": parent_id}]
    GTHREADS[key] = {}
    for box in BOXES:
        labels = ["SENT"] if box == ART else INBOX
        if reply_to_key:
            tref = GTHREADS[reply_to_key][box]
        else:
            tid = M[key]['gmail_id'] if box == JL else str(ms << 20 | int(h('g' + box + at, 5), 16) & 0xFFFFF)
            tref = f"{box}/{tid}"
            ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [tref, box, thread_snippet or snippet, None], tref)
        GTHREADS[key][box] = tref
        ins('gmail.gmail_messages', GM_COLS,
            [f"{box}/{msgid}", tref, box, js(labels), snippet, ms, at, len(body) + 900, subject, ART, NAMES[ART],
             js([f"{NAMES[e]} <{e}>" for e in TO]), '[]', '[]', '[]', body, None, js(hdrs), parent_id, parent_id, None, '[]'],
            f"{box}/{msgid}")


mail('G_BUILD', P['G_BUILD_SUBJECT'], P['G_BUILD_BODY'], thread_snippet=' '.join(P['G_BUILD_RE_BODY'].split())[:140])
mail('G_BUILD_RE', 'Re: ' + P['G_BUILD_SUBJECT'], P['G_BUILD_RE_BODY'], reply_to_key='G_BUILD')

# =========================================================== GCal (one copy per attendee calendar; no invitation mails)
GC = M['GCAL_TUNING']
att_order = [LEO, JL, ROB, ART, BRI]
GC_COLS = ['event_id', 'calendar_id', 'summary', 'description', 'location', 'start_ts', 'end_ts', 'start_json', 'end_json',
           'organizer_email', 'creator_email', 'attendees_json', 'status', 'visibility', 'transparency', 'rrule_json',
           'recurring_event_id', 'original_start_json', 'sequence', 'created', 'updated', 'hangout_link', 'ical_uid']
for cal in att_order:
    attl = []
    for e in att_order:
        a = {"email": e, "organizer": e == LEO, "responseStatus": "accepted" if e in (LEO, ROB) else "needsAction"}
        if e == cal:
            a["self"] = True
        attl.append(a)
    ins('gcal.gcal_events', GC_COLS, [GC['copies'][cal], cal, P['GCAL_SUMMARY'], None, None, GC['start'], GC['end'],
                                      js({"dateTime": GC['start']}), js({"dateTime": GC['end']}), LEO, LEO, js(attl), 'confirmed',
                                      None, 'opaque', '[]', None, None, 0, GC['created'], GC['at'], None, GC['ical_uid']],
        GC['copies'][cal])

# =========================================================== GitHub: Blake's comment on match3d#401
ins('github.github_pr_comments', ['id', 'pr_id', 'author_login', 'body', 'created_at', 'updated_at'],
    [c401['id'], c401['pr'], c401['author'], P['PRC_244_BODY'], c401['at'], c401['at']], c401['id'])
ins('github.github_timeline_events', ['id', 'pr_id', 'event', 'actor_login', 'created_at', 'data_json'],
    [c401['timeline_event'], c401['pr'], 'commented', c401['author'], c401['at'], '{}'], c401['timeline_event'])

# =========================================================== Linear comments (one note per candidate)
LC_COLS = ['id', 'issue_id', 'author_id', 'parent_id', 'body', 'is_edited', 'created_at', 'updated_at', 'sequence']
LINROWS = {}
for k, n in sorted(M['LIN_NOTES'].items(), key=lambda x: int(x[0].split('-')[1])):
    iss = ISSUES[k]
    assert iss['created_at'] < n['at'] < CLOCK, (k, n['at'])
    ins('linear.linear_comments', LC_COLS, [n['id'], k, n['author'], None, n['text'], False, n['at'], n['at'], 1], n['id'])
    LINROWS[k] = n
    if n['at'] > iss['updated_at']:
        upd('linear.linear_issues', {'updated_at': n['at']}, 'id', k)

# =========================================================== write
order = ['gdrive', 'gdocs', 'gsheets', 'gslides', 'slack', 'trello', 'gmail', 'gcal', 'github', 'linear']
n_ins = sum(1 for s in OUT for x in OUT[s] if x.startswith('INSERT'))
n_upd = sum(1 for s in OUT for x in OUT[s] if x.startswith('UPDATE'))
head = ['-- Are you planning to inject? Yes',
        f'-- HarmonyGames injection - persona Julia Lawson <{JL}> (Product Manager), Long Horizon.',
        f'-- Services: {", ".join(order)}. Statements: {n_ins} INSERT (one row each), {n_upd} UPDATE.',
        '-- Literal values only; parents before children; re-apply this exact SQL before every agent run.', 'BEGIN;']
body = []
for s in order:
    body.append(f'-- ===================== {s.upper()} =====================')
    body += OUT.get(s, [])
(ROOT / 'task_inputs/01_Universe_Inject.sql').write_text('\n'.join(head + body + ['COMMIT;']) + '\n')
json.dump({'rows': ROWS, 'gmail_threads': GTHREADS, 'cards': CARDINFO, 'linear_comments': LINROWS},
          open(HERE / 'sql_ids.json', 'w'), indent=1)
print(n_ins, n_upd, {k: len(v) for k, v in ROWS.items()})
