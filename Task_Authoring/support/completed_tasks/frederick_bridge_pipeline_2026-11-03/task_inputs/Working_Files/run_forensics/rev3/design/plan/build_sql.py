#!/usr/bin/env python3
"""Builds task_inputs/01_Universe_Inject.sql for the Frederick bridge-pipeline scenario (injection rev1).
Read-only on the base; writes only under Task_Authoring/task_inputs. Never executes SQL."""
import base64, datetime as D, email.utils, hashlib, json, re
from pathlib import Path

HERE = Path(__file__).resolve().parent
TI = HERE.parents[1]
FRED, LEO, ART, ROB = ('frederick.stone@harmonygames.co', 'leonard.hayes@harmonygames.co',
                       'arthur.blake@harmonygames.co', 'robert@harmonygames.co')
NAMES = {FRED: 'Frederick Stone', LEO: 'Leonard Hayes', ART: 'Arthur Blake', ROB: 'Robert'}
ROOTS = {FRED: 'd_175c0d7bc72ed244b944cb', LEO: 'd_63fffeb4fab5233ed5bb73'}
SLACK_U = {LEO: 'EMPLOYEE_0038_SLACK_ID', ART: 'EMPLOYEE_0025_SLACK_ID', ROB: 'EMPLOYEE_0016_SLACK_ID'}
TR_LEO = 'PERSON_6094_TRELLO_USER_ID'
HG_BOARD = {'id': '640643a3fd8f3ca308d9318e', 'name': 'Harmony Games', 'shortLink': 'f4LGcmuh'}
DOING = {'id': '640643a3fd8f3ca308d93196', 'name': 'Doing'}
LIN_ART = 'usr_cc3e90160f490686'
ANTON, PAUL, EDITH, ILSE = 'PERSON_9901_EMAIL', 'PERSON_9902_EMAIL', 'PERSON_9903_EMAIL', 'PERSON_9904_EMAIL'
HIRO_DIR = 'PERSON_5282_EMAIL'                       # Hiro Capital Investment Director (base thread 1842278433020808799)
KARTHIC = 'PERSON_3242_EMAIL'                        # T-Accelerate (base thread 1842283406259093714)
DENTSU = [('PERSON_2581_EMAIL', 'PERSON_2581_NAME'), ('PERSON_5584_EMAIL', 'PERSON_5584_NAME'),
          ('PERSON_5221_EMAIL', 'PERSON_5221_NAME')]
DOCUSIGN = ('SVC_1302_EMAIL', 'SVC_1302_NAME')
CLOCK = '2025-10-01T00:00:00Z'


def h(seed, n):
    return hashlib.sha256(seed.encode()).hexdigest()[:n]


def dt(iso):
    return D.datetime.fromisoformat(iso.replace('Z', '+00:00'))


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
    svc = table.split('.')[0]
    OUT.setdefault(svc, []).append(f"INSERT INTO {table} ({', '.join(cols)})\nVALUES ({', '.join(q(v) for v in vals)});")
    ROWS.setdefault(table, []).append(key)


def upd(table, sets, key_col, key):
    svc = table.split('.')[0]
    OUT.setdefault(svc, []).append(f"UPDATE {table} SET {', '.join(f'{k} = {q(v)}' for k, v in sets.items())} "
                                   f"WHERE {key_col} = {q(key)};")


def tid(at, k):
    ms = int(dt(at).timestamp() * 1000)
    return str((ms << 20) + k)


def trello_id(at, seed):
    return f"{int(dt(at).timestamp()):08x}" + h(seed, 16)


# ============================================================ texts (seeded claims and evidence; no conclusions)
HUB_SUBJ = 'Oct 14 board pre-read - fundraising section'
HUB_BODY = """Fred,

I'm flying to LA tomorrow morning for the Griffin AGM and the Dentsu meeting, so can you own the fundraising section of the Oct 14 pre-read? I'll stitch it into the deck when I'm back.

What I need is where every firm on the 2025 game investor list, plus anyone we've had a call with since the Sep 3 kickoff who isn't on it, stands as of tonight. One sheet, one row per firm. Please use the buckets and definitions in the board pre-read template so it matches the other sections. The money lines matter most, the board will ask what's actually committed.

Please put the sheet in your Board - Oct 14 2025 folder, the README in that folder says how to name it. Whatever the Existing Investor Update card says to do for firms that pass, do that too. The Board Deck card says which numbers the slide takes, so once it's done reply here with the numbers the fundraising slide needs. I put Monday's review on your calendar so we can go through it together.

Robert asked about emailing the pipeline straight to the board. Let's not, it goes in the deck.

Thanks,
Leonard"""

TEMPLATE_TITLE = 'Board pre-read - fundraising section (Oct 14)'
TEMPLATE_BODY = TEMPLATE_TITLE + """
Leonard, Sep 26. Same layout as the other sections of the pre-read.

Who goes in the table
One row per name on the 2025 game investor list, angels included. The list has a few names twice, and a repeated name is still one row. Add any firm not on the list that we've had a pitch call or meeting with since we kicked off the bridge on Sep 3. A call counts when it's on our calendars. Investment talks only, strategic investors included. Service or work-for-hire deals, publishing-only talks and calls with other engine companies don't go in.

Status, as of end of day Tue Sep 30 (Pacific)
Passed: they told us no for this round in writing. A pass one of us heard by phone counts once it is written in #bridge-pitch.
In talks: we've had a call or meeting this round and they haven't passed.
Awaiting reply: we reached out this round, no call yet and no answer.
Not contacted this round: nothing from us since Sep 3.
A partner writing from their own address counts for their firm. If the name doesn't ring a bell, check contacts and the earlier threads.

Last two-way contact
Date of the latest message or call where both sides took part, Pacific.

Money
Committed: signed SAFE only, meaning the DocuSign Completed notice is in.
Soft-circled: a yes in writing with an amount that isn't signed yet. Use the latest amount the investor gave us.
Put the committed and soft-circled totals at the bottom of the sheet.

Build access
For firms in talks: whether they are on the tester list for the current internal Zombie Match 3D build, TestFlight on iOS and the Play internal test track on Android. The public App Store page doesn't count. Arthur tracks the tester adds.
"""
TEMPLATE_OLD_TITLE = 'Board pre-read - fundraising section'
TEMPLATE_OLD_BODY = TEMPLATE_OLD_TITLE + """
Leonard, for the Jul 16 board.

Table
One row per firm we've spoken to since the April update. Status: Passed, Active, Cold.

Money
Committed: a verbal yes from a named investor or angel, with an amount.
Interested: said they'd look at it, no amount.
Show committed at the top, it's the first thing Griffin asks.

Notes
Keep it to one page. Robert adds the product slide, Arthur the tech slide.
"""
README_TITLE = 'README - Oct 14 board materials'
README_BODY = README_TITLE + """
One file per section in this folder, named "<section> - Oct 14 board", e.g. "Fundraising - Oct 14 board" or "Product - Oct 14 board".
Google Sheets or Docs only, no uploads, so I can link them from the deck.
Leonard collects everything on Monday Oct 6.
"""
DECK_TITLE = 'HG BoD Oct 14 2025 (draft)'
DECK = [
    ('Harmony Games Board Meeting\nOctober 14, 2025 (draft)', None),
    ('Agenda\nQ3 recap / Zombie Match 3D alpha / Engine / Fundraising / Runway and options', None),
    ('Q3 recap\nDomino Delights: publisher search\nZombie Match 3D: alpha builds on iOS and Android', None),
    ('Zombie Match 3D\nAlpha metrics (Robert to fill)', None),
    ('Engine\nWhat shipped in Q3 (Arthur to fill)', None),
    ('Team\nHeadcount and contractors (Leonard to fill)', None),
    ('Runway\nCash and burn (Leonard to fill)', None),
    ('Options\nBridge / co-dev / engine deals', None),
    ('Fundraising\nBridge round, pipeline as of Sep 30\nFirms on the list: __   Committed: $__   Soft-circled: $__\n'
     'Table from Fred\'s sheet: firm, status, last two-way contact, build access for firms in talks, committed, soft-circled', None),
    ('Asks for the board\nIntros, especially games funds and strategics', None),
    ('Appendix\nInvestor FAQ (link)', None),
    ('Thank you', None),
]
CARD_DECK_NAME = 'Board Deck - Oct 14'
CMT_DECK = ("Fundraising slide takes three numbers from Fred's sheet: how many firms are on it, total committed and "
            "total soft-circled. Slide 9 of the draft deck lists the table's columns.")
CMT_KEEPWARM = ("Going forward: anyone who passes on the bridge after we've actually pitched them (a call or meeting) goes on "
                "a Keep warm checklist on this card, one item per firm, so they get the Q4 update with the rest. Email-only "
                "no's don't need it.")
S_ANGELS = ("angel update: Paul Heydon is in for $50K and Anton Bernstein for $40K on the SAFE. sending the docs through "
            "docusign next week. not a round but it buys us a bit")
S_ARTHUR = "for the board pipeline I'd just list who Leonard emailed this month, the rest of that list is noise imo"
S_ROB_ROOT = "going to drop notes from my phone calls in the firm threads here so they're written down somewhere"
S_ROB_SCIPLAY = ("Sciplay - D called me this morning, they're out for this round. too early on metrics for them. "
                 "said keep them posted when we hit beta")
ROB_MAIL_SUBJ = 'board pipeline'
ROB_MAIL_BODY = ("Fred - for the 14th could you just email the pipeline to the board directly once it's done? saves Leonard "
                 "a step.\n\nRobert")
ANTON_SUBJ = 'SAFE amount'
ANTON_BODY = ("Leonard,\n\nHad another look at my numbers. I can do $25K this time, not the 40 we talked about. Send the docs "
              "over at 25 and I'll sign.\n\nAnton")
PAUL_SUBJ = 'SAFE in DocuSign'
PAUL_BODY = ("Hi Paul,\n\nGentle nudge on the SAFE in DocuSign, it's still sitting with you. Would love to have it signed "
             "before the board meets on the 14th.\n\nThanks,\nLeonard")
DS_DOC = 'Harmony Games SAFE - Anton Bernstein.pdf'
DS_SUBJ = f'Completed: Complete with docusign: {DS_DOC}'
DS_BODY = (f"Hello Frederick Stone,\r\n\r\nAll signers completed Complete with docusign: {DS_DOC}\r\n\r\n"
           "Review the document your Recipients have signed\r\n\r\n"
           "https://na4.docusign.net/member/EmailStart.aspx?m=[IDENTIFIER_99011]\r\n\r\n"
           "If clicking the link does not work, you can highlight and copy the entire line above and paste it into your "
           "browser to get started.\r\n\r\nThis message was sent to you by Leonard Hayes who is using the docusign Electronic "
           "Signature Service. If you would rather not receive email from this sender you may contact the sender with your "
           "request.\r\n\r\nDo Not Share This Email\r\nThis email contains a secure link to docusign. Please do not share this "
           "email, link, or access code with others.")
HIRO_SUBJ = 'Harmony Games bridge'
HIRO_BODY = ("Leonard,\n\nThanks again for the session on Tuesday. We discussed it as a team yesterday and we're going "
             "to pass on the bridge. Without live KPIs it's too early for our games fund, but we'd be "
             "glad to stay in touch as Zombie Match gets to beta.\n\nBest,\nEdith\n\nEdith Vane | Partner")
DENTSU_SUBJ = 'Zombie Match 3D access'
DENTSU_RYO_BODY = ("Leonard-san,\n\nThank you for the offer. Please add the three of us with these addresses:\n"
                   "PERSON_2581_EMAIL\nPERSON_5584_EMAIL\nPERSON_5221_EMAIL\n\nBest regards,\nRyo")
DENTSU_BODY = ("Koji-san, Ryo-san and team,\n\nThank you for sending your emails. Invites for Zombie Match 3D are out to all "
               "three of you.\n\nLooking forward to seeing you in LA on Oct 1.\n\nBest regards,\nLeonard")
BRIGHT_SUBJ = 'Harmony Games - follow up'
BRIGHT_BODY = ("Hi Ilse,\n\nThanks for the time this morning. I'll send the deck and the puzzle engine doc over in a "
               "separate email. Happy to set up a longer session with your partners next week if that's useful.\n\nBest,\nLeonard")
BRIGHT_RE_BODY = ("Thanks Leonard. I'll brief the partners and come back to you next week on a second meeting.\n\n"
                  "Ilse Marrow | Principal, Brightwater Games Fund")
LIN_TITLE = 'Investor testers on ZM internal tracks'
LIN_DESC = ("Adding investor testers to the Zombie Match 3D TestFlight group and the Play internal test track. "
            "One comment per firm as the adds land.")
LIN_C_TACC = "T-Accelerate (Karthic, Rutik): TestFlight added Sep 22, Play internal track added Sep 23, Karthic confirmed it installs."
LIN_C_DENTSU = ("Dentsu (3 accounts from Ryo-san, came in Thursday night): TestFlight added. Play internal track not added yet, I don't "
                "have console owner rights on that app, Leonard does. Will chase Thursday.")

# ============================================================ minted ids and times
T = {
    'TEMPLATE_OLD': ('f_8d2c47a91e05b3f6d7c418', '2025-07-08T18:00:00Z', '2025-07-10T16:12:00Z'),
    'TEMPLATE': ('f_3b9e61c04d7a52e8f1a6c2', '2025-09-26T18:00:00Z', '2025-09-26T18:41:00Z'),
    'FOLDER': ('d_5e8a1c3f9b07d2e64a1b93', '2025-09-26T18:20:00Z', '2025-09-26T18:20:00Z'),
    'README': ('f_c61a0e93b7d24f58a2e917', '2025-09-26T18:30:00Z', '2025-09-26T18:33:00Z'),
    'DECK': ('f_a47d0e2c95b18f63e2c0d5', '2025-09-27T17:00:00Z', '2025-09-28T04:40:00Z'),
}
G_HUB_AT = '2025-09-30T21:05:00Z'
S_ANGELS_AT, S_ARTHUR_AT = '2025-09-19T17:40:00Z', '2025-09-29T18:00:00Z'
S_ROB_ROOT_AT, S_ROB_SCI_AT = '2025-09-29T16:00:00Z', '2025-09-29T22:14:00Z'
ROOT_0912 = ('73c2247f4a31f32d10b3068ecd1d13ac', '1757716998.377299')
KW_CMT_AT = '2025-09-14T04:20:00Z'
DECKCARD_AT = '2025-09-27T17:05:00Z'
DECK_CMT_AT = '2025-09-27T17:30:24Z'

# ============================================================ Drive / Docs / Slides
DF_COLS = ['id', 'name', 'mime_type', 'parents_json', 'owner_email', 'shared_with_emails_json', 'shared_roles_json',
           'visibility', 'owners_json', 'modified_time', 'created_time', 'trashed', 'starred']
FOLDER_MT, DOC_MT, SLIDE_MT = ('application/vnd.google-apps.folder', 'application/vnd.google-apps.document',
                               'application/vnd.google-apps.presentation')


def drive(fid, name, mime, parent, owner, shares, created, modified):
    ins('gdrive.drive_files', DF_COLS,
        [fid, name, mime, js([parent]), owner, js([e for e, _ in shares]),
         js([{'email': e, 'role': r} for e, r in shares]), 'private', js([owner]), modified, created, False, False], fid)


def doc(key, title, body, parent, owner, shares, heads=()):
    fid, created, modified = T[key]
    drive(fid, title, DOC_MT, parent, owner, shares, created, modified)
    runs, pos = [{'start': 0, 'end': len(title) + 1, 'named_style': 'TITLE', 'list_id': None, 'list_nesting': 0}], len(title) + 1
    for hd in heads:
        i = body.index('\n' + hd + '\n', pos - 1) + 1
        if i > pos:
            runs.append({'start': pos, 'end': i, 'named_style': 'NORMAL_TEXT', 'list_id': None, 'list_nesting': 0})
        runs.append({'start': i, 'end': i + len(hd) + 1, 'named_style': 'HEADING_2', 'list_id': None, 'list_nesting': 0})
        pos = i + len(hd) + 1
    runs.append({'start': pos, 'end': len(body), 'named_style': 'NORMAL_TEXT', 'list_id': None, 'list_nesting': 0})
    ins('gdocs.docs_documents', ['document_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility', 'body_text',
                                 'style_runs_json', 'revision_id', 'drive_file_id', 'created_time', 'modified_time'],
        [fid, title, owner, js([e for e, _ in shares]), 'private', body, js(runs), h('rev' + fid, 10), fid, created,
         modified], fid)


FOUNDER_READ = [(FRED, 'reader'), (ROB, 'reader'), (ART, 'reader')]
doc('TEMPLATE_OLD', TEMPLATE_OLD_TITLE, TEMPLATE_OLD_BODY, ROOTS[LEO], LEO, FOUNDER_READ, ['Table', 'Money', 'Notes'])
doc('TEMPLATE', TEMPLATE_TITLE, TEMPLATE_BODY, ROOTS[LEO], LEO, FOUNDER_READ,
    ['Who goes in the table', 'Status, as of end of day Tue Sep 30 (Pacific)', 'Last two-way contact', 'Money',
     'Build access'])
fid, created, modified = T['FOLDER']
drive(fid, 'Board - Oct 14 2025', FOLDER_MT, ROOTS[FRED], FRED, [(LEO, 'writer')], created, modified)
doc('README', README_TITLE, README_BODY, T['FOLDER'][0], LEO, [(FRED, 'writer')])

fid, created, modified = T['DECK']
drive(fid, DECK_TITLE, SLIDE_MT, ROOTS[LEO], LEO, FOUNDER_READ, created, modified)
ins('gslides.slides_presentations', ['presentation_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility',
                                     'drive_file_id', 'revision_id', 'created_time', 'modified_time'],
    [fid, DECK_TITLE, LEO, js([e for e, _ in FOUNDER_READ]), 'private', fid, h('rev' + fid, 10), created, modified], fid)
for i, (txt, notes) in enumerate(DECK):
    sid, eid = 'slide_' + h(fid + 's' + str(i), 12), 'el_' + h(fid + 'e' + str(i), 12)
    ins('gslides.slides_pages', ['presentation_id', 'object_id', '"index"', 'layout', 'notes'],
        [fid, sid, i, 'BLANK', notes], f"{fid}#{sid}")
    title, _, rest = txt.partition('\n')
    parts = [(eid, 'TITLE', title, 0, 457200, 1143000)] + ([('el_' + h(fid + 'b' + str(i), 12), 'BODY', rest, 1, 1600200, 3200400)] if rest else [])
    for oid, ph, text, ordn, y, hgt in parts:
        ins('gslides.slides_page_elements', ['presentation_id', 'page_object_id', 'object_id', 'kind', 'text',
                                             'placeholder_type', 'x_emu', 'y_emu', 'width_emu', 'height_emu', 'table_json',
                                             'ordinal'],
            [fid, sid, oid, 'SHAPE', text, ph, 457200, y, 8229600, hgt, None, ordn], f"{fid}#{oid}")

# Leonard's angel tracker (stale after Sep 20; never updated)
ANG = ('f_6e1d93a0c4b72f85d39a0e', '2025-09-19T17:52:00Z', '2025-09-20T03:15:00Z')
drive(ANG[0], 'Bridge angels', 'application/vnd.google-apps.spreadsheet', ROOTS[LEO], LEO, FOUNDER_READ, ANG[1], ANG[2])
ins('gsheets.sheets_spreadsheets', ['spreadsheet_id', 'title', 'owner_email', 'shared_with_emails_json', 'visibility',
                                    'drive_file_id', 'created_time', 'modified_time'],
    [ANG[0], 'Bridge angels', LEO, js([e for e, _ in FOUNDER_READ]), 'private', ANG[0], ANG[1], ANG[2]], ANG[0])
ins('gsheets.sheets_sheets', ['spreadsheet_id', 'sheet_id', 'title', '"index"', 'row_count', 'column_count', 'grid_json'],
    [ANG[0], 0, 'Angels', 0, 1000, 26, js([['Name', 'Amount', 'Status', 'Notes'],
                                           ['Paul Heydon', 50000, 'in', 'docs via docusign next week'],
                                           ['Anton Bernstein', 40000, 'in', 'docs via docusign next week']])], f"{ANG[0]}#0")
IDS['SHEET_ANGELS'] = ANG[0]

# ============================================================ Slack
SL_COLS = ['id', 'ts', 'channel_id', 'type', 'user_id', 'text', 'thread_parent_id', 'thread_ts_legacy', 'reply_count',
           'reply_users_count', 'latest_reply', 'is_activity_message', 'subtype', 'reactions_json', 'files_json',
           'attachments_json', 'created_at', 'metadata_json']


def sts(at):
    return f"{dt(at).timestamp():.0f}." + {S_ANGELS_AT: '418207', S_ARTHUR_AT: '117903', S_ROB_ROOT_AT: '226431',
                                           S_ROB_SCI_AT: '552871'}[at]


def slack(ch, user, text, at, parent=None):
    ts = sts(at)
    mid = h(f"{ch}|{ts}", 32)
    ins('slack.slack_messages', SL_COLS, [mid, ts, ch, 'message', user, text, parent[0] if parent else None,
                                          parent[1] if parent else None, 0, 0, None, False, None, '[]', '[]', '[]',
                                          at.replace('Z', '.000000Z'), '{}'], f"{ch}/{ts}")
    return f"{ch}/{ts}", mid


IDS['S_ANGELS'], _ = slack('C07C2866011', SLACK_U[LEO], S_ANGELS, S_ANGELS_AT)
IDS['S_ARTHUR'], _ = slack('C07C2866011', SLACK_U[ART], S_ARTHUR, S_ARTHUR_AT)
IDS['S_ROB_ROOT'], _ = slack('C096HFA5Z8W', SLACK_U[ROB], S_ROB_ROOT, S_ROB_ROOT_AT)
IDS['S_ROB_SCI'], _ = slack('C096HFA5Z8W', SLACK_U[ROB], S_ROB_SCIPLAY, S_ROB_SCI_AT, parent=ROOT_0912)
upd('slack.slack_messages', {'reply_count': 1, 'reply_users_count': 1, 'latest_reply': sts(S_ROB_SCI_AT),
                             'thread_ts_legacy': ROOT_0912[1]}, 'id', ROOT_0912[0])

# ============================================================ Trello
TA_COLS = ['id', 'type', 'date', '"idMemberCreator"', '"idBoard"', '"idCard"', 'data_json']
TC_COLS = ['id', 'name', '"idBoard"', '"idList"', '"desc"', 'pos', 'closed', 'due', '"dueComplete"', '"idMembers_json"',
           '"idLabels_json"', '"idShort"', '"shortLink"', '"shortUrl"', 'url', '"dateLastActivity"', 'cover_json',
           'badges_json']


def badges(comments, description):
    return {"attachments": 0, "attachmentsByType": {"trello": {"board": 0, "card": 0}}, "checkItems": 0,
            "checkItemsChecked": 0, "checkItemsEarliestDue": None, "comments": comments, "description": description,
            "due": None, "dueComplete": False, "externalSource": None, "fogbugz": "", "lastUpdatedByAi": False,
            "location": False, "maliciousAttachments": 0, "start": None, "votes": 0}


KW = {'id': '68c5a49e8491a9d7faf869d0', 'idShort': 455, 'name': 'Existing Investor Update', 'shortLink': 'MfMCBpMm'}
IDS['TR_KW_CMT'] = trello_id(KW_CMT_AT, 'kw-comment')
ins('trello.trello_actions', TA_COLS, [IDS['TR_KW_CMT'], 'commentCard', KW_CMT_AT, TR_LEO, HG_BOARD['id'], KW['id'],
                                       js({"board": HG_BOARD, "card": KW, "idCard": KW['id'], "list": DOING,
                                           "text": CMT_KEEPWARM, "textData": {"emoji": {}}})], IDS['TR_KW_CMT'])
upd('trello.trello_cards', {'badges_json': js(badges(1, False)), '"dateLastActivity"': KW_CMT_AT}, 'id', KW['id'])
upd('trello.trello_boards', {'"dateLastActivity"': '2025-09-27T17:30:24Z'}, 'id', HG_BOARD['id'])

IDS['TR_DECKCARD'] = trello_id(DECKCARD_AT, 'deck-card')
sl = base64.b64encode(hashlib.sha256(IDS['TR_DECKCARD'].encode()).digest()).decode().replace('+', 'x').replace('/', 'Q')[:8]
DC = {'id': IDS['TR_DECKCARD'], 'idShort': 466, 'name': CARD_DECK_NAME, 'shortLink': sl}
ins('trello.trello_cards', TC_COLS, [DC['id'], CARD_DECK_NAME, HG_BOARD['id'], DOING['id'], '', 147456.0, False,
                                     '2025-10-14T16:00:00Z', False, '[]', '[]', 466, None, None,
                                     f"https://PERSON_6092_TRELLO_USERNAME.com/c/{sl}/466-board-deck-oct-14", DECK_CMT_AT,
                                     None, js(dict(badges(1, False), checkItems=4))], DC['id'])
IDS['TR_DECKCARD_CREATE'] = trello_id(DECKCARD_AT, 'deck-card-create')
ins('trello.trello_actions', TA_COLS, [IDS['TR_DECKCARD_CREATE'], 'createCard', DECKCARD_AT, TR_LEO, HG_BOARD['id'], DC['id'],
                                       js({"board": HG_BOARD, "card": DC, "list": DOING})], IDS['TR_DECKCARD_CREATE'])
CL_AT = '2025-09-27T17:12:00Z'
IDS['TR_DECK_CL'] = trello_id(CL_AT, 'deck-checklist')
ins('trello.trello_checklists', ['id', 'name', '"idCard"', '"idBoard"', 'pos'], [IDS['TR_DECK_CL'], 'Sections', DC['id'],
                                                                                HG_BOARD['id'], 16384.0], IDS['TR_DECK_CL'])
for n, item in enumerate(['Fundraising - Fred', 'Product - Robert', 'Engine - Arthur', 'Runway and options - Leonard']):
    iid = trello_id(CL_AT, 'deck-item' + str(n))
    ins('trello.trello_check_items', ['id', 'name', 'state', '"idChecklist"', 'pos', 'due', '"idMember"'],
        [iid, item, 'incomplete', IDS['TR_DECK_CL'], 16384.0 * (n + 1), None, None], iid)
IDS['TR_DECK_CL_ACT'] = trello_id(CL_AT, 'deck-checklist-act')
ins('trello.trello_actions', TA_COLS, [IDS['TR_DECK_CL_ACT'], 'addChecklistToCard', CL_AT, TR_LEO, HG_BOARD['id'], DC['id'],
                                       js({"board": HG_BOARD, "card": DC, "checklist": {"id": IDS['TR_DECK_CL'], "name": "Sections"}})],
    IDS['TR_DECK_CL_ACT'])
IDS['TR_DECK_CMT'] = '68d81f30a6c94e2b7d05e1f4'
assert int(IDS['TR_DECK_CMT'][:8], 16) == int(dt(DECK_CMT_AT).timestamp())
ins('trello.trello_actions', TA_COLS, [IDS['TR_DECK_CMT'], 'commentCard', DECK_CMT_AT, TR_LEO, HG_BOARD['id'], DC['id'],
                                       js({"board": HG_BOARD, "card": DC, "idCard": DC['id'], "list": DOING,
                                           "text": CMT_DECK, "textData": {"emoji": {}}})], IDS['TR_DECK_CMT'])

# ============================================================ Gmail
GM_COLS = ['id', 'thread_id', 'user_email', 'label_ids_json', 'snippet', 'internal_date', 'date', 'size_estimate', 'subject',
           'from_email', 'from_name', 'to_json', 'cc_json', 'bcc_json', 'reply_to_json', 'body_text', 'body_html',
           'headers_json', 'in_reply_to', '"references"', 'mbox_from', 'attachments_meta_json']
INBOX = ["INBOX", "IMPORTANT", "CATEGORY_PERSONAL"]
THREADS = {}


def addr(e, n):
    return f"{n} <{e}>"


def mail(key, at, k, subject, body, frm, to, cc, boxes, parent=None, labels_for=None):
    """frm/to/cc: (email, name); boxes: mailboxes holding a copy (sender copy labelled SENT)."""
    d0 = dt(at)
    ms = int(d0.timestamp() * 1000)
    msgid = '<CA' + base64.b64encode(hashlib.sha256(key.encode()).digest()).decode()[:38].replace('/', '_').replace('+', '-') + '@mail.gmail.com>'
    body_r = body.replace('\r\n', '\n').replace('\n', '\r\n')
    snippet = ' '.join(body.split())[:140]
    hdrs = [{"name": "Message-ID", "value": msgid}, {"name": "Date", "value": email.utils.format_datetime(d0)},
            {"name": "Subject", "value": subject}, {"name": "From", "value": addr(*frm)},
            {"name": "To", "value": ', '.join(addr(*x) for x in to)}]
    if cc:
        hdrs.append({"name": "Cc", "value": ', '.join(addr(*x) for x in cc)})
    pid = None
    if parent:
        pid = THREADS[parent]['msgid']
        hdrs += [{"name": "In-Reply-To", "value": pid}, {"name": "References", "value": pid}]
    THREADS[key] = {'msgid': msgid, 'boxes': {}}
    for box in boxes:
        if parent:
            tref = THREADS[parent]['boxes'][box]
            upd('gmail.gmail_threads', {'snippet': snippet}, 'id', tref)
        else:
            tref = f"{box}/{tid(at, k + (0 if box == FRED else 1 + boxes.index(box)))}"
            ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [tref, box, snippet, None], tref)
        THREADS[key]['boxes'][box] = tref
        labels = ["SENT"] if box == frm[0] else (labels_for or INBOX)
        ins('gmail.gmail_messages', GM_COLS,
            [f"{box}/{msgid}", tref, box, js(labels), snippet, ms, at, len(body_r) + 900, subject, frm[0], frm[1],
             js([addr(*x) for x in to]), js([addr(*x) for x in cc]), '[]', '[]', body_r, None, js(hdrs), pid, pid,
             None, '[]'], f"{box}/{msgid}")
    return THREADS[key]['boxes'].get(FRED)


P = lambda e: (e, NAMES[e])
IDS['G_ROBERT_ASK'] = mail('g_robert_ask', '2025-09-29T18:20:00Z', 59, ROB_MAIL_SUBJ, ROB_MAIL_BODY, P(ROB), [P(FRED)],
                           [P(LEO)], [FRED, ROB, LEO])
IDS['G_HUB'] = mail('g_hub', G_HUB_AT, 11, HUB_SUBJ, HUB_BODY, P(LEO), [P(FRED)], [P(ROB), P(ART)], [FRED, LEO, ROB, ART])
IDS['G_ANTON'] = mail('g_anton', '2025-09-24T16:10:00Z', 23, ANTON_SUBJ, ANTON_BODY, (ANTON, 'Anton Bernstein'),
                      [P(LEO)], [P(FRED)], [FRED, LEO])
IDS['G_DS_ANTON'] = mail('g_ds_anton', '2025-09-26T19:02:00Z', 31, DS_SUBJ, DS_BODY, DOCUSIGN, [P(FRED)], [], [FRED],
                         labels_for=["INBOX", "CATEGORY_UPDATES"])
IDS['G_DS_PAUL'] = mail('g_paul_nudge', '2025-09-29T15:00:00Z', 37, PAUL_SUBJ, PAUL_BODY, P(LEO),
                        [(PAUL, 'Paul Heydon')], [P(FRED)], [FRED, LEO])
IDS['G_HIRO'] = mail('g_hiro', '2025-09-26T09:40:00Z', 41, HIRO_SUBJ, HIRO_BODY, (EDITH, 'Edith Vane'), [P(LEO)],
                     [P(FRED), (HIRO_DIR, 'PERSON_5282_NAME')], [FRED, LEO])
IDS['G_DENTSU'] = mail('g_dentsu_ryo', '2025-09-26T03:10:00Z', 45, DENTSU_SUBJ, DENTSU_RYO_BODY, DENTSU[2], [P(LEO)],
                       [DENTSU[0], DENTSU[1], P(ROB), P(FRED), P(ART)], [FRED, LEO, ROB, ART])
mail('g_dentsu', '2025-09-26T17:20:00Z', 47, 'Re: ' + DENTSU_SUBJ, DENTSU_BODY, P(LEO), DENTSU,
     [P(ROB), P(FRED), P(ART)], [FRED, LEO, ROB, ART], parent='g_dentsu_ryo')
IDS['G_BRIGHT'] = mail('g_bright', '2025-09-25T22:30:00Z', 53, BRIGHT_SUBJ, BRIGHT_BODY, P(LEO), [(ILSE, 'Ilse Marrow')],
                       [P(ROB), P(FRED), P(ART)], [FRED, LEO, ROB, ART])
mail('g_bright_re', '2025-09-26T15:05:00Z', 54, 'Re: ' + BRIGHT_SUBJ, BRIGHT_RE_BODY, (ILSE, 'Ilse Marrow'), [P(LEO)],
     [P(ROB), P(FRED), P(ART)], [FRED, LEO, ROB, ART], parent='g_bright')

# ============================================================ Calendar (one copy per attendee calendar; no invitation mails)
GC_COLS = ['event_id', 'calendar_id', 'summary', 'description', 'location', 'start_ts', 'end_ts', 'start_json', 'end_json',
           'organizer_email', 'creator_email', 'attendees_json', 'status', 'visibility', 'transparency', 'rrule_json',
           'recurring_event_id', 'original_start_json', 'sequence', 'created', 'updated', 'hangout_link', 'ical_uid']


def event(key, summary, desc, start, end, attendees, cals, created, first_id, hangout):
    uid = h('uid' + key, 32) + '@hg4'
    ids = {}
    for cal in cals:
        eid = first_id if cal == FRED else 'evt_' + h(key + cal, 22)
        att = []
        for e in attendees:
            a = {"email": e, "organizer": e == LEO, "responseStatus": "accepted" if e in (LEO, cal) else "needsAction"}
            if e == cal:
                a["self"] = True
            att.append(a)
        ins('gcal.gcal_events', GC_COLS, [eid, cal, summary, desc, None, start, end, js({"dateTime": start}),
                                          js({"dateTime": end}), LEO, LEO, js(att), 'confirmed', None, 'opaque', '[]', None,
                                          None, 0, created, created, hangout, uid], eid)
        ids[cal] = eid
    return ids


IDS['EVT_BRIGHT'] = event('bright', 'Ilse Marrow and Leonard Hayes', None, '2025-09-25T15:30:00Z', '2025-09-25T16:15:00Z',
                          [ART, FRED, LEO, ROB, ILSE], [FRED, LEO, ROB, ART], '2025-09-22T19:12:00Z',
                          'evt_2f86b0d4c9e17a35b64e0d', 'https://meet.google.com/qkd-rwfn-tbe?hs=224')
IDS['EVT_HIRO'] = event('hiro', 'PERSON_5487_NAME and Leonard Hayes', None, '2025-09-23T16:00:00Z', '2025-09-23T16:45:00Z',
                        [ART, FRED, LEO, ROB, 'PERSON_5487_EMAIL', EDITH], [FRED, LEO, ROB, ART], '2025-09-19T18:30:00Z',
                        'evt_7d3e19b04a6c25f8e1b9a0', 'https://meet.google.com/hvt-qmbe-kwr?hs=224')
IDS['EVT_REVIEW'] = event('review', 'Board pre-read review - fundraising', "Fred to bring the pipeline sheet.",
                          '2025-10-06T16:00:00Z', '2025-10-06T16:45:00Z', [FRED, LEO], [FRED, LEO], '2025-09-30T21:00:00Z',
                          'evt_9c41e7a2d05b38f6e1a7c4', 'https://meet.google.com/wpz-hmyc-avr?hs=224')

def invitation(key, at, k, summary, when_hdr, when_body, meet, note, guests, boxes):
    d0 = dt(at)
    ms = int(d0.timestamp() * 1000)
    for box in boxes:
        msgid = f"<calendar-{h(key + box, 8)}-{h(key + box + '1', 4)}-{h(key + box + '2', 4)}-{h(key + box + '3', 4)}-{h(key + box + '4', 12)}@google.com>"
        subject = f"Invitation: {summary} @ {when_hdr} ({box})"
        body = (f"{summary}\r\n{when_body}\r\nPacific Time - Los Angeles\r\n\r\nJoin with Google Meet\r\n{meet}\r\n\r\n"
                + (f"{note}\r\n\r\n" if note else "")
                + "Organizer\r\nLeonard Hayes\r\nleonard.hayes@harmonygames.co\r\n\r\nGuests\r\nLeonard Hayes - organizer\r\n"
                + "\r\n".join(guests) + "\r\n")
        tref = f"{box}/{tid(at, k + (0 if box == FRED else 1 + boxes.index(box)))}"
        snippet = ' '.join(body.split())[:140]
        ins('gmail.gmail_threads', ['id', 'user_email', 'snippet', 'history_id'], [tref, box, snippet, None], tref)
        hdrs = [{"name": "Message-ID", "value": msgid}, {"name": "Date", "value": email.utils.format_datetime(d0)},
                {"name": "Subject", "value": subject}, {"name": "From", "value": f"leonard hayes <{LEO}>"},
                {"name": "To", "value": ', '.join(guests)}]
        ins('gmail.gmail_messages', GM_COLS,
            [f"{box}/{msgid}", tref, box, js(["INBOX", "CATEGORY_PERSONAL"]), snippet, ms, at, len(body) + 3000, subject,
             LEO, 'leonard hayes', js(guests), '[]', '[]', js([f"leonard hayes <{LEO}>"]), body, None, js(hdrs), None, None,
             None, '[]'], f"{box}/{msgid}")
        IDS.setdefault('INVITES', {})[f"{key}:{box}"] = tref


invitation('inv_bright', '2025-09-22T19:12:00Z', 61, 'Ilse Marrow and Leonard Hayes', 'Thu Sep 25, 2025 8:30am - 9:15am (PDT)',
           'Thursday Sep 25, 2025 ⋅ 8:30am – 9:15am', 'https://meet.google.com/qkd-rwfn-tbe?hs=224',
           'Event Name\r\n[SOURCE_ORG_0001]\r\n\r\nPlease share anything that will help prepare for our meeting.: Looking forward to it. Ilse',
           [FRED, ILSE, ROB, ART], [FRED, ROB, ART])
invitation('inv_hiro', '2025-09-19T18:30:00Z', 63, 'PERSON_5487_NAME and Leonard Hayes', 'Tue Sep 23, 2025 9am - 9:45am (PDT)',
           'Tuesday Sep 23, 2025 \u22c5 9am \u2013 9:45am', 'https://meet.google.com/hvt-qmbe-kwr?hs=224',
           'Event Name\r\n[SOURCE_ORG_0001]\r\n\r\nPlease share anything that will help prepare for our meeting.: Looking forward to catching up.',
           [FRED, 'PERSON_5487_EMAIL', EDITH, ROB, ART], [FRED, ROB, ART])
invitation('inv_review', '2025-09-30T21:00:00Z', 67, 'Board pre-read review - fundraising', 'Mon Oct 6, 2025 9am - 9:45am (PDT)',
           'Monday Oct 6, 2025 ⋅ 9am – 9:45am', 'https://meet.google.com/wpz-hmyc-avr?hs=224',
           'Fred to bring the pipeline sheet.', [FRED], [FRED])

# ============================================================ Linear (Arthur's tester ticket; facts in comments, not description)
LIN_AT, C1_AT, C2_AT = '2025-09-30T17:10:00Z', '2025-09-30T17:25:00Z', '2025-09-30T18:40:00Z'
ins('linear.linear_issues', ['id', 'project_id', 'team_id', 'parent_id', 'assignee_id', 'creator_id', 'state_id', 'cycle_id',
                             'identifier', 'number', 'title', 'description', 'priority', 'estimate', 'due_date', 'started_at',
                             'completed_at', 'canceled_at', 'archived_at', 'time_in_status_minutes', 'labels_json',
                             'links_json', 'relations_json', 'state_history_json', 'is_archived', 'created_at', 'updated_at'],
    ['ZOM-567', None, 'team_ZOM', None, LIN_ART, LIN_ART, 'Todo', None, 'ZOM-567', 567, LIN_TITLE, LIN_DESC, 3, None, None,
     None, None, None, None, None, '[]', '[]', '[]', '[]', False, LIN_AT, C2_AT], 'ZOM-567')
LC_COLS = ['id', 'issue_id', 'author_id', 'parent_id', 'body', 'is_edited', 'created_at', 'updated_at', 'sequence']
IDS['LIN_C_TACC'] = 'lc_' + h('ZOM-567-tacc', 24)
IDS['LIN_C_DENTSU'] = 'lc_' + h('ZOM-567-dentsu', 24)
ins('linear.linear_comments', LC_COLS, [IDS['LIN_C_TACC'], 'ZOM-567', LIN_ART, None, LIN_C_TACC, False, C1_AT, C1_AT, 1],
    IDS['LIN_C_TACC'])
ins('linear.linear_comments', LC_COLS, [IDS['LIN_C_DENTSU'], 'ZOM-567', LIN_ART, None, LIN_C_DENTSU, False, C2_AT, C2_AT, 2],
    IDS['LIN_C_DENTSU'])

# ============================================================ Contacts (partner -> firm)
CT_COLS = ['contact_id', 'first_name', 'last_name', 'is_user', 'gender', 'status', 'job', 'email']
for cid, fn, ln, job, em in [('e3a91c07d5b48f26a0c7e314', 'Edith', 'Vane', 'Partner, Hiro Capital', EDITH),
                             ('b72f0d6e19c3a84e5d21f9a0', 'Ilse', 'Marrow', 'Principal, Brightwater Games Fund', ILSE),
                             ('5d0e8b31f7a29c64e1b0d3a8', 'Karthic', 'R', 'T-Accelerate Capital (PXLite fund)', KARTHIC)]:
    ins('contacts.contacts', CT_COLS, [cid, fn, ln, False, 'Unknown', 'Unknown', job, em], cid)

# ============================================================ write
order = ['gdrive', 'gdocs', 'gsheets', 'gslides', 'slack', 'trello', 'gmail', 'gcal', 'linear', 'contacts']
n_ins = sum(1 for s in OUT for x in OUT[s] if x.startswith('INSERT'))
n_upd = sum(1 for s in OUT for x in OUT[s] if x.startswith('UPDATE'))
head = ['-- Are you planning to inject? Yes',
        f'-- HarmonyGames injection - persona Frederick Stone <{FRED}> (Co-founder), Long Horizon.',
        f'-- Services: {", ".join(order)}. Statements: {n_ins} INSERT (one row each), {n_upd} UPDATE.',
        '-- Literal values only; parents before children; re-apply this exact SQL before every agent run.', 'BEGIN;']
body = []
for s in order:
    body.append(f'-- ===================== {s.upper()} =====================')
    body += OUT.get(s, [])
(TI / '01_Universe_Inject.sql').write_text('\n'.join(head + body + ['COMMIT;']) + '\n')
IDS['THREADS'] = {k: v['boxes'] for k, v in THREADS.items()}
IDS['MSGIDS'] = {k: v['msgid'] for k, v in THREADS.items()}
IDS['DECK_CARD'] = DC
json.dump({'ids': IDS, 'rows': ROWS}, open(HERE / 'sql_ids.json', 'w'), indent=1)
print(n_ins, 'INSERT', n_upd, 'UPDATE', {k: len(v) for k, v in ROWS.items()})
