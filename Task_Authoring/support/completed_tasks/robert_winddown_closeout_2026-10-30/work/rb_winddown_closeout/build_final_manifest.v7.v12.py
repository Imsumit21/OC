"""Final manifest = the draft (every id kept) + facts (with home_ids) + design_delta, written to Working_Files."""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
WF = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'task_inputs', 'Working_Files'))
M = json.load(open(os.path.join(HERE, 'minted_ids.json')))
ACC = json.load(open(os.path.join(HERE, 'accounts.json')))
issue = {a['vendor']: a for a in ACC['accounts']}
man = json.load(open(os.path.join(WF, '01_Hardness_Manifest.draft.json')))
G = lambda k: M[k]['robert_message']


def per_record(key, value, kind, home, aliases=None):
    f = {"key": key, "value": value, "kind": kind, "home_ids": [home], "must_appear_in": [home]}
    if aliases:
        f["aliases"] = aliases
    return f


def cmt(vendor, i=0):
    return issue[vendor]['comment_ids'][i]


facts = [
    {"key": "they close the card", "value": "2026-02-20", "kind": "date", "must_appear_in": [M['T_SVB']['id']]},
    {"key": "one of our personal cards", "value": "2026-02-19", "kind": "date", "must_appear_in": [M['T_SVB']['id']]},
    per_record("Figma Professional (annual)", "2026-09-11", "date", G('G_FIGMA')),
    per_record("Pond5 Annual Membership", "2026-03-02", "date", G('G_POND5')),
    per_record("Layer Pro", "2026-02-25", "date", G('G_LAYER')),
    per_record("Linear Basic (annual)", "2027-02-01", "date", G('G_LINEAR')),
    per_record("cancelled zapier yesterday", "73.50", "amount", cmt('Zapier', 1)),
    per_record("the subscription itself is untouched", "3852", "amount", cmt('Carta')),
    per_record("docusign goes to robert", "300", "amount", cmt('Docusign')),
]
man['facts'] = facts
man['design_delta'] = []
json.dump(man, open(os.path.join(WF, '01_Hardness_Manifest.json'), 'w'), indent=1, ensure_ascii=False)
print('final manifest', len(facts), 'facts')
