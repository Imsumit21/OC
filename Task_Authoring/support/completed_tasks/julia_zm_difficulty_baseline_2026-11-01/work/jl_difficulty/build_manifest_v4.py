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
          "starts with 'tiers:' - duplicates out, open/cancelled ones in; "
          f"{T['members']} tickets ({T['card_only']} by title, {T['amend']} by attack power, {T['tagged']} by Arthur's notes)",
    'R2': "status per ticket (Live, Editor only, Replaced, Not shipped) judged against the store builds players have "
          "(iOS 0.3.49, Android 0.3.133) under Blake's store builds mail: level editor / LevelDesigner and debug tooling "
          "never reach players (ZOM-45 and ZOM-303 Live, ZOM-277 Editor only)",
    'R3': "replaced-by per Replaced ticket: ZOM-254 by ZOM-282",
    'R4': "rules in force today: starting tier (first 10 levels avg CPM > 90 -> tier 1, 90 or less tier 0); promotion (win "
          "rate >= 80% over up to the last 10 attempts; tier -2 promotes after one win); demotion (4 losses in a row, or "
          "win rate <= 50% over up to the last 10; the record resets after every move); after a demotion the current level "
          "loads one tier down; enrage on blunder adds speed and damage per monster (Live tab of the monster enrage sheet; "
          "MonsterBase 0.8/0.8 for the rest), no HP boost",
    'R5': "register saved in the ZM Difficulty folder",
    'R6': f"reply to Leonard in the DM with the counts: {T['members']} tickets, {counts.get('Live')} Live, "
          f"{counts.get('Editor only')} Editor only, {counts.get('Replaced')} Replaced, {counts.get('Not shipped')} Not shipped",
    'R7': "comment on ZOM-199 that the build checks CPM > 90 (not >= 90) and on ZOM-254 naming ZOM-282 as its "
          "replacement; same tickets, no new ones",
    'R8': "register shared with everyone on the tuning session invite: Robert as editor; Leonard, Arthur and Brian as commenters",
    'R9': "register is one Google Sheet with two tabs, Tickets and Rules in force",
}

SERVICES = {
    'slack': {'role': "anchor ask in the Leonard-Julia DM (reply destination); Robert's wrong summary and Brian's post-it-here "
                      "request in #zombie-design",
              'weight_reason': "the ask and the reply destination exist only in the DM"},
    'trello': {'role': "H1 difficulty baseline card on ZM ROADMAP + Leonard's amendment comment; Domino Delights decoy card",
               'weight_reason': "cohort rule, status vocabulary, replaced rule, write rules and destination live only on the card"},
    'gmail': {'role': "H2 Blake's store builds mail and his reply in the same thread",
              'weight_reason': "what reaches players (editor/debug tooling stripped) and the > 90 starting-tier check exist only there"},
    'linear': {'role': "the 109 candidates; Arthur's and the owners' closing notes; ZOM-42 spec; the ZOM-303 write",
               'weight_reason': "membership by code touched and the per-ticket files/replacement facts exist only in the comments"},
    'github': {'role': "match3d#401 (+ Blake's seeded comment); #243 / #265 file tables vs notes",
               'weight_reason': "what #401 changed (speed/damage split, hp boost gone) and the shared-PR file tables live here"},
    'gsheets': {'role': "H3 ZM monster enrage sheet (Julia's; Live, Next pass, History); the register write; DD Parameter "
                        "Optimization decoy (base)",
                'weight_reason': "the per-monster enrage numbers in force exist only on the Live tab"},
    'confluence': {'role': "dynamic difficulty page (tier rules without the 50% demotion rule, stale enrage) + Blake's comment",
                   'weight_reason': "the page is the named tier-rules source; its comment retires the +25% enrage text"},
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
     delegation_quote=q('S_ASK', "reply here when it's in the folder with how many tickets made the list and how many"), requirement_ids=['R6'],
     names_authorities=[{'id': 'H1', 'quote': q('S_ASK', 'the rules for the register are on the difficulty baseline card on the zm roadmap board')}])
frag(id='K2', service='trello', container=CARD, locator=f'trello:{CARD} desc', kind='requirement', incorporated_via=['A1'],
     seeded_ids=[CARD, M['T_H1CREATE']['id']], delegated_by_record=ASK,
     delegation_quote=q('S_ASK', 'the rules for the register are on the difficulty baseline card on the zm roadmap board'),
     requirement_ids=['R1', 'R2', 'R3', 'R7'],
     names_authorities=[{'id': 'H2', 'quote': q('H1_DESC', "Blake's store builds mail")},
                        {'id': 'H3', 'quote': q('H1_DESC', "your monster enrage sheet has the numbers")}])
frag(id='K3', service='trello', container=CARD, locator=f'trello:{CMT} (commentCard on {CARD})', kind='amendment',
     incorporated_via=['A1', 'K2'], seeded_ids=[CMT], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', 'Julia owns this one.'), requirement_ids=['R1'],
     supersedes='K2 rule 1 (vocabulary): attack power in the title counts too', resolver='newer comment by the card author; rest stands')
frag(id='K4', service='gmail', container=M['G_BUILD']['gmail_id'], locator=G1, kind='requirement', incorporated_via=['A1', 'K2'],
     seeded_ids=[G1], delegated_by_record=CARD, delegation_quote=q('H1_DESC', "Blake's store builds mail"), requirement_ids=['R2'])
frag(id='K5', service='gmail', container=M['G_BUILD']['gmail_id'], locator=G2, kind='amendment', incorporated_via=['A1', 'K2'],
     seeded_ids=[G2], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', "What is in the store builds and what counts as shipped: Blake's store builds mail."),
     requirement_ids=['R4', 'R7'], supersedes="ZOM-199's '>= 90' and the page's '90 or more'", resolver='newer reply in the same thread')
frag(id='K6', service='gsheets', container=SHEET, locator=f'gsheets:{SHEET} tab Live', kind='requirement',
     incorporated_via=['A1', 'K2'], seeded_ids=[SHEET], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', "Enrage is per monster: your monster enrage sheet has the numbers."), requirement_ids=['R4'])
frag(id='K7', service='confluence', container=PAGE, locator=f'confluence:{PAGE}', kind='requirement', incorporated_via=['A1', 'K2'],
     seeded_ids=[PAGE], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', 'The tier rules are written up on the dynamic difficulty page in Confluence'), requirement_ids=['R4'])
frag(id='K8', service='confluence', container=PAGE, locator=f'confluence:{PCMT}', kind='amendment', incorporated_via=['A1', 'K2'],
     seeded_ids=[PCMT], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', 'The tier rules are written up on the dynamic difficulty page in Confluence'), requirement_ids=['R4'],
     supersedes='K7 blunder line (+25% speed, damage, HP)', resolver='newer comment on the page by Blake')
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
     incorporated_via=['A1', 'K2'], seeded_ids=[], base_pointers=['ZOM-42'], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', 'in ZOM-42 itself'), requirement_ids=['R4'])
frag(id='K13', service='linear', container='ZOM-305', locator=f"linear:{N['ZOM-305']['id']} (comment on ZOM-305)", kind='requirement',
     incorporated_via=['A1', 'K2'], seeded_ids=[N['ZOM-305']['id']], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', 'his closing note on those starts with \"tiers:\"'), requirement_ids=['R1'])

AUTH = [
    {'id': 'H1', 'name': 'the difficulty baseline rules (card)', 'home_service': 'trello', 'decoy_service': 'trello',
     'governs': ['R1', 'R3', 'R5', 'R7'], 'findable_query': 'difficulty baseline', 'seeded_ids': [CARD, CMT],
     'base_pointers': [], 'decoy_seeded_ids': [DDCARD], 'decoy_base_pointers': [],
     'decoy_scope': {'dimension': 'game', 'decoy': 'Domino Delights April difficulty pass (DD Product Roadmap board)',
                     'task': 'Zombie Match 3D (ZM ROADMAP board)'}},
    {'id': 'H2', 'name': "Blake's store builds mail", 'home_service': 'gmail', 'decoy_service': 'slack',
     'governs': ['R2'], 'findable_query': 'store builds', 'seeded_ids': [G1, G2], 'base_pointers': [],
     'decoy_seeded_ids': [M['S_ROBERT_SUM']['id']], 'decoy_base_pointers': []},
    {'id': 'H3', 'name': "the monster enrage sheet", 'home_service': 'gsheets', 'decoy_service': 'gsheets',
     'governs': ['R4'], 'findable_query': 'monster enrage', 'seeded_ids': [SHEET], 'base_pointers': [],
     'decoy_seeded_ids': [], 'decoy_base_pointers': [f'gsheets:{DDSHEET}'],
     'decoy_scope': {'dimension': 'game', 'decoy': 'Domino Delights (Parameter Optimization, Leonard)',
                     'task': 'Zombie Match 3D (ZM monster enrage, Julia)'}},
]

notes_all = [v['id'] for v in N.values()]
decisive = [v['id'] for v in N.values() if v.get('decisive')]
COHORT = {
    'definition_source': 'H1',
    'key': "ZOM ticket created 2025-04-21..2025-08-31 (not Duplicate) matching the card vocabulary or attack power in the "
           "title, or assigned to Blake (Arthur; membership then by the 'tiers:' tag in his closing note)",
    'size': T['candidates'],
    'evidence_surfaces': [
        {'service': 'linear', 'tool': 'linear_list_comments', 'per_record_calls': 1, 'records': T['candidates'], 'seeded': True,
         'seeded_ids': notes_all,
         'why_no_bulk': "linear_list_issues returns titles, states, assignees and descriptions but no comments; the base has "
                        "no Linear comments; Blake's 'tiers:' tag exists only in his closing notes",
         'short_circuit': "membership of Blake's 94 tickets is decided only by the tag; the 4 tagged ones have titles with no "
                          "difficulty word (spawn gaps, item removal, lives, level 1 order) while difficulty-sounding ones "
                          "(insertion, replacement, algo, stats, spawn limits, CPS/DPS) are untagged; every Blake ticket has a "
                          "note, so having a note reveals nothing",
         'requirement': 'R1', 'decides': 'register membership'},
        {'service': 'linear', 'tool': 'linear_list_comments', 'per_record_calls': 0.12, 'records': T['members'], 'seeded': True,
         'seeded_ids': decisive,
         'why_no_bulk': "where a member's change lives (editor panel vs runtime) is stated only in its note",
         'short_circuit': "titles suggest gameplay for ZOM-277 and editor for ZOM-45; ZOM-173's and ZOM-312's PRs also touch "
                          "runtime folders and only the note says which part is the ticket's",
         'requirement': 'R2', 'decides': 'status per ticket'},
        {'service': 'github', 'tool': 'github_get_pull_request+github_get_pull_request_comments', 'per_record_calls': 0.1,
         'records': T['members'], 'seeded': True, 'seeded_ids': [PRC],
         'why_no_bulk': "PR search returns titles and merge state, not the CodeRabbit file table or the conversation",
         'short_circuit': "ZOM-282's status depends on what #401 changed (it finished the hp part, so ZOM-282 is Live); the "
                          "#243 / #265 tables are where a run checks the notes' split of a shared PR",
         'requirement': 'R2', 'decides': 'status per ticket'},
    ],
}

CHAINS = [
    {'id': 'C1', 'root_cause': 'A1', 'ends_in': 'R4',
     'hops': [{'service': 'slack', 'record': SUM, 'finding': "Brian: the same +50% for every monster, like 282 says"},
              {'service': 'confluence', 'record': PCMT, 'finding': "Blake: speed and damage only, values per monster, julia keeps them"},
              {'service': 'gsheets', 'record': SHEET, 'finding': "Live tab: per-monster values, MonsterBase 0.8/0.8, hp 0"}]},
    {'id': 'C2', 'root_cause': 'A12', 'ends_in': 'R1',
     'hops': [{'service': 'slack', 'record': ASK, 'finding': "rules are on the difficulty baseline card"},
              {'service': 'trello', 'record': CARD, 'finding': "vocabulary, window, Blake's tagged tickets"},
              {'service': 'trello', 'record': CMT, 'finding': "attack power counts too (+5)"},
              {'service': 'linear', 'record': N['ZOM-305']['id'], 'finding': "ZOM-305 'Losing a level deducts 2 lives' tagged tiers: -> member"}]},
    {'id': 'C3', 'root_cause': 'A15', 'ends_in': 'R2',
     'hops': [{'service': 'trello', 'record': CARD, 'finding': "status judged against the store builds"},
              {'service': 'gmail', 'record': G1, 'finding': "level editor / LevelDesigner and debug tooling stripped"},
              {'service': 'linear', 'record': N['ZOM-277']['id'], 'finding': "ZOM-277 is the editor stats panel average -> Editor only though Done"}]},
    {'id': 'C4', 'root_cause': 'A13', 'ends_in': 'R8',
     'hops': [{'service': 'trello', 'record': CARD, 'finding': "share with everyone on the tuning session invite"},
              {'service': 'gcal', 'record': EVT, 'finding': "attendees Leonard, Robert, Arthur, Brian"},
              {'service': 'gdrive', 'record': FOLDER, 'finding': "Robert editor, the other three commenters"}]},
    {'id': 'C5', 'root_cause': 'A16', 'ends_in': 'R4',
     'hops': [{'service': 'linear', 'record': 'ZOM-42', 'finding': "spec: first 10 level avg CPM > 90 -> tier 1"},
              {'service': 'linear', 'record': 'ZOM-199', 'finding': "restates it as >= 90"},
              {'service': 'confluence', 'record': PAGE, 'finding': "page: 90 or more"},
              {'service': 'gmail', 'record': G2, 'finding': "Blake's reply: the build checks > 90; ZOM-199 is wrong"}]},
    {'id': 'C6', 'root_cause': 'A3', 'ends_in': 'R4',
     'hops': [{'service': 'trello', 'record': CARD, 'finding': "rule 5: tier rules on the Confluence page and in ZOM-42 itself"},
              {'service': 'confluence', 'record': PAGE, 'finding': "page: demotion = 4 losses in a row only"},
              {'service': 'linear', 'record': 'ZOM-42', 'finding': "full spec (past the list truncation): also <= 50% over up to 10; record resets"}]},
    {'id': 'C7', 'root_cause': 'A17', 'ends_in': 'R1',
     'hops': [{'service': 'trello', 'record': CARD, 'finding': "Apr 21 - Aug 31, whole words, duplicates out"},
              {'service': 'linear', 'record': 'ZOM-517', 'finding': "enrage title, created Sep 3 -> out"},
              {'service': 'linear', 'record': 'ZOM-271', 'finding': "ATK POWER is not 'attack power' -> out"}]},
    {'id': 'C8', 'root_cause': 'A8', 'ends_in': 'R7',
     'hops': [{'service': 'gmail', 'record': G2, 'finding': "ZOM-199's >= is not what the build does"},
              {'service': 'trello', 'record': CARD, 'finding': "rule 6: comment on that ticket, same tickets, no new ones"},
              {'service': 'linear', 'record': 'ZOM-200', 'finding': "lookalike CPM debug-menu ticket is not the one"}]},
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
     resolver="the notes (runtime label; editor stats panel) against the mail's stripped tooling", discovery_order='titles are read before notes')
trap(id='T6', family='superseding', services=['linear', 'confluence', 'gmail'], base_pointers=['ZOM-199'], seeded_ids=[PAGE, G2],
     requirement='R4', expected_wrong_reading='starting tier at 90 or more (ZOM-199, the page)',
     resolver="Blake's reply in the store builds thread: the build checks > 90",
     discovery_order='the first mail looks complete; the reply sits under it',
     version_records=[{'service': 'confluence', 'id': PAGE, 'seeded': True, 'at': M['CONF_DDA']['at']},
                      {'service': 'gmail', 'id': G2, 'seeded': True, 'at': M['G_BUILD_RE']['at']}])
trap(id='T7', family='superseding', distractor_type='stale_summary', services=['slack'], seeded_ids=[M['S_ROBERT_SUM']['id']],
     requirement='R2', expected_wrong_reading="Brian: the editor bits (tier delete, stats window, debug menu) are in the store builds -> Live",
     resolver='the store builds mail: editor and debug tooling are stripped', discovery_order='#zombie-design is the first channel a difficulty search hits',
     version_records=[{'service': 'slack', 'id': M['S_ROBERT_SUM']['id'], 'seeded': True, 'at': M['S_ROBERT_SUM']['at']},
                      {'service': 'gmail', 'id': G1, 'seeded': True, 'at': M['G_BUILD']['at']}])
trap(id='T8', family='superseding', services=['linear', 'github', 'gsheets'], base_pointers=['ZOM-254', 'ZOM-282'], seeded_ids=[N['ZOM-282']['id'], PRC, SHEET],
     requirement='R4', expected_wrong_reading='enrage +25% (ZOM-254) or +50% (ZOM-282) for every monster, hp boost on respawns', resolver='Live tab (per monster, hp 0)',
     version_records=[{'service': 'linear', 'id': N['ZOM-282']['id'], 'seeded': True, 'at': N['ZOM-282']['at']},
                      {'service': 'github', 'id': PRC, 'seeded': True, 'at': M['PRC_244']['at']},
                      {'service': 'gsheets', 'id': SHEET, 'seeded': True, 'at': M['SHEET_KNOBS']['at']}])
trap(id='T9', family='distractor', distractor_type='scope_adjacent', services=['gsheets'], seeded_ids=[SHEET], requirement='R4',
     expected_wrong_reading="copies the Next pass tab (Leonard's per-level proposal)", resolver='card rule 5: as they work today -> Live tab')
trap(id='T10', family='tool_surface', services=['linear', 'confluence'], base_pointers=['ZOM-42'], seeded_ids=[PAGE], requirement='R4',
     expected_wrong_reading='demotion only after 4 losses in a row (page, truncated list description)',
     resolver='ZOM-42 read in full: also <= 50% over up to the last 10, record resets after every move',
     discovery_order='linear_list_issues truncates the 4,244-char description; the page restates only the streak')
trap(id='T11', family='superseding', services=['confluence', 'gsheets'], seeded_ids=[PAGE, SHEET, PCMT], requirement='R4',
     expected_wrong_reading='enrage +25% speed, damage and max HP from the page', resolver="the sheet's Live tab; Blake's page comment retires the line",
     version_records=[{'service': 'confluence', 'id': PAGE, 'seeded': True, 'at': M['CONF_DDA']['at']},
                      {'service': 'gsheets', 'id': SHEET, 'seeded': True, 'at': M['SHEET_KNOBS']['at']},
                      {'service': 'confluence', 'id': PCMT, 'seeded': True, 'at': M['CC_ART']['at']}])
trap(id='T12', family='distractor', distractor_type='lookalike_entity', services=['trello'], seeded_ids=[DDCARD], requirement='R8',
     expected_wrong_reading='shares with Brian and Vincent as editors / saves in the Difficulty Optimization sheet (DD card)',
     resolver='the ZM ROADMAP card named in the ask', discovery_order='a Trello search for "difficulty baseline" returns both')
trap(id='T13', family='cross_reference_gap', services=['gcal', 'gdrive'], seeded_ids=[EVT], requirement='R8',
     expected_wrong_reading='shares with Robert only, or with Robert and Blake (people named on the card)', resolver='invite attendees: Leonard, Robert, Arthur, Brian')
trap(id='T14', family='reuse_exclusion', services=['linear'], base_pointers=['ZOM-199', 'ZOM-200'], seeded_ids=[G2], requirement='R7',
     expected_wrong_reading='opens a new ticket for the CPM check, or comments on ZOM-42 / ZOM-200', resolver='card rule 6: comment on the ticket that says it (ZOM-199)')
trap(id='T15', family='eliminating_evidence', services=['linear', 'github'], seeded_ids=[N['ZOM-173']['id'], N['ZOM-312']['id']],
     base_pointers=['harmonygames-Games/match3d#243', 'harmonygames-Games/match3d#265'],
     requirement='R2', expected_wrong_reading='ZOM-173 / ZOM-312 Live (their PRs also change runtime folders)',
     resolver="the notes: ZOM-173 is the set count in the level objects panel (the rest is ZOM-307's); ZOM-312's events are the editor's")
trap(id='T16', family='distractor', distractor_type='non_authoritative_instruction', services=['slack'], seeded_ids=[M['S_BRIAN_POST']['id']],
     requirement='R6', expected_wrong_reading='posts the counts in #zombie-design instead of the DM', resolver="Leonard's ask: reply here")
trap(id='T17', family='distractor', distractor_type='scope_adjacent', services=['gsheets'], base_pointers=[f'gsheets:{DDSHEET}'],
     requirement='R4', expected_wrong_reading="takes Domino Delights parameters for the rules tab", resolver='H3 is the ZM monster enrage sheet')
trap(id='T18', family='exact_predicate', services=['linear'], base_pointers=['ZOM-257', 'ZOM-289', 'ZOM-383', 'ZOM-209', 'ZOM-190', 'ZOM-96', 'ZOM-24'],
     requirement='R1', expected_wrong_reading='adds difficulty-sounding Blake tickets (insertion, replacement, algo, stats, CPS/DPS) as tier work',
     resolver='their notes carry no tiers: tag')
trap(id='T19', family='superseding', services=['slack', 'gmail'], base_pointers=['C08R27X0EAH/1758081917.318539'], seeded_ids=[G1],
     requirement='R2', expected_wrong_reading='judges against iOS 0.3.38 (submitted Sep 17)', resolver="the mail: iOS 0.3.49 / Android 0.3.133",
     version_records=[{'service': 'slack', 'base_pointer': 'C08R27X0EAH/1758081917.318539', 'seeded': False, 'at': '2025-09-17T04:05:17Z'},
                      {'service': 'gmail', 'id': G1, 'seeded': True, 'at': M['G_BUILD']['at']}])
trap(id='T20', family='exact_predicate', services=['linear'], base_pointers=['ZOM-305', 'ZOM-352'], requirement='R1',
     expected_wrong_reading="treats the two lives tickets alike: both in, or both out",
     resolver="ZOM-305's note is tagged tiers:; ZOM-352's note cites match3d#282 with no tag")
trap(id='T21', family='eliminating_evidence', services=['linear', 'github'], base_pointers=['ZOM-282', 'harmonygames-Games/match3d#401'],
     seeded_ids=[PRC], requirement='R3', expected_wrong_reading='ZOM-282 Replaced by #401 (or ZOM-254 replaced by #401)',
     resolver="#401 finished what ZOM-282 asked (no hp, speed and damage); rule 4 'name the first one that did' -> ZOM-254 by ZOM-282")

BUDGET = [
    {'phase': 'discovery', 'service': 'slack', 'calls': 2, 'reason': "read the ask in the Leonard-Julia DM; resolve Leonard's DM"},
    {'phase': 'discovery', 'service': 'trello', 'calls': 3, 'reason': 'search the board for the difficulty baseline card, read it, read its comments (amendment)'},
    {'phase': 'discovery', 'service': 'gmail', 'calls': 2, 'reason': "search for Blake's store builds mail, open the thread (the reply with the > 90 check)"},
    {'phase': 'discovery', 'service': 'gsheets', 'calls': 2, 'reason': 'find the monster enrage sheet, read the Live tab'},
    {'phase': 'discovery', 'service': 'confluence', 'calls': 3, 'reason': 'search the dynamic difficulty page, read it, list its comments'},
    {'phase': 'discovery', 'service': 'gcal', 'calls': 2, 'reason': 'find the Oct 6 tuning session and read its attendees (share list)'},
    {'phase': 'discovery', 'service': 'gdocs', 'calls': 2, 'reason': 'find and read the session agenda (sheet with two tabs)'},
    {'phase': 'discovery', 'service': 'gdrive', 'calls': 1, 'reason': 'find the ZM Difficulty folder id (destination)'},
    {'phase': 'enumeration', 'service': 'linear', 'calls': 5, 'reason': "page through ZOM issues created Apr 21 - Aug 31 (~470) to apply the title words and pick out Blake's"},
    {'phase': 'rules', 'service': 'linear', 'calls': 1, 'reason': 'read ZOM-42 in full (4,244-char spec: > 90, the 50% demotion rule and the record reset are past the truncation)'},
    {'phase': 'rules', 'service': 'linear', 'calls': 3, 'reason': 'read ZOM-199, ZOM-254, ZOM-282 in full for the rules tab', 'conditional_on': 'list_issues truncates these shorter descriptions'},
    {'phase': 'per-record', 'service': 'linear', 'calls': T['candidates'], 'reason': "one linear_list_comments per candidate: the closing note's tiers: tag decides membership and the note decides where a change lives; no bulk comment call"},
    {'phase': 'per-record', 'service': 'github', 'calls': 3, 'reason': 'read #401 (what changed; Blake comment), #243 and #265 (file tables vs notes)'},
    {'phase': 'writes', 'service': 'gsheets', 'calls': 3, 'reason': 'create the register with Tickets and Rules in force tabs; write the rows'},
    {'phase': 'writes', 'service': 'gdrive', 'calls': 5, 'reason': 'move the sheet into ZM Difficulty; share with Robert (edit), Leonard, Arthur, Brian (comment)'},
    {'phase': 'writes', 'service': 'slack', 'calls': 1, 'reason': 'reply to Leonard in the DM with the counts'},
    {'phase': 'writes', 'service': 'linear', 'calls': 2, 'reason': 'comment on ZOM-199 (build checks > 90) and on ZOM-254 (replaced by ZOM-282)'},
    {'phase': 'read-back', 'service': 'gsheets', 'calls': 1, 'reason': 'read the register back to check the rows and counts'},
]

WRITES = [
    {'service': 'gsheets', 'tool': 'gsheets_create_spreadsheet+gsheets_values_update', 'count': 3,
     'depends_on': ['K2', 'K3', 'K4', 'K5', 'K6', 'K7', 'K8', 'K11', 'K12', 'K13', 'C1', 'C2', 'C3', 'C5', 'C6', 'C7', 'T1', 'T5', 'T6', 'T8', 'T10', 'T15'],
     'requirements': ['R1', 'R2', 'R3', 'R4', 'R9']},
    {'service': 'gdrive', 'tool': 'gdrive_move_file+gdrive_share_file', 'count': 5, 'depends_on': ['K9', 'K10', 'C4', 'T12', 'T13'],
     'requirements': ['R5', 'R8']},
    {'service': 'slack', 'tool': 'slack_send_message', 'count': 1, 'depends_on': ['K1', 'C2', 'C3', 'T16'], 'requirements': ['R6']},
    {'service': 'linear', 'tool': 'linear_create_comment', 'count': 2, 'depends_on': ['K5', 'C5', 'C8', 'T14', 'T21'],
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
         'why_safe': "ZOM-292 (Todo, match3d#267 merged) and ZOM-387 (Todo, match3d#319 merged) are candidates only; the SQL "
                     "does not modify them or their PRs. Blake's seeded notes (before each issue's updated_at) say each stays open "
                     "for the rest of its list and that the first part went in with the PR - dated human claims that explain the "
                     "state; neither is a member (no tier-code file)", 'requirement': 'R1'}],
    'denied_probes': [],
}
json.dump(MAN, open(WF + '01_Hardness_Manifest.draft.json', 'w'), indent=1)
print('fragments', len(F), 'traps', len(Tr), 'chains', len(CHAINS),
      'budget', sum(b['calls'] for b in BUDGET if 'conditional_on' not in b), '(+cond', sum(b['calls'] for b in BUDGET if 'conditional_on' in b), ')')
