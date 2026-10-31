#!/usr/bin/env python3
"""The two bundled universes and the per-task date that selects one.

Every task names its date before anything reads the universe. The answer is
saved as the `universe` input (Task_Authoring/support/local_search/NO_EVAL_TASK_INPUTS/02_Universe_Date.txt). There is
no default: without a saved date, universe reads stop and the question is asked.
"""
import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[4]
INDEX = Path('Task_Authoring/support/local_search/NO_EVAL_TASK_INPUTS/universe/inputs.json')
REFERENCES = Path('Evals/references/universes')
UNIVERSES = {
    'normal': {
        'date': '2026-02-14', 'label': 'Feb 14, 2026 (normal)', 'folder': 'Universe_Normal', 'prefix': 'Normal',
        'clock': datetime(2026, 2, 14, tzinfo=timezone.utc),
        'clock_text': '2026-02-14 00:00 UTC',
        'source': 'hg4-2026-08-31 v37', 'shutdown_rules': True,
    },
    'synthcut': {
        'date': '2025-10-01', 'label': 'Oct 1, 2025 (synth-cut)', 'folder': 'Universe_SynthCut', 'prefix': 'SynthCut',
        # Data is cut at 2025-09-30 23:59:59 PT; the clock is the next PT midnight.
        'clock': datetime(2025, 10, 1, 7, tzinfo=timezone.utc),
        'clock_text': '2025-10-01 00:00 PT (2025-10-01 07:00 UTC)',
        'source': 'hg4-synth-sep30cut v16', 'shutdown_rules': False,
    },
}
QUESTION = 'Which date is this task on: Oct 1, 2025 (synth-cut) or Feb 14, 2026 (normal)?'
ANSWERS = {
    'normal': ('2026-02-14', 'feb 14', 'feb 14 2026', 'february 14', 'february 14 2026', 'normal',
               'feb 14 2026 normal'),
    'synthcut': ('2025-10-01', 'oct 1', 'oct 1 2025', 'october 1', 'october 1 2025',
                 'synth', 'synthcut', 'synth-cut', 'synth cut', 'oct 1 2025 synth-cut'),
}


class UniverseNotSelected(ValueError):
    """No date is saved for this task; ask QUESTION and save the answer first."""


def parse(answer):
    """Map a user's answer to a universe key; anything else is rejected, never guessed."""
    text = re.sub(r'\s+', ' ', re.sub(r'[,.()]', ' ', str(answer))).strip().casefold()
    matches = [key for key, forms in ANSWERS.items() if text in forms]
    if len(matches) != 1:
        raise ValueError('Unrecognized date %r. %s' % (str(answer).strip(), QUESTION))
    return matches[0]


def selected(root=None):
    """Return the saved universe key for this task, or raise UniverseNotSelected."""
    root = Path(root) if root is not None else ROOT
    path = root / INDEX
    entry = {}
    if path.is_file():
        entry = json.loads(path.read_text()).get('inputs', {}).get('universe', {})
    files = entry.get('files', [])
    if entry.get('state') != 'saved' or len(files) != 1:
        raise UniverseNotSelected('No task date is saved. Ask: ' + QUESTION +
                                  ' Then run: python3 Evals/tools/hg_store_input.py universe <answer>')
    saved = root / files[0]['path']
    try:
        raw = saved.read_bytes()
    except OSError:
        raise UniverseNotSelected('The saved task date is missing; ask again: ' + QUESTION)
    if hashlib.sha256(raw).hexdigest() != files[0]['sha256']:
        raise UniverseNotSelected('The saved task date changed outside the input tool; ask again: ' + QUESTION)
    return parse(raw.decode('utf-8'))


def info(root=None, key=None):
    key = key or selected(root)
    return {'key': key, **UNIVERSES[key]}


def references(root=None, key=None):
    """Universe-derived reference folder: routing manifest, layout and indexes."""
    root = Path(root) if root is not None else ROOT
    return root / REFERENCES / (key or selected(root))


def base_folder(key, name):
    """Workspace-relative base folder, e.g. base_folder('normal', 'Gmail')."""
    entry = UNIVERSES[key]
    return '%s/%s_HarmonyGames_%s' % (entry['folder'], entry['prefix'], name)


def manifest_path(root=None, key=None):
    return references(root, key) / 'universe_manifest.json'


def clock(root=None, key=None):
    return info(root, key)['clock']


def report_line(key):
    """The Clock line every new stage report carries in its verdict block."""
    entry = UNIVERSES[key]
    return 'Clock: %s, %s' % (entry['clock_text'], entry['label'])


def check_report_clock(value, root=None):
    """A report's Clock value must name the saved task date."""
    key = selected(root)
    other = [k for k in UNIVERSES if k != key and UNIVERSES[k]['date'] in value]
    if UNIVERSES[key]['date'] not in value or other:
        raise ValueError('Clock line must show the saved task date: ' + report_line(key))
    return key


def describe(key):
    entry = UNIVERSES[key]
    return {'key': key, 'date': entry['date'], 'label': entry['label'],
            'clock': entry['clock_text'], 'universe_folder': entry['folder'],
            'source': entry['source'], 'shutdown_rules_apply': entry['shutdown_rules'],
            'report_line': report_line(key)}


def main():
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('operation', choices=('show', 'list'))
    args = parser.parse_args()
    try:
        result = describe(selected()) if args.operation == 'show' else {
            'question': QUESTION, 'universes': [describe(k) for k in UNIVERSES]}
    except ValueError as error:
        print(json.dumps({'error': str(error), 'question': QUESTION}))
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
