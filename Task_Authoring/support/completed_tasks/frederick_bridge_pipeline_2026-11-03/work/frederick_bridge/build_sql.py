#!/usr/bin/env python3
"""Builds task_inputs/01_Universe_Inject.sql for the Frederick Q4 update send-list scenario (injection rev7).
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
HUB_SUBJ = 'Q4 investor update - send list'
HUB_BODY = """Fred,

I'm flying to LA tomorrow morning for the Griffin AGM and the Dentsu meeting, so can you take the send list for the Q4 investor update off my plate? It goes out the week after the Oct 14 board and I'll write the update itself on the plane.

Our existing investors are already on my own list. What I need from you is everyone from the bridge round who should get it, as of tonight, with the groups and details in the Q4 update send list doc so I know which paragraph each one gets. The draft update deck shows what each group gets. Get the new investors right, they'll look for their own check in it.

Please put it in your Q4 investor update folder, the README in that folder says how to name it. Then do what I put on the Existing Investor Update card in Trello. Once it's done reply here with how many firms and angels are in each group. I put Monday's review on your calendar so we can go through it together.

Robert asked about just sending it to everyone on the 2025 list. Let's not, only the people the doc says.

Thanks,
Leonard"""

TEMPLATE_TITLE = 'Q4 investor update - send list'
TEMPLATE_BODY = TEMPLATE_TITLE + """
Leonard, Sep 26. Existing investors are on my own list, this doc is only for the bridge round.

Who to look at
Every name on the 2025 game investor list, angels included. The list has a few names twice, and a repeated name is still one entry. Plus any firm not on the list that we've had a pitch call or meeting with since we kicked off the bridge on Sep 3. A call counts when it's on Fred's calendar, even if he couldn't make it; calls that never went on Fred's calendar don't. Investment talks only, strategic investors included: if we pitched them the bridge or an investment alongside a co-dev deal, they count even when co-dev or publishing was on the table too. Service or work-for-hire deals, banks (our SVB catch-ups), RFPs, publishing-only talks and calls with other engine companies don't.

Groups, as of end of day Tue Sep 30 (Pacific)
Go by what has happened since the Sep 3 kickoff, that day included. On the list, go only by the Latest Status notes (as of 09/11), which are all from this round, and they count as written: a note that they passed or don't do bridges is their no, and a note that we reached out is our outreach. The list's Status and comment columns, answers from earlier rounds and plans to reach out don't count.
New investor: signed a SAFE this round (see my note in #executives on what counts as signed). Put the amount on their row.
In talks: we've had a call or meeting with them this round (on Fred's calendar) and they haven't passed. Angels who've said yes but haven't signed go here too, with the amount they said yes to.
Awaiting reply: we reached out this round, no call yet and no no, even if they've written back.
Keep warm: they passed after we pitched them on a call or meeting this round.
Everyone else stays off: they passed without a call or meeting, or nothing from us since Sep 3.
Passed means they've told us no for this round. A no to our pitch that they sent Griffin or an advisor rather than us counts too. An advisor's own read on whether a firm invests isn't the firm's answer.
"Us" includes anyone who reached out or made an intro on our behalf (IH, Matthew, an advisor). Only outreach about the bridge counts, not RFP or partnership mail.
Accelerator programs like a16z speedrun are separate from the bridge. The interview counts as a call with that firm, but the program's decision and the feedback that comes with it aren't their answer on the bridge; that has to come on our bridge thread with them or in #bridge-pitch.

Build access
For firms in talks: whether they can get the current internal build, TestFlight on iOS and the Play internal test track on Android, so the update can carry the right link. Write iOS only, Android only, iOS and Android, or none. The public store pages don't count. Arthur tracks the tester adds. Leave it blank for angels.

Sheet
One row per firm or angel that gets the update, off-list firms with a call included: firm, group, amount (new investors and angels in talks), build access (firms in talks). The ones who stay off don't go in the sheet.
"""
TEMPLATE_OLD_TITLE = 'Q3 investor update - send list'
TEMPLATE_OLD_BODY = TEMPLATE_OLD_TITLE + """
Leonard, for the July update.

Who gets it
Existing investors, plus anyone we've talked to about investing since the spring update.

Groups
New investor: anyone who's told us yes with an amount.
Interested: said they'd look at it, no amount.
Cold: no reply.

Notes
Keep it to one page. Robert adds the product numbers, Arthur the tech part.
"""
README_TITLE = 'README - Q4 investor update'
README_BODY = README_TITLE + """
Working files for the Q4 update. Name the send list "Q4 update - send list".
Google Sheets or Docs only, no uploads, so I can link them from the draft.
Leonard picks everything up on Monday Oct 6.
"""
DECK_TITLE = 'Harmony Games Q4 2025 update (draft)'
DECK = [
    ('Harmony Games\nQ4 2025 update (draft)', None),
    ('Highlights\nZombie Match 3D alpha numbers (Robert to fill)', None),
    ('Product\nBoss Arena, Season Pass, 300+ levels (Robert to fill)', None),
    ('Engine\nWhat shipped in Q3 (Arthur to fill)', None),
    ('Team\nHeadcount and contractors (Leonard to fill)', None),
    ('Bridge round\nNew investors: welcome, with your check as signed\nIn talks: thanks for the time, here is where we are\n'
     'Awaiting reply: a short recap and the deck link\nKeep warm: no ask, just progress since we spoke', None),
    ('Try the game\nFirms in talks get the internal build links they can use (TestFlight, Play internal test)', None),
    ('Thank you', None),
]
CMT_KEEPWARM = ("Going forward: anyone who passes on the bridge after we've actually pitched them on a call or meeting this round goes on "
                "a Keep warm checklist on this card, one item per firm, so they get the Q4 update with the rest. No's from firms "
                "we only ever emailed don't need it.")
CMT_Q4_SEND = ("For the Q4 send: besides the Keep warm one, give every other group on the send list (New investor, In talks, "
               "Awaiting reply) its own checklist on this card, one item per firm or angel, so Arthur can tick them off as "
               "they go out. Then everyone In talks or Awaiting reply gets a follow-up card in To Do on this board, named "
               "F/up with and the name, so we chase them the week after. If one of them already has a card in To Do, comment on "
               "that card instead of adding another. Anyone we already have a call or meeting with on Fred's calendar after "
               "Sep 30 doesn't need one.")
FU_ANEL_NAME = 'F/up with Anel after the engine deep dive'
S_ANGELS = ("angel update: Paul Heydon is in for $50K and Anton Bernstein for $40K on the SAFE. sending the docs through "
            "docusign next week. not a round but it buys us a bit")
S_ARTHUR = "for the Q4 send list I'd just use who Leonard emailed this month, the rest of that list is noise imo"
S_LEO_SIGNED = ("for the Q4 update send list: someone only counts as a new investor once the DocuSign Completed notice is in. "
                "them telling us they're in doesn't count, and neither does me posting it here")
S_ROB_SCIPLAY = ("Sciplay's out too. D called me this morning, they're passing on this round, too early on metrics for them. "
                 "said keep them posted when we hit beta")
S_DM_ANTON = ("fyi Anton emailed me, he can only do 25 this time, not the 40. voiding his docusign and sending a new SAFE "
              "at 25 tonight")
S_DM_ANTON_SIGNED = "Anton signed the 25 one"
# rev12: Arthur's correction is his own root post in #zombie-match3d (as in rev9, without "testflight" or the ticket id).
# It says "investor tester list" (the README says "Arthur tracks the tester adds") and names everyone on that Play list:
# Karthic (T-Accelerate), the 3 Dentsu folks, Anel's two at NCsoft and Ilse (Brightwater). The rev11 T-Accelerate mail
# replies are removed.
S_ZM_ARTHUR = ("Leonard - found a problem with investor android access: the investor tester list I made in the Play console "
               "never got attached to the internal track, so nobody on it has android yet (Karthic, the 3 Dentsu folks, "
               "Anel's two at NCsoft and Ilse from Brightwater), whatever the Linear log says. iOS is fine for all of them. "
               "I'll attach it with tomorrow's push")
S_ZM_LEO = "ok thx, ping me when it's live so I can tell Karthic, Ryo-san and the others"
# rev11: Paul backs out by mail to Leonard only (not reply-all). rev12: Leonard tells Frederick in their 1:1 DM (not in the
# thread under the angel post, which every run opened). No SAFE, DocuSign, signed, counts or angel wording, so it is
# reached by reading the DM or by a search for Paul
S_LEO_PAUL_OUT = "Paul's out, he wrote me this morning that he can't put money in this year after all"
PAUL_OUT_BODY = ("Leonard,\n\nSorry, I've thought about it more and I have to back out of this one. Something came up on my "
                 "side and I can't put money in this year after all. Really rooting for you and the team.\n\nPaul")
S_LEO_1AM = ("1AM Gaming is the March Gaming Fund row on our list, they renamed from March Capital. they passed on the re-seed, "
             "I forwarded you guys the email")
S_LEO_PLAY = ("correction on Play Ventures: the no I pasted here on the 15th was what they told Griffin, not us. that's why I "
              "said they never answered us. it's still their no for this round, the \"discussing\" Robert heard via Applovin "
              "doesn't change that")
S_LEO_TREO = "Treo VC pinged me again on LinkedIn this morning, I sent them the deck and the blurb there"
S_LEO_MATTEL = ("told Mattel we're passing on the Barbie RFP. since the kickoff that's only been an RFP conversation, we haven't "
                "pitched them the bridge")
S_LEO_INITIAL = ("pinged Initial Capital on LinkedIn about the bridge, they wrote back that they won't lead but might write a "
                 "small check")
ANTON_SUBJ = 'SAFE amount'
ANTON_BODY = ("Leonard,\n\nHad another look at my numbers. I can do $25K this time, not the 40 we talked about. Send the docs "
              "over at 25 and I'll sign.\n\nAnton")
ROB_MAIL_SUBJ = 'Q4 update list'
ROB_MAIL_BODY = ("Fred - for the Q4 update could we just send it to everyone on the 2025 investor list? saves sorting "
                 "who gets what.\n\nRobert")
PAUL_SUBJ = 'SAFE in DocuSign'
PAUL_BODY = ("Hi Paul,\n\nGentle nudge on the SAFE in DocuSign, it's still sitting with you. Would love to have it signed "
             "before the board meets on the 14th.\n\nThanks,\nLeonard")
# rev11: Paul's rev10 "Done, signed it" reply is removed; he backs out the next morning (PAUL_OUT_BODY, Leonard only)
PAUL_OUT_AT = '2025-09-30T14:55:00Z'
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
BRIGHT_BODY = ("Hi Ilse,\n\nThanks for the time this morning and the questions on the bridge round. Happy to set up a longer "
               "session with your partners next week if that's useful.\n\nBest,\nLeonard")
BRIGHT_RE_BODY = ("Thanks Leonard. I'll brief the partners and come back to you next week on a second meeting.\n\n"
                  "Ilse Marrow | Principal, Brightwater Games Fund")
LIN_TITLE = 'Investor testers on ZM internal tracks'
LIN_DESC = ("Log of investor testers on the Zombie Match 3D TestFlight group and the Play internal test track, one comment "
            "per firm with the date each add landed.")
LIN_C_TACC = "T-Accelerate (Karthic): TestFlight and Play internal track both added Sep 22."
LIN_C_DENTSU = ("Dentsu (3 accounts from Ryo-san, came in Thursday night): TestFlight added Sep 26, Play internal track "
                "added Sep 26 (investor tester list).")
# rev12: two more firms in talks on the same lists, so Arthur's post decides four Build access cells
LIN_C_NCSOFT = "NCsoft (2 accounts from Anel's team, after the Sep 19 call): TestFlight and Play internal track both added Sep 22."
LIN_C_BRIGHT = "Brightwater (Ilse Marrow): TestFlight and Play internal track both added Sep 26."

# ============================================================ minted ids and times
T = {
    'TEMPLATE_OLD': ('f_8d2c47a91e05b3f6d7c418', '2025-07-08T18:00:00Z', '2025-07-10T16:12:00Z'),
    'TEMPLATE': ('f_3b9e61c04d7a52e8f1a6c2', '2025-09-26T18:00:00Z', '2025-09-26T18:41:00Z'),
    'FOLDER': ('d_5e8a1c3f9b07d2e64a1b93', '2025-09-26T18:20:00Z', '2025-09-26T18:20:00Z'),
    'README': ('f_c61a0e93b7d24f58a2e917', '2025-09-26T18:30:00Z', '2025-09-26T18:33:00Z'),
    'DECK': ('f_a47d0e2c95b18f63e2c0d5', '2025-09-27T17:00:00Z', '2025-09-28T04:40:00Z'),   # rev7: the draft Q4 update
}
G_HUB_AT = '2025-09-30T21:05:00Z'
S_ANGELS_AT, S_ARTHUR_AT = '2025-09-19T17:40:00Z', '2025-09-29T18:00:00Z'
S_ROB_SCI_AT = '2025-09-30T16:06:00Z'
S_DM_ANTON_AT, S_DM_SIGNED_AT = '2025-09-24T16:25:00Z', '2025-09-26T19:15:00Z'
S_ZM_ARTHUR_AT, S_ZM_LEO_AT = '2025-09-30T23:20:00Z', '2025-09-30T23:48:00Z'
S_PAUL_OUT_AT = '2025-09-30T17:05:00Z'    # rev12: Leonard, Sep 30 10:05 AM PT, in his 1:1 DM with Frederick
S_1AM_AT, S_PLAY_AT, S_MATTEL_AT = '2025-09-08T21:05:00Z', '2025-09-25T16:20:00Z', '2025-09-26T22:50:00Z'
S_SIGNED_AT = '2025-09-26T18:35:00Z'
S_TREO_AT = '2025-09-03T23:31:00Z'
S_INITIAL_AT = '2025-09-09T18:20:00Z'
ROOT_ZM_REL = ('c891232a8b395a701268cff14cffd883', '1759182908.627389')  # rev10: base #zombie-match3d root, Leonard Sep 29 2:55 PM PT: "I just released 0.3.49 on IOS"
ROOT_A16Z = ('99aa913348bb05e6eda8daa06d37fc2a', '1759196326.309469')   # base #executives root, Leonard Sep 29 18:38 PT (speedrun: we didn't get in)
KW_CMT_AT = '2025-09-14T04:20:00Z'
Q4_CMT_AT = '2025-09-29T22:10:00Z'        # rev9: Leonard's second comment on the card (checklists per group, follow-up cards)
FU_ANEL_AT = '2025-09-16T17:30:00Z'       # rev9: Leonard's open To Do card for NCsoft's partner (idShort 456)

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
doc('TEMPLATE_OLD', TEMPLATE_OLD_TITLE, TEMPLATE_OLD_BODY, ROOTS[LEO], LEO, FOUNDER_READ, ['Who gets it', 'Groups', 'Notes'])
doc('TEMPLATE', TEMPLATE_TITLE, TEMPLATE_BODY, ROOTS[LEO], LEO, FOUNDER_READ,
    ['Who to look at', 'Groups, as of end of day Tue Sep 30 (Pacific)', 'Build access', 'Sheet'])
fid, created, modified = T['FOLDER']
drive(fid, 'Q4 2025 investor update', FOLDER_MT, ROOTS[FRED], FRED, [(LEO, 'writer')], created, modified)
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

# rev8: base 2025 investor list, row No. 8 (London Venture Partners), Latest Status: the base cell dates the LVP
# catch-up "09/07" (a Sunday) while the calendar (evt_e59dc0a675d0c407b79acf, Tue Sep 9), #bridge-pitch Sep 8 ("meeting on
# Sep 9th") and Fred's Sep 12 mail agree on Sep 9 (known data issue SC-10; platform /prompt rev7 Cross-Service Coherence 3).
# Only that cell changes; the grid is otherwise the base grid byte for byte and the list keeps its base modified_time.
import ast as _ast
LIST = 'f_48247af79428823c3cac92'
_ws = HERE.parents[3]
_ss = next(x for x in json.load(open(_ws / 'Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/gsheets/data.json'))['sheets_spreadsheets']
           if x['spreadsheet_id'] == LIST)
_sheets = _ast.literal_eval(_ss['sheets']) if isinstance(_ss['sheets'], str) else _ss['sheets']
_sheet = _sheets[0]
_grid = json.loads(json.dumps(_sheet['grid']))
_hdr = _grid[0]
_ls = _hdr.index('Latest Status')
_lvp = [r for r in _grid[1:] if len(r) > 1 and r[1] == 'London Venture Partners']
assert len(_lvp) == 1 and _lvp[0][_ls] == 'Pitch/Catch up on 09/07 - waiting to hear back from them if they want to pursue further'
_lvp[0][_ls] = 'Pitch/Catch up on 09/09 - waiting to hear back from them if they want to pursue further'
OUT.setdefault('gsheets', []).append(
    f"UPDATE gsheets.sheets_sheets SET grid_json = {q(js(_grid))} WHERE spreadsheet_id = {q(LIST)} AND sheet_id = {int(_sheet['sheet_id'])};")
ROWS.setdefault('gsheets.sheets_sheets (UPDATE)', []).append(f"{LIST}#{int(_sheet['sheet_id'])}")

# ============================================================ Slack
SL_COLS = ['id', 'ts', 'channel_id', 'type', 'user_id', 'text', 'thread_parent_id', 'thread_ts_legacy', 'reply_count',
           'reply_users_count', 'latest_reply', 'is_activity_message', 'subtype', 'reactions_json', 'files_json',
           'attachments_json', 'created_at', 'metadata_json']


def sts(at):
    return f"{dt(at).timestamp():.0f}." + {S_ANGELS_AT: '418207', S_ARTHUR_AT: '117903', S_ROB_SCI_AT: '377105',
                                           S_1AM_AT: '384216', S_PLAY_AT: '730591', S_MATTEL_AT: '205874',
                                           S_TREO_AT: '617302', S_INITIAL_AT: '492583', S_DM_ANTON_AT: '281734',
                                           S_DM_SIGNED_AT: '640218', S_ZM_ARTHUR_AT: '518306', S_ZM_LEO_AT: '094417',
                                           S_SIGNED_AT: '336170', S_PAUL_OUT_AT: '863415'}[at]


def slack(ch, user, text, at, parent=None, replies=None):
    """replies: (reply_count, reply_users_count, latest_reply_ts) for a seeded thread root."""
    ts = sts(at)
    mid = h(f"{ch}|{ts}", 32)
    rc, ru, lr = replies or (0, 0, None)
    tl = parent[1] if parent else (ts if replies else None)
    ins('slack.slack_messages', SL_COLS, [mid, ts, ch, 'message', user, text, parent[0] if parent else None,
                                          tl, rc, ru, lr, False, None, '[]', '[]', '[]',
                                          at.replace('Z', '.000000Z'), '{}'], f"{ch}/{ts}")
    return f"{ch}/{ts}", mid


IDS['S_ANGELS'], ANGELS_MID = slack('C07C2866011', SLACK_U[LEO], S_ANGELS, S_ANGELS_AT)   # rev12: no replies again
IDS['S_ARTHUR'], _ = slack('C07C2866011', SLACK_U[ART], S_ARTHUR, S_ARTHUR_AT)
IDS['S_LEO_SIGNED'], _ = slack('C07C2866011', SLACK_U[LEO], S_LEO_SIGNED, S_SIGNED_AT)
IDS['S_LEO_TREO'], _ = slack('C096HFA5Z8W', SLACK_U[LEO], S_LEO_TREO, S_TREO_AT)
IDS['S_LEO_INITIAL'], _ = slack('C096HFA5Z8W', SLACK_U[LEO], S_LEO_INITIAL, S_INITIAL_AT)
IDS['S_LEO_1AM'], _ = slack('C096HFA5Z8W', SLACK_U[LEO], S_LEO_1AM, S_1AM_AT)
IDS['S_LEO_PLAY'], _ = slack('C096HFA5Z8W', SLACK_U[LEO], S_LEO_PLAY, S_PLAY_AT)
IDS['S_LEO_MATTEL'], _ = slack('C096HFA5Z8W', SLACK_U[LEO], S_LEO_MATTEL, S_MATTEL_AT)
IDS['S_ROB_SCI'], _ = slack('C07C2866011', SLACK_U[ROB], S_ROB_SCIPLAY, S_ROB_SCI_AT, parent=ROOT_A16Z)
upd('slack.slack_messages', {'reply_count': 1, 'reply_users_count': 1, 'latest_reply': sts(S_ROB_SCI_AT),
                             'thread_ts_legacy': ROOT_A16Z[1]}, 'id', ROOT_A16Z[0])
IDS['S_DM_ANTON'], _ = slack('D05S58U4SAK', SLACK_U[LEO], S_DM_ANTON, S_DM_ANTON_AT)
IDS['S_DM_ANTON_SIGNED'], _ = slack('D05S58U4SAK', SLACK_U[LEO], S_DM_ANTON_SIGNED, S_DM_SIGNED_AT)
IDS['S_LEO_PAUL_OUT'], IDS['S_LEO_PAUL_OUT_ID'] = slack('D05S58U4SAK', SLACK_U[LEO], S_LEO_PAUL_OUT, S_PAUL_OUT_AT)  # rev12
# rev12: Arthur's root post (one reply from Leonard); the base Sep 29 release post keeps its own counters
IDS['S_ZM_ARTHUR'], ZM_ARTHUR_MID = slack('C0880U9751A', SLACK_U[ART], S_ZM_ARTHUR, S_ZM_ARTHUR_AT,
                                          replies=(1, 1, sts(S_ZM_LEO_AT)))
IDS['S_ZM_LEO'], _ = slack('C0880U9751A', SLACK_U[LEO], S_ZM_LEO, S_ZM_LEO_AT, parent=(ZM_ARTHUR_MID, sts(S_ZM_ARTHUR_AT)))

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
# rev9: Leonard's Sep 29 comment (a checklist per group, follow-up cards in To Do) and his open Sep 16 To Do card for
# NCsoft's partner Anel Ceman (the 2025 list's Partner column), named only by the partner's first name
IDS['TR_Q4_CMT'] = trello_id(Q4_CMT_AT, 'q4-send-comment')
ins('trello.trello_actions', TA_COLS, [IDS['TR_Q4_CMT'], 'commentCard', Q4_CMT_AT, TR_LEO, HG_BOARD['id'], KW['id'],
                                       js({"board": HG_BOARD, "card": KW, "idCard": KW['id'], "list": DOING,
                                           "text": CMT_Q4_SEND, "textData": {"emoji": {}}})], IDS['TR_Q4_CMT'])
upd('trello.trello_cards', {'badges_json': js(badges(2, False)), '"dateLastActivity"': Q4_CMT_AT}, 'id', KW['id'])
TODO = {'id': '640643a3fd8f3ca308d93195', 'name': 'To Do'}
FU_ANEL = {'id': trello_id(FU_ANEL_AT, 'fu-anel'), 'idShort': 456, 'name': FU_ANEL_NAME, 'shortLink': 'Rk7vQe2W'}
IDS['TR_FU_ANEL'] = FU_ANEL['id']
ins('trello.trello_cards', TC_COLS, [FU_ANEL['id'], FU_ANEL_NAME, HG_BOARD['id'], TODO['id'], '', 40960, False, None, False,
                                     '[]', '[]', 456, None, None,
                                     'https://PERSON_6092_TRELLO_USERNAME.com/c/Rk7vQe2W/456-f-up-with-anel-after-the-engine-deep-dive',
                                     FU_ANEL_AT, None, js(badges(0, False))], FU_ANEL['id'])
IDS['TR_FU_ANEL_CREATE'] = trello_id(FU_ANEL_AT, 'fu-anel-create')
ins('trello.trello_actions', TA_COLS, [IDS['TR_FU_ANEL_CREATE'], 'createCard', FU_ANEL_AT, TR_LEO, HG_BOARD['id'], FU_ANEL['id'],
                                       js({"board": HG_BOARD, "card": FU_ANEL, "list": TODO})], IDS['TR_FU_ANEL_CREATE'])
upd('trello.trello_boards', {'"dateLastActivity"': Q4_CMT_AT}, 'id', HG_BOARD['id'])

# ============================================================ Gmail
GM_COLS = ['id', 'thread_id', 'user_email', 'label_ids_json', 'snippet', 'internal_date', 'date', 'size_estimate', 'subject',
           'from_email', 'from_name', 'to_json', 'cc_json', 'bcc_json', 'reply_to_json', 'body_text', 'body_html',
           'headers_json', 'in_reply_to', '"references"', 'mbox_from', 'attachments_meta_json']
INBOX = ["INBOX", "IMPORTANT", "CATEGORY_PERSONAL"]
THREADS = {}


def addr(e, n):
    return f"{n} <{e}>"


def mail(key, at, k, subject, body, frm, to, cc, boxes, parent=None, labels_for=None, snip=True):
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
            if snip:            # rev11: a later reply in the same build sets the thread snippet once
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
# rev6: Anton's mail reaches Leonard only (Frederick learns of it from Leonard's DM, D05S58U4SAK)
IDS['G_ANTON_LEO'] = mail('g_anton', '2025-09-24T16:10:00Z', 23, ANTON_SUBJ, ANTON_BODY, (ANTON, 'Anton Bernstein'),
                          [P(LEO)], [], [LEO])
IDS['G_DS_ANTON'] = mail('g_ds_anton', '2025-09-26T19:02:00Z', 31, DS_SUBJ, DS_BODY, DOCUSIGN, [P(FRED)], [], [FRED],
                         labels_for=["INBOX", "CATEGORY_UPDATES"])
IDS['G_DS_PAUL'] = mail('g_paul_nudge', '2025-09-29T15:00:00Z', 37, PAUL_SUBJ, PAUL_BODY, P(LEO),
                        [(PAUL, 'Paul Heydon')], [P(FRED)], [FRED, LEO])
# rev11: Paul answers Leonard only (Frederick dropped from cc), so it sits in Leonard's copy of the nudge thread
mail('g_paul_out', PAUL_OUT_AT, 38, 'Re: ' + PAUL_SUBJ, PAUL_OUT_BODY, (PAUL, 'Paul Heydon'), [P(LEO)], [], [LEO],
     parent='g_paul_nudge')
IDS['G_PAUL_OUT_LEO'] = f"{LEO}/{THREADS['g_paul_out']['msgid']}"
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
            status = ("accepted" if e == LEO else "needsAction") if key in ('review', 'makers') else \
                     ("accepted" if e in (LEO, cal) else "needsAction")      # rev7: the review shows the same RSVP on both copies
            a = {"email": e, "organizer": e == LEO, "responseStatus": status}
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
IDS['EVT_REVIEW'] = event('review', 'Q4 update send list review', "Fred to bring the send list.",
                          '2025-10-06T21:00:00Z', '2025-10-06T21:45:00Z', [FRED, LEO], [FRED, LEO], '2025-09-30T21:00:00Z',
                          'evt_9c41e7a2d05b38f6e1a7c4', 'https://meet.google.com/wpz-hmyc-avr?hs=224')
# rev9: Makers Fund's partner Michael Cheung (2025 list, Makers row) booked a first call through Leonard's booking page for
# Wed Oct 8 (made Sep 29), titled by person like the base and seeded investor calls; Makers stays Awaiting reply (no call
# yet at Sep 30) and needs no follow-up card.
MICHAEL = 'PERSON_9905_EMAIL'
IDS['EVT_MAKERS'] = event('makers', 'Michael Cheung and Leonard Hayes', None, '2025-10-08T16:00:00Z', '2025-10-08T16:45:00Z',
                          [ART, FRED, LEO, ROB, MICHAEL], [FRED, LEO, ROB, ART], '2025-09-29T17:40:00Z',
                          'evt_6b2e94d0c17a3f58e9d2b1', 'https://meet.google.com/rnv-oxtq-jdw?hs=224')

def invitation(key, at, k, summary, when_hdr, when_body, meet, note, guests, boxes, eastern=None):
    """eastern: (when_hdr, when_body) for Arthur's copy; his calendar is America/New_York like his base invitations."""
    d0 = dt(at)
    ms = int(d0.timestamp() * 1000)
    pac_hdr, pac_body = when_hdr, when_body
    for box in boxes:
        tz_line = "Pacific Time - Los Angeles"
        when_hdr, when_body = pac_hdr, pac_body
        if box == ART and eastern:
            when_hdr, when_body = eastern
            tz_line = "Eastern Time - New York"
        msgid = f"<calendar-{h(key + box, 8)}-{h(key + box + '1', 4)}-{h(key + box + '2', 4)}-{h(key + box + '3', 4)}-{h(key + box + '4', 12)}@google.com>"
        subject = f"Invitation: {summary} @ {when_hdr} ({box})"
        body = (f"{summary}\r\n{when_body}\r\n{tz_line}\r\n\r\nJoin with Google Meet\r\n{meet}\r\n\r\n"
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
           [FRED, ILSE, ROB, ART], [FRED, ROB, ART],
           eastern=('Thu Sep 25, 2025 11:30am - 12:15pm (EDT)', 'Thursday Sep 25, 2025 ⋅ 11:30am – 12:15pm'))
invitation('inv_hiro', '2025-09-19T18:30:00Z', 63, 'PERSON_5487_NAME and Leonard Hayes', 'Tue Sep 23, 2025 9am - 9:45am (PDT)',
           'Tuesday Sep 23, 2025 \u22c5 9am \u2013 9:45am', 'https://meet.google.com/hvt-qmbe-kwr?hs=224',
           'Event Name\r\n[SOURCE_ORG_0001]\r\n\r\nPlease share anything that will help prepare for our meeting.: Looking forward to catching up.',
           [FRED, 'PERSON_5487_EMAIL', EDITH, ROB, ART], [FRED, ROB, ART],
           eastern=('Tue Sep 23, 2025 12pm - 12:45pm (EDT)', 'Tuesday Sep 23, 2025 \u22c5 12pm \u2013 12:45pm'))
invitation('inv_makers', '2025-09-29T17:40:00Z', 69, 'Michael Cheung and Leonard Hayes', 'Wed Oct 8, 2025 9am - 9:45am (PDT)',
           'Wednesday Oct 8, 2025 \u22c5 9am \u2013 9:45am', 'https://meet.google.com/rnv-oxtq-jdw?hs=224',
           'Event Name\r\n[SOURCE_ORG_0001]\r\n\r\nPlease share anything that will help prepare for our meeting.: Looking forward to it.',
           [FRED, MICHAEL, ROB, ART], [FRED, ROB, ART],
           eastern=('Wed Oct 8, 2025 12pm - 12:45pm (EDT)', 'Wednesday Oct 8, 2025 \u22c5 12pm \u2013 12:45pm'))
invitation('inv_review', '2025-09-30T21:00:00Z', 67, 'Q4 update send list review', 'Mon Oct 6, 2025 2pm - 2:45pm (PDT)',
           'Monday Oct 6, 2025 ⋅ 2pm – 2:45pm', 'https://meet.google.com/wpz-hmyc-avr?hs=224',
           'Fred to bring the send list.', [FRED], [FRED])

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
IDS['LIN_C_NCSOFT'] = 'lc_' + h('ZOM-567-ncsoft', 24)      # rev12
IDS['LIN_C_BRIGHT'] = 'lc_' + h('ZOM-567-bright', 24)      # rev12
CN_AT, CB_AT = '2025-09-30T17:45:00Z', '2025-09-30T18:05:00Z'
ins('linear.linear_comments', LC_COLS, [IDS['LIN_C_TACC'], 'ZOM-567', LIN_ART, None, LIN_C_TACC, False, C1_AT, C1_AT, 1],
    IDS['LIN_C_TACC'])
ins('linear.linear_comments', LC_COLS, [IDS['LIN_C_NCSOFT'], 'ZOM-567', LIN_ART, None, LIN_C_NCSOFT, False, CN_AT, CN_AT, 2],
    IDS['LIN_C_NCSOFT'])
ins('linear.linear_comments', LC_COLS, [IDS['LIN_C_BRIGHT'], 'ZOM-567', LIN_ART, None, LIN_C_BRIGHT, False, CB_AT, CB_AT, 3],
    IDS['LIN_C_BRIGHT'])
ins('linear.linear_comments', LC_COLS, [IDS['LIN_C_DENTSU'], 'ZOM-567', LIN_ART, None, LIN_C_DENTSU, False, C2_AT, C2_AT, 4],
    IDS['LIN_C_DENTSU'])

# ============================================================ Contacts (partner -> firm)
CT_COLS = ['contact_id', 'first_name', 'last_name', 'is_user', 'gender', 'status', 'job', 'email']
for cid, fn, ln, job, em in [('e3a91c07d5b48f26a0c7e314', 'Edith', 'Vane', 'Partner, Hiro Capital', EDITH),
                             ('b72f0d6e19c3a84e5d21f9a0', 'Ilse', 'Marrow', 'Principal, Brightwater Games Fund', ILSE),
                             ('5d0e8b31f7a29c64e1b0d3a8', 'Karthic', 'R', 'T-Accelerate Capital (PXLite fund)', KARTHIC),
                             ('a4c2e9f07b31d85e6c0f1b29', 'Ryo', 'Ishikawa', 'Dentsu Ventures (games and AI investments)', 'PERSON_5221_EMAIL')]:
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
json.dump({'ids': IDS, 'rows': ROWS}, open(HERE / 'sql_ids.json', 'w'), indent=1)
print(n_ins, 'INSERT', n_upd, 'UPDATE', {k: len(v) for k, v in ROWS.items()})
