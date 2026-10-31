#!/usr/bin/env python3
"""Row ledger for /rubric (rubric-flow-v2): remember each row's result between runs.

  plan    Decide FULL or DELTA for the current rubric and classify every row.
          Writes drafts/rubric_delta_plan.json (and drafts/rubric_delta_carry.json in DELTA).
  write   After the final rubric-score save, record every row's text hash and result
          in drafts/rubric_ledger.json. Carries the full row list, never only the rows
          re-checked in this run.
  show    Print the current ledger.

Row identity is the SHA-256 of the row's graded fields (title, weight, category,
justification, evidence). A row whose hash and task context are unchanged and that
passed last time is LOCKED: it is not re-reviewed. Any change to the prompt, OE,
injection SQL or task details forces FULL, because locked rows may depend on them.
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
INPUTS = ROOT / 'Evals/task_inputs'
DRAFTS = INPUTS / 'reports/drafts'
LEDGER = DRAFTS / 'rubric_ledger.json'
PLAN = DRAFTS / 'rubric_delta_plan.json'
CARRY = DRAFTS / 'rubric_delta_carry.json'
RECORD = DRAFTS / 'rubric_score_record.json'
CANDIDATE = INPUTS / 'fixcheck/rubric_candidate.json'
FIX_STATUS = INPUTS / 'fixcheck/fix_status.json'
CONTEXT_KEYS = ('task-details', 'prompt', 'injection', 'oe')
# 2 (2026-10-17): rows locked under the old rules (no do-nothing, valid-case, PT-day or OE
# cross-check) cannot carry forward; the first run on the new release is FULL.
FORMAT = 2


def sha(data):
    return hashlib.sha256(data if isinstance(data, bytes) else data.encode('utf-8')).hexdigest()


def load(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def index():
    path = INPUTS / 'inputs.json'
    return load(path)['inputs'] if path.is_file() else {}


def rubric_rows(path=None):
    if path is None:
        entry = index().get('rubric') or {}
        files = entry.get('files') or []
        if entry.get('state') != 'saved' or not files:
            raise SystemExit('No saved rubric input; save it with hg_store_input.py save rubric first.')
        path = ROOT / files[0]['path']
    rows = load(path)
    if isinstance(rows, dict):
        rows = rows.get('criteria') or rows.get('rubric') or []
    if not isinstance(rows, list) or not rows:
        raise SystemExit('Rubric input is not a non-empty criteria array.')
    return rows, Path(path)


def field(row, name):
    annotations = row.get('annotations') or {}
    if name == 'category':
        value = row.get('category', annotations.get('rubric_category', ''))
    else:
        value = row.get(name, annotations.get(name, ''))
    return ' '.join(str(value if value is not None else '').split())


def row_hash(row):
    graded = {name: field(row, name) for name in ('title', 'weight', 'category', 'justification', 'evidence')}
    graded['category'] = graded['category'].lower()
    return sha(json.dumps(graded, sort_keys=True, ensure_ascii=False))


def context():
    entries = index()
    result = {}
    for key in CONTEXT_KEYS:
        entry = entries.get(key) or {}
        if entry.get('state') == 'saved':
            result[key] = '|'.join(f.get('sha256', '') for f in entry.get('files', []))
        elif entry.get('state'):
            result[key] = entry['state']
        else:
            result[key] = None
    return result


def flagged_rows(record):
    """Row number -> list of reasons it is not clean in the scoring record."""
    rubric = {}
    for issue in record.get('issues') or []:
        for number in issue.get('rows') or []:
            rubric.setdefault(number, []).append(
                dict(kind='issue', type=issue.get('type'), severity=issue.get('severity'), reason=issue.get('reason', '')))
    return rubric


def write(args):
    rows, path = rubric_rows(args.rubric)
    record = load(args.record or RECORD)
    flags = flagged_rows(record)
    weights = {w.get('row'): w for w in record.get('weight_reviews') or []}
    for item in record.get('predicted_all_fail') or []:
        for number in (item.get('rows') or ([item['row']] if 'row' in item else [])):
            flags.setdefault(number, []).append(dict(kind='predicted_all_fail', reason=item.get('reason', '')))
    previous = load(LEDGER) if LEDGER.is_file() else {}
    dismissals = previous.get('dismissals') or {}
    out_rows = []
    for number, row in enumerate(rows, 1):
        reasons = list(flags.get(number, []))
        review = weights.get(number)
        actual = row.get('weight')
        if review and review.get('expected_weight') not in (None, actual):
            reasons.append(dict(kind='weight', expected_weight=review['expected_weight'], actual_weight=actual,
                                reason=review.get('reason', '')))
        out_rows.append(dict(row=number, title=field(row, 'title'), row_sha256=row_hash(row), weight=actual,
                             status='FLAGGED' if reasons else 'PASS', findings=reasons))
    checked = list(previous.get('checked_fix_hashes') or []) if args.keep_checked else []
    if args.checked_candidate:
        candidate, _ = rubric_rows(args.checked_candidate)
        for number in [int(x) for x in (args.checked_rows or '').split(',') if x.strip()]:
            if not 1 <= number <= len(candidate):
                raise SystemExit(f'--checked-rows: candidate row {number} does not exist')
            checked.append(row_hash(candidate[number - 1]))
    elif (CANDIDATE.is_file() and FIX_STATUS.is_file()
          and CANDIDATE.stat().st_mtime >= path.stat().st_mtime):  # ignore a stale candidate from an earlier run
        # Read the (checked) marks from fix_status.json so no checked fix is missed.
        candidate, _ = rubric_rows(CANDIDATE)
        status = {int(k): v for k, v in (load(FIX_STATUS).get('rows') or {}).items()}
        changed = [c['row'] for c in changed_rows(rows, candidate)['changed_or_new']]
        missing = [n for n in changed if n not in status]
        if missing:
            raise SystemExit('fix_status.json has no status for changed/new candidate rows: '
                             + ', '.join(map(str, missing)) + ' (use "checked" or "revised")')
        bad = {n: v for n, v in status.items() if v not in ('checked', 'revised') or not 1 <= n <= len(candidate)}
        if bad:
            raise SystemExit(f'fix_status.json has invalid entries: {bad}')
        checked.extend(row_hash(candidate[n - 1]) for n, v in status.items() if v == 'checked')
    ledger = dict(format=FORMAT, flow='rubric-flow-v2', rubric_path=str(path.relative_to(ROOT)),
                  rubric_sha256=sha(path.read_bytes()), context=context(),
                  verdict=(record.get('verdict') or record.get('qc_verdict')), run_mode=args.mode,
                  rows=out_rows, dismissals=dismissals, checked_fix_hashes=sorted(set(checked)))
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    passed = sum(r['status'] == 'PASS' for r in out_rows)
    print(json.dumps(dict(ledger=str(LEDGER.relative_to(ROOT)), rows=len(out_rows), passed=passed,
                          flagged=len(out_rows) - passed)))


def plan(args):
    rows, path = rubric_rows(args.rubric)
    reason = None
    ledger = None
    if args.ledger:
        ledger = load(args.ledger)
    elif LEDGER.is_file():
        ledger = load(LEDGER)
    if args.force_full:
        reason = 'Full review requested.'
    elif not ledger:
        reason = 'No saved row ledger in this workspace (first run, or a new workspace without the previous ledger).'
    elif ledger.get('format') != FORMAT:
        reason = 'Saved ledger has an unsupported format.'
    else:
        changed = [k for k in CONTEXT_KEYS if (ledger.get('context') or {}).get(k) != context().get(k)]
        if changed:
            reason = 'Task context changed since the last run (' + ', '.join(changed) + '); locked rows may depend on it.'
    if reason:
        result = dict(mode='FULL', reason=reason, rows=len(rows))
        PLAN.parent.mkdir(parents=True, exist_ok=True)
        PLAN.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        CARRY.unlink(missing_ok=True)
        print(json.dumps(result, indent=2))
        return
    by_hash = {}
    for item in ledger['rows']:
        by_hash.setdefault(item['row_sha256'], []).append(item)
    by_title = {}
    for item in ledger['rows']:
        by_title.setdefault(item['title'], []).append(item)
    used = set()
    classified = []
    hashes = {row_hash(r) for r in rows}
    checked_fixes = set(ledger.get('checked_fix_hashes') or [])
    for number, row in enumerate(rows, 1):
        digest = row_hash(row)
        if digest in checked_fixes and not any(i['row_sha256'] == digest and i['row'] not in used
                                                for i in ledger['rows']):
            classified.append(dict(row=number, previous_row=None, status='LOCKED_CHECKED_FIX',
                                   title=field(row, 'title'), previous_findings=[]))
            continue
        match = next((i for i in by_hash.get(digest, []) if i['row'] not in used), None)
        if match:
            used.add(match['row'])
            status = 'LOCKED' if match['status'] == 'PASS' else 'RECHECK_FLAGGED'
            classified.append(dict(row=number, previous_row=match['row'], status=status, title=field(row, 'title'),
                                   previous_findings=match.get('findings', [])))
            continue
        similar = next((i for i in by_title.get(field(row, 'title'), []) if i['row'] not in used), None)
        if not similar:
            # Retitled in place: same position, previous row not matched elsewhere.
            similar = next((i for i in ledger['rows'] if i['row'] == number and i['row'] not in used
                            and i['row_sha256'] not in hashes), None)
        if similar:
            used.add(similar['row'])
            classified.append(dict(row=number, previous_row=similar['row'], status='EDITED', title=field(row, 'title'),
                                   previous_findings=similar.get('findings', [])))
        else:
            classified.append(dict(row=number, previous_row=None, status='NEW', title=field(row, 'title'),
                                   previous_findings=[]))
    removed = [dict(previous_row=i['row'], title=i['title'], status=i['status'])
               for i in ledger['rows'] if i['row'] not in used]
    targets = [c['row'] for c in classified if c['status'] not in ('LOCKED', 'LOCKED_CHECKED_FIX')]
    checked_rows = [c['row'] for c in classified if c['status'] == 'LOCKED_CHECKED_FIX']
    counts = {}
    for c in classified:
        counts[c['status']] = counts.get(c['status'], 0) + 1
    if not targets and not removed:
        mode, reason = 'UNCHANGED', 'Rubric and task context are identical to the last run; the previous verdict stands.'
    else:
        mode, reason = 'DELTA', 'Only changed, new and previously flagged rows are re-reviewed; locked rows carry forward.'
    result = dict(mode=mode, reason=reason, rows=len(rows), counts=counts, target_rows=targets,
                  checked_fix_rows=checked_rows,
                  removed_rows=removed, previous_verdict=ledger.get('verdict'),
                  dismissals=ledger.get('dismissals') or {}, classification=classified)
    PLAN.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    carry(classified)
    print(json.dumps({k: v for k, v in result.items() if k != 'classification'}, indent=2, ensure_ascii=False))
    print('Full row classification: ' + str(PLAN.relative_to(ROOT)))


def carry(classified):
    """Previous per-row check entries for LOCKED rows, renumbered to the current row numbers."""
    history = sorted((DRAFTS / 'rubric_history').glob('rubric_score_record*.json'), key=lambda p: p.stat().st_mtime)
    source = RECORD if RECORD.is_file() else (history[-1] if history else None)
    if not source:
        CARRY.unlink(missing_ok=True)
        return
    record = load(source)
    remap = {c['previous_row']: c['row'] for c in classified if c['status'] == 'LOCKED'}
    rows = []
    for entry in (record.get('checks') or {}).get('rows') or []:
        if entry.get('row') in remap:
            rows.append({**entry, 'row': remap[entry['row']]})
    weights = []
    for entry in record.get('weight_reviews') or []:
        if entry.get('row') in remap:
            weights.append({**entry, 'row': remap[entry['row']]})
    all_map = {c['previous_row']: c['row'] for c in classified if c['previous_row']}
    CARRY.write_text(json.dumps(dict(
        source_record=str(source.relative_to(ROOT)),
        note=('Locked rows only, renumbered to current row numbers. Copy these entries into the new record '
              'unchanged. previous_to_current maps every surviving row for remapping requirements, sampling '
              'samples and overlap references; rows absent from it were removed.'),
        previous_to_current={str(k): v for k, v in sorted(all_map.items())},
        check_rows=rows, weight_reviews=weights), indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def diff(args):
    """Changed, new and removed rows between the current rubric and a candidate rubric."""
    current, _ = rubric_rows(args.rubric)
    candidate, _ = rubric_rows(args.candidate)
    print(json.dumps(changed_rows(current, candidate), indent=2, ensure_ascii=False))


def changed_rows(current, candidate):
    old = {}
    for number, row in enumerate(current, 1):
        old.setdefault(row_hash(row), []).append(number)
    titles = {field(r, 'title'): n for n, r in enumerate(current, 1)}
    used, out = set(), []
    for number, row in enumerate(candidate, 1):
        match = next((n for n in old.get(row_hash(row), []) if n not in used), None)
        if match:
            used.add(match)
            continue
        prev = titles.get(field(row, 'title'))
        if prev is None and number <= len(current) and number not in used \
                and row_hash(current[number - 1]) not in {row_hash(r) for r in candidate}:
            prev = number
        if prev is not None and prev not in used:
            used.add(prev)
            out.append(dict(row=number, status='CHANGED', previous_row=prev, title=field(row, 'title')))
        else:
            out.append(dict(row=number, status='NEW', previous_row=None, title=field(row, 'title')))
    removed = [dict(previous_row=n, title=field(r, 'title')) for n, r in enumerate(current, 1) if n not in used]
    return dict(changed_or_new=out, removed=removed, candidate_rows=len(candidate))


def dismiss(args):
    """Record a CB/QM dismissal reason for a flagged row so the next DELTA run checks the reason."""
    if not LEDGER.is_file():
        raise SystemExit('No ledger yet; run a full /rubric first.')
    ledger = load(LEDGER)
    ledger.setdefault('dismissals', {})[str(args.row)] = dict(reason=args.reason, title=next(
        (r['title'] for r in ledger['rows'] if r['row'] == args.row), ''))
    LEDGER.write_text(json.dumps(ledger, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print(json.dumps(dict(row=args.row, dismissal=args.reason)))


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest='command', required=True)
    p = sub.add_parser('plan')
    p.add_argument('--rubric')
    p.add_argument('--ledger', help='A ledger exported from another workspace (Slack <-> sandbox).')
    p.add_argument('--force-full', action='store_true')
    w = sub.add_parser('write')
    w.add_argument('--rubric')
    w.add_argument('--record')
    w.add_argument('--mode', choices=('FULL', 'DELTA'), required=True)
    w.add_argument('--checked-candidate', help='Candidate rubric holding the (checked) fixes')
    w.add_argument('--checked-rows', help='Comma-separated candidate row numbers marked (checked)')
    w.add_argument('--keep-checked', action='store_true',
                   help='Keep checked-fix hashes from the previous ledger (DELTA runs)')
    d = sub.add_parser('dismiss')
    d.add_argument('row', type=int)
    d.add_argument('reason')
    x = sub.add_parser('diff')
    x.add_argument('--candidate', required=True)
    x.add_argument('--rubric')
    sub.add_parser('show')
    args = parser.parse_args()
    if args.command == 'plan':
        plan(args)
    elif args.command == 'write':
        write(args)
    elif args.command == 'diff':
        diff(args)
    elif args.command == 'dismiss':
        dismiss(args)
    else:
        print(LEDGER.read_text() if LEDGER.is_file() else 'No ledger.')


if __name__ == '__main__':
    sys.exit(main())
