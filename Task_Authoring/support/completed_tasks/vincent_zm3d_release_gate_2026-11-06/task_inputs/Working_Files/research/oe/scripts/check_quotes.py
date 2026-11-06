"""Check every double-quoted span in 08_Oracle_Events.md against the SQL overlay text and the base records it cites."""
import json, glob, re, sys
ROOT = '/Users/sumitkumar/Source/Outlier/OC'
OS_ = ROOT + '/Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/'
oe = open(ROOT + '/Task_Authoring/task_inputs/08_Oracle_Events.md').read()
sql = open(ROOT + '/Task_Authoring/task_inputs/01_Universe_Inject.sql').read().replace("''", "'")
corpus = [sql]
def jtext(o):
    if isinstance(o, dict): return ' '.join(jtext(v) for v in o.values())
    if isinstance(o, list): return ' '.join(jtext(v) for v in o)
    return str(o)
for f in ['slack/messages/C05433XK267/2025-09.json', 'slack/messages/C05433XK267/2025-10.json']:
    for m in json.load(open(OS_ + f)):
        corpus.append((m.get('text') or '') + '\n' + '\n'.join((a.get('fallback') or '') + '\n' + (a.get('text') or '') for a in (m.get('attachments') or [])))
for f in glob.glob(OS_ + 'slack/messages/D079SNE2TL4/*.json'):
    for m in json.load(open(f)): corpus.append(m.get('text') or '')
conf = json.load(open(OS_ + 'confluence/confluence_working.json'))
for pg in conf['pages']:
    if pg['id'] in ('page_qa_runbook', 'page_release_checklist'):
        b = re.sub(r'<[^>]+>', '', pg['body']); corpus.append(pg['title'] + '\n' + b)
lin = json.load(open(OS_ + 'linear/data.json'))
for i in lin['issues']: corpus.append((i.get('title') or '') + '\n' + (i.get('description') or ''))
blob = '\n'.join(corpus)
spans = re.findall(r'"([^"]+)"', oe)
bad = [q for q in spans if q not in blob]
print(f'{len(spans)} quoted spans, {len(bad)} not found verbatim')
for q in bad: print('  MISSING:', q[:160])
