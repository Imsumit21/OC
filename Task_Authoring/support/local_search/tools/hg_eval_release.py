"""Verify the installed prompt/rubric release and separate historical audit results."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
MANIFEST = Path('Evals/references/prompt_rubric_release.json')
RELEASE = 'task-quality-v1'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def snapshot(stage, root=None):
    root = Path(root) if root is not None else ROOT
    if stage not in {'prompt', 'rubric', 'oe'}:
        raise ValueError('Release binding applies to prompt, rubric and OE')
    path = root / MANIFEST
    if not path.is_file():
        raise ValueError('Missing prompt/rubric release manifest; use the complete current installed package')
    record = json.loads(path.read_text())
    if record.get('release') != RELEASE or not record.get('files'):
        raise ValueError('Unsupported or empty eval release manifest')
    for name, expected in record['files'].items():
        file = (root / name).resolve()
        if not file.is_relative_to(root.resolve()) or not file.is_file() or sha(file) != expected:
            raise ValueError('Eval package changed or incomplete: ' + name + '; reinstall/rebuild the approved release')
    return dict(version=RELEASE, manifest_sha256=sha(path), stage=stage)


def require_binding(record, stage):
    current = snapshot(stage)
    if record.get('eval_release') != current:
        raise ValueError('Review record needs the current eval_release fingerprint; old audits cannot be relabeled current')
    return current


def report_binding(parsed, current):
    if parsed.get('eval_version') != current['version'] or parsed.get('eval_release_sha256') != current['manifest_sha256']:
        raise ValueError('Report needs matching Eval version and Eval release SHA-256')
    return dict(eval_version=current['version'], eval_release_sha256=current['manifest_sha256'])


def classify_report(path, stage):
    """Version/matching-record inventory, not a fresh semantic/source re-audit."""
    from hg_report_contract import parse_result
    current = snapshot(stage)
    result = dict(path=str(path), classification='HISTORICAL_OR_UNBOUND')
    try:
        parsed = parse_result(stage, path.read_text())
        result.update(verdict=parsed['verdict'], score=parsed['verdict_score'], status=parsed['execution_status'])
        if parsed.get('eval_version') != current['version'] or parsed.get('eval_release_sha256') != current['manifest_sha256']:
            return result
        filename, hash_key = ('rubric_score_record.json', 'scoring_record_sha256') if stage == 'rubric' else ('prompt_check_record.json', 'prompt_record_sha256')
        if stage == 'oe':
            filename, hash_key = 'oe_review_record.json', 'oe_record_sha256'
        record_path = path.parent / 'drafts' / filename
        record = json.loads(record_path.read_text())
        if sha(record_path) != parsed.get(hash_key) or record.get('eval_release') != current:
            result['classification'] = 'INVALID_BINDING'
            return result
        required = {'checks', 'weight_reviews', 'oe_cross_check', 'reviewed_json_sha256', 'review_context_sha256'} if stage == 'rubric' else {'premises', 'sources', 'unique_ground_truth', 'reviewed_prompt_sha256', 'review_context_sha256'}
        if stage == 'oe':
            required = {'steps', 'coverage', 'segments', 'sources', 'path_review', 'expected_values', 'reviewed_oe_sha256', 'review_context_sha256'}
        if record.get('format_version') != {'rubric': 5, 'oe': 2, 'prompt': 2}[stage] or not required <= record.keys():
            result['classification'] = 'INVALID_BINDING'
            return result
        if stage == 'prompt':
            from hg_prompt_ugt import validate_report
            if not isinstance(record['unique_ground_truth'], dict):
                raise ValueError('Missing structured Unique Ground Truth review')
            # Check the displayed outcome against its ledger without claiming
            # a fresh task/source audit or reusing the report as evidence.
            validate_report(record['unique_ground_truth'],
                            {source['id']: source for source in record['sources']}, path.read_text())
        result['classification'] = 'CURRENT_RELEASE'
        # Fresh input/source correctness is deliberately not claimed by this index.
        result['evidence_revalidated'] = False
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
        result.update(classification='INVALID_OR_UNREADABLE', reason=str(error))
    return result


def summarize(paths, stage):
    items = [classify_report(Path(p), stage) for p in dict.fromkeys(map(str, paths))]
    bands = {}
    for item in items:
        bucket = bands.setdefault(item['classification'], dict(total=0, complete=0, passing=0))
        bucket['total'] += 1
        if item.get('status') == 'COMPLETE':
            bucket['complete'] += 1
            bucket['passing'] += item.get('verdict') in {'PASS', 'NON-FAIL'}
    return dict(stage=stage, release=snapshot(stage), groups=bands, items=items,
                limits='Version/binding inventory. Pass rate is not evaluator precision; no confusion matrix or fresh source audit is implied.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=('snapshot', 'summarize'))
    parser.add_argument('stage', choices=('prompt', 'rubric', 'oe'))
    parser.add_argument('reports', nargs='*', type=Path)
    args = parser.parse_args()
    try:
        result = snapshot(args.stage) if args.operation == 'snapshot' else summarize(args.reports, args.stage)
    except (OSError, ValueError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
