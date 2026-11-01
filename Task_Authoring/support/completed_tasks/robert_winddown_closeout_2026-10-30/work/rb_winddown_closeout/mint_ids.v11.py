"""Deterministic ids, planned wording and per-account ground truth for the Robert wind-down close-out scenario.

Design only; never writes to the base. Writes minted_ids.json (every seeded id with its own timestamp),
planned_text.json (the wording /create-injection seeds verbatim; every delegation quote in the manifest is an exact
substring of one of these) and truth.json (the register the design expects, emitted from the account table below so no
total is hand-typed).
"""
import datetime as D
import hashlib
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def ts(s):
    return D.datetime.fromisoformat(s.replace('Z', '+00:00')).timestamp()


def h(seed, n):
    return hashlib.sha256(seed.encode()).hexdigest()[:n]


out, text = {}, {}

# ---------------------------------------------------------------- Slack (id = sha256(channel|ts)[:32])
WD = 'C0ADGSZKR3R'      # #winddown (Leonard, Robert, Arthur; 206 base msgs Feb 9-12)
PROTO = 'C09UHHN6PFZ'   # #prototype (Robert, Oliver are members)
KEEP_TS = '1770933601.686309'   # base: Leonard's keep list (Feb 12 22:00:01Z)
slack = [
    ('S_GUSTO_REPLY', WD, '2026-02-13T02:14:36.205117Z', KEEP_TS, 'arthur'),
    ('S_OLIVER_CURSOR', PROTO, '2026-02-13T10:02:18.774231Z', None, 'oliver'),
    ('S_ANCHOR', WD, '2026-02-13T17:21:07.448213Z', None, 'leonard'),
]
for k, c, t, thread, who in slack:
    tsv = f"{ts(t):.6f}"
    out[k] = {'channel': c, 'ts': tsv, 'id': h(f"{c}|{tsv}", 32), 'at': t, 'thread_ts': thread, 'author': who,
              'locator': f"{c}/{tsv}"}

text['S_ANCHOR'] = (
    "<@EMPLOYEE_0016_SLACK_ID> can you own the account close-out register before I archive anything on Google? "
    "Arthur put every account into the Linear shutdown project last night. I need one sheet with every account: what "
    "we do with it, where it stands, by when, who does it and what it costs us a month — share it with me and Arthur "
    "as editors. Go by my keep list from last night and the replies under it, Arthur's moves to his LLC card, Sunset's "
    "data checklist, SVB's card terms and the conventions doc I just put in the Wind Down folder. Settle each Linear "
    "issue as you go and leave a line on each, then reply here with the two monthly totals and anything in the plan that clashes with what we "
    "already decided.")
text['S_GUSTO_REPLY'] = (
    "gusto pulls its invoice from the bank on the 3rd. i pulled every doc and 1099 out of it tonight so we don't "
    "need it anymore — let's cancel before mar 3")
text['S_OLIVER_CURSOR'] = (
    "if cursor is getting cut can we keep it till the last combo fighter build? it's doing half my refactors")

# ---------------------------------------------------------------- Gmail (19-digit ids that grow with time)


def gid(t, salt=''):
    return str(int(ts(t) * 1000) << 20 | int(h('g' + t + salt, 5), 16) & 0xFFFFF)


def msgid(key):
    import base64
    return '<CA' + base64.b64encode(hashlib.sha256(key.encode()).digest()).decode()[:38].replace('/', '_').replace('+', '-') + '@mail.gmail.com>'


ROB = 'robert@harmonygames.co'
# key: (sent at, from, subject, thread key (messages sharing a thread), mailboxes holding a copy)
FOUNDERS = [ROB, 'leonard.hayes@harmonygames.co', 'arthur.blake@harmonygames.co']
gmail = {
    'G_SHERWOOD': ('2026-02-12T18:40:12Z', 'PERSON_0728_EMAIL', 'Wind-down checklist – Harmony Games', 'G_SHERWOOD', FOUNDERS),
    'G_SUNSET1': ('2026-02-12T23:58:21Z', 'PERSON_7731_EMAIL', 'Harmony Games – data delivery checklist', 'G_SUNSET1', FOUNDERS),
    'G_SUNSET2': ('2026-02-13T18:20:44Z', 'PERSON_7731_EMAIL', 'Re: Harmony Games – data delivery checklist', 'G_SUNSET1', FOUNDERS),
    # vendor billing mail reaches Robert through the billing@ group (base precedent: 00016086 Singular, 00016704 Workspace)
    'G_FIGMA': ('2025-09-11T16:04:52Z', 'SVC_7702_EMAIL', 'Your Figma receipt – Harmony Games', 'G_FIGMA', [ROB]),
    'G_LAYER': ('2026-02-03T14:30:05Z', 'SVC_7704_EMAIL', 'Receipt from Layer', 'G_LAYER', [ROB]),
    'G_POND5': ('2025-09-08T16:12:40Z', 'SVC_7709_EMAIL', 'Your Pond5 membership has ended', 'G_POND5', [ROB]),
    'G_SOUNDLY': ('2026-02-11T19:47:10Z', 'SVC_3550_EMAIL', 'Your Soundly subscription has been cancelled', 'G_SOUNDLY', [ROB]),
}
for k, (t, frm, subj, thread, boxes) in gmail.items():
    tk = gmail[thread][0]
    out[k] = {'at': t, 'from': frm, 'subject': subj, 'mailboxes': boxes,
              'thread_id': {b: f"{b}/{gid(tk, b)}" for b in boxes},
              'message_id': {b: f"{b}/{msgid(k + b)}" for b in boxes}}
    out[k]['robert_thread'] = out[k]['thread_id'][ROB]
    out[k]['robert_message'] = out[k]['message_id'][ROB]

text['G_SHERWOOD'] = (
    "Leonard,\n\nAs promised on our call, here is the checklist we run on an assignment for the benefit of creditors:\n"
    "1. Cancel every subscription right away except payroll and accounting.\n2. Export whatever records you need "
    "before you cancel.\n3. Close the company cards last, once nothing bills them.\n\nIf you decide to engage us we would "
    "run this for you.\n\nBest,\nSherwood Partners")
text['G_SUNSET1'] = (
    "Hi Leonard, Robert, Arthur,\n\nThanks for signing today. Before we can deliver the licensed data set, these "
    "accounts need to stay active with their full history and every user in place until we confirm delivery: Slack "
    "(stay on the paid plan — the free plan hides history older than 90 days), Google Workspace (every user account, "
    "including former staff — please don't archive or delete any), Figma, Linear, GitHub and Metabase. "
    "Nothing on this list should be closed, downgraded or archived before the delivery review call Leonard booked with "
    "us. Accounts that aren't on the list aren't part of the licensed bundle, so close them whenever suits you.\n\n"
    "For Helpshift, please export the full ticket history to Drive before your subscription ends.\n\nIf our engineers change anything on this list, we'll reply on this "
    "thread.\n\nBest,\nMaya\nClient onboarding, Sunset")
text['G_SUNSET2'] = (
    "Hi all — one change after our engineers walked through your data map today: Trello is part of the bundle too, and "
    "Metabase isn't (it only reads from BigQuery), so please keep BigQuery and dbt instead. The rest of the list "
    "stands.\n\nMaya")
text['G_FIGMA'] = ("Figma Professional (annual) — $1,212.00. Charged to the card on file. Your plan renews on September 11, "
                   "2026.")
text['G_LAYER'] = ("Layer Pro (monthly) — $49.00. Paid with the card on file. Your next payment is on March 3, 2026.")
text['G_POND5'] = ("Your Pond5 Annual Membership was not renewed and ended on September 8, 2025. Your licensed downloads "
                    "stay yours; renew any time to download again.")
text['G_SOUNDLY'] = ("Your Soundly Pro (monthly, $10.00) subscription has been cancelled. You'll keep access until March 3, "
                     "2026 and won't be charged again.")

# ---------------------------------------------------------------- Linear
PROJECT_ID = '3f0c6a52-' + h('proj-shutdown', 4) + '-4b1e-' + h('proj-shutdown-b', 4) + '-' + h('proj-shutdown-c', 12)
out['L_PROJECT'] = {'id': PROJECT_ID, 'name': 'Shutdown – accounts', 'team': 'team_ENG', 'lead': 'usr_cc3e90160f490686',
                    'at': '2026-02-12T23:24:10Z'}
text['L_PROJECT'] = (
    "One issue per vendor we pay or used to pay, taken from the January P&L costs tab and the #winddown lists. This "
    "replaces my subscriptions sheet from Tuesday. A few costs-tab lines are filed under other names: the $6,250 one is Singular and "
    "the hosting one is GitHub; the two $30 game-ops lines I'm handling myself, and we cancelled the unity ads in the UA line after october, so they're not in here. Settle "
    "them as you go: Done once the account counts as closed in the register (access can run out later), Canceled if it doesn't belong on the list, everything else stays "
    "open — and leave a comment on each with what happens and by when.")

ARTHUR, LEONARD, ROBERT, OLIVER = 'usr_cc3e90160f490686', 'usr_63fffeb4fab5233e', 'usr_Robert', 'usr_bdf01b53c6a92c5e'
WHO = {ARTHUR: 'Arthur', LEONARD: 'Leonard', ROBERT: 'Robert', OLIVER: 'Oliver'}

# The 40 project issues, in creation order. Truth columns follow the conventions doc (H3), Sunset's list as corrected
# (H1), SVB's card terms (H2) and the review call date. Deadlines are ISO dates or '—'.
# fields: vendor, assignee, in_register, why_out, action, status, deadline, owner, cost, cost_src, comments[(who, at, text, decisive)]
HOLD_END = '2026-03-12'
CARD_MOVE = '2026-02-19'
A = []


def acct(vendor, assignee, **kw):
    A.append(dict(vendor=vendor, assignee=assignee, **kw))


acct('Unity', ARTHUR, inr=True, action='Cancel', status='Requested', deadline='2026-02-18', owner='Arthur', cost=2348.50,
     cost_src='owner figure: Unity Pro 11 seats, $2,348.50 a month (invoiced on the 19th)', evidence=[],
     comments=[(ARTHUR, '2026-02-13T19:05:12Z', "sent unity the termination this morning, cc leonard. unity pro is 11 seats at $2,348.50 a month with tax, next invoice is the 19th", True)])
acct('Helpshift', LEONARD, inr=True, action='Cancel', status='Closed', deadline='—', owner='Leonard', cost=150.00,
     cost_src="owner figure: $150 a month", evidence=['ZIP'],
     comments=[(OLIVER, '2026-02-13T15:12:18Z', "exported the full helpshift ticket history to the wind down folder today, it's helpshift_export_2026-02-13.zip. both games' support buttons now open email instead of helpshift", True),
               (LEONARD, '2026-02-13T16:12:40Z', "helpshift wrote back that they're discontinuing us at the end of february. it's $150 a month", True)])
acct('Soundly', ROBERT, inr=True, action='Cancel', status='Closed', deadline='—', owner='Robert', cost=10.00,
     cost_src='own charge (shares the Sound line)', evidence=['G_SOUNDLY'],
     comments=[(ARTHUR, '2026-02-12T23:52:03Z', "robert cancelled this on the 11th per #winddown", False)])
acct('OpenAI', ROBERT, inr=False, why_out='one-off purchases (prepaid API credit top-ups)', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:41:09Z', "the openai line is prepaid api credits we topped up now and then, nothing recurring", True)])
acct('Typecast.ai', ROBERT, inr=False, why_out='cancelled before Feb 9 (Leonard cancelled it in Jul 2025; free tier since)', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:43:30Z', "we stopped paying for typecast after the summer, it's on the free tier now", True)])
acct('Unity Asset Store', ARTHUR, inr=False, why_out='one-off purchases', evidence=[],
     comments=[(ARTHUR, '2026-02-12T23:55:41Z', "asset store is per purchase, nothing recurring", False)])
acct('Veed', ROBERT, inr=False, why_out='cancelled before Feb 9 (Robert cancelled it in Dec 2025)', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:45:02Z', "cancelled in december", False)])
acct('Kling', ROBERT, inr=False, why_out='cancelled before Feb 9 (dropped after Sep 2025)', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:45:51Z', "dropped kling after september", False)])
acct('Hailuo.ai', ROBERT, inr=False, why_out='cancelled before Feb 9 (last charge Oct 2025)', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:46:20Z', "cancelled hailuo in october, the last charge was october's", True)])
acct('JetBrains', ARTHUR, inr=False, why_out='cancelled before Feb 9 (license cancelled end of Dec 2025)', evidence=[],
     comments=[(ARTHUR, '2026-02-12T23:57:10Z', "that was the license for the engineer who left in october, i cancelled it at the end of december", True)])
acct('Linear', ARTHUR, inr=True, action='Hold for Sunset', status='', deadline=HOLD_END, owner='Arthur', cost=152.72,
     cost_src='owner figure: annual Standard $1,832.65 paid Aug 21 2025 / 12', evidence=['E_REVIEW'],
     comments=[(ARTHUR, '2026-02-12T23:58:30Z', "linear is on standard, paid yearly. we paid $1,832.65 last august for the year to aug 21, it moves to basic at that renewal. the p&l stops after the 2024 payment", True)])
acct('Figma', ROBERT, inr=True, action='Hold for Sunset', status='', deadline=HOLD_END, owner='Robert', cost=101.00,
     cost_src='own charge, annual $1,212 / 12', evidence=['G_FIGMA', 'E_REVIEW'], comments=[])
acct('Adobe', ROBERT, inr=False, why_out='cancelled before Feb 9 (company plan ended Oct 2024)', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:47:15Z', "the company adobe plan ended in october 2024, marcus bennett uses his own now", True)])
acct('Trello', LEONARD, inr=True, action='Hold for Sunset', status='', deadline=HOLD_END, owner='Leonard', cost=0.00,
     cost_src='free plan since Nov 21, 2025', evidence=['G_SUNSET2', 'E_REVIEW'], comments=[])
acct('Dailybot', ARTHUR, inr=False, why_out='cancelled before Feb 9 (last charge early 2024; workspace deleted Sep 2025)', evidence=[],
     comments=[(ARTHUR, '2026-02-12T23:58:05Z', "we stopped paying for dailybot in early 2024, it sat on the free plan until they deleted the workspace last september", True)])
acct('Solsten', LEONARD, inr=False, why_out='one-off purchase (one study, 2024)', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:20:33Z', "one-time study in 2024, contract is done", True)])
acct('Singular', LEONARD, inr=True, action='Cancel', status='Requested', deadline='2026-02-28', owner='Leonard', cost=2083.33,
     cost_src='own charge, quarterly $6,250 / 3', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:24:02Z', "sent the termination on the singular billing thread yesterday. the next quarterly invoice is mar 1; mar 15 is only their extension on the old one", True)])
acct('AWS', ARTHUR, inr=True, action='Cancel', status='Open', deadline='2026-02-28', owner='Arthur', cost=1485.00,
     cost_src='own January line in the finance ledger (FIN-000687, -1,485)', evidence=[],
     comments=[(ARTHUR, '2026-02-13T19:12:45Z', "keeping dd prod up through the month for the store transfer, then terminating everything. all of aws was $1,485 in january (dd prod is about $1k of it)", True)])
acct('Metabase', ARTHUR, inr=True, action="Move to Arthur's LLC", status='', deadline='—', owner='Arthur', cost=148.00,
     cost_src='owner figure: $148 a month', evidence=['G_SUNSET2'],
     comments=[(ARTHUR, '2026-02-13T01:30:22Z', "metabase billing switched to the kubllc card, it's $148 a month", True)])
acct('dbt', ARTHUR, inr=True, action='Hold for Sunset', status='', deadline=HOLD_END, owner='Arthur', cost=100.00,
     cost_src='owner figure: $100 a month', evidence=['G_SUNSET2'],
     comments=[(ARTHUR, '2026-02-13T01:29:55Z', "dbt is on the kubllc card now, same as github and metabase. $100 a month", True)])
acct('BigQuery', ARTHUR, inr=True, action='Hold for Sunset', status='', deadline=HOLD_END, owner='Arthur', cost=4.97,
     cost_src='owner figure: $4.97 charged Feb 1', evidence=['G_SUNSET2'],
     comments=[(ARTHUR, '2026-02-13T01:33:10Z', "google cloud charges my card on the 1st, not the svb one. it was $4.97 this month", True)])
acct('Vercel', ARTHUR, drop=True, inr=True, action='Cancel', status='Open', deadline='2026-02-21', owner='Arthur', cost=86.00,
     cost_src='costs tab Dec-25 (col AF, unlabeled hosting line)', evidence=[],
     comments=[(ARTHUR, '2026-02-13T19:15:08Z', "pro plan for the marketing site, bills on the 22nd", True)])
acct('QuickBooks', LEONARD, inr=True, row='Intuit QuickBooks', action='Keep', status='', deadline=CARD_MOVE, owner='Leonard',
     cost=115.00, cost_src='owner figure: $115 on the 4th', evidence=['T_SVB'],
     comments=[(LEONARD, '2026-02-13T16:25:31Z', "intuit takes the $115 off the svb card on the 4th", True)])
acct('Intuit', LEONARD, inr=False, why_out='duplicate of the QuickBooks issue (newer)', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:26:19Z', "same account as the quickbooks issue", False)])
acct('Carta', LEONARD, inr=True, action='Cancel', status='Open', deadline='2026-08-14', owner='Leonard', cost=321.00,
     cost_src='owner figure: annual $3,852 / 12', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:29:47Z', "the carta terminations this week were the contractor grants, the subscription itself is untouched. annual, $3,852 last august, renews aug 15", True)])
acct('Calendly', ROBERT, inr=False, why_out='cancelled before Feb 9 (cancelled Oct 2025 after the annual charge)', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:38:44Z', "we cancelled calendly in october right after the annual charge, it just runs out", True)])
acct('Google Workspace', LEONARD, inr=True, action='Hold for Sunset', status='', deadline=CARD_MOVE, owner='Leonard',
     cost=298.13, cost_src="owner figure: this month's invoice $298.13 (= Feb 2 2026 invoice PDF)", evidence=['G_SUNSET1', 'robert@harmonygames.co/1856033699491658253'],
     comments=[(LEONARD, '2026-02-13T16:31:05Z', "workspace is on the svb card, this month's invoice was $298.13", True)])
acct('Slack', LEONARD, inr=True, action='Hold for Sunset', status='', deadline=CARD_MOVE, owner='Leonard', cost=87.22,
     cost_src='owner figure: renewed Feb 3 for $87.22', evidence=['G_SUNSET1'],
     comments=[(LEONARD, '2026-02-13T16:31:48Z', "slack renews on the 3rd, it's on the svb card. it was $87.22 this month", True)])
acct('iPostal', LEONARD, inr=False, why_out='cancelled before Feb 9 (mailbox closed Jan 16, 2026)', evidence=[], comments=[])
acct('Gusto', LEONARD, inr=True, action='Cancel', status='Open', deadline='2026-03-02', owner='Leonard', cost=116.00,
     cost_src="owner figure: January's invoice $116", evidence=['S_GUSTO_REPLY'],
     comments=[(LEONARD, '2026-02-13T16:32:02Z', "gusto's january invoice was $116, they take it on the 3rd", True)])
acct('Deel', LEONARD, inr=True, action='Keep', status='', deadline='—', owner='Leonard', cost=300.00,
     cost_src='owner figure: $300 a month', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:32:20Z', "deel gets paid by transfer from the bank account, nothing on a card. it's $300 a month", True)])
acct('Docusign', LEONARD, inr=True, action='Cancel', status='Open', deadline='2026-04-19', owner='Robert', cost=25.00,
     cost_src='own charge, annual $300 / 12', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:33:51Z', "docusign goes to robert from here. annual, $300, renews apr 20 (the p&l missed last april's charge)", True)])
acct('Fondo', LEONARD, inr=False, why_out='filing service (taxes and filings)', evidence=[], comments=[])
acct('Insurance', LEONARD, inr=False, why_out='insurance', evidence=[], comments=[])
acct('Office 365', ARTHUR, inr=False, why_out='cancelled before Feb 9 (dropped end of 2024)', evidence=[],
     comments=[(ARTHUR, '2026-02-13T00:02:44Z', "we dropped office 365 at the end of 2024, the line's been 0 since", False)])
acct('Layer', LEONARD, inr=True, action='Cancel', status='Requested', deadline='2026-03-02', owner='Leonard', cost=49.00,
     cost_src='own charge (not on the tab)', evidence=['G_LAYER'],
     comments=[(LEONARD, '2026-02-13T16:36:10Z', "cancelled it in the app on the 11th", True)])
acct('CodeRabbit', ARTHUR, inr=True, action='Cancel', status='Closed', deadline='—', owner='Arthur', cost=45.00,
     cost_src='own charge (not on the tab)', evidence=['GH_CR'],
     comments=[(ARTHUR, '2026-02-13T00:05:31Z', "cancelled. lite plan, 3 seats at $15", False)])
acct('Cursor', ARTHUR, inr=True, action='Cancel', status='Requested', deadline='2026-03-04', owner='Arthur', cost=40.00,
     cost_src='own charge (not on the tab)', evidence=[],
     comments=[(ARTHUR, '2026-02-13T00:06:58Z', "cancelled in the dashboard. $40/mo, renews on the 5th", True)])
acct('Zapier', LEONARD, inr=True, action='Cancel', status='Closed', deadline='—', owner='Leonard', cost=73.50,
     cost_src='own charge (not on the tab)', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:37:02Z', "cancelled zapier yesterday, their email says the plan runs until feb 27. it was $73.50 a month", True)])
acct('GitHub', ARTHUR, inr=True, action='Hold for Sunset', status='', deadline=HOLD_END, owner='Arthur', cost=90.00,
     cost_src='owner figure: $90 this month all in', evidence=['G_SUNSET1', 'E_REVIEW'],
     comments=[(ARTHUR, '2026-02-13T01:28:49Z', "github is on the kubllc card now. it was $90 this month all in", True)])

acct('Kapwing', ARTHUR, inr=True, action='Cancel', status='Closed', deadline='—', owner='Arthur', cost=24.00,
     cost_src='own charge (not on the tab)', evidence=[],
     comments=[(ARTHUR, '2026-02-13T00:09:12Z', "cancelled with cursor. kapwing emailed to confirm, pro runs out later this month. it was $24 a month", True)])

acct('1Password', ARTHUR, inr=True, action='Cancel', status='Open', deadline='2026-03-07', owner='Arthur', cost=19.95,
     cost_src='own charge (not on the tab)', evidence=[],
     comments=[(ARTHUR, '2026-02-13T01:34:02Z', "everyone's logins live here, cancel it last. $19.95 a month, renews on the 8th", True)])
acct('Notarize', LEONARD, inr=False, why_out='one-off purchases (per notarization)', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:38:44Z', "pay per notarization, no plan", True)])
acct('UA Assets', ROBERT, inr=False, why_out='one-off purchases (campaign creative buys, last Apr 2025)', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:50:40Z', "there's no ua assets account, that line was one-off creative buys for campaigns, the last one was last april", True)])
acct('Lucidchart', ARTHUR, inr=False, why_out='cancelled before Feb 9 (subscription canceled Oct 10, 2025, expired Nov 4, 2025)', evidence=[], comments=[])
acct('Google Ads', LEONARD, inr=False, why_out='cancelled before Feb 9 (account canceled Oct 16, 2025)', evidence=[], comments=[])

assert len(A) == 46, len(A)
# Accounts the project lacks (rule 3 / Sunset's list); each needs a new issue in the project
ADDED = [
    dict(vendor='ElevenLabs', action='Cancel', status='Open', deadline='2026-07-08', owner='Robert', cost=4.17,
         cost_src='own charge, annual $50 / 12 (shares the Sound line)', evidence=['robert@harmonygames.co/1837122624854744558']),
    dict(vendor='Meta Ads', action='Cancel', status='Open', deadline='2026-02-28', owner='Robert', cost=2843.84,
         cost_src='ledger Jan marketing_ua meta (FIN-000689; shares the UA line)', evidence=['FIN-000689', 'FIN-000700']),
    dict(vendor='AppLovin (UA)', action='Cancel', status='Open', deadline='2026-02-28', owner='Robert', cost=9.80,
         cost_src='ledger Jan marketing_ua applovin (FIN-000688)', evidence=['FIN-000688', 'FIN-000699']),
]

for i, a in enumerate(A):
    n = 2438 + i
    a['issue'] = f"ENG-{n}"
    a['created'] = (D.datetime(2026, 2, 12, 23, 24, 10, tzinfo=D.timezone.utc) + D.timedelta(seconds=17 * i + 3)).strftime('%Y-%m-%dT%H:%M:%SZ')
    a['comment_ids'] = []
    for j, c in enumerate(a['comments']):
        a['comment_ids'].append('cmt_' + h(f"rb-{n}-{j}", 20))
A[:] = [a for a in A if not a.get('drop')]   # ENG-2459 (Vercel) removed at /prompt r3; numbering kept
out['L_ISSUES'] = [{k: a[k] for k in ('issue', 'vendor', 'assignee', 'created', 'comment_ids')} for a in A]

# ---------------------------------------------------------------- Trello (24 hex: 8 hex unix time + 16 hex)
BOARD = '640643a3fd8f3ca308d9318e'
LIST_TODO, LIST_DONE = '640643a3fd8f3ca308d93195', '640643a3fd8f3ca308d93197'


def trello(seed, t):
    return format(int(ts(t)), '08x') + h('trello-rb-' + seed, 16)


for k, t, lst in [('T_SVB', '2026-02-13T15:52:30Z', LIST_TODO)]:
    out[k] = {'id': trello(k, t), 'at': t, 'board': BOARD, 'list': lst, 'create_action': trello(k + '-create', t)}
text['T_SVB'] = (
    "From the call with SVB today: once the payoff from the data deal posts, they close the card on Feb 20. "
    "Any charge after that is declined. Anything we keep that will charge the card again while we still need it has to "
    "move to Arthur's KubLLC card or one of our personal cards by end of day Feb 19. Whatever we're cancelling can stay "
    "on the card until it ends.")
out['T_SVB']['name'] = 'SVB card payoff + closure'

# ---------------------------------------------------------------- Drive family (f_ + 22 hex)
WIND_DOWN = 'd_e5caf6a8c630421942ee59'
out['DOC_CONV'] = {'id': 'f_' + h('drive-rb-conventions', 22), 'created': '2026-02-13T16:38:02Z', 'at': '2026-02-13T16:58:40Z',
                   'name': 'Close-out register conventions', 'parent': WIND_DOWN,
                   'owner': 'Resource: 7240535625619857401',
                   'shared_with': ['leonard.hayes@harmonygames.co', 'arthur.blake@harmonygames.co', ROB]}
out['SHEET_SUBS'] = {'id': 'f_' + h('drive-rb-subs-sheet', 22), 'created': '2026-02-10T18:05:12Z', 'at': '2026-02-10T18:31:55Z',
                     'name': 'Subscriptions', 'owner': 'arthur.blake@harmonygames.co',
                     'shared_with': ['leonard.hayes@harmonygames.co', ROB]}
text['DOC_CONV'] = (
    "Close-out register conventions\n"
    "1. One row per vendor account. If the same vendor shows up twice (two issues, two names), it's one row under the "
    "name on its invoice, and the newer issue is the duplicate.\n"
    "2. Leave out people, contractors and professional firms (legal, accounting, Sunset), taxes and filing services, "
    "insurance, bank fees, one-off purchases, anything the company itself never paid for, and anything cancelled before "
    "Feb 9. Exception: anything on Sunset's list goes on the register whatever else applies.\n"
    "3. Arthur's project came from the P&L and our lists, one issue per costs-tab line. Before you call it complete, add "
    "two kinds of account it misses: anything else still charging us in the January and February lines of the finance "
    "ledger, and every other account hiding inside a costs-tab line that covers several vendors — each one gets its own "
    "row, whether or not it has a ledger line of its own.\n"
    "4. What we do: Cancel, Keep (my keep list, as amended in the thread), Move to Arthur's LLC (his card), or Hold for "
    "Sunset. Sunset's list wins over everything above.\n"
    "5. Where it stands, for Cancel rows only: Closed = the vendor itself has confirmed (their email, an in-app or bot "
    "notice, a final invoice) — say where. Requested = one of us has cancelled or asked but nothing has come back from "
    "the vendor. Open = nobody has done anything yet. Leave it blank on the other rows.\n"
    "6. By when: for Cancel rows that aren't Closed, the day before the next charge (for accounts billed on usage — "
    "ads, cloud — use Feb 28). For Keep and Hold rows still charging the SVB card while we need them, follow "
    "SVB's card terms. Hold rows already off that card, or that won't charge it again before Sunset's review call, stay "
    "until the review call; Keep rows that aren't on the SVB card get a dash. Moved and Closed rows get a dash, "
    "unless an export or a switch-over still has to happen before the access ends — then the day before it ends.\n"
    "7. Owner: the Linear assignee unless the issue hands it to someone else. Anything you add is yours.\n"
    "8. Monthly cost, rounded to cents. A cloud or ad-spend account with its own line in the finance ledger uses its "
    "January line there. Everything else: the monthly figure its owner gives in its Linear issue, or else its own "
    "last invoice or receipt brought to a month (annual ÷ 12, quarterly ÷ 3). Free plans and accounts that have never "
    "charged us are 0.\n"
    "9. Two totals at the bottom: the sum of the monthly cost column over every row (what it all costs us today), and the "
    "same sum over the Keep and Hold rows only (what's left after the plan).\n"
    "10. A clash is a decision one of us already posted in #winddown that Sunset's list or SVB's card terms would undo. "
    "Moving who pays for an account isn't one (it closes nothing), and requests or suggestions aren't decisions.")
text['SHEET_SUBS'] = (
    "Tab 'Feb': Vendor | Monthly — Unity 1200 | Helpshift 150 | Singular 2000 | Slack 120 | Google Workspace 300 | "
    "Gusto 120 | Deel 250 | QuickBooks 115 | Metabase 140 | dbt 120 | BigQuery 25 | Figma 0 | Soundly 15 | "
    "Cursor 20 | CodeRabbit 30 | Layer 39 | Zapier 20")

# ---------------------------------------------------------------- GCal (one ical_uid, a copy per attendee calendar)
REVIEW_CALS = ['leonard.hayes@harmonygames.co', ROB, 'arthur.blake@harmonygames.co']
out['E_REVIEW'] = {'ical_uid': h('ical_sunset_review', 32) + '@hg4', 'summary': 'Sunset – data delivery review',
                   'start': '2026-03-12T17:00:00Z', 'end': '2026-03-12T17:45:00Z', 'created': '2026-02-12T22:40:15Z',
                   'at': '2026-02-12T22:40:15Z', 'organizer': 'leonard.hayes@harmonygames.co',
                   'attendees': REVIEW_CALS + ['PERSON_7731_EMAIL'],
                   'copies': {cal: 'evt_' + h('sunset-review' + cal, 22) for cal in REVIEW_CALS}}
out['E_REVIEW']['robert_copy'] = out['E_REVIEW']['copies'][ROB]

# ---------------------------------------------------------------- Confluence
out['CONF_UA'] = {'id': 'page_ua_vendor_closeout', 'space': 'space_OPS', 'title': 'Vendor close-out conventions (Growth/UA)',
                  'author': 'user_EMPLOYEE_0008', 'at': '2025-03-18T15:20:00Z'}
text['CONF_UA'] = (
    "How Growth/UA closes out an ad network or attribution vendor in the UA vendor tracker: 1. Pause every campaign; the "
    "vendor counts as closed once spend reads $0 for 7 days. 2. Cost in the tracker = trailing 30-day spend. 3. Owner = "
    "the UA manager on the account. These conventions apply to the Growth/UA team's tracker only.")

# ---------------------------------------------------------------- GitHub (a new Combo-Fighters PR; #37 is hazard L13)
out['GH_PR'] = {'id': 'harmonygames-Games/Combo-Fighters#38', 'author': 'EMPLOYEE_0003_GITHUB_USERNAME',
                'title': 'Final build settings', 'at': '2026-02-13T09:38:51Z', 'state': 'open'}
out['GH_CR'] = {'id': 'harmonygames-Games/Combo-Fighters#38#c_1', 'author': 'PERSON_6026_GITHUB_USERNAME',
                'at': '2026-02-13T09:41:12Z'}
text['GH_CR'] = (
    "<!-- This is an auto-generated comment: skip review by coderabbit.ai -->\n\n> [!IMPORTANT]\n> ## Review skipped\n> \n"
    "> The CodeRabbit subscription for **harmonygames-Games** was canceled on Feb 12, 2026, so this pull request "
    "was not reviewed. Reactivate the subscription to resume reviews.")

# ---------------------------------------------------------------- truth (emitted, never hand-typed)
rows = []
for a in A:
    if a['inr']:
        rows.append(dict(account=a.get('row', a['vendor']), issue=a['issue'], action=a['action'], status=a['status'],
                         deadline=a['deadline'], owner=a['owner'], cost=a['cost'], cost_src=a['cost_src'],
                         evidence=a['evidence']))
for a in ADDED:
    rows.append(dict(account=a['vendor'], issue='(new issue)', action=a['action'], status=a['status'],
                     deadline=a['deadline'], owner=a['owner'], cost=a['cost'], cost_src=a['cost_src'],
                     evidence=a['evidence']))
t1 = round(sum(r['cost'] for r in rows), 2)
t2 = round(sum(r['cost'] for r in rows if r['action'] in ('Keep', 'Hold for Sunset')), 2)
outs = [dict(issue=a['issue'], vendor=a['vendor'], why=a['why_out']) for a in A if not a['inr']]
from collections import Counter
truth = dict(rows=rows, excluded=outs, total_today=t1, total_after=t2,
             counts=dict(rows=len(rows), excluded=len(outs), by_action=Counter(r['action'] for r in rows),
                         by_status=Counter(r['status'] for r in rows if r['action'] == 'Cancel')),
             linear=dict(done=[a['issue'] for a in A if a['inr'] and a['status'] == 'Closed'],
                         canceled=[a['issue'] for a in A if not a['inr']],
                         open=[a['issue'] for a in A if a['inr'] and a['status'] != 'Closed'],
                         new_issues=[a['vendor'] for a in ADDED]))
json.dump(out, open(os.path.join(HERE, 'minted_ids.json'), 'w'), indent=1, ensure_ascii=False)
json.dump(text, open(os.path.join(HERE, 'planned_text.json'), 'w'), indent=1, ensure_ascii=False)
json.dump(dict(accounts=A, added=ADDED), open(os.path.join(HERE, 'accounts.json'), 'w'), indent=1, ensure_ascii=False)
json.dump(truth, open(os.path.join(HERE, 'truth.json'), 'w'), indent=1, ensure_ascii=False, default=dict)
print(json.dumps(truth['counts'], default=dict), 'total_today', t1, 'total_after', t2)
