#!/usr/bin/env python3
"""Mechanical rubric checks in code (rubric-flow-v2). Run on the supplied rubric and on every candidate fix.

Never misses what a word list can find, so reviewers do not have to. Prints one JSON finding per hit:
  vague_exemplar      "such as", "e.g." or "for example" in any field (Moderate, Eval 3 §2.7A)
  tool_name           an exact catalog tool identifier or mcp__ name in a title (Agent-Centric FAIL)
  markdown_artifact   markdown links/mailto or backslash-escaped punctuation in any field (non-failing repair)
  schema              blank title/justification/evidence, weight not 1/3/5, category not Outcome/Process
  whitespace          leading/trailing or doubled spaces in a title (non-failing repair)
  prohibition_title   title starts "The Agent does not / never / avoids ..." (Negative Criteria check)
  disguised_negative  "leaves … as found / as is / unchanged / untouched / open / off" or "keeps … off" in a
                      title: run the do-nothing test (Eval 3 §2.9); a row an idle Agent passes fails Negative Criteria
  format_lock         a length, line, sentence or section count in a title ("5 lines", "at most 3",
                      "one sentence per line"): grade it only when the prompt states that count (Eval 3 §2.7)
  anon_token          an anonymized placeholder ([PERSON_NAME_0854]) in any field: the source string; bind it
                      as LITERAL and accept it as shown (rubric_factual_checks.md)
  evidence_no_record  the evidence field names no record (ID, key, path, pointer, email, channel or SQL line)
                      holding the expected value (Eval 3 §2.3 "Cited record")
Usage: hg_rubric_lint.py [rubric.json]   (default: the saved rubric input)
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from hg_rubric_qc import VAGUE  # same pattern the scorer enforces
from hg_rubric_checks import NEGATIVE_ACTION, DISGUISED_NEGATIVE, FORMAT_LOCK
from hg_rubric_facts import ANON_TOKEN

MARKDOWN = re.compile(r'\[[^\]]+\]\((?:https?:|mailto:)[^)]*\)|\\[*_"#\[\]]')
# A cited record: a ticket key or snake_case/prefixed ID, a long hex ID, a path or JSON pointer,
# an email, a #channel or PR number, a Slack ts or a SQL line reference.
RECORD = re.compile(r'[A-Z][A-Z0-9]{1,9}-\d+|\b[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+\b|\b[0-9a-f]{12,}\b'
                    r'|[\w.@-]*/[\w.@-]+/[\w./@-]*|\b[\w-]+\.(?:json|md|sql|csv|cs|py|ts|js|txt|docx?|xlsx?|pdf|pptx?)\b'
                    r'|[\w.+-]+@[\w-]+(?:\.[\w-]+)+|#[\w-]+|\b\d{9,}\.\d+\b|\bSQL\s+L\d+'
                    r'|\b[A-Z][A-Z0-9]{8,}\b|\blines?\s+\d+')


def rows(path):
    if path is None:
        entry = json.loads((ROOT / 'Task_Authoring/support/local_search/NO_EVAL_TASK_INPUTS/inputs.json').read_text())['inputs']['rubric']
        path = ROOT / entry['files'][0]['path']
    data = json.loads(Path(path).read_text(encoding='utf-8'))
    return data if isinstance(data, list) else data.get('criteria', [])


def field(row, name):
    ann = row.get('annotations') or {}
    if name == 'category':
        return row.get('category', ann.get('rubric_category', ''))
    return row.get(name, ann.get(name, ''))


def lint(rubric):
    catalog = ROOT / 'Evals/references/tools/catalog.json'
    tools = {t['name'] for t in json.loads(catalog.read_text())} if catalog.exists() else set()
    out = []
    for n, row in enumerate(rubric, 1):
        title = str(field(row, 'title') or '')
        texts = {k: str(field(row, k) or '') for k in ('title', 'justification', 'evidence')}
        for k, v in texts.items():
            if VAGUE.search(v):
                out.append(dict(row=n, field=k, check='vague_exemplar', severity='Moderate',
                                text=VAGUE.search(v).group(0)))
            if MARKDOWN.search(v):
                out.append(dict(row=n, field=k, check='markdown_artifact', severity='repair',
                                text=MARKDOWN.search(v).group(0)))
            if not v.strip():
                out.append(dict(row=n, field=k, check='schema', severity='gate', text='blank field'))
        hits = sorted(set(re.findall(r'[\w]+', title)) & tools)
        if hits or re.search(r'\bmcp__\w+', title):
            out.append(dict(row=n, field='title', check='tool_name', severity='Major', text=', '.join(hits) or 'mcp__'))
        if row.get('weight') not in (1, 3, 5):
            out.append(dict(row=n, field='weight', check='schema', severity='gate', text=str(row.get('weight'))))
        if str(field(row, 'category') or '') not in ('Outcome', 'Process'):
            out.append(dict(row=n, field='category', check='schema', severity='gate', text=str(field(row, 'category'))))
        if title != title.strip() or '  ' in title:
            out.append(dict(row=n, field='title', check='whitespace', severity='repair', text='extra spaces'))
        if NEGATIVE_ACTION.match(title.strip()):
            out.append(dict(row=n, field='title', check='prohibition_title', severity='check', text=title[:60]))
        disguised = DISGUISED_NEGATIVE.search(title)
        if disguised:
            out.append(dict(row=n, field='title', check='disguised_negative', severity='check', text=disguised.group()))
        for hit in FORMAT_LOCK.finditer(title):
            out.append(dict(row=n, field='title', check='format_lock', severity='check', text=hit.group()))
        for k, v in texts.items():
            for hit in ANON_TOKEN.finditer(v):
                out.append(dict(row=n, field=k, check='anon_token', severity='check', text=hit.group()))
        if texts['evidence'].strip() and not RECORD.search(texts['evidence']):
            out.append(dict(row=n, field='evidence', check='evidence_no_record', severity='check',
                            text=texts['evidence'][:60]))
    return out


if __name__ == '__main__':
    findings = lint(rows(sys.argv[1] if len(sys.argv) > 1 else None))
    print(json.dumps(dict(findings=findings, count=len(findings)), indent=2, ensure_ascii=False))
