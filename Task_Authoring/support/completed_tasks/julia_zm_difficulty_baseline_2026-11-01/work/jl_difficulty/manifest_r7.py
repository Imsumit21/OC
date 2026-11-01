"""Round 7 manifest update (pairs with harden_r7.py). Idempotent from the round-6 manifest backup.

Usage: manifest_r7.py <round-6 manifest> <out manifest>
"""
import json
import sys

M = json.load(open(sys.argv[1]))
PR = 'harmonygames-Games/match3d#271'
REV, RC = PR + '#rev_2', PR + '#rc_1'
CARD = '68daca5871dba40417a00383'
ROBERT = 'abe096ff0b5d7216efbc889e91d6d13a'


def by_id(lst, i):
    return next(x for x in lst if x.get('id') == i)


R = M['requirements']
R['R1'] = R['R1'].replace(
    "minus ZOM-312 (Blake marked it 'not tiers' in his review on match3d#265)",
    "minus ZOM-312 and ZOM-295 (Blake marked them 'not tiers' in his reviews on match3d#265 and match3d#271)").replace(
    "24 tickets (15 by title, 4 by attack power, 5 by Arthur's notes)",
    "23 tickets (14 by title, 4 by attack power, 5 by Arthur's notes)")
assert 'ZOM-295' in R['R1'] and '23 tickets' in R['R1']
R['R6'] = R['R6'].replace("24 tickets, 16 Live,", "23 tickets, 15 Live,")
assert '23 tickets, 15 Live' in R['R6']
R['R10'] = R['R10'].replace(
    "the day it was marked done (blank when it never got done: ZOM-202, ZOM-280, ZOM-293)",
    "the day it was marked done as a Pacific day (Robert: 'pacific time'; ZOM-200 2025-06-12, ZOM-274 2025-06-20, "
    "ZOM-282 2025-06-20, where the UTC day is one later; blank when it never got done: ZOM-202, ZOM-280, ZOM-293)")
assert 'Pacific day' in R['R10']

if not any(k['id'] == 'K20' for k in M['ask_fragments']):
    M['ask_fragments'].append({
        "id": "K20", "service": "github", "container": PR,
        "locator": f"{RC} (inline comment on Blake's APPROVED review {REV}, empty body)",
        "kind": "amendment", "incorporated_via": ["K2"], "seeded_ids": [REV, RC],
        "delegated_by_record": CARD,
        "delegation_quote": "a title match Blake marked 'not tiers' in his review on its PR stays off",
        "requirement_ids": ["R1", "R6"], "base_pointers": ["ZOM-295"]})

if not any(t['id'] == 'T33' for t in M['traps']):
    M['traps'].append({
        "id": "T33", "family": "scope_alias", "services": ["github", "linear"],
        "seeded_ids": [REV, RC], "base_pointers": ["ZOM-295", PR],
        "requirement": "R1",
        "expected_wrong_reading": ("keeps ZOM-295 (enrage title match, Done, Live): reads the PR's reviews list only, where "
                                   "Blake's review is an approval with an empty body, and never opens the inline comments"),
        "resolver": ("rule 1: a title match Blake marked 'not tiers' in his review on its PR stays off; ZOM-295's closing "
                     "note says 'merged with match3d#271' and Blake's inline comment there starts with 'not tiers'"),
        "discovery_order": "the card is read first; ZOM-295's closing note names the PR; the mark is an inline review comment"})
if not any(t['id'] == 'T34' for t in M['traps']):
    M['traps'].append({
        "id": "T34", "family": "exact_predicate", "services": ["slack", "linear"],
        "seeded_ids": [ROBERT], "base_pointers": ["ZOM-200", "ZOM-274", "ZOM-282"],
        "requirement": "R10",
        "expected_wrong_reading": ("writes the UTC date from Linear's completed_at: 2025-06-13 for ZOM-200 and 2025-06-21 "
                                   "for ZOM-274 and ZOM-282"),
        "resolver": ("Robert asks for the day it got marked done in pacific time; completed_at 01:17Z on those three is the "
                     "evening before in Pacific time")})
t32 = by_id(M['traps'], 'T32')
t32['base_pointers'] = [p if p != 'ZOM-295' else 'ZOM-200' for p in t32['base_pointers']]

if not any(c['id'] == 'C16' for c in M['chains']):
    M['chains'].append({"id": "C16", "root_cause": "A3", "ends_in": "R1", "hops": [
        {"service": "trello", "record": CARD, "finding": "rule 1: a title match Blake marked 'not tiers' in his review on its PR stays off"},
        {"service": "linear", "record": "ZOM-295", "finding": "closing note: merged with match3d#271"},
        {"service": "github", "record": PR, "finding": "Blake's approval has an empty body; its inline comment on MonsterSpawner.cs says 'not tiers'"}]})

for b in M['call_budget']:
    if b.get('service') == 'github' and b.get('phase') == 'discovery' and "Blake's inline note on #265" in b['reason']:
        b['reason'] = b['reason'].replace("(Blake's inline note on #265)", "(Blake's inline notes on #265 and #271)")

for w in M['writes']:
    if w['service'] in ('gsheets', 'slack'):
        w['depends_on'] = sorted(set(w['depends_on']) | {'K20', 'T33'})
    if w['service'] == 'gsheets':
        w['depends_on'] = sorted(set(w['depends_on']) | {'T34'})

if not any(e.get('record_id') == REV for e in M.get('integration_exceptions', [])):
    pass  # approval and comment are mirrored in C093LEZGF6J (base_check INT-01), no exception needed

DD = M['design_delta']
if not any(d.get('id') == 'R7-K20' for d in DD):
    DD.append({"id": "R7-K20", "change": f"Blake's 'not tiers' inline review comment on {PR} (ZOM-295 off: 23 tickets, 15 Live); Robert's done day in pacific time",
               "reason": ("hardening round 7: replay over 15 runs; #271 inline comments were fetched by 5 of 15, every run wrote the UTC day; "
                          "two levers on different carriers so failing runs split")})
json.dump(M, open(sys.argv[2], 'w'), indent=2, ensure_ascii=False)
print('ok', len(M['traps']), 'traps', len(M['chains']), 'chains')
