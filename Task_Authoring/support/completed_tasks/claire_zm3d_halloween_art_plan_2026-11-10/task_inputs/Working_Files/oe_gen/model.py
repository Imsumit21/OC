"""Re-derive every ad's call, due date and maker from the seeded rows alone and assert against solver/truth.json.
Rows are parsed from 01_Universe_Inject.sql (never executed). Used by the ledger, event and check builders."""
import json, os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.dirname(HERE)
TI = os.path.dirname(WF)
S = json.load(open(os.path.join(HERE, 'sql_rows.json')))
TRUTH = json.load(open(os.path.join(WF, 'solver', 'truth.json')))
def rows(t, **kw):
    return [x['row'] for x in S if x.get('table') == t and x['op'] == 'insert' and all(x['row'].get(k) == v for k, v in kw.items())]
def sql_line(t, **kw):
    return [x['line'] for x in S if x.get('table') == t and x['op'] == 'insert' and all(x['row'].get(k) == v for k, v in kw.items())][0]
ISS = {r['id']: r for r in rows('linear.linear_issues')}
CM = collections.defaultdict(list)
for c in rows('linear.linear_comments'):
    CM[c['issue_id']].append(c)
for k in CM:
    CM[k].sort(key=lambda c: c['created_at'])
GRID = {r['title']: json.loads(r['grid_json']) for r in rows('gsheets.sheets_sheets')}
ARCHIVE = [r[3] for r in GRID['Archive'][1:]]
SHEET = {r[3]: r[0] for r in GRID['Unity'][1:]}
ADS = sorted(k for k in ISS if k not in ARCHIVE)
assert len(ADS) == 58 and len(ARCHIVE) == 4 and len(SHEET) == 56
OFF_SHEET = [k for k in ADS if k not in SHEET]
assert OFF_SHEET == ['ART-826', 'ART-831']
def name(k):
    return re.sub(r' \([^()]*\)$', '', ISS[k]['title'])
def kind(k):
    return re.search(r'\(([^()]*)\)$', ISS[k]['title']).group(1)
SWAP = 1452
NEW_CAPTURE = {'ART-795': 1935, 'ART-805': 1896, 'ART-797': 1966}     # Marcus's #zm-animations note
PACKS = ['ART-833', 'ART-834', 'ART-835', 'ART-848']                  # Frederick's Trello comment
TRIM = ['ART-811', 'ART-813']                                         # Frederick's restart mail
MUSIC_THREAD = ['ART-809']                                            # Frederick's Aug 13 thread
def campaigns(k):
    c = None
    for x in CM[k]:
        m = re.search(r'Unity(?: Sep \d+)?: ([^.(]+?)(?: \(checked [^)]*\))?\.', x['body'])
        if m: c = [s.strip() for s in m.group(1).split(',')]
    if k in TRIM:
        assert 'iOS UK tablet' in c
        c = [x for x in c if x != 'iOS UK tablet']
    return c
def source(k):
    """newest capture build number, or None when the ticket gives only a date"""
    if k in NEW_CAPTURE: return NEW_CAPTURE[k]
    b = [int(n) for x in CM[k] for n in re.findall(r'Android #(\d+)', x['body'])]
    return max(b) if b else None
def prescap(k):
    s = source(k)
    if s is not None: return s < SWAP
    body = CM[k][0]['body']
    return bool(re.search(r'Captured (Dec 5, 2024|Apr \d+|Jul 28)', body))
def music(k):
    return k in MUSIC_THREAD or any('music baked into the master' in x['body'] for x in CM[k]) 
def call(k):
    if campaigns(k) == ['Android US tablet']: return 'Skip'
    if k in PACKS or prescap(k) or music(k): return 'Refresh first'
    return 'Halloween version'
def due(k):
    if call(k) == 'Skip': return None
    return 'Fri Oct 10' if 'Android US phone' in campaigns(k) else 'Wed Oct 15'
def maker(k):
    if call(k) == 'Skip': return None
    return 'Julia Lawson' if kind(k).endswith('static') else 'Marcus Bennett'
TMAP = {'HALLOWEEN VERSION': 'Halloween version', 'REFRESH FIRST': 'Refresh first', 'SKIP': 'Skip', 'REUSE': 'Reuse'}
for k in ADS:
    t = TRUTH[name(k)]
    assert TMAP[t['call']] == call(k), (k, t, call(k))
    assert t['due'] == due(k), (k, t, due(k))
    assert t['owner'] == maker(k), (k, t, maker(k))
BY = collections.defaultdict(list)
for k in ADS: BY[call(k)].append(k)
assert (len(BY['Halloween version']), len(BY['Refresh first']), len(BY['Skip'])) == (12, 36, 10)
D10 = [k for k in ADS if due(k) == 'Fri Oct 10']; D15 = [k for k in ADS if due(k) == 'Wed Oct 15']
assert (len(D10), len(D15)) == (30, 18)
JULIA = [k for k in ADS if maker(k) == 'Julia Lawson']; MARCUS = [k for k in ADS if maker(k) == 'Marcus Bennett']
assert (len(JULIA), len(MARCUS)) == (6, 42)
if __name__ == '__main__':
    print('model matches truth for', len(ADS))
    for c, v in BY.items(): print(c, len(v), v)
    print('D10', D10); print('D15', D15); print('J', JULIA)
    pre = [k for k in BY['Refresh first'] if prescap(k)]
    print('refresh prescap', len(pre)); print('refresh other', [k for k in BY['Refresh first'] if not prescap(k)])
    print('music', [k for k in ADS if music(k)])
    print('nobuild', [k for k in ADS if source(k) is None])
    print(collections.Counter(tuple(campaigns(k)) for k in ADS))
    ev = rows('gcal.gcal_events', event_id='evt_d947bf7cd910549b674b1f')[0]
    print(ev['attendees_json'])
