#!/usr/bin/env python3
"""Draft 08_Oracle_Events.md from the seeded rows, the base records and the re-derived model.

Every double-quoted span on an Expected line is checked as a substring of the record it is taken from, so a typo
stops the build. One write per event; no final-response or non-action events; no em or en dash anywhere in the file."""
import json
import os
import re
import sys

from model import (ADS, ARCHIVE, BY, CM, D10, D15, GRID, HERE, ISS, JULIA, MARCUS, OFF_SHEET, SHEET, TI, call,
                   campaigns, due, kind, maker, name, rows)

BASE = json.load(open(os.path.join(HERE, 'base_quotes.json')))
EVENTS = []          # (key, heading, expected)
LABEL = {}           # key -> OE number
SOURCES = {}         # key -> list of (source label, text) for the quote check


def clean(s):
    return (s or '').replace('\\n', '\n').replace('\r', '')


def norm(s):
    return re.sub(r'\s+', ' ', s).replace('’', "'").strip()


def ev(key, heading, expected, *sources):
    EVENTS.append((key, heading, expected))
    LABEL[key] = len(EVENTS)
    SOURCES[key] = list(sources)


def oe(*keys):
    """'OE 5' or 'OE 5 and OE 7' for already-placed events."""
    n = [f'OE {LABEL[k]}' for k in keys]
    return n[0] if len(n) == 1 else ', '.join(n[:-1]) + ' and ' + n[-1]


def join_ids(ids):
    return ', '.join(ids)


def slack(ts):
    return clean(rows('slack.slack_messages', ts=ts)[0]['text'])


def mail(subject):
    m = [r for r in rows('gmail.gmail_messages', subject=subject) if r['user_email'] == 'claire.morgan@harmonygames.co']
    return clean(m[0]['body_text'])


ASK = slack('1759269913.882683')
EVT = rows('gcal.gcal_events', event_id='evt_d947bf7cd910549b674b1f')[0]
README = GRID['Read me'][0][0]
CAL = clean(rows('gdocs.docs_documents', document_id='f_fdd6d2d2f4a4d2f5b908fb')[0]['body_text'])
DECK = '\n'.join(clean(r['text']) for r in rows('gslides.slides_page_elements', presentation_id='f_5ebf55ad29e815d46243c8'))
TA = {a['id']: json.loads(a['data_json'])['text'] for a in rows('trello.trello_actions', type='commentCard')}
CARD = rows('trello.trello_cards', id='68dc52e015f87c50c441d1a9')[0]
UNITY = '\n'.join(' | '.join(r) for r in GRID['Unity'])
STORE = '\n'.join(' | '.join(r) for r in GRID['Store'])
ARCH = '\n'.join(' | '.join(r) for r in GRID['Archive'])

# ------------------------------------------------------------------ the ask and its sources
ev('ask', 'Find #zombie_marketing in Slack and read Leonard\'s message of yesterday (channel search with private channels included, since the channel is private, then read the channel)',
   'Leonard Hayes, Tue Sep 30 2025 3:05 PM PT, tagging Claire: "go through everything that\'s live today and work out what gets a halloween version, what needs work first, what we already have, and who makes what by when". Sources: "the live creatives sheet is what\'s running"; "Arthur\'s release calendar has the Q4 dates"; "Robert has direction for seasonal art"; "Frederick is sending his october UA plan tonight"; "Martin has the icon and the stills, Marcus has video and end cards". "maybe we swap the icon around the 24th?" Asks: "put it all in a plan doc we can comment on plus a tracker"; "drop a comment on each ad\'s ART ticket with its call and due date, and assign the ones that need new work to whoever\'s making them so Frederick can queue the uploads"; "open tickets for any new store art and post the links here before thursday\'s review". Channel C06DJBJL798, message ts 1759269913.882683.',
   ('ask', ASK + ' C06DJBJL798 1759269913.882683'))

ev('review', 'Find the review on Claire\'s calendar in Google Calendar (search "review", Oct 1 to Oct 4 2025)',
   'Event "ZM3D Halloween review", starts Thu Oct 2 2025 9:00 AM PT, organizer leonard.hayes@harmonygames.co. "Claire walks us through the Halloween plan and tracker." Attendees besides Claire: leonard.hayes@harmonygames.co, frederick.stone@harmonygames.co, martin.walsh@harmonygames.co, marcus.bennett@harmonygames.co, robert@harmonygames.co, arthur.blake@harmonygames.co.',
   ('event', EVT['summary'] + ' ' + EVT['description'] + ' ' + EVT['attendees_json'] + ' ' + EVT['organizer_email']))

ev('readme', 'Find the live creatives sheet in Drive (search "live creatives") and read its Read me and Store tabs in Sheets (ranges "Read me" and "Store")',
   'Spreadsheet "ZM3D live creatives", owner frederick.stone@harmonygames.co, tabs Read me, Store, Unity, Archive. Read me: "One row per creative serving on our four Unity retention campaigns today (iOS UK phone, iOS UK tablet, Android US phone, Android US tablet) plus the store listing sets."; "Paused or retired creatives move to Archive."; "campaigns, capture and master notes are in the ticket comments"; "Store sets have no ART ticket."; "Halloween push: see the Halloween push card on the ZM roadmap." Store rows: "app icon", "iPhone 6.5" set", "iPad 12.9" set", "Google Play phone set", 4 surfaces.',
   ('sheet', README + ' ZM3D live creatives ' + json.dumps(GRID['Store'])))

ev('unity', 'Read the Unity tab of the sheet from {readme} in Sheets, every row',
   f'56 rows, each with its creative, format and ART ticket: ' + '; '.join(f'{SHEET[k]} {k}' for k in sorted(SHEET)) + '.',
   ('unity', UNITY))

ev('archive', 'Read the Archive tab of the sheet from {readme} in Sheets',
   '4 paused rows, left out of the plan: GreenCouch 001 ART-836, Professional Mode 9x16 test ART-837, sophie ocean portrait ART-838, squirrelfail portrait text ART-839.',
   ('arch', ARCH))

ev('card', 'Find the Halloween push card and its comment in Trello (the Read me in {readme} names it; search "halloween")',
   f'Card "{CARD["name"]}" on board ZM ROADMAP. Frederick\'s comment, Tue Sep 30 2025 4:20 PM PT: "Julia\'s 4:5 static (They\'re coming, stop them!) is still running on iOS UK"; "It never made it onto the live creatives sheet, so count it in for Halloween." That static is ART-826, the 4:5 static off the sheet.',
   ('card', CARD['name'] + ' ZM ROADMAP ' + TA['68dc65a0f2d7fb28743f5860']))

ev('calendar', 'Find Arthur\'s release calendar in Drive and read it in Docs (search "release calendar", which finds his one Q4 doc)',
   'Owner arthur.blake@harmonygames.co. "Oct 17 submission: the last build that can carry Halloween changes. Merge cut is Thu Oct 16, 12:00 PT. Anything that ships in the build has to be merged by then. Submit Fri Oct 17." "iOS screenshots can only change with a new version, so new iOS screenshots go up with the Oct 17 submission and are due by the same Oct 16 12:00 PT cut." "plan on that build and its iOS store listing being live from Wed Oct 22." "Google Play listing graphics are not tied to a build: upload any day and allow 1 day for review." "Nov 6 submission: post-Halloween clean-up (icon and screenshots back to normal)." So the icon rides the Oct 17 build, not a swap around the 24th.',
   ('cal', CAL + ' ZM3D release calendar ' + 'arthur.blake@harmonygames.co'))

ev('deck', 'Find Robert\'s seasonal direction deck in Drive and read it in Slides (search "seasonal"; the ask in {ask} says Robert has it)',
   'Owner robert@harmonygames.co. "Anything captured or rendered from a build older than Android #1452 / iOS 1232 (the zombie swap with the new background, Jul 29) is redone on the current build first. If a later capture has replaced it, the newest capture is the one that counts." "A video whose master has the music baked in is re-cut first from a master without music (re-export one from the project if there is none), so the seasonal pass can be edited." Calls: "Halloween version: dress it from the current art." "Refresh first: re-capture, re-render or re-cut before any seasonal pass." "Reuse: it already has a seasonal version, use that one." "Skip: no seasonal version this time."',
   ('deck', DECK + ' robert@harmonygames.co'))

ev('mails', 'List the mail from Frederick in Claire\'s Gmail (search "from:frederick.stone@harmonygames.co"; the ask in {ask} says his plan is coming)',
   '3 message ids with their thread ids; the subject, date and body come from opening each one.',
   ('mails', ''))

ev('draft', 'Open the first of Frederick\'s 3 mails in Gmail (oldest id from {mails})',
   'Subject "October UA plan (draft)", Fri Sep 12 2025 10:40 AM PT: "Halloween flight Oct 20-31 on all four campaigns. Halloween creatives to me by Fri Oct 17 so I can upload them."',
   ('draft', 'October UA plan (draft) ' + mail('October UA plan (draft)')))

ev('changes', 'Open the newest of Frederick\'s 3 mails in Gmail (newest id from {mails})',
   'Subject "October UA plan - changes", Tue Sep 30 2025 4:10 PM PT, replacing the Sep 12 dates: "The Android US tablet campaign ends Sun Oct 12 and its budget moves to iOS UK, so don\'t make Halloween versions of anything that only runs there." "The Halloween flight now runs Sat Oct 18 - Fri Oct 31 on the other three campaigns." "every Halloween ad needs to be with me by Wed Oct 15, not the 17th."',
   ('changes', 'October UA plan - changes ' + mail('October UA plan - changes')))

ev('restart', 'Open the third of Frederick\'s 3 mails in Gmail (remaining id from {mails})',
   'Subject "Unity retention restart", Mon Sep 29 2025 4:48 PM PT: "I left squirrelfail landscape and mrfluffernot landscape off iOS UK tablet this time, they were the weakest there. Both stay on Android US tablet." So ART-811 and ART-813 now run only on Android US tablet, whatever their ticket notes say.',
   ('restart', 'Unity retention restart ' + mail('Unity retention restart')))

ev('reply', 'Search Slack for anything newer on the Android US phone campaign and read the hit in #zombie-match3d (search "Android US phone"; the campaign name comes from {readme})',
   'A reply by Frederick, Tue Sep 30 2025 4:42 PM PT, after his 4:10 PM mail: "They\'re putting every new Android creative through manual review for the next few weeks, about 5 days each. So any new ad going on Android US phone has to be with me by Fri Oct 10, not the 15th. iOS UK stays on the 15th." So every working ad on Android US phone is due Fri Oct 10, also when it runs on iOS UK too; every other working ad stays Wed Oct 15.',
   ('reply', slack('1759275738.984915')))

ev('leave', 'Check who makes the ad stills while the plan runs: search Slack for "ad statics" and read the thread it finds in #company-internal',
   'Martin Walsh, Tue Sep 30 2025 7:41 AM PT: "I\'ll be on vacation Oct 6-15. <@EMPLOYEE_0005_SLACK_ID> takes the ad statics while I\'m out, store art stays with me." Leonard\'s reply, Tue Sep 30 2025 4:31 PM PT, after his ask: "thanks martin. julia on the ad statics works for me".',
   ('leave', slack('1759243286.478812') + ' ' + slack('1759275107.322377')))

ev('who', 'Look up the person Martin tags in Slack (user profile for EMPLOYEE_0005_SLACK_ID)',
   'Julia Lawson, julia.lawson@harmonygames.co. So Julia makes the ad statics and Martin keeps the icon and store art.',
   ('who', 'Julia Lawson julia.lawson@harmonygames.co'))

ev('note', 'Search Slack for the April-captured cuts by creative name and read Marcus\'s post in #zm-animations (search "couch alpha 50", the name on ART-795)',
   'Marcus Bennett, Thu Sep 25 2025 11:12 AM PT: "re-recorded 3 of the old ua cuts for frederick, same edits, no music: couch alpha 50 on android #1935, barrel marketing2 4:5 on #1896, balloons alpha 50 (1) on #1966". These newer captures beat the April notes on ART-795, ART-805 and ART-797 under the deck\'s newest-capture line. The other cuts of those names keep their own captures.',
   ('note', slack('1758823964.738872')))

ev('im', 'Search Slack for the cheer fastcouch cuts and read Marcus\'s reply in Claire\'s DM with him (search "cheer fastcouch")',
   'Marcus Bennett, Mon Sep 29 2025 10:20 AM PT: "did the cheer fastcouch one, both 9:16 and 16:9, from the no music masters."',
   ('im', slack('1759166437.080255')))

ev('masters', 'Find the Halloween folder in Drive and list its UA masters subfolder (search "ZM3D Halloween 2025"; Marcus names the subfolder)',
   'Folder "ZM3D Halloween 2025" holds subfolders "Store" and "UA masters". "UA masters" holds 2 files owned by marcus.bennett@harmonygames.co: cheer_fastcouch_halloween_9x16.mp4 and cheer_fastcouch_halloween_16x9.mp4.',
   ('masters', 'ZM3D Halloween 2025 Store UA masters cheer_fastcouch_halloween_9x16.mp4 cheer_fastcouch_halloween_16x9.mp4'))

ev('review_test', 'Read the thread on that test in Slack #zombie-art (Marcus\'s post is the #zombie-art hit of the "cheer fastcouch" search in {im}; read its thread for the replies)',
   'Marcus, Mon Sep 29 2025 10:31 AM PT: "quick test on cheer fastcouch, 9:16 and 16:9, pumpkins and fog over the cut. files are in ua masters". Robert, Tue Sep 30 2025 9:05 AM PT: "Fog reads well but this is the July capture, the old background is still under it. We can\'t ship these, they need doing again from the Sep 16 one". Marcus, 9:21 AM PT: "ok, i will redo both from the sep 16 capture". So Marcus\'s test in {im} and {masters} can\'t ship: cheer fastcouch 9:16 and 16:9 (ART-808, ART-816) are not Reuse, they get new Halloween versions from the Sep 16 capture, assigned to Marcus.',
   ('rt', slack('1759167065.499092') + ' ' + slack('1759248337.170599') + ' ' + slack('1759249269.380507')))

ev('packs', 'Search Trello comments for end card 001 by creative name (search "end card 001", the name on ART-833)',
   'Frederick Stone\'s comment on card "Marketing Video Refresh (Marcus/[PERSON_NAME_0036])", Fri Sep 26 2025 10:40 AM PT: "end card 001 still has the old zombies on the packs, Martin\'s new packs came after Marcus rendered it. Same on the 16:9, 1:1 and 4:5 cut from it. They can keep serving for now but they need a re-render before anyone builds on them." So ART-833, ART-834, ART-835 and ART-848 are Refresh first, whatever build their tickets name.',
   ('packs', 'Marketing Video Refresh (Marcus/[PERSON_NAME_0036]) ' + TA['68d6cff0c6568da5d9c8e81f']))

ev('music', 'Read Frederick\'s Aug 13 thread in Slack #zombie_marketing (ART-809\'s comment points to it; search "in:zombie_marketing on:2025-08-13", then read the thread)',
   BASE['music']['expected'], ('music', BASE['music']['text']))

ev('export', 'Search Slack for the store export and read Martin\'s post and Leonard\'s reply in #zombie-art (search "store screens", then the thread)',
   'Martin, Tue Sep 30 2025 8:20 AM PT: "halloween store screens are exported to the halloween folder". Leonard, 8:47 AM PT: "whatever is already exported is done so no tickets needed for those, tickets are just for store art that still has to be made".',
   ('export', slack('1759245641.309714') + ' ' + slack('1759247246.453725')))

folder = [r for r in rows('gdrive.drive_files') if 'd_74a7c95c28097dd9777e01' in str(r.get('parents_json'))]
names = sorted(r['name'] for r in folder)
assert len(names) == 11
ev('store', 'List the Store subfolder of "ZM3D Halloween 2025" in Drive (folder from {masters})',
   'The Store subfolder holds 11 PNG files: ZM3D_Halloween_iPhone65_01_1242x2688.png to ZM3D_Halloween_iPhone65_05_1242x2688.png (5) and ZM3D_Halloween_GooglePlay_phone_01_1080x1920.png to ZM3D_Halloween_GooglePlay_phone_06_1080x1920.png (6). The iPhone 6.5" and Google Play sets exist, so they are Reuse. The iPad 12.9" set is on the sheet ({readme}) with no file here, so it is new art.',
   ('store', ' '.join(names)))

ev('icon', 'Search Slack for the icon concept and read Martin\'s post and Robert\'s reply in #zombie-art (search "app icon", then the thread)',
   BASE['icon']['expected'], ('icon', BASE['icon']['text'] + ' ' + slack('1758127951.679146')))

ev('library', 'List the ART team\'s tickets created since Sep 1 2025 in Linear to catch ads the sheet leaves out (team ART, created from 2025-09-01, limit 100)',
   '62 tickets, ART-793 to ART-854, each described as "UA creative library". 56 are on the Unity tab, 4 are the Archive rows ("Paused on Sep 15, see the Archive tab" on ART-836 to ART-838, "Paused on Sep 19" on ART-839) and 2 are off the sheet: ART-826 "julia 4:5" and ART-831 "marcus portrait UA end card". 58 serving ads.',
   ('lib', ' '.join(ISS[k]['title'] + ' ' + ISS[k]['description'] + ' ' + k for k in sorted(ISS))))

# ------------------------------------------------------------------ ticket comments, in ticket order
BATCHES = [('ART-793', 'ART-804'), ('ART-805', 'ART-816'), ('ART-817', 'ART-824'), ('ART-825', 'ART-835'), ('ART-840', 'ART-854')]
for i, (a, b) in enumerate(BATCHES, 1):
    ks = [k for k in ADS if a <= k <= b]
    parts = []
    src = []
    for k in ks:
        notes = [c['body'] for c in CM[k]]
        keep = [notes[0]] + [n for n in notes[1:] if not n.startswith('Still running on Unity') or k == 'ART-831']
        parts.append(f'{k} ' + ' '.join(f'"{n}"' for n in keep))
        src.extend(notes)
    ev(f'cmts{i}', f'Read the comments on each ticket {a} to {b} in Linear, one call per ticket ({len(ks)} tickets from {{library}})',
       '; '.join(parts) + '.', (f'cm{i}', ' '.join(src)))


def render(k):
    return k


# ------------------------------------------------------------------ decisions
skip = BY['Skip']
ev('d_skip', 'Work out the Skip ads from the campaigns in the ticket comments and the two mails (Linear comments plus Gmail, rule from {changes})',
   f'{len(skip)} ads run only on Android US tablet, which ends Sun Oct 12: {join_ids(skip)}. ART-811 and ART-813 are in this set through {{restart}}. Each is Skip, with no due date and no assignee.')

hv = BY['Halloween version']
ev('d_hv', 'Work out the Halloween version ads against the deck\'s rule (Linear comments, Slack posts and the deck)',
   f'{len(hv)} working ads whose newest capture is at or after Android #1452 with a master without music, leaving out the four end card 001 cuts of {{packs}}: ART-795, ART-797 and ART-805 (new captures, {{note}}); ART-808 and ART-816 (Android #1896 re-capture, with the test turned down in {{review_test}}); ART-817, ART-818 and ART-819 (Android #1630); ART-851, ART-852, ART-853 and ART-854 (Android #1896, #1935 and #1966).')

rf = BY['Refresh first']
pre = [k for k in rf if k not in ('ART-809', 'ART-833', 'ART-834', 'ART-835', 'ART-848')]
ev('d_rf', 'Work out the Refresh first ads against the deck\'s rule (Linear comments, Slack and Trello)',
   f'{len(rf)} working ads. Source older than Android #1452, or captured before Jul 29 ({len(pre)}): {join_ids(pre)}. ART-831 is Android #1450, two builds short. ART-840\'s capture is Jul 28; its Sep 11 opening is an edit, not a capture. ART-823 keeps its April capture ({{note}} names three other cuts). Music baked into the master on a current capture: ART-809 ({{music}}). Old zombies on the packs: ART-833, ART-834, ART-835, ART-848 ({{packs}}).')

ev('d_due', 'Work out each working ad\'s due date from its campaigns (Linear comments, Frederick\'s mail in {changes} and reply in {reply})',
   f'Fri Oct 10, on Android US phone ({len(D10)}): {join_ids(D10)}. Wed Oct 15, every other working ad ({len(D15)}): {join_ids(D15)}. 48 working ads in all.')

ev('d_maker', 'Work out who makes each working ad (Slack, the ask in {ask} and the cover in {leave})',
   f'Julia Lawson, the ad statics ({len(JULIA)}): {join_ids(JULIA)}. Their due dates fall inside Martin\'s Oct 6-15 vacation. Marcus Bennett, video and end cards ({len(MARCUS)}): every other ad in {{d_hv}} and {{d_rf}}, including ART-832, though its description says "Made by Martin Walsh", and the ART-808 and ART-816 redo.')

ev('d_store', 'Work out the four store calls (Sheets, Drive, Docs and Slack, from {readme}, {store}, {icon} and {calendar})',
   'App icon: Halloween version, Martin Walsh, due by the Thu Oct 16 12:00 PT merge cut for the Oct 17 build. iPad 12.9" set: Halloween version, Martin Walsh, due by the same cut. iPhone 6.5" set: Reuse, Martin Walsh, ships with the Oct 17 submission by the same cut. Google Play phone set: Reuse, Martin Walsh, upload any day and allow 1 day for review. Martin keeps these through his vacation ("store art stays with me", {leave}). New store art is the icon and the iPad set, so those two get tickets; the exported sets get none ({export}).')

ev('users', 'Look up the makers in Linear (users Marcus Bennett, Julia Lawson and Martin Walsh; team ART)',
   BASE['users']['expected'], ('users', BASE['users']['text']))

# ------------------------------------------------------------------ writes
ev('w_doc', 'Create the plan doc in Claire\'s Drive in Google Docs',
   'A new Google Doc owned by Claire with the Halloween plan: the calls by surface type, with counts ({d_store}, {d_hv}, {d_rf}, {d_skip}); the ship route and dates: the icon, the iPad 12.9" set and the iPhone 6.5" set by the Thu Oct 16 12:00 PT cut for the Oct 17 submission (the icon rides that build, not a swap around the 24th), the Google Play phone set any day with 1 day for review, ads on Android US phone with Frederick by Fri Oct 10, every other working ad by Wed Oct 15; what is reused: the iPhone 6.5" and Google Play sets; owners: Martin the icon and store art, Julia the ad statics, Marcus video and end cards.')

ev('w_sheet', 'Create the tracker spreadsheet in Claire\'s Drive in Google Sheets',
   'A new spreadsheet owned by Claire with Halloween in its title.')

ev('w_rows', 'Write the tracker rows into the spreadsheet from {w_sheet} in Sheets (rows from {d_skip}, {d_hv}, {d_rf}, {d_due}, {d_maker} and {d_store})',
   'A header and 62 rows, one per serving surface: 4 store surfaces, 56 Unity rows, ART-826 and ART-831; each with its call and a short reason, plus its owner and due date as worked out above (Skip rows have neither; the Google Play phone set has an owner and no fixed date). Calls: Halloween version 14, Refresh first 36, Reuse 2, Skip 10. The 4 Archive rows stay out.')

SHARE = [('Leonard Hayes', 'leonard.hayes@harmonygames.co'), ('Frederick Stone', 'frederick.stone@harmonygames.co'),
         ('Martin Walsh', 'martin.walsh@harmonygames.co'), ('Marcus Bennett', 'marcus.bennett@harmonygames.co'),
         ('Robert', 'robert@harmonygames.co'), ('Arthur Blake', 'arthur.blake@harmonygames.co')]
for what, key in (('plan doc', 'w_doc'), ('tracker', 'w_sheet')):
    for who, addr in SHARE:
        ev(f'w_share_{key}_{addr}', f'Share the {what} from {{{key}}} with {who} in Drive (address from {{review}})',
           f'{addr} has commenter access on the {what}.')

for k in ADS:
    d = due(k)
    src = 'd_skip' if call(k) == 'Skip' else ('d_hv' if call(k) == 'Halloween version' else 'd_rf')
    tail = f'{call(k)}, due {d}' if d else 'Skip, with no due date'
    pts = f'{{{src}}}' + ('' if not d else ', {d_due}')
    ev(f'w_c_{k}', f'Comment the call and due date on {k} ({name(k)}) in Linear ({pts})',
       f'A new comment on {k}: {tail}.')

MAIL = {'Marcus Bennett': 'marcus.bennett@harmonygames.co', 'Julia Lawson': 'julia.lawson@harmonygames.co'}
for k in ADS:
    if maker(k):
        ev(f'w_a_{k}', f'Assign {k} to {maker(k)} in Linear ({{d_maker}}, {{users}})',
           f'{k} has assignee {MAIL[maker(k)]}.')

ev('w_t_icon', 'Open an ART ticket for the Halloween app icon in Linear (team ART, {d_store})',
   'A new ART ticket for the Halloween app icon, assignee martin.walsh@harmonygames.co, due 2025-10-16 for the Thu Oct 16 12:00 PT merge cut.')
ev('w_t_ipad', 'Open an ART ticket for the Halloween iPad 12.9" set in Linear (team ART, {d_store})',
   'A new ART ticket for the Halloween iPad 12.9" set, assignee martin.walsh@harmonygames.co, due 2025-10-16 for the Thu Oct 16 12:00 PT merge cut.')
ev('w_reply', 'Reply in Leonard\'s thread in Slack #zombie_marketing with both links (thread from {ask}; the doc link comes back on the shares in {w_share_w_doc_leonard.hayes@harmonygames.co}, the tracker link on {w_sheet})',
   'A thread reply under ts 1759269913.882683 in C06DJBJL798 holding the plan doc link and the tracker link.')


FRONT = ['ask', 'review', 'readme', 'unity', 'archive', 'calendar', 'deck', 'library', 'card', 'cmts1', 'cmts2', 'cmts3', 'cmts4', 'cmts5',
         'mails', 'draft', 'changes', 'restart', 'reply', 'leave', 'who', 'note', 'im', 'masters', 'review_test', 'packs', 'music', 'export', 'store', 'icon']
_pos = {k: i for i, k in enumerate(FRONT)}
EVENTS.sort(key=lambda e: _pos.get(e[0], len(FRONT)))
LABEL.update({e[0]: i for i, e in enumerate(EVENTS, 1)})


def fill(text):
    def sub(m):
        return f'OE {LABEL[m.group(1)]}' if m.group(1) in LABEL else m.group(0)
    return re.sub(r'\{([a-zA-Z0-9_.@-]+)\}', sub, text)


out = []
for i, (key, h, e) in enumerate(EVENTS, 1):
    out.append(f'OE {i}  {fill(h)}\nExpected: {fill(e)}\n')
text = '\n'.join(out)

# ------------------------------------------------------------------ checks
assert '—' not in text and '–' not in text, 'dash in OE text'
assert not re.search(r'\{[a-zA-Z0-9_.@-]+\}', text), re.findall(r'\{[a-zA-Z0-9_.@-]+\}', text)[:5]
bad = 0
total = 0
for key, h, e in EVENTS:
    srcs = SOURCES[key]
    if not srcs:
        continue
    inch = lambda x: re.sub(r'(\d\.\d)\\?"', r'\1 inch', x)
    hay = norm(inch(' '.join(t for _, t in srcs)))
    for q in re.findall(r'"((?:[^"\\]|\\.)+)"', inch(e)):
        q2 = norm(q)
        total += 1
        if q2 not in hay and q2.rstrip('.') not in hay:
            bad += 1
            print('QUOTE NOT IN SOURCE', key, repr(q2[:110]))
print('events', len(EVENTS), 'chars', len(text), 'quotes checked', total, 'bad', bad)
if bad:
    sys.exit(1)
open(os.path.join(TI, '08_Oracle_Events.md'), 'w').write(text)
json.dump({'label': LABEL, 'events': [(k, h, e) for k, h, e in EVENTS]}, open(os.path.join(HERE, 'events.json'), 'w'), indent=0)
