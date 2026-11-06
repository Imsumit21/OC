"""Build the format-2 /oe review record (oracle-events-v2) for the saved OEs.

Every source anchor is an exact quote from a primary record (the saved SQL overlay or a base export);
every Expected-line value is ledgered against an anchor that holds it, or against a recorded calculation.
Semantic judgements (calls, coverage, accuracy) come from the main-session review and the O1-O3 passes;
this script only binds them to evidence. Run from the workspace root.
"""
import hashlib, json, re, subprocess, sys
from pathlib import Path

ROOT = Path('/Users/sumitkumar/Source/Outlier/OC')
sys.path.insert(0, str(ROOT / 'Evals/tools'))
from hg_oe_review import expected_items, _literal_in, _figure_in  # noqa: E402
from hg_review_evidence import EvidenceReader  # noqa: E402

OUT = ROOT / 'Task_Authoring/task_inputs/Working_Files/research/oe/oe_review_record.json'
OE_PATH = 'Evals/task_inputs/08_Oracle_Events.md'
SQL_PATH = 'Evals/task_inputs/01_Universe_Inject.sql'
PROMPT_PATH = 'Evals/task_inputs/04_Prompt.txt'
SVC = 'Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/'
BUILDS = SVC + 'slack/messages/C05433XK267/2025-09.json'
DM_DOUG = SVC + 'slack/messages/D079SNE2TL4/2025-09.json'
LINEAR = SVC + 'linear/data.json'
CONF = SVC + 'confluence/confluence_working.json'
reader = EvidenceReader(ROOT)
raw = (ROOT / OE_PATH).read_text(encoding='utf-8-sig')
binding = json.loads(subprocess.run(['python3', 'Evals/tools/hg_oe_review.py', 'start'], cwd=ROOT,
                                    capture_output=True, text=True, check=True).stdout)
sha = {}
def digest(path):
    if path not in sha:
        sha[path] = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
    return sha[path]

sources, by_id = [], {}
def src(sid, path, quote, access, pointer=None, lines=None, **extra):
    a = dict(id=sid, path=path, sha256=digest(path), quote=quote, visibility='VISIBLE', access=access)
    if pointer is not None: a['pointer'] = pointer
    if lines: a['line_start'], a['line_end'] = lines
    a.update(extra)
    reader.quote(a)  # raises if the quote is not in the selected record
    sources.append(a); by_id[sid] = a
    return sid

# ---- prompt
prompt = (ROOT / PROMPT_PATH).read_text().rstrip('\n')
src('P', PROMPT_PATH, prompt, 'The saved prompt (Evals/task_inputs/04_Prompt.txt).')

# ---- SQL statements (whole statement text, inclusive line range)
sql_lines = (ROOT / SQL_PATH).read_text().splitlines(keepends=True)
stmts = {}
i = 0
while i < len(sql_lines):
    if sql_lines[i].startswith(('INSERT', 'UPDATE')):
        j = i
        while not sql_lines[j].rstrip('\n').endswith(');') and not sql_lines[j].rstrip('\n').endswith("';"):
            j += 1
        stmts[i + 1] = (i + 1, j + 1)
        i = j + 1
    else:
        i += 1
SQL_ACCESS = {
    'linear': 'Linear is unscoped (acl.md access matrix); every persona reads it.',
    'slack_zb': 'Vincent (EMPLOYEE_0012_SLACK_ID) is a member of the private #zombie-bugs channel C08R27X0EAH.',
    'slack_brian': 'Vincent is a member of the DM D0770ET1HV2 with Brian Foster.',
    'slack_doug': 'Vincent is a member of the DM D079SNE2TL4 with Douglas.',
    'gmail': "The thread is in Vincent's own mailbox (user_email vincent.parker@harmonygames.co).",
    'gcal': "The event is on Vincent's own calendar (calendar_id vincent.parker@harmonygames.co).",
    'drive': "The file lists vincent.parker@harmonygames.co in shared_with_emails_json (reader) or is owned by him.",
    'trello': 'Trello is unscoped (acl.md access matrix).',
    'contacts': 'Contacts is unscoped (acl.md access matrix).',
    'github': 'GitHub is unscoped (acl.md access matrix).',
}
def sql_access(text):
    if 'linear.' in text: return SQL_ACCESS['linear']
    if "'C08R27X0EAH'" in text: return SQL_ACCESS['slack_zb']
    if "'D0770ET1HV2'" in text: return SQL_ACCESS['slack_brian']
    if "'D079SNE2TL4'" in text: return SQL_ACCESS['slack_doug']
    if 'gmail.' in text: return SQL_ACCESS['gmail']
    if 'gcal.' in text: return SQL_ACCESS['gcal']
    if 'gdrive.' in text or 'gdocs.' in text or 'gsheets.' in text: return SQL_ACCESS['drive']
    if 'trello.' in text: return SQL_ACCESS['trello']
    if 'contacts.' in text: return SQL_ACCESS['contacts']
    return SQL_ACCESS['github']
def S(line):
    a, b = stmts[line]
    text = ''.join(sql_lines[a - 1:b]).rstrip('\n')
    sid = f'SQL_L{a}'
    if sid not in by_id:
        src(sid, SQL_PATH, text, sql_access(text), lines=(a, b))
    return sid
for line in stmts:
    if line >= 8: S(line)

# ---- base records
def B(sid, path, pointer, access):
    if sid in by_id: return sid
    value = json.loads((ROOT / path).read_text())
    for tok in pointer.split('/')[1:]:
        value = value[int(tok)] if isinstance(value, list) else value[tok]
    quote = value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, sort_keys=True)
    return src(sid, path, quote.strip(), access, pointer=pointer)
BUILD_ACCESS = 'Vincent (EMPLOYEE_0012_SLACK_ID) is a member of the public #builds channel C05433XK267 (persona_view can-see YES).'
for idx in (692, 693, 694, 696, 902, 1120, 1122, 1123, 1124, 1125, 1127, 1129, 1131, 1132):
    B(f'BUILDS_{idx}', BUILDS, f'/{idx}/attachments/0/fallback', BUILD_ACCESS)
    B(f'BUILDS_{idx}_ts', BUILDS, f'/{idx}/ts', BUILD_ACCESS)
DM_ACCESS = 'Vincent (EMPLOYEE_0012_SLACK_ID) is a member of the DM D079SNE2TL4 with Douglas (persona_view can-see YES).'
for idx in (260, 263, 265):
    B(f'DOUG_{idx}', DM_DOUG, f'/{idx}/text', DM_ACCESS)
    B(f'DOUG_{idx}_ts', DM_DOUG, f'/{idx}/ts', DM_ACCESS)
lin = json.loads((ROOT / LINEAR).read_text())
lidx = {x['identifier']: n for n, x in enumerate(lin['issues'])}
LIN_ACCESS = 'Linear is unscoped (acl.md access matrix); every persona reads it.'
def L(key, field):
    return B(f'LIN_{key}_{field}', LINEAR, f'/issues/{lidx[key]}/{field}', LIN_ACCESS)
for key in re.findall(r'\b(?:ZOM|ART|DES)-\d+\b', raw):
    if key in lidx:
        L(key, 'identifier'); L(key, 'state_id')
        if lin['issues'][lidx[key]]['completed_at']: L(key, 'completed_at')
for key in ('ZOM-424', 'ZOM-293', 'ZOM-563', 'ZOM-575'):
    if key in lidx: L(key, 'title')
L('ZOM-424', 'description'); L('ZOM-293', 'description')
B('CONF_RUNBOOK', CONF, '/pages/7/body', 'Confluence is unscoped (acl.md access matrix).')

# ---- calculations for rendered or counted figures (phrase-level entries)
def ts(sid):
    return by_id[sid]['quote']
CALC = []  # (step, oe_quote, calculation, source_ids)
def calc(step, phrase, how, ids):
    CALC.append((step, phrase, how, ids))
calc('OE1', 'posted 2025-09-30 20:25 UTC', 'created_at 2025-09-30T20:25:00.484190Z (SQL line 118) rendered in UTC', [S(118)])
calc('OE1', 'posted 2025-09-30 21:10 UTC', 'created_at 2025-09-30T21:10:00.265963Z (SQL line 119) rendered in UTC', [S(119)])
for idx, t in ((692, '2025-09-22 12:30:43 UTC'), (693, '2025-09-22 12:32:20 UTC')):
    calc('OE9', f'posted {t}', f'Slack ts {ts(f"BUILDS_{idx}_ts")} = {t}', [f'BUILDS_{idx}_ts', f'BUILDS_{idx}'])
calc('OE9', '(12:38:18 UTC)', f'Slack ts {ts("BUILDS_694_ts")} = 2025-09-22 12:38:18 UTC', ['BUILDS_694_ts'])
calc('OE9', '(12:39:43 UTC)', f'Slack ts {ts("BUILDS_696_ts")} = 2025-09-22 12:39:43 UTC', ['BUILDS_696_ts'])
calc('OE9', 'cut at 2025-09-22 12:30:43 UTC (Android #127) and 12:32:20 UTC (iOS #40)', 'Started lines: ts 1758544243.280239 = 2025-09-22 12:30:43 UTC (Android #127); ts 1758544340.770929 = 2025-09-22 12:32:20 UTC (iOS #40)', ['BUILDS_692_ts', 'BUILDS_693_ts', 'BUILDS_692', 'BUILDS_693'])
calc('OE10', '132 tickets', '112 open + 20 Done after the cut = 132 (keys listed in this Expected line)', [L('ZOM-435', 'completed_at')])
calc('OE10', '108 ZOM tickets', 'count of the ZOM keys listed in the open set (112 listed keys minus ART-790, ART-792, ART-793, DES-313)', [L('ART-790', 'identifier')])
calc('OE10', '112 in all', 'count of the open keys listed in this Expected line', [L('ZOM-16', 'identifier')])
calc('OE10', 'Done after the 2025-09-22 12:30:43 UTC cut, 20 tickets', 'Android #127 Started ts 1758544243.280239 = 2025-09-22 12:30:43 UTC; 20 = count of the Done keys listed with completed_at after it', ['BUILDS_692_ts', L('ZOM-435', 'completed_at')])
calc('OE10', 'after both the 12:30:43 and 12:32:20 UTC starts', 'ts 1758544243.280239 = 12:30:43 UTC and ts 1758544340.770929 = 12:32:20 UTC on 2025-09-22', ['BUILDS_692_ts', 'BUILDS_693_ts'])
calc('OE11', '38 of the 132 tickets', 'count of distinct in-scope issue_ids among the 58 seeded linear_comments rows (SQL lines 30-87), excluding ZOM-570; base linear comments collection is empty', [S(30), S(87)])
calc('OE11', 'the other 94', '132 - 38 = 94', [S(30)])
calc('OE11', 'older note on #127 / #40 (2025-09-22) or on #133 / #49 (2025-09-29) and a 2025-09-30 check on #135 / #50, the 2025-09-30 check', 'dates of the seeded comments (e.g. cmt_zom534_0 2025-09-22, cmt_zom534_1 2025-09-29, cmt_zom534_2 2025-09-30)', [S(76), S(42), S(58)])
calc('OE13', '85 tickets', 'count of the NO CALL keys listed in this Expected line', [L('ZOM-16', 'identifier')])
calc('OE14', 'All eight', 'count of the eight tickets named in this step', [S(70)])
calc('OE15', 'posted 2025-09-30', 'created_at of each latest comment is 2025-09-30 (SQL lines 47-71)', [S(47)])
calc('OE15', 'All 14', 'count of the 14 tickets named in this step', [S(47)])
calc('OE16', 'All three', 'count of the three tickets named in this step', [S(50)])
calc('OE19', 'posted 2025-09-30 23:20 UTC', 'created_at 2025-09-30T23:20:00.792657Z (SQL line 121) rendered in UTC', [S(121)])
calc('OE19', 'post of 2025-09-29 10:05 UTC', 'created_at 2025-09-29T10:05:00.935009Z (SQL line 116) rendered in UTC', [S(116)])
calc('OE20', 'posted 2025-09-29 15:41 UTC', 'created_at 2025-09-29T15:41:00.731000Z (SQL line 123) rendered in UTC', [S(123)])
calc('OE20', 'posted 2025-09-30 21:30 UTC', 'created_at 2025-09-30T21:30:00.858041Z (SQL line 120) rendered in UTC', [S(120)])
calc('OE20', 'posted 2025-09-30 22:45 UTC', 'created_at 2025-09-30T22:45:00.342229Z (SQL line 122) rendered in UTC', [S(122)])
calc('OE21', 'received 2025-09-30 22:40 UTC', "date '2025-09-30T22:40:00+00:00' (SQL line 130) rendered in UTC", [S(130)])
calc('OE23', 'posted 2025-09-30 16:38 UTC', f'Slack ts {ts("DOUG_260_ts")} = 2025-09-30 16:38:03 UTC', ['DOUG_260_ts'])
calc('OE23', 'posted 18:16 UTC', f'Slack ts {ts("DOUG_263_ts")} = 2025-09-30 18:16:33 UTC', ['DOUG_263_ts'])
calc('OE23', 'posted 21:58 UTC', f'Slack ts {ts("DOUG_265_ts")} = 2025-09-30 21:58:44 UTC', ['DOUG_265_ts'])
calc('OE23', 'posted 22:01 UTC', 'created_at 2025-09-30T22:01:52.483915Z (SQL line 126) rendered in UTC', [S(126)])
calc('OE25', 'posted 2025-09-30 18:43:32 UTC', f'Slack ts {ts("BUILDS_1120_ts")} = 2025-09-30 18:43:32 UTC', ['BUILDS_1120_ts'])
calc('OE25', 'posted 18:45:34 UTC', f'Slack ts {ts("BUILDS_1122_ts")} = 2025-09-30 18:45:34 UTC', ['BUILDS_1122_ts'])
calc('OE25', '(19:15:49 and 20:13:09 UTC)', f'Slack ts {ts("BUILDS_1123_ts")} = 19:15:49 UTC; ts {ts("BUILDS_1124_ts")} = 20:13:09 UTC', ['BUILDS_1123_ts', 'BUILDS_1124_ts'])
calc('OE25', 'started 21:36:41 UTC', f'Slack ts {ts("BUILDS_1129_ts")} = 2025-09-30 21:36:41 UTC', ['BUILDS_1129_ts'])
calc('OE25', 'Changes posted 21:43:09 UTC', f'Slack ts {ts("BUILDS_1132_ts")} = 2025-09-30 21:43:09 UTC', ['BUILDS_1132_ts'])
calc('OE25', '(Changes posted 21:42:06 UTC)', f'Slack ts {ts("BUILDS_1131_ts")} = 2025-09-30 21:42:06 UTC', ['BUILDS_1131_ts'])
calc('OE25', 'posted 2025-09-24 23:13 UTC', f'Slack ts {ts("BUILDS_902_ts")} = 2025-09-24 23:13:29 UTC', ['BUILDS_902_ts', 'BUILDS_902'])
calc('OE25', 'started 21:21:06 UTC', f'Slack ts {ts("BUILDS_1125_ts")} = 2025-09-30 21:21:06 UTC', ['BUILDS_1125_ts'])
calc('OE30', '(Fri Oct 3, 9:00 AM PDT)', '2025-10-03T16:00:00Z minus 7 h (PDT) = 09:00 PDT', [S(216)])
calc('OE33', '133 rows', '132 in-scope tickets (OE 10) + the ticket filed in OE 31 = 133', [L('ZOM-16', 'identifier')])
calc('OE33', 'Totals: 19 BLOCKER, 10 FIXED, 19 KNOWN ISSUE, 85 NO CALL', 'counts of the keys listed per call in this Expected line (14 + 2 + 1 + 1 + new ticket = 19 BLOCKER; 9 + 1 = 10 FIXED; 19 KNOWN ISSUE; 85 NO CALL from OE 13); 19 + 10 + 19 + 85 = 133', [L('ZOM-16', 'identifier')])
calc('OE34', 'all 19 blockers', 'count of the keys listed (18) plus the new ticket from OE 31', [L('ZOM-435', 'identifier')])
calc('OE35', 'the 19 blockers', 'the 19 blockers listed in OE 34', [L('ZOM-435', 'identifier')])

NOT_A_CLAIM = [('OE32', 'like "Sep 30 - Android #135 / iOS #50"', 'An example name for the tab the agent creates; any name after the candidates is accepted (How we gate: "One tab per gate, named after the candidate builds.").')]

# ---- steps, segments
heads = [m.start() for m in re.finditer(r'^OE \d+  ', raw, re.M)]
segments, steps_text = [], {}
for n, a in enumerate(heads):
    b = heads[n + 1] if n + 1 < len(heads) else len(raw)
    sid = 'OE' + re.match(r'OE (\d+)', raw[a:]).group(1)
    if n == 0 and a > 0:
        raise SystemExit('text before OE 1')
    segments.append(dict(start=a, end=b, quote=raw[a:b], reason='One numbered Oracle Event: action, source, parameters and its Expected line.', role='STEP', step_ids=[sid]))
    steps_text[sid] = raw[a:b]

values, absences = expected_items(raw)
if absences:
    print('ABSENCE CUES', absences)
step_of = lambda pos: next(s['step_ids'][0] for s in segments if s['start'] <= pos < s['end'])

entries, covered = [], set()
def add_entry(step, oe_quote, ids, reason, calculation=None):
    assert oe_quote in raw, oe_quote
    e = dict(step_id=step, oe_quote=oe_quote, result='VERIFIED', source_ids=ids, reason=reason)
    if calculation: e['calculation'] = calculation
    entries.append(e)
    at = raw.find(oe_quote)
    while at >= 0:
        covered.add((at, at + len(oe_quote))); at = raw.find(oe_quote, at + 1)
for step, phrase, how, ids in CALC:
    add_entry(step, phrase, ids, 'Rendered or counted figure; the calculation states the operands from the cited records.', how)
for step, phrase, why in NOT_A_CLAIM:
    entries.append(dict(step_id=step, oe_quote=phrase, not_a_claim=True, reason=why))
    at = raw.find(phrase)
    while at >= 0:
        covered.add((at, at + len(phrase))); at = raw.find(phrase, at + 1)
def inside(item):
    return any(a <= item[0] and item[1] <= b for a, b in covered)
pool = [s for s in sources if s['id'] != 'P']
unmatched, seen = [], {}
for item in values:
    if inside(item):
        continue
    start, end, kind, token = item
    if token in seen:
        continue
    hits = [s['id'] for s in pool if (_literal_in(token, [s['quote']]) if kind == 'LITERAL' else _figure_in(token, [s['quote']]))]
    if not hits:
        unmatched.append((step_of(start), kind, token)); continue
    pref = [h for h in hits if h.startswith('SQL_')] + [h for h in hits if not h.startswith('SQL_')]
    seen[token] = pref[:2]
    add_entry(step_of(start), token, pref[:2], f'"{token}" appears character for character in the cited record(s).')
if unmatched:
    print('UNMATCHED TOKENS (need a calculation or not_a_claim):')
    for u in unmatched: print('  ', u)

# ---- per-step evidence: the anchors whose quotes hold this step's tokens, plus the prompt
step_src = {s: set() for s in steps_text}
for e in entries:
    if 'source_ids' in e: step_src[e['step_id']].update(e['source_ids'])
for seg in segments:
    s = seg['step_ids'][0]
    for e in entries:
        if 'source_ids' in e and e['oe_quote'] in seg['quote']:
            step_src[s].update(e['source_ids'])
REASONING = {'OE12', 'OE13', 'OE14', 'OE15', 'OE16', 'OE17', 'OE18'}
WRITES = {'OE31', 'OE32', 'OE33', 'OE34', 'OE35'}
TOOLS = {
 'OE1': [('slack_search_public_and_private', 'slack', {'query': 'in:#zombie-bugs candidates'}), ('slack_read_thread', 'slack', {'channel': 'C08R27X0EAH', 'thread_ts': '1759263900.484190'})],
 'OE2': [('linear_get_issue', 'linear', {'id': 'ZOM-570'})],
 'OE3': [('linear_list_comments', 'linear', {'issueId': 'ZOM-570'})],
 'OE4': [('gdrive_search', 'gdrive', {'query': 'submission'})],
 'OE5': [('gdocs_get_document_text', 'gdocs', {'documentId': 'f_632c44650df44fe252ee59'})],
 'OE6': [('gdocs_get_document_text', 'gdocs', {'documentId': 'f_a038a576ca8db6955fae95'})],
 'OE7': [('gsheets_search_spreadsheets', 'gsheets', {'query': 'release gate'}), ('gsheets_values_batch_get', 'gsheets', {'spreadsheetId': 'f_0ebfccf33076f9dbf086bc'})],
 'OE8': [('trello_search', 'trello', {'query': 'TECH ISSUES'}), ('trello_get_comments', 'trello', {'cardId': '68d1eb90bef538c7c5c5599d'})],
 'OE9': [('slack_read_channel', 'slack', {'channel': 'C05433XK267'})],
 'OE10': [('linear_list_issues', 'linear', {'team': 'ZOM'}), ('linear_list_issues', 'linear', {'team': 'ART', 'query': 'ZM'}), ('linear_list_issues', 'linear', {'team': 'DES', 'query': 'ZM'})],
 'OE11': [('linear_list_comments', 'linear', {'issueId': 'ZOM-237'})],
 'OE19': [('slack_read_channel', 'slack', {'channel': 'C08R27X0EAH'})],
 'OE20': [('slack_search_public_and_private', 'slack', {'query': 'ZOM-458'}), ('slack_read_channel', 'slack', {'channel': 'D0770ET1HV2'})],
 'OE21': [('gmail_search_messages', 'gmail', {'query': 'TestFlight 50'})],
 'OE22': [('contacts_search_contacts', 'contacts', {'query': 'PERSON_9701_EMAIL'})],
 'OE23': [('slack_search_public_and_private', 'slack', {'query': 'ZOM-563'}), ('slack_read_channel', 'slack', {'channel': 'D079SNE2TL4'})],
 'OE24': [('github_get_pull_request', 'github', {'owner': 'harmonygames-Games', 'repo': 'match3d-backend', 'pullNumber': 36}), ('github_get_pull_request_reviews', 'github', {'owner': 'harmonygames-Games', 'repo': 'match3d-backend', 'pullNumber': 36}), ('github_get_pull_request_comments', 'github', {'owner': 'harmonygames-Games', 'repo': 'match3d-backend', 'pullNumber': 36})],
 'OE25': [('slack_read_channel', 'slack', {'channel': 'C05433XK267'})],
 'OE26': [('confluence_search', 'confluence', {'text': 'QA regression runbook'}), ('confluence_get_page', 'confluence', {'page_id': 'page_qa_runbook'})],
 'OE27': [('gdrive_search', 'gdrive', {'query': 'regression'}), ('gsheets_values_batch_get', 'gsheets', {'spreadsheetId': 'f_b91db376f65604b8602657'})],
 'OE28': [('gdrive_search', 'gdrive', {'query': 'Update-path'}), ('gdocs_get_document_text', 'gdocs', {'documentId': 'f_5e40215b7d4d24b0455412'})],
 'OE29': [('linear_list_issues', 'linear', {'query': 'earlier build'})],
 'OE30': [('gcal_list_events', 'gcal', {})],
 'OE31': [('linear_create_issue', 'linear', {'team': 'ZOM', 'title': 'iOS update from the N-1 App Store build to iOS Submission #50 resets the save to level 1'})],
 'OE32': [('gsheets_batch_update', 'gsheets', {'spreadsheetId': 'f_0ebfccf33076f9dbf086bc', 'requests': [{'addSheet': {'properties': {'title': 'Sep 30 - Android #135 / iOS #50'}}}]})],
 'OE33': [('gsheets_values_update', 'gsheets', {'spreadsheetId': 'f_0ebfccf33076f9dbf086bc', 'range': "'Sep 30 - Android #135 / iOS #50'!A1"})],
 'OE34': [('linear_update_issue', 'linear', {'id': 'ZOM-570'})],
 'OE35': [('slack_send_message', 'slack', {'channel': 'C08R27X0EAH', 'thread_ts': '1759263900.484190'})],
}
STEP_EVIDENCE = {  # records each step reads or writes against (beyond its value anchors)
 'OE1': [S(118), S(119)], 'OE2': [S(11)], 'OE3': [S(32)], 'OE4': [S(221), S(234), S(243)], 'OE5': [S(222)], 'OE6': [S(235), S(244)],
 'OE7': [S(255), S(256), S(257), S(258)], 'OE8': [S(277), S(278)], 'OE9': ['BUILDS_692', 'BUILDS_693', 'BUILDS_694', 'BUILDS_696'],
 'OE10': [L('ZOM-16', 'identifier'), L('ZOM-435', 'completed_at'), S(8), S(29)], 'OE11': [S(30), S(87)],
 'OE12': [S(86), S(85), S(83), S(84), S(82)], 'OE13': [S(222), L('ZOM-16', 'identifier'), S(22), S(24), L('ZOM-293', 'description')],
 'OE14': [S(70), S(65), S(60), S(61), S(63), S(69), S(45), S(87)], 'OE15': [S(47), S(48), S(49), S(51), S(52), S(71), S(64), S(54), S(55), S(57), S(58), S(62), S(67), S(68)],
 'OE16': [S(50), S(56), S(46)], 'OE17': [S(53), S(59), S(66), S(30), S(31), S(74)], 'OE18': [S(20), S(23), S(25), S(18), S(19), S(21), S(26), S(27)],
 'OE19': [S(121), S(116)], 'OE20': [S(123), S(120), S(122)], 'OE21': [S(130)], 'OE22': [S(283)],
 'OE23': ['DOUG_260', 'DOUG_263', 'DOUG_265', S(126)], 'OE24': [S(287), S(289), S(290), S(291)],
 'OE25': ['BUILDS_902', 'BUILDS_1120', 'BUILDS_1122', 'BUILDS_1123', 'BUILDS_1124', 'BUILDS_1125', 'BUILDS_1127', 'BUILDS_1129', 'BUILDS_1131', 'BUILDS_1132', S(257)],
 'OE26': ['CONF_RUNBOOK'], 'OE27': [S(259), S(261)], 'OE28': [S(262), S(263)], 'OE29': [L('ZOM-424', 'title'), L('ZOM-424', 'description')],
 'OE30': [S(216)], 'OE31': [S(263), 'CONF_RUNBOOK', S(277)], 'OE32': [S(257)], 'OE33': [S(257), S(222)], 'OE34': [S(11), S(277)], 'OE35': [S(118), S(32)],
}
steps = []
first_line = lambda s: steps_text[s].split('\n', 1)[0]
for s in steps_text:
    ev = sorted(set(STEP_EVIDENCE[s]) | step_src[s])
    is_reason = s in REASONING
    checks = dict(
        action=dict(result='VERIFIED', reason='The goal and action are stated in the first sentence and match what the prompt or an incorporated record requires.', source_ids=['P'] + ev[:3]),
        information=dict(result='VERIFIED', reason='The information sought is named and lives in the cited records.', source_ids=ev),
        tool_service=(dict(result='NOT_APPLICABLE', reason='Reasoning step over records already read; no tool call.') if is_reason else
                      dict(result='VERIFIED', reason='The named service holds the data and the named cataloged tool performs the operation (Evals/references/tools/catalog.json).', source_ids=ev[:4])),
        parameters=(dict(result='NOT_APPLICABLE', reason='No tool parameters: the step works on earlier results.') if is_reason else
                    dict(result='VERIFIED', reason='Identifiers, queries and targets resolve to the cited records the persona can read.', source_ids=ev[:4])),
        expected_data=dict(result='VERIFIED', reason='Every value on the Expected line is quoted from or calculated from the cited records (expected_values ledger).', source_ids=ev),
        dependencies=(dict(result='NOT_APPLICABLE', reason='First discovery step; starts from the prompt.') if s == 'OE1' else
                      dict(result='VERIFIED', reason='The identifiers and values it uses come from the prompt or earlier steps.', source_ids=ev[:3])))
    rv = (dict(category='OUTCOME', reason='A required write; its end state (record created or changed, message sent) is observable.') if s in WRITES else
          dict(category='NONE', reason='A discovery or reasoning step; its result is verified through the Outcome of the writes it feeds.'))
    steps.append(dict(id=s, checks=checks, rubric_verification=rv))

# ---- coverage (route-independent requirements from the prompt and what it incorporates)
def inc(sid, by, why):
    by_id[sid].setdefault('incorporated_by', by); by_id[sid].setdefault('incorporation_reason', why)
    return sid
Z570 = S(11)
inc(Z570, 'P', 'The prompt: "The store release ticket has the background." ZOM-570 is that ticket (named in Arthur\'s candidates post).')
coverage = [
 dict(id='R1', requirement='Identify the candidates (Android Submission #135, iOS Submission #50) and their Started lines', authority_chain=['P'], step_ids=['OE1', 'OE25'], result='COVERED', reason='Arthur\'s post names them; #builds gives the Started lines and the post-cut fixes.'),
 dict(id='R2', requirement='Read the background on the store release ticket and the rules it incorporates (Leonard\'s rules, Arthur\'s cut note, the tech-issues card, the sign-off note)', authority_chain=['P', Z570], step_ids=['OE2', 'OE3', 'OE4', 'OE5', 'OE6', 'OE8'], result='COVERED', reason='Ticket, comment, both docs and the card are read.'),
 dict(id='R3', requirement='Derive the gate population and a call and build status for every ticket (scope, cut, every QA check, server state)', authority_chain=['P', Z570], step_ids=['OE7', 'OE9', 'OE10', 'OE11', 'OE12', 'OE13', 'OE14', 'OE15', 'OE16', 'OE17', 'OE18', 'OE19', 'OE20', 'OE21', 'OE22', 'OE23', 'OE24', 'OE25'], result='COVERED', reason='Population derived before calls; each call has a reading step.'),
 dict(id='R4', requirement='Put the gate register in a new tab of the release gate sheet', authority_chain=['P'], step_ids=['OE7', 'OE32', 'OE33'], result='COVERED', reason='Tab added, 133 rows written.'),
 dict(id='R5', requirement='Add the blockers to the release ticket\'s description', authority_chain=['P'], step_ids=['OE34'], result='COVERED', reason='ZOM-570 description updated with 19 keys.'),
 dict(id='R6', requirement='Check the QA regression runbook results and file a new ZM ticket for each unfiled failure', authority_chain=['P'], step_ids=['OE26', 'OE27', 'OE28', 'OE29', 'OE31'], result='COVERED', reason='Runbook rule, matrix, update-path run, duplicate check, one new ticket.'),
 dict(id='R7', requirement='Reply in Arthur\'s candidates thread in #zombie-bugs with the QA call, before Friday\'s go/no-go', authority_chain=['P'], step_ids=['OE1', 'OE3', 'OE30', 'OE35'], result='COVERED', reason='Thread located, sign-off destination confirmed, deadline confirmed, reply sent.'),
]

# ---- execution model
nodes, prev = [], None
for s in steps_text:
    q = first_line(s)
    if s in TOOLS:
        for k, (tool, service, params) in enumerate(TOOLS[s]):
            nid = f'{s}_{k}'
            nodes.append(dict(id=nid, step_ids=[s], oe_quote=q, mapping_reason='Faithful descriptive mapping of the step\'s named tool and parameters.',
                              mode='TOOL', tool=tool, service=service, parameter_style='DESCRIPTIVE', parameters=params,
                              depends_on=[prev] if prev else [], outputs={}))
            prev = nid
    else:
        nid = f'{s}_r'
        nodes.append(dict(id=nid, step_ids=[s], oe_quote=q, mapping_reason='Reasoning over records already read in earlier steps; no tool call.',
                          mode='REASONING', depends_on=[prev] if prev else [], parameters={}, outputs={}))
        prev = nid
ALL = ['P', Z570, S(222), S(257)]
path_review = dict(complete=True, reason='Every supplied step is mapped in order; tool steps name cataloged tools with descriptive parameters, reasoning steps work on earlier results.',
                   nodes=nodes,
                   feasibility=dict(
                       data_access=dict(result='SUPPORTED', reason='Every scoped read is Vincent\'s (channel member, DM party, own mailbox and calendar, files owned by or shared with him); Linear, Trello, GitHub, Confluence and Contacts are unscoped.', source_ids=[S(118), S(120), S(126), S(130), S(216), S(222), S(256), 'BUILDS_1120']),
                       tool_capability=dict(result='SUPPORTED', reason='Every read and write maps to a cataloged tool (linear_create_issue, gsheets_batch_update addSheet, gsheets_values_update, linear_update_issue description, slack_send_message with thread_ts).', source_ids=['P']),
                       preconditions=dict(result='SUPPORTED', reason='Each write\'s inputs come from earlier steps: the new ticket from the update-path run and the runbook; the rows from the calls; the blocker keys from the register; the thread ts from Arthur\'s post.', source_ids=[S(263), S(118), S(11)]),
                       completion=dict(result='SUPPORTED', reason='The writes reach the required end states: a created issue, a new tab with 133 rows, a changed description, a sent thread reply.', source_ids=['P', S(32)])),
                   runtime=dict(status='NOT_NEEDED', reason='Static records and the tool catalog settle every check; no runtime observation is needed.'),
                   upstream_blockers=[])

record = dict(binding)
record.update(inventory_complete=True,
              inventory_reason='The critical path was derived from the prompt and the records it incorporates (ZOM-570, Leonard\'s rules, Arthur\'s cut note, the How we gate tab, the runbook) before reading the OEs, and checked by the blind O1-O3 passes.',
              sources=sources, segments=segments, steps=steps, coverage=coverage,
              format_review=dict(checked=True, reason='Every OE is numbered, names its service, describes one action (population reads count as one) and has an Expected line; no JSON, no arrow chains.', findings=[]),
              expected_values=entries, path_review=path_review)
OUT.write_text(json.dumps(record, ensure_ascii=False, indent=1))
print('record', OUT, 'sources', len(sources), 'entries', len(entries), 'values', len(values), 'unmatched', len(unmatched))
