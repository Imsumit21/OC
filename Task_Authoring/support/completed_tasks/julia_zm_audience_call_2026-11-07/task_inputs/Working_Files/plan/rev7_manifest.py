"""rev7 S0r delta for the draft and final manifests (de-signposted request, two-sided K3, R_G, R_T, retention
correction on the KPI tab, 82-session cohort). Reads the rev7 SQL and the solver truth; never executes SQL.
Run from the workspace root: python -X utf8 Task_Authoring/task_inputs/Working_Files/plan/rev7_manifest.py
"""
import copy, hashlib, json, pathlib, re

TI = pathlib.Path('Task_Authoring/task_inputs')
WF = TI / 'Working_Files'
SQL = (TI / '01_Universe_Inject.sql').read_text(encoding='utf-8')
TRUTH = json.loads((WF / 'solver' / 'truth.json').read_text(encoding='utf-8'))
SESS = [k for k in TRUTH if k not in ('panel', 'retention')]
ZOM = [k for k in SESS if k.startswith('ZOM-')]

A1 = 'C090N54TG79/1758517286.431379'
L707 = 'C090N54TG79/1759266627.418203'
CARD = '68dc0acf1815df76ed9b887d'
LOG_NOTE = 'f_c691d577b8f837eb4f9eaa'
GATE_DOC = 'f_748d26e760e54651eaa0d8'
GATE_POST = '2c84150a541063a6138e2f5a0cff9f33'
REL_RULE = 'ba19de7863a540175f2aeadc12916fa6'
IND_RULE = 'e72083b249987542a134098010edd305'
QA_SHEET, QA_POST, QA_REPLY = 'f_cadae9f611d82d56ac02c3', '3dd0b6d6c52c21cd5bbfcd6d6f5345cd', '3d8e451a198d5d59b39e60064b590305'
T_MAIL = 'julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com>'
KPI = 'f_4e21b203a62910bdae0353'
L705 = '2ca968ace3e14d1a34c535f8a5c0cd6e'
G_CONTACTS = ['0810fb8287e489c125fe2cd9', '038b5eb5a30326895cb54756']
RC27 = 'harmonygames-Games/match3d#476#rc_27'
ZOM567_CMT = 'cmt_38b3cc50dceda37f40f5'


def row_text(rid):
    lines = [ln for ln in SQL.split('\n') if "'" + rid + "'" in ln]
    assert lines, rid
    return '\n'.join(lines).replace("''", "'").replace('\\n', '\n')


def must_in(rid, quote):
    assert quote in row_text(rid), (rid, quote)
    return quote


A1_TEXT = ("get real-life feedback from 25–45 casual and/or RPG gamer friends (not kids). No coaching, just observe "
           "and collect honest reactions.\n• Once we have clean data from a tech-stable beta in 15-20 days")


def frag_updates(frags):
    by = {f['id']: f for f in frags}

    def setf(fid, via, ev, quote, **kw):
        f = by[fid]
        f['incorporated_via'], f['delegated_by_record'] = via, ev
        f['delegation_quote'] = quote if ev == A1 else must_in(ev if not ev.startswith('C090N54TG79/') else
                                                                 '1759266627.418203', quote)
        f.update(kw)

    assert '25–45 casual and/or RPG gamer friends (not kids)' in A1_TEXT
    setf('F-AGE', ['A1'], A1, '25–45 casual and/or RPG gamer friends (not kids)',
         seeded_ids=['12b40a5b7cc18f7c9fe2d0a9e0e929b4', '4bd8937a7616a1ba2d6e6151ffc3a492', REL_RULE])
    setf('F-INDUSTRY', ['A1'], A1, 'collect honest reactions', seeded_ids=[IND_RULE, REL_RULE])
    setf('F-GATE', ['A1'], A1, 'clean data from a tech-stable beta')
    setf('F-RERUN', ['A1'], A1, 'get real-life feedback')
    setf('F-LEAD', ['A2'], L707, 'casual, RPG or no clear lead')
    for fid in ('F-DEVICE', 'F-BUILD'):
        by[fid]['incorporated_via'] = ['A1', 'F-GATE']
    setf('F-LIMIT', ['A1', 'F-GATE', 'F-DEVICE'], GATE_DOC,
         "Arthur Blake owns the Vision Bot job and says what its passes do and don't cover")
    setf('F-MEMO', ['A2'], L707, 'what goes in it is on the roadmap card')
    by['F-FOLDER']['incorporated_via'] = ['A2', 'F-MEMO']
    setf('F-STATE', ['A2', 'F-MEMO'], CARD, 'with her log note')
    setf('F-PANEL', ['A2', 'F-MEMO'], CARD, 'with the panel and retention as context')
    setf('F-PANELDEF', ['A2', 'F-MEMO'], CARD, 'the panel and retention as context')
    setf('F-RET', ['A2', 'F-MEMO'], CARD, 'retention as context')
    new = [
        dict(id='F-QA', service='slack', container='C08R27X0EAH/1759158757.418562',
             locator='C08R27X0EAH/1759158757.418562', kind='requirement', incorporated_via=['A1', 'F-GATE', 'F-DEVICE'],
             seeded_ids=[QA_POST, QA_REPLY, QA_SHEET], base_pointers=[], delegated_by_record=GATE_DOC,
             delegation_quote=must_in(GATE_DOC, 'A pass is a clean test run of the build players get'),
             requirement_ids=['R2']),
        dict(id='F-PLAYERS', service='contacts', container='contacts:julia.lawson', locator='contacts job field',
             kind='exclusion', incorporated_via=['A2', 'F-MEMO', 'F-STATE'], seeded_ids=list(G_CONTACTS),
             base_pointers=[], delegated_by_record=LOG_NOTE,
             delegation_quote=must_in(LOG_NOTE, 'Players are in my contacts'), requirement_ids=['R4']),
        dict(id='F-LATE', service='gmail', container='julia.lawson@harmonygames.co/1844324114366762178',
             locator=T_MAIL, kind='requirement', incorporated_via=['A2', 'F-MEMO', 'F-STATE'], seeded_ids=[T_MAIL],
             base_pointers=[], delegated_by_record=LOG_NOTE,
             delegation_quote=must_in(LOG_NOTE, 'Any form that comes in after this batch gets a ticket and a log row when I see it'),
             requirement_ids=['R7', 'R14']),
        dict(id='F-RETCUT', service='gsheets', container=KPI, locator='KPI tab, note row', kind='amendment',
             incorporated_via=['A2', 'F-MEMO', 'F-RET'], seeded_ids=[KPI], base_pointers=[], delegated_by_record=L705,
             delegation_quote=must_in(L705, 'when we quote ZM retention'), requirement_ids=['R11']),
    ]
    assert must_in(GATE_POST, 'ZM session stability gate')
    out = [f for f in frags if f['id'] not in {n['id'] for n in new}] + new
    return out


def traps_update(traps):
    by = {t['id']: t for t in traps}
    t = by['T-K3']
    t.update(services=['gdocs', 'slack', 'gsheets', 'linear', 'github'],
             seeded_ids=['ZOM-567', ZOM567_CMT, RC27, 'harmonygames-Games/match3d#476#rev_3', QA_POST, QA_REPLY, QA_SHEET],
             expected_wrong_reading=("the 13 Samsung sessions are dropped, with re-run notes: ZOM-567's Vision Bot "
                                     "pass is editor play mode per Arthur's rc_27, so no on-device pass seems to exist"),
             resolver=("Vincent's Sep 29 QA matrix in #zombie-bugs and its sheet: real device yes, SM-A546E, "
                       "0.3.127 (127), PASS. A clean pass of the build players get ran on a Samsung phone, and the "
                       "gate says once there is a pass it covers all the Samsung sessions"),
             discovery_order=("the gate Doc, ZOM-567 and Arthur's rc_27 are met on the gate path and all argue "
                              "exclusion; the matrix sits in #zombie-bugs, which nothing in the ask names, and names "
                              "the phone only by model number"),
             version_records=[
                 {"service": "slack", "seeded": True, "at": "2025-09-29T15:12:37Z", "id": QA_POST,
                  "container": "slack:C08R27X0EAH"},
                 {"service": "linear", "seeded": True, "at": "2025-09-30T16:50:22Z", "id": ZOM567_CMT,
                  "container": "linear:ZOM-567"},
                 {"service": "github", "seeded": True, "at": "2025-09-30T20:10:26Z", "id": RC27,
                  "container": "github:harmonygames-Games/match3d#476"}])
    by['T-K5']['expected_wrong_reading'] = ("the 13 sessions count: form and log look complete and the build id reads "
                                            "as one more ordinary id")
    by['T-F']['expected_wrong_reading'] = ("not-counted tickets get a state and nothing else, or every one of the 37 "
                                           "gets a re-run note, or the Samsung sessions get one")
    by['T-559']['expected_wrong_reading'] = ("drops the Samsung sessions because ZOM-559 is open")
    by['T-559']['resolver'] = ("the stability gate says ZOM-559 stays in the bug queue and nobody waits on it; only a "
                               "device pass decides, and Vincent's matrix is one")
    by['T-S23']['expected_wrong_reading'] = ("adds Leonard's S23 Ultra bug report as an 83rd session or a Samsung data "
                                             "point")
    r = by['T-RET']
    r['expected_wrong_reading'] = ("install-weighted D7 over every mature cohort (9.09 %), or the KPI tab's simple "
                                   "cohort mean")
    r['resolver'] = ("Robert's post sets install weighting over mature cohorts from USER_COHORT_RETENTION; Vincent's "
                     "later note on his KPI tab leaves out the Calm Play cohorts before 2025-07-24, so 16 rows, "
                     "2,607 installs, 10.47 %")
    vr = list(r.get('version_records') or [])
    if not any(v['id'] == KPI for v in vr):
        vr.append({"service": "gsheets", "seeded": True, "at": "2025-09-30T10:22:41Z", "id": KPI,
                   "container": "gsheets:" + KPI})
    r['version_records'] = sorted(vr, key=lambda v: v['at'])
    r['seeded_ids'] = sorted(set(r.get('seeded_ids') or []) | {KPI})
    new = [
        {"id": "T-G", "family": "near_miss_mention", "services": ["contacts", "gdocs", "slack"],
         "seeded_ids": list(G_CONTACTS) + [IND_RULE], "base_pointers": [], "requirement": "R4",
         "expected_wrong_reading": ("only Brian's batch is game industry; ZOM-598 and ZOM-622 count because no doc, "
                                    "ticket or form says what their players do"),
         "resolver": ("the log note says players are in Julia's contacts; the contacts' job field shows a console "
                      "games publisher QA tester and a mobile games studio live ops producer, and Leonard's rule "
                      "drops anyone who works in games, sessions already run included"),
         "discovery_order": "the notes docs give only 'Player: First Last'; the job sits in Contacts, a service no ask names"},
        {"id": "T-T", "family": "cross_reference_gap", "services": ["gmail", "gdocs", "linear", "gsheets"],
         "seeded_ids": [T_MAIL, LOG_NOTE], "base_pointers": [], "requirement": "R14",
         "expected_wrong_reading": "the read covers the 80 ticketed sessions only; Owen's two late sessions are missed",
         "resolver": ("Owen's Sep 30 20:40Z reply in his form thread reports two Sep 28 sessions inline, and the log "
                      "note says a form that comes in after the batch gets a ticket and a log row"),
         "discovery_order": "no ticket, Log row or notes doc carries them; the reply sits under Owen's older form mail"},
    ]
    return [t for t in traps if t['id'] not in ('T-G', 'T-T')] + new


def chains_update(chains):
    by = {c['id']: c for c in chains}
    by['CH-K3']['hops'] = [
        {"service": "gdocs", "record": GATE_DOC, "finding": "Samsung is the one device group; a session counts once a clean pass ran on that device, and one pass covers all the Samsung sessions"},
        {"service": "linear", "record": "ZOM-567", "finding": "Done ticket cites Vision Bot run #15 and an editor repro"},
        {"service": "github", "record": RC27, "finding": "Arthur: the Vision Bot pass is Unity editor play mode, no phone in the loop"},
        {"service": "slack", "record": QA_POST, "finding": "Vincent's Sep 29 0.3.127 (127) regression matrix in #zombie-bugs, all green"},
        {"service": "gsheets", "record": QA_SHEET, "finding": "real device yes, SM-A546E, 0.3.127 (127), PASS"}]
    new = {"id": "CH-G", "root_cause": "A13", "ends_in": "R4", "hops": [
        {"service": "gdocs", "record": LOG_NOTE, "finding": "players are in Julia's contacts"},
        {"service": "contacts", "record": G_CONTACTS[1], "finding": "job: QA tester, console games publisher"},
        {"service": "slack", "record": IND_RULE, "finding": "game-industry people do not count, sessions already run included"}]}
    return [c for c in chains if c['id'] != 'CH-G'] + [new]


def portfolio_update(mp):
    import importlib.util
    spec = importlib.util.spec_from_file_location('s7', str(WF / 'solver' / 'solver.py'))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    keep = {x['id']: x for x in mp}
    reasons = {k: v.get('prior_family_reason') for k, v in keep.items()}
    reasons['R_K3'] = ("same mechanism id: done in one service, the missing piece in a joined second service "
                       "(ledger trial julia_card_art_signoff); rev7 makes it two-sided, so the safe default now fails")
    reasons['R_G'] = ("same family as R_K4 (A13, inclusion by attribute): the deciding fact is a structured field in a "
                      "service no ask names; completed-task evidence: inclusion by attribute, not keyword, beat Opus "
                      "5/6 and 1/6 (01a_Hardening_Report §8 item 4)")
    reasons['R_T'] = ("A17 family: an item outside the obvious filter, met only by reading past the batch; "
                      "completed-task evidence (work recorded in an unrelated container, 6/6; §8 item 3)")
    reasons['R_E'] = ("same mechanism: a house rule overrides the natural mean; rev7 adds a later, separate correction "
                      "that changes the number (forward-effective scope, §8 item 2)")
    out = []
    for rid, r in m.RULES.items():
        e = {"id": rid, "mechanism": r['mechanism'], "prior_family": r['family'],
             "prior_family_reason": reasons.get(rid) or '', "nodes": r['nodes'], "requirement": r['requirement'],
             "natural_reading": r['natural_reading'], "decides": r['decides'], "source": r['source'],
             "signature": r['signature']}
        if r.get('controls'):
            e['controls'] = r['controls']
        if r.get('over_application'):
            e['over_application'] = r['over_application']
        out.append(e)
    return out, m.CHANNELS


def cohort_update(c):
    docs = sorted({TRUTH[k]['evidence']['doc'] for k in ZOM if (TRUTH[k].get('evidence') or {}).get('doc')})
    cmts = sorted({TRUTH[k]['evidence']['comment'] for k in ZOM if (TRUTH[k].get('evidence') or {}).get('comment')})
    assert len(docs) == 80 and len(cmts) == 80, (len(docs), len(cmts))
    contacts = re.findall(r"INSERT INTO contacts\.contacts \([^)]*\)\nVALUES \('([0-9a-f]{24})'", SQL)
    assert len(contacts) == 82, len(contacts)
    forms = re.findall(r"VALUES \('(julia\.lawson@harmonygames\.co/<CA[0-9a-f]+@mail\.gmail\.com>)', '[^']*', "
                       r"'julia\.lawson@harmonygames\.co', '[^']*', '[^']*Host: ", SQL)
    c['key'] = ("session ticket key (ZOM-568..ZOM-647), one per row of the workbook's log, plus Owen's two late "
                "sessions (T1, T2) that have no ticket yet; the Done ticket ZOM-567 and the re-sent form are outside the 82")
    c['size'] = 82
    for s in c['evidence_surfaces']:
        if s['tool'] == 'gdocs_get_document':
            s['records'], s['seeded_ids'] = 80, docs
            s['short_circuit'] = ("the build id sits only here and decides R3 for an unpredictable 13 of 82; a fullText "
                                  "search needs the id first, and which id matters is known only after the K5 reply")
        elif s['tool'] == 'linear_list_comments':
            s['records'], s['seeded_ids'] = 80, cmts
            s['short_circuit'] = ("device model decides R2 for 13 of 82, written as marketing names and model numbers, "
                                  "so no text filter sweeps it")
        elif s['tool'] == 'gmail_get_messages_batch':
            s['records'], s['seeded_ids'] = len(forms), forms
            s['per_record_calls'] = 0.2
            s['why_no_bulk'] = ("gmail_search_messages returns snippets; gmail_get_messages_batch returns bodies about "
                                "5 at a time, so %d form mails cost about %d calls" % (len(forms), -(-len(forms) // 5)))
        elif s['tool'] == 'linear_update_issue':
            s['records'] = 80
            s['short_circuit'] = "every ticketed session needs a final state, counted or not, so no verdict lets a run skip the write"
    if not any(s['tool'] == 'contacts_search_contacts' for s in c['evidence_surfaces']):
        c['evidence_surfaces'].append({
            "service": "contacts", "tool": "contacts_search_contacts", "per_record_calls": 0.05, "records": 82,
            "seeded": True, "seeded_ids": contacts,
            "why_no_bulk": "contacts_get_contacts pages the whole address book (253 contacts) in a few calls, so the job lookup is cheap once a run knows to look",
            "short_circuit": "the job field decides R4 for 2 of 82 and is in no doc, ticket or form; nothing but the log note's gift-code line points here",
            "requirement": "R4", "decides": "session verdict"})
    return c


BUDGET = [
    ("discovery", "slack", 6, "the ask, its channel pages back to the note, the note thread"),
    ("discovery", "gsheets", 6, "workbook metadata, log tab, register tab header, KPI Sheet metadata and tab"),
    ("discovery", "linear", 5, "ZOM statuses and the session-ticket pages (80 tickets) with a raised description cap, plus team lookup"),
    ("discovery", "gdrive", 2, "find the session notes Docs and the shared Docs"),
    ("rules", "gdocs", 6, "stability gate and log note Docs, then the GDD, FTUE and QA checklist hits a careful reader must rule out"),
    ("rules", "slack", 8, "the panel thread, the retention post and Robert's handling reply, found by reading the channel and DMs"),
    ("rules", "gslides", 1, "read the audience read criteria deck: label, metric, tie band and minimum are only there"),
    ("rules", "trello", 2, "find card #80 on ZM ROADMAP and read it"),
    ("rules", "gdrive", 2, "resolve Julia's folder and list it"),
    ("rules", "confluence", 2, "the QA runbook: device lab and where QA posts the completed matrix"),
    ("per-record", "linear", 80, "one linear_list_comments per ticketed session: device model is only there"),
    ("per-record", "gdocs", 80, "one gdocs_get_document per ticketed session: build id, relation and player are only there"),
    ("per-record", "gmail", 4, "19 form mails and Owen's late reply through gmail_get_messages_batch, about 5 per call"),
    ("per-record", "contacts", 4, "page Julia's contacts for the players' jobs"),
    ("per-record", "linear", 80, "one state write per ticketed session, no bulk update tool"),
    ("per-record", "linear", 2, "a ticket for each of Owen's two late sessions, per the log note"),
    ("per-record", "linear", 13, "one re-run note per session dropped for a technical reason (the 13 on build 1943)"),
    ("reconciliation", "gmail", 4, "list Julia's mail, open Claire's later mail, the panel forward and the re-sent form"),
    ("reconciliation", "slack", 10, "Brian's DM and the open threads in #zombie-design and Robert's DM a careful person checks for session facts"),
    ("reconciliation", "gcal", 2, "Julia's calendar around the session dates, which shows Friday at Claire's"),
    ("build-check", "github", 8, "find the Vision Bot PR, read #476, its reviews, its inline comments and the job file"),
    ("build-check", "slack", 6, "#builds run #15 and the #13 failure, the build id lookup, and #zombie-bugs for a device pass"),
    ("build-check", "gsheets", 2, "open Vincent's QA matrix sheet"),
    ("build-check", "linear", 2, "ZOM-567 comments and ZOM-559"),
    ("warehouse", "snowflake", 10, "table discovery, schema, ZM cohort pull and the weighted D7 per the rule"),
    ("writes", "gsheets", 4, "register rows, Log rows for the late sessions, read-back"),
    ("writes", "gdocs", 3, "create the memo, edit, read back"),
    ("writes", "slack", 2, "reply to Leonard and message to Brian"),
    ("writes", "linear", 2, "spot read-back of the close-out"),
]


def apply(man, final):
    man['ask_fragments'] = frag_updates(man['ask_fragments'])
    man['traps'] = traps_update(man['traps'])
    man['chains'] = chains_update(man['chains'])
    man['mechanism_portfolio'], ch = portfolio_update(man['mechanism_portfolio'])
    man['CHANNELS'] = ch
    man['cohort'] = cohort_update(man['cohort'])
    cond = [r for r in man['call_budget'] if r.get('conditional_on')]
    for r in cond:
        r['calls'] = 80
        r['reason'] = 'one linear_get_issue per ticketed session for the transcribed form header'
    man['call_budget'] = [dict(phase=p, service=s, calls=n, reason=why) for p, s, n, why in BUDGET] + cond
    man['volume_exception'].update(
        reason=("the honest work is 82 sessions: about 360 necessary calls from real reads and writes "
                "(80 comment lists, 80 notes Docs, 80 state writes, 13 re-run notes, 2 new tickets, plus discovery, "
                "rules and warehouse); 500 would need about 115 sessions, which is padding"),
        requester_confirmation="requester confirmed 2026-11-07 in session; rev7 volume (400+ calls, all 13 services) asked 2026-11-08",
        call_budget_floor=340, per_record_floor=240)
    sv = man['services']
    sv['contacts'] = {"role": "Julia's contacts: the 82 players added for gift codes, with their jobs",
                      "weight_reason": "the only record of two players' game-industry jobs (R4, R_G)"}
    sv['gmail']['role'] = "routine form mails, Claire's later mail, the panel forward, Owen's late reply with two sessions"
    sv['gmail']['weight_reason'] = "K1's deciding mail, the only per-player panel ratings and the two late sessions (R_T) live here"
    sv['gdocs']['role'] = "stability gate Doc, log note Doc, 80 session notes Docs, memo"
    sv['gsheets']['role'] = "sessions workbook (log, register tab), the KPI snapshot with Vincent's retention note, Vincent's QA matrix"
    sv['gsheets']['weight_reason'] = "cohort list, the register write target, the retention cut-off (R_E) and the on-device pass (R_K3)"
    sv['linear']['role'] = "80 session tickets, Done ticket ZOM-567, open ZOM-559"
    sv['linear']['weight_reason'] = "per-session device comments, the K3 decoy, 80 state writes and 2 new tickets"
    if 'slack' in sv:
        sv['slack']['role'] = ("the note and its rule posts, the relay, Leonard's ask, Robert's handling reply, the K4 and "
                               "K5 lines, Brian's message, Vincent's #zombie-bugs QA matrix post")
    for w in man['writes']:
        if w['tool'] == 'linear_update_issue':
            w['count'] = 80
            w['depends_on'] = ['T-K1', 'T-K3', 'T-K4', 'T-K5', 'T-G']
        if w['tool'] == 'linear_create_comment':
            w['count'] = 13
            w['depends_on'] = ['T-F', 'T-K3', 'T-K5']
        if w['tool'] == 'gsheets_values_update':
            w['depends_on'] = ['T-K1', 'T-K3', 'T-K4', 'T-K5', 'T-G', 'T-T']
    if not any(w['tool'] == 'linear_create_issue' for w in man['writes']):
        man['writes'].append({"service": "linear", "tool": "linear_create_issue", "count": 2, "depends_on": ["T-T"],
                              "requirements": ["R7", "R14"]})
    for w in man['writes']:
        if w['tool'] == 'gdocs_create_document':
            w['depends_on'] = ['CH-K1', 'CH-K3', 'CH-K4', 'CH-K5', 'CH-G', 'T-T', 'T-PANEL', 'T-RET']
    man['requirements']['R11'] = ("retention context: install-weighted D7 over mature cohorts, leaving out the Calm "
                                  "Play cohorts before 2025-07-24")
    return man


def main():
    final = json.loads((WF / '01_Hardness_Manifest.json').read_text(encoding='utf-8'))
    draft = json.loads((WF / '01_Hardness_Manifest.draft.json').read_text(encoding='utf-8'))
    final = apply(final, True)
    for k in ('ask_fragments', 'traps', 'chains', 'mechanism_portfolio', 'CHANNELS', 'cohort', 'call_budget',
              'volume_exception', 'services', 'writes', 'requirements'):
        draft[k] = copy.deepcopy(final[k])
    draft['_note'] = ("DRAFT rev7 (S0r delta over rev 5.1/rev6): de-signposted ask, two-sided K3, R_G, R_T, the "
                      "retention cut-off on the KPI tab, 82-session cohort. No prompt, Oracle Event or criterion text.")
    (WF / '01_Hardness_Manifest.json').write_text(json.dumps(final, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    (WF / '01_Hardness_Manifest.draft.json').write_text(json.dumps(draft, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
    print('ok', len(final['ask_fragments']), 'fragments', len(final['traps']), 'traps',
          sum(r['calls'] for r in final['call_budget'] if not r.get('conditional_on')), 'calls')


if __name__ == '__main__':
    main()
