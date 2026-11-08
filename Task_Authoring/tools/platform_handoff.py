#!/usr/bin/env python3
"""Validate evidence of platform state; never deploy, execute SQL or infer state.

A locally reviewed receipt can describe any vendor export format. Evidence files
must exist, retain their exact hashes, and be in the selected task. The reviewer
owns interpretation of deployment and readability evidence; hashes only bind it.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

VERSION = 'platform_handoff/1'


def evidence_errors(evidence, task_dir):
    errors = []
    if not isinstance(evidence, list) or not evidence:
        return ['supporting evidence missing']
    root = Path(task_dir).resolve()
    for item in evidence:
        if not isinstance(item, dict):
            errors.append('evidence reference must be an object')
            continue
        try:
            path = Path(item['path'])
            path = (root / path).resolve() if not path.is_absolute() else path.resolve()
            path.relative_to(root)
            if hashlib.sha256(path.read_bytes()).hexdigest() != item.get('sha256'):
                errors.append(f'stale evidence: {path.name}')
            if not isinstance(item.get('reason'), str) or not item['reason'].strip():
                errors.append(f'evidence interpretation missing: {path.name}')
        except (KeyError, ValueError, OSError, TypeError) as exc:
            errors.append(f'invalid/outside-task evidence: {exc}')
    return errors


def validate(receipt, *, task_dir, task_id, revision, universe, sql_hash, bundle_hash, run_ids=None):
    if not isinstance(receipt, dict) or receipt.get('schema_version') != 1:
        return ['PLATFORM_PENDING: supported reviewed platform evidence missing']
    errors = []
    for key, expected in [('task_id', task_id), ('revision', revision), ('universe', universe), ('bundle_hash', bundle_hash)]:
        if not expected or receipt.get(key) != expected:
            errors.append(f'platform {key} missing/mismatched')
    for key in ('reviewer', 'reason', 'environment_id', 'environment_state_id'):
        if not isinstance(receipt.get(key), str) or not receipt[key].strip():
            errors.append(f'platform {key} missing')
    injection = receipt.get('injection', {})
    if sql_hash is None:
        if injection.get('state') != 'not-used' or injection.get('sha256') is not None:
            errors.append('explicit no-injection state required; do not invent SQL')
    elif injection.get('state') != 'applied' or injection.get('sha256') != sql_hash:
        errors.append('applied SQL identity missing/mismatched')
    for key in ('fresh_base', 'application', 'readability'):
        section = receipt.get(key)
        if not isinstance(section, dict):
            errors.append(f'platform {key} evidence missing')
            continue
        if section.get('environment_state_id') != receipt.get('environment_state_id'):
            errors.append(f'{key}: environment state mismatch')
        if section.get('verified') is not True:
            errors.append(f'{key}: not verified')
        errors.extend(f'{key}: {e}' for e in evidence_errors(section.get('evidence'), task_dir))
    fresh = receipt.get('fresh_base') or {}
    if fresh.get('source') != 'base-universe':
        errors.append('fresh environment must originate from base universe, not accumulated snapshot')
    reads = receipt.get('readability') or {}
    if not isinstance(reads.get('decisive_records'), list) or not reads['decisive_records']:
        errors.append('agent-tool readability of decisive records missing')
    if not reads.get('tool_assumptions'):
        errors.append('readability tool assumptions missing')
    manual = receipt.get('manual_changes')
    if not isinstance(manual, list):
        errors.append('intervening manual changes must be explicitly disclosed (empty list if none)')
    elif manual:
        # Merely disclosing contamination cannot establish base + final SQL state.
        for change in manual:
            if not isinstance(change, dict) or change.get('included_in_final_sql') is not True or change.get('sql_sha256') != sql_hash:
                errors.append('manual change not reconciled into final applied SQL')
    recorded_runs = receipt.get('baseline_run_ids')
    if not isinstance(recorded_runs, list) or len(set(recorded_runs)) != len(recorded_runs):
        errors.append('environment-associated baseline run identities missing/duplicated')
    if run_ids is not None and set(recorded_runs or []) != set(run_ids):
        errors.append('baseline run identities differ from environment evidence')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--receipt', required=True, type=Path)
    parser.add_argument('--context', required=True, type=Path, help='JSON validate() keyword arguments')
    args = parser.parse_args()
    errors = validate(json.loads(args.receipt.read_text()), **json.loads(args.context.read_text()))
    print(json.dumps({'status': 'PLATFORM_PENDING' if errors else 'READY', 'errors': errors}, indent=2))
    return bool(errors)

if __name__ == '__main__':
    raise SystemExit(main())
