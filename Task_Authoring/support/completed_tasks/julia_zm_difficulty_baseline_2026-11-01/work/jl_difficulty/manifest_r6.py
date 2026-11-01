"""Round 6 manifest update (pairs with harden_r6.py). Idempotent from the round-5 manifest backup.

Usage: manifest_r6.py <round-5 manifest> <out manifest>
"""
import json
import sys

M = json.load(open(sys.argv[1]))
CH = 'CAFC495E4006'
P_ID, P_TS = 'cec246a6e43158f200fe144f0dd7039c', '1759226461.318204'
R_ID, R_TS = 'abe096ff0b5d7216efbc889e91d6d13a', '1759229513.774912'
CARD = '68daca5871dba40417a00383'
RULE2 = "Layout as in the session agenda, plus the three things Robert asked for when I asked him in our group chat."


def by_id(lst, i):
    return next(x for x in lst if x.get('id') == i)


R = M['requirements']
if 'R10' not in R:
    R['R10'] = ("three extra Tickets-tab columns after status, from Robert's thread reply in the Robert / Leonard / Julia group "
                "chat (card rule 2 points to it): the ticket's Linear assignee, the day it was marked done (blank when it never "
                "got done: ZOM-202, ZOM-280, ZOM-293), and its Linear priority (1 Urgent, 2 High, 3 Medium, 4 Low)")
    R['R9'] = R['R9'] + "; the Tickets tab carries the agenda's columns plus Robert's three (R10)"

if not any(k['id'] == 'K19' for k in M['ask_fragments']):
    M['ask_fragments'].append({
        "id": "K19", "service": "slack", "container": CH,
        "locator": f"{CH}/{R_TS} (Robert's thread reply under Leonard's question {CH}/{P_TS})",
        "kind": "amendment", "incorporated_via": ["A1", "K2"], "seeded_ids": [P_ID, R_ID],
        "delegated_by_record": CARD, "delegation_quote": RULE2,
        "requirement_ids": ["R9", "R10"], "base_pointers": []})
k11 = by_id(M['ask_fragments'], 'K11')
k11['delegation_quote'] = "Layout as in the session agenda, plus"
k2 = by_id(M['ask_fragments'], 'K2')
k2['requirement_ids'] = sorted(set(k2['requirement_ids']) | {'R10'})

if not any(t['id'] == 'T32' for t in M['traps']):
    M['traps'].append({
        "id": "T32", "family": "tool_surface", "services": ["slack", "trello", "linear"],
        "seeded_ids": [P_ID, R_ID, CARD], "base_pointers": ["ZOM-23", "ZOM-42", "ZOM-288", "ZOM-293", "ZOM-295"],
        "requirement": "R10",
        "expected_wrong_reading": ("reads the group chat's top-level messages only (Leonard's question shows reply_count 1) "
                                   "and builds the Tickets tab with the agenda's five columns: no assignee, done date or priority"),
        "resolver": "card rule 2 names 'the three things Robert asked for when I asked him in our group chat'; Robert's answer is the thread reply under Leonard's question",
        "discovery_order": "the card is read first; the group chat holds Leonard's question at top level and Robert's answer only in its thread"})

if not any(c['id'] == 'C15' for c in M['chains']):
    M['chains'].append({"id": "C15", "root_cause": "A14", "ends_in": "R10", "hops": [
        {"service": "trello", "record": CARD, "finding": "rule 2: layout as in the agenda plus the three things Robert asked for in the group chat"},
        {"service": "slack", "record": P_ID, "finding": "Leonard asks Robert what he wants on Julia's list; reply_count 1"},
        {"service": "slack", "record": R_ID, "finding": "Robert, in the thread: assignee, the day it got marked done (blank if never), Linear priority, after status"},
        {"service": "linear", "record": "ZOM-293", "finding": "assignee robert, priority 4, never done -> blank done date"}]})

for b in M['call_budget']:
    if b.get('service') == 'slack' and b.get('phase') == 'discovery' and 'ask in the Leonard-Julia DM' in b.get('reason', ''):
        if 'group chat' not in b['reason']:
            b['calls'] += 2
            b['reason'] += "; find the Robert / Leonard / Julia group chat and open the thread under Leonard's question (Robert's reply)"

for w in M['writes']:
    if w['service'] == 'gsheets':
        w['depends_on'] = sorted(set(w['depends_on']) | {'K19', 'T32'})
        w['requirements'] = sorted(set(w['requirements']) | {'R10'})

DD = M['design_delta']
if not any(d.get('id') == 'R6-K19' for d in DD):
    DD.append({"id": "R6-K19", "change": f"third hidden thread reply in a different conversation (group chat {CH}): Robert's three extra Tickets-tab columns; card rule 2 points to it",
               "reason": "hardening round 6: 22 baseline/hardness runs show only thread replies land; spread graded weight over threads in separate conversations so failures split"})
json.dump(M, open(sys.argv[2], 'w'), indent=2, ensure_ascii=False)
print('ok', len(M['traps']), 'traps', len(M['chains']), 'chains')
