#!/usr/bin/env python3
"""Generate Mode B diagnosis from current, bound raw exports without rewriting them.

The report is a proposal for the owning stage, never permission to mutate an
artifact. One precheck is explicitly provisional. Baseline patterns and scoring
are delegated to the existing calculator, including its transitive grouping.
"""
from __future__ import annotations
import copy
import hashlib
import json
from pathlib import Path
import difficulty_stats as stats
from design_readiness import evidence_ok, digest

REPAIR_OWNERS = {'universe': 'create-scenario --revise', 'prompt': 'create-prompt-writing',
                'oe': 'create-oe-writing', 'rubric': 'create-rubric-writing'}
OBSERVATIONS = {
    'heavy_all_pass': 'repair meaningful evidence/reasoning; routine volume is not a repair',
    'dominant_pattern': 'inspect shared gateways and independent decisions',
    'transitive_bridge': 'inspect complete outcome coverage; do not cosmetically split criteria',
    'all_fail': 'check fairness, tool readability and grader accuracy first',
    'first_read_correction': 'reassess placement while preserving fair discovery',
    'reviewer_disagreement': 'inspect policy/release and evidence differences first',
}
RERUN_STAGES = {'scenario', 'injection', 'hardening', 'reference-files', 'error-async',
                'prompt-writing', 'prompt-check', 'humantime', 'oe-writing', 'oe-check',
                'rubric-writing', 'rubric-check', 'allfail', 'difficulty', 'release',
                'local-build', 'platform-handoff', 'baseline', 'precheck', 'verifier'}


def scope_difference_ok(scope):
    """A reason class alone is not the before/after scope or volume difference."""
    if not isinstance(scope, dict):
        return False
    count_fields = ('rows_added', 'rows_removed', 'items_added', 'items_removed',
                    'calls_added', 'calls_removed', 'writes_added', 'writes_removed')
    counts = [scope[key] for key in count_fields if key in scope]
    if counts:
        return all(type(value) is int and value >= 0 for value in counts)
    if 'volume_delta' in scope:
        return type(scope['volume_delta']) in (int, float)
    return all(isinstance(scope.get(key), str) and scope[key].strip() for key in ('before', 'after'))


def build(data, *, verifier=None, trajectories, task_id, revision, bundle_hash, receipt=None,
          diagnoses=None, repairs=None, correction_evidence=None, task_dir=None, precheck=False):
    from trajectory_ledger import bind_verifier_exports
    if precheck:
        review = json.loads(Path(receipt).read_text()) if isinstance(receipt, (str, Path)) else receipt
        if (len(trajectories) != 1 or not isinstance(review, dict) or review.get('kind') != 'PRECHECK_EXPORT_REVIEW'
                or review.get('schema_version') != 1 or review.get('task_id') != task_id
                or review.get('revision') != revision or review.get('bundle_hash') != bundle_hash
                or not review.get('reviewer') or not evidence_ok(review, task_dir)):
            raise ValueError('UNBOUND: precheck needs an evidenced task/revision/export review')
        path = Path(trajectories[0])
        if review.get('export_sha256') != hashlib.sha256(path.read_bytes()).hexdigest():
            raise ValueError('UNBOUND: precheck export changed')
        if review.get('source_matrix_sha256') != digest(data):
            raise ValueError('UNBOUND: precheck surface/proxy review is stale')
        binding = {'verdict': 'BOUND', 'runs': {1: path}, 'evidence': review}
    else:
        if verifier is None:
            raise ValueError('UNBOUND: baseline verifier is required')
        binding = bind_verifier_exports(Path(verifier), [Path(p) for p in trajectories], task_id=task_id,
                                        revision=revision, bundle_hash=bundle_hash, receipt=receipt, task_dir=task_dir)
    raw = copy.deepcopy(data)
    blockers = []
    def need(ok, text):
        if not ok:
            blockers.append(text)
    rollouts = raw.get('rollouts', [])
    need(len(rollouts) == (1 if precheck else 6), 'precheck needs one slot; baseline needs exactly six slots')
    parsed = stats.parse_verifier(Path(verifier)) if not precheck else {}
    rubrics = raw.get('rubrics', [])
    by_title = {}
    for row in rubrics:
        by_title.setdefault(stats.norm_title(row.get('title', '')), []).append(row['id'])
    paths = {f'run-{n}': Path(p) for n, p in binding['runs'].items()}
    need(set(paths) == {r['id'] for r in rollouts}, 'bound exports and matrix slots differ')
    for run in rollouts:
        path = paths.get(run['id'])
        if path is None:
            continue
        status, _, detail = stats.read_trajectory(path)
        need(run['status'] == status, run['id'] + ': actual export completion status differs')
        if status != 'completed':
            continue
        actual, used = {}, {}
        for row in parsed.get(int(run['id'].split('-')[-1]), []):
            title = stats.norm_title(row['title'])
            candidates = by_title.get(title, [])
            ix = used.get(title, 0)
            if ix >= len(candidates):
                blockers.append(run['id'] + ': verifier row not in reviewed rubric')
                continue
            actual[candidates[ix]] = row['passed']
            used[title] = ix + 1
        if not precheck:
            need(actual == run.get('results'), run['id'] + ': raw matrix differs from bound verifier')
        need(detail['counted'] == run.get('tool_calls'), run['id'] + ': tool-call count differs from actual export')
        if raw.get('spec_version') == 'V3':
            need(set(run.get('models', [])) == set(stats.trajectory_models(path)), run['id'] + ': model evidence differs from export')
    evidence = correction_evidence or {}
    for row in rubrics:
        if row.get('valid') is False:
            need(evidence_ok(evidence.get('invalid:' + row['id']), task_dir), row['id'] + ': invalidation lacks evidence')
    for run in rollouts:
        need(run.get('status') == 'completed' or not run.get('judge_corrections'), run['id'] + ': errored slot cannot carry score corrections')
        for rid in run.get('judge_corrections', {}):
            need(evidence_ok(evidence.get(run['id'] + ':' + rid), task_dir), run['id'] + ':' + rid + ': correction lacks evidence')
    matrix = []
    for row in rubrics:
        if row.get('weight') != 5:
            continue
        values = []
        for run in rollouts:
            value = run.get('results', {}).get(row['id']) if run['status'] == 'completed' else None
            corrected = run.get('judge_corrections', {}).get(row['id'], value) if row.get('valid') is not False and run['status'] == 'completed' else None
            values.append({'run': run['id'], 'status': run['status'], 'raw': value, 'corrected': corrected,
                           'correction_evidence': evidence.get(run['id'] + ':' + row['id']),
                           'invalid_evidence': evidence.get('invalid:' + row['id'])})
        matrix.append({'criterion': row['id'], 'weight': 5, 'valid': row.get('valid', True), 'runs': values,
                       'all_completed_pass_raw': bool(values) and all(v['raw'] is True for v in values)})
    statistics = None
    if not precheck:
        statistics = stats.compute(copy.deepcopy(raw))
    else:
        # Validate shape without pretending this one-run diagnostic is a V3 baseline.
        validation = copy.deepcopy(raw)
        validation['spec_version'] = 'V2'
        if validation.get('rubrics'):
            stats.validate(validation)
        else:
            need(not any(r.get('results') for r in rollouts), 'unmapped precheck results need provisional surface slots')
    patterns = {}
    if statistics:
        for name, view in statistics['views'].items():
            failed = {r['id']: r['failed_rubrics'] for r in view['per_rollout'] if r['failed_rubrics']}
            groups = view['patterns']
            patterns[name] = {'failure_sets': failed, 'transitive_groups': groups,
                              'largest_group_share': max(map(len, groups), default=0) / len(failed) if failed else 0,
                              'transitive_bridges': view['chained_pattern_merges']}
    diagnoses = diagnoses or []
    repairs = repairs or []
    need(bool(diagnoses), 'mechanism-level causal diagnosis required')
    diagnosis_ids = set()
    completed = [run for run in rollouts if run['status'] == 'completed']
    all_fail = {row['id'] for row in rubrics if completed and
                all(run.get('results', {}).get(row['id']) is False for run in completed)}
    heavy_pass = {row['id'] for row in rubrics if row.get('weight') == 5 and completed and
                  all(run.get('results', {}).get(row['id']) is True for run in completed)}
    covered = set()
    for diagnosis in diagnoses:
        did = diagnosis.get('id')
        need(bool(did) and did not in diagnosis_ids, 'diagnosis IDs must be unique')
        diagnosis_ids.add(did)
        need(bool(diagnosis.get('mechanism')) and evidence_ok(diagnosis, task_dir), f'{did}: causal evidence required')
        criteria = set(diagnosis.get('criteria', []))
        need(criteria <= {row['id'] for row in rubrics}, f'{did}: unknown diagnosed criteria')
        covered.update(criteria)
        events = diagnosis.get('trajectory_events', [])
        need(bool(events), f'{did}: trajectory events required')
        for event in events:
            path = paths.get(event.get('run'))
            need(path is not None, f'{did}: event run not bound')
            if path:
                need(event.get('export_sha256') == hashlib.sha256(path.read_bytes()).hexdigest(), f'{did}: stale event export')
                # Quote the actual call/write content, so an arbitrary step number is insufficient.
                quote = event.get('quote')
                exported = json.loads(path.read_text())
                index = event.get('event')
                valid_index = type(index) is int and isinstance(exported, list) and 0 <= index < len(exported)
                need(valid_index, f'{did}: actual zero-based trajectory event index required')
                need(valid_index and bool(quote) and quote in json.dumps(exported[index], ensure_ascii=False),
                     f'{did}: quote absent from the cited event')
        observation = diagnosis.get('observation')
        need(observation in OBSERVATIONS, f'{did}: unknown repair routing observation')
        if observation == 'all_fail' or criteria & all_fail:
            for check in ('fairness', 'readability', 'grader_accuracy'):
                need(evidence_ok(diagnosis.get(check), task_dir), f'{did}: all-fail {check} review required')
    need(all_fail <= covered, 'all-fail criteria require explicit causal and fairness diagnosis: ' + str(sorted(all_fail - covered)))
    need(heavy_pass <= covered, 'heavy all-pass criteria require explicit causal diagnosis: ' + str(sorted(heavy_pass - covered)))
    for repair in repairs:
        rid = repair.get('id', '?')
        need(repair.get('diagnosis') in diagnosis_ids, f'{rid}: repair needs causal diagnosis')
        for field in ('original_placement', 'proposed_change', 'affected_outcomes', 'scope_difference',
                      'fair_discovery_path', 'required_reruns'):
            need(bool(repair.get(field)), f'{rid}: missing {field}')
        need(evidence_ok(repair, task_dir), f'{rid}: repair evidence required')
        scope = repair.get('scope_difference', {})
        classification = scope.get('reason_class') if isinstance(scope, dict) else None
        need(classification in ('difficulty', 'missing_data', 'fairness', 'grader_defect'), f'{rid}: scope change reason required')
        need(scope_difference_ok(scope), f'{rid}: concrete scope/volume difference required')
        change_kind = repair.get('change_kind')
        need(isinstance(change_kind, str) and bool(change_kind.strip()), f'{rid}: explicit change kind required')
        outcomes = repair.get('affected_outcomes')
        need(isinstance(outcomes, list) and bool(outcomes) and all(isinstance(outcome, str) and outcome.strip() for outcome in outcomes),
             f'{rid}: affected outcomes must be a nonempty list')
        if isinstance(outcomes, list) and rubrics:
            need(set(outcomes) <= {row['id'] for row in rubrics}, f'{rid}: affected outcome is not a reviewed criterion/provisional slot')
        reruns = repair.get('required_reruns')
        need(isinstance(reruns, list) and bool(reruns) and all(isinstance(stage, str) and stage in RERUN_STAGES for stage in reruns),
             f'{rid}: required reruns must be a bounded list of stages')
        need(not (classification == 'difficulty' and repair.get('change_kind') == 'volume_only'), f'{rid}: volume alone cannot repair difficulty')
        need(repair.get('owner') == REPAIR_OWNERS.get(repair.get('artifact')), f'{rid}: wrong stage owner')
    return {'schema_version': 1, 'kind': 'MODE_B_DIAGNOSIS', 'task_id': task_id, 'revision': revision,
            'verdict': 'FAIL' if blockers else 'PASS', 'blockers': blockers,
            'evidence_scope': 'PROVISIONAL_SINGLE_PRECHECK' if precheck else 'SIX_SLOT_BASELINE',
            'source_matrix_sha256': digest(data), 'binding': {**binding, 'runs': {str(n): str(p) for n, p in binding['runs'].items()}},
            'heavy_rows': matrix, 'raw_matrix': raw, 'statistics': statistics, 'patterns': patterns,
            'observed_all_fail': sorted(all_fail), 'observed_heavy_all_pass': sorted(heavy_pass),
            'diagnoses': diagnoses, 'repairs': repairs, 'routing_rules': OBSERVATIONS,
            'correction_evidence': evidence}


def from_request(request, task_dir, context=None):
    """Read a task-local request; all source paths must remain within that task."""
    import json
    root = Path(task_dir).resolve()
    def local(value):
        path = (root / value).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            raise ValueError('missing or cross-task Mode B source: ' + str(value))
        return path
    request = dict(request)
    from trajectory_ledger import binding_bundle_hash
    if request.get('bundle_hash') != binding_bundle_hash(root, stage='precheck' if request.get('precheck') else 'baseline'):
        raise ValueError('stale Mode B task input bundle')
    data = json.loads(local(request.pop('data_path')).read_text())
    for key in ('verifier', 'receipt'):
        if request.get(key) is not None:
            request[key] = local(request[key])
    request['trajectories'] = [local(p) for p in request['trajectories']]
    from task_context import load_context
    context = context or load_context(root)
    if Path(context.get('task_dir', '')).resolve() != root or request.get('task_id') != context.get('task_identity'):
        raise ValueError('Mode B request disagrees with selected task identity')
    if request.get('precheck'):
        # A single provisional proxy matrix is not a final six-run baseline, but
        # it still cannot silently change the assigned model/mode/task policy.
        for key in ('spec_version', 'difficulty_mode', 'task_type'):
            if data.get(key) != context.get(key):
                raise ValueError('precheck matrix disagrees with assigned ' + key)
    else:
        # Bundle identity binds artifact bytes, not the independently supplied
        # matrix's weights, labels or assignment. Reuse the scoring owner's raw
        # reconstruction rather than accepting an edited heavy-row matrix.
        stats.bind_context(data, context)
        validation_data = copy.deepcopy(data)
        if request.get('correction_evidence') is not None:
            validation_data['correction_evidence'] = request['correction_evidence']
        stats.revalidate_binding(validation_data, context, verifier=request.get('verifier'),
                                 rubrics=root / '09_Rubrics.json')
    return build(data, task_dir=root, **request)


def main(argv=None):
    import argparse
    import json
    import os
    import tempfile
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--task-dir', type=Path, required=True)
    ap.add_argument('--request', type=Path, required=True)
    ap.add_argument('--out', type=Path)
    args = ap.parse_args(argv)
    root = args.task_dir.resolve()
    request_path = args.request.resolve()
    if not request_path.is_relative_to(root):
        raise ValueError('request must belong to selected task')
    report = from_request(json.loads(request_path.read_text()), root)
    encoded = json.dumps(report, indent=2, ensure_ascii=False) + '\n'
    if args.out:
        output = args.out.resolve()
        if not output.is_relative_to(root):
            raise ValueError('output must belong to selected task')
        output.parent.mkdir(parents=True, exist_ok=True)
        fd, tmp = tempfile.mkstemp(prefix='.mode-b-', dir=output.parent)
        try:
            with os.fdopen(fd, 'w') as handle:
                handle.write(encoded)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(tmp, output)
        finally:
            if os.path.exists(tmp):
                os.unlink(tmp)
    print(encoded, end='')
    return 0 if report['verdict'] == 'PASS' else 1


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, TypeError, OSError) as exc:
        import sys
        print('mode_b_report: ' + str(exc), file=sys.stderr)
        raise SystemExit(2)
