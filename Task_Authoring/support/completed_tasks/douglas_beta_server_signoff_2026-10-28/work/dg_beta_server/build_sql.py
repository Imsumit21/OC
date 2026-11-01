"""Builds task_inputs/01_Universe_Inject.sql for the Douglas beta server sign-off scenario (design v2).

Read-only on the base; writes only under Task_Authoring-2/. Never executes SQL. Every id and planned wording comes from
minted_ids.json / planned_text.json (mint_ids.py); the cohort comes from cohort.json.
"""
import datetime as D
import email.utils
import hashlib
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
WS = ROOT.parent
P = json.load(open(HERE / 'planned_text.json'))
M = json.load(open(HERE / 'minted_ids.json'))
COHORT = json.load(open(HERE / 'cohort.json'))
LIN = json.load(open(WS / 'HarmonyGames_Other_Services/Services_Data/linear/data.json'))
ISSUES = {i['identifier']: i for i in LIN['issues']}

DG, ART, OLI, LEO, VIN, OWEN = ('douglas@harmonygames.co', 'arthur.blake@harmonygames.co', 'oliver.brooks@harmonygames.co',
                               'leonard.hayes@harmonygames.co', 'vincent.parker@harmonygames.co', 'owen.baker@harmonygames.co')
NAMES = {DG: 'Douglas', ART: 'Arthur Blake', OLI: 'Oliver Brooks', LEO: 'Leonard Hayes', VIN: 'Vincent Parker', OWEN: 'Owen Baker'}
SLACK_U = {DG: 'EMPLOYEE_0031_SLACK_ID', ART: 'EMPLOYEE_0025_SLACK_ID', OLI: 'EMPLOYEE_0003_SLACK_ID', LEO: 'EMPLOYEE_0038_SLACK_ID'}
ROOTS = {DG: 'd_cd7849ec043ab3da107f8c', ART: 'd_cc3e90160f490686039986', OLI: 'd_bdf01b53c6a92c5e167c65'}
GH = {'douglas': 'PERSON_5760_GITHUB_USERNAME', 'contractor': 'PERSON_2967_GITHUB_USERNAME', 'arthur': 'EMPLOYEE_0025_GITHUB_USERNAME',
      'vincent': 'EMPLOYEE_0012_GITHUB_USERNAME', 'coderabbit': 'PERSON_6026_GITHUB_USERNAME'}
CR_ACTOR = 'SVC_0321_GITHUB_USERNAME'      # base timeline actor for CodeRabbit comments (I07)
LU = {'vincent': 'usr_65c76e0b87aa7e9b', 'oliver': 'usr_bdf01b53c6a92c5e', 'samuel': 'usr_caafeec2804b3a67',
      'calvin': 'usr_49b9dfa5208d400d', 'claire': 'usr_7fe31e7ec8199618', 'marcus': 'usr_c77c50cc15c5342d',
      'arthur': 'usr_cc3e90160f490686', 'douglas': 'usr_cd7849ec043ab3da', 'owen': 'usr_4e13bd40cc73d0fc',
      'brian': 'usr_fc22d5941b2aeb5c', 'leonard': 'usr_63fffeb4fab5233e', 'robert': 'usr_Robert'}
ACTIVE_LIN = set(LU.values()) - {'usr_Robert'}
TR_ART = '2162c1ba310341bf318f48b7'
ZM_BOARD = {'id': '6851a6569f3bf818760632ab', 'name': 'ZM ROADMAP', 'shortLink': 'HSqnngwQ'}
BETA_LIST = {'id': '6851a674975da1fe76e70d93', 'name': 'BETA: Oct 10'}
REPO = 'harmonygames-Games/match3d-backend'
ZM = 'C0880U9751A'


def h(seed, n):
    return hashlib.sha256(seed.encode()).hexdigest()[:n]


def ts_of(iso):
    return D.datetime.fromisoformat(iso.replace('Z', '+00:00')).timestamp()


def iso(t):
    return D.datetime.fromtimestamp(t, D.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


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


BETA, CLIENTQA = M['FOLDER_BETA']['id'], M['FOLDER_CLIENTQA']['id']
drive(BETA, P['FOLDER_BETA_NAME'], FOLDER, ROOTS[ART], ART, [(DG, 'writer'), (OLI, 'writer'), (VIN, 'writer')],
      M['FOLDER_BETA']['at'], M['FOLDER_BETA']['at'])
drive(CLIENTQA, P['FOLDER_CLIENTQA_NAME'], FOLDER, ROOTS[OLI], OLI, [(DG, 'reader'), (VIN, 'writer'), (ART, 'writer')],
      M['FOLDER_CLIENTQA']['at'], M['FOLDER_CLIENTQA']['at'])

# --- H2 doc
DOCID = M['DOC_DEPLOYS']['id']
DOC_TEXT = P['DOC_TITLE'] + '\n' + P['DOC_BODY'] + '\n'
doc_shares = [(ART, 'reader'), (OLI, 'reader'), (VIN, 'reader')]
drive(DOCID, P['DOC_TITLE'], DOC, ROOTS[DG], DG, doc_shares, M['DOC_DEPLOYS']['created'], M['DOC_DEPLOYS']['at'])
tl = len(P['DOC_TITLE']) + 1
runs = [{'start': 0, 'end': tl, 'named_style': 'TITLE', 'list_id': None, 'list_nesting': 0},
        {'start': tl, 'end': len(DOC_TEXT), 'named_style': 'NORMAL_TEXT', 'list_id': None, 'list_nesting': 0}]
ins('gdocs.docs_documents', ['document_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility', 'body_text',
                             'style_runs_json', 'revision_id', 'drive_file_id', 'created_time', 'modified_time'],
    [DOCID, P['DOC_TITLE'], DG, js([e for e, _ in doc_shares]), 'private', DOC_TEXT, js(runs), h('rev' + DOCID, 10), DOCID,
     M['DOC_DEPLOYS']['created'], M['DOC_DEPLOYS']['at']], DOCID)

# --- deploy log (two tabs, one spreadsheet)
LOG = M['SHEET_DEPLOYLOG']['id']
CON = 'PERSON_2967_NAME'
PRS = M['PRS']
TD = iter(range(41, 80))
prod_rows = [['When (UTC)', 'What', 'Task def', 'By']]
prod_rows.append(['2025-08-25 11:52', 'beta prod cut: prod branch from main (#37, #38)', f'zm-api:{next(TD)}', CON])
for when, what, by in [('2025-09-02 17:30', '#39', CON), ('2025-09-03 16:30', '#41', 'Douglas'), ('2025-09-04 12:50', '#43', CON),
                       ('2025-09-08 17:18', '#42, #44', 'Douglas'), ('2025-09-09 20:29', '#46', 'Douglas'),
                       ('2025-09-10 18:20', '#45', 'Douglas')]:
    prod_rows.append([when, what, f'zm-api:{next(TD)}', by])
con_rows = [['When (UTC)', 'Type', 'What', 'Target', 'By'],
            ['2025-08-26 10:30', 'import', 'plague race table', 'dev', 'Douglas'],
            ['2025-08-28 17:05', 'console', 'plague race bot names', 'prod', 'Douglas'],
            ['2025-09-02 18:05', 'import', 'trophy path copy table', 'dev', 'Douglas'],
            ['2025-09-08 16:45', 'import', 'Zombie Lane rewards', 'prod', 'Douglas'],
            ['2025-09-10 17:40', 'import', 'loadout table', 'dev', 'Douglas'],
            ['2025-09-11 16:30', 'import', 'algo levels 2.0 level pack', 'dev', 'Douglas'],
            ['2025-09-12 19:20', 'import', 'analytics events table', 'dev', 'Douglas'],
            ['2025-09-16 14:20', 'import', 'economy table', 'dev', 'Douglas'],
            ['2025-09-17 15:50', 'import', 'boss arena HP table', 'dev', 'Douglas']]
log_shares = [(ART, 'reader'), (OLI, 'reader'), (VIN, 'reader')]
drive(LOG, P['SHEET_DEPLOYLOG_TITLE'], SHEET, ROOTS[DG], DG, log_shares, M['SHEET_DEPLOYLOG']['created'], M['SHEET_DEPLOYLOG']['at'])
ins('gsheets.sheets_spreadsheets', ['spreadsheet_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility',
                                    'drive_file_id', 'created_time', 'modified_time'],
    [LOG, P['SHEET_DEPLOYLOG_TITLE'], DG, js([e for e, _ in log_shares]), 'private', LOG, M['SHEET_DEPLOYLOG']['created'],
     M['SHEET_DEPLOYLOG']['at']], LOG)
for i, (tname, grid) in enumerate([('Prod deploys', prod_rows), ('Console & imports', con_rows)]):
    ins('gsheets.sheets_sheets', ['spreadsheet_id', 'sheet_id', 'title', '"index"', 'row_count', 'column_count', 'grid_json'],
        [LOG, i, tname, i, 1000, 26, js(grid)], f'{LOG}#{i}')

# prod task-definition numbers for every prod/rollback event, in time order (continues the log's numbering)
td_counter = 41 + len(prod_rows) - 1
events = sorted([(e['at'], n, e) for n, v in PRS.items() for e in v['events'] if e['kind'] in ('prod', 'rollback')],
                key=lambda x: (x[0], int(x[1])))
TDNUM, logged, last_td = {}, {}, {}
for at, n, e in events:
    key = at[:16].replace('T', ' ')
    match = next((r for r in prod_rows[1:] if r[0] == key and ('#' + n) in r[1]), None)
    if match:
        TDNUM[e['comment_id']] = match[2]
    else:
        TDNUM[e['comment_id']] = f'zm-api:{td_counter}'
        td_counter += 1

# =========================================================== Confluence
CONF_COLS = ['id', 'space_id', 'parent_id', 'title', 'body', 'body_format', 'status', 'version', 'author_id', 'created_at', 'updated_at']
VER_COLS = ['id', 'page_id', 'number', 'title', 'body', 'author_id', 'message', 'created_at']


def conf(pid, title, html, at):
    ins('confluence.confluence_pages', CONF_COLS, [pid, 'space_OPS', 'page_ops_home', title, html, 'storage', 'current', 1,
                                                    'user_EMPLOYEE_0025', at, at], pid)
    vid = 'ver_' + h('ver' + pid + '1', 32)
    ins('confluence.confluence_page_versions', VER_COLS, [vid, pid, 1, title, html, 'user_EMPLOYEE_0025', None, at], vid)


def html(text):
    return ''.join(f'<p>{line}</p>' for line in text.split('\n'))


conf(M['CONF_DD']['id'], P['CONF_TITLE'], html(P['CONF_BODY']), M['CONF_DD']['at'])
conf(M['CONF_BETA']['id'], P['CONF_BETA_TITLE'], html(P['CONF_BETA_BODY']), M['CONF_BETA']['at'])
# hardening r1: QA question and Arthur's reply in the beta page's comments
for ck, bk in [('CC_OLI', 'CC_OLI_BODY'), ('CC_ART', 'CC_ART_BODY')]:
    c = M[ck]
    ins('confluence.confluence_comments', ['id', 'page_id', 'author_id', 'parent_id', 'body', 'created_at', 'updated_at'],
        [c['id'], M['CONF_BETA']['id'], c['author'], c.get('parent'), f"<p>{P[bk]}</p>", c['at'], c['at']], c['id'])

# =========================================================== Slack
SL_COLS = ['id', 'ts', 'channel_id', 'type', 'user_id', 'text', 'thread_parent_id', 'thread_ts_legacy', 'reply_count',
           'reply_users_count', 'latest_reply', 'is_activity_message', 'subtype', 'reactions_json', 'files_json',
           'attachments_json', 'created_at', 'metadata_json']


def slack(mid, ts, ch, user, text, at, parent=None, rc=0, ru=0, latest=None):
    ins('slack.slack_messages', SL_COLS, [mid, ts, ch, 'message', user, text, parent[0] if parent else None,
                                          parent[1] if parent else (ts if rc else None), rc, ru, latest, False, None, '[]', '[]', '[]',
                                          at, '{}'],
        f'{ch}/{ts}')


def sm(k):
    return M[k]


OK_AT = '2025-09-27T02:07:12.553908Z'
OK_TS = f"{ts_of(OK_AT):.6f}"
OK_ID = h(f"{ZM}|{OK_TS}", 32)
for k, who in [('S_OLIVER_MERGED', OLI), ('S_FREEZE_MON', ART), ('S_DG_CLAIM', DG), ('S_OLIVER_SUM', OLI),
               ('S_OLIVER_POST', OLI)]:
    m = sm(k)
    slack(m['id'], m['ts'], m['channel'], SLACK_U[who], P[k], m['at'])
ak = sm('S_ASK')
slack(ak['id'], ak['ts'], ak['channel'], SLACK_U[ART], P['S_ASK'], ak['at'])
pa = sm('S_DG_ASK47')
slack(pa['id'], pa['ts'], ZM, SLACK_U[DG], P['S_DG_ASK47'], pa['at'], rc=2, ru=2, latest=OK_TS)
ra = sm('S_ART_DEVONLY')
slack(ra['id'], ra['ts'], ZM, SLACK_U[ART], P['S_ART_DEVONLY'], ra['at'], parent=(pa['id'], pa['ts']))
slack(OK_ID, OK_TS, ZM, SLACK_U[DG], 'ok', OK_AT, parent=(pa['id'], pa['ts']))

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
    import re
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def shortlink(seed):
    import base64
    return base64.b64encode(hashlib.sha256(seed.encode()).digest()).decode().replace('+', 'x').replace('/', 'Q')[:8]


CARDINFO = {}
for ck, ak, name, desc, short, pos, last, ncom in [
        ('T_H1CARD', 'T_H1CREATE', P['H1_TITLE'], P['H1_DESC'], 80, 140737488658432.0, M['T_H1CMT']['at'], 1),
        ('T_CLIENTCARD', 'T_CLIENTCREATE', P['CLIENT_TITLE'], P['CLIENT_DESC'], 81, 140737488666624.0, M['T_CLIENTCARD']['at'], 0)]:
    cid = M[ck]['id']
    sl = shortlink(cid)
    CARDINFO[ck] = (cid, short, name, sl)
    url = f"https://PERSON_6092_TRELLO_USERNAME.com/c/{sl}/{short}-{slug(name)}"
    ins('trello.trello_cards', TC_COLS, [cid, name, ZM_BOARD['id'], BETA_LIST['id'], desc, pos, False, None, False, '[]', '[]',
                                         short, None, None, url, last, None, js(badges(ncom))], cid)
    ins('trello.trello_actions', TA_COLS, [M[ak]['id'], 'createCard', M[ak]['at'], TR_ART, ZM_BOARD['id'], cid, js(
        {"board": ZM_BOARD, "card": {"id": cid, "idShort": short, "name": name, "shortLink": sl}, "list": BETA_LIST})], M[ak]['id'])
cid, short, name, sl = CARDINFO['T_H1CARD']
ins('trello.trello_actions', TA_COLS, [M['T_H1CMT']['id'], 'commentCard', M['T_H1CMT']['at'], TR_ART, ZM_BOARD['id'], cid,
                                       js({"board": ZM_BOARD, "card": {"id": cid, "idShort": short, "name": name, "shortLink": sl},
                                           "idCard": cid, "list": BETA_LIST, "text": P['H1_CMT'], "textData": {"emoji": {}}})],
    M['T_H1CMT']['id'])

# =========================================================== Gmail
GM_COLS = ['id', 'thread_id', 'user_email', 'label_ids_json', 'snippet', 'internal_date', 'date', 'size_estimate', 'subject',
           'from_email', 'from_name', 'to_json', 'cc_json', 'bcc_json', 'reply_to_json', 'body_text', 'body_html',
           'headers_json', 'in_reply_to', '"references"', 'mbox_from', 'attachments_meta_json']
GTHREADS = {}


def mail(key, sender, to, cc, subject, body_text, copies, reply_to_key=None, thread_snippet=None):
    at = M[key]['at']
    dt = D.datetime.fromisoformat(at.replace('Z', '+00:00'))
    ms = int(dt.timestamp() * 1000)
    import base64
    msgid = '<CA' + base64.b64encode(hashlib.sha256(key.encode()).digest()).decode()[:38].replace('/', '_').replace('+', '-') + '@mail.gmail.com>'
    assert msgid == M[key]['message_id']
    parent_id = M[reply_to_key]['message_id'] if reply_to_key else None
    body = body_text.replace('\n', '\r\n')
    snippet = ' '.join(body_text.split())[:140]
    hdrs = [{"name": "Message-ID", "value": msgid}, {"name": "Date", "value": email.utils.format_datetime(dt)},
            {"name": "Subject", "value": subject}, {"name": "From", "value": f"{NAMES[sender]} <{sender}>"},
            {"name": "To", "value": f"{NAMES[to]} <{to}>"}, {"name": "Cc", "value": f"{NAMES[cc]} <{cc}>"}]
    if parent_id:
        hdrs += [{"name": "In-Reply-To", "value": parent_id}, {"name": "References", "value": parent_id}]
    GTHREADS[key] = {}
    for box, labels in copies:
        if reply_to_key:
            tref = GTHREADS[reply_to_key][box]
        else:
            tid = M[key]['gmail_id'] if box == DG else str(ms << 20 | int(h('g' + box + at, 5), 16) & 0xFFFFF)
            tref = f"{box}/{tid}"
            ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [tref, box, thread_snippet or snippet, None], tref)
        GTHREADS[key][box] = tref
        ins('gmail.gmail_messages', GM_COLS,
            [f"{box}/{msgid}", tref, box, js(labels), snippet, ms, at, len(body) + 900, subject, sender, NAMES[sender],
             js([f"{NAMES[to]} <{to}>"]), js([f"{NAMES[cc]} <{cc}>"]), '[]', '[]', body, None, js(hdrs), parent_id, parent_id, None, '[]'],
            f"{box}/{msgid}")
    return msgid


INBOX = ["INBOX", "IMPORTANT", "CATEGORY_PERSONAL"]
# hardening r1: Arthur's amendment is his reply-all inside Leonard's go/no-go thread (the thread shows the newest snippet)
mail('G_LEO', LEO, DG, ART, P['G_LEO_SUBJECT'], P['G_LEO_BODY'], [(DG, INBOX), (ART, INBOX), (LEO, ["SENT"])],
     thread_snippet=' '.join(P['G_AMEND_BODY'].split())[:140])
mail('G_AMEND', ART, DG, LEO, P['G_AMEND_SUBJECT'], P['G_AMEND_BODY'], [(DG, INBOX), (LEO, INBOX), (ART, ["SENT"])],
     reply_to_key='G_LEO')

# =========================================================== GCal (one copy per attendee calendar)
GC = M['GCAL_FREEZE']
att_order = [ART, DG, OLI, OWEN, VIN]
GC_COLS = ['event_id', 'calendar_id', 'summary', 'description', 'location', 'start_ts', 'end_ts', 'start_json', 'end_json',
           'organizer_email', 'creator_email', 'attendees_json', 'status', 'visibility', 'transparency', 'rrule_json',
           'recurring_event_id', 'original_start_json', 'sequence', 'created', 'updated', 'hangout_link', 'ical_uid']
for cal in att_order:
    att = []
    for e in att_order:
        a = {"email": e, "organizer": e == ART, "responseStatus": "accepted" if e in (ART, DG) else "needsAction"}
        if e == cal:
            a["self"] = True
        att.append(a)
    ins('gcal.gcal_events', GC_COLS, [GC['copies'][cal], cal, P['GCAL_SUMMARY'], P['GCAL_DESC'], None, GC['start'], GC['end'],
                                      js({"dateTime": GC['start']}), js({"dateTime": GC['end']}), ART, ART, js(att), 'confirmed',
                                      None, 'opaque', '[]', None, None, 1, GC['created'], GC['at'], None, GC['ical_uid']],
        GC['copies'][cal])

# =========================================================== GitHub match3d-backend #37-#54
TITLES = {37: 'Algo levels: spawn points from the server seed', 38: 'Plague race: count algo levels',
          39: 'Trophy path: container headlines config', 40: 'Catalog: add usable item entries',
          41: 'Algo levels 100+: seed endpoint', 42: 'Teams: ack lives gift', 43: 'Inventory: drop non-card items from equipped',
          44: 'Profile: other players profile v2', 45: 'Inventory: keep equipped slots across sessions',
          46: 'Economy: September adjustments', 47: 'Analytics: log endless_start on the server',
          48: 'Boss arena: infinite HP event config', 49: 'Boss arena: mirror balance values',
          50: "Boss arena: don't take a life on a win", 51: 'Trophy path: ignore duplicate claim requests',
          52: 'Teams: push lives refresh to client', 53: 'Boss arena: mirror refill and nuke values',
          54: 'Login streak: count days in player timezone'}
NOTE_EXTRA = {('44', 'rollback'): ' profile endpoint 500s for players on old clients',
              ('54', 'rollback'): ' streak resets for players east of UTC'}
PR_COLS = ['id', 'repo_id', 'number', 'title', 'state', 'merged', 'draft', 'locked', 'author_login',
           'merged_by_login', 'body', 'base_ref', 'head_ref', 'base_sha', 'head_sha', 'merge_commit_sha', 'additions', 'deletions',
           'changed_files', 'labels_json', 'assignee_logins_json', 'requested_reviewer_logins_json', 'created_at', 'updated_at',
           'merged_at', 'closed_at', 'html_url']
CM_COLS = ['id', 'pr_id', 'author_login', 'body', 'created_at', 'updated_at']
RV_COLS = ['id', 'pr_id', 'author_login', 'state', 'body', 'submitted_at', 'commit_id', 'seq']
TL_COLS = ['id', 'pr_id', 'event', 'actor_login', 'created_at', 'data_json']
RC_COLS = ['id', 'pr_id', 'author_login', 'body', 'path', 'diff_hunk', 'line', 'position', 'commit_id', 'in_reply_to_id',
           'created_at', 'seq', 'pull_request_review_id', 'side', 'subject_type']
REVIEW_BODY = {('50', 'COMMENTED'): 'looks fine, ship it after go/no-go', ('44', 'CHANGES_REQUESTED'): 'old clients still call this without the new fields, keep the v1 shape for them',
               ('45', 'CHANGES_REQUESTED'): 'this clears the slots for cards that are still owned, check ownership first'}


def plus(at, minutes):
    return iso(ts_of(at) + minutes * 60)


PRINFO = {}
for n_s, pr in sorted(PRS.items(), key=lambda x: int(x[0])):
    n = int(n_s)
    pid = pr['id']
    author = GH[pr['author']]
    other = GH['contractor'] if pr['author'] == 'douglas' else GH['douglas']
    head_ref = slug(TITLES[n])[:40]
    head_sha, base_sha, merge_sha = h('head' + pid, 40), h('base' + pid, 40), h('merge' + pid, 40)
    body = ('\n\n<!-- This is an auto-generated comment: release notes by coderabbit.ai -->\n\n## Summary by CodeRabbit\n\n'
            f'* **Changes**\n  * {TITLES[n].split(": ", 1)[1].capitalize()}.\n\n'
            '<!-- end of auto-generated comment: release notes by coderabbit.ai -->')
    comments = [(pr['coderabbit']['comment_id'], GH['coderabbit'],
                 '<!-- This is an auto-generated comment: summarize by coderabbit.ai -->\n<!-- walkthrough_start -->\n\n## Walkthrough\n\n'
                 f'{TITLES[n].split(": ", 1)[1].capitalize()} in the zombies_game backend.\n\n<!-- walkthrough_end -->',
                 plus(pr['created'], 2))]
    for e in pr['events']:
        who = GH[e['by']]
        t = e['at'][:16].replace('T', ' ')
        if e['kind'] == 'prod':
            txt = f"prod: {t} UTC, {TDNUM[e['comment_id']]}"
        elif e['kind'] == 'rollback':
            txt = f"rollback: {t} UTC, pick reverted, {TDNUM[e['comment_id']]}.{NOTE_EXTRA.get((n_s, 'rollback'), '')}"
        else:
            txt = f"on dev for Vincent to try ({t} UTC)"
        comments.append((e['comment_id'], who, txt, e['at']))
    if n == 51:
        comments.append((f'{pid}#c_{len(comments) + 1}', GH['vincent'], 'works on dev, double tapping claim only counts once now',
                         '2025-09-22T09:14:00Z'))
    reviews = [(pr['coderabbit']['review_id'], GH['coderabbit'], 'COMMENTED', '**Actionable comments posted: 0**', plus(pr['created'], 6))]
    for r in pr['reviews']:
        reviews.append((r['id'], GH[r['by']], r['state'], REVIEW_BODY.get((n_s, r['state']), ''), r['at']))
    last = max([c[3] for c in comments] + [r[4] for r in reviews] + [pr['merged']])
    merged_by = other if pr['author'] != 'douglas' else GH['douglas']
    ins('github.github_pull_requests', PR_COLS,
        [pid, REPO, n, TITLES[n], 'closed', True, False, False, author, merged_by, body, 'main', head_ref, base_sha, head_sha,
         None, 20 + int(h('a' + pid, 2), 16) % 120, 3 + int(h('d' + pid, 2), 16) % 40, 2 + int(h('f' + pid, 1), 16) % 9,
         '[]', '[]', js([other]), pr['created'], last, pr['merged'], pr['merged'], None], pid)
    ins('github.github_branches', ['id', 'repo_id', 'name', 'head_sha', 'protected', 'is_default'],
        [f'{REPO}:{head_ref}', REPO, head_ref, head_sha, False, False], f'{REPO}:{head_ref}')
    ins('github.github_commits', ['sha', 'repo_id', 'message', 'authored_date', 'committed_date', 'author_login', 'author_name',
                                  'author_email', 'committer_login', 'committer_name', 'committer_email', 'parent_shas_json'],
        [head_sha, REPO, TITLES[n].split(': ', 1)[1].capitalize(), plus(pr['created'], -20), None, author,
         'PERSON_5760_NAME' if pr['author'] == 'douglas' else 'PERSON_2967_NAME',
         'PERSON_5760_EMAIL' if pr['author'] == 'douglas' else 'PERSON_2967_EMAIL', author,
         'PERSON_5760_NAME' if pr['author'] == 'douglas' else 'PERSON_2967_NAME',
         'PERSON_5760_EMAIL' if pr['author'] == 'douglas' else 'PERSON_2967_EMAIL',
         '[]'], head_sha)
    ins('github.github_pull_request_commits', ['id', 'pr_id', 'commit_sha', 'position'], [f'{pid}#c_0', pid, head_sha, 0], f'{pid}#c_0')
    for cid_, who, txt, at in comments:
        ins('github.github_pr_comments', CM_COLS, [cid_, pid, who, txt, at, at], cid_)
    for i, (rid, who, state, rb, at) in enumerate(reviews, 1):
        ins('github.github_reviews', RV_COLS, [rid, pid, who, state, rb, at, head_sha, i], rid)
    # inline review comments, each attached to the PR's own Approve: r2 Arthur on #46 (ZOM-537's economy table import);
    # r3 the contractor on #38 (ZOM-459's plague race table import) and Douglas on #39 (ZOM-509's trophy path copy table import)
    for rck, rcn, rline in (('RC_ART46', 46, 21), ('RC_C38', 38, 34), ('RC_DG39', 39, 47)):
        if n == rcn:
            rc = M[rck]
            ins('github.github_review_comments', RC_COLS,
                [rc['id'], pid, GH[rc['by']], P[rck], rc['path'], P[rck + '_HUNK'], rline, None, head_sha, None, rc['at'], 1,
                 rc['review_id'], 'RIGHT', 'line'], rc['id'])
    tl = [('review_requested', author, pr['created'], {"requested_reviewer": {"login": other}})]
    for cid_, who, txt, at in comments:
        tl.append(('commented', CR_ACTOR if who == GH['coderabbit'] else who, at, {}))
    for rid, who, state, rb, at in reviews:
        tl.append(('reviewed', who, at, {"commit_id": head_sha, "state": state.lower()}))
    tl += [('merged', merged_by, pr['merged'], {"commit_id": merge_sha}), ('closed', merged_by, pr['merged'], {})]
    tl.sort(key=lambda x: x[2])
    for i, (ev, actor, at, data) in enumerate(tl, 1):
        ins('github.github_timeline_events', TL_COLS, [f'{pid}#ev_{i}', pid, ev, actor, at, js(data)], f'{pid}#ev_{i}')
    PRINFO[n_s] = {'title': TITLES[n], 'comments': [(c[0], c[2], c[3]) for c in comments], 'updated_at': last}

# --- prod branch (H2: prod runs from the prod branch; head = the last pick, #52 on 2025-09-30)
PROD_HEAD = h('prod-pick' + PRS['52']['id'], 40)
ins('github.github_commits', ['sha', 'repo_id', 'message', 'authored_date', 'committed_date', 'author_login', 'author_name',
                              'author_email', 'committer_login', 'committer_name', 'committer_email', 'parent_shas_json'],
    [PROD_HEAD, REPO, 'Teams: push lives refresh to client (cherry picked from #52)', '2025-09-30T18:05:00Z', None, GH['douglas'],
     'PERSON_5760_NAME', 'PERSON_5760_EMAIL', GH['douglas'], 'PERSON_5760_NAME', 'PERSON_5760_EMAIL', '[]'], PROD_HEAD)
ins('github.github_branches', ['id', 'repo_id', 'name', 'head_sha', 'protected', 'is_default'],
    [f'{REPO}:prod', REPO, 'prod', PROD_HEAD, False, False], f'{REPO}:prod')

# =========================================================== Linear comments
LC_COLS = ['id', 'issue_id', 'author_id', 'parent_id', 'body', 'is_edited', 'created_at', 'updated_at', 'sequence']
DECISIVE = {
    'ZOM-461': "spawn points come from the server seed now, backend part is match3d-backend#37",
    'ZOM-459': "client sends the algo level flag now. backend part is match3d-backend#38, plague race counts it",
    'ZOM-509': "container + headlines come from the trophy path config, backend part is match3d-backend#39",
    'ZOM-336': "cooler model done. it's usable (cools zombies down), Douglas says that needs a catalog entry on the backend too: match3d-backend#40",
    'ZOM-392': "100+ levels pull their seeds from the server now, backend part match3d-backend#41",
    'ZOM-503': "client side was ok, the gift call was the problem. backend parts are match3d-backend#42 (ack) and match3d-backend#52 (refresh push)",
    'ZOM-518': "backend part is match3d-backend#43, drops items that aren't cards anymore from the equipped list on login",
    'ZOM-531': "it was the backend wiping the slots on a new session. backend part match3d-backend#45",
    'ZOM-537': "new values are in match3d-backend#46",
    'ZOM-444': "client fires it, and the backend logs endless_start too now: match3d-backend#47",
    'ZOM-499': "other players' profile fields come from the backend, that part is match3d-backend#44",
    'ZOM-487': "infinite HP boss config is served by the backend: match3d-backend#48",
    'ZOM-547': "balance values updated in the client sheet, backend copy in match3d-backend#49",
    'ZOM-550': "life was taken on the backend when you won boss arena. backend part match3d-backend#50",
    'ZOM-435': "double tap sends two claims. backend part is match3d-backend#51, it ignores the second one",
    'ZOM-553': "refill/nuke values updated in the client sheet, backend copy in match3d-backend#53",
    'ZOM-557': "client side fixed in 0.3.124, the streak count itself is on the backend: match3d-backend#54",
    'ZOM-510': "rewards were off because the backend still had the old sheet. fix is the Zombie Lane rewards import on the backend",
    'ZOM-256': "algo levels 2.0 pack is ready, needs the level pack imported on the backend",
}
NEUTRAL = {
    'client': ["fixed in the client, in Android {b}. nothing needed in match3d-backend",
               "client only, checked on {b}",
               "merged in match3d, ok on the {b} dev build",
               "tested on device with {b}, looks good",
               "client side fix, nothing needed in match3d-backend. ok on {b}"],
    'art': ["model + textures in, prefab hooked up", "asset in, scale checked in the level editor",
            "done, nothing needed in match3d-backend for this one", "art drop in, Calvin hooked it up"],
    'vfx': ["vfx in scene, checked in {b}", "animation in, timing ok on {b}", "vfx done, nothing needed in match3d-backend"],
    'tool': ["tool side only, works on dev", "editor change, nothing needed in match3d-backend"],
}
OWNER_LU = {'oliver.brooks': 'oliver', 'samuel.turner': 'samuel', 'calvin.price': 'calvin', 'claire.morgan': 'claire',
            'marcus.bennett': 'marcus', 'arthur.blake': 'arthur', 'douglas': 'douglas', 'owen.baker': 'owen',
            'brian.foster': 'brian', 'leonard.hayes': 'leonard'}


def build_of(at):
    d = D.datetime.fromisoformat(at.replace('Z', '+00:00'))
    base = (d - D.datetime(2025, 8, 20, tzinfo=D.timezone.utc)).days
    return f"0.3.{100 + max(0, base * 22 // 28)}"


def kind_of(t):
    tl = t['title'].lower()
    if t['parent'] == 'ZOM-97':
        return 'art'
    if 'vfx' in tl or 'animation' in tl or 'effects' in tl:
        return 'vfx'
    if 'simulat' in tl or 'bot' in tl or 'editor' in tl or 'library' in tl:
        return 'tool'
    return 'client'


LINNOTES = M['LIN_NOTES']
LINROWS = {}
targets = [(t['id'], t) for t in COHORT] + [(k, {'id': k, 'title': ISSUES[k]['title'], 'parent': ISSUES[k]['parent_id'],
                                                 'assignee': None}) for k in ['ZOM-461', 'ZOM-480', 'ZOM-479', 'ZOM-489']]
PARENT_NOTE = {'ZOM-457': "parent for the algo level bugs, the fixes are on the child tickets"}
for k, t in targets:
    iss = ISSUES[k]
    created, done = iss['created_at'], iss['completed_at']
    ceiling = done if done else min('2025-09-30T15:00:00Z', iss['updated_at'] if iss['updated_at'] > '2025-09-30' else '2025-09-30T15:00:00Z')
    if k in LINNOTES:
        n = LINNOTES[k]
        cid, author, at, body = n['id'], n['author'], n['at'], DECISIVE[k]
    else:
        owner = (ISSUES[k]['assignee_id'] or '')
        email_ = next((u['email'] for u in LIN['users'] if u['id'] == owner), '') or ''
        author = LU.get(OWNER_LU.get(email_.split('@')[0], ''), LU['vincent'])
        if author not in ACTIVE_LIN:
            author = LU['vincent']
        span = max(60, ts_of(ceiling) - ts_of(created))
        off = 120 + int(h('t' + k, 6), 16) % int(min(span - 60, 3 * 3600)) if span > 180 else 30
        at = iso(ts_of(ceiling) - off)
        if at <= created:
            at = iso(ts_of(created) + 30)
        kd = kind_of(t)
        tmpl = NEUTRAL[kd][int(h('n' + k, 4), 16) % len(NEUTRAL[kd])]
        body = PARENT_NOTE.get(k) or tmpl.format(b=build_of(at))
        cid = 'cmt_' + h('lin' + k, 20)
    assert created < at and (not done or at <= done) and at < '2025-10-01', (k, created, at, done)
    ins('linear.linear_comments', LC_COLS, [cid, k, author, None, body, False, at, at, 1], cid)
    LINROWS[k] = {'id': cid, 'at': at, 'body': body, 'author': author}
    if at > iss['updated_at']:
        upd('linear.linear_issues', {'updated_at': at}, 'id', k)

# =========================================================== write
order = ['gdrive', 'gdocs', 'gsheets', 'confluence', 'slack', 'trello', 'gmail', 'gcal', 'github', 'linear']
n_ins = sum(1 for s in OUT for x in OUT[s] if x.startswith('INSERT'))
n_upd = sum(1 for s in OUT for x in OUT[s] if x.startswith('UPDATE'))
head = ['-- Are you planning to inject? Yes',
        f'-- HarmonyGames injection - persona Douglas <{DG}> (Software Engineer), Long Horizon.',
        f'-- Services: {", ".join(order)}. Statements: {n_ins} INSERT (one row each), {n_upd} UPDATE.',
        '-- Literal values only; parents before children; re-apply this exact SQL before every agent run.', 'BEGIN;']
body = []
for s in order:
    body.append(f'-- ===================== {s.upper()} =====================')
    body += OUT[s]
(ROOT / 'task_inputs/01_Universe_Inject.sql').write_text('\n'.join(head + body + ['COMMIT;']) + '\n')
json.dump({'rows': ROWS, 'gmail_threads': GTHREADS, 'cards': CARDINFO, 'ok_reply': {'id': OK_ID, 'ts': OK_TS, 'at': OK_AT},
           'linear_comments': LINROWS, 'prs': PRINFO, 'tdnum': TDNUM, 'prod_rows': prod_rows, 'con_rows': con_rows},
          open(HERE / 'sql_ids.json', 'w'), indent=1)
print(n_ins, n_upd, {k: len(v) for k, v in ROWS.items()})
