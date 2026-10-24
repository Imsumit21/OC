"""Bind Oracle Event reviews and calculate the two user-supplied QC dimensions.

Evidence anchors and arithmetic are checked here; semantic relevance and the
identification of the full critical path remain the reviewer's responsibility.
"""
import argparse
import hashlib
import json
from pathlib import Path

from hg_eval_release import snapshot, report_binding
from hg_preflight import reject_constant, unique_object
from hg_review_evidence import EvidenceReader, sources, links, authority
from hg_rubric_loop import local, review_context
from hg_source_checks import metadata_source, check_absence
from hg_oe_path import validate_path

POLICY = 'oracle-events-v2'
RECORD = Path('Evals/task_inputs/reports/drafts/oe_review_record.json')
REPORT = Path('Evals/task_inputs/reports/2_oe.md')
INPUT = Path('Evals/task_inputs/08_Oracle_Events.md')
FIELDS = ('action', 'information', 'tool_service', 'parameters', 'expected_data', 'dependencies')
FORMAT_DEFECTS = {'NO_DETAILS_OR_EXPECTED', 'ARROW_CHAIN', 'MULTIPLE_ACTIONS', 'JSON', 'NO_NUMBER_OR_SERVICE'}
INPUT_KEYS = {'task-details', 'prompt', 'oe', 'injection', 'error-async'}
REFERENCES = ('Evals/2_Oracle_Events_Eval.md', 'claude/skills/oe/SKILL.md',
              'Evals/WORKFLOW.md', 'Evals/INPUTS.md', 'Evals/ENVIRONMENT.md',
              'Evals/references/rules/oracle_events.md', 'Evals/references/persona/acl.md',
              'Evals/references/persona/roster.json', 'Evals/references/tools/catalog.json',
              'Evals/references/tools/manifest.json', 'Evals/tools/hg_oe_review.py',
              'Evals/tools/hg_oe_path.py')


def context(root):
    return review_context(root, input_filter=lambda k: k.removeprefix('source:') in INPUT_KEYS or
                          k.startswith('reference:'), reference_paths=REFERENCES, policy=POLICY)


def start(root):
    from hg_store_input import SLOTS
    ctx = context(root)
    entries = ctx['manifest']['inputs']
    def supplied(key):
        return any(entries.get(k, {}).get('state') == 'saved' for k in (key, 'source:' + key)) or (
            key not in entries and local(root, Path('Evals/task_inputs') / SLOTS[key]).is_file())
    for key in ('prompt', 'task-details'):
        if not supplied(key):
            raise ValueError('Save the required ' + key + ' input before reviewing OEs')
    if not (supplied('injection') or entries.get('injection', {}).get('usage') == 'not_used'):
        raise ValueError('Save injection SQL or the explicit no-injection decision first')
    # Saving a replacement source clears the canonical slot. Saving a new text
    # extraction/replacement afterwards restores the canonical slot as current.
    entry = entries.get('oe')
    if not entry or entry.get('state') != 'saved':
        entry = entries.get('source:oe') if entries.get('source:oe', {}).get('state') == 'saved' else entry
    if entry and entry.get('state') == 'saved':
        files = entry['files']
        if len(files) != 1:
            raise ValueError('Select one complete OE artifact; do not concatenate unrelated exports')
        path = Path(files[0]['path'])
    elif entry:
        raise ValueError('OE input is cleared; supply Oracle Events')
    else:
        path = INPUT
    raw = local(root, path).read_bytes()
    try:
        text = raw.decode('utf-8-sig')
    except UnicodeDecodeError as error:
        raise ValueError('Retain the original OE upload and save its verified text extraction under oe') from error
    if not text.strip():
        raise ValueError('OE artifact is empty; collect the supplied OEs')
    return dict(format_version=2, review_policy=POLICY, oe_path=path.as_posix(),
                reviewed_oe_sha256=hashlib.sha256(raw).hexdigest(),
                review_context_sha256=ctx['sha256'], eval_release=snapshot('oe', root))


def validate_record(root, content):
    record = json.loads(content, object_pairs_hook=unique_object, parse_constant=reject_constant)
    def need(ok, message):
        if not ok:
            raise ValueError('OE review: ' + message)
    def text(value):
        return isinstance(value, str) and bool(value.strip())
    need(isinstance(record, dict), 'record must be an object')
    current = start(root)
    for key, value in current.items():
        need(record.get(key) == value, 'missing or stale binding: ' + key)
    need(type(record['format_version']) is int, 'format_version must be an integer')
    ctx = context(root)['manifest']
    reader = EvidenceReader(root)
    known = sources(reader, record.get('sources'))
    raw = local(root, Path(current['oe_path'])).read_text(encoding='utf-8-sig')
    pending, missing, inaccurate, minor, soft = [], [], [], [], []
    need(type(record.get('inventory_complete')) is bool and text(record.get('inventory_reason')),
         'declare and explain critical-path inventory completeness')
    if not record['inventory_complete']:
        pending.append('critical-path inventory incomplete')
    steps = record.get('steps')
    need(isinstance(steps, list), 'steps must be an array')
    ids = set()
    for step in steps:
        need(isinstance(step, dict) and text(step.get('id')) and step['id'] not in ids, 'unique step IDs required')
        ids.add(step['id'])
    covered_steps, cursor = set(), 0
    segments = record.get('segments')
    need(isinstance(segments, list) and bool(segments), 'partition the entire supplied OE artifact')
    for segment in segments:
        need(isinstance(segment, dict), 'segment must be an object')
        first, last = segment.get('start'), segment.get('end')
        need(type(first) is int and type(last) is int and first == cursor and first < last <= len(raw),
             'segments must cover OE text exactly without gaps or overlaps')
        need(segment.get('quote') == raw[first:last] and text(segment.get('reason')), 'segment quote/reason missing')
        role = segment.get('role')
        need(role in {'STEP', 'CONTEXT', 'RESPONSE_DESCRIPTION', 'NON_ACTION'}, 'unknown segment role')
        refs = segment.get('step_ids')
        need(isinstance(refs, list) and all(isinstance(i, str) and i in ids for i in refs) and len(refs) == len(set(refs)),
             'segment needs known step IDs')
        need(role != 'STEP' or bool(refs), 'a step segment needs a reviewed step')
        covered_steps.update(refs)
        if role == 'RESPONSE_DESCRIPTION':
            soft.append('final-response description is not a trajectory step: ' + segment['reason'])
        if role == 'NON_ACTION':
            soft.append('non-action statement is not an observable step: ' + segment['reason'])
        cursor = last
    need(cursor == len(raw) and covered_steps == ids, 'all supplied text and steps must be reviewed')

    def evidence(item, label):
        refs = links(item.get('source_ids'), known, label)
        if any(s['visibility'] != 'VISIBLE' or metadata_source(s, root, ctx) for s in refs):
            pending.append(label + ': unavailable or non-primary evidence')
        if item.get('evidence_check') is not None:
            pending.extend(label + ': ' + p for p in check_absence(item['evidence_check'], reader, known, root, ctx))
        return refs

    for step in steps:
        sid = step['id']
        checks = step.get('checks')
        need(isinstance(checks, dict) and set(checks) == set(FIELDS), 'review all six step fields for ' + sid)
        for field, check in checks.items():
            need(isinstance(check, dict) and text(check.get('reason')), 'each check needs a reason')
            result = check.get('result')
            need(result in {'VERIFIED', 'MINOR', 'INACCURATE', 'MISSING', 'UNRESOLVED', 'NOT_APPLICABLE'},
                 'invalid step check result')
            label = sid + '.' + field
            if result == 'UNRESOLVED':
                pending.append(label + ': ' + check['reason'])
            elif result == 'MISSING':
                missing.append(label + ': ' + check['reason'])
            elif result != 'NOT_APPLICABLE':
                before = len(pending)
                evidence(check, label)
                if len(pending) == before:
                    if result == 'INACCURATE': inaccurate.append(label)
                    if result == 'MINOR': minor.append(label)
            else:
                need(field in {'tool_service', 'parameters', 'dependencies'},
                     'action, information and expected data must be reviewed, not waived')
        verification = step.get('rubric_verification')
        need(isinstance(verification, dict) and text(verification.get('reason')), 'explain Outcome-first mapping')
        need(verification.get('category') in {'OUTCOME', 'PROCESS', 'NONE'}, 'invalid rubric mapping')
        if verification['category'] == 'PROCESS':
            need(text(verification.get('why_no_outcome')), 'Process needs an explanation of why no Outcome can verify it')

    coverage = record.get('coverage')
    need(isinstance(coverage, list) and bool(coverage), 'map the prompt critical path, including absent steps')
    requirement_ids = set()
    for requirement in coverage:
        need(isinstance(requirement, dict) and text(requirement.get('id')) and requirement['id'] not in requirement_ids,
             'unique coverage IDs required')
        requirement_ids.add(requirement['id'])
        need(text(requirement.get('requirement')) and text(requirement.get('reason')), 'explain the path requirement')
        visible = authority(requirement.get('authority_chain'), known, root, ctx)
        visible = visible and not any(metadata_source(known[s], root, ctx) for s in requirement['authority_chain'])
        if not visible:
            pending.append(requirement['id'] + ': unresolved requirement authority')
        refs = requirement.get('step_ids')
        need(isinstance(refs, list) and all(isinstance(i, str) and i in ids for i in refs) and len(refs) == len(set(refs)),
             'coverage must name known steps')
        result = requirement.get('result')
        need(result in {'COVERED', 'MISSING', 'UNRESOLVED'}, 'invalid coverage result')
        need(result != 'COVERED' or bool(refs), 'covered requirements need actual OE steps')
        if result == 'MISSING' and visible: missing.append(requirement['id'])
        if result == 'UNRESOLVED': pending.append(requirement['id'])

    format_review = record.get('format_review')
    need(isinstance(format_review, dict) and format_review.get('checked') is True and text(format_review.get('reason')),
         'check Format & Standardization and explain the result')
    findings = format_review.get('findings')
    need(isinstance(findings, list), 'format_review.findings must be an array (empty when the format is clean)')
    format_defects = []
    for finding in findings:
        need(isinstance(finding, dict) and finding.get('defect') in FORMAT_DEFECTS, 'unknown format defect')
        need(text(finding.get('quote')) and finding['quote'] in raw and text(finding.get('reason')),
             'a format finding needs an exact OE quote and a reason')
        refs = finding.get('step_ids')
        need(isinstance(refs, list) and all(isinstance(i, str) and i in ids for i in refs), 'format finding needs known step IDs')
        format_defects.append('format:' + finding['defect'] + ': ' + finding['reason'])
    minor.extend(format_defects)

    path = validate_path(record.get('path_review'), record, reader, known, root, ctx)
    inaccurate.extend('path:' + item['code'] + ': ' + item['detail'] for item in path['inaccurate'])
    minor.extend('path:' + item['code'] + ': ' + item['detail'] for item in path['minor'])
    pending.extend('path:' + item['code'] + ': ' + item['detail'] for item in path['unresolved'])
    complete = not pending
    failed = bool(missing or inaccurate)
    completeness = 2 if missing else 3 if soft else 5
    accuracy = 2 if inaccurate else 3 if minor else 5
    scored = complete or failed
    score = min(completeness, accuracy) if scored else None
    verdict = 'FAIL' if failed else 'PASS' if score == 5 else 'NON-FAIL'
    feasibility = 'BROKEN' if inaccurate else 'UNRESOLVED' if pending else 'INCOMPLETE' if missing else 'SUPPORTED'
    solvability = ('UPSTREAM_BLOCKER' if path['upstream_blockers'] else
                  'SUPPORTED_BY_OE' if feasibility == 'SUPPORTED' else 'NOT_ESTABLISHED')
    return dict(**current, verdict=verdict, verdict_score=score,
                execution_status='COMPLETE' if complete else 'PARTIAL',
                completeness_score=completeness if scored else None,
                accuracy_score=accuracy if scored else None,
                path_feasibility=feasibility, task_solvability=solvability,
                prompt_follow_up='REQUIRED' if path['upstream_blockers'] else 'NONE', path_checks=path,
                missing=missing, inaccurate=inaccurate, minor=minor, format_defects=format_defects,
                soft_defects=soft, unresolved=pending,
                oe_record_sha256=hashlib.sha256(content.encode()).hexdigest())


def approve_report(root, parsed):
    path = local(root, RECORD)
    if not path.is_file():
        raise ValueError('Save oe-review before a scored OE report')
    computed = validate_record(root, path.read_text())
    for key in ('verdict', 'verdict_score', 'execution_status', 'review_policy', 'reviewed_oe_sha256',
                'review_context_sha256', 'oe_record_sha256', 'completeness_score', 'accuracy_score',
                'path_feasibility', 'task_solvability', 'prompt_follow_up'):
        if parsed.get(key) != computed[key]:
            raise ValueError('OE report contradicts its evidence record: ' + key)
    return {**computed, **report_binding(parsed, computed['eval_release'])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=('start', 'validate'))
    parser.add_argument('record', nargs='?', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[4]
    try:
        result = start(root) if args.operation == 'start' else validate_record(root, args.record.read_text())
    except (OSError, ValueError, AttributeError) as error:
        parser.error(str(error))
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
