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
    "gusto bills on the 1st. i pulled every doc and 1099 out of it tonight so we don't need it anymore — "
    "let's cancel before mar 1")
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
    'G_SHERWOOD': ('2026-02-11T18:40:12Z', 'PERSON_0728_EMAIL', 'Wind-down checklist – Harmony Games', 'G_SHERWOOD', FOUNDERS),
    'G_SUNSET1': ('2026-02-12T23:58:21Z', 'PERSON_7731_EMAIL', 'Harmony Games – data delivery checklist', 'G_SUNSET1', FOUNDERS),
    'G_SUNSET2': ('2026-02-13T18:20:44Z', 'PERSON_7731_EMAIL', 'Re: Harmony Games – data delivery checklist', 'G_SUNSET1', FOUNDERS),
    # vendor billing mail reaches Robert through the billing@ group (base precedent: 00016086 Singular, 00016704 Workspace)
    'G_SENTRY': ('2026-01-20T10:15:33Z', 'SVC_7710_EMAIL', 'Sentry receipt – Harmony Games', 'G_SENTRY', [ROB]),
    'G_NOTION': ('2026-02-12T23:01:40Z', 'SVC_7711_EMAIL', 'Your Notion plan has been canceled', 'G_NOTION', [ROB]),
    'G_FIGMA': ('2025-09-11T16:04:52Z', 'SVC_7702_EMAIL', 'Your Figma receipt – Harmony Games', 'G_FIGMA', [ROB]),
    'G_VERCEL': ('2026-01-22T06:40:12Z', 'SVC_7703_EMAIL', 'Vercel invoice for Harmony Games', 'G_VERCEL', [ROB]),
    'G_LINEAR': ('2026-02-01T09:00:27Z', 'SVC_0251_EMAIL', 'Your Linear receipt', 'G_LINEAR', [ROB]),
    'G_1PASS': ('2026-02-08T13:22:05Z', 'SVC_7712_EMAIL', 'Your 1Password Teams receipt', 'G_1PASS', [ROB]),
    'G_LAYER': ('2026-01-25T14:30:05Z', 'SVC_7704_EMAIL', 'Receipt from Layer', 'G_LAYER', [ROB]),
    'G_DEEL': ('2026-02-01T08:02:11Z', 'SVC_1177_EMAIL', 'Deel invoice for February 2026 – Harmony Games, Inc.', 'G_DEEL', [ROB]),
    'G_GCLOUD': ('2026-02-02T11:40:31Z', 'SVC_0982_EMAIL', 'Google Cloud: your January invoice is available', 'G_GCLOUD', [ROB]),
    'G_DBT': ('2026-02-03T07:15:48Z', 'SVC_7705_EMAIL', 'dbt Cloud payment receipt', 'G_DBT', [ROB]),
    'G_ZAPIER': ('2026-02-03T12:08:19Z', 'SVC_7706_EMAIL', 'Your Zapier receipt', 'G_ZAPIER', [ROB]),
    'G_INTUIT': ('2026-02-05T10:22:57Z', 'SVC_7707_EMAIL', 'Your QuickBooks Online payment receipt', 'G_INTUIT', [ROB]),
    'G_CURSOR': ('2026-02-05T17:44:06Z', 'SVC_7708_EMAIL', 'Your receipt from Cursor', 'G_CURSOR', [ROB]),
    'G_DOCUSIGN': ('2026-02-06T15:31:12Z', 'SVC_2600_EMAIL', 'Your Docusign plan renews soon', 'G_DOCUSIGN', [ROB]),
    'G_POND5': ('2026-02-09T13:05:44Z', 'SVC_7709_EMAIL', 'Your Pond5 annual plan renews on March 2', 'G_POND5', [ROB]),
    'G_SLACK': ('2026-02-09T16:20:03Z', 'SVC_0124_EMAIL', 'Your Slack invoice for Harmony Games', 'G_SLACK', [ROB]),
    'G_UNITY': ('2026-02-10T17:41:26Z', 'SVC_5771_EMAIL', 'Unity Technologies SF Invoice#: CINV_00031877 for Harmony Games Inc.', 'G_UNITY', [ROB]),
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
    "including former staff — please don't archive or delete any), Figma, Linear, GitHub, Confluence and Metabase. "
    "Nothing on this list should be closed, downgraded or archived before the delivery review call Leonard booked with "
    "us. Accounts that aren't on the list aren't part of the licensed bundle, so close them whenever suits you.\n\n"
    "For Helpshift, please export the full ticket history to Drive before your subscription ends; Oliver said he'll log "
    "the export on your support handover page.\n\nIf our engineers change anything on this list, we'll reply on this "
    "thread.\n\nBest,\nMaya\nClient onboarding, Sunset")
text['G_SUNSET2'] = (
    "Hi all — one change after our engineers walked through your data map today: Trello is part of the bundle too, and "
    "Metabase isn't (it only reads from BigQuery), so please keep BigQuery and dbt instead. The rest of the list "
    "stands.\n\nMaya")
text['G_SENTRY'] = ("Sentry Team (monthly) — $26.00. Paid with Mastercard •••• 4417. Next billing date: February 20, 2026.")
text['G_NOTION'] = ("Your Notion Plus plan for Harmony Games has been canceled. You'll keep access until March 1, 2026 and "
                    "won't be charged again. Last charge: $20.00 on February 1, 2026.")
text['G_VERCEL'] = ("Vercel Pro (monthly) — $86.00. Charged to Mastercard •••• 4417. Next invoice: February 22, 2026.")
text['G_LINEAR'] = ("Linear Basic (annual), 4 seats — $480.00. Paid with Mastercard ending 4417. Renews on February 1, 2027.")
text['G_1PASS'] = ("1Password Teams Starter Pack (monthly) — $19.95. Charged to Mastercard ending 4417. Next charge: March 8, 2026.")
text['G_FIGMA'] = ("Figma Professional (annual) — $1,212.00. Payment method: MASTERCARD ending in 4417. Your plan renews on "
                   "September 11, 2026.")
text['G_LAYER'] = ("Layer Pro (monthly) — $49.00. Card: Mastercard (4417). Your next payment is on February 25, 2026.")
text['G_DEEL'] = ("Deel platform fee, February 2026 — $300.00. Paid by the Mastercard on file (…4417); the March fee will be "
                  "charged on March 1, 2026.")
text['G_GCLOUD'] = ("Billing account Harmony Games — January 2026 invoice $14.33 (BigQuery). Charged automatically to "
                    "Mastercard-4417. Your next invoice will be issued on March 1, 2026.")
text['G_DBT'] = ("dbt Cloud Team (monthly) — $100.00. Charged to card ending 4417 (Mastercard). Next charge: March 3, 2026.")
text['G_ZAPIER'] = ("Zapier Starter (monthly) — $29.99. Billed to MC •••4417. Your plan renews on March 3, 2026.")
text['G_INTUIT'] = ("QuickBooks Online Plus — $115.00. Payment: Mastercard x4417. Your next payment of $115.00 is due on "
                    "March 5, 2026.")
text['G_CURSOR'] = ("Cursor Pro (monthly) — $40.00. Mastercard ending in 4417. Renews on March 5, 2026.")
text['G_DOCUSIGN'] = ("Your Docusign Standard plan (annual, $300.00) renews on April 8, 2026 and will be charged to the "
                      "Mastercard ending 4417.")
text['G_POND5'] = ("Your Pond5 Annual Membership ($60.00/year) renews on March 2, 2026. We'll charge the card on file (Mastercard "
                   "4417).")
text['G_SLACK'] = ("Slack Pro — Harmony Games — $129.50 for February. Charged to MasterCard ••4417. Your next bill is on "
                   "March 9, 2026.")
text['G_UNITY'] = ("Invoice CINV_00031877 — Unity Pro seats, monthly — $2,172.00. Next invoice date: March 10, 2026. "
                   "Payment: bank transfer, net 30.")
text['G_SOUNDLY'] = ("Your Soundly Pro (monthly, $10.00) subscription has been cancelled. You'll keep access until March 3, "
                     "2026 and won't be charged again.")

# ---------------------------------------------------------------- Linear
PROJECT_ID = '3f0c6a52-' + h('proj-shutdown', 4) + '-4b1e-' + h('proj-shutdown-b', 4) + '-' + h('proj-shutdown-c', 12)
out['L_PROJECT'] = {'id': PROJECT_ID, 'name': 'Shutdown – accounts', 'team': 'team_ENG', 'lead': 'usr_cc3e90160f490686',
                    'at': '2026-02-12T23:24:10Z'}
text['L_PROJECT'] = (
    "One issue per vendor we pay or used to pay, taken from the January P&L costs tab and the #winddown lists. This "
    "replaces my subscriptions sheet from Tuesday. The costs tab leaves a few lines unlabeled: the $6,250 one is Singular and "
    "the hosting one is Vercel; the two $30 game-ops lines are people's tool stipends, so they're not in here. In Leonard's Feb 11 cancel list the one between Zapier and Cursor is Notion, and the third account in my KubLLC message is Sentry. Settle "
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


acct('Unity', ARTHUR, inr=True, action='Cancel', status='Requested', deadline='2026-03-09', owner='Arthur', cost=2172.00,
     cost_src='costs tab Dec-25 (col AF)', evidence=['G_UNITY'],
     comments=[(ARTHUR, '2026-02-13T19:05:12Z', "sent unity the termination this morning, cc leonard", True)])
acct('Helpshift', LEONARD, inr=True, action='Cancel', status='Closed', deadline='—', owner='Leonard', cost=150.00,
     cost_src='costs tab Dec-25 (col AF)', evidence=['CONF_C2'],
     comments=[(LEONARD, '2026-02-13T16:12:40Z', "helpshift wrote back: \"your subscription ends on February 28, 2026. your final invoice for $300 is attached.\"", True)])
acct('Soundly', ROBERT, inr=True, action='Cancel', status='Closed', deadline='—', owner='Robert', cost=10.00,
     cost_src='own charge (shares the Sound line)', evidence=['G_SOUNDLY'],
     comments=[(ARTHUR, '2026-02-12T23:52:03Z', "robert cancelled this on the 11th per #winddown", False)])
acct('OpenAI', ROBERT, inr=False, why_out='never paid by the company', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:41:09Z', "chatgpt plus is on my own card, the company never paid for it", True)])
acct('Typecast.ai', ROBERT, inr=False, why_out='never paid by the company', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:43:30Z', "free tier for the zm trailer voice, we never paid", True)])
acct('Unity Asset Store', ARTHUR, inr=False, why_out='one-off purchases', evidence=[],
     comments=[(ARTHUR, '2026-02-12T23:55:41Z', "asset store is per purchase, nothing recurring", False)])
acct('Veed', ROBERT, inr=False, why_out='cancelled before Feb 9 (last charge Nov 2025)', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:45:02Z', "cancelled in december", False)])
acct('Kling', ROBERT, inr=False, why_out='cancelled before Feb 9 (after the Sep 2025 trial)', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:45:51Z', "dropped after the september trial", False)])
acct('Hailuo.ai', ROBERT, inr=False, why_out='cancelled before Feb 9 (last charge Oct 2025)', evidence=[], comments=[])
acct('JetBrains', ARTHUR, inr=False, why_out='cancelled before Feb 9 (license cancelled end of Dec 2025)', evidence=[],
     comments=[(ARTHUR, '2026-02-12T23:57:10Z', "that was the license for the contractor who left, i cancelled it at the end of december", True)])
acct('Linear', ARTHUR, inr=True, action='Hold for Sunset', status='', deadline=HOLD_END, owner='Arthur', cost=40.00,
     cost_src='own charge, annual $480 / 12 (tab shows 0)', evidence=['G_LINEAR', 'E_REVIEW'],
     comments=[(ARTHUR, '2026-02-12T23:58:30Z', "we went to basic at the renewal, it's annual now", False)])
acct('Figma', ROBERT, inr=True, action='Hold for Sunset', status='', deadline=HOLD_END, owner='Robert', cost=101.00,
     cost_src='own charge, annual $1,212 / 12', evidence=['G_FIGMA', 'E_REVIEW'], comments=[])
acct('Adobe', ROBERT, inr=False, why_out='never paid by the company', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:47:15Z', "we never had a company adobe plan, marcus bennett used his own", True)])
acct('Trello', LEONARD, inr=True, action='Hold for Sunset', status='', deadline=HOLD_END, owner='Leonard', cost=0.00,
     cost_src='costs tab Dec-25 (col AF, free since Nov 21, 2025)', evidence=['G_SUNSET2', 'E_REVIEW'], comments=[])
acct('Dailybot', ARTHUR, inr=False, why_out='cancelled before Feb 9 (2023)', evidence=[], comments=[])
acct('Solsten', LEONARD, inr=False, why_out='one-off purchase (one study, 2024)', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:20:33Z', "one-time study in 2024, contract is done", True)])
acct('Singular', LEONARD, inr=True, action='Cancel', status='Requested', deadline='2026-02-28', owner='Leonard', cost=2083.33,
     cost_src='own charge, quarterly $6,250 / 3', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:24:02Z', "sent the termination on the singular billing thread yesterday", True)])
acct('AWS', ARTHUR, inr=True, action='Cancel', status='Open', deadline='2026-02-28', owner='Arthur', cost=1485.00,
     cost_src='ledger Jan cloud_infra (tab shows 0)', evidence=[],
     comments=[(ARTHUR, '2026-02-13T19:12:45Z', "keeping dd prod up through the month for the store transfer, then terminating everything", True)])
acct('Metabase', ARTHUR, inr=True, action="Move to Arthur's LLC", status='', deadline='—', owner='Arthur', cost=148.00,
     cost_src='costs tab Dec-25 (col AF)', evidence=['G_SUNSET2'],
     comments=[(ARTHUR, '2026-02-13T01:30:22Z', "metabase billing switched to the kubllc card", True)])
acct('dbt', ARTHUR, inr=True, action='Hold for Sunset', status='', deadline=CARD_MOVE, owner='Arthur', cost=100.00,
     cost_src='costs tab Dec-25 (col AF)', evidence=['G_SUNSET2', 'G_DBT'], comments=[])
acct('BigQuery', ARTHUR, inr=True, action='Hold for Sunset', status='', deadline=CARD_MOVE, owner='Arthur', cost=14.33,
     cost_src='costs tab Dec-25 (col AF)', evidence=['G_SUNSET2', 'G_GCLOUD'], comments=[])
acct('Vercel', ARTHUR, inr=True, action='Cancel', status='Open', deadline='2026-02-21', owner='Arthur', cost=86.00,
     cost_src='costs tab Dec-25 (col AF, unlabeled hosting line)', evidence=['G_VERCEL'],
     comments=[(ARTHUR, '2026-02-13T19:15:08Z', "pro plan for the marketing site", False)])
acct('QuickBooks', LEONARD, inr=True, row='Intuit QuickBooks', action='Keep', status='', deadline=CARD_MOVE, owner='Leonard',
     cost=115.00, cost_src='costs tab Dec-25 (col AF)', evidence=['G_INTUIT'], comments=[])
acct('Intuit', LEONARD, inr=False, why_out='duplicate of the QuickBooks issue (newer)', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:26:19Z', "same account as the quickbooks issue", False)])
acct('Carta', LEONARD, inr=True, action='Cancel', status='Open', deadline='2026-08-13', owner='Leonard', cost=321.00,
     cost_src='own charge, annual $3,852 / 12 (tab Aug-25)', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:29:47Z', "the carta terminations this week were the contractor grants, the subscription itself is untouched. annual, $3,852 last august, renews aug 14", True)])
acct('Calendly', ROBERT, inr=False, why_out='cancelled before Feb 9 (auto-renew off since Oct 2025)', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:49:58Z', "turned off auto-renew in october right after it charged", True)])
acct('Google Workspace', LEONARD, inr=True, action='Hold for Sunset', status='', deadline=CARD_MOVE, owner='Leonard',
     cost=316.56, cost_src='costs tab Dec-25 (col AF)', evidence=['G_SUNSET1', 'robert@harmonygames.co/1856033699491658253'],
     comments=[(LEONARD, '2026-02-13T16:31:05Z', "workspace is on the svb card", True)])
acct('Slack', LEONARD, inr=True, action='Hold for Sunset', status='', deadline=CARD_MOVE, owner='Leonard', cost=129.50,
     cost_src='costs tab Dec-25 (col AF)', evidence=['G_SUNSET1', 'G_SLACK'], comments=[])
acct('iPostal', LEONARD, inr=False, why_out='cancelled before Feb 9 (mailbox closed Jan 16, 2026)', evidence=[], comments=[])
acct('Gusto', LEONARD, inr=True, action='Cancel', status='Open', deadline='2026-02-28', owner='Leonard', cost=116.00,
     cost_src='costs tab Dec-25 (col AF)', evidence=['S_GUSTO_REPLY'], comments=[])
acct('Deel', LEONARD, inr=True, action='Keep', status='', deadline=CARD_MOVE, owner='Leonard', cost=300.00,
     cost_src='costs tab Dec-25 (col AF)', evidence=['G_DEEL'], comments=[])
acct('Docusign', LEONARD, inr=True, action='Cancel', status='Open', deadline='2026-04-07', owner='Robert', cost=25.00,
     cost_src='own charge, annual $300 / 12', evidence=['G_DOCUSIGN'],
     comments=[(LEONARD, '2026-02-13T16:33:51Z', "docusign goes to robert, he used it for the art contracts", True)])
acct('Fondo', LEONARD, inr=False, why_out='filing service (taxes and filings)', evidence=[], comments=[])
acct('Insurance', LEONARD, inr=False, why_out='insurance', evidence=[], comments=[])
acct('Office 365', ARTHUR, inr=False, why_out='never paid by the company', evidence=[],
     comments=[(ARTHUR, '2026-02-13T00:02:44Z', "we never used it, the line has always been 0", False)])
acct('Layer', LEONARD, inr=True, action='Cancel', status='Requested', deadline='2026-02-24', owner='Leonard', cost=49.00,
     cost_src='own charge (not on the tab)', evidence=['G_LAYER'],
     comments=[(LEONARD, '2026-02-13T16:36:10Z', "cancelled it in the app on the 11th", True)])
acct('CodeRabbit', ARTHUR, inr=True, action='Cancel', status='Closed', deadline='—', owner='Arthur', cost=48.00,
     cost_src='own charge (not on the tab)', evidence=['GH_CR'],
     comments=[(ARTHUR, '2026-02-13T00:05:31Z', "cancelled. 2 seats at $24", False)])
acct('Cursor', ARTHUR, inr=True, action='Cancel', status='Requested', deadline='2026-03-04', owner='Arthur', cost=40.00,
     cost_src='own charge (not on the tab)', evidence=['G_CURSOR'],
     comments=[(ARTHUR, '2026-02-13T00:06:58Z', "cancelled in the dashboard", False)])
acct('Zapier', LEONARD, inr=True, action='Cancel', status='Open', deadline='2026-03-02', owner='Leonard', cost=29.99,
     cost_src='own charge (not on the tab)', evidence=['G_ZAPIER'],
     comments=[(OLIVER, '2026-02-13T11:20:37Z', "fyi zapier is what pipes helpshift tickets into #issuefeed", False)])
acct('GitHub', ARTHUR, inr=True, action='Hold for Sunset', status='', deadline=HOLD_END, owner='Arthur', cost=16.00,
     cost_src='own charge (not on the tab)', evidence=['G_SUNSET1', 'E_REVIEW'],
     comments=[(ARTHUR, '2026-02-13T01:28:49Z', "github team billing is on the kubllc card now. 4 seats, $16/mo", True)])

acct('Notion', ARTHUR, inr=True, action='Cancel', status='Closed', deadline='—', owner='Arthur', cost=20.00,
     cost_src='own charge (not on the tab)', evidence=['G_NOTION'],
     comments=[(ARTHUR, '2026-02-13T00:09:12Z', "cancelled with cursor", False)])
acct('Sentry', ARTHUR, inr=True, action="Move to Arthur's LLC", status='', deadline='—', owner='Arthur', cost=26.00,
     cost_src='own charge (not on the tab)', evidence=['G_SENTRY'],
     comments=[(ARTHUR, '2026-02-13T01:31:40Z', "sentry is on the kubllc card now", True)])

acct('1Password', ARTHUR, inr=True, action='Cancel', status='Open', deadline='2026-03-07', owner='Arthur', cost=19.95,
     cost_src='own charge (not on the tab)', evidence=['G_1PASS'],
     comments=[(ARTHUR, '2026-02-13T01:34:02Z', "everyone's logins live here, cancel it last", False)])
acct('Notarize', LEONARD, inr=False, why_out='one-off purchases (per notarization)', evidence=[],
     comments=[(LEONARD, '2026-02-13T16:38:44Z', "pay per notarization, no plan", True)])
acct('UA Assets', ROBERT, inr=False, why_out='never paid by the company (line always 0)', evidence=[], comments=[])
acct('Miro', ROBERT, inr=False, why_out='never paid by the company', evidence=[],
     comments=[(ROBERT, '2026-02-13T20:51:20Z', "free board, we never paid", True)])
acct('Lucidchart', ARTHUR, inr=False, why_out='cancelled before Feb 9 (Oct 10, 2025)', evidence=[], comments=[])
acct('Google Ads', LEONARD, inr=False, why_out='cancelled before Feb 9 (account canceled Oct 17, 2025)', evidence=[], comments=[])

assert len(A) == 48, len(A)
# Accounts the project lacks (rule 3 / Sunset's list); each needs a new issue in the project
ADDED = [
    dict(vendor='Pond5', action='Cancel', status='Open', deadline='2026-03-01', owner='Robert', cost=5.00,
         cost_src='own charge, annual $60 / 12 (shares the Sound line)', evidence=['G_POND5']),
    dict(vendor='ElevenLabs', action='Cancel', status='Open', deadline='2026-07-08', owner='Robert', cost=4.17,
         cost_src='own charge, annual $50 / 12 (shares the Sound line)', evidence=['robert@harmonygames.co/1837122624854744558']),
    dict(vendor='Meta Ads', action='Cancel', status='Open', deadline='2026-02-28', owner='Robert', cost=2843.84,
         cost_src='ledger Jan marketing_ua meta (FIN-000689; shares the UA line)', evidence=['FIN-000689', 'FIN-000700']),
    dict(vendor='AppLovin (UA)', action='Cancel', status='Open', deadline='2026-02-28', owner='Robert', cost=9.80,
         cost_src='ledger Jan marketing_ua applovin (FIN-000688)', evidence=['FIN-000688', 'FIN-000699']),
    dict(vendor='Confluence', action='Hold for Sunset', status='', deadline=HOLD_END, owner='Robert', cost=0.00,
         cost_src='free plan, never charged', evidence=['G_SUNSET1', 'E_REVIEW']),
]

for i, a in enumerate(A):
    n = 2438 + i
    a['issue'] = f"ENG-{n}"
    a['created'] = (D.datetime(2026, 2, 12, 23, 24, 10, tzinfo=D.timezone.utc) + D.timedelta(seconds=17 * i + 3)).strftime('%Y-%m-%dT%H:%M:%SZ')
    a['comment_ids'] = []
    for j, c in enumerate(a['comments']):
        a['comment_ids'].append('cmt_' + h(f"rb-{n}-{j}", 20))
out['L_ISSUES'] = [{k: a[k] for k in ('issue', 'vendor', 'assignee', 'created', 'comment_ids')} for a in A]

# ---------------------------------------------------------------- Trello (24 hex: 8 hex unix time + 16 hex)
BOARD = '640643a3fd8f3ca308d9318e'
LIST_TODO, LIST_DONE = '640643a3fd8f3ca308d93195', '640643a3fd8f3ca308d93197'


def trello(seed, t):
    return format(int(ts(t)), '08x') + h('trello-rb-' + seed, 16)


for k, t, lst in [('T_CHASE', '2025-04-07T16:10:44Z', LIST_DONE), ('T_SVB', '2026-02-13T15:52:30Z', LIST_TODO)]:
    out[k] = {'id': trello(k, t), 'at': t, 'board': BOARD, 'list': lst, 'create_action': trello(k + '-create', t)}
text['T_SVB'] = (
    "From the call with SVB today: once the payoff from the data deal posts, they close the Mastercard ending 4417 on Feb 20. "
    "Any charge after that is declined. Anything we keep that will charge the card again while we still need it has to "
    "move to Arthur's KubLLC card or one of our personal cards by end of day Feb 19. Whatever we're cancelling can stay "
    "on the card until it ends.")
text['T_CHASE'] = (
    "Chase closes the operating account on Apr 30. Nothing may pull from it after Apr 25 — check every autopay and "
    "payroll draft before then.")
out['T_SVB']['name'] = 'SVB card payoff + closure'
out['T_CHASE']['name'] = 'Chase account closure'

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
    "Close-out register — how we fill it in\n"
    "1. One row per vendor account. If the same vendor shows up twice (two issues, two names), it's one row under the "
    "name on its invoice, and the newer issue is the duplicate.\n"
    "2. Leave out people, contractors and professional firms (legal, accounting, Sunset), taxes and filing services, "
    "insurance, bank fees, one-off purchases, anything the company itself never paid for, and anything cancelled before "
    "Feb 9. Exception: anything on Sunset's list goes on the register whatever else applies.\n"
    "3. Arthur's project came from the P&L and our lists. Before you call it complete, check the January and February "
    "lines in the finance ledger for anything else that is still charging us and add it — that includes accounts that "
    "share a costs-tab line with another vendor.\n"
    "4. What we do: Cancel, Keep (my keep list, as amended in the thread), Move to Arthur's LLC (his card), or Hold for "
    "Sunset. Sunset's list wins over everything above.\n"
    "5. Where it stands, for Cancel rows only: Closed = the vendor itself has confirmed (their email, an in-app or bot "
    "notice, a final invoice) — say where. Requested = one of us has cancelled or asked but nothing has come back from "
    "the vendor. Open = nobody has done anything yet. Leave it blank on the other rows.\n"
    "6. By when: for Cancel rows that aren't Closed, the day before the next charge (accounts billed on usage — ads, "
    "cloud — bill on the 1st, so Feb 28). For Keep and Hold rows still charging the SVB card while we need them, follow "
    "SVB's card terms. Hold rows already off that card, or that won't charge it again before Sunset's review call, stay "
    "until the review call; Keep rows that won't charge before Feb 20 get a dash. Moved and Closed rows get a dash, "
    "unless an export or a switch-over still has to happen before the access ends — then the day before it ends.\n"
    "7. Owner: the Linear assignee unless the issue hands it to someone else. Anything you add is yours.\n"
    "8. Monthly cost: the Dec-25 column of the costs tab in the January P&L, rounded to cents. The dates in that tab's "
    "header row are off by a year, so go by position: it's column AF, the same column as Dec-25 on the HG P&L tab; "
    "everything to its right is forecast. If the account isn't on "
    "the tab, shares a line with other accounts, or shows 0 or blank there, use its own last full month in the ledger "
    "(January), or its last invoice or receipt brought to a month: annual ÷ 12, quarterly ÷ 3. Free plans and accounts "
    "that have never charged us are 0.\n"
    "9. Two totals at the bottom: the sum of the monthly cost column over every row (what it all costs us today), and the "
    "same sum over the Keep and Hold rows only (what's left after the plan).")
text['SHEET_SUBS'] = (
    "Tab 'Feb': Vendor | Monthly — Unity 1200 | Helpshift 150 | Singular 2000 | Slack 120 | Google Workspace 300 | "
    "Gusto 120 | Deel 250 | QuickBooks 115 | Metabase 140 | dbt 120 | BigQuery 25 | Vercel 90 | Figma 0 | Soundly 15 | "
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
out['CONF_C1'] = {'id': 'page_support_after_helpshift', 'page': 'page_support_after_helpshift', 'space': 'space_OPS',
                  'title': 'Support handover after Helpshift', 'author': 'user_EMPLOYEE_0038', 'at': '2026-02-12T20:05:14Z',
                  'parent': None}
out['CONF_C2'] = {'id': 'comment_support_after_helpshift_c1', 'page': 'page_support_after_helpshift', 'author': 'user_EMPLOYEE_0003',
                  'at': '2026-02-13T15:10:27Z', 'parent': None}
text['CONF_C1'] = ("Helpshift ends on Feb 28. After that, support in Domino Delights and Zombie Match moves to plain email. "
                   "Before then the full ticket history has to be exported to Drive, and the in-game support buttons switched to "
                   "email. Whoever does either, log it in the comments here.")
text['CONF_C2'] = ("Done: full Domino Delights and Zombie Match ticket history exported to the Wind Down folder today "
                   "(helpshift_export_2026-02-13.zip), and both games' support buttons now open email instead of Helpshift.")

# ---------------------------------------------------------------- GitHub (a new Combo-Fighters PR; #37 is hazard L13)
out['GH_PR'] = {'id': 'harmonygames-Games/Combo-Fighters#38', 'author': 'EMPLOYEE_0003_GITHUB_USERNAME',
                'title': 'Final build settings', 'at': '2026-02-13T09:38:51Z', 'state': 'open'}
out['GH_CR'] = {'id': 'harmonygames-Games/Combo-Fighters#38#c_1', 'author': 'PERSON_6026_GITHUB_USERNAME',
                'at': '2026-02-13T09:41:12Z'}
text['GH_CR'] = (
    "<!-- This is an auto-generated comment: skip review by coderabbit.ai -->\n\n> [!IMPORTANT]\n> ## Review skipped\n> \n"
    "> The CodeRabbit Pro subscription for **harmonygames-Games** has been canceled and ends on Feb 26, 2026. Reviews "
    "continue until then; this pull request was not selected for review.")

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
