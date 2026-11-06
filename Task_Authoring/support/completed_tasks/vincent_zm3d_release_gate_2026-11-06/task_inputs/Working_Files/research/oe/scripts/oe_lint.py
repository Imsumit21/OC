"""Lint 08_Oracle_Events.md the way /oe's validator reads it: quoted spans verbatim in a record,
absence cue words on Expected lines, and every Expected-line value token present in some record
(tokens absent from every record need a recorded calculation or are not_a_claim)."""
import json, glob, re, sys, html
ROOT = '/Users/sumitkumar/Source/Outlier/OC'
OS_ = ROOT + '/Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/'
oe = open(ROOT + '/Task_Authoring/task_inputs/08_Oracle_Events.md', encoding='utf-8').read()
sql = open(ROOT + '/Task_Authoring/task_inputs/01_Universe_Inject.sql', encoding='utf-8').read().replace("''", "'")
corpus = [sql]
def jt(o):
    if isinstance(o, dict): return '\n'.join(jt(v) for v in o.values())
    if isinstance(o, list): return '\n'.join(jt(v) for v in o)
    return str(o)
for f in glob.glob(OS_ + 'slack/messages/C05433XK267/*.json') + glob.glob(OS_ + 'slack/messages/D079SNE2TL4/*.json') + glob.glob(OS_ + 'slack/messages/C08R27X0EAH/2025-09.json'):
    corpus.append(jt(json.load(open(f))))
conf = json.load(open(OS_ + 'confluence/confluence_working.json'))
for pg in conf['pages']:
    if pg['id'] in ('page_qa_runbook', 'page_release_checklist', 'page_cicd_pipeline'):
        corpus.append(pg['title'] + '\n' + pg['body'])
lin = json.load(open(OS_ + 'linear/data.json'))
corpus.append(jt(lin['issues'])); corpus.append(jt(lin['users'])); corpus.append(jt(lin['teams']))
blob = '\n'.join(corpus)
# 1 quoted spans
spans = re.findall(r'"([^"]+)"', oe)
bad = [q for q in spans if q not in blob]
print(f'[quotes] {len(spans)} quoted spans, {len(bad)} not verbatim in a record:')
for q in bad: print('   -', q[:150])
# 2 expected spans / absence cues / tokens (regexes copied from Evals/tools/hg_oe_review.py)
EXPECTED_CUE = re.compile(r'\bExpected(?:[ \t]+(?:data|results?|outputs?|values?))?[ \t]*:|\b(?:the[ \t]+)?agent[ \t]+finds\b', re.I)
EXPECTED_END = re.compile(r'\n[ \t]*\n|\n(?=[ \t]*(?:#{1,6}[ \t]|OE[ \t]*\d|Step[ \t]*\d))', re.I)
OE_REFERENCE = re.compile(r'\bOEs?[ \t]*\d+(?:[ \t]*(?:[-–+,&]|and|to|or)[ \t]*(?:OEs?[ \t]*)?\d+)*', re.I)
LITERAL_VALUES = tuple(re.compile(p) for p in (r'`[^`\n]+`', r'[\w.+-]+@[\w-]+(?:\.[\w-]+)+', r'(?<![\w.-])[A-Za-z0-9]+(?:_[A-Za-z0-9]+)+(?!\w)',
    r'\b[A-Z][A-Z0-9]{1,9}-\d{1,6}\b', r'\b(?=[A-Z0-9]*\d)(?=[A-Z0-9]*[A-Z])[A-Z0-9]{9,12}\b', r'\b(?=[0-9a-f]*\d)(?=[0-9a-f]*[a-f])[0-9a-f]{7,40}\b',
    r'(?<![\w.])\d{10,}(?:\.\d+)?(?![\w.])', r'(?<![\w.])\d+\.\d+\.\d+(?:\.\d+)?(?![\w.])', r'(?<![\w#])#[a-z][a-z0-9_-]{2,}\b'))
FIGURE_VALUES = tuple(re.compile(p) for p in (r'\$[ \t]?\d[\d,]*(?:\.\d+)?', r'\b\d[\d,]*(?:\.\d+)?[ \t]?%', r'\b\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?Z?)?',
    r'\b\d{1,2}:\d{2}(?::\d{2})?(?!\d)', r'(?<![\w#])#\d{1,6}\b', r'(?<![\w.,:$#])\d[\d,]*(?:\.\d+)?(?![\w%:]|[.,]\d)'))
ABSENCE_CUE = re.compile(r"\b(?:none|nothing|nobody|no[ \t]+one|nowhere|never|absent|missing|not[ \t]+found|"
                         r"no[ \t]+(?:other|such|later|further|newer|known|records?|fix(?:es)?|commits?|follow-ups?|"
                         r"repl(?:y|ies)|response|evidence|trace|mention)|do(?:es)?[ \t]+not[ \t]+exist|"
                         r"do(?:es)?n't[ \t]+exist|no[ \t]+longer[ \t]+exists?)\b", re.I)
def spans_of(raw):
    out = []
    for cue in EXPECTED_CUE.finditer(raw):
        stop = len(raw)
        for p in (EXPECTED_END, EXPECTED_CUE):
            f = p.search(raw, cue.end())
            if f: stop = min(stop, f.start())
        out.append((cue.end(), stop))
    return out
flat = blob.replace(',', '')
def lit_ok(tok):
    v = tok.strip('`'); v = v[1:] if v.startswith('#') else v
    return v in blob
def fig_ok(tok):
    v = re.sub(r'[\s$,%#]', '', tok).rstrip('Z')
    return re.search(r'(?<!\d)' + re.escape(v) + r'(?!\d)', flat) is not None
nabs = 0; unfound = []
for a, b in spans_of(oe):
    step = re.findall(r'OE (\d+)', oe[:a])[-1]
    taken = [m.span() for m in OE_REFERENCE.finditer(oe, a, b)]
    for kind, pats in (('L', LITERAL_VALUES), ('F', FIGURE_VALUES)):
        for p in pats:
            for m in p.finditer(oe, a, b):
                if any(m.start() < y and x < m.end() for x, y in taken): continue
                taken.append(m.span())
                ok = lit_ok(m.group(0)) if kind == 'L' else fig_ok(m.group(0))
                if not ok: unfound.append((step, kind, m.group(0)))
    for m in ABSENCE_CUE.finditer(oe, a, b):
        nabs += 1; print(f'[absence] OE {step}: "{m.group(0)}" …{oe[max(a,m.start()-50):m.end()+30]!r}')
print(f'[absence] {nabs} absence cue(s) on Expected lines')
print(f'[tokens] {len(unfound)} Expected-line tokens absent from every record (need calculation / not_a_claim):')
for s, k, t in unfound: print(f'   OE {s} {k} {t}')
n_ev = len(re.findall(r'^\s*(?:#+\s*)?(?:\*\*)?OE\s*\d+', oe, re.M))
print(f'[shape] events {n_ev} · characters {len(oe)} · arrows {oe.count("->")} · json {oe.count("{")}')
