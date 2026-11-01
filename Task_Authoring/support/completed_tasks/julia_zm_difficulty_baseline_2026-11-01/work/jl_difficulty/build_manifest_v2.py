"""Draft hardness manifest for the Julia difficulty baseline register (reads truth/minted/planned; writes the draft)."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
WF = '/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/Working_Files/'
T = json.load(open(os.path.join(HERE, 'truth.json')))
M = json.load(open(os.path.join(HERE, 'minted_ids.json')))
P = json.load(open(os.path.join(HERE, 'planned_text.json')))

ASK = f"{M['S_ASK']['channel']}/{M['S_ASK']['ts']}"
SUM = f"{M['S_ROBERT_SUM']['channel']}/{M['S_ROBERT_SUM']['ts']}"
BRIAN = f"{M['S_BRIAN_POST']['channel']}/{M['S_BRIAN_POST']['ts']}"
CARD, CMT, DDCARD = M['T_H1CARD']['id'], M['T_H1CMT']['id'], M['T_DDCARD']['id']
G1 = f"julia.lawson@harmonygames.co/{M['G_BUILD']['gmail_id']}"
G2 = f"julia.lawson@harmonygames.co/{M['G_BUILD_RE']['gmail_id']}"
SHEET, AGENDA, FOLDER = M['SHEET_KNOBS']['id'], M['DOC_AGENDA']['id'], M['FOLDER_ZMDIFF']['id']
EVT = M['GCAL_TUNING']['copies']['julia.lawson@harmonygames.co']
PAGE, PCMT = M['CONF_DDA']['id'], M['CC_ART']['id']
PRC = M['PRC_244']['id']
N = M['LIN_NOTES']
DDSHEET = 'f_34f0950581934de1278969'      # base: Domino Delights "Parameter Optimization" (Leonard; shared with Julia)


def q(key, s):
    text = json.dumps(P[key]) if not isinstance(P[key], str) else P[key]
    assert s in text, (key, s)
    return s


members = [r for r in T['rows'] if r['member']]
counts = T['counts']
REQ = {
    'R1': "register membership: the ZOM tickets created Apr 21 - Aug 31 that changed difficulty - a whole-word title match "
          "on the card's vocabulary, attack power in the title (card comment), or one of Arthur's tickets whose closing note "
          "lists a file under Assets/Scripts/DynamicDifficulty - duplicates out; "
          f"{T['members']} tickets ({T['card_only']} by title, {T['amend']} by attack power, {T['tagged']} by Arthur's notes)",
    'R2': "status per ticket (Live, Editor only, Replaced, Not shipped) judged against the store builds players have "
          "(iOS 0.3.49, Android 0.3.133) under Arthur's store builds mail: level editor, Editor folders and the debug menu "
          "never reach players; flagged code counts only with the flag on (ZOM-303 Not shipped)",
    'R3': "replaced-by per Replaced ticket: ZOM-23 match3d#341, ZOM-254 ZOM-282, ZOM-282 match3d#401, ZOM-209 ZOM-392, "
          "ZOM-257 ZOM-289",
    'R4': "rules in force today: starting tier (first 10 levels avg CPM >= 90 -> tier 1), promotion (>= 80% over the last "
          "12 attempts; tier -2 promotes after one win), demotion (4 losses in a row, no level drop - flag off), enrage on "
          "blunder (speed x1.40, damage x1.30, HP x1.00)",
    'R5': "register saved in the ZM Difficulty folder",
    'R6': f"reply to Leonard in the DM with the counts: {T['members']} tickets, {counts.get('Live')} Live, "
          f"{counts.get('Editor only')} Editor only, {counts.get('Replaced')} Replaced, {counts.get('Not shipped')} Not shipped",
    'R7': "every ticket Done in Linear that players don't have (ZOM-303) moved back to Todo with a comment saying what's "
          "missing; same ticket, no new one",
    'R8': "register shared with everyone on the tuning session invite: Robert as editor; Leonard, Arthur and Brian as commenters",
    'R9': "register is one Google Sheet with two tabs, Tickets and Rules in force",
}

SERVICES = {
    'slack': {'role': "anchor ask in the Leonard-Julia DM (reply destination); Robert's wrong summary and Brian's post-it-here "
                      "request in #zombie-design",
              'weight_reason': "the ask and the reply destination exist only in the DM"},
    'trello': {'role': "H1 difficulty baseline card on ZM ROADMAP + Leonard's amendment comment; Domino Delights decoy card",
               'weight_reason': "cohort rule, status vocabulary, replaced rule, write rules and destination live only on the card"},
    'gmail': {'role': "H2 Arthur's store builds mail and his reply in the same thread",
              'weight_reason': "what reaches players (editor/debug stripped, flags) and the flag state of ZOM-303 exist only there"},
    'linear': {'role': "the 109 candidates; Arthur's and the owners' closing notes; ZOM-42 spec; the ZOM-303 write",
               'weight_reason': "membership by code touched and the per-ticket files/replacement facts exist only in the comments"},
    'github': {'role': "match3d#244 (ZOM-303) with the June flag plan comment; match3d#341 and #401 as replacing PRs",
               'weight_reason': "the replaced-by PRs and the superseded flag plan are only here"},
    'gsheets': {'role': "H3 ZM difficulty knobs sheet (Live, Next pass, History); the register write; DD Parameter "
                        "Optimization decoy (base)",
                'weight_reason': "the enrage and starting-tier numbers in force exist only on the Live tab"},
    'confluence': {'role': "dynamic difficulty page (tier rules, stale enrage numbers) + Arthur's comment (12 attempts)",
                   'weight_reason': "the promotion window in force is only in the page comment"},
    'gcal': {'role': "the Oct 6 tuning session invite (attendees = share list)",
             'weight_reason': "Brian is named as a recipient only by the invite's attendee list"},
    'gdrive': {'role': "ZM Difficulty folder (destination) and the share writes",
               'weight_reason': "destination folder and the four shares"},
    'gdocs': {'role': "the tuning session agenda (register layout)",
              'weight_reason': "the sheet format and tab names are stated only in the agenda"},
}

ANCHORS = [{'id': 'A1', 'prompt_reference': "Leonard's difficulty baseline ask", 'service': 'slack', 'locator': ASK,
            'requirement_ids': ['R6']}]

F = []


def frag(**k):
    k.setdefault('base_pointers', [])
    F.append(k)


frag(id='K1', service='slack', container=M['S_ASK']['channel'], locator=ASK, kind='delegation', incorporated_via=['A1'],
     seeded_ids=[M['S_ASK']['id']], delegated_by_record=ASK,
     delegation_quote=q('S_ASK', "reply here with the counts when it's in the folder"), requirement_ids=['R6'],
     names_authorities=[{'id': 'H1', 'quote': q('S_ASK', 'the rules for the register are on the difficulty baseline card on the zm roadmap board')}])
frag(id='K2', service='trello', container=CARD, locator=f'trello:{CARD} desc', kind='requirement', incorporated_via=['A1'],
     seeded_ids=[CARD, M['T_H1CREATE']['id']], delegated_by_record=ASK,
     delegation_quote=q('S_ASK', 'the rules for the register are on the difficulty baseline card on the zm roadmap board'),
     requirement_ids=['R1', 'R2', 'R3', 'R7'],
     names_authorities=[{'id': 'H2', 'quote': q('H1_DESC', "Arthur's store builds mail")},
                        {'id': 'H3', 'quote': q('H1_DESC', "Arthur's difficulty knobs sheet")}])
frag(id='K3', service='trello', container=CARD, locator=f'trello:{CMT} (commentCard on {CARD})', kind='amendment',
     incorporated_via=['A1', 'K2'], seeded_ids=[CMT], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', 'Julia owns this one.'), requirement_ids=['R1'],
     supersedes='K2 rule 1 (vocabulary): attack power in the title counts too', resolver='newer comment by the card author; rest stands')
frag(id='K4', service='gmail', container=M['G_BUILD']['gmail_id'], locator=G1, kind='requirement', incorporated_via=['A1', 'K2'],
     seeded_ids=[G1], delegated_by_record=CARD, delegation_quote=q('H1_DESC', "Arthur's store builds mail"), requirement_ids=['R2'])
frag(id='K5', service='gmail', container=M['G_BUILD']['gmail_id'], locator=G2, kind='amendment', incorporated_via=['A1', 'K2'],
     seeded_ids=[G2], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', "What is in the store builds and what counts as shipped: Arthur's store builds mail."),
     requirement_ids=['R2', 'R7'], supersedes='match3d#244 June flag plan; Robert summary', resolver='newer reply in the same thread')
frag(id='K6', service='gsheets', container=SHEET, locator=f'gsheets:{SHEET} tab Live', kind='requirement',
     incorporated_via=['A1', 'K2'], seeded_ids=[SHEET], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', "The numbers designers tune are on Arthur's difficulty knobs sheet"), requirement_ids=['R4'])
frag(id='K7', service='confluence', container=PAGE, locator=f'confluence:{PAGE}', kind='requirement', incorporated_via=['A1', 'K2'],
     seeded_ids=[PAGE], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', 'the tier rules are written up on the dynamic difficulty page in Confluence'), requirement_ids=['R4'])
frag(id='K8', service='confluence', container=PAGE, locator=f'confluence:{PCMT}', kind='amendment', incorporated_via=['A1', 'K2'],
     seeded_ids=[PCMT], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', 'the tier rules are written up on the dynamic difficulty page in Confluence'), requirement_ids=['R4'],
     supersedes='K7 promotion window (10 -> 12 attempts)', resolver='newer comment on the page by Arthur')
frag(id='K9', service='gcal', container=M['GCAL_TUNING']['ical_uid'], locator=f'gcal:{EVT}', kind='recipient',
     incorporated_via=['A1', 'K2'], seeded_ids=[EVT], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', 'Share it with everyone on the tuning session invite: Robert can edit, everyone else comments.'),
     requirement_ids=['R8'])
frag(id='K10', service='gdrive', container=FOLDER, locator=f'gdrive:{FOLDER}', kind='destination', incorporated_via=['A1', 'K2'],
     seeded_ids=[FOLDER], delegated_by_record=CARD, delegation_quote=q('H1_DESC', 'The register goes in the ZM Difficulty folder.'),
     requirement_ids=['R5'])
frag(id='K11', service='gdocs', container=AGENDA, locator=f'gdocs:{AGENDA}', kind='format', incorporated_via=['A1', 'K2'],
     seeded_ids=[AGENDA], delegated_by_record=CARD, delegation_quote=q('H1_DESC', 'Layout as in the session agenda.'),
     requirement_ids=['R9'])
frag(id='K12', service='linear', container='ZOM-42', locator='linear:ZOM-42 description', kind='requirement',
     incorporated_via=['A1', 'K2', 'K7'], seeded_ids=[], base_pointers=['ZOM-42'], delegated_by_record=PAGE,
     delegation_quote=q('CONF_DDA_BODY', '(ZOM-42)'), requirement_ids=['R4'])
frag(id='K13', service='linear', container='ZOM-392', locator=f"linear:{N['ZOM-392']['id']} (comment on ZOM-392)", kind='requirement',
     incorporated_via=['A1', 'K2'], seeded_ids=[N['ZOM-392']['id']], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', "Arthur's closing note on each of his tickets lists the files."), requirement_ids=['R1', 'R3'])

AUTH = [
    {'id': 'H1', 'name': 'the difficulty baseline rules (card)', 'home_service': 'trello', 'decoy_service': 'trello',
     'governs': ['R1', 'R3', 'R5', 'R7'], 'findable_query': 'difficulty baseline', 'seeded_ids': [CARD, CMT],
     'base_pointers': [], 'decoy_seeded_ids': [DDCARD], 'decoy_base_pointers': [],
     'decoy_scope': {'dimension': 'game', 'decoy': 'Domino Delights April difficulty pass (DD Product Roadmap board)',
                     'task': 'Zombie Match 3D (ZM ROADMAP board)'}},
    {'id': 'H2', 'name': "Arthur's store builds mail", 'home_service': 'gmail', 'decoy_service': 'slack',
     'governs': ['R2'], 'findable_query': 'store builds', 'seeded_ids': [G1, G2], 'base_pointers': [],
     'decoy_seeded_ids': [M['S_ROBERT_SUM']['id']], 'decoy_base_pointers': []},
    {'id': 'H3', 'name': "Arthur's difficulty knobs sheet", 'home_service': 'gsheets', 'decoy_service': 'gsheets',
     'governs': ['R4'], 'findable_query': 'difficulty knobs', 'seeded_ids': [SHEET], 'base_pointers': [],
     'decoy_seeded_ids': [], 'decoy_base_pointers': [f'gsheets:{DDSHEET}'],
     'decoy_scope': {'dimension': 'game', 'decoy': 'Domino Delights (Parameter Optimization, Leonard)',
                     'task': 'Zombie Match 3D (ZM difficulty knobs, Arthur)'}},
]

notes_all = [v['id'] for v in N.values()]
decisive = [v['id'] for v in N.values() if v.get('decisive')]
COHORT = {
    'definition_source': 'H1',
    'key': 'ZOM ticket created 2025-04-21..2025-08-31 (not Duplicate) matching the card vocabulary or attack power in the '
           'title, or assigned to Arthur (membership then by the files in his closing note)',
    'size': T['candidates'],
    'evidence_surfaces': [
        {'service': 'linear', 'tool': 'linear_list_comments', 'per_record_calls': 1, 'records': T['candidates'], 'seeded': True,
         'seeded_ids': notes_all,
         'why_no_bulk': "linear_list_issues returns titles, states, assignees and descriptions but no comments; the base has "
                        "no Linear comments; which of Arthur's tickets touched Assets/Scripts/DynamicDifficulty and which files "
                        "each ticket changed are only in the closing notes",
         'short_circuit': "membership of Arthur's 94 tickets is decided only by the note (9 join by path, not title); for the "
                          "title members the note's file list decides Editor only vs Live (ZOM-45 runtime, ZOM-277 editor) "
                          "and three notes carry the replacement (ZOM-23, ZOM-289, ZOM-392); neutral notes sit on the other 85 "
                          "Arthur tickets, so having a note reveals nothing and no search over issue fields returns them",
         'requirement': 'R1', 'decides': 'register membership'},
        {'service': 'linear', 'tool': 'linear_list_comments', 'per_record_calls': 0.37, 'records': T['members'], 'seeded': True,
         'seeded_ids': decisive,
         'why_no_bulk': "the file list in each member's note is the only per-ticket evidence of where the change lives",
         'short_circuit': "title words suggest gameplay for ZOM-277 and editor for ZOM-45; only the files decide, so the read "
                          "cannot be skipped once the title has matched",
         'requirement': 'R2', 'decides': 'status per ticket'},
        {'service': 'github', 'tool': 'github_get_pull_request+github_get_pull_request_comments', 'per_record_calls': 0.15,
         'records': T['members'], 'seeded': True, 'seeded_ids': [PRC],
         'why_no_bulk': "PR search returns titles and merge state, not the conversation; #244's flag comment and what #401/#341 "
                        "changed are per-PR reads",
         'short_circuit': "the replaced-by column for ZOM-282 and ZOM-23 names a PR the ticket never mentions in Linear fields; "
                          "the #244 comment is the version the mail reply overturns",
         'requirement': 'R3', 'decides': 'replaced-by per Replaced ticket'},
    ],
}

CHAINS = [
    {'id': 'C1', 'root_cause': 'A1', 'ends_in': 'R2',
     'hops': [{'service': 'slack', 'record': SUM, 'finding': "Robert: everything from June is in the store builds incl. the level drop"},
              {'service': 'github', 'record': PRC, 'finding': "June plan: flag goes on with the next store build"},
              {'service': 'gmail', 'record': G2, 'finding': "Arthur's reply: dda_level_demotion still off for everyone -> ZOM-303 Not shipped"}]},
    {'id': 'C2', 'root_cause': 'A12', 'ends_in': 'R1',
     'hops': [{'service': 'slack', 'record': ASK, 'finding': "rules are on the difficulty baseline card"},
              {'service': 'trello', 'record': CARD, 'finding': "vocabulary, window, Arthur's tier-code tickets"},
              {'service': 'trello', 'record': CMT, 'finding': "attack power counts too (+5)"},
              {'service': 'linear', 'record': N['ZOM-24']['id'], 'finding': "ZOM-24 note: DynamicDifficulty/Editor path -> member"}]},
    {'id': 'C3', 'root_cause': 'A15', 'ends_in': 'R2',
     'hops': [{'service': 'trello', 'record': CARD, 'finding': "status judged against the store builds"},
              {'service': 'gmail', 'record': G1, 'finding': "level editor, Editor folders, debug menu stripped"},
              {'service': 'linear', 'record': N['ZOM-277']['id'], 'finding': "ZOM-277 only LevelStatsPanel.cs -> Editor only though Done"}]},
    {'id': 'C4', 'root_cause': 'A13', 'ends_in': 'R8',
     'hops': [{'service': 'trello', 'record': CARD, 'finding': "share with everyone on the tuning session invite"},
              {'service': 'gcal', 'record': EVT, 'finding': "attendees Leonard, Robert, Arthur, Brian"},
              {'service': 'gdrive', 'record': FOLDER, 'finding': "Robert editor, the other three commenters"}]},
    {'id': 'C5', 'root_cause': 'A4', 'ends_in': 'R4',
     'hops': [{'service': 'linear', 'record': 'ZOM-254', 'finding': "+25% speed, damage, max HP"},
              {'service': 'linear', 'record': 'ZOM-282', 'finding': "+50% speed and damage only"},
              {'service': 'github', 'record': 'harmonygames-Games/match3d#401', 'finding': "separate knobs, health boosts removed"},
              {'service': 'gsheets', 'record': SHEET, 'finding': "Live tab: speed 1.40, damage 1.30, hp 1.00 (not Next pass)"}]},
    {'id': 'C6', 'root_cause': 'A14', 'ends_in': 'R4',
     'hops': [{'service': 'linear', 'record': 'ZOM-42', 'finding': "promotion over the last 10 attempts"},
              {'service': 'confluence', 'record': PAGE, 'finding': "page restates last 10"},
              {'service': 'confluence', 'record': PCMT, 'finding': "comment: last 12 attempts now"}]},
    {'id': 'C7', 'root_cause': 'A17', 'ends_in': 'R1',
     'hops': [{'service': 'trello', 'record': CARD, 'finding': "Apr 21 - Aug 31, whole words, duplicates out"},
              {'service': 'linear', 'record': 'ZOM-517', 'finding': "enrage title, created Sep 3 -> out"},
              {'service': 'linear', 'record': 'ZOM-271', 'finding': "ATK POWER is not 'attack power' -> out"}]},
    {'id': 'C8', 'root_cause': 'A8', 'ends_in': 'R7',
     'hops': [{'service': 'gmail', 'record': G2, 'finding': "ZOM-303 level drop never reached players"},
              {'service': 'trello', 'record': CARD, 'finding': "same ticket back to Todo, no new ones"},
              {'service': 'linear', 'record': 'ZOM-293', 'finding': "lookalike 'Tiering Down Issue' (Todo) is not the ticket"}]},
]

Tr = []


def trap(**k):
    k.setdefault('base_pointers', [])
    k.setdefault('seeded_ids', [])
    Tr.append(k)


trap(id='T1', family='superseding', services=['trello'], seeded_ids=[CARD, CMT], requirement='R1',
     expected_wrong_reading='26 tickets by the card words; misses ZOM-246, 250, 263, 277, 315',
     resolver='the card comment (attack power counts too); rest stands',
     discovery_order='the card description is read first; the comment sits in the activity feed',
     version_records=[{'service': 'trello', 'id': M['T_H1CREATE']['id'], 'seeded': True, 'at': M['T_H1CREATE']['at']},
                      {'service': 'trello', 'id': CMT, 'seeded': True, 'at': M['T_H1CMT']['at']}])
trap(id='T2', family='exact_predicate', services=['linear'], base_pointers=['ZOM-517', 'ZOM-576', 'ZOM-593', 'ZOM-622'],
     requirement='R1', expected_wrong_reading='includes ZOM-517 (enrage, created Sep 3) or the October tiering tickets',
     resolver='card rule 1 window Apr 21 - Aug 31', discovery_order='a title search for enrage/tier returns them first')
trap(id='T3', family='distractor', distractor_type='keyword_collision', services=['linear'], base_pointers=['ZOM-271'],
     requirement='R1', expected_wrong_reading="adds ZOM-271 ('ATK POWER BU...') as an attack power ticket",
     resolver="the comment says attack power in the title; ATK POWER is not the phrase", discovery_order='a search for "attack" returns it')
trap(id='T4', family='distractor', distractor_type='near_duplicate_record', services=['linear'], base_pointers=['ZOM-203', 'ZOM-276'],
     requirement='R1', expected_wrong_reading='lists the two Duplicate tickets', resolver='card rule 1: duplicates are out')
trap(id='T5', family='scope_alias', services=['linear', 'gmail'], seeded_ids=[N['ZOM-45']['id'], N['ZOM-277']['id'], G1],
     requirement='R2', expected_wrong_reading='ZOM-45 Editor only (title says editor); ZOM-277 Live (title says items in level)',
     resolver="files in the notes against the mail's stripped folders", discovery_order='titles are read before notes')
trap(id='T6', family='superseding', services=['github', 'slack', 'gmail'], seeded_ids=[PRC, M['S_ROBERT_SUM']['id'], G2],
     requirement='R2', expected_wrong_reading='ZOM-303 Live (flag planned for the next store build; Robert says the level drop is in)',
     resolver="Arthur's reply in the store builds thread: flag still off for everyone",
     discovery_order='the first mail looks complete; the reply sits under it',
     version_records=[{'service': 'github', 'id': PRC, 'seeded': True, 'at': M['PRC_244']['at']},
                      {'service': 'slack', 'id': M['S_ROBERT_SUM']['id'], 'seeded': True, 'at': M['S_ROBERT_SUM']['at']},
                      {'service': 'gmail', 'id': G2, 'seeded': True, 'at': M['G_BUILD_RE']['at']}])
trap(id='T7', family='stale_summary', distractor_type='stale_summary', services=['slack'], seeded_ids=[M['S_ROBERT_SUM']['id']],
     requirement='R4', expected_wrong_reading='enrage +50% speed and damage (Robert)', resolver='knobs sheet Live tab 1.40 / 1.30',
     discovery_order='#zombie-design is the first channel a difficulty search hits')
trap(id='T8', family='superseding', services=['linear', 'gsheets'], base_pointers=['ZOM-254', 'ZOM-282'], seeded_ids=[SHEET],
     requirement='R4', expected_wrong_reading='enrage +25% (ZOM-254) or +50% (ZOM-282)', resolver='Live tab (Aug 26, match3d#401)',
     version_records=[{'service': 'linear', 'base_pointer': 'ZOM-254', 'seeded': False, 'at': '2025-06-12T00:00:00Z'},
                      {'service': 'linear', 'base_pointer': 'ZOM-282', 'seeded': False, 'at': '2025-06-19T00:00:00Z'},
                      {'service': 'gsheets', 'id': SHEET, 'seeded': True, 'at': M['SHEET_KNOBS']['at']}])
trap(id='T9', family='distractor', distractor_type='scope_adjacent', services=['gsheets'], seeded_ids=[SHEET], requirement='R4',
     expected_wrong_reading="copies the Next pass tab (Robert's proposals, 85 CPM)", resolver='card rule 5: as they work today -> Live tab')
trap(id='T10', family='superseding', services=['linear', 'confluence'], base_pointers=['ZOM-42'], seeded_ids=[PAGE, PCMT],
     requirement='R4', expected_wrong_reading='promotion over the last 10 attempts', resolver="Arthur's page comment: 12",
     discovery_order='the page body is read; comments are a separate call',
     version_records=[{'service': 'linear', 'base_pointer': 'ZOM-42', 'seeded': False, 'at': '2025-04-21T00:00:00Z'},
                      {'service': 'confluence', 'id': PAGE, 'seeded': True, 'at': M['CONF_DDA']['at']},
                      {'service': 'confluence', 'id': PCMT, 'seeded': True, 'at': M['CC_ART']['at']}])
trap(id='T11', family='superseding', services=['confluence', 'gsheets'], seeded_ids=[PAGE, SHEET], requirement='R4',
     expected_wrong_reading='enrage +25% speed, damage and max HP from the page', resolver='knobs sheet Live tab',
     version_records=[{'service': 'confluence', 'id': PAGE, 'seeded': True, 'at': M['CONF_DDA']['at']},
                      {'service': 'gsheets', 'id': SHEET, 'seeded': True, 'at': M['SHEET_KNOBS']['at']}])
trap(id='T12', family='distractor', distractor_type='lookalike_entity', services=['trello'], seeded_ids=[DDCARD], requirement='R8',
     expected_wrong_reading='shares with Brian and Vincent / saves in the Difficulty Optimization sheet (DD card)',
     resolver='the ZM ROADMAP card named in the ask', discovery_order='a Trello search for "difficulty baseline" returns both')
trap(id='T13', family='cross_reference_gap', services=['gcal', 'gdrive'], seeded_ids=[EVT], requirement='R8',
     expected_wrong_reading='shares with Robert and Arthur only (people named on the card)', resolver='invite attendees include Brian and Leonard')
trap(id='T14', family='reuse_exclusion', services=['linear'], base_pointers=['ZOM-293'], seeded_ids=[G2], requirement='R7',
     expected_wrong_reading='creates a new ticket for the level drop or comments on ZOM-293', resolver='card rule 6: same ticket (ZOM-303)')
trap(id='T15', family='eliminating_evidence', services=['linear', 'github'], seeded_ids=[N['ZOM-23']['id'], N['ZOM-289']['id'], N['ZOM-392']['id']],
     requirement='R3', expected_wrong_reading='ZOM-23, ZOM-209 and ZOM-257 Live (Done, no Linear field says otherwise)',
     resolver='the notes name match3d#341, ZOM-392 and ZOM-289')
trap(id='T16', family='distractor', distractor_type='non_authoritative_instruction', services=['slack'], seeded_ids=[M['S_BRIAN_POST']['id']],
     requirement='R6', expected_wrong_reading='posts the counts in #zombie-design instead of the DM', resolver="Leonard's ask: reply here")
trap(id='T17', family='distractor', distractor_type='scope_adjacent', services=['gsheets'], base_pointers=[f'gsheets:{DDSHEET}'],
     requirement='R4', expected_wrong_reading="takes Domino Delights parameters for the rules tab", resolver='H3 is the ZM sheet by Arthur')
trap(id='T18', family='exact_predicate', services=['linear'], base_pointers=['ZOM-279', 'ZOM-284', 'ZOM-285', 'ZOM-286'],
     requirement='R1', expected_wrong_reading='adds the cancelled dynamic insertion tickets as tier-code tickets',
     resolver='their notes: nothing merged; touched means files changed')
trap(id='T19', family='superseding', services=['slack', 'gmail'], base_pointers=['C08R27X0EAH/1758081917.318539'], seeded_ids=[G1],
     requirement='R2', expected_wrong_reading='judges against iOS 0.3.38 (submitted Sep 17)', resolver="the mail: iOS 0.3.49 / Android 0.3.133",
     version_records=[{'service': 'slack', 'base_pointer': 'C08R27X0EAH/1758081917.318539', 'seeded': False, 'at': '2025-09-17T04:05:17Z'},
                      {'service': 'gmail', 'id': G1, 'seeded': True, 'at': M['G_BUILD']['at']}])

BUDGET = [
    {'phase': 'discovery', 'service': 'slack', 'calls': 2, 'reason': "read the ask in the Leonard-Julia DM; resolve Leonard's user / DM id"},
    {'phase': 'discovery', 'service': 'trello', 'calls': 3, 'reason': 'search the board for the difficulty baseline card, read it, read its comments (amendment)'},
    {'phase': 'discovery', 'service': 'gmail', 'calls': 2, 'reason': "search for Arthur's store builds mail, open the thread (the reply with the flag state)"},
    {'phase': 'discovery', 'service': 'gsheets', 'calls': 3, 'reason': 'find the knobs sheet, read the Live tab and the History tab (where #401 split the knobs)'},
    {'phase': 'discovery', 'service': 'confluence', 'calls': 3, 'reason': 'search the dynamic difficulty page, read it, list its comments (12 attempts)'},
    {'phase': 'discovery', 'service': 'gcal', 'calls': 2, 'reason': 'find the Oct 6 tuning session and read its attendees (share list)'},
    {'phase': 'discovery', 'service': 'gdocs', 'calls': 2, 'reason': 'find and read the session agenda (sheet with two tabs)'},
    {'phase': 'discovery', 'service': 'gdrive', 'calls': 1, 'reason': 'find the ZM Difficulty folder id (destination)'},
    {'phase': 'enumeration', 'service': 'linear', 'calls': 5, 'reason': 'page through ZOM issues created Apr 21 - Aug 31 (~470) to apply the title words and pick out Arthur\'s'},
    {'phase': 'rules', 'service': 'linear', 'calls': 1, 'reason': 'read ZOM-42 in full (4,244-char spec: promotion, demotion, tier -2) - the list truncates descriptions'},
    {'phase': 'rules', 'service': 'linear', 'calls': 4, 'reason': 'read ZOM-199, ZOM-254, ZOM-282, ZOM-303 in full for the rules tab', 'conditional_on': 'list_issues truncates these shorter descriptions'},
    {'phase': 'per-record', 'service': 'linear', 'calls': T['candidates'], 'reason': "one linear_list_comments per candidate: Arthur's closing note decides membership (tier-code files) and status (editor vs runtime files, replacements); no bulk comment call"},
    {'phase': 'per-record', 'service': 'github', 'calls': 3, 'reason': 'read match3d#244 conversation (June flag plan), #401 and #341 (what replaced ZOM-282 and ZOM-23)'},
    {'phase': 'reads-before-writes', 'service': 'linear', 'calls': 1, 'reason': 'list ZOM workflow states to move ZOM-303 back to Todo'},
    {'phase': 'writes', 'service': 'gsheets', 'calls': 3, 'reason': 'create the register with Tickets and Rules in force tabs; write 40 rows and the rules rows'},
    {'phase': 'writes', 'service': 'gdrive', 'calls': 5, 'reason': 'move the sheet into ZM Difficulty; share with Robert (edit), Leonard, Arthur, Brian (comment)'},
    {'phase': 'writes', 'service': 'slack', 'calls': 1, 'reason': 'reply to Leonard in the DM with the counts'},
    {'phase': 'writes', 'service': 'linear', 'calls': 2, 'reason': 'ZOM-303 back to Todo + comment saying the level drop is behind a flag that is off'},
    {'phase': 'read-back', 'service': 'gsheets', 'calls': 1, 'reason': 'read the register back to check the 40 rows and counts'},
]

WRITES = [
    {'service': 'gsheets', 'tool': 'gsheets_create_spreadsheet+gsheets_values_update', 'count': 3,
     'depends_on': ['K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K11', 'K12', 'K13', 'C1', 'C2', 'C3', 'C5', 'C6', 'C7', 'T1', 'T5', 'T6', 'T8', 'T10', 'T15'],
     'requirements': ['R1', 'R2', 'R3', 'R4', 'R9']},
    {'service': 'gdrive', 'tool': 'gdrive_move_file+gdrive_share_file', 'count': 5, 'depends_on': ['K9', 'K10', 'C4', 'T12', 'T13'],
     'requirements': ['R5', 'R8']},
    {'service': 'slack', 'tool': 'slack_send_message', 'count': 1, 'depends_on': ['K1', 'C2', 'C3', 'T16'], 'requirements': ['R6']},
    {'service': 'linear', 'tool': 'linear_update_issue+linear_create_comment', 'count': 2, 'depends_on': ['K5', 'C1', 'C8', 'T14'],
     'requirements': ['R7']},
]

MAN = {
    'persona': 'julia_lawson',
    'horizon': 'Long Horizon',
    'effective_profile': 'long',
    'profile_exception': {
        'reason': "author target: at least 120 tool calls in every baseline run and an average weighted pass rate under 75% "
                  "(00_Assigments.md 'Author targets'); the extreme profile's ~600-call design would overshoot it, so the long "
                  "profile keeps the extreme breadth, authorities, chains and traps with a ~150-call necessary budget",
        'requester_confirmation': "task author in chat on 2026-10-30: 'make sure my task is a long horizon task so i want minimum "
                                  "120 tool calls in each runs and also make sure i want difficulty under 75%'; recorded in "
                                  "task_inputs/00_Assigments.md ('Author targets for this task')"},
    'requirements': REQ,
    'services': SERVICES,
    'anchors': ANCHORS,
    'ask_fragments': F,
    'authorities': AUTH,
    'cohort': COHORT,
    'chains': CHAINS,
    'traps': Tr,
    'call_budget': BUDGET,
    'writes': WRITES,
    'hazard_acknowledgements': [
        {'hazard_id': 'L03', 'resolution': 'dated_claim',
         'why_safe': "ZOM-292 (Todo, match3d#267 merged) is a candidate only; the SQL does not modify it. Arthur's seeded note "
                     "(before its updated_at) says it stays open as the umbrella for the rest of the Level Editor 2.0 list and "
                     "that copy monsters went in with #267 - a dated human claim that explains the state; it is not a member "
                     "(LevelEditor files only)", 'requirement': 'R1'}],
    'denied_probes': [],
}
json.dump(MAN, open(WF + '01_Hardness_Manifest.draft.json', 'w'), indent=1)
print('fragments', len(F), 'traps', len(Tr), 'chains', len(CHAINS),
      'budget', sum(b['calls'] for b in BUDGET if 'conditional_on' not in b), '(+cond', sum(b['calls'] for b in BUDGET if 'conditional_on' in b), ')')
