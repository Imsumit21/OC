#!/usr/bin/env python3
"""Builds task_inputs/01_Universe_Inject.sql for frederick_dd_publishing.
Read-only on the base; writes only under Task_Authoring/task_inputs. Never executes SQL.
Row shapes follow base records and the accepted Q4 commitments injection (helpers adapted, no content reused)."""
import base64, datetime as D, email.utils, hashlib, json, re, sys
from pathlib import Path
sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
TI = HERE.parents[1]
sys.path.insert(0, str(HERE))
import build_scenario as B  # noqa: E402

FRED, LEO, ART, ROB = ('frederick.stone@harmonygames.co', 'leonard.hayes@harmonygames.co', 'arthur.blake@harmonygames.co', 'robert@harmonygames.co')
NAMES = {FRED: 'Frederick Stone', LEO: 'Leonard Hayes', ART: 'Arthur Blake', ROB: 'Robert'}
LOWER = {FRED: 'frederick stone', LEO: 'leonard hayes', ART: 'arthur blake', ROB: 'robert'}
ROOT_FRED, ROOT_LEO = 'd_175c0d7bc72ed244b944cb', 'd_63fffeb4fab5233ed5bb73'
SLACK_U = {LEO: 'EMPLOYEE_0038_SLACK_ID', ART: 'EMPLOYEE_0025_SLACK_ID', ROB: 'EMPLOYEE_0016_SLACK_ID', FRED: 'EMPLOYEE_0008_SLACK_ID'}
TR_FRED, TR_LEO = '4b4a68fc0fec0b254e4f9d8e', 'PERSON_6094_TRELLO_USER_ID'
BOARD = {'id': B.UABD_BOARD, 'name': 'UA/BD', 'shortLink': 'Fdkseaxw'}
BDLIST = {'id': B.BD_LIST, 'name': 'BD Follow Up'}
LIN_ART = 'usr_cc3e90160f490686'
ESG_P = ('PERSON_2694_EMAIL', 'PERSON_2694_NAME')
I, T, Q, BOD = B.IDS, B.T, B.Q, B.BODIES

def h(seed, n): return hashlib.sha256((B.SALT + seed).encode()).hexdigest()[:n]
def dt(iso): return D.datetime.fromisoformat(iso.replace('Z', '+00:00'))
def q(v):
    if v is None: return 'NULL'
    if isinstance(v, bool): return 'true' if v else 'false'
    if isinstance(v, (int, float)): return repr(v)
    s = str(v)
    if '\n' in s or '\\' in s or '\r' in s:
        return "E'" + s.replace('\\', '\\\\').replace("'", "''").replace('\r', '\\r').replace('\n', '\\n') + "'"
    return "'" + s.replace("'", "''") + "'"
def js(x): return json.dumps(x, ensure_ascii=False)
OUT, ROWS, IDS = {}, {}, {}
def ins(table, cols, vals, key):
    OUT.setdefault(table.split('.')[0], []).append(f"INSERT INTO {table} ({', '.join(cols)})\nVALUES ({', '.join(q(v) for v in vals)});")
    ROWS.setdefault(table, []).append(key)
def upd(table, sets, key_col, key):
    OUT.setdefault(table.split('.')[0], []).append(f"UPDATE {table} SET {', '.join(f'{k} = {q(v)}' for k, v in sets.items())} WHERE {key_col} = {q(key)};")
    ROWS.setdefault(table + ' (UPDATE)', []).append(key)
def trello_id(at, seed): return f"{int(dt(at).timestamp()):08x}" + h(seed, 16)
def thread_num(at, seed): return str((int(dt(at).timestamp() * 1000) << 20) + (int(h(seed, 8), 16) & 0xFFFFF))

# ============================================================ Drive / Docs / Sheets / Slides
DF_COLS = ['id', 'name', 'mime_type', 'parents_json', 'owner_email', 'shared_with_emails_json', 'shared_roles_json', 'visibility', 'owners_json', 'modified_time', 'created_time', 'trashed', 'starred']
FOLDER_MT, DOC_MT, SLIDE_MT, SHEET_MT = ('application/vnd.google-apps.folder', 'application/vnd.google-apps.document', 'application/vnd.google-apps.presentation', 'application/vnd.google-apps.spreadsheet')
def drive(fid, name, mime, parent, owner, shares, created, modified):
    ins('gdrive.drive_files', DF_COLS, [fid, name, mime, js([parent]), owner, js([e for e, _ in shares]), js([{'email': e, 'role': r} for e, r in shares]), 'private', js([owner]), modified, created, False, False], fid)
def doc(fid, title, body, parent, owner, shares, created, modified, heads=()):
    drive(fid, title, DOC_MT, parent, owner, shares, created, modified)
    first = len(body.split('\n', 1)[0])
    runs, pos = [{'start': 0, 'end': first + 1, 'named_style': 'TITLE', 'list_id': None, 'list_nesting': 0}], first + 1
    for hd in heads:
        i = body.index('\n' + hd + '\n', pos - 1) + 1
        if i > pos: runs.append({'start': pos, 'end': i, 'named_style': 'NORMAL_TEXT', 'list_id': None, 'list_nesting': 0})
        runs.append({'start': i, 'end': i + len(hd) + 1, 'named_style': 'HEADING_2', 'list_id': None, 'list_nesting': 0})
        pos = i + len(hd) + 1
    runs.append({'start': pos, 'end': len(body), 'named_style': 'NORMAL_TEXT', 'list_id': None, 'list_nesting': 0})
    ins('gdocs.docs_documents', ['document_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility', 'body_text', 'style_runs_json', 'revision_id', 'drive_file_id', 'created_time', 'modified_time'],
        [fid, title, owner, js([e for e, _ in shares]), 'private', body, js(runs), h('rev' + fid, 10), fid, created, modified], fid)
def sheet(fid, title, grid, tab, parent, owner, shares, created, modified):
    drive(fid, title, SHEET_MT, parent, owner, shares, created, modified)
    ins('gsheets.sheets_spreadsheets', ['spreadsheet_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility', 'drive_file_id', 'created_time', 'modified_time'],
        [fid, title, owner, js([e for e, _ in shares]), 'private', fid, created, modified], fid)
    ins('gsheets.sheets_sheets', ['spreadsheet_id', 'sheet_id', 'title', '"index"', 'row_count', 'column_count', 'grid_json'], [fid, 0, tab, 0, 1000, 26, js(grid)], f"{fid}#0")
def deck(fid, title, slides, parent, owner, shares, created, modified):
    drive(fid, title, SLIDE_MT, parent, owner, shares, created, modified)
    ins('gslides.slides_presentations', ['presentation_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility', 'drive_file_id', 'revision_id', 'created_time', 'modified_time'],
        [fid, title, owner, js([e for e, _ in shares]), 'private', fid, h('rev' + fid, 10), created, modified], fid)
    for i, (head, body) in enumerate(slides):
        sid = 'slide_' + h(fid + 's' + str(i), 12)
        ins('gslides.slides_pages', ['presentation_id', 'object_id', '"index"', 'layout', 'notes'], [fid, sid, i, 'TITLE_AND_BODY', None], f"{fid}#{sid}")
        for oid, ph, text, ordn, y, hgt in [('el_' + h(fid + 'e' + str(i), 12), 'TITLE', head, 0, 457200, 1143000), ('el_' + h(fid + 'b' + str(i), 12), 'BODY', body, 1, 1600200, 3200400)]:
            ins('gslides.slides_page_elements', ['presentation_id', 'page_object_id', 'object_id', 'kind', 'text', 'placeholder_type', 'x_emu', 'y_emu', 'width_emu', 'height_emu', 'table_json', 'ordinal'],
                [fid, sid, oid, 'SHAPE', text, ph, 457200, y, 8229600, hgt, None, ordn], f"{fid}#{oid}")
FOUNDERS = [(FRED, 'reader'), (ROB, 'reader'), (ART, 'reader')]
drive(I['dd_folder'], 'DD publishing', FOLDER_MT, ROOT_FRED, FRED, [(LEO, 'writer')], T['folder'], '2025-09-26T17:00:00Z')
doc(I['rule_doc'], 'DD publishing model: ground rules', Q['rules'], ROOT_LEO, LEO, FOUNDERS, T['rule_doc'], T['rule_doc'],
    ["Who's in", 'Status (first that fits, top to bottom)', 'Valuing a Live offer', 'Q4 cash', 'Keep value', 'First pick', 'Reminders', 'Layout'])
CODEV = ("Co-dev: what we'd take\nFred, Sep 19. For the co-dev talks only, not DD.\nThey fund a team of 6 to 10 for a fixed term.\nMilestones paid monthly, not on launch.\nWe keep the engine and the IP in the game.\nA 50/50 net split after they recoup the dev spend is the starting point.")
doc(I['codev_doc'], "Co-dev: what we'd take", CODEV, ROOT_FRED, FRED, [(LEO, 'reader')], T['codev_doc'], T['codev_doc'])
def contact_of(m):
    return f"{m['person'][0]} {m['person'][1]}" if m.get('person') else 'partnerships inbox'
def first_dates(m):
    return {1: 'May 2025', 2: 'Sep 2025', 3: 'Sep 24, 2025'}.get(m['tranche'], '')
GRID = [['Publisher', 'Contact', 'First contact', 'Tranche', 'What we sent']]
for m in B.M:
    if m['key'] in ('Copperleaf Games', 'Redwood Arcade'): continue
    if m['key'] == 'Appodeal': GRID.append(['Appodeal', 'their partnerships team', 'Apr 17, 2025', 'we applied', 'Intake form (DAU, ARPDAU)'])
    elif m['key'] == 'Rayking Game': GRID.append(['Rayking Game', 'their marketing manager', 'Sep 4, 2025 (to me)', 'came to us', 'nothing, they wrote first'])
    else: GRID.append([m['key'], contact_of(m), first_dates(m), str(m['tranche']), m['sent']])
GRID[0] += ['', BOD['sheet_note']]
sheet(I['outreach_sheet'], 'DD publisher outreach', GRID, 'Outreach', I['dd_folder'], FRED, [(LEO, 'reader')], T['outreach_sheet'], '2025-09-24T21:30:00Z')
deck(I['onepager_deck'], 'Domino Delights one-pager (May 2025)', [
     ('Domino Delights', 'A tile puzzle game with a hybrid IAP and rewarded-ad model. Live on iOS and Android in the US.'),
     ('Early numbers', 'First 3K installs, incentivized traffic. D1 retention 50%+. D7 retention 20%+. ARPDAU about $0.13.')],
     ROOT_FRED, FRED, [(LEO, 'reader')], T['onepager'], T['onepager'])
TERM_AT = {'Oakline Games': T['oakline_terms'], 'Tallwater Games': T['pb_terms'], 'Sunfold Mobile': T['sunfold_terms'], 'Harbor Lane Games': '2025-09-25T16:00:00Z',
           'Wavecrest Play': '2025-09-25T16:30:00Z', 'Moonrail Studios': T['moonrail_terms'], 'Northglow Publishing': '2025-09-26T16:00:00Z', 'Pinegrove Games': '2025-09-26T17:00:00Z'}
MEM = {m['key']: m for m in B.M}
def addr_of(m): return f"{m['person'][0].lower()}@{m['dom']}" if m.get('person') else f"partnerships@{m['dom']}"
def rep(m):
    return (addr_of(m), f"{m['person'][0]} {m['person'][1]}" if m.get('person') else m['key'])
for k, v in B.TERM_DOCS.items():
    m = MEM[k]
    parts = [x.strip() for x in re.split(r", (?=\$\d+,\d+ advance|\d+,\d+ installs|mobile stores|exclusive across|ownership of|respond by)", v)]
    title = f"{k} - term sheet - Domino Delights"
    body = title + "\nTerms for Harmony Games\n" + "\n".join(p[0].upper() + p[1:] for p in parts) + "\n" + f"{m['person'][0]} {m['person'][1]}, {k}"
    doc(B.term(k), title, body, I['dd_folder'], addr_of(m), [(FRED, 'reader')], TERM_AT[k], TERM_AT[k])

# ============================================================ Slack
SL_COLS = ['id', 'ts', 'channel_id', 'type', 'user_id', 'text', 'thread_parent_id', 'thread_ts_legacy', 'reply_count', 'reply_users_count', 'latest_reply', 'is_activity_message', 'subtype', 'reactions_json', 'files_json', 'attachments_json', 'created_at', 'metadata_json']
def slack(chan_ts, user, text, parent=None):
    ch, ts = chan_ts.split('/')
    mid = hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]
    ins('slack.slack_messages', SL_COLS, [mid, ts, ch, 'message', user, text, parent[0] if parent else None, parent[1] if parent else None, 0, 0, None, False, None, '[]', '[]', '[]',
        D.datetime.fromtimestamp(float(ts), D.UTC).strftime('%Y-%m-%dT%H:%M:%S.%fZ'), '{}'], chan_ts)
    return mid
IDS['slack_mid'] = {}
ROOTS = {'banker': ('330b95fd38236b4e7192e24f272685b4', '1757345405.134829', 3, 3), 'seventy': ('aaec7171d897e134a22b41511467f646', '1758736960.824899', 9, 1), 'matthew': ('0f6848b39af117c741af520ce5204eac', '1758147530.732569', 5, 2)}
def reply(name, chan_ts, user, text, root):
    rid, rts, rc, ru = ROOTS[root]
    IDS['slack_mid'][name] = slack(chan_ts, user, text, parent=(rid, rts))
    upd('slack.slack_messages', {'reply_count': rc, 'reply_users_count': ru, 'latest_reply': chan_ts.split('/')[1]}, 'id', rid)
IDS['slack_mid']['rayking_dm'] = slack(I['rayking_dm'], SLACK_U[FRED], Q['rayking_dm'])
reply('standing_line', I['standing_line'], SLACK_U[LEO], Q['standing'], 'matthew')
reply('copperleaf_relay', I['copperleaf_relay'], SLACK_U[ROB], Q['relay'], 'seventy')
IDS['slack_mid']['arthur_analytics'] = slack(I['arthur_analytics'], SLACK_U[ART], Q['analytics'])
IDS['slack_mid']['kestrel_post'] = slack(I['kestrel_post'], SLACK_U[ROB], Q['kestrel'])
reply('arthur_cash', I['arthur_cash'], SLACK_U[ART], Q['arthur_cash'], 'banker')

# ============================================================ Trello
TA_COLS = ['id', 'type', 'date', '"idMemberCreator"', '"idBoard"', '"idCard"', 'data_json']
TC_COLS = ['id', 'name', '"idBoard"', '"idList"', '"desc"', 'pos', 'closed', 'due', '"dueComplete"', '"idMembers_json"', '"idLabels_json"', '"idShort"', '"shortLink"', '"shortUrl"', 'url', '"dateLastActivity"', 'cover_json', 'badges_json']
def badges(comments, description):
    return {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0, "checkItemsChecked": 0, "checkItemsEarliestDue": None, "comments": comments, "description": description,
            "due": None, "dueComplete": False, "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False, "location": False, "maliciousAttachments": 0, "start": None, "votes": 0}
def card(key, cid, name, desc, short, idshort, pos, at, member, comment=None, members=None):
    last = comment[0] if comment else at
    ref = {'id': cid, 'idShort': idshort, 'name': name, 'shortLink': short}
    ins('trello.trello_cards', TC_COLS, [cid, name, BOARD['id'], BDLIST['id'], desc, pos, False, None, False, js(members or [member]), '[]', idshort, None, None,
        f"https://PERSON_6092_TRELLO_USERNAME.com/c/{short}/{idshort}-{name.lower().replace(' ', '-').replace('/', '-')}", last, None, js(badges(1 if comment else 0, bool(desc)))], cid)
    aid = trello_id(at, key + '-create'); IDS[key + '_create'] = aid
    ins('trello.trello_actions', TA_COLS, [aid, 'createCard', at, member, BOARD['id'], cid, js({"board": BOARD, "card": ref, "list": BDLIST})], aid)
    if comment:
        cat, ctext, cidn = comment
        ins('trello.trello_actions', TA_COLS, [cidn, 'commentCard', cat, member, BOARD['id'], cid, js({"board": BOARD, "card": ref, "idCard": cid, "list": BDLIST, "text": ctext, "textData": {"emoji": {}}})], cidn)
card('oakline_card', I['oakline_card'], 'F/up with Marek', '', 'Ok4mRw7T', 41, 81920.0, T['oakline_card'], TR_FRED, (T['oakline_card_comment'], Q['oak_card'], I['oakline_card_comment']))
card('sunfold_card', I['sunfold_card'], 'F/up with Lena', '', 'Sf9tLq2B', 42, 98304.0, T['sunfold_card'], TR_FRED, (T['sunfold_comment'], Q['sunfold_note'], I['sunfold_comment']))
card('dd_card', I['dd_card'], 'DD publishing', Q['card'], 'Dp3nVx8K', 43, 114688.0, T['dd_card'], TR_LEO, members=[TR_LEO, TR_FRED])
upd('trello.trello_boards', {'"dateLastActivity"': T['sunfold_comment']}, 'id', BOARD['id'])

# ============================================================ Gmail
GM_COLS = ['id', 'thread_id', 'user_email', 'label_ids_json', 'snippet', 'internal_date', 'date', 'size_estimate', 'subject', 'from_email', 'from_name', 'to_json', 'cc_json', 'bcc_json', 'reply_to_json', 'body_text', 'body_html', 'headers_json', 'in_reply_to', '"references"', 'mbox_from', 'attachments_meta_json']
INBOX = ["INBOX", "CATEGORY_PERSONAL"]
THREADS = {}
def addr(e, n): return f"{n} <{e}>"
def msgid_for(key, domain='mail.gmail.com'):
    return '<CA' + base64.b64encode(hashlib.sha256((B.SALT + key).encode()).digest()).decode()[:38].replace('/', '_').replace('+', '-') + f'@{domain}>'
def mail(key, at, subject, body, frm, to, cc, boxes, thread=None, parent=None, labels_for=None, tid=None, domain='mail.gmail.com'):
    d0 = dt(at); ms = int(d0.timestamp() * 1000); msgid = msgid_for(key, domain)
    body_r = body.replace('\r\n', '\n').replace('\n', '\r\n'); snippet = ' '.join(body.split())[:140]
    hdrs = [{"name": "Message-ID", "value": msgid}, {"name": "Date", "value": email.utils.format_datetime(d0)}, {"name": "Subject", "value": subject}, {"name": "From", "value": addr(*frm)}, {"name": "To", "value": ', '.join(addr(*x) for x in to)}]
    if cc: hdrs.append({"name": "Cc", "value": ', '.join(addr(*x) for x in cc)})
    pid = None
    if parent:
        pid = THREADS[parent]['last_msgid']
        hdrs += [{"name": "In-Reply-To", "value": pid}, {"name": "References", "value": ' '.join(THREADS[parent]['refs'] + [pid])}]
    root = thread or key
    if root not in THREADS: THREADS[root] = {'boxes': {}, 'refs': [], 'last_msgid': None}
    for box in boxes:
        if box in THREADS[root]['boxes']:
            tref = THREADS[root]['boxes'][box]; upd('gmail.gmail_threads', {'snippet': snippet}, 'id', tref)
        else:
            num = tid.split('/')[1] if (tid and box == FRED) else thread_num(at, f"{root}|{box}")
            tref = f"{box}/{num}"
            ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [tref, box, snippet, None], tref)
            THREADS[root]['boxes'][box] = tref
        labels = ["SENT"] if box == frm[0] else (labels_for or INBOX)
        ins('gmail.gmail_messages', GM_COLS, [f"{box}/{msgid}", tref, box, js(labels), snippet, ms, at, len(body_r) + 900, subject, frm[0], frm[1], js([addr(*x) for x in to]), js([addr(*x) for x in cc]), '[]', '[]', body_r, None, js(hdrs), pid,
            (' '.join(THREADS[root]['refs'] + [pid]) if pid else None), None, '[]'], f"{box}/{msgid}")
    if pid: THREADS[root]['refs'].append(pid)
    THREADS[root]['last_msgid'] = msgid
    return THREADS[root]['boxes'].get(FRED), f"{FRED}/{msgid}"
P = lambda e: (e, NAMES[e])
IDS['msg'] = {}
_, IDS['msg']['hub'] = mail('hub', T['hub'], 'DD publishing: what I need for Monday', Q['hub'], P(LEO), [P(FRED)], [], [FRED, LEO], tid=I['hub_thread'])
_, IDS['msg']['esg_note'] = mail('esg_note', T['esg_note'], 'License paper timing', Q['esg_note'] + "\n\nBest,\nPERSON_2694_NAME\nPARTNER, ESG Law", ESG_P, [P(LEO)], [P(FRED)], [FRED, LEO], tid=I['esg_thread'], thread='esg')
_, IDS['msg']['esg_leo'] = mail('esg_leo', T['esg_leonard'], 'Re: License paper timing', Q['esg_leo'] + "\n\nLeonard", P(LEO), [ESG_P], [P(FRED)], [FRED, LEO], thread='esg', parent='esg')
def greet(m): return m['person'][0] if m.get('person') else 'there'
OUT_AT = {1: ['2025-05-05T17:10:00Z', '2025-05-05T17:30:00Z', '2025-05-05T17:50:00Z', '2025-05-05T18:10:00Z', '2025-05-06T16:20:00Z', '2025-05-06T16:50:00Z', '2025-05-06T17:20:00Z', '2025-05-06T17:50:00Z'],
          2: ['2025-09-09T16:10:00Z', '2025-09-09T16:40:00Z', '2025-09-09T17:10:00Z', '2025-09-10T16:20:00Z', '2025-09-10T16:50:00Z', '2025-09-10T17:20:00Z', '2025-09-11T16:30:00Z', '2025-09-11T17:00:00Z'],
          3: ['2025-09-24T20:05:00Z', '2025-09-24T20:15:00Z', '2025-09-24T20:25:00Z', '2025-09-24T20:35:00Z', '2025-09-24T20:45:00Z', '2025-09-24T20:55:00Z']}
SUBJ = {1: 'Domino Delights: publishing partners', 2: 'Domino Delights on mobile', 3: 'Domino Delights publishing'}
PING = "Hi {first}, picking this back up. We're ready to talk about a mobile publishing deal for Domino Delights if you are."
PASS_AT = {'Fernhollow Media': '2025-05-13T15:10:00Z', 'Quietbay Games': '2025-05-15T15:20:00Z', 'Slatewood Mobile': '2025-09-17T15:30:00Z', 'Ironbridge Interactive': '2025-09-19T15:40:00Z', 'Tidewell Studios': '2025-09-29T15:50:00Z', 'Marlin Play': '2025-09-30T15:10:00Z'}
idx = {1: 0, 2: 0, 3: 0}; THREAD_IDS = {}
for m in B.M:
    k = m['key']
    if m.get('base') or k in ('Copperleaf Games', 'Redwood Arcade'): continue
    t = m['tranche']; at0 = OUT_AT[t][idx[t]]; idx[t] += 1
    tid = B.thr(k); subj = SUBJ[t]; r = rep(m); th = 't:' + k; n = [0]
    def step(at, who, body, domain='mail.gmail.com', labels=None):
        s = subj if n[0] == 0 else 'Re: ' + subj
        frm, to = (r, [P(FRED)]) if who == 'V' else (P(FRED), [r])
        _, mid = mail(f"m:{k}:{n[0]}", at, s, body, frm, to, [], [FRED], thread=th, parent=th if n[0] else None, tid=tid, domain=domain, labels_for=labels)
        IDS['msg'][f"{k}:{n[0]}"] = mid; n[0] += 1
    step(at0, 'F', BOD['out_t%d' % t].format(first=greet(m)) + "\n\nFrederick")
    sig = "\n\n" + (BOD['moonrail_sig'] if k == 'Moonrail Studios' else (f"{m['person'][0]} {m['person'][1]}\n{k}" if m.get('person') else k))
    if k in B.TERM_DOCS:
        if t == 1:
            step(D.datetime.fromisoformat(at0[:-1]).replace(tzinfo=D.UTC).__add__(D.timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%SZ'), 'V', BOD['later'][k] + sig)
            step('2025-09-24T21:%02d:00Z' % (5 + 10 * (idx[1] % 5)), 'F', PING.format(first=greet(m)) + "\n\nFrederick")
        step(TERM_AT[k], 'V', BOD['terms'][k] + sig)
        if k == 'Oakline Games':
            step(T['oakline_paid'], 'V', Q['oak_paid'] + sig)
    elif m['status'] == 'Passed':
        step(PASS_AT[k], 'V', BOD['pass'][k] + sig)
    elif k == 'Kitebridge Games':
        step('2025-09-26T16:00:00Z', 'V', BOD['kitebridge'] + sig)
    elif m.get('ack'):
        a0 = dt(at0) + D.timedelta(minutes=1)
        _, mid = mail(f"m:{k}:ack", a0.strftime('%Y-%m-%dT%H:%M:%SZ'), 'Automatic reply: ' + subj, BOD['summit_ack'], ('noreply@' + m['dom'], k), [P(FRED)], [], [FRED], thread=th, parent=th, tid=tid, labels_for=["INBOX", "CATEGORY_UPDATES"], domain=m['dom'])
        IDS['msg'][f"{k}:ack"] = mid
    THREAD_IDS[k] = THREADS[th]['boxes'][FRED]
    assert THREAD_IDS[k] == tid, (k, THREAD_IDS[k], tid)

# ============================================================ Calendar (+ INT-11 invitation mails)
GC_COLS = ['event_id', 'calendar_id', 'summary', 'description', 'location', 'start_ts', 'end_ts', 'start_json', 'end_json', 'organizer_email', 'creator_email', 'attendees_json', 'status', 'visibility', 'transparency', 'rrule_json', 'recurring_event_id', 'original_start_json', 'sequence', 'created', 'updated', 'hangout_link', 'ical_uid']
def event(key, summary, desc, start, end, organizer, attendees, cals, created, updated, first_id, hangout, rsvp):
    uid = h('uid' + key, 32) + '@hg4'; ids = {}
    for cal in cals:
        eid = first_id if cal == FRED else 'evt_' + h(key + cal, 22); att = []
        for e in attendees:
            a = {"email": e, "organizer": e == organizer, "responseStatus": rsvp.get(e, "needsAction")}
            if e == cal: a["self"] = True
            att.append(a)
        ins('gcal.gcal_events', GC_COLS, [eid, cal, summary, desc, None, start, end, js({"dateTime": start}), js({"dateTime": end}), organizer, organizer, js(att), 'confirmed', None, 'opaque', '[]', None, None, 0, created, updated, hangout, uid], eid)
        ids[cal] = eid
    IDS.setdefault('uid', {})[key] = uid
    IDS.setdefault('events', {})[key] = ids
    return ids
def invitation(key, at, summary, when_hdr, when_body, meet, organizer, guests, boxes):
    d0 = dt(at); ms = int(d0.timestamp() * 1000)
    for box in boxes:
        mid = f"<calendar-{h(key + box, 8)}-{h(key + box + '1', 4)}-{h(key + box + '2', 4)}-{h(key + box + '3', 4)}-{h(key + box + '4', 12)}@google.com>"
        subject = f"Invitation: {summary} @ {when_hdr} ({box})"
        body = (f"{summary}\r\n{when_body}\r\nPacific Time - Los Angeles\r\n\r\nJoin with Google Meet\r\n{meet}\r\n\r\n" + f"Organizer\r\n{NAMES[organizer]}\r\n{organizer}\r\n\r\nGuests\r\n{NAMES[organizer]} - organizer\r\n" + "\r\n".join(guests) + "\r\n")
        tref = f"{box}/{thread_num(at, key + box)}"; snippet = ' '.join(body.split())[:140]
        ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [tref, box, snippet, None], tref)
        hdrs = [{"name": "Message-ID", "value": mid}, {"name": "Date", "value": email.utils.format_datetime(d0)}, {"name": "Subject", "value": subject}, {"name": "From", "value": f"{LOWER[organizer]} <{organizer}>"}, {"name": "To", "value": ', '.join(guests)}]
        ins('gmail.gmail_messages', GM_COLS, [f"{box}/{mid}", tref, box, js(["INBOX", "CATEGORY_PERSONAL"]), snippet, ms, at, len(body) + 3000, subject, organizer, LOWER[organizer], js(guests), '[]', '[]', js([f"{LOWER[organizer]} <{organizer}>"]), body, None, js(hdrs), None, None, None, '[]'], f"{box}/{mid}")
PAOLA, DIEGO, SOFIA = addr_of(MEM['Tallwater Games']), addr_of(MEM['Harbor Lane Games']), addr_of(MEM['Wavecrest Play'])
event('pb_event', 'Tallwater follow-up', Q['pb_note'], T['pb_event'], '2025-09-29T19:00:00Z', LEO, [FRED, LEO, PAOLA], [FRED, LEO], '2025-09-26T17:00:00Z', T['pb_event_update'], I['pb_event'], 'https://meet.google.com/tqw-hrnd-mzx?hs=224', {LEO: 'accepted', FRED: 'accepted'})
invitation('inv_pb', '2025-09-26T17:00:00Z', 'Tallwater follow-up', 'Mon Sep 29, 2025 11:30am - 12pm (PDT)', 'Monday Sep 29, 2025 \u22c5 11:30am \u2013 12pm', 'https://meet.google.com/tqw-hrnd-mzx?hs=224', LEO, [FRED, PAOLA], [FRED])
event('harbor_event', 'Harbor Lane call', BOD['harbor_note'], T['harbor_event'], '2025-09-26T19:30:00Z', FRED, [FRED, DIEGO], [FRED], '2025-09-25T18:00:00Z', '2025-09-26T19:40:00Z', I['harbor_event'], 'https://meet.google.com/vbk-pjse-qtr?hs=224', {FRED: 'accepted'})
event('wavecrest_event', 'Wavecrest call', BOD['wavecrest_note'], T['wavecrest_event'], '2025-09-25T18:30:00Z', FRED, [FRED, SOFIA], [FRED], '2025-09-25T17:00:00Z', '2025-09-25T18:40:00Z', I['wavecrest_event'], 'https://meet.google.com/ydm-cawz-kfu?hs=224', {FRED: 'accepted'})
event('monday_event', 'DD publishing: execs', 'What each publisher would bring in, and which offer goes first.', '2025-10-06T17:00:00Z', '2025-10-06T18:00:00Z', LEO, [ART, FRED, LEO, ROB], [FRED, LEO, ROB, ART], T['hub'], T['hub'], I['monday_event'], 'https://meet.google.com/hgr-dtwq-mpn?hs=224', {LEO: 'accepted'})
invitation('inv_monday', T['hub'], 'DD publishing: execs', 'Mon Oct 6, 2025 10am - 11am (PDT)', 'Monday Oct 6, 2025 \u22c5 10am \u2013 11am', 'https://meet.google.com/hgr-dtwq-mpn?hs=224', LEO, [FRED, ROB, ART], [FRED, ROB, ART])

# ============================================================ Linear (Arthur's note on his own open ticket)
ins('linear.linear_comments', ['id', 'issue_id', 'author_id', 'parent_id', 'body', 'is_edited', 'created_at', 'updated_at', 'sequence'], [I['eng2362_comment'], 'ENG-2362', LIN_ART, None, Q['eng'], False, T['eng2362_comment'], T['eng2362_comment'], 1], I['eng2362_comment'])
upd('linear.linear_issues', {'updated_at': T['eng2362_comment']}, 'id', 'ENG-2362')

# ============================================================ Contacts
CT_COLS = ['contact_id', 'first_name', 'last_name', 'is_user', 'gender', 'status', 'job', 'email']
ins('contacts.contacts', CT_COLS, [I['anika_contact'], 'Anika', 'Rao', False, 'Unknown', 'Unknown', 'Partnerships, Kestrel Group', addr_of(MEM['Moonrail Studios'])], I['anika_contact'])
ins('contacts.contacts', CT_COLS, [I['lena_contact'], 'Lena', 'Fischer', False, 'Unknown', 'Unknown', 'Sunfold Mobile', addr_of(MEM['Sunfold Mobile'])], I['lena_contact'])

# ============================================================ write
order = ['gdrive', 'gdocs', 'gsheets', 'gslides', 'slack', 'trello', 'gmail', 'gcal', 'linear', 'contacts']
n_ins = sum(1 for s in OUT for x in OUT[s] if x.startswith('INSERT')); n_upd = sum(1 for s in OUT for x in OUT[s] if x.startswith('UPDATE'))
head = ['-- Are you planning to inject? Yes', f'-- HarmonyGames injection - persona Frederick Stone <{FRED}> (Co-founder), Long Horizon.', f'-- Services: {", ".join(order)}. Statements: {n_ins} INSERT (one row each), {n_upd} UPDATE.', '-- Literal values only; parents before children; re-apply this exact SQL before every agent run.', 'BEGIN;']
body = []
for s in order:
    body.append(f'-- {s}'); body += OUT.get(s, [])
(TI / '01_Universe_Inject.sql').write_text('\n'.join(head + body + ['COMMIT;']) + '\n')
IDS['threads'] = THREAD_IDS
json.dump({'ids': IDS, 'rows': ROWS}, open(HERE / 'sql_ids.json', 'w'), indent=1)
print(n_ins, 'INSERT', n_upd, 'UPDATE', {k: len(v) for k, v in ROWS.items()})
