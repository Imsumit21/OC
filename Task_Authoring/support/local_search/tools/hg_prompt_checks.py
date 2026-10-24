"""Bind prompt premise and outcome review to exact input and source evidence."""
import argparse
import hashlib
import json
from pathlib import Path
import re

from hg_eval_release import snapshot, require_binding, report_binding
from hg_review_evidence import EvidenceReader, sources, links
from hg_rubric_fact_binding import checked_facts
from hg_rubric_loop import review_context, local
from hg_source_checks import metadata_source
import hg_prompt_ugt as ugt

POLICY = 'prompt-source-checks-v2'
RECORD = Path('Evals/task_inputs/reports/drafts/prompt_check_record.json')
PROMPT = Path('Evals/task_inputs/04_Prompt.txt')
INPUTS = {'task-details', 'prompt', 'injection', 'error-async', 'dynamic-context'}
REFERENCES = ('Evals/1_Prompt_Eval.md', 'claude/skills/prompt/SKILL.md', 'Evals/WORKFLOW.md',
              'Evals/ENVIRONMENT.md', 'Evals/EXECUTION.md', 'Evals/INPUTS.md', 'Evals/SEARCH.md',
              'Evals/references/rules/scoring.json', 'Evals/references/rules/prompt_rubric_reliability.md',
              'Evals/references/persona/acl.md', 'Evals/references/persona/roster.json',
              'Evals/tools/hg_prompt_checks.py', 'Evals/tools/hg_prompt_ugt.py',
              'Evals/tools/hg_source_checks.py')


def context(root):
    return review_context(root, input_filter=lambda k: k.removeprefix('source:') in INPUTS or k.startswith('reference:'),
                          reference_paths=REFERENCES, policy=POLICY)


def start(root):
    raw = local(root, PROMPT).read_bytes()
    return dict(format_version=2, eval_release=snapshot('prompt'),
                reviewed_prompt_sha256=hashlib.sha256(raw).hexdigest(), review_context_sha256=context(root)['sha256'])


def validate_record(root, content):
    from hg_preflight import reject_constant, unique_object
    from hg_report_contract import parse_result
    record = json.loads(content, object_pairs_hook=unique_object, parse_constant=reject_constant)
    def need(ok, message):
        if not ok:
            raise ValueError('Prompt checks: ' + message)
    def text(value):
        return isinstance(value, str) and bool(value.strip())
    need(isinstance(record, dict) and type(record.get('format_version')) is int and record['format_version'] == 2,
         'unsupported record format')
    release = require_binding(record, 'prompt')
    current = start(root)
    for key in ('reviewed_prompt_sha256', 'review_context_sha256'):
        need(record.get(key) == current[key], 'input/context changed: ' + key)
    prompt = local(root, PROMPT).read_text()
    reader = EvidenceReader(root)
    known = sources(reader, record.get('sources'))
    bound_context = context(root)['manifest']
    prompt_paths = {local(root, PROMPT).resolve()}
    prompt_paths.update((Path(root) / f['path']).resolve()
                        for k, entry in bound_context['inputs'].items() if k.removeprefix('source:') == 'prompt'
                        for f in entry.get('files', []))
    premise_known = {sid: ({**source, 'source_role': 'AUTHORING_METADATA'}
                          if (Path(root) / source['path']).resolve() in prompt_paths
                          else source) for sid, source in known.items()}
    pending, contradicted, ids = [], [], set()
    need(type(record.get('inventory_complete')) is bool and text(record.get('inventory_reason')),
         'record completeness and explain the premise inventory')
    need(type(record.get('other_checks_complete')) is bool, 'declare completion of the remaining Eval 1 phases')
    if not record['inventory_complete'] or not record['other_checks_complete']:
        pending.append('prompt inventory or remaining checks incomplete')
    premises = record.get('premises')
    need(isinstance(premises, list), 'premises must be an array')
    for premise in premises:
        need(isinstance(premise, dict) and text(premise.get('id')) and premise['id'] not in ids, 'premise IDs must be unique')
        ids.add(premise['id'])
        quote, offset = premise.get('quote'), premise.get('start')
        need(text(quote) and type(offset) is int and offset >= 0 and prompt[offset:offset+len(quote)] == quote,
             'premise must quote the exact saved prompt')
        need(premise.get('kind') in {'EXISTENCE', 'STATE', 'RELATIONSHIP'}, 'classify each premise')
        need(text(premise.get('reason')), 'explain why this is an asserted existing fact')
        review = premise.get('fact_review')
        need(isinstance(review, dict) and bool(review.get('claims')), 'each premise needs evidence-linked factual checks')
        checked = checked_facts(review, dict(title=quote), reader, premise_known, root, bound_context)
        pending.extend(premise['id'] + ': ' + x['reason'] for x in checked['unresolved'])
        if checked['mismatches']:
            contradicted.append(premise['id'])
    clauses = record.get('clauses')
    need(isinstance(clauses, list) and bool(clauses), 'partition the entire prompt into reviewed clauses')
    cursor, mapped = 0, set()
    for clause in clauses:
        need(isinstance(clause, dict), 'clause must be an object')
        first, last = clause.get('start'), clause.get('end')
        need(type(first) is int and type(last) is int and first == cursor and first < last <= len(prompt),
             'clause ranges must cover the whole prompt without gaps or overlap')
        need(clause.get('quote') == prompt[first:last] and text(clause.get('reason')), 'clause quote/reason missing')
        role = clause.get('role')
        need(role in {'REQUEST', 'PREMISE', 'HYPOTHESIS', 'CONTEXT'}, 'invalid clause role')
        refs = clause.get('premise_ids')
        need(isinstance(refs, list) and all(isinstance(r, str) and r in ids for r in refs)
             and len(refs) == len(set(refs)), 'clause needs known premise IDs')
        need(role != 'PREMISE' or bool(refs), 'an asserted fact needs a premise check')
        for p in premises:
            if p['id'] in refs:
                need(first <= p['start'] and p['start'] + len(p['quote']) <= last, 'premise belongs to another clause')
        mapped.update(refs)
        cursor = last
    need(cursor == len(prompt) and mapped == ids, 'all prompt text and premises must be reviewed')
    outcome_review = ugt.validate_review(record.get('unique_ground_truth'), known, root, bound_context)
    pending.extend('Unique Ground Truth: ' + reason for reason in outcome_review['pending'])
    # Other prompt dimensions keep their existing rules; these are supported
    # phase findings, not a second score calculator or a route around fact checks.
    other = record.get('other_failures', [])
    need(isinstance(other, list), 'other_failures must be an array')
    for item in other:
        need(isinstance(item, dict) and text(item.get('dimension')) and text(item.get('reason')), 'phase failure needs dimension/reason')
        need(item['dimension'].casefold() != 'truthfulness', 'truthfulness failures must use premise checks')
        dimension = re.sub(r'[^a-z0-9]+', ' ', item['dimension'].casefold()).strip()
        need('unique ground truth' not in dimension and 'ugt' not in dimension.split()
             and dimension not in {'2 1', 'phase 2 1', 'section 2 1'},
             'Unique Ground Truth findings must use unique_ground_truth, not other_failures')
        refs = links(item.get('source_ids'), known, 'phase failure sources')
        need(all(s['visibility'] == 'VISIBLE' and not metadata_source(s, root, bound_context) for s in refs),
             'phase failure needs available primary source/instruction evidence')
    verdict, score, status = record.get('verdict'), record.get('verdict_score'), record.get('execution_status')
    reason = record.get('verdict_reason')
    need(text(reason), 'explain the verdict under the existing phase scores')
    limits = '; '.join(pending) if pending else 'None'
    parsed = parse_result('prompt', f'### FINAL VERDICT: {verdict}\nScore: {score if score is not None else "null"}\nExecution status: {status}\nNext action: Review findings\nEvidence limits: {limits}\n')
    outcome_failure = outcome_review['verdict'] == 'FAIL'
    if contradicted or other or outcome_failure:
        need(verdict == 'FAIL', 'confirmed contradiction/phase failure requires FAIL under existing rules')
    if verdict == 'FAIL':
        need(bool(contradicted or other or outcome_failure), 'FAIL needs a demonstrated defect, not missing evidence')
    if outcome_failure:
        need(score <= outcome_review['score'], 'overall score cannot exceed the failed Unique Ground Truth score')
    if pending:
        need(status in {'PARTIAL', 'BLOCKED'}, 'unresolved evidence cannot establish COMPLETE')
    return {**parsed, **current, 'eval_release': release, 'contradicted_premises': contradicted,
            'unresolved': pending, 'unique_ground_truth': outcome_review,
            'ugt_report_section': ugt.render_review(outcome_review, known),
            'prompt_record_sha256': hashlib.sha256(content.encode()).hexdigest()}


def approve_report(root, parsed, content):
    path = local(root, RECORD)
    if not path.is_file():
        raise ValueError('Save prompt-checks before a scored prompt report')
    raw = path.read_text()
    computed = validate_record(root, raw)
    for key in ('verdict', 'verdict_score', 'execution_status', 'reviewed_prompt_sha256',
                'review_context_sha256', 'prompt_record_sha256'):
        if parsed.get(key) != computed[key]:
            raise ValueError('Prompt report contradicts its bound check record: ' + key)
    known = {source['id']: source for source in json.loads(raw)['sources']}
    ugt.validate_report(computed['unique_ground_truth'], known, content)
    return {**computed, **report_binding(parsed, computed['eval_release'])}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('operation', choices=('start', 'validate', 'render-ugt'))
    parser.add_argument('record', nargs='?', type=Path)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[4]
    try:
        result = start(root) if args.operation == 'start' else validate_record(
            root, (args.record or local(root, RECORD)).read_text())
    except (OSError, ValueError, AttributeError) as error:
        parser.error(str(error))
    if args.operation == 'render-ugt':
        print(result['ugt_report_section'], end='')
    else:
        print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
