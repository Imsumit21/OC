"""Builds task_inputs/01_Universe_Inject.sql for the account-custody scenario (design v2, injection rev 3).
Read-only on the base; writes only under Task_Authoring-2/. Never executes SQL."""
import hashlib, json, datetime as D, email.utils, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parents[2]
P = json.load(open(HERE / 'planned_text.json'))
M = json.load(open(HERE / 'minted_ids.json'))

FRED, LEO, ART, ROB = ('frederick.stone@harmonygames.co', 'leonard.hayes@harmonygames.co',
                       'arthur.blake@harmonygames.co', 'robert@harmonygames.co')
NAMES = {FRED: 'Frederick Stone', LEO: 'Leonard Hayes', ART: 'Arthur Blake'}
ROOTS = {FRED: 'd_175c0d7bc72ed244b944cb', LEO: 'd_63fffeb4fab5233ed5bb73', ART: 'd_cc3e90160f490686039986'}
SLACK_U = {LEO: 'EMPLOYEE_0038_SLACK_ID', ART: 'EMPLOYEE_0025_SLACK_ID', FRED: 'EMPLOYEE_0008_SLACK_ID'}
TR_ART = '2162c1ba310341bf318f48b7'
HG_BOARD = {'id': '640643a3fd8f3ca308d9318e', 'name': 'Harmony Games', 'shortLink': 'f4LGcmuh'}
TODO = {'id': '640643a3fd8f3ca308d93195', 'name': 'To Do'}


def h(seed, n):
    return hashlib.sha256(seed.encode()).hexdigest()[:n]


def ts_of(iso):
    return D.datetime.fromisoformat(iso.replace('Z', '+00:00')).timestamp()


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
    return json.dumps(x)


OUT = []
ROWS = {}


def ins(table, cols, vals, key=None):
    cl = ', '.join(cols)
    OUT.append(f"INSERT INTO {table} ({cl})\nVALUES ({', '.join(q(v) for v in vals)});")
    ROWS.setdefault(table, []).append(key)


# ------------------------------------------------------------------ ids changed at injection (design_delta)
FOLDER_SWEEP = 'd_' + M['FOLDER_SWEEP']['id'][2:]     # folders are d_ in the base (Ask_Carriers 2.4)
FOLDER_OPS = 'd_' + M['FOLDER_OPS']['id'][2:]
DECOY90_AT = '2025-09-24T18:43:56.208417Z'            # moved from Sep 15 to the Sep 24 "2 months left" discussion
DECOY90_TS = f"{ts_of(DECOY90_AT):.6f}"
DECOY90_ID = hashlib.sha256(f"C07C2866011|{DECOY90_TS}".encode()).hexdigest()[:32]

# ------------------------------------------------------------------ Drive / Sheets / Docs
DF_COLS = ['id', 'name', 'mime_type', 'parents_json', 'owner_email', 'shared_with_emails_json', 'shared_roles_json',
           'visibility', 'owners_json', 'modified_time', 'created_time', 'trashed', 'starred']
FOLDER = 'application/vnd.google-apps.folder'
SHEET = 'application/vnd.google-apps.spreadsheet'
DOC = 'application/vnd.google-apps.document'


def drive(fid, name, mime, parent, owner, shares, created, modified):
    ins('gdrive.drive_files', DF_COLS,
        [fid, name, mime, js([parent]), owner, js([e for e, _ in shares]),
         js([{'email': e, 'role': r} for e, r in shares]), 'private', js([owner]), modified, created, False, False], fid)


def spreadsheet(fid, title, parent, owner, shares, created, modified, tabs):
    drive(fid, title, SHEET, parent, owner, shares, created, modified)
    ins('gsheets.sheets_spreadsheets',
        ['spreadsheet_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility', 'drive_file_id',
         'created_time', 'modified_time'],
        [fid, title, owner, js([e for e, _ in shares]), 'private', fid, created, modified], fid)
    for i, (tname, grid) in enumerate(tabs):
        ins('gsheets.sheets_sheets', ['spreadsheet_id', 'sheet_id', 'title', '"index"', 'row_count', 'column_count',
                                      'grid_json'], [fid, i, tname, i, 1000, 26, js(grid)], f"{fid}#{i}")


SWEEP_SHARES = [(LEO, 'writer'), (FRED, 'reader')]
drive(FOLDER_SWEEP, 'Admin sweep - Sep 30', FOLDER, ROOTS[ART], ART, SWEEP_SHARES,
      '2025-09-30T19:50:00Z', '2025-09-30T20:31:00Z')

E = {FRED: FRED, LEO: LEO, ART: ART, ROB: ROB}
NODE_YT = '[EMAIL_126620]'          # Node staff address Node gave for access (C08MCEP1B9B/1727689480.986899)
FRED_PERSONAL = '[EMAIL_912045]'    # unused body-text token (1.F): Frederick's personal Google account

EXPORTS = [
    ('meta', 'Meta Business - Domino Delights ad account - people', '2025-09-30T19:52:00Z', [
        ('People', [
            ['Ad account', 'Domino Delights', '', ''],
            ['Ad account ID', '907669287942378', '', ''],
            ['Name', 'Email', 'Ad account role', 'Added'],
            ['Frederick Stone', FRED, 'Admin (created the ad account)', '2024-10-06'],
            ['Robert', ROB, 'Admin', '2024-10-06'],
            ['Leonard Hayes', LEO, 'Admin (business portfolio admin)', '2024-01-22 (portfolio)'],
            ['Arthur Blake', ART, 'Admin', '2025-04-29']]),
        ('Partners', [
            ['Partner business', 'Access on Domino Delights ad account', 'Shared by', 'Date shared'],
            ['Node Media LLC', 'Partner admin (manage campaigns, billing view)', FRED, '2024-10-07']])]),
    ('gads_569', 'Google Ads 569-350-5790 - access', '2025-09-30T19:55:00Z', [
        ('Access', [
            ['Customer ID', '569-350-5790', '', '', ''],
            ['Account name', 'Harmony Games, Inc.', '', '', ''],
            ['Enabled campaigns', 0, '', '', ''],
            ['Name', 'Email', 'Access level', 'Status', 'Added'],
            ['Leonard Hayes', LEO, 'Admin', 'Active', '2024-09-20'],
            ['Frederick Stone', FRED, 'Admin', 'Active', '2024-10-07']]),
        ('Linked managers', [
            ['Manager account', 'Manager ID', 'Status', 'Changed', 'Changed by'],
            ['Node Media LLC', '645-364-1205', 'Unlinked', '2024-12-20', FRED]])]),
    ('gads_449', 'Google Ads 449-481-1590 - access', '2025-09-30T19:57:00Z', [
        ('Access', [
            ['Customer ID', '449-481-1590', '', '', ''],
            ['Account name', 'Calm Play LLC', '', '', ''],
            ['Enabled campaigns', 0, '', '', ''],
            ['Name', 'Email', 'Access level', 'Status', 'Added'],
            ['Robert', ROB, 'Admin', 'Active', '2024-01-10'],
            ['Leonard Hayes', LEO, 'Admin', 'Active', '2024-01-20'],
            ['Arthur Blake', ART, 'Admin', 'Active', '2024-01-20'],
            ['Frederick Stone', FRED, 'Admin', 'Active', '2024-09-05']]),
        ('Linked managers', [
            ['Manager account', 'Manager ID', 'Status', 'Changed', 'Changed by'],
            ['Node Media LLC', '645-364-1205', 'Unlinked', '2024-12-20', FRED]])]),
    ('unity_ads', 'Unity - Harmony Games Inc org - owners and managers', '2025-09-30T19:58:00Z', [
        ('Members', [
            ['Organization', 'Harmony Games Inc', ''],
            ['Organization ID', '20067043314233', ''],
            ['Filter', 'Role: Owner, Manager (seat-only users not shown)', ''],
            ['Name', 'Email', 'Role'],
            ['Arthur Blake', ART, 'Owner'],
            ['Robert', ROB, 'Owner'],
            ['Leonard Hayes', LEO, 'Owner'],
            ['Frederick Stone', FRED, 'Manager']])]),
    ('applovin', 'AppLovin - Harmony Games - account users', '2025-09-30T20:01:00Z', [
        ('Users', [
            ['Name', 'Email', 'Role', 'Added'],
            ['Frederick Stone', FRED, 'Admin', '2024-09-25'],
            ['Leonard Hayes', LEO, 'Admin', '2024-10-11'],
            ['', 'EMPLOYEE_0032_EMAIL', 'User', '2024-10-24'],
            ['Arthur Blake', ART, 'User', '2025-05-06'],
            ['Brian Foster', 'brian.foster@harmonygames.co', 'User', '2025-05-08']])]),
    ('adjoe', 'adjoe advertiser dashboard - users', '2025-09-30T20:04:00Z', [
        ('Users', [
            ['Name', 'Email', 'Role', 'Added'],
            ['Frederick Stone', FRED, 'Admin', '2024-10-31'],
            ['Leonard Hayes', LEO, 'Admin', '2025-04-28']])]),
    ('admob', 'AdMob pub-3556282811018998 - users', '2025-09-30T20:07:00Z', [
        ('Users', [
            ['Publisher ID', 'pub-3556282811018998', '', ''],
            ['Name', 'Email', 'Role', 'Since'],
            ['Leonard Hayes', LEO, 'Admin (account owner)', '2025-03-03'],
            ['Frederick Stone', FRED, 'Admin', '2025-08-25']])]),
    ('tiktok', 'TikTok - harmonygames - access', '2025-09-30T20:10:00Z', [
        ('Access', [
            ['Account', 'Login email', 'Role', 'Status', 'Notes'],
            ['@harmonygames (64 followers)', FRED, 'Admin', 'Active', 'recovered 2025-09-29; Leonard signs in with this login'],
            ['@harmonygames.app', 'SVC_0009_EMAIL', 'Admin', 'Deactivated 2025-09-29 (deletion pending)', 'made 2025-09-29 while the old one was locked']])]),
    ('youtube', 'YouTube - Harmony Games channel - permissions', '2025-09-30T20:13:00Z', [
        ('Permissions', [
            ['Name', 'Email', 'Role', 'Added'],
            ['Frederick Stone', FRED, 'Owner (created the channel)', '2024-11-21'],
            ['Leonard Hayes', LEO, 'Manager', '2025-04-27']]),
        ('Removed users', [
            ['Name', 'Email', 'Role', 'Removed', 'Removed by'],
            ['Node Media LLC', NODE_YT, 'Manager', '2024-12-20', FRED]])]),
    ('linkedin', 'LinkedIn - Harmony Games page - admins', '2025-09-30T20:16:00Z', [
        ('Page admins', [
            ['Name', 'Login email', 'Role', 'Added'],
            ['Leonard Hayes', LEO, 'Super admin', '2023-04-18'],
            ['Robert', ROB, 'Super admin', '2023-04-18'],
            ['Arthur Blake', ART, 'Super admin', '2023-04-18'],
            ['Frederick Stone', FRED, 'Super admin', '2024-09-12']])]),
    ('x', 'X - harmonygames - access', '2025-09-30T20:18:00Z', [
        ('Access', [
            ['Account', 'Login email', 'Role', 'Notes'],
            ['@harmonygames', FRED, 'Owner', 'no delegates set up']])]),
    ('instagram', 'Instagram - harmonygames - access', '2025-09-30T20:21:00Z', [
        ('Access', [
            ['Account', 'Name', 'Login email', 'Role', 'Notes'],
            ['@harmonygames', 'Frederick Stone', FRED_PERSONAL, 'Owner (account login)', "Fred's personal gmail, not harmonygames.co"]])]),
    ('discord', 'Discord - Harmony Games server - admin roles', '2025-09-30T20:24:00Z', [
        ('Admins', [
            ['Name', 'Login email', 'Server role', 'Added'],
            ['Leonard Hayes', LEO, 'Owner', '2024-12-13'],
            ['Frederick Stone', FRED, 'Admin', '2024-12-14'],
            ['Robert', ROB, 'Admin', '2024-12-14']])]),
    ('play_console', 'Google Play Console - Harmony Games, Inc. developer account - users', '2025-09-30T20:26:00Z', [
        ('Users', [
            ['Name', 'Email', 'Access', 'Accepted'],
            ['Leonard Hayes', LEO, 'Account owner', ''],
            ['Frederick Stone', FRED, 'User', '2024-09-22'],
            ['Robert', ROB, 'User', '2024-09-23'],
            ['Arthur Blake', ART, 'User', '2024-09-30'],
            ['', 'PERSON_3494_EMAIL', 'User', '2024-10-08'],
            ['', 'PERSON_2218_EMAIL', 'User', '2024-12-11'],
            ['Samuel Turner', 'samuel.turner@harmonygames.co', 'User', '2024-12-11'],
            ['Douglas', 'douglas@harmonygames.co', 'User', '2024-12-11'],
            ['Brian Foster', 'brian.foster@harmonygames.co', 'User', '2025-05-05'],
            ['', 'EMPLOYEE_0032_EMAIL', 'User', '2025-09-30']])]),
    ('app_store_connect', 'App Store Connect - Harmony Games, Inc. team - users', '2025-09-30T20:28:00Z', [
        ('Users', [
            ['Name', 'Email', 'Role', 'Status', 'Joined'],
            ['Leonard Hayes', LEO, 'Account Holder', 'Active', '2024-09-25'],
            ['Frederick Stone', FRED, 'Member', 'Active', '2024-09-25'],
            ['Robert', ROB, 'Member', 'Active', '2024-09-30'],
            ['Calvin Price', 'calvin.price@harmonygames.co', 'Member', 'Active', '2024-12-11']])]),
    ('singular', 'Singular - users', '2025-09-30T20:31:00Z', [
        ('Users', [
            ['Name', 'Email', 'Role', 'Invited', 'Status'],
            ['Leonard Hayes', LEO, 'Admin', '2024-01-01', 'Active'],
            ['Robert', ROB, 'User', '2024-01-01', 'Active'],
            ['Douglas', 'douglas@harmonygames.co', 'User', '2024-02-19', 'Active'],
            ['Frederick Stone', FRED, 'User', '2024-09-04', 'Active'],
            ['Simon Walker', 'simon.walker@harmonygames.co', 'User', '2024-10-22', 'Active'],
            ['Node Media LLC', NODE_YT, 'User', '2024-10-07', 'Removed 2024-12-20']])]),
]
for key, title, at, tabs in EXPORTS:
    spreadsheet(M['SW_' + key]['id'], title, FOLDER_SWEEP, ART, SWEEP_SHARES, at, at, tabs)

# Fred's March logins sheet (stale, partial)
spreadsheet(M['SHEET_MARCH']['id'], P['MARCH_TITLE'], ROOTS[FRED], FRED, [], '2025-03-10T17:40:00Z',
            '2025-03-10T17:58:00Z', [('Sheet1', [
                ['Platform', 'Login', "Who's on it", 'Notes'],
                ['Meta Ads', FRED, 'Fred, Leonard', 'receipts to my inbox'],
                ['Google Ads', FRED, 'Fred, Leonard', ''],
                ['Unity Ads', FRED, 'Fred, Leonard', 'ZM3D campaigns'],
                ['AppLovin MAX', FRED, 'Fred, Leonard', 'payouts monthly'],
                ['adjoe', FRED, 'Fred', ''],
                ['AdMob', FRED, 'Fred, Leonard', 'pub-2341961509332343'],
                ['Singular', LEO, 'Leonard, Fred', 'MMP'],
                ['TikTok', 'SVC_0009_EMAIL', 'Fred, Leonard', 'check which login'],
                ['YouTube', FRED, 'Fred', ''],
                ['LinkedIn page', LEO, 'Leonard, Fred', ''],
                ['PlayableX', FRED, 'Fred', 'playables portal']])])

# Leonard's cash notes doc (H2)
DOC_BODY = (P['DOC_CASH_TITLE'] + '\n'
            'Leonard - started Sep 25, updated Sep 30\n\n'
            'Where we are\n'
            'About two months before we have to let people go unless the bridge or an engine deal lands. '
            'Keep enough aside to close the company properly (legal, final payroll, state filings). '
            'No new commitments without the three of us agreeing.\n\n'
            'Shutdown reserve\n'
            'Legal: ask our lawyer for a quote to wind down. Final payroll and accrued PTO through Gusto. '
            'Delaware franchise tax and the annual report are due in March whatever happens.\n\n'
            + P['DOC_CASH_MONEY'] + '\n\n'
            'Cuts\n'
            'Fred: marketing, UA and socials. Arthur: engineering, stores and data tools. '
            "I'll take software subscriptions and the card.\n\n"
            'Open\n'
            'Bridge: still talking to two funds. Engine: NCsoft is slow, follow up next week.\n')


def runs(body, heads):
    out, pos = [], 0
    tl = len(P['DOC_CASH_TITLE']) + 1
    out.append({'start': 0, 'end': tl, 'named_style': 'TITLE', 'list_id': None, 'list_nesting': 0})
    pos = tl
    for hd in heads:
        i = body.index('\n' + hd + '\n', pos) + 1
        if i > pos:
            out.append({'start': pos, 'end': i, 'named_style': 'NORMAL_TEXT', 'list_id': None, 'list_nesting': 0})
        out.append({'start': i, 'end': i + len(hd) + 1, 'named_style': 'HEADING_2', 'list_id': None, 'list_nesting': 0})
        pos = i + len(hd) + 1
    out.append({'start': pos, 'end': len(body), 'named_style': 'NORMAL_TEXT', 'list_id': None, 'list_nesting': 0})
    return out


heads = ['Where we are', 'Shutdown reserve', P['DOC_CASH_MONEY'].split('\n')[0], 'Cuts', 'Open']
DOCID = M['DOC_CASH']['id']
drive(DOCID, P['DOC_CASH_TITLE'], DOC, ROOTS[LEO], LEO, [(FRED, 'reader'), (ART, 'reader')],
      '2025-09-25T16:12:00Z', '2025-09-30T17:48:00Z')
ins('gdocs.docs_documents', ['document_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility', 'body_text',
                             'style_runs_json', 'revision_id', 'drive_file_id', 'created_time', 'modified_time'],
    [DOCID, P['DOC_CASH_TITLE'], LEO, js([FRED, ART]), 'private', DOC_BODY, js(runs(DOC_BODY, heads)),
     h('rev' + DOCID, 10), DOCID, '2025-09-25T16:12:00Z', '2025-09-30T17:48:00Z'], DOCID)

# Company Ops folder (destination)
drive(FOLDER_OPS, 'Company Ops', FOLDER, ROOTS[LEO], LEO, [(FRED, 'writer'), (ART, 'writer')],
      '2025-09-30T22:31:00Z', '2025-09-30T22:31:00Z')

# ------------------------------------------------------------------ Slack
SL_COLS = ['id', 'ts', 'channel_id', 'type', 'user_id', 'text', 'thread_parent_id', 'thread_ts_legacy', 'reply_count',
           'reply_users_count', 'latest_reply', 'is_activity_message', 'subtype', 'reactions_json', 'files_json',
           'attachments_json', 'created_at', 'metadata_json']


def slack(mid, ts, ch, user, text, at):
    ins('slack.slack_messages', SL_COLS, [mid, ts, ch, 'message', user, text, None, None, 0, 0, None, False, None,
                                          '[]', '[]', '[]', at, '{}'], f"{ch}/{ts}")


slack(DECOY90_ID, DECOY90_TS, 'C07C2866011', SLACK_U[LEO], P['S_DECOY90'], DECOY90_AT)
for k, who in [('S_CLAIM', LEO), ('S_ARTHUR_SUM', ART), ('S_HUB', LEO)]:
    m = M[k]
    slack(m['id'], m['ts'], m['channel'], SLACK_U[who], P[k], m['at'])

# ------------------------------------------------------------------ Trello
TC_COLS = ['id', 'name', '"idBoard"', '"idList"', '"desc"', 'pos', 'closed', 'due', '"dueComplete"', '"idMembers_json"',
           '"idLabels_json"', '"idShort"', '"shortLink"', '"shortUrl"', 'url', '"dateLastActivity"', 'cover_json',
           'badges_json']
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


cards = [('T_H1CARD', 'T_H1CREATE', P['H1_TITLE'], P['H1_DESC'], 456, 1327104.0, M['T_H1CMT']['at'], 1),
         ('T_ENGCARD', 'T_ENGCREATE', P['ENG_TITLE'], P['ENG_DESC'], 457, 1392640.0, M['T_ENGCARD']['at'], 0)]
CARDINFO = {}
for ck, ak, name, desc, short, pos, last, ncom in cards:
    cid = M[ck]['id']
    sl = shortlink(cid)
    CARDINFO[ck] = (cid, short, name, sl)
    url = f"https://PERSON_6092_TRELLO_USERNAME.com/c/{sl}/{short}-{slug(name)}"
    ins('trello.trello_cards', TC_COLS, [cid, name, HG_BOARD['id'], TODO['id'], desc, pos, False, None, False, '[]', '[]',
                                         short, None, None, url, last, None, js(badges(ncom))], cid)
    ins('trello.trello_actions', TA_COLS, [M[ak]['id'], 'createCard', M[ak]['at'], TR_ART, HG_BOARD['id'], cid, js(
        {"board": HG_BOARD, "card": {"id": cid, "idShort": short, "name": name, "shortLink": sl}, "list": TODO})],
        M[ak]['id'])
cid, short, name, sl = CARDINFO['T_H1CARD']
ins('trello.trello_actions', TA_COLS, [M['T_H1CMT']['id'], 'commentCard', M['T_H1CMT']['at'], TR_ART, HG_BOARD['id'], cid,
                                       js({"board": HG_BOARD, "card": {"id": cid, "idShort": short, "name": name,
                                                                       "shortLink": sl}, "idCard": cid, "list": TODO,
                                           "text": P['H1_CMT'], "textData": {"emoji": {}}})], M['T_H1CMT']['id'])

# ------------------------------------------------------------------ Gmail (Arthur -> Fred, cc Leonard)
G_AT = M['G_AMEND']['at']
G_SUBJ = P['H1_TITLE']               # new mail on the card's own title (no parent to reply to)
dt = D.datetime.fromisoformat(G_AT.replace('Z', '+00:00'))
ms = int(dt.timestamp() * 1000)
msgid = '<CAOOpSq6' + __import__('base64').b64encode(hashlib.sha256(b'g_amend').digest()).decode()[:35].replace('/', '_') + '@mail.gmail.com>'
body = P['G_AMEND_BODY'].replace('\n', '\r\n')
snippet = ' '.join(P['G_AMEND_BODY'].split())[:140]
hdrs = [{"name": "Message-ID", "value": msgid}, {"name": "Date", "value": email.utils.format_datetime(dt)},
        {"name": "Subject", "value": G_SUBJ}, {"name": "From", "value": f"Arthur Blake <{ART}>"},
        {"name": "To", "value": f"Frederick Stone <{FRED}>"}, {"name": "Cc", "value": f"Leonard Hayes <{LEO}>"}]
GM_COLS = ['id', 'thread_id', 'user_email', 'label_ids_json', 'snippet', 'internal_date', 'date', 'size_estimate', 'subject',
           'from_email', 'from_name', 'to_json', 'cc_json', 'bcc_json', 'reply_to_json', 'body_text', 'body_html',
           'headers_json', 'in_reply_to', '"references"', 'mbox_from', 'attachments_meta_json']


def gid(seed):
    return str(ms << 20 | int(h('g' + seed, 5), 16) & 0xFFFFF)


GTHREADS = {}
for box, labels in [(FRED, ["INBOX", "IMPORTANT", "CATEGORY_PERSONAL"]), (LEO, ["INBOX", "IMPORTANT", "CATEGORY_PERSONAL"]),
                    (ART, ["SENT"])]:
    tid = M['G_AMEND']['gmail_id'] if box == FRED else gid(box + G_AT)
    GTHREADS[box] = f"{box}/{tid}"
    ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [f"{box}/{tid}", box, snippet, None], f"{box}/{tid}")
    ins('gmail.gmail_messages', GM_COLS,
        [f"{box}/{msgid}", f"{box}/{tid}", box, js(labels), snippet, ms, G_AT, len(body) + 900, G_SUBJ, ART, 'Arthur Blake',
         js([f"Frederick Stone <{FRED}>"]), js([f"Leonard Hayes <{LEO}>"]), '[]', '[]', body, None, js(hdrs), None, None,
         None, '[]'], f"{box}/{msgid}")

# ------------------------------------------------------------------ Confluence (2024, superseded)
CONF_HTML = ('<p>' + P['CONF_BODY'] + '</p>'
             '<h2>What counts as an account</h2><ul><li>App stores (App Store Connect, Google Play Console)</li>'
             '<li>Ad networks and ad accounts (Meta, Google Ads, Unity Ads, AppLovin)</li>'
             '<li>Analytics and attribution tools</li><li>Social channels (YouTube, LinkedIn, TikTok)</li>'
             '<li>Cloud and source control (AWS, GitHub)</li></ul>'
             '<h2>Owner and backup</h2><p>The owner is the person who uses the account day to day. The backup is one of '
             'the founders with admin rights, so we can always get in if the owner is out. Shared logins go in the '
             'Company vault in 1Password, never in Slack or email.</p>'
             '<h2>When someone leaves</h2><ol><li>The backup takes over as owner the same day.</li>'
             '<li>Remove the leaver from every account they had a seat on and rotate any shared password.</li>'
             '<li>Pick a new backup.</li></ol>'
             '<p>Agencies and contractors get the narrowest role the platform offers and are removed when the '
             'engagement ends. Questions to Leonard.</p>')
CP = M['CONF_PAGE']
ins('confluence.confluence_pages', ['id', 'space_id', 'parent_id', 'title', 'body', 'body_format', 'status', 'version',
                                    'author_id', 'created_at', 'updated_at'],
    [CP['id'], 'space_COMPANY', 'page_company_home', P['CONF_TITLE'], CONF_HTML, 'storage', 'current', 1,
     'user_EMPLOYEE_0038', CP['at'], CP['at']], CP['id'])
ins('confluence.confluence_page_versions', ['id', 'page_id', 'number', 'title', 'body', 'author_id', 'message', 'created_at'],
    ['ver_' + h('ver' + CP['id'] + '1', 32), CP['id'], 1, P['CONF_TITLE'], CONF_HTML, 'user_EMPLOYEE_0038', None, CP['at']],
    'ver_' + h('ver' + CP['id'] + '1', 32))

# ------------------------------------------------------------------ write
n_ins = len(OUT)
svcs = sorted({k.split('.')[0] for k in ROWS})
head = ['-- Are you planning to inject? Yes',
        f'-- HarmonyGames injection - persona Frederick Stone <{FRED}> (Co-founder), Normal Horizon.',
        f'-- Services: {", ".join(svcs)}. Statements: {n_ins} INSERT (one row each), 0 UPDATE.',
        '-- Literal values only; parents before children; re-apply this exact SQL before every agent run.']
order = ['gdrive', 'gsheets', 'gdocs', 'slack', 'trello', 'gmail', 'confluence']
(ROOT / 'task_inputs/01_Universe_Inject.sql').write_text('\n'.join(head) + '\n' + '\n'.join(OUT) + '\n')
json.dump({'rows': ROWS, 'folder_sweep': FOLDER_SWEEP, 'folder_ops': FOLDER_OPS, 'decoy90': {'id': DECOY90_ID, 'ts': DECOY90_TS,
           'at': DECOY90_AT}, 'gmail_threads': GTHREADS, 'msgid': msgid, 'cards': CARDINFO, 'conf_ver': 'ver_' + h('ver' + CP['id'] + '1', 32)},
          open(HERE / 'sql_ids.json', 'w'), indent=1)
print(n_ins, {k: len(v) for k, v in ROWS.items()})
