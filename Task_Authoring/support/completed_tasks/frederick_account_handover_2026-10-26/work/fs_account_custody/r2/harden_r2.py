"""Hardening round 2: hide three custody facts outside the sweep exports.

Edits task_inputs/01_Universe_Inject.sql in place (bytes, so line endings are kept).
"""
import hashlib, json, sys
from datetime import datetime, timezone

SQL = sys.argv[1]
s = open(SQL, 'rb').read().decode('utf-8')

def cut(stmt_start):
    i = s.index(stmt_start)
    j = s.index(");\n", i) + 3
    return i, j

# 1. YouTube: drop the Brand Account tab (Node's ownership now only in Google's notice)
yt = "INSERT INTO gsheets.sheets_sheets (spreadsheet_id, sheet_id, title, \"index\", row_count, column_count, grid_json)\nVALUES ('f_fc27672c5bfea8b760b074', 2, 'Brand Account'"
i, j = cut(yt); s = s[:i] + s[j:]

# 2. Instagram: drop the business-portfolio tab and the pointer to it
ig = "INSERT INTO gsheets.sheets_sheets (spreadsheet_id, sheet_id, title, \"index\", row_count, column_count, grid_json)\nVALUES ('f_215ff8da73e4173f78515c', 1, 'Business portfolio access'"
i, j = cut(ig); s = s[:i] + s[j:]
old = "Fred''s personal gmail, not harmonygames.co. Login only, portfolio access on the next tab"
assert s.count(old) == 1
s = s.replace(old, "Fred''s personal gmail, not harmonygames.co. Login only")

# 3. TikTok: say what the export covers, as the YouTube one does
old = "'[[\"Account\", \"Login email\", \"Role\", \"Status\", \"Notes\"], [\"@harmonygames (64 followers)\""
assert s.count(old) == 1
s = s.replace(old, "'[[\"Scope\", \"Account logins\", \"\", \"\", \"\"], [\"Account\", \"Login email\", \"Role\", \"Status\", \"Notes\"], [\"@harmonygames (64 followers)\"")

FRED = 'frederick.stone@harmonygames.co'

def h(seed, n):
    return hashlib.sha256(seed.encode()).hexdigest()[:n]

def uuidish(seed):
    x = h(seed, 32)
    return f"{x[:8]}-{x[8:12]}-{x[12:16]}-{x[16:20]}-{x[20:32]}"

def q(t):
    return t.replace("'", "''")

def esc(t):
    # E-string body: CRLF as escapes, quotes doubled
    return q(t).replace('\\', '\\\\').replace('\r\n', '\\r\\n')

def mail(key, when, msgid, sender, subject, body):
    dt = datetime.strptime(when, '%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    ms = int(dt.timestamp() * 1000)
    thread = (ms << 20) | (int(h('thread' + key, 8), 16) & 0xFFFFF)
    tid = f"{FRED}/{thread}"
    mid = f"{FRED}/<{msgid}>"
    plain = body.replace('\r\n', ' ').replace('  ', ' ')
    snippet = plain[:140]
    rfc = dt.strftime('%a, %d %b %Y %H:%M:%S +0000')
    headers = [{"name": "Message-ID", "value": f"<{msgid}>"}, {"name": "Date", "value": rfc},
               {"name": "Subject", "value": subject}, {"name": "From", "value": f"{sender[0]} <{sender[1]}>"},
               {"name": "To", "value": FRED}]
    t = ("INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id)\n"
         f"VALUES ('{tid}', '{FRED}', '{q(snippet)}', NULL);\n")
    m = ("INSERT INTO gmail.gmail_messages (id, thread_id, user_email, label_ids_json, snippet, internal_date, date, size_estimate, subject, from_email, from_name, to_json, cc_json, bcc_json, reply_to_json, body_text, body_html, headers_json, in_reply_to, \"references\", mbox_from, attachments_meta_json)\n"
         f"VALUES ('{mid}', '{tid}', '{FRED}', '[\"INBOX\", \"CATEGORY_UPDATES\"]', '{q(snippet)}', {ms}, '{when}', {len(body.encode()) + 900}, '{q(subject)}', '{sender[1]}', '{sender[0]}', '[\"{FRED}\"]', '[]', '[]', '[]', E'{esc(body)}', NULL, '{q(json.dumps(headers))}', NULL, NULL, NULL, '[]');\n")
    return t + m, tid, mid

GOOGLE = ('SVC_0065_NAME', 'SVC_0065_EMAIL')   # Google Accounts sender in Fred's base mail
META = ('SVC_0237_NAME', 'SVC_0237_EMAIL')     # Meta Business Suite portfolio sender in Fred's base mail
TIKTOK = ('SVC_5366_NAME', 'SVC_5366_EMAIL')   # direct TikTok sender in Fred's base mail (SVC_0009 is the ads Google Group)

yt_body = "\r\n".join([
    "Google",
    "",
    "Review who can manage your Brand Account",
    "",
    "Harmony Games (Brand Account for the YouTube channel Harmony Games)",
    "",
    "People who can manage this Brand Account:",
    "Frederick Stone (frederick.stone@harmonygames.co) - Primary owner",
    "[EMAIL_126620] - Owner",
    "",
    "Owners can manage the YouTube channel, add or remove people and delete the Brand Account. People you add in YouTube Studio > Permissions are listed in Studio, not here.",
    "",
    "If someone on this list shouldn't have access, remove them at myaccount.google.com/brandaccounts.",
    "",
    "You received this email to let you know about important changes to your Google Account and services.",
    "(c) 2025 Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA",
])
tt_body = "\r\n".join([
    "TikTok for Business",
    "",
    "Hi Frederick,",
    "",
    "A partner in your Business Center can still manage one of your TikTok accounts. We send this reminder every few months so you can check that the right people and partners have access.",
    "",
    "TikTok account: @harmonygames",
    "Partner: Node Media LLC",
    "Permission: Admin (manage account, post videos, run ads)",
    "Shared on: Oct 8, 2024",
    "",
    "If you no longer work with this partner, remove them in Business Center > Users > Partners.",
    "",
    "The TikTok for Business team",
])
ig_body = "\r\n".join([
    "Meta Business Suite",
    "",
    "Hi Frederick,",
    "",
    "Here's who can manage the Instagram account @harmonygames in your business portfolio.",
    "",
    "Full control (admin)",
    "Leonard Hayes (leonard.hayes@harmonygames.co) - added Jan 22, 2024",
    "Frederick Stone (frederick.stone@harmonygames.co) - added Sep 5, 2024",
    "",
    "Partners with access to this account: none",
    "",
    "The account's own login is managed in the Instagram app and isn't shown here.",
    "",
    "To change access, go to Business settings > Accounts > Instagram accounts.",
    "",
    "Meta Platforms, Inc., Attention: Community Support, 1 Meta Way, Menlo Park, CA 94025",
])

import base64
ytid = base64.urlsafe_b64encode(bytes.fromhex(h('yt-brand', 32))).decode().rstrip('=') + "@notifications.google.com"
blocks = [
    mail('yt-brand', '2025-06-11T15:42:18Z', ytid, GOOGLE, 'Review who can manage Harmony Games', yt_body),
    mail('tt-partner', '2025-07-16T17:12:40Z', uuidish('tt-partner') + '.no-reply@ads-service.tiktok.com', TIKTOK,
         'Partner reminder: Node Media LLC can manage @harmonygames', tt_body),
    mail('ig-portfolio', '2025-08-06T14:05:33Z', uuidish('ig-portfolio') + '@facebookmail.com', META,
         'People with full control of @harmonygames', ig_body),
]
s = s.rstrip('\n') + '\n' + ''.join(b[0] for b in blocks)

n = s.count('\nINSERT INTO ') + (1 if s.startswith('INSERT INTO ') else 0)
old_hdr = [l for l in s.split('\n') if l.startswith('-- Services:')][0]
new_hdr = old_hdr.split('Statements:')[0] + f'Statements: {n} INSERT (one row each), 0 UPDATE.'
s = s.replace(old_hdr, new_hdr)
open(SQL, 'wb').write(s.encode('utf-8'))
print('INSERTs', n)
for b in blocks: print(b[1], '|', b[2])
