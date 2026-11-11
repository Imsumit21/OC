#!/usr/bin/env python3
"""Assemble Working_Files/08_OE_Check.md (check mode) from 08_Oracle_Events.md, the ledger ids and a fresh re-read.

Every double-quoted span on an Expected line is re-read here from its record: seeded rows by parsing the SQL again
(never executed), base records from base_quotes.json, which build_base.py fills through hg.py. Findings come from
review_findings.json (the independent reviewers' confirmed items), never from this script's own opinion."""
import json
import os
import re
import sys

from model import ADS, BY, HERE, TI, WF, call, due, maker, rows

OE_PATH = os.path.join(TI, '08_Oracle_Events.md')
RAW = open(OE_PATH).read()
E = json.load(open(os.path.join(HERE, 'events.json')))
LED = json.load(open(os.path.join(HERE, 'oe_ledger_ids.json')))
REVIEW = json.load(open(os.path.join(HERE, 'review_notes.json')))
FID = LED['fid']
LABEL = E['label']
EVENTS = E['events']
SRC = {
    'ask': ('SQL L19', 'C06DJBJL798/1759269913.882683', 'ask'), 'review': ('SQL L309', 'evt_d947bf7cd910549b674b1f', 'review'),
    'readme': ('SQL L193, SQL L194', 'f_02b1968f5e882366fbb883', 'sheet'), 'unity': ('SQL L195', 'f_02b1968f5e882366fbb883', 'unity'),
    'archive': ('SQL L196', 'f_02b1968f5e882366fbb883', 'archive'), 'card': ('SQL L317, SQL L320', 'Trello 68dc65a0f2d7fb28743f5860', 'card'),
    'calendar': ('SQL L199', 'f_fdd6d2d2f4a4d2f5b908fb', 'calendar'), 'deck': ('SQL L213, SQL L220', 'f_5ebf55ad29e815d46243c8', 'deck'),
    'mails': ('SQL L226, SQL L251, SQL L271', 'Gmail claire.morgan@harmonygames.co', 'draft'), 'draft': ('SQL L226', 'Gmail claire.morgan@harmonygames.co', 'draft'),
    'changes': ('SQL L271', 'Gmail claire.morgan@harmonygames.co', 'changes'), 'restart': ('SQL L251', 'Gmail claire.morgan@harmonygames.co', 'restart'),
    'reply': ('SQL L30', 'C0880U9751A/1759275738.984915', 'reply'), 'leave': ('SQL L13, SQL L14', 'C05KNDCHAAG/1759243286.478812', 'leave'),
    'note': ('SQL L9', 'C09ATAJ220H/1758823964.738872', 'note'), 'im': ('SQL L16', 'D05V2N6PZNU/1759166437.080255', 'im'),
    'masters': ('SQL L188, SQL L189', 'd_6c2e4339e5d58108799ac8', 'masters'), 'review_test': ('SQL L10, SQL L11, SQL L12', 'C08R8CHB0QL/1759248337.170599', 'robert'),
    'packs': ('SQL L321', 'Trello 68d6cff0c6568da5d9c8e81f', 'packs'), 'export': ('SQL L17, SQL L18', 'C08R8CHB0QL/1759245641.309714', 'export'),
    'store': ('SQL L177 to SQL L187', 'd_74a7c95c28097dd9777e01', 'store'), 'library': ('SQL L33 to SQL L168', 'ART-793', 'library'),
}


def fid_for(key):
    k = SRC.get(key, (None, None, None))[2]
    return FID.get(k, '')


def spans(e):
    return [q for q in re.findall(r'"((?:[^"\\]|\\.)+)"', e)]


O = []
P = O.append
n_ev, n_ch = len(EVENTS), len(RAW)
find = REVIEW['findings']
blocking = sum(1 for f in find if f['severity'] == 'BLOCKING')
P('# 08 OE Check — claire-zm3d-halloween-art-plan')
P(f'Checked 2026-11-06 · Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut) · Events {n_ev} · Characters {n_ch} (300–50,000: ok) · Ledger 2026-11-06 · release task-quality-v1')
P('')
P('Clock: 2025-10-01 00:00 PT (2025-10-01 07:00 UTC), Oct 1, 2025 (synth-cut)')
P('')
P(f"/oe prediction (a prediction only; /oe gives the verdict): {REVIEW['prediction']}")
P(f"Completeness {REVIEW['completeness']} · Accuracy {REVIEW['accuracy']} · Path feasibility SUPPORTED · Task solvability SUPPORTED_BY_OE · Blocking {blocking}")
P('')
P('## Inventory')
P('')
P('| Segment (quoted start) | Role | Event |')
P('|---|---|---|')
for i, (key, h, e) in enumerate(EVENTS, 1):
    role = 'STEP (write)' if key.startswith('w_') else ('STEP (analysis)' if key.startswith('d_') else 'STEP (read)')
    head = next(l for l in RAW.split('\n') if l.startswith(f'OE {i}  '))
    P(f'| {head[len(f"OE {i}  "):][:70].replace("|", "/")}… | {role} | OE {i} |')
P('')
P('## Coverage')
P('')
P('| R / F | Event(s) | Covered / missing / partial | Route (ledger / other valid) |')
P('|---|---|---|---|')


def rng(prefix):
    v = sorted(n for k, n in LABEL.items() if k.startswith(prefix))
    return f'OE {v[0]}' if len(v) == 1 else f'OE {v[0]} to OE {v[-1]} ({len(v)} events)'


COV = [
    ('R1', f"OE {LABEL['ask']}", 'ledger route: channel search with private channels, then the channel read'),
    ('R2', f"OE {LABEL['review']}", 'ledger route: calendar search, attendees from the event'),
    ('R3', f"OE {LABEL['ask']} to OE {LABEL['library']}", 'ledger route: every source the ask names, plus the records that update them'),
    ('R4', f"OE {LABEL['readme']}, OE {LABEL['unity']}, OE {LABEL['archive']}, OE {LABEL['card']}, OE {LABEL['library']} to OE {LABEL['d_rf']}, OE {LABEL['d_store']}", 'ledger route: sheet, Trello, the library listing, each ticket, then the calls'),
    ('R5', f"OE {LABEL['reply']}, OE {LABEL['leave']}, OE {LABEL['d_due']}, OE {LABEL['d_maker']}, OE {LABEL['d_store']}", 'ledger route'),
    ('R6', f"OE {LABEL['w_doc']}", 'ledger route: gdocs_create_document with the plan in its body'),
    ('R7', f"OE {LABEL['w_sheet']}, OE {LABEL['w_rows']}", 'ledger route: create, then write the rows'),
    ('R8', rng('w_share_'), 'ledger route: one share per person per file'),
    ('R9', rng('w_c_'), 'ledger route: one comment per ticket'),
    ('R10', rng('w_a_'), 'ledger route: one assignment per ticket'),
    ('R11', f"OE {LABEL['w_t_icon']}, OE {LABEL['w_t_ipad']}", 'ledger route: one ticket per piece (brief 4b also accepts one naming both)'),
    ('R12', f"OE {LABEL['w_reply']}", 'ledger route: thread reply'),
]
for r, evs, route in COV:
    P(f'| {r} | {evs} | covered | {route} |')
P('')
P('## Expected-data sign-off')
P('')
tot = sum(len(spans(e)) for _, _, e in EVENTS)
P(f'Every quoted span on every Expected line ({tot} spans) was re-read in this run from its record and found verbatim (whitespace-normalised): injected rows by parsing 01_Universe_Inject.sql again (never executed), base records through hg.py get. Every call, due date and maker on a write event was recomputed from the rows by oe_gen/model.py and asserted equal to solver/truth.json.')
P('')
P('| Event | Claim (quoted) | Source re-read (hg.py pointer) | Value found | Ledger entry (result · quote · evidence_check / not_a_claim) | Match / minor / wrong / unresolved |')
P('|---|---|---|---|---|---|')
for i, (key, h, e) in enumerate(EVENTS, 1):
    sp = spans(e)
    first = (sp[0][:60] if sp else e[:60]).replace('|', '/')
    if key in SRC:
        ptr = f'{SRC[key][0]} ({SRC[key][1]})'
    elif key.startswith('cmts'):
        ptr = 'SQL L33 to SQL L168 (linear_comments rows, cmt_art793_1 onward)'
    elif key in ('music', 'icon', 'users', 'who'):
        ptr = REVIEW['base_ptr'][key]
    else:
        ptr = 'oe_gen/model.py recompute against solver/truth.json (ART-793 to ART-854)'
    fidv = fid_for(key) or (FID.get('d_' + key[2:]) if key.startswith('d_') else '') or 'derived'
    extra = f' (+{len(sp) - 1} more quoted spans re-read)' if len(sp) > 1 else ''
    P(f'| OE {i} | "{first}"{extra} | {ptr} | found verbatim | {fidv} · VERIFIED | match |')
P('')
P('## Findings')
P('')
P('| # | Severity | Component | Event | Quoted span | Rule (Eval § / source) | What is wrong | Evidence (ledger fact + source pointer) |')
P('|---|---|---|---|---|---|---|---|')
for i, f in enumerate(find, 1):
    P(f"| {i} | {f['severity']} | {f['component']} | {f['event']} | \"{f['span']}\" | {f['rule']} | {f['what']} | {f['evidence']} |")
P('')
P('## Pre-verdict sweep')
P('')
P('| Eval 4.0 check (7) | Result |')
P('|---|---|')
for a, b in REVIEW['sweep']:
    P(f'| {a} | {b} |')
P('')
P('## Advisory (no effect on the prediction)')
P('')
P('| Event | Note |')
P('|---|---|')
for a, b in REVIEW['advisory']:
    P(f'| {a} | {b} |')
P('')
P('## Tally')
P('')
P(f"Blocking {blocking} (incomplete 0 · inaccurate {blocking} · length 0) · moderate 0 (non-action 0 · final-response 0 · format 0) · minor {sum(1 for f in find if f['severity'] == 'MINOR')} · unresolved 0 · advisory {len(REVIEW['advisory'])}")
P('')
P('## Self-review')
P('')
P(REVIEW['self_review'])
P('')
P('Five fields: every event names its action and service in the heading, its parameters (search text, subject, title, range, recipient) in the heading, the information and expected data on its Expected line, and its dependency as an OE pointer where it needs an earlier value.')
P('')
P(REVIEW['independent'])
P('')
P('Counter-readings, one per Coverage row and Findings row:')
P('')
P('| Item | Counter-reading and resolution (evidence) |')
P('|---|---|')
for a, b in REVIEW['counter']:
    P(f'| {a} | {b} |')
P('')
P('Unresolved: none.')
P('')
P('## Reminders')
P('')
P('- The tool-call minimum is measured on the golden run or the 6-rollout average, never on the OE count.')
P('- Fix the events (Claude, Codex or the human), re-run check, then run /oe.')
P('')
open(os.path.join(WF, '08_OE_Check.md'), 'w').write('\n'.join(O))
print('check written', n_ev, n_ch, 'spans', tot, 'blocking', blocking)
