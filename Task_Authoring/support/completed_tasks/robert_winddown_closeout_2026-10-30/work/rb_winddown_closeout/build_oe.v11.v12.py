"""Writes task_inputs/08_Oracle_Events.md (draft mode) from the minted ids, planned text, accounts and truth."""
import datetime as D
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TI = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'task_inputs'))
M = json.load(open(os.path.join(HERE, 'minted_ids.json')))
P = json.load(open(os.path.join(HERE, 'planned_text.json')))
ACC = json.load(open(os.path.join(HERE, 'accounts.json')))
TR = json.load(open(os.path.join(HERE, 'truth.json')))
A = ACC['accounts']
issue = {a['vendor']: a for a in A}
row = {r['issue']: r for r in TR['rows'] if r['issue'].startswith('ENG')}
WHO = {'usr_cc3e90160f490686': 'Arthur', 'usr_63fffeb4fab5233e': 'Leonard', 'usr_Robert': 'Robert', 'usr_bdf01b53c6a92c5e': 'Oliver'}
txt = lambda k: ' '.join(P[k].split())
fmt = lambda x: f"{x:,.2f}"


def ts(t):
    d = D.datetime.fromtimestamp(float(t), D.timezone.utc)
    return d.strftime('%a %b %-d %Y %H:%M UTC')


def day(s):
    if s in ('—', ''):
        return 'a dash'
    return D.date.fromisoformat(s).strftime('%b %-d, %Y')


E = []
e = lambda head, exp: E.append((head, exp))

an = M['S_ANCHOR']
e("Read Leonard's ask in #winddown, the newest message before the clock (Slack: find the channel \"winddown\", read its latest messages)",
  f"Leonard, {ts(an['ts'])} (Fri Feb 13, 9:21 AM PT): \"{txt('S_ANCHOR')}\" It has no replies yet.")
e("Page back through #winddown to Leonard's keep list from Feb 12 and read its thread (Slack: the same #winddown history OE 1 reads; the keep list is a few messages back on that first page; then open its thread replies)",
  f"Leonard, {ts('1770933601.686309')}: \"During shutdown, let's keep Deel, gusto, Intuit. I canceled other subscriptions under mine. ...\" "
  f"One reply, Arthur, {ts(M['S_GUSTO_REPLY']['ts'])}: \"{txt('S_GUSTO_REPLY')}\" So Gusto comes off the keep list: Cancel, by Mar 2.")
e("Read Arthur's card-move message and Leonard's Feb 12 action items in #winddown (same channel history)",
  f"Arthur, {ts('1770937232.664809')}: \"I'll be moving github, [USERNAME_30019], and Metabase to my KubLLC card.\" "
  f"Leonard, {ts('1770933903.645709')}: action items including \"archieve account on google after Feb 15\" and \"I think we keep Metabase and dbt\" "
  "(so the redacted name in Arthur's message is dbt).")
e("Read the Feb 11 Slack plan and Leonard's Feb 12 subscriptions checklist in #winddown, including the table inside the message's attachment (channel history paged back to Feb 11; read attachments, not only text)",
  f"Leonard {ts('1770839825.928989')}: \"For Slack, should I just go back to free version with no history?\" Arthur {ts('1770840054.486779')}: "
  f"\"yeah free version\". Leonard {ts('1770842080.379699')}: \"I guess I'll keep only a few accounts active and turn people into guest accounts\", "
  f"then {ts('1770842405.931359')}: \"let me do that\". Leonard {ts('1770933450.410449')}, \"latest and greatest on subscriptions\": the attached "
  "checklist table marks \"[x] Slack (down to 3 FT members)\" done. These are decisions on record about Slack's plan and users.")
e("Find and read the conventions doc Leonard names (Drive search \"Close-out register conventions\", then read the Google Doc)",
  f"Doc \"Close-out register conventions\" in the Wind Down folder, shared with Leonard, Arthur and Robert, modified Feb 13 2026 16:58 UTC: \"{txt('DOC_CONV')}\"")
e("Find the Linear project Leonard's ask points to and read its description (Linear: list projects, open the one named Shutdown, en dash, accounts)",
  f"The project named \"Shutdown\", an en dash, then \"accounts\" (team ENG, lead Arthur, created Feb 12 2026 23:24 UTC): \"{txt('L_PROJECT')}\"")
e("List the project's issues (Linear issues filtered to the project)",
  "45 issues, all in Todo, created Feb 12 2026 by Arthur: " + "; ".join(f"{a['issue']} {a['vendor']} ({WHO[a['assignee']]})" for a in A)
  + ". There is no ENG-2459.")
cm = lambda a: " / ".join(f"{WHO[c[0]]}: \"{' '.join(c[2].split())}\"" for c in a['comments']) or "no comment"
e("Read the comments on every one of the 45 issues (Linear comments, one issue at a time; the issue list does not include comments)",
  "; ".join(f"{a['issue']} {a['vendor']} — {cm(a)}" for a in A) + ".")
s1 = M['G_SUNSET1']['thread_id']['robert@harmonygames.co']
e("Find Sunset's data checklist in Robert's Gmail and read the whole thread (Gmail search \"data delivery checklist\", then the thread)",
  f"Thread whose subject is \"Harmony Games\", an en dash, then \"data delivery checklist\", from Maya at Sunset to Leonard, Robert and Arthur. First message Feb 12 2026 23:58 UTC: \"{txt('G_SUNSET1')}\" "
  f"Second message, Feb 13 2026 18:20 UTC: \"{txt('G_SUNSET2')}\" So the hold list is Slack (paid plan, every user), Google Workspace (every user, "
  "nothing archived or deleted), Figma, Linear, GitHub, Trello, BigQuery and dbt; Metabase is out. Trap: Sherwood Partners' Feb 12 \"Wind-down "
  "checklist\" (cancel everything except payroll and accounting) is from a firm that was not engaged and does not govern.")
e("Find SVB's card terms on the founders' Trello board (Trello search \"SVB card\", open the card)",
  f"Card \"SVB card payoff + closure\" in To Do, created Feb 13 2026 15:52 UTC by Leonard: \"{txt('T_SVB')}\" Trap: the Done card \"move subscriptions "
  "to SVB credit card\" (2023–24) is the old move onto the card, not these terms.")
e("Find the delivery review call Sunset's mail refers to on Robert's calendar (Calendar search \"data delivery review\")",
  "Event titled \"Sunset\", an en dash, then \"data delivery review\", organizer Leonard, starts Thu Mar 12 2026 17:00 UTC (a future meeting). Hold rows that won't charge the SVB card again before it stay until Mar 12.")
e("Read the HG Costs tab of the January P&L for the lines Arthur's project came from (Drive search \"P&L and forecast\", spreadsheet \"Harmony Games P&L and forecast - Jan 2026\", tab HG Costs)",
  "75 rows. Shared lines: \"Sound (Pond5, Soundly,Elevenlabs)\" (three accounts in one line) and \"UA\" (ad networks). The $6,250 line is Singular and "
  "the hosting line is GitHub (per the project description). Pond5, Soundly and ElevenLabs each count as an account under rule 3.")
e("Query the finance ledger for January and February 2026 lines (Snowflake FINANCE.EXPENSES.FINANCE_LEDGER, date from 2026-01-01)",
  "Still charging: AWS cloud_infra -1,485.00 (Jan 31) and -1,485.00 (Feb 13); meta marketing_ua -2,843.84 (Jan 31) and -956.45 (Feb 13); applovin "
  "marketing_ua -9.80 (Jan 31) and -9.83 (Feb 13). The rest are revenue, salaries, Legal & accounting, the SaaS vendors aggregate and Sunset. meta "
  "and applovin have no issue in the project, so rule 3 adds them; their January lines are their monthly cost (rule 8).")
for k, q, exp in [
    ('G_FIGMA', 'Figma', "Figma Professional (annual) — $1,212.00, renews Sep 11, 2026 → 101.00 a month; it won't charge again before the review call"),
    ('G_LAYER', 'Layer', "Layer Pro (monthly) — $49.00, next payment Mar 3, 2026 → by Mar 2"),
    ('G_POND5', 'Pond5', "the Pond5 Annual Membership was not renewed and ended Sep 8, 2025 → cancelled before Feb 9, left off (rule 2)"),
    ('G_SOUNDLY', 'Soundly', "Soundly Pro (monthly, $10.00) cancelled, access until Mar 3, 2026, no further charge → Closed (Soundly's email)")]:
    e(f"Find the {q} billing email in Robert's Gmail (Gmail search \"{q}\")", f"\"{txt(k)}\" — {exp}.")
e("Find ElevenLabs' receipt in Robert's Gmail (Gmail search \"ElevenLabs\")",
  "Receipt Jul 9 2025, annual $50 plan → prepaid to Jul 9, 2026: 4.17 a month, by Jul 8, 2026. ElevenLabs sits in the Sound line and has no issue, so rule 3 adds it.")
e("Read Singular's billing thread in Robert's Gmail (Gmail search \"Singular invoice\")",
  "Quarterly $6,250 invoices on Sep 1 and Dec 1 2025; the Mar 15 date is only the extension on the past-due balance. Next charge Mar 1 → by Feb 28; 6,250 / 3 = 2,083.33 a month.")
e("Check iPostal and Trello in Robert's Gmail (Gmail searches \"iPostal\" and \"Changes to your Trello subscription\")",
  "iPostal: mailbox cancelled Jan 16 2026 → cancelled before Feb 9, left off. Trello: Nov 21 2025 \"You still have access to Trello Free\" → free plan, 0.00, but Sunset's correction holds it.")
e("Check the Typecast cancellation in #admin_foundersonly (Slack search \"typecast\")",
  f"Leonard, {ts('1751915329.675849')}: \"this typecast thing I'm canceling since we are not adding any voiceovers anymore\" → cancelled before Feb 9; the free tier left is not an account to keep.")
e("Check whether the two \"From old receipts\" issues, Lucidchart and Google Ads, are still live; neither has a comment or a costs-tab line (Gmail searches \"Lucidchart\" and \"Google Ads account was canceled\")",
  "\"Your Lucidchart subscription has been canceled\", Oct 10 2025 16:11 UTC: \"Your Lucidchart subscription has been canceled and will expire on Nov 4, 2025.\" "
  "\"Your Google Ads account was canceled (449-481-1590)\", Oct 17 2025 06:04 UTC: the account \"was canceled on 10/16/25.\" Both were cancelled before Feb 9, "
  "so both stay off the register (rule 2) and ENG-2482 and ENG-2483 go to Canceled.")
e("Look for CodeRabbit's own word on GitHub (GitHub: the bot's comment on pull request 38 \"Final build settings\" in harmonygames-Games/Combo-Fighters)",
  f"CodeRabbit bot comment, Feb 13 2026 09:41 UTC: \"The CodeRabbit subscription for harmonygames-Games was canceled on Feb 12, 2026, so this pull request "
  "was not reviewed.\" A bot notice counts as the vendor's confirmation (rule 5) → CodeRabbit is Closed (say where: this PR notice), by-when a dash, ENG-2474 Done.")
WHERE = {'Helpshift': "Helpshift's reply, per Leonard's ENG-2439 comment", 'Soundly': "Soundly's cancellation email",
         'Zapier': "Zapier's email, per Leonard's ENG-2476 comment", 'Kapwing': "Kapwing's confirmation email, per Arthur's ENG-2478 comment",
         'CodeRabbit': "CodeRabbit bot notice on PR 38"}
st = lambda r: (', ' + r['status'] + (f" ({WHERE[r['account']]})" if r['status'] == 'Closed' else '')) if r['status'] else ''
rws = "; ".join(f"{r['account']}: {r['action']}{st(r)}, {day(r['deadline'])}, {r['owner']}, {fmt(r['cost'])}" for r in TR['rows'])
e("Work out the register from the rules and the records above (calculation)",
  f"28 rows (account: action, status for Cancel rows, by when, owner, monthly cost): {rws}. Left off: the 19 issues cancelled before Feb 9 or "
  "outside rule 2 (OpenAI, Typecast.ai, Unity Asset Store, Veed, Kling, Hailuo.ai, JetBrains, Adobe, Dailybot, Solsten, Calendly, iPostal, Fondo, "
  "Insurance, Office 365, Notarize, UA Assets, Lucidchart, Google Ads) and Intuit, the duplicate of the QuickBooks issue (rule 1).")
e("Add up the two monthly totals (calculation, rule 9)",
  f"Every row: {fmt(TR['total_today'])}. Keep and Hold for Sunset rows only: {fmt(TR['total_after'])}.")
e("Create the register as a new Google Sheet in Robert's Drive (Sheets: create a spreadsheet)",
  "A new spreadsheet exists, owned by Robert.")
e("Write the 28 rows and the two totals into the sheet (Sheets: update values)",
  "The sheet holds the 28 rows of the register (account, what we do, where it stands, by when, owner, monthly cost) and the two totals "
  f"{fmt(TR['total_today'])} and {fmt(TR['total_after'])}.")
e("Share the register with Leonard as an editor (Drive: share file, leonard.hayes@harmonygames.co, role writer)", "Leonard has edit access.")
e("Share the register with Arthur as an editor (Drive: share file, arthur.blake@harmonygames.co, role writer)", "Arthur has edit access.")
L_ = TR['linear']
for a in A:
    k = a['issue']
    if k in L_['done']:
        e(f"Set {k} {a['vendor']} to Done, per the project rule (Linear update of {k}: state Done)", f"{k} moves from Todo to Done.")
    elif k in L_['canceled']:
        e(f"Set {k} {a['vendor']} to Canceled, per the project rule (Linear update of {k}: state Canceled)", f"{k} moves from Todo to Canceled.")
    r = row.get(k)
    if r:
        what = f"{r['action']}{' (' + r['status'] + ')' if r['status'] else ''}, by {day(r['deadline'])}" if r['deadline'] != '—' else \
            f"{r['action']}{' (' + r['status'] + ')' if r['status'] else ''}, nothing left to do by a date"
    elif k == 'ENG-2461':
        what = "it is a duplicate of ENG-2460 QuickBooks, which carries the row"
    else:
        what = f"it is off the register: {a['why_out']}"
    e(f"Comment on {k} {a['vendor']} with what happens and by when (Linear comment on {k})", f"A new comment on {k} saying {what}.")
e("Reply to Leonard in his thread with the two totals and the clashes (Slack message in #winddown under his Feb 13 ask)",
  f"A reply in the thread of Leonard's ask stating: every row {fmt(TR['total_today'])} a month; Keep and Hold rows {fmt(TR['total_after'])} a month; "
  "two clashes with what was already decided: (1) Slack going to the free version / a few accounts with everyone else as guests, against Sunset's "
  "paid plan with every user in place until the review call; (2) archiving Google accounts after Feb 15, against Sunset's \"please don't archive or "
  "delete any\" until the review call.")

out = []
for i, (h, x) in enumerate(E, 1):
    out.append(f"OE {i}  {h}\n        Expected: {x}\n")
text = "\n".join(out)
# plain ASCII for typing: no em/en dashes, no arrows (an arrow chain is an /oe format defect), no division sign
for x, y in [(" \u2192 ", ", so "), ("\u2192", ", so"), ("\u2014", "-"), ("\u2013", "-"), (" \u00f7 ", " / "), ("\u00f7", "/"),
             ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"')]:
    text = text.replace(x, y)
assert all(ord(c) < 128 for c in text), sorted({c for c in text if ord(c) > 127})
dst = os.path.join(TI, '08_Oracle_Events.md')
open(dst, 'w').write(text)
out = [text]
print('wrote', dst, len(E), 'events', len(text), 'chars')
