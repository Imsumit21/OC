"""rev7 final-manifest bookkeeping: facts, design_delta, solver/surface digests. Run from the workspace root."""
import hashlib, json, pathlib
WF = pathlib.Path('Task_Authoring/task_inputs/Working_Files')
P = WF / '01_Hardness_Manifest.json'
m = json.loads(P.read_text(encoding='utf-8'))
facts = {f['key']: f for f in m['facts']}
nb = facts['non-store build']
for d in ('f_41675dd5d215cf647b240e', 'f_e055f907c7c1359b39bec5', 'f_ba6a734ddf36318e9bb3f3'):
    if d not in nb['home_ids']:
        nb['home_ids'].append(d)
dv = facts['device of ZOM-588']
if 'f_cadae9f611d82d56ac02c3' not in dv['home_ids']:
    dv['home_ids'].append('f_cadae9f611d82d56ac02c3')
new = [
    {"key": "job of Alper Koçak", "value": "QA tester, console games publisher", "kind": "status", "home_ids": ["038b5eb5a30326895cb54756"]},
    {"key": "job of Arda Keskin", "value": "Live ops producer, mobile games studio", "kind": "status", "home_ids": ["0810fb8287e489c125fe2cd9"]},
    {"key": "retention cut-off", "value": "2025-07-24", "kind": "date", "home_ids": ["f_4e21b203a62910bdae0353"]},
]
for f in new:
    if f['key'] not in facts:
        m['facts'].append(f)
DELTA = [
    ("C090N54TG79/1759266627.418203", "ask text: the rule index, the panel and retention pointers and 'Robert already told you' removed; asks only", "01a §9 de-signposting"),
    ("f_748d26e760e54651eaa0d8", "gate Doc: 'A closed ticket isn't a pass.' and the Sep 30 update line removed; Passes line now 'A pass is a clean test run of the build players get. Arthur Blake owns the Vision Bot job and says what its passes do and don't cover.'", "01a §9"),
    ("cmt_38b3cc50dceda37f40f5", "ZOM-567 comment: no 'no Samsung phone', no device-gate claim", "K3 decoy no longer contradicts the matrix"),
    ("ba19de7863a540175f2aeadc12916fa6", "Leonard's relation rule id re-derived from 676eb4bb7c6fde75e63edf27ad453971 to sha256('C090N54TG79|1758818538.552913')[:32]", "base_check Check A Slack id contract"),
    ("F-QA, F-PLAYERS, F-LATE, F-RETCUT", "fragments added; F-AGE, F-INDUSTRY, F-GATE, F-RERUN re-chained through the note A1; F-STATE, F-PANEL, F-PANELDEF, F-RET through the roadmap card", "the ask no longer delegates by index"),
    ("T-G, T-T, CH-G", "traps and chain added; T-K3, T-RET, T-K5, T-F, T-559, T-S23 restated for the rev7 truth", "S0r rebuilds 01a §10"),
    ("3dd0b6d6c52c21cd5bbfcd6d6f5345cd, 3d8e451a198d5d59b39e60064b590305, f_cadae9f611d82d56ac02c3", "Vincent's #zombie-bugs QA matrix post, reply and sheet added (SM-A546E row PASS)", "R_K3 two-sided"),
    ("contacts.contacts (82 rows)", "the players added to Julia's contacts on Sep 22; two games jobs (038b5eb5a30326895cb54756, 0810fb8287e489c125fe2cd9), Brian's nine with no job; contact_groups/members not written (not writable)", "R_G"),
    ("julia.lawson@harmonygames.co/<CAab474c9390349b2f96626bafff9ff2c5f9cd@mail.gmail.com>", "Owen's Sep 30 20:40Z late reply with two sessions inline (and his SENT copy)", "R_T"),
    ("f_4e21b203a62910bdae0353", "KPI tab note row added above the header (Vincent, Sep 30); sheet modified 2025-09-30T10:22:41Z", "R_E later correction; the planned ZOM-227 comment was dropped (comment after a closed issue fails Check C)"),
    ("ZOM-628..ZOM-647", "20 more sessions (Douglas 12, Frederick Stone 8) with notes Docs, device comments, Log rows and two form mails", "requester volume ask 400+ calls; routine, governed by existing rules"),
    ("Victor Barnes -> Douglas", "the 12-session batch first drafted under Victor Barnes moved to Douglas (Docs 02-13 in d_cd7849ec043ab3da107f8c); form mail dated Mon 2025-09-29T07:41:17Z", "Victor Barnes left in April 2025 (SC-36, Evals/ENVIRONMENT.md)"),
    ("CHANNELS.delegation:handling", "latent batch -> run", "the ledger record hev_7d1cece325d7815b is on a run basis (01a §1)"),
    ("cohort", "60 -> 82 (80 ticketed + T1, T2); truth 45 counted, casual 27 at 3.8333, RPG 18 at 3.5000, gap 0.3333, HOLD", "solver/truth.json"),
]
have = {d['id'] for d in m.get('design_delta', [])}
for i, ch, why in DELTA:
    if i not in have:
        m['design_delta'].append({"id": i, "change": "rev7: " + ch, "reason": why})
def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()
m['solver']['digest'] = sha(WF / 'solver' / 'solver.py')
m['gradable_surface']['digest'] = sha(WF / '01_Gradable_Surface.json')
m['_note'] = ("Final manifest for rev7 (S0r delta over rev6). planned_records stay in the draft; the changes are in "
              "design_delta. No prompt, Oracle Event or criterion text.")
P.write_text(json.dumps(m, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print('facts', len(m['facts']), 'delta', len(m['design_delta']))
