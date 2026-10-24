#!/usr/bin/env python3
"""Compact, complete views of canonical workflow, schemas and source locations."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

import hg_context

ROOT = Path(__file__).resolve().parents[2]
COMMON = [
    '0. Read the local universe', 'Stage input contract', 'Save and reuse supplied inputs',
    '2. Load authority and identify conflicts', 'Stage ownership and evidence reuse',
    '4. Audit versus author', '5. Save an evidence-bearing report',
    '6. Invalidate downstream evidence after edits',
]
TASK = ['Required prompt assignment', 'Reference files used by the prompt',
        'Output capability and failure attribution', 'Task requirement authority']


def sections(text):
    """Locate real Markdown headings, ignoring headings inside fenced examples."""
    rows = text.splitlines(keepends=True)
    headings = []
    fence = None
    for i, line in enumerate(rows):
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if match:
            marker = match[1]
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence):
                fence = None
            continue
        if fence is None:
            match = re.match(r'^(#{1,6}) (.+?)\s*$', line)
            if match:
                headings.append((i, len(match[1]), match[2]))
    result = {}
    for n, (start, level, title) in enumerate(headings):
        end = next((i for i, depth, _ in headings[n + 1:] if depth <= level), len(rows))
        if title in result:
            raise ValueError('Duplicate canonical heading: ' + title)
        result[title] = (start, end, ''.join(rows[start:end]))
    return result


def guide(stage):
    path = ROOT / 'Evals/WORKFLOW.md'
    raw = path.read_bytes()
    available = sections(raw.decode())
    names = COMMON + ([] if stage == 'injection' else TASK)
    spans = []
    for name in names:
        if name not in available:
            raise ValueError('Canonical workflow heading changed: ' + name)
        spans.append(available[name])
    # Parent sections carry all descendants, including the full output contract.
    selected = [span for span in spans if not any(
        other != span and other[0] <= span[0] and other[1] >= span[1] for other in spans)]
    selected.sort()
    header = (f'# {stage}: applicable shared workflow\n\n'
              f'Source: Evals/WORKFLOW.md; SHA-256: {hashlib.sha256(raw).hexdigest()}\n\n'
              'The sections below are verbatim, including their nested sections. '
              'Read the selected numbered Eval in full and follow EXECUTION.md for other references. '
              'This view replaces the corresponding WORKFLOW reads and hg_context scoring call; '
              'it does not replace source evidence or the selected Eval. '
              'Conditional contracts inside Task requirement authority include optional SQL.\n\n')
    body = '\n'.join(f'<!-- WORKFLOW.md lines {a + 1}-{b} -->\n{text}' for a, b, text in selected)
    old_root = hg_context.ROOT
    try:
        hg_context.ROOT = ROOT
        scoring = hg_context.context(stage)
    finally:
        hg_context.ROOT = old_root
    return header + body + '\n## Canonical scoring groups\n\n```json\n' + json.dumps(
        scoring, ensure_ascii=False, separators=(',', ':')) + '\n```\n'


def schema(tables):
    path = ROOT / 'Evals/references/schema/injection.json'
    raw = path.read_bytes()
    entries = json.loads(raw)
    selected, found = [], set()
    for entry in entries:
        name = entry.get('table_name', entry.get('name', entry.get('table')))
        aliases = {name, str(entry.get('table_schema')) + '.' + str(name)}
        matched = set(tables) & aliases
        if matched:
            selected.append(entry)
            found.update(matched)
    return {'source': str(path.relative_to(ROOT)), 'source_sha256': hashlib.sha256(raw).hexdigest(),
            'limits': 'Unverified backing-schema snapshot. Missing/mismatched definitions alone are advisory, '
                      'not proof of a defect or live compatibility. Apply Eval 0 and schema/README.md.',
            'tables': selected, 'missing_tables': sorted(set(tables) - found),
            'complete_entries': True}


def routes(services):
    path = ROOT / 'Evals/references/source_layout.json'
    data = json.loads(path.read_text())
    universe = json.loads((ROOT / 'Evals/references/universe_manifest.json').read_text())
    selected = services or list(data['services'])
    result = {}
    for service in selected:
        if service not in data['services']:
            raise ValueError('Unknown service: ' + service)
        folder = ROOT / universe['services'][service]['path']
        result[service] = {'directory': str(folder.relative_to(ROOT)),
                           'locations': data['services'][service]}
    return {'services': result, 'scope': 'Navigation map, not a SQL schema or proof of data availability. '
            'Record helpers validate actual arrays and complete scan coverage. '
            'Use hg_search.py files/inventory for unlisted paths; do not guess SQL table names as filenames.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_subparsers(dest='mode', required=True)
    combined = modes.add_parser('guide')
    combined.add_argument('stage', choices=hg_context.GROUPS)
    combined.add_argument('--services', nargs='+', help='Also return complete selected source routes')
    combined.add_argument('--tables', nargs='+', help='Also return complete selected schema entries')
    modes.add_parser('schema').add_argument('tables', nargs='+')
    modes.add_parser('routes').add_argument('services', nargs='*')
    args = parser.parse_args()
    try:
        if args.mode == 'guide':
            output = guide(args.stage)
            for title, value in [('Source routes', routes(args.services) if args.services else None),
                                 ('Schema entries', schema(args.tables) if args.tables else None)]:
                if value is not None:
                    output += '\n## ' + title + '\n\n```json\n' + json.dumps(
                        value, ensure_ascii=False, separators=(',', ':')) + '\n```\n'
            print(output)
        else:
            value = schema(args.tables) if args.mode == 'schema' else routes(args.services)
            print(json.dumps(value, ensure_ascii=False, separators=(',', ':')))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(json.dumps({'error': str(error)}), file=sys.stderr)
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
