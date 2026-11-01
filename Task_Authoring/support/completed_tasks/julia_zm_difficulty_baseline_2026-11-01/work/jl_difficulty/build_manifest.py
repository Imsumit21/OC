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
PAGE = M['CONF_DDA']['id']
PCMT = M['CC_ART']['id']
PCMT_LOC = f"{M['CC_ART']['channel']}/{M['CC_ART']['ts']}"
PRC = M['PRC_244']['id']
N = M['LIN_NOTES']
ASK_REPLY = f"{M['S_ASK_REPLY']['channel']}/{M['S_ASK_REPLY']['ts']}"
JQ = f"{M['S_JQ']['channel']}/{M['S_JQ']['ts']}"
JQ_REPLY = f"{M['S_JQ_REPLY']['channel']}/{M['S_JQ_REPLY']['ts']}"
CL = M['T_H1CL']['id']
DDSHEET = 'f_34f0950581934de1278969'      # base: Domino Delights "Parameter Optimization" (Leonard; shared with Julia)


def q(key, s):
    text = json.dumps(P[key]) if not isinstance(P[key], str) else P[key]
    assert s in text, (key, s)
    return s


members = [r for r in T['rows'] if r['member']]
counts = T['counts']
REQ = {
    'R1': "register membership: the ZOM tickets created up to Aug 31 (since ZM started) that changed difficulty - a whole-word title match "
          "on the card's vocabulary, attack power in the title (card comment), or any ticket whose closing note from Arthur "
          "starts with 'tiers:' (incl. ZOM-281, assigned to someone else) - duplicates out, open/cancelled ones in; "
          "minus the analytics and tutorial tickets Leonard drops in his thread reply under the ask (ZOM-30, ZOM-49, "
          "ZOM-50, ZOM-161, ZOM-262, ZOM-275), minus ZOM-312 (Blake marked it 'not tiers' in his review on match3d#265) and "
          "ZOM-258 (Leonard's 'notes for monday' doc attached to the card), minus the four tickets Leonard names as the only extra ones to drop in his "
          "reply in the thread under Julia's Sep 29 DM question (ZOM-162, ZOM-163, ZOM-201, ZOM-250); "
          f"{T['members']} tickets ({T['card_only']} by title, {T['amend']} by attack power, {T['tagged']} by Arthur's notes)",
    'R2': "status per ticket (Live, Editor only, Replaced, Not shipped) judged against the store builds players have "
          "(iOS 0.3.49, Android 0.3.133) under Blake's store builds mail: level editor / LevelDesigner and debug tooling "
          "never reach players (ZOM-45 and ZOM-303 Live, ZOM-277 Editor only)",
    'R3': "replaced-by per Replaced ticket: ZOM-254 by ZOM-282",
    'R4': "rules in force today: starting tier (after a new player's first 10 games, wins and losses, average CPM over them > 90 -> tier 1, 90 or less tier 0; the build, not the write-ups' '10 levels'); promotion (win "
          "rate >= 80% over up to the last 10 attempts; tier -2 promotes after one win); demotion (4 losses in a row, or "
          "win rate <= 50% over up to the last 10; the record resets after every move); after a demotion the current level "
          "loads one tier down; enrage on blunder adds speed and damage per monster (Live tab of the monster enrage sheet; "
          "MonsterBase 0.8/0.8 for the rest), no HP boost",
    'R5': "register saved in the ZM Difficulty folder",
    'R6': f"reply to Leonard in the DM with the counts: {T['members']} tickets, {counts.get('Live')} Live, "
          f"{counts.get('Editor only')} Editor only, {counts.get('Replaced')} Replaced, {counts.get('Not shipped')} Not shipped, "
          "plus the keys of the Not shipped and the Editor only tickets (Leonard's thread reply), and when a new player gets the "
          "starting tier: after their first 10 games (wins and losses), not after level 10; and which ticket replaced which "
          "(ZOM-254 by ZOM-282; Leonard's 'notes for monday' doc)",
    'R7': "comment on ZOM-199 that the build checks CPM > 90 (not >= 90) and on ZOM-254 naming ZOM-282 as its "
          "replacement; and (checklist rule 6 change) a comment on each of the " + f"{counts.get('Editor only')} Editor only and {counts.get('Not shipped')} Not shipped tickets saying "
          "the change isn't in the store builds; none on the four dropped tickets (ZOM-162, ZOM-163, ZOM-201, ZOM-250); same tickets, no new ones",
    'R8': "register shared with everyone on the tuning session invite: Robert as editor; Brian as commenter (the checklist's rule 7 "
          "change gave him edit, Leonard's later reply under Julia's Sep 29 question takes it back); "
          "Leonard as commenter; Arthur as viewer (Leonard's 'notes for monday' doc: view access is enough for him)",
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
               'weight_reason': "what #401 changed (speed/damage split; the unused EnrageHealth method dropped) and the shared-PR file tables live here"},
    'gsheets': {'role': "H3 ZM monster enrage sheet (Julia's; Live, Next pass, History); the register write; DD Parameter "
                        "Optimization decoy (base)",
                'weight_reason': "the per-monster enrage numbers in force exist only on the Live tab"},
    'gslides': {'role': "Robert's dynamic difficulty deck (tier rules without the 50% demotion rule, stale +25% blunder line)",
                'weight_reason': "the deck is the named tier-rules source (card rule 5)"},
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
frag(id='K7', service='gslides', container=PAGE, locator=f'gslides:{PAGE}', kind='requirement', incorporated_via=['A1', 'K2'],
     seeded_ids=[PAGE], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', "The tier rules are written up in Robert's dynamic difficulty deck"), requirement_ids=['R4'])
frag(id='K8', service='slack', container='C090N54TG79', locator=PCMT_LOC, kind='amendment', incorporated_via=['A1', 'K2'],
     seeded_ids=[PCMT], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', "The tier rules are written up in Robert's dynamic difficulty deck"), requirement_ids=['R4'],
     supersedes='K7 blunder line (+25% speed, damage, HP)', resolver="Blake's newer #zombie-design message about the deck")
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
     delegation_quote=q('H1_DESC', "his closing note on those starts with 'tiers:'"), requirement_ids=['R1'])

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
    'key': "ZOM ticket created up to 2025-08-31 (first ZOM ticket 2025-04-18; not Duplicate) matching the card vocabulary or attack power in the "
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
         'short_circuit': "ZOM-282's status depends on what #401 changed (it only split ZOM-282's shared value, so ZOM-282 is Live); the "
                          "#243 / #265 tables are where a run checks the notes' split of a shared PR",
         'requirement': 'R2', 'decides': 'status per ticket'},
    ],
}

CHAINS = [
    {'id': 'C1', 'root_cause': 'A1', 'ends_in': 'R4',
     'hops': [{'service': 'slack', 'record': SUM, 'finding': "Brian: the same +50% for every monster, like 282 says"},
              {'service': 'slack', 'record': PCMT_LOC, 'finding': "Blake: speed and damage only, values per monster, julia keeps them"},
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
              {'service': 'gdrive', 'record': FOLDER, 'finding': "Robert editor, the others comment (then: Brian edits per the checklist, Arthur views per Leonard's notes, Brian back to comment per Leonard's later reply)"}]},
    {'id': 'C5', 'root_cause': 'A16', 'ends_in': 'R4',
     'hops': [{'service': 'linear', 'record': 'ZOM-42', 'finding': "spec: first 10 level avg CPM > 90 -> tier 1"},
              {'service': 'linear', 'record': 'ZOM-199', 'finding': "restates it as >= 90"},
              {'service': 'gslides', 'record': PAGE, 'finding': "deck: 90 or more"},
              {'service': 'gmail', 'record': G2, 'finding': "Blake's reply: the build checks > 90; ZOM-199 is wrong"}]},
    {'id': 'C6', 'root_cause': 'A3', 'ends_in': 'R4',
     'hops': [{'service': 'trello', 'record': CARD, 'finding': "rule 5: tier rules in Robert's deck and in ZOM-42 itself"},
              {'service': 'gslides', 'record': PAGE, 'finding': "deck: demotion = 4 losses in a row only"},
              {'service': 'linear', 'record': 'ZOM-42', 'finding': "full spec (past the list truncation): also <= 50% over up to 10; record resets"}]},
    {'id': 'C7', 'root_cause': 'A17', 'ends_in': 'R1',
     'hops': [{'service': 'trello', 'record': CARD, 'finding': "up to Aug 31, whole words, duplicates out"},
              {'service': 'linear', 'record': 'ZOM-517', 'finding': "enrage title, created Sep 3 -> out"},
              {'service': 'linear', 'record': 'ZOM-271', 'finding': "ATK POWER is not 'attack power' -> out"}]},
    {'id': 'C8', 'root_cause': 'A8', 'ends_in': 'R7',
     'hops': [{'service': 'gmail', 'record': G2, 'finding': "ZOM-199's >= is not what the build does"},
              {'service': 'trello', 'record': CARD, 'finding': "rule 6: comment on that ticket, same tickets, no new ones"},
              {'service': 'linear', 'record': 'ZOM-200', 'finding': "lookalike CPM debug-menu ticket is not the one"}]},
    {'id': 'C9', 'root_cause': 'A14', 'ends_in': 'R1',
     'hops': [{'service': 'slack', 'record': ASK, 'finding': "the ask (reply_count 1): rules on the card, reply with counts"},
              {'service': 'slack', 'record': ASK_REPLY, 'finding': "thread reply: drop ZOM-30/49/50/161/262/275; put the Not shipped and Editor only keys in the reply"},
              {'service': 'linear', 'record': 'ZOM-30', 'finding': "an analytics ticket that matches the card words but is off the list"}]},
    {'id': 'C10', 'root_cause': 'A3', 'ends_in': 'R7',
     'hops': [{'service': 'trello', 'record': CARD, 'finding': "rule 6: Editor only tickets stay as they are; rule 7: everyone else comments"},
              {'service': 'trello', 'record': CL, 'finding': "checklist (not in the search or comments result): rule 6 and rule 7 changes"},
              {'service': 'linear', 'record': 'ZOM-173', 'finding': "each Editor only and Not shipped ticket gets a comment; Brian edits"}]},
    {'id': 'C11', 'root_cause': 'A3', 'ends_in': 'R1',
     'hops': [{'service': 'trello', 'record': CARD, 'finding': "rule 1: a title match Blake marked 'not tiers' in his review on its PR stays off"},
              {'service': 'linear', 'record': 'ZOM-312', 'finding': "closing note: merged with match3d#265"},
              {'service': 'github', 'record': 'harmonygames-Games/match3d#265', 'finding': "Blake's review has an empty body; its inline comment says 'not tiers'"}]},
    {'id': 'C12', 'root_cause': 'A3', 'ends_in': 'R1',
     'hops': [{'service': 'trello', 'record': CARD, 'finding': "badges: 1 attachment (not in the default card read)"},
              {'service': 'trello', 'record': M['T_H1ATT']['id'], 'finding': "link to Leonard's 'notes for monday' doc"},
              {'service': 'gdocs', 'record': M['DOC_LEO_NOTES']['id'], 'finding': "leave ZOM-258 off; Arthur view only; reply says which ticket replaced which"}]},
    {'id': 'C13', 'root_cause': 'A3', 'ends_in': 'R1',
     'hops': [{'service': 'slack', 'record': JQ, 'finding': "Julia's Sep 29 question to Leonard, an older top-level DM message with reply_count 1"},
              {'service': 'slack', 'record': JQ_REPLY, 'finding': "Leonard's reply in that thread: 'take 162, 163, 201 and 250 off … just those four', no comments on them; Brian comment only"},
              {'service': 'linear', 'record': 'ZOM-162', 'finding': "a title-matched Editor only ticket that is off the list and gets no comment"}]},
]

Tr = []


frag(id='K14', service='slack', container=M['S_ASK']['channel'], locator=f'{ASK_REPLY} (thread reply under {ASK})', kind='amendment',
     incorporated_via=['A1'], seeded_ids=[M['S_ASK_REPLY']['id']], delegated_by_record=ASK,
     delegation_quote=q('S_ASK', 'i want a baseline of the difficulty system from you'), requirement_ids=['R1', 'R6'])
frag(id='K18', service='slack', container=M['S_JQ']['channel'], locator=f'{JQ_REPLY} (thread reply under Julia\'s question {JQ})', kind='amendment',
     incorporated_via=['A1'], seeded_ids=[M['S_JQ']['id'], M['S_JQ_REPLY']['id']], delegated_by_record=ASK,
     delegation_quote=q('S_ASK', 'i want a baseline of the difficulty system from you'), requirement_ids=['R1', 'R6', 'R7', 'R8'])
frag(id='K15', service='trello', container=CARD, locator=f'trello:{CL} (checklist "Before Monday" on {CARD})', kind='amendment',
     incorporated_via=['A1', 'K2'], seeded_ids=[CL, M['T_H1CI1']['id'], M['T_H1CI2']['id']], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', 'Julia owns this one.'), requirement_ids=['R7', 'R8'])
RV265, RC265, ATT, LNOTES = M['GH_265_REV']['id'], M['GH_265_RC']['id'], M['T_H1ATT']['id'], M['DOC_LEO_NOTES']['id']
frag(id='K16', service='github', container='harmonygames-Games/match3d#265', locator=f'{RC265} (inline comment on Blake\'s review {RV265})',
     kind='amendment', incorporated_via=['K2'], seeded_ids=[RV265, RC265], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', "a title match Blake marked 'not tiers' in his review on its PR stays off"), requirement_ids=['R1', 'R6', 'R7'])
frag(id='K17', service='gdocs', container=LNOTES, locator=f'trello:{ATT} (attachment on {CARD}) -> gdocs:{LNOTES}', kind='amendment',
     incorporated_via=['A1', 'K2'], seeded_ids=[ATT, LNOTES], delegated_by_record=CARD,
     delegation_quote=q('H1_DESC', 'Julia owns this one.'), requirement_ids=['R1', 'R6', 'R8'])


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
     resolver='card rule 1 window up to Aug 31', discovery_order='a title search for enrage/tier returns them first')
trap(id='T3', family='distractor', distractor_type='keyword_collision', services=['linear'], base_pointers=['ZOM-271'],
     requirement='R1', expected_wrong_reading="adds ZOM-271 ('ATK POWER BU...') as an attack power ticket",
     resolver="the comment says attack power in the title; ATK POWER is not the phrase", discovery_order='a search for "attack" returns it')
trap(id='T4', family='distractor', distractor_type='near_duplicate_record', services=['linear'], base_pointers=['ZOM-203', 'ZOM-276'],
     requirement='R1', expected_wrong_reading='lists the two Duplicate tickets', resolver='card rule 1: duplicates are out')
trap(id='T5', family='scope_alias', services=['linear', 'gmail'], seeded_ids=[N['ZOM-45']['id'], N['ZOM-277']['id'], G1],
     requirement='R2', expected_wrong_reading='ZOM-45 Editor only (title says editor); ZOM-277 Live (title says items in level)',
     resolver="the notes (runtime label; editor stats panel) against the mail's stripped tooling", discovery_order='titles are read before notes')
trap(id='T6', family='superseding', services=['linear', 'gslides', 'gmail'], base_pointers=['ZOM-199'], seeded_ids=[PAGE, G2],
     requirement='R4', expected_wrong_reading='starting tier at 90 or more (ZOM-199, the page)',
     resolver="Blake's reply in the store builds thread: the build checks > 90",
     discovery_order='the first mail looks complete; the reply sits under it',
     version_records=[{'service': 'gslides', 'id': PAGE, 'seeded': True, 'at': M['CONF_DDA']['at']},
                      {'service': 'gmail', 'id': G2, 'seeded': True, 'at': M['G_BUILD_RE']['at']}])
trap(id='T7', family='superseding', distractor_type='stale_summary', services=['slack'], seeded_ids=[M['S_ROBERT_SUM']['id']],
     requirement='R2', expected_wrong_reading="Brian: the editor bits (tier delete, stats window, debug menu) are in the store builds -> Live",
     resolver='the store builds mail: editor and debug tooling are stripped', discovery_order='#zombie-design is the first channel a difficulty search hits',
     version_records=[{'service': 'slack', 'id': M['S_ROBERT_SUM']['id'], 'seeded': True, 'at': M['S_ROBERT_SUM']['at']},
                      {'service': 'gmail', 'id': G1, 'seeded': True, 'at': M['G_BUILD']['at']}])
trap(id='T8', family='superseding', services=['linear', 'github', 'gsheets'], base_pointers=['ZOM-254', 'ZOM-282'], seeded_ids=[N['ZOM-282']['id'], PRC, SHEET],
     requirement='R4', expected_wrong_reading='enrage +25% (ZOM-254) or +50% (ZOM-282) for every monster, plus an hp boost (ZOM-254, the deck)', resolver='Live tab (per monster, hp 0)',
     version_records=[{'service': 'linear', 'id': N['ZOM-282']['id'], 'seeded': True, 'at': N['ZOM-282']['at']},
                      {'service': 'github', 'id': PRC, 'seeded': True, 'at': M['PRC_244']['at']},
                      {'service': 'gsheets', 'id': SHEET, 'seeded': True, 'at': M['SHEET_KNOBS']['at']}])
trap(id='T9', family='distractor', distractor_type='scope_adjacent', services=['gsheets'], seeded_ids=[SHEET], requirement='R4',
     expected_wrong_reading="copies the Next pass tab (Leonard's per-level proposal)", resolver='card rule 5: as they work today -> Live tab')
trap(id='T10', family='tool_surface', services=['linear', 'gslides'], base_pointers=['ZOM-42'], seeded_ids=[PAGE], requirement='R4',
     expected_wrong_reading='demotion only after 4 losses in a row (page, truncated list description)',
     resolver='ZOM-42 read in full: also <= 50% over up to the last 10, record resets after every move',
     discovery_order='linear_list_issues truncates the 4,244-char description; the page restates only the streak')
trap(id='T11', family='superseding', services=['gslides', 'gsheets', 'slack'], seeded_ids=[PAGE, SHEET, PCMT], requirement='R4',
     expected_wrong_reading='enrage +25% speed, damage and max HP from the page', resolver="the sheet's Live tab; Blake's page comment retires the line",
     version_records=[{'service': 'gslides', 'id': PAGE, 'seeded': True, 'at': M['CONF_DDA']['at']},
                      {'service': 'slack', 'id': PCMT, 'seeded': True, 'at': M['CC_ART']['at']},
                      {'service': 'gsheets', 'id': SHEET, 'seeded': True, 'at': M['SHEET_KNOBS']['at']}])
trap(id='T12', family='distractor', distractor_type='lookalike_entity', services=['trello'], seeded_ids=[DDCARD], requirement='R8',
     expected_wrong_reading='shares with Brian and Vincent as editors / saves in the Difficulty Optimization sheet (DD card)',
     resolver='the ZM ROADMAP card named in the ask', discovery_order='a Trello search for "difficulty baseline" returns both')
trap(id='T13', family='cross_reference_gap', services=['gcal', 'gdrive'], seeded_ids=[EVT], requirement='R8',
     expected_wrong_reading='shares with Robert only, or with Robert and Blake (people named on the card)', resolver='invite attendees: Leonard, Robert, Arthur, Brian')
trap(id='T14', family='reuse_exclusion', services=['linear'], base_pointers=['ZOM-199', 'ZOM-200'], seeded_ids=[G2], requirement='R7',
     expected_wrong_reading='opens a new ticket for the CPM check, or comments on ZOM-42 / ZOM-200', resolver='card rule 6: comment on the ticket that says it (ZOM-199)')
trap(id='T15', family='eliminating_evidence', services=['linear', 'github'], seeded_ids=[N['ZOM-173']['id']],
     base_pointers=['harmonygames-Games/match3d#243'],
     requirement='R2', expected_wrong_reading='ZOM-173 Live (its PR also changes runtime folders)',
     resolver="the note: ZOM-173 is the set count in the level objects panel (the rest is ZOM-307's)")
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
     resolver="rule 4: only another ticket's closing note that says it replaces a ticket makes it Replaced; ZOM-282's note says it replaces ZOM-254; #401 only splits ZOM-282's numbers")

trap(id='T22', family='superseding', services=['slack'], seeded_ids=[M['S_ASK_REPLY']['id']], requirement='R1',
     expected_wrong_reading='keeps ZOM-30, ZOM-49, ZOM-50, ZOM-161, ZOM-262 and ZOM-275 (35 rows, 22 Live) and replies with counts only',
     resolver="Leonard's thread reply under his ask drops the analytics and tutorial tickets and asks for the Not shipped and Editor only keys",
     version_records=[{'service': 'trello', 'id': CARD, 'seeded': True, 'at': M['T_H1UPD']['at']},
                      {'service': 'slack', 'id': M['S_ASK']['id'], 'seeded': True, 'at': M['S_ASK']['at']},
                      {'service': 'slack', 'id': M['S_ASK_REPLY']['id'], 'seeded': True, 'at': M['S_ASK_REPLY']['at']}])
trap(id='T23', family='superseding', services=['trello'], seeded_ids=[CL, M['T_H1CI1']['id'], M['T_H1CI2']['id']], requirement='R7',
     expected_wrong_reading='follows rule 6 and 7 as written: no comments on the Editor only and Not shipped tickets; Brian as commenter',
     resolver="the card's 'Before Monday' checklist: rule 6 change (a comment on each Editor only and Not shipped ticket) and rule 7 change (Brian edits)",
     version_records=[{'service': 'trello', 'id': M['T_H1UPD']['id'], 'seeded': True, 'at': M['T_H1UPD']['at']},
                      {'service': 'trello', 'id': M['T_H1CLACT']['id'], 'seeded': True, 'at': M['T_H1CLACT']['at']}])

trap(id='T24', family='scope_alias', services=['linear'], seeded_ids=[N['ZOM-281']['id']], base_pointers=['ZOM-281'], requirement='R1',
     expected_wrong_reading="scans only keyword tickets and Blake's own tickets for the tiers: tag and misses ZOM-281 (assigned to someone else)",
     resolver="rule 1: any ticket Blake counts as tier work; his note on ZOM-281 starts with 'tiers:'")
trap(id='T25', family='superseding', services=['linear', 'gslides', 'github'], base_pointers=['ZOM-42', 'ZOM-199'], seeded_ids=[PAGE],
     requirement='R6', expected_wrong_reading="'after the first 10 levels' (ZOM-42, ZOM-199, the deck)",
     resolver="rule 5: for when a new player gets their starting tier, go by the build where a write-up disagrees; TierManager buckets at totalGames == 10, GetTotalGames = wins + losses",
     version_records=[{'service': 'linear', 'base_pointer': 'ZOM-42', 'seeded': False, 'at': '2025-05-31T02:54:30Z'},
                      {'service': 'gslides', 'id': PAGE, 'seeded': True, 'at': M['CONF_DDA']['at']}])
trap(id='T26', family='scope_alias', services=['github', 'linear'], seeded_ids=[RV265, RC265], base_pointers=['ZOM-312', 'harmonygames-Games/match3d#265'],
     requirement='R1', expected_wrong_reading="keeps ZOM-312 (title match, Editor only), comments on it and lists it among the Editor only keys",
     resolver="rule 1: a title match Blake marked 'not tiers' in his review on its PR stays off; his review on #265 is an empty COMMENTED review whose inline comment starts with 'not tiers'")
trap(id='T27', family='superseding', services=['trello', 'gdocs'], seeded_ids=[ATT, LNOTES], base_pointers=['ZOM-258'], requirement='R1',
     expected_wrong_reading="keeps ZOM-258 (title match 'Enraged', Live): 29 rows, 17 Live; Arthur as commenter; no replaced-by line in the reply",
     resolver="Leonard's 'notes for monday' doc, attached to the rules card: leave ZOM-258 off, Arthur view only, say which ticket replaced which",
     version_records=[{'service': 'trello', 'id': M['T_H1UPD']['id'], 'seeded': True, 'at': M['T_H1UPD']['at']},
                      {'service': 'trello', 'id': ATT, 'seeded': True, 'at': M['T_H1ATT']['at']}])
trap(id='T28', family='superseding', services=['slack', 'linear'], seeded_ids=[M['S_JQ']['id'], M['S_JQ_REPLY']['id']],
     base_pointers=['ZOM-162', 'ZOM-163', 'ZOM-201', 'ZOM-250'], requirement='R1',
     expected_wrong_reading="keeps ZOM-162/163/201/250 as Editor only (28 rows, 8 Editor only), comments on all four and lists them among the keys",
     resolver="Leonard's reply in the thread under Julia's Sep 29 DM question: take 162, 163, 201 and 250 off, 'just those four, on top of the ones i already left off', no comments on them",
     version_records=[{'service': 'trello', 'id': M['T_H1UPD']['id'], 'seeded': True, 'at': M['T_H1UPD']['at']},
                      {'service': 'slack', 'id': M['S_JQ_REPLY']['id'], 'seeded': True, 'at': M['S_JQ_REPLY']['at']}])
trap(id='T29', family='superseding', services=['slack', 'trello', 'gdrive'], seeded_ids=[M['S_JQ_REPLY']['id'], M['T_H1CI2']['id']],
     base_pointers=[], requirement='R8',
     expected_wrong_reading="shares the register with Brian as an editor (checklist rule 7 change)",
     resolver="Leonard's later reply (Sep 30 21:16Z) after the checklist (Sep 30 16:20Z): scratch Brian editing, comment access is enough",
     version_records=[{'service': 'trello', 'id': M['T_H1CLACT']['id'], 'seeded': True, 'at': M['T_H1CLACT']['at']},
                      {'service': 'slack', 'id': M['S_JQ_REPLY']['id'], 'seeded': True, 'at': M['S_JQ_REPLY']['at']}])

BUDGET = [
    {'phase': 'discovery', 'service': 'slack', 'calls': 4, 'reason': "read the ask in the Leonard-Julia DM; resolve Leonard's DM; open the ask's thread (Leonard's reply); open the thread under Julia's Sep 29 question (Leonard's later reply)"},
    {'phase': 'discovery', 'service': 'trello', 'calls': 4, 'reason': 'search the board for the difficulty baseline card, read it, read its comments (amendment)'},
    {'phase': 'discovery', 'service': 'gmail', 'calls': 2, 'reason': "search for Blake's store builds mail, open the thread (the reply with the > 90 check)"},
    {'phase': 'discovery', 'service': 'gsheets', 'calls': 2, 'reason': 'find the monster enrage sheet, read the Live tab'},
    {'phase': 'discovery', 'service': 'gslides', 'calls': 2, 'reason': "find Robert's dynamic difficulty deck and read its text"},
    {'phase': 'discovery', 'service': 'slack', 'calls': 1, 'reason': "search #zombie-design for the deck (Blake's Sep 3 correction)"},
    {'phase': 'discovery', 'service': 'gcal', 'calls': 2, 'reason': 'find the Oct 6 tuning session and read its attendees (share list)'},
    {'phase': 'discovery', 'service': 'gdocs', 'calls': 2, 'reason': 'find and read the session agenda (sheet with two tabs)'},
    {'phase': 'discovery', 'service': 'gdrive', 'calls': 1, 'reason': 'find the ZM Difficulty folder id (destination)'},
    {'phase': 'enumeration', 'service': 'linear', 'calls': 5, 'reason': "page through ZOM issues created up to Aug 31 (~470) to apply the title words and pick out Blake's"},
    {'phase': 'rules', 'service': 'linear', 'calls': 1, 'reason': 'read ZOM-42 in full (4,244-char spec: > 90, the 50% demotion rule and the record reset are past the truncation)'},
    {'phase': 'rules', 'service': 'linear', 'calls': 3, 'reason': 'read ZOM-199, ZOM-254, ZOM-282 in full for the rules tab', 'conditional_on': 'list_issues truncates these shorter descriptions'},
    {'phase': 'per-record', 'service': 'linear', 'calls': T['candidates'], 'reason': "one linear_list_comments per candidate: the closing note's tiers: tag decides membership and the note decides where a change lives; no bulk comment call"},
    {'phase': 'per-record', 'service': 'github', 'calls': 3, 'reason': 'read #401 (what changed; Blake comment), #243 and #265 (file tables vs notes)'},
    {'phase': 'writes', 'service': 'gsheets', 'calls': 3, 'reason': 'create the register with Tickets and Rules in force tabs; write the rows'},
    {'phase': 'writes', 'service': 'gdrive', 'calls': 5, 'reason': 'move the sheet into ZM Difficulty; share with Robert (edit), Brian and Leonard (comment), Arthur (view)'},
    {'phase': 'writes', 'service': 'slack', 'calls': 1, 'reason': 'reply to Leonard in the DM with the counts'},
    {'phase': 'writes', 'service': 'linear', 'calls': 2 + counts.get('Editor only') + counts.get('Not shipped'), 'reason': f"comment on ZOM-199 (build checks > 90), on ZOM-254 (replaced by ZOM-282) and on each of the {counts.get('Editor only')} Editor only and {counts.get('Not shipped')} Not shipped tickets (checklist rule 6 change)"},
    {'phase': 'discovery', 'service': 'github', 'calls': 8, 'reason': "rule 1 'not tiers': find the PRs of the title matches (#243, #244, #265, #271) and read each PR's review comments (Blake's inline note on #265)"},
    {'phase': 'discovery', 'service': 'trello', 'calls': 1, 'reason': "list the rules card's attachments (Leonard's notes for monday)"},
    {'phase': 'discovery', 'service': 'gdocs', 'calls': 1, 'reason': "read Leonard's notes for monday (drop ZOM-258)"},
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
