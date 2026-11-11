"""Re-bind 00_V3_Authoring_Evidence.json to the refreshed context and the rev7 scenario design (role review)."""
import json, pathlib, sys
sys.path.insert(0, 'Task_Authoring/tools')
import stage_gate as sg
TI = pathlib.Path('Task_Authoring/task_inputs'); WF = TI / 'Working_Files'
p = WF / '00_V3_Authoring_Evidence.json'
d = json.loads(p.read_text(encoding='utf-8'))
ctx = json.loads((WF / '00_Task_Context.json').read_text(encoding='utf-8'))
d['context_hash'] = ctx['context_hash']
r = d['role_reviews']['scenario']
r['artifact_hash'] = sg.file_digest(WF / '01_Scenario_Design.md')
if 'rev7' not in r['rationale']:
    r['rationale'] += (" rev7 re-review (2026-11-08): the de-signposted ask still names only deliverables a PM owns; "
                       "joining players to her own gift-code contacts, ticketing a late form per her log note, and quoting "
                       "Vincent's corrected retention scope are ordinary PM read work. Observer swap (Victor Barnes left in "
                       "April 2025) keeps every session with an active employee.")
for sid in ('C090N54TG79/1759266627.418203', 'f_c691d577b8f837eb4f9eaa'):
    if sid not in r['source_ids']:
        r['source_ids'].append(sid)
p.write_text(json.dumps(d, ensure_ascii=False, indent=1) + '\n', encoding='utf-8')
print(r['artifact_hash'], d['context_hash'][:12])
