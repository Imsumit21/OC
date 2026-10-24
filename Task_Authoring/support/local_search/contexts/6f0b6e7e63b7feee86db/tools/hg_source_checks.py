"""Prompt/rubric source boundaries and conditional absence evidence.

These checks validate evidence declarations and detectable search errors, not
the semantic completeness of a source selection. OE reviews share these source
boundaries; other stages retain their own contracts.
"""
from copy import deepcopy
from decimal import Decimal
import json
from pathlib import Path
import re

METADATA_KEYS = {'dynamic-context', 'difficulty', 'human-time', 'golden', 'oe', 'rubric',
                 'baseline-verifier', 'all-fail', 'haiku', 'opus', 'baseline', 'reference'}
METADATA_NAMES = {'07_Dynamic_Context.md', '12_Difficulty_Stats.txt', '06_Human_Time.txt',
                  'oracle_events_qc_cases.json', 'oracle_events_qc_examples.md',
                  'prompt_qc_cases.json', 'prompt_qc_examples.md',
                  'rubric_qc_cases.json', 'rubric_qc_examples.md',
                  '08_Golden_Answer.md', '08_Oracle_Events.md', '2_oe.md', '09_Rubrics.json', '5_Rubric.json', '2_golden.md',
                  '10_Baseline_Verifier_Results.txt', '11_Baseline_AllFail_Justifications.txt'}
SURFACES = {'JSON', 'ATTACHMENTS', 'REPOSITORY_FILES', 'REPOSITORY_REFS', 'TABLE_METADATA', 'INJECTION'}
NEGATIVE_FACT = re.compile(r'\b(?:no|never|absent|missing|only|sole|unavailable|does not exist)\b', re.I)


def metadata_source(source, root, context):
    path = (Path(root) / source['path']).resolve()
    if source.get('source_role') in {'AUTHORING_METADATA', 'AUDIT_REPORT', 'MODEL_OUTPUT'}:
        return True
    if path.name in METADATA_NAMES or 'Evals/task_inputs/reports/' in path.as_posix():
        return True
    for key, entry in context.get('inputs', {}).items():
        if key.removeprefix('source:') in METADATA_KEYS:
            if any(path == (Path(root) / item['path']).resolve() for item in entry.get('files', [])):
                return True
    return False


def prepare_facts(review, known, root, context):
    """Neutralize untrusted evidence before it can create a numeric mismatch."""
    result = deepcopy(review)
    if not isinstance(result, dict) or not isinstance(result.get('claims'), list):
        return result
    for claim in result['claims']:
        if not isinstance(claim, dict):
            continue
        claim.pop('evidence_check', None)
        refs = [known[s] for s in claim.get('source_ids', []) if s in known]
        if refs and any(metadata_source(s, root, context) for s in refs):
            for field in ('calculation', 'selection', 'comparison', 'status'):
                claim.pop(field, None)
            claim.update(kind='UNRESOLVED', reason='Authoring metadata, OE/golden/rubric/verifier content or audit/model output is not primary factual authority; verify the underlying source.')
    return result


def check_absence(check, reader, known, root, context):
    def need(ok, message):
        if not ok:
            raise ValueError('Absence evidence: ' + message)
    def text(value):
        return isinstance(value, str) and bool(value.strip())
    need(isinstance(check, dict), 'needs a structured evidence_check')
    need(text(check.get('reason')), 'explain the evidence method')
    method = check.get('method')
    need(method in {'DIRECT', 'ABSENCE'}, 'method must be DIRECT or ABSENCE')
    if method == 'DIRECT':
        need(text(check.get('positive_evidence')), 'quote the positive evidence or explain why this is not an absence inference')
        sid = check.get('source_id')
        need(isinstance(sid, str) and sid in known, 'direct evidence needs a known source_id')
        source = known[sid]
        need(check['positive_evidence'] in reader.quote(source), 'positive evidence quote is absent')
        return ['direct evidence is unavailable or non-primary'] if source['visibility'] != 'VISIBLE' or metadata_source(source, root, context) else []
    need(text(check.get('scope')), 'state the exact collection/entity/period being searched')
    need(isinstance(check.get('errors'), list), 'record search errors explicitly')
    pending = ['search errors prevent absence proof'] if check['errors'] else []
    surfaces = check.get('surfaces')
    need(isinstance(surfaces, list), 'inventory relevant evidence surfaces')
    seen = set()
    for surface in surfaces:
        need(isinstance(surface, dict) and surface.get('kind') in SURFACES, 'unknown surface')
        kind = surface['kind']
        need(kind not in seen, 'duplicate surface')
        seen.add(kind)
        need(surface.get('status') in {'COMPLETE', 'INCOMPLETE', 'NOT_APPLICABLE'}, 'invalid surface status')
        need(text(surface.get('reason')), 'each surface needs a scope/completeness reason')
        refs = surface.get('source_ids')
        need(isinstance(refs, list) and all(isinstance(s, str) and s in known for s in refs)
             and len(refs) == len(set(refs)), 'surface references need known source IDs')
        if surface['status'] == 'INCOMPLETE':
            pending.append(kind + ': incomplete coverage')
        if surface['status'] == 'COMPLETE':
            need(bool(refs), 'a complete surface needs source or search-receipt evidence')
            for sid in refs:
                source = known[sid]
                if source['visibility'] != 'VISIBLE' or metadata_source(source, root, context):
                    pending.append(kind + ': unavailable or non-primary evidence')
                raw = reader.quote(source)
                try:
                    receipt = json.loads(raw)
                except json.JSONDecodeError:
                    continue
                if isinstance(receipt, dict):
                    if receipt.get('errors') or receipt.get('scan_complete') is False or receipt.get('truncated') is True:
                        pending.append(kind + ': source receipt reports an incomplete/error result')
                    if receipt.get('exit_code', 0) not in (0, None):
                        pending.append(kind + ': command failed')
                    if kind == 'REPOSITORY_REFS' and re.search(r'\bgit\s+tag\b', str(receipt.get('command', ''))) and not str(receipt.get('stdout', '')).strip():
                        pending.append(kind + ': empty git tag output alone does not establish exported ref coverage')
                    scope = str(receipt.get('scope', '')).lower()
                    if kind != 'JSON' and ('json scalar' in scope or 'excludes root/' in scope):
                        pending.append(kind + ': JSON-only search cannot cover this surface')
    need(seen == SURFACES, 'account for JSON, attachments, repository files/refs, table metadata and injection; use NOT_APPLICABLE with reasons')
    need(any(s['status'] != 'NOT_APPLICABLE' for s in surfaces), 'absence must identify an applicable evidence surface')
    control = check.get('positive_control')
    need(isinstance(control, dict) and control.get('source_id') in known and text(control.get('quote')),
         'record a known-present positive control')
    source = known[control['source_id']]
    need(control['quote'] in reader.quote(source), 'positive-control quote is absent')
    if source['visibility'] != 'VISIBLE' or metadata_source(source, root, context):
        pending.append('positive control is unavailable or non-primary')
    return pending


def guard_absence(result, review, reader, known, root, context):
    claims = {c['id']: c for c in review['claims']}
    removed = set()
    for item in result['computed']:
        claim = claims[item['claim_id']]
        check = claim.get('evidence_check')
        zero_count = (item.get('operation') in {'count', 'distinct_count'} and
                      Decimal(item.get('raw_actual', item.get('actual'))) == 0)
        negative = claim['kind'] == 'SEMANTIC' and claim.get('status') == 'VERIFIED' and NEGATIVE_FACT.search(claim['quote'])
        pending = []
        if check is not None:
            pending = check_absence(check, reader, known, root, context)
            if zero_count and check.get('method') != 'ABSENCE':
                pending.append('zero-count absence needs collection coverage evidence')
        elif zero_count or negative:
            pending = ['absence/exclusivity inference needs a scope-bound evidence_check; a positive contradiction can use direct evidence']
        if pending:
            removed.add(item['claim_id'])
            item['matched'] = None
            result['unresolved'].append(dict(claim_id=item['claim_id'], quote=item['quote'], reason='; '.join(pending)))
    result['mismatches'] = [m for m in result['mismatches'] if m['claim_id'] not in removed]
    return result
