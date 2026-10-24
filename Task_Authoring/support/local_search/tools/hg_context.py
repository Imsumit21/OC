#!/usr/bin/env python3
"""Read the stage's original scoring groups without loading unrelated groups."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
GROUPS = {
    'injection': ['Authority and Thresholds', 'Injection'],
    'prompt': ['Authority and Thresholds', 'Prompt', 'Universe'],
    'hardness': ['Authority and Thresholds'],
    'golden': ['Authority and Thresholds', 'Prompt', 'Universe'],  # Historical.
    'oe': ['Oracle Events'],
    'rubric': ['Authority and Thresholds', 'Universe', 'Rubric'],
}


def context(stage):
    path = ROOT / 'Evals/references/rules/scoring.json'
    raw = path.read_bytes()
    groups = json.loads(raw)
    selected = [group for group in groups if group['Dimension'] in GROUPS[stage]]
    if {g['Dimension'] for g in selected} != set(GROUPS[stage]):
        raise ValueError('Scoring groups changed; inspect the canonical reference before proceeding')
    return {
        'workspace': str(ROOT), 'stage': stage,
        'helpers': {name: str(ROOT / 'Evals/tools' / name) for name in
                    ['hg_store_input.py', 'hg_search.py', 'hg_write_output.py']},
        'source': str(path.relative_to(ROOT)),
        'source_sha256': hashlib.sha256(raw).hexdigest(),
        'scoring_groups': selected,
        'omitted_groups': [g['Dimension'] for g in groups if g not in selected],
        'interpretation': 'Original groups, not a new score calculation. Apply the selected numbered Eval and its explicit scope/overrides; included definitions do not create extra gates.',
        'hardness_note': 'Hardness uses model-aware-v3. Select by actual run model and read only one eval: Opus -> Evals/1A_Hardness_Eval.md (OPUS_OBSERVED); Haiku -> Evals/1B_Haiku_Prediction_Eval.md (HAIKU_TO_OPUS). Explicit run selection wins; otherwise prefer Opus. Keep actual provenance, exclude task/environment defects, and follow the scoring/report contract in the selected eval.' if stage == 'hardness' else None,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('stage', choices=GROUPS)
    args = parser.parse_args()
    print(json.dumps(context(args.stage), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
