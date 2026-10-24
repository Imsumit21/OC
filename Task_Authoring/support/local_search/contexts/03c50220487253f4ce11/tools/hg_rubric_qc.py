"""Rubric v10 QC tally. No verifier inputs; semantic judgments remain explicit.

QC percentages determine the audit grade. Repair/readiness checks do not silently
escalate that grade. This module implements rubric-revision-v10 with the local
hg-strict-overrides-v1 severities and the predicted all-fail gate.
"""
import re

FORMAT_VERSION = 4
DIMENSIONS = ('overall_quality', 'criteria_weights', 'category_balance', 'process',
              'agent_centric', 'negative')
GATES = ('schema', 'self_containment', 'accuracy_acceptance', 'atomicity', 'coverage',
         'duplicates', 'weights', 'contradiction')
SEVERITIES = {
    'incorrect': 'Major', 'unauthorized': 'Major', 'unobservable': 'Major',
    'non_atomic': 'Major', 'not_self_contained': 'Major', 'missing_coverage': 'Major',
    'overly_specific': 'Major', 'non_agent_centric': 'Major',
    'duplicate': 'Moderate', 'category': 'Moderate',
    'vague_exemplar': 'Moderate', 'overly_broad': 'Moderate', 'harmless_specificity': 'Minor',
}
ALL_FAIL_BASES = ('target_data_absent', 'required_tool_absent', 'filter_impossible',
                  'entity_unreachable')
WORK_WEIGHTS = {
    'direct_lookup': 1, 'literal_verification': 1,
    'interpretation': 3, 'calculation': 3, 'comparison': 3, 'limited_reconciliation': 3,
    'multi_source_reconciliation': 5, 'deep_reasoning': 5, 'cross_modal': 5, 'tracing': 5,
}
VAGUE = re.compile(r'\bsuch\s+as\b|\bfor\s+example\b|\be\.g\.(?=\s|,|$)', re.I)


def require(ok, message):
    if not ok:
        raise ValueError('Rubric QC: ' + message)


def prose(value, label):
    require(isinstance(value, str) and bool(value.strip()), label + ' needs evidence/reason')


def weight_tally(reviews, rubric):
    require(isinstance(reviews, list) and len(reviews) == len(rubric),
            'one weight review is required per actual criterion')
    seen, one, two, pending = set(), [], [], []
    for review in reviews:
        require(isinstance(review, dict), 'weight review must be an object')
        row = review.get('row')
        require(type(row) is int and 1 <= row <= len(rubric) and row not in seen,
                'weight review rows must match the actual array exactly')
        seen.add(row)
        assigned = rubric[row-1].get('weight')
        require(type(assigned) is int and assigned in (1, 3, 5), 'invalid authored weight')
        prose(review.get('reason'), 'weight review')
        source_ids = review.get('source_ids')
        require(isinstance(source_ids, list) and bool(source_ids) and
                all(isinstance(s, str) and s for s in source_ids) and
                len(set(source_ids)) == len(source_ids), 'weight review needs distinct source IDs')
        kind = review.get('work_kind')
        if kind == 'UNRESOLVED':
            require(review.get('expected_weight') is None, 'unresolved weight must not invent a value')
            pending.append(row)
            continue
        require(kind in WORK_WEIGHTS, 'unknown weight work kind')
        expected = WORK_WEIGHTS[kind]
        require(type(review.get('expected_weight')) is int and review['expected_weight'] == expected,
                'expected weight contradicts declared reasoning work')
        distance = abs((1, 3, 5).index(assigned) - (1, 3, 5).index(expected))
        if distance == 1:
            one.append(row)
        elif distance == 2:
            two.append(row)
    n = len(rubric)
    # Stricter than QC (QC: <30% one-level, <15% two-level): Non-Fail only when
    # 10% or fewer rows are one level off and none are two levels off.
    band = ('FAIL' if two or len(one) * 100 > 10 * n else 'NON-FAIL' if one else 'PASS')
    return dict(band=band, one_level_rows=one, two_level_rows=two,
                unresolved_rows=pending, denominator=n)


def calculate(record, rubric, checked=None):
    from hg_rubric_checks import title_facts
    require(type(record.get('format_version')) is int and record['format_version'] == FORMAT_VERSION,
            'v10 requires scoring record format 4')
    require(isinstance(rubric, list) and rubric and all(isinstance(r, dict) for r in rubric),
            'need actual nonempty criterion array')
    require(not any(k in record for k in ('platform_defects', 'all_failing', 'baseline_verifier')),
            'verifier-dependent fields are outside this rubric evaluation')
    n = len(rubric)
    rows, missing, acceptance = {}, {}, set()
    overlap_groups, overlap_members, redundant_rows = {}, set(), set()
    issues = record.get('issues')
    require(isinstance(issues, list), 'issues must be an array')
    provenance = {'rubric_original': 0, 'inherited_from_golden': 0, 'inherited_from_prompt': 0}
    levels = {'Minor': 1, 'Moderate': 2, 'Major': 3}
    for issue in issues:
        require(isinstance(issue, dict) and issue.get('type') in SEVERITIES,
                'unknown issue type; weight disagreements belong to weight_reviews')
        kind = issue['type']
        prose(issue.get('reason'), 'issue')
        require(issue.get('provenance') in provenance, 'issue needs provenance')
        provenance[issue['provenance']] += 1
        if issue['provenance'] != 'rubric_original':
            prose(issue.get('inherited_quote'), 'inherited issue')
        affected = issue.get('rows')
        require(isinstance(affected, list) and len(affected) == len(set(affected)) and
                all(type(r) is int and 1 <= r <= n for r in affected), 'invalid affected rows')
        impact = issue.get('impact')
        require(impact in ('rejects_correct', 'accepts_wrong', 'precision_only'), 'invalid issue impact')
        prose(issue.get('witness' if impact != 'precision_only' else 'omission_test'), 'issue test')
        severity = SEVERITIES[kind]
        require(issue.get('severity', severity) == severity, 'severity must follow QC category')
        if kind == 'missing_coverage':
            require(affected == [], 'missing outcomes are set-level findings')
            oid = issue.get('outcome_id')
            prose(oid, 'missing outcome ID')
            require(oid not in missing, 'duplicate missing outcome')
            require(issue.get('criticality') in ('critical', 'non_critical'), 'missing outcome criticality')
            missing[oid] = severity
        else:
            require(bool(affected), 'criterion issue needs affected rows')
        if kind == 'duplicate':
            mode = issue.get('duplicate_kind')
            require(mode in {'COMPLETELY_REDUNDANT', 'OVERLAP_GROUP'},
                    'duplicate findings need COMPLETELY_REDUNDANT or OVERLAP_GROUP')
            if mode == 'OVERLAP_GROUP':
                group = issue.get('overlap_group_id')
                prose(group, 'overlap_group_id')
                require(len(affected) >= 2 and group not in overlap_groups,
                        'overlap group needs at least two rows and a unique ID')
                require(not set(affected) & overlap_members,
                        'overlap groups cannot share rows; use one canonical group')
                overlap_groups[group] = affected
                overlap_members.update(affected)
            else:
                redundant_rows.update(affected)
        for row in affected:
            if levels[severity] > levels.get(rows.get(row), 0):
                rows[row] = severity
            if impact != 'precision_only':
                acceptance.add(row)
    predicted = record.get('predicted_all_fail')
    require(isinstance(predicted, list),
            'record predicted_all_fail; use an empty array when no criterion is predicted to fail every run')
    all_fail_rows = []
    for entry in predicted:
        require(isinstance(entry, dict), 'predicted all-fail entry must be an object')
        row = entry.get('row')
        require(type(row) is int and 1 <= row <= n and row not in all_fail_rows,
                'predicted all-fail rows must be unique actual rows')
        require(entry.get('basis') in ALL_FAIL_BASES, 'unknown predicted all-fail basis')
        prose(entry.get('reason'), 'predicted all-fail')
        require(row in rows, f'R{row}: a predicted all-fail criterion needs its recorded defect')
        all_fail_rows.append(row)
    all_fail_gate = 'FAIL' if len(all_fail_rows) >= 2 else 'PASS'
    # Obvious syntax cannot disappear merely because a reviewer omitted an issue.
    # A phrase inside an exact source name still counts (C9 over C8, local override).
    for row, criterion in enumerate(rubric, 1):
        annotations = criterion.get('annotations') or {}
        fields = [criterion.get('title', '')] + [str(criterion.get(k, annotations.get(k, '')) or '')
                                                 for k in ('justification', 'evidence')]
        # Eval 3 §2.7A scans every field, not only the title (rubric-flow-v2).
        if any(VAGUE.search(text) for text in fields):
            require(any(i['type'] == 'vague_exemplar' and row in i['rows'] for i in issues),
                    f'R{row}: vague exemplar phrase needs its Moderate finding')
    coverage = record.get('coverage')
    require(isinstance(coverage, dict), 'missing coverage ledger')
    required, covered = coverage.get('required_outcomes'), coverage.get('covered_outcomes')
    outstanding = coverage.get('unresolved_outcomes', 0)
    require(type(required) is int and type(covered) is int and required >= 1 and
            0 <= covered <= required and type(outstanding) is int and outstanding >= 0,
            'invalid coverage counts')
    require(required-covered == len(missing)+outstanding, 'coverage contradicts recorded omissions')
    counts = {level: list(rows.values()).count(level)+list(missing.values()).count(level) for level in levels}
    # QC counts a set of overlapping criteria as one Moderate issue. Members
    # already counted at Major are excluded; a completely redundant criterion
    # or separate Moderate defect still has its own row-level count.
    other_moderate = set(redundant_rows)
    for issue in issues:
        if issue['type'] != 'duplicate' and SEVERITIES[issue['type']] == 'Moderate':
            other_moderate.update(issue['rows'])
    counted_groups = {}
    for group, members in overlap_groups.items():
        eligible = [r for r in members if rows.get(r) == 'Moderate' and r not in other_moderate]
        counts['Moderate'] -= max(0, len(eligible)-1)
        counted_groups[group] = {'members': members, 'eligible_rows': eligible,
                                 'numerator': 1 if eligible else 0}
    major, moderate, minor = (counts[k] for k in ('Major', 'Moderate', 'Minor'))
    # Stricter than QC (QC Non-Fail: <=10% Major, <=15% Moderate, 5-20% Minor):
    # any Major or Moderate fails; Minor on 5-10% of rows is Non-Fail; over 10% fails.
    quality = ('FAIL' if major or moderate or minor * 100 > 10 * n
               else 'NON-FAIL' if minor * 100 >= 5 * n else 'PASS')
    weights = weight_tally(record.get('weight_reviews'), rubric)
    gates = record.get('hard_gates')
    require(isinstance(gates, dict) and set(gates) == set(GATES), 'record the eight static review gates')
    forced = {}
    gate_for = {'incorrect': 'accuracy_acceptance', 'unauthorized': 'accuracy_acceptance',
                'unobservable': 'accuracy_acceptance', 'overly_specific': 'accuracy_acceptance',
                'overly_broad': 'accuracy_acceptance', 'non_atomic': 'atomicity',
                'not_self_contained': 'self_containment', 'missing_coverage': 'coverage',
                'duplicate': 'duplicates'}
    for issue in issues:
        if issue['type'] in gate_for:
            forced[gate_for[issue['type']]] = True
    if weights['one_level_rows'] or weights['two_level_rows']:
        forced['weights'] = True
    for name, gate in gates.items():
        require(isinstance(gate, dict) and gate.get('result') in ('PASS', 'FAIL', 'UNRESOLVED'),
                'invalid static gate')
        prose(gate.get('reason'), name)
        if name in forced:
            require(gate['result'] == 'FAIL', name + ' contradicts recorded defects')
    require(record.get('hard_gate_score') is None,
            'readiness gates do not invent an additional QC score')
    dims = record.get('dimensions')
    require(isinstance(dims, dict) and set(dims) == set(DIMENSIONS), 'record six static QC dimensions')
    for name, dim in dims.items():
        require(isinstance(dim, dict) and type(dim.get('score')) is int and 1 <= dim['score'] <= 5,
                name + ' needs a 1–5 score')
        prose(dim.get('reason'), name)
    allowed = {'PASS': {5}, 'NON-FAIL': {3, 4}, 'FAIL': {1, 2}}
    require(dims['overall_quality']['score'] in allowed[quality], 'wrong overall quality band')
    require(dims['criteria_weights']['score'] in ({4} if weights['band'] == 'NON-FAIL' else allowed[weights['band']]),
            'wrong Criteria Weights band')
    facts = [title_facts(r.get('title', '')) for r in rubric]
    bad = {i for i, f in enumerate(facts, 1) if f['subject'] == 'NON_AGENT' or f['tool_names']}
    if checked:
        bad.update(checked['wording_fail_rows'])
        if checked['negative_fail_rows']:
            require(dims['negative']['score'] in (1, 2), 'prohibition-only acceptance requires Negative FAIL')
        off = checked['wording_nonstandard_rows']
        if off and not bad:
            # Stricter than QC: off-pattern but agent-centric titles are Non-Fail (3)
            # only on 10% or fewer rows; more fails.
            if len(off) * 100 <= 10 * n:
                require(dims['agent_centric']['score'] == 3, 'off-pattern Agent phrasing on <=10% of rows is NON-FAIL 3')
            else:
                require(dims['agent_centric']['score'] in (1, 2), 'off-pattern Agent phrasing on >10% of rows fails')
    phrasing_rows = {r for i in issues if i['type'] == 'non_agent_centric' for r in i['rows']}
    if bad or phrasing_rows:
        require(dims['agent_centric']['score'] in (1, 2), 'non-Agent subject requires FAIL')
    # Stricter than QC: exactly one missing ordering check (and no invalid Process row)
    # is Non-Fail 3; two or more missing, or any invalid Process row, fails.
    require(dims['process']['score'] in (1, 2, 3, 5), 'Process Rubrics score must be 1-2, 3 or 5')
    if dims['process']['score'] == 3:
        require(record.get('missing_process_checks') == 1,
                'Process NON-FAIL 3 requires missing_process_checks == 1')
    require(dims['agent_centric']['score'] in (1, 2, 3, 5), 'Agent-Centric Phrasing score must be 1-2, 3 or 5')
    if dims['agent_centric']['score'] == 3:
        require(bool(checked and checked['wording_nonstandard_rows']) and not bad,
                'Agent-Centric NON-FAIL 3 is only for off-pattern Agent titles')
    require(bad <= phrasing_rows, 'non-Agent subject or tool name needs a non_agent_centric issue on rows '
            + ', '.join(map(str, sorted(bad - phrasing_rows))))
    categories = [r.get('category', r.get('annotations', {}).get('rubric_category', '')).lower() for r in rubric]
    balance_bad = 'outcome' not in categories
    require(dims['category_balance']['score'] in ({1, 2} if balance_bad else {5}), 'wrong category balance')
    unresolved = record.get('unresolved')
    require(isinstance(unresolved, list) and all(isinstance(v, str) and v.strip() for v in unresolved),
            'unresolved must describe remaining checks')
    check_pending = checked['unresolved'] if checked else []
    partial = bool(unresolved or check_pending or outstanding or weights['unresolved_rows']) or any(
        g['result'] == 'UNRESOLVED' for g in gates.values())
    score = min(d['score'] for d in dims.values())
    if all_fail_gate == 'FAIL':
        score = min(score, 2)
    verdict = 'FAIL' if score <= 2 else 'NON-FAIL' if score < 5 or partial else 'PASS'
    if partial and verdict != 'FAIL':
        score = None
    failed_gate = any(g['result'] == 'FAIL' for g in gates.values())
    repairs = sorted(set(rows) | bad | set(weights['one_level_rows']) | set(weights['two_level_rows']))
    ready = verdict == 'PASS' and not partial and not issues and not failed_gate and not repairs
    return dict(criterion_count=n, denominator=n, missing_outcome_count=len(missing),
        severity_counts=counts, counted_rows=sorted(rows), overlap_groups=counted_groups,
        acceptance_impact_rows=sorted(acceptance),
        absolute_rule_triggered=False, fractions={'major':[major,n], 'major_moderate':[major+moderate,n],
        'all':[major+moderate+minor,n]}, coverage_ratio=[covered,required], overall_quality_band=quality,
        criteria_weights=weights, forced_gates=sorted(forced), gate_tier='localized' if failed_gate else 'none',
        catastrophic_reasons=[], provenance_counts=provenance, wording_fail_rows=sorted(bad),
        check_unresolved=check_pending, fact_results=checked.get('fact_results', []) if checked else [],
        predicted_all_fail_rows=sorted(all_fail_rows), all_fail_gate=all_fail_gate,
        repairs=repairs, verdict=verdict, verdict_score=score,
        execution_status='PARTIAL' if partial else 'COMPLETE', repair_free=ready)
