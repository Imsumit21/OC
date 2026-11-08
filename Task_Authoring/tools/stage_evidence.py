#!/usr/bin/env python3
"""Immutable task-local stage attestations. Readiness is a derived view, never an input.

Digests are supplied by the stage owner (stage_gate.file_digest for artifacts), so
pasting a certificate retains the existing normalization and cannot stale itself.
The CLI records an already reviewed JSON request; it does not perform that review.
"""
from __future__ import annotations
import argparse
import fcntl
import hashlib
import json
import os
from pathlib import Path
import tempfile

VERSION = 'stage_evidence/1'
SCHEMA_VERSION = 1
DIRECTORY = 'Working_Files/stage_evidence'
# These are logical evidence dependencies, not a chronological global revision.
DEPENDENCIES = {
    'scenario': (), 'injection': ('scenario',),
    'error-async': ('injection',), 'reference-files': ('injection',),
    'prompt-writing': ('injection', 'error-async', 'reference-files'), 'prompt-check': ('prompt-writing',),
    'humantime': ('prompt-check',), 'oe-writing': ('prompt-check',),
    'oe-check': ('oe-writing',), 'rubric-writing': ('oe-check', 'oe-writing'),
    'rubric-check': ('rubric-writing',), 'local-build': ('rubric-check',),
    'platform-handoff': ('local-build',), 'baseline': ('platform-handoff',),
    'allfail': ('baseline',), 'difficulty': ('allfail',),
    'hardening': ('injection',), 'release': ('difficulty', 'rubric-check', 'humantime', 'error-async', 'reference-files', 'hardening'),
}

def content_id(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()


def task_identity(task_dir):
    return content_id(str(Path(task_dir).resolve()))


def _nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def ancestors(stage):
    if stage not in DEPENDENCIES:
        raise ValueError(f'unknown stage {stage!r}')
    result, visiting = set(), set()
    def visit(node):
        if node in visiting:
            raise ValueError('stage dependency cycle')
        visiting.add(node)
        for parent in DEPENDENCIES[node]:
            result.add(parent)
            visit(parent)
        visiting.remove(node)
    visit(stage)
    return result


def availability_errors(items, stage):
    errors = []
    for item in items:
        if not isinstance(item, dict) or not _nonempty(item.get('id')):
            errors.append('availability item needs id')
            continue
        state = item.get('state')
        if state == 'required-now':
            if not item.get('evidence_refs'):
                errors.append(f"{item['id']}: required evidence missing")
        elif state == 'deferred':
            due = item.get('required_at')
            if due not in DEPENDENCIES or not _nonempty(item.get('reason')):
                errors.append(f"{item['id']}: deferred evidence needs named stage and reason")
            elif due == stage or due in ancestors(stage):
                errors.append(f"{item['id']}: evidence is now required at {due}")
            elif stage not in ancestors(due):
                errors.append(f"{item['id']}: cannot defer to unrelated/earlier stage {due}")
        elif state == 'not-applicable':
            if not _nonempty(item.get('reason')):
                errors.append(f"{item['id']}: not-applicable needs reason")
        elif state == 'unresolved-required':
            errors.append(f"{item['id']}: required evidence unresolved")
        else:
            errors.append(f"{item['id']}: invalid availability state")
    return errors


def make_record(*, task_id, stage, revision, inputs, upstream, checks, availability,
                reviewer, tool_identity, policy_identity, supersedes=None, producer=None):
    if not all(_nonempty(x) for x in (task_id, revision, reviewer)):
        raise ValueError('task_id, revision and reviewer are required')
    allowed = ancestors(stage)
    if not isinstance(inputs, dict) or not inputs or not all(_nonempty(v) for v in inputs.values()):
        raise ValueError('nonempty relevant input digests required')
    if not isinstance(upstream, dict) or any(k not in allowed for k in upstream):
        raise ValueError('upstream evidence must be an ancestor; summary/downstream dependencies are forbidden')
    if not all(_nonempty(v) for v in upstream.values()):
        raise ValueError('upstream identities required')
    if not tool_identity or not policy_identity:
        raise ValueError('tool/check and policy identities required')
    if not isinstance(checks, list) or not checks:
        raise ValueError('check outcomes required')
    for check in checks:
        if not isinstance(check, dict) or not _nonempty(check.get('id')) or check.get('outcome') not in ('PASS', 'FAIL', 'WARN', 'SKIP', 'INFO'):
            raise ValueError('each check needs id and explicit outcome')
        if check.get('outcome') in ('WARN', 'SKIP') and not check.get('disposition'):
            raise ValueError('warning/skipped check needs an evidenced disposition')
    if not isinstance(availability, list):
        raise ValueError('availability must be an array')
    errors = availability_errors(availability, stage)
    if errors:
        raise ValueError('; '.join(errors))
    value = dict(schema_version=SCHEMA_VERSION, kind='STAGE_ATTESTATION', task_id=task_id,
                 revision=revision, stage=stage, inputs=inputs, upstream=upstream, checks=checks,
                 availability=availability, reviewer=reviewer, tool_identity=tool_identity,
                 policy_identity=policy_identity, supersedes=supersedes, producer=producer)
    value['evidence_id'] = content_id(value)
    return value


def validate(record, *, task_id, stage, inputs, upstream, tool_identity=None,
             policy_identity=None, current_stage=None):
    """Return errors without changing historical records or assuming newer hash = authority."""
    if not isinstance(record, dict) or record.get('schema_version') != SCHEMA_VERSION:
        return ['HISTORICAL_UNVERIFIED: supported stage attestation missing']
    errors = []
    body = {k: v for k, v in record.items() if k != 'evidence_id'}
    if record.get('evidence_id') != content_id(body):
        errors.append('attestation identity mismatch')
    if record.get('task_id') != task_id or record.get('stage') != stage:
        errors.append('task/stage identity mismatch')
    for label, actual in [('inputs', inputs), ('upstream', upstream)]:
        if record.get(label) != actual:
            errors.append(f'STALE: {label} changed')
    for label, actual in [('tool_identity', tool_identity), ('policy_identity', policy_identity)]:
        if actual is not None and record.get(label) != actual:
            errors.append(f'REVIEW_REQUIRED: {label} differs; no release authority inferred')
    errors.extend(availability_errors(record.get('availability', []), current_stage or stage))
    if any(c.get('outcome') == 'FAIL' for c in record.get('checks', [])):
        errors.append('failed check remains')
    try:
        make_record(**{k: record[k] for k in ('task_id', 'stage', 'revision', 'inputs', 'upstream', 'checks',
                                             'availability', 'reviewer', 'tool_identity', 'policy_identity')},
                    supersedes=record.get('supersedes'), producer=record.get('producer'))
    except (KeyError, ValueError, TypeError) as exc:
        errors.append(str(exc))
    return errors


def _atomic_json(path, value):
    fd, name = tempfile.mkstemp(prefix='.' + path.name, dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as stream:
            json.dump(value, stream, sort_keys=True, indent=2)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def attest(task_dir, **kwargs):
    """Serialize validation/history update; never overwrite an immutable record."""
    from trajectory_ledger import safe_out
    root = safe_out(Path(task_dir)).resolve()
    if any((p / 'SHA256SUMS').is_file() for p in (root, *root.parents)):
        raise ValueError('cannot attest into frozen historical task')
    expected = task_identity(root)
    if kwargs.get('task_id', expected) != expected:
        raise ValueError('task identity disagrees with output directory')
    kwargs['task_id'] = expected
    directory = (root / DIRECTORY).resolve()
    directory.relative_to(root)
    directory.mkdir(parents=True, exist_ok=True)
    lock_fd = os.open(directory / '.lock', os.O_CREAT | os.O_RDWR | getattr(os, 'O_NOFOLLOW', 0), 0o600)
    with os.fdopen(lock_fd, 'a+') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX)
        index_path = directory / 'index.json'
        index = json.loads(index_path.read_text()) if index_path.exists() else {}
        stage = kwargs['stage']
        previous_id = index.get(stage)
        if previous_id:
            if not isinstance(previous_id, str) or len(previous_id) != 64 or any(c not in '0123456789abcdef' for c in previous_id):
                raise ValueError('invalid immutable evidence identity in index')
            previous = json.loads((directory / (previous_id + '.json')).read_text())
            candidate = make_record(**kwargs, supersedes=previous.get('supersedes'))
            if candidate == previous:
                return previous
        record = make_record(**kwargs, supersedes=previous_id)
        path = directory / (record['evidence_id'] + '.json')
        if path.exists() and json.loads(path.read_text()) != record:
            raise ValueError('immutable evidence identity conflict')
        if not path.exists():
            _atomic_json(path, record)
        index[stage] = record['evidence_id']
        _atomic_json(index_path, index)
        return record


def latest(task_dir, stage):
    directory = Path(task_dir) / DIRECTORY
    try:
        identity = json.loads((directory / 'index.json').read_text()).get(stage)
        if identity and (not isinstance(identity, str) or len(identity) != 64 or any(c not in '0123456789abcdef' for c in identity)):
            raise ValueError('invalid immutable evidence identity in index')
        return json.loads((directory / (identity + '.json')).read_text()) if identity else None
    except FileNotFoundError:
        return None


def evaluator_compatibility(local, reported, review=None, *, task_dir=None):
    if not reported:
        return {'status': 'UNKNOWN', 'local': local, 'reported': reported, 'reason': 'platform release not reported'}
    if local == reported:
        return {'status': 'MATCH', 'local': local, 'reported': reported}
    accepted = (isinstance(review, dict) and review.get('local') == local and review.get('reported') == reported
                and review.get('compatible') is True and _nonempty(review.get('reviewer'))
                and _nonempty(review.get('reason')) and bool(review.get('evidence_refs'))
                and str(review.get('reason')).strip().lower() not in ('reviewed', 'ok', 'accepted', 'n/a'))
    proof_errors = []
    if accepted:
        if task_dir is None:
            proof_errors = ['selected task required to verify compatibility evidence']
        else:
            from platform_handoff import evidence_errors
            proof_errors = evidence_errors(review.get('evidence_refs'), task_dir)
        accepted = not proof_errors
    return {'status': 'REVIEWED_COMPATIBLE' if accepted else 'REVIEW_REQUIRED', 'local': local, 'reported': reported,
            'reason': 'release difference; hashes do not establish authority or chronology', 'review': review,
            'evidence_errors': proof_errors}


def readiness(statuses, *, no_injection=False):
    """Read-only projection. Missing platform proof does not prevent local readiness."""
    local = all(statuses.get(s) == 'CURRENT' or (s == 'injection' and no_injection and statuses.get(s) == 'NOT_APPLICABLE') for s in ('scenario', 'injection', 'prompt-check', 'oe-check', 'rubric-check'))
    return {'local_build_ready': local, 'platform_baseline_ready': local and statuses.get('platform-handoff') == 'CURRENT',
            'stages': dict(statuses)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--task-dir', required=True, type=Path)
    parser.add_argument('--record', type=Path, help='JSON request of reviewed checks, inputs and evidence availability')
    parser.add_argument('--stage', choices=sorted(DEPENDENCIES))
    args = parser.parse_args()
    if args.record:
        request = json.loads(args.record.read_text())
        if request.get('producer') is not None:
            parser.error('producer is reserved for the executing gate; generic record imports cannot certify stage execution')
        value = attest(args.task_dir, **request)
    elif args.stage:
        value = latest(args.task_dir, args.stage)
    else:
        parser.error('--record or --stage required')
    print(json.dumps(value, indent=2))

if __name__ == '__main__':
    main()
