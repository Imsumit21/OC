"""Builds task_inputs/01_Universe_Inject.sql for the Robert wind-down close-out scenario.

Read-only on the base; writes only under Task_Authoring-2/. Never executes SQL. Every id and planned wording comes from
minted_ids.json / planned_text.json / accounts.json (mint_ids.py).
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
ACC = json.load(open(HERE / 'accounts.json'))
A = ACC['accounts']

ROB, LEO, ART, OLI = 'robert@harmonygames.co', 'leonard.hayes@harmonygames.co', 'arthur.blake@harmonygames.co', 'oliver.brooks@harmonygames.co'
NAMES = {ROB: 'robert', LEO: 'leonard hayes', ART: 'arthur blake', OLI: 'Oliver Brooks'}
SLACK_U = {ROB: 'EMPLOYEE_0016_SLACK_ID', LEO: 'EMPLOYEE_0038_SLACK_ID', ART: 'EMPLOYEE_0025_SLACK_ID', OLI: 'EMPLOYEE_0003_SLACK_ID'}
ARTHUR, LEONARD, ROBERT, OLIVER = 'usr_cc3e90160f490686', 'usr_63fffeb4fab5233e', 'usr_Robert', 'usr_bdf01b53c6a92c5e'
TR_LEO = 'PERSON_6094_TRELLO_USER_ID'
BOARD = {'id': '640643a3fd8f3ca308d9318e', 'name': 'Harmony Games', 'shortLink': 'f4LGcmuh'}
LISTS = {'640643a3fd8f3ca308d93195': 'To Do', '640643a3fd8f3ca308d93197': 'Done'}
ART_ROOT = 'd_cc3e90160f490686039986'


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
SHEET, DOC = 'application/vnd.google-apps.spreadsheet', 'application/vnd.google-apps.document'


def drive(fid, name, mime, parent, owner, shares, created, modified):
    ins('gdrive.drive_files', DF_COLS, [fid, name, mime, js([parent]), owner, js([e for e, _ in shares]),
                                        js([{'email': e, 'role': r} for e, r in shares]), 'private', js([owner]),
                                        modified, created, False, False], fid)


dc = M['DOC_CONV']
doc_shares = [(LEO, 'writer'), (ART, 'writer'), (ROB, 'writer')]
title = dc['name']
body_lines = P['DOC_CONV'].split('\n')
DOC_TEXT = title + '\n' + '\n'.join(body_lines[1:]) + '\n'   # first planned line is the heading
drive(dc['id'], title, DOC, dc['parent'], dc['owner'], doc_shares, dc['created'], dc['at'])
tl = len(title) + 1
runs = [{'start': 0, 'end': tl, 'named_style': 'TITLE', 'list_id': None, 'list_nesting': 0},
        {'start': tl, 'end': len(DOC_TEXT), 'named_style': 'NORMAL_TEXT', 'list_id': None, 'list_nesting': 0}]
ins('gdocs.docs_documents', ['document_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility', 'body_text',
                             'style_runs_json', 'revision_id', 'drive_file_id', 'created_time', 'modified_time'],
    [dc['id'], title, dc['owner'], js([e for e, _ in doc_shares]), 'private', DOC_TEXT, js(runs), h('rev' + dc['id'], 10),
     dc['id'], dc['created'], dc['at']], dc['id'])

ZIP = 'f_' + h('drive-rb-helpshift-export', 22)
drive(ZIP, 'helpshift_export_2026-02-13.zip', 'application/zip', dc['parent'], dc['owner'],
      [(LEO, 'writer'), (ART, 'writer'), (ROB, 'writer'), (OLI, 'writer')], '2026-02-13T15:04:51Z', '2026-02-13T15:04:51Z')

ss = M['SHEET_SUBS']
sub_shares = [(LEO, 'writer'), (ROB, 'writer')]
drive(ss['id'], ss['name'], SHEET, ART_ROOT, ART, sub_shares, ss['created'], ss['at'])
ins('gsheets.sheets_spreadsheets', ['spreadsheet_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility',
                                    'drive_file_id', 'created_time', 'modified_time'],
    [ss['id'], ss['name'], ART, js([e for e, _ in sub_shares]), 'private', ss['id'], ss['created'], ss['at']], ss['id'])
grid = [['Vendor', 'Monthly']]
for part in P['SHEET_SUBS'].split('— ', 1)[1].split(' | '):
    v, amt = part.rsplit(' ', 1)
    grid.append([v, int(amt)])
ins('gsheets.sheets_sheets', ['spreadsheet_id', 'sheet_id', 'title', '"index"', 'row_count', 'column_count', 'grid_json'],
    [ss['id'], 0, 'Feb', 0, 1000, 26, js(grid)], f"{ss['id']}#0")

# =========================================================== Confluence
CONF_COLS = ['id', 'space_id', 'parent_id', 'title', 'body', 'body_format', 'status', 'version', 'author_id', 'created_at', 'updated_at']
VER_COLS = ['id', 'page_id', 'number', 'title', 'body', 'author_id', 'message', 'created_at']
cu = M['CONF_UA']
ua_html = ''.join(f'<p>{s.strip()}</p>' for s in re.split(r'(?<=\.) (?=\d\. |These)', P['CONF_UA']))
ins('confluence.confluence_pages', CONF_COLS, [cu['id'], cu['space'], 'page_ops_home', cu['title'], ua_html, 'storage',
                                                'current', 1, cu['author'], cu['at'], cu['at']], cu['id'])
vid = 'ver_' + h('ver' + cu['id'] + '1', 32)
ins('confluence.confluence_page_versions', VER_COLS, [vid, cu['id'], 1, cu['title'], ua_html, cu['author'], None, cu['at']], vid)

# =========================================================== Slack
SL_COLS = ['id', 'ts', 'channel_id', 'type', 'user_id', 'text', 'thread_parent_id', 'thread_ts_legacy', 'reply_count',
           'reply_users_count', 'latest_reply', 'is_activity_message', 'subtype', 'reactions_json', 'files_json',
           'attachments_json', 'created_at', 'metadata_json']
KEEP_ID, KEEP_TS = '6d8c8d8affd1255b13d8d875f1547e70', '1770933601.686309'
for k, who in (('S_GUSTO_REPLY', ART), ('S_OLIVER_CURSOR', OLI), ('S_ANCHOR', LEO)):
    m = M[k]
    parent = (KEEP_ID, KEEP_TS) if m['thread_ts'] else None
    ins('slack.slack_messages', SL_COLS, [m['id'], m['ts'], m['channel'], 'message', SLACK_U[who], P[k],
                                          parent[0] if parent else None, parent[1] if parent else None, 0, 0, None, False, None,
                                          '[]', '[]', '[]', m['at'], '{}'], m['locator'])
g = M['S_GUSTO_REPLY']
upd('slack.slack_messages', {'thread_ts_legacy': KEEP_TS, 'reply_count': 1, 'reply_users_count': 1, 'latest_reply': g['ts']},
    'id', KEEP_ID)

# =========================================================== Trello
TC_COLS = ['id', 'name', '"idBoard"', '"idList"', '"desc"', 'pos', 'closed', 'due', '"dueComplete"', '"idMembers_json"',
           '"idLabels_json"', '"idShort"', '"shortLink"', '"shortUrl"', 'url', '"dateLastActivity"', 'cover_json', 'badges_json']
TA_COLS = ['id', 'type', 'date', '"idMemberCreator"', '"idBoard"', '"idCard"', 'data_json']


def badges():
    return {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0,
            "checkItemsChecked": 0, "checkItemsEarliestDue": None, "comments": 0, "description": True,
            "due": None, "dueComplete": False, "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False,
            "location": False, "maliciousAttachments": 0, "start": None, "votes": 0}


def slug(s):
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


def shortlink(seed):
    return base64.b64encode(hashlib.sha256(seed.encode()).digest()).decode().replace('+', 'x').replace('/', 'Q')[:8]


TRELLO = json.load(open(WS / 'HarmonyGames_Other_Services/Services_Data/trello/data.json'))
used_short = {c.get('idShort') for c in TRELLO['cards'] if c['idBoard'] == BOARD['id']}
# the SVB card takes the next number after the board's last card (455)
SHORTS = {'T_SVB': 456}
CARDINFO = {}
for k in ('T_SVB',):
    c = M[k]
    short = SHORTS[k]
    sl = shortlink(c['id'])
    url = f"https://PERSON_6092_TRELLO_USERNAME.com/c/{sl}/{short}-{slug(c['name'])}"
    ins('trello.trello_cards', TC_COLS, [c['id'], c['name'], BOARD['id'], c['list'], P[k], 2.0, False,
                                         None, False, '[]', '[]', short, None, None, url, c['at'], None, js(badges())], c['id'])
    ins('trello.trello_actions', TA_COLS, [c['create_action'], 'createCard', c['at'], TR_LEO, BOARD['id'], c['id'], js(
        {"board": BOARD, "card": {"id": c['id'], "idShort": short, "name": c['name'], "shortLink": sl},
         "list": {"id": c['list'], "name": LISTS[c['list']]}})], c['create_action'])
    CARDINFO[k] = {'id': c['id'], 'idShort': short, 'shortLink': sl}

# =========================================================== Gmail
GM_COLS = ['id', 'thread_id', 'user_email', 'label_ids_json', 'snippet', 'internal_date', 'date', 'size_estimate', 'subject',
           'from_email', 'from_name', 'to_json', 'cc_json', 'bcc_json', 'reply_to_json', 'body_text', 'body_html',
           'headers_json', 'in_reply_to', '"references"', 'mbox_from', 'attachments_meta_json']
SENDER_NAME = {'PERSON_0728_EMAIL': 'PERSON_0728_NAME', 'PERSON_7731_EMAIL': 'PERSON_7731_NAME'}


def fmt_addr(e):
    if e in NAMES:
        return f'{NAMES[e]} <{e}>'
    return f'{SENDER_NAME.get(e, e.replace("_EMAIL", "_NAME"))} <{e}>'


THREAD_ROWS = set()
GLOG = {}


def mail(key, to, cc, reply_to=None, labels=("INBOX", "IMPORTANT", "CATEGORY_PERSONAL")):
    m = M[key]
    at, sender, subject = m['at'], m['from'], m['subject']
    dt = D.datetime.fromisoformat(at.replace('Z', '+00:00'))
    ms = int(dt.timestamp() * 1000)
    raw_id = m['message_id'][ROB].split('/', 1)[1]
    parent = M[reply_to]['message_id'][ROB].split('/', 1)[1] if reply_to else None
    body = P[key].replace('\n', '\r\n')
    snippet = ' '.join(P[key].split())[:140]
    hdrs = [{"name": "Message-ID", "value": raw_id}, {"name": "Date", "value": email.utils.format_datetime(dt)},
            {"name": "Subject", "value": subject}, {"name": "From", "value": fmt_addr(sender)},
            {"name": "To", "value": ', '.join(fmt_addr(e) for e in to)}]
    if cc:
        hdrs.append({"name": "Cc", "value": ', '.join(fmt_addr(e) for e in cc)})
    if parent:
        hdrs += [{"name": "In-Reply-To", "value": parent}, {"name": "References", "value": parent}]
    GLOG[key] = {}
    for box in m['mailboxes']:
        tid = (M[reply_to] if reply_to else m)['thread_id'][box]
        if tid not in THREAD_ROWS:
            ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [tid, box, snippet, None], tid)
            THREAD_ROWS.add(tid)
        else:
            upd('gmail.gmail_threads', {'snippet': snippet}, 'id', tid)
        mid = f"{box}/{raw_id}"
        ins('gmail.gmail_messages', GM_COLS,
            [mid, tid, box, js(list(labels)), snippet, ms, at, len(body) + 900, subject, sender,
             SENDER_NAME.get(sender, sender.replace('_EMAIL', '_NAME')) if sender not in NAMES else NAMES[sender],
             js([fmt_addr(e) for e in to]), js([fmt_addr(e) for e in cc]), '[]', '[]', body, None, js(hdrs), parent, parent,
             None, '[]'], mid)
        GLOG[key][box] = {'message': mid, 'thread': tid}


FOUNDERS_TO, FOUNDERS_CC = [LEO], [ROB, ART]
mail('G_SHERWOOD', FOUNDERS_TO, FOUNDERS_CC)
mail('G_SUNSET1', FOUNDERS_TO, FOUNDERS_CC)
mail('G_SUNSET2', FOUNDERS_TO, FOUNDERS_CC, reply_to='G_SUNSET1')
BILL = ("INBOX", "CATEGORY_UPDATES")
for k in sorted((k for k in M if k.startswith('G_') and k not in ('G_SHERWOOD', 'G_SUNSET1', 'G_SUNSET2')),
                key=lambda k: M[k]['at']):
    mail(k, [ROB], [], labels=BILL)

# =========================================================== GCal (one copy per attendee calendar)
GC = M['E_REVIEW']
GC_COLS = ['event_id', 'calendar_id', 'summary', 'description', 'location', 'start_ts', 'end_ts', 'start_json', 'end_json',
           'organizer_email', 'creator_email', 'attendees_json', 'status', 'visibility', 'transparency', 'rrule_json',
           'recurring_event_id', 'original_start_json', 'sequence', 'created', 'updated', 'hangout_link', 'ical_uid']
for cal, evt in GC['copies'].items():
    att = []
    for e in GC['attendees']:
        a = {"email": e, "organizer": e == LEO, "responseStatus": "accepted" if e in (LEO, 'PERSON_7731_EMAIL') else "needsAction"}
        if e == cal:
            a["self"] = True
        att.append(a)
    ins('gcal.gcal_events', GC_COLS, [evt, cal, GC['summary'], None, None, GC['start'], GC['end'],
                                      js({"dateTime": GC['start']}), js({"dateTime": GC['end']}), LEO, LEO, js(att), 'confirmed',
                                      None, 'opaque', '[]', None, None, 0, GC['created'], GC['at'],
                                      'https://meet.google.com/' + h('meet' + GC['ical_uid'], 3) + '-' + h('m2' + GC['ical_uid'], 4) + '-' + h('m3' + GC['ical_uid'], 3),
                                      GC['ical_uid']], evt)

# =========================================================== GitHub (Combo-Fighters #38, open)
REPO = 'harmonygames-Games/Combo-Fighters'
pr, cr = M['GH_PR'], M['GH_CR']
OLI_GH, CR_GH, CR_ACTOR = 'EMPLOYEE_0003_GITHUB_USERNAME', 'PERSON_6026_GITHUB_USERNAME', 'SVC_0321_GITHUB_USERNAME'
head_ref, head_sha, base_sha = 'oliver/final-build-settings', h('head' + pr['id'], 40), '4e9e1e94d7d89fb7ef9985d1a6c271421129888a'  # base: Combo-Fighters#37 base_sha (develop)
ins('github.github_pull_requests',
    ['id', 'repo_id', 'number', 'title', 'state', 'merged', 'draft', 'locked', 'author_login', 'merged_by_login', 'body',
     'base_ref', 'head_ref', 'base_sha', 'head_sha', 'merge_commit_sha', 'additions', 'deletions', 'changed_files',
     'labels_json', 'assignee_logins_json', 'requested_reviewer_logins_json', 'created_at', 'updated_at', 'merged_at',
     'closed_at', 'html_url'],
    [pr['id'], REPO, 38, pr['title'], 'open', False, False, False, OLI_GH, None,
     'Bumps the build number, turns off the debug overlay and points the release config at the live backend.',
     'develop', head_ref, base_sha, head_sha, None, 41, 12, 5, '[]', '[]', '[]', pr['at'], cr['at'], None, None, None], pr['id'])
ins('github.github_branches', ['id', 'repo_id', 'name', 'head_sha', 'protected', 'is_default'],
    [f'{REPO}:{head_ref}', REPO, head_ref, head_sha, False, False], f'{REPO}:{head_ref}')
ins('github.github_commits', ['sha', 'repo_id', 'message', 'authored_date', 'committed_date', 'author_login', 'author_name',
                              'author_email', 'committer_login', 'committer_name', 'committer_email', 'parent_shas_json'],
    [head_sha, REPO, 'final build settings', iso(ts_of(pr['at']) - 900), None, OLI_GH, 'Oliver Brooks',
     OLI, OLI_GH, 'Oliver Brooks', OLI, '[]'], head_sha)
ins('github.github_pull_request_commits', ['id', 'pr_id', 'commit_sha', 'position'], [f"{pr['id']}#c_0", pr['id'], head_sha, 0],
    f"{pr['id']}#c_0")
ins('github.github_pr_comments', ['id', 'pr_id', 'author_login', 'body', 'created_at', 'updated_at'],
    [cr['id'], pr['id'], CR_GH, P['GH_CR'], cr['at'], cr['at']], cr['id'])
ins('github.github_timeline_events', ['id', 'pr_id', 'event', 'actor_login', 'created_at', 'data_json'],
    [f"{pr['id']}#ev_1", pr['id'], 'commented', CR_ACTOR, cr['at'], '{}'], f"{pr['id']}#ev_1")

# =========================================================== Linear
lp = M['L_PROJECT']
ins('linear.linear_projects', ['id', 'team_id', 'name', 'summary', 'description', 'lead_id', 'priority', 'state', 'start_date',
                               'target_date', 'labels_json', 'links_json', 'is_archived', 'created_at', 'updated_at'],
    [lp['id'], lp['team'], lp['name'], None, P['L_PROJECT'], lp['lead'], 0, 'started', '2026-02-12', None, '[]', '[]', False,
     lp['at'], lp['at']], lp['id'])
ins('linear.linear_project_teams', ['id', 'project_id', 'team_id', 'created_at'],
    ['ptm_' + h('ptm' + lp['id'], 16), lp['id'], lp['team'], lp['at']], 'ptm_' + h('ptm' + lp['id'], 16))
for u in (ARTHUR, LEONARD, ROBERT):
    pmid = 'pmem_' + h('pmem' + lp['id'] + u, 16)
    ins('linear.linear_project_members', ['id', 'project_id', 'user_id', 'created_at'], [pmid, lp['id'], u, lp['at']], pmid)

SRC = {'Kapwing': "Leonard's subscriptions list (Feb 12)",
       'Layer': 'the #winddown lists', 'CodeRabbit': 'the #winddown lists', 'Cursor': 'the #winddown lists',
       'Zapier': 'the #winddown lists', 'GitHub': 'costs tab (hosting line)', 'Singular': 'costs tab ($6,250 line)',
       'Intuit': 'the #winddown keep list', 'QuickBooks': 'costs tab',
       '1Password': "Arthur's own list", 'Lucidchart': 'old receipts',
       'Google Ads': 'old receipts', 'Docusign': 'costs tab', 'Notarize': 'costs tab', 'UA Assets': 'costs tab'}
LC_COLS = ['id', 'issue_id', 'author_id', 'parent_id', 'body', 'is_edited', 'created_at', 'updated_at']
LI_COLS = ['id', 'project_id', 'team_id', 'parent_id', 'assignee_id', 'creator_id', 'state_id', 'cycle_id', 'identifier',
           'number', 'title', 'description', 'priority', 'estimate', 'due_date', 'started_at', 'completed_at', 'canceled_at',
           'archived_at', 'time_in_status_minutes', 'labels_json', 'links_json', 'relations_json', 'state_history_json',
           'is_archived', 'created_at', 'updated_at']
LINROWS = {}
for a in A:
    k = a['issue']
    last = max([a['created']] + [c[1] for c in a['comments']])
    desc = f"From {SRC.get(a['vendor'], 'costs tab')}."
    ins('linear.linear_issues', LI_COLS,
        [k, lp['id'], 'team_ENG', None, a['assignee'], ARTHUR, 'Todo', None, k, int(k.split('-')[1]), a['vendor'], desc, 0,
         None, None, None, None, None, None, None, '[]', '[]', '[]', '[]', False, a['created'], last], k)
    for j, (cid, (who, at, body, _dec)) in enumerate(zip(a['comment_ids'], a['comments']), 1):
        assert a['created'] < at < '2026-02-14', (k, at)
        ins('linear.linear_comments', LC_COLS, [cid, k, who, None, body, False, at, at], cid)
    LINROWS[k] = {'vendor': a['vendor'], 'comments': a['comment_ids'], 'updated_at': last, 'description': desc}

# =========================================================== write
order = ['gdrive', 'gdocs', 'gsheets', 'confluence', 'slack', 'trello', 'gmail', 'gcal', 'github', 'linear']
n_ins = sum(1 for s in OUT for x in OUT[s] if x.startswith('INSERT'))
n_upd = sum(1 for s in OUT for x in OUT[s] if x.startswith('UPDATE'))
head = ['-- Are you planning to inject? Yes',
        f'-- HarmonyGames injection - persona Robert <{ROB}> (Co-Founder & Creative Director), Long Horizon.',
        f'-- Services: {", ".join(order)}. Statements: {n_ins} INSERT (one row each), {n_upd} UPDATE.',
        '-- Literal values only; parents before children; re-apply this exact SQL before every agent run.', 'BEGIN;']
body = []
for s in order:
    body.append(f'-- ===================== {s.upper()} =====================')
    body += OUT[s]
(ROOT / 'task_inputs/01_Universe_Inject.sql').write_text('\n'.join(head + body + ['COMMIT;']) + '\n')
json.dump({'zip': ZIP, 'rows': ROWS, 'gmail': GLOG, 'cards': CARDINFO, 'linear': LINROWS, 'doc_text': DOC_TEXT},
          open(HERE / 'sql_ids.json', 'w'), indent=1)
print(n_ins, n_upd, {k: len(v) for k, v in ROWS.items()})
