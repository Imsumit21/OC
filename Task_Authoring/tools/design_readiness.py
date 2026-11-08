#!/usr/bin/env python3
"""Stage-aware review of difficulty evidence; never invents outcomes or weights.

Review schema 1 binds exact stage inputs with input_hashes(). Semantic judgments
are signed, evidence-backed reviews, not claims that lexical checks prove truth.
The stage gate remains responsible for the ordinary manifest/rubric validators.
"""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import hardness_v2_check
from gradable_surface import WORK_BANDS

STAGES = ('scenario', 'injection', 'prompt', 'rubric', 'baseline')
ALIASES = {'design': 'scenario', 'prompt-writing': 'prompt', 'prompt-check': 'prompt',
           'rubric-writing': 'rubric', 'rubric-check': 'rubric', 'pre-baseline': 'baseline'}


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()).hexdigest()


def input_hashes(stage, manifest, surface, *, sql_text='', prompt='', rubric=None, builder_rubric=None):
    stage = ALIASES.get(stage, stage)
    if stage not in STAGES:
        raise ValueError('unknown design review stage: ' + stage)
    values = {'manifest': manifest, 'surface': surface}
    if STAGES.index(stage) >= 1:
        values['sql'] = sql_text
    if STAGES.index(stage) >= 2:
        # Reuse the certificate normalization, so a pasted result is not an input edit.
        from stage_gate import digest_text
        values['prompt'] = digest_text(prompt)
    if STAGES.index(stage) >= 3:
        values['rubric'] = rubric
    if stage == 'baseline':
        values['builder_rubric'] = builder_rubric
    return {key: digest(value) for key, value in values.items()}


def evidence_ok(item, root):
    """Evidence points to actual immutable bytes under the selected task only."""
    if not isinstance(item, dict) or not item.get('reason') or not item.get('evidence'):
        return False
    if str(item['reason']).strip().lower() in ('reviewed', 'ok', 'accepted', 'n/a'):
        return False
    if root is None:
        return False
    root = Path(root).resolve()
    for ref in item['evidence']:
        if not isinstance(ref, dict) or not ref.get('path') or not ref.get('sha256'):
            return False
        path = (root / ref['path']).resolve()
        if not path.is_relative_to(root) or not path.is_file():
            return False
        if hashlib.sha256(path.read_bytes()).hexdigest() != ref['sha256']:
            return False
    return True


def evaluate(stage, manifest, surface, review, *, sql_text='', prompt='', rubric=None,
             builder_rubric=None, task_dir=None, task_id=None, revision=None, difficulty_mode=None):
    stage = ALIASES.get(stage, stage)
    expected = input_hashes(stage, manifest, surface, sql_text=sql_text, prompt=prompt,
                            rubric=rubric, builder_rubric=builder_rubric)
    blockers, deferred = [], []
    def require(ok, name):
        if not ok:
            blockers.append(name)
    if not isinstance(review, dict):
        return {'verdict': 'FAIL', 'blockers': ['missing applicable hardness review'], 'deferred': [], 'input_hashes': expected}
    require(review.get('schema_version') == 1, 'review schema version')
    require(review.get('stage') == stage, 'review is for a different stage')
    require(bool(task_id) and review.get('task_id') == task_id, 'review task identity')
    require(bool(revision) and review.get('revision') == revision, 'review revision identity')
    require(bool(review.get('reviewer')), 'missing reviewer')
    require(review.get('input_hashes') == expected, 'stale or incomplete hardness review inputs')
    rank = STAGES.index(stage)
    mechanisms = {m['id']: m for m in manifest.get('mechanism_portfolio', []) if isinstance(m, dict) and m.get('id')}
    slots = {s['id']: s for s in (surface or {}).get('slots', []) if isinstance(s, dict) and s.get('id')}
    selected = review.get('diversity_channels', [])
    mode = str(difficulty_mode or manifest.get('difficulty_mode', '')).lower()
    require(review.get('difficulty_mode') == mode, 'review difficulty mode differs from assignment')
    require(mode in ('easy', 'medium', 'hard'), 'assigned difficulty mode required')
    minimum = 4 if mode == 'hard' else 3
    require(len(set(selected)) >= minimum, f'at least {minimum} independent loss channels required')
    require(set(selected) <= mechanisms.keys(), 'unknown diversity channel')
    records = review.get('mechanisms', {})
    require(set(records) == set(mechanisms), 'review must cover exactly the selected manifest mechanisms')
    deciders = []
    for mid, mechanism in mechanisms.items():
        row = records.get(mid, {})
        for field in ('initial_plausible_answer', 'deciding_evidence', 'authority_chronology',
                      'fair_discovery_path', 'changed_outcome', 'independent_operation'):
            require(evidence_ok(row.get(field), task_dir), f'{mid}: missing evidenced {field}')
        changed = row.get('changed_outcome', {})
        require('before' in changed and 'after' in changed and changed.get('before') != changed.get('after'),
                f'{mid}: no real outcome change')
        covered = row.get('outcome_slots', [])
        require(bool(covered) and set(covered) <= slots.keys(), f'{mid}: unknown or absent outcome slots')
        for sid in covered:
            slot = slots.get(sid, {})
            require(slot.get('weight') == WORK_BANDS.get(slot.get('work_kind')) and bool(slot.get('work_reason')),
                    f'{sid}: weight must follow work kind')
            require(mid in slot.get('mechanisms', []) or mid in slot.get('flipped_by', []), f'{mid}: outcome {sid} not linked by surface')
        # Concrete access defects can never be deferred or waived.
        access = row.get('access', {})
        require(access.get('status') not in ('inaccessible', 'unreachable', 'impossible'), f'{mid}: inaccessible required evidence')
        if rank == 0 and access.get('status') == 'deferred' and access.get('required_at') == 'injection':
            deferred.append({'mechanism': mid, 'evidence': 'materialization/readability', 'required_at': 'injection'})
        else:
            require(access.get('status') == 'verified' and evidence_ok(access, task_dir), f'{mid}: required readability evidence unresolved')
        retrieval = row.get('natural_retrieval', {})
        if rank == 0 and retrieval.get('status') == 'deferred' and retrieval.get('required_at') == 'injection':
            deferred.append({'mechanism': mid, 'evidence': 'natural retrieval', 'required_at': 'injection'})
        else:
            require(evidence_ok(retrieval, task_dir) and bool(retrieval.get('query')) and
                    isinstance(retrieval.get('returned_ids'), list) and bool(retrieval.get('assessment')),
                    f'{mid}: natural search/list results need semantic review')
        if mid in selected:
            require(row.get('channel_kind') not in ('volume', 'decoy', 'routine'), f'{mid}: routine work is not a diversity channel')
            independent = row.get('independent_operation', {})
            require(set(independent.get('others_solvable_if_missed', [])) >= set(selected) - {mid}, f'{mid}: independence counterfactual incomplete')
            deciders.append(row.get('deciding_evidence', {}).get('record_id'))
            pair = row.get('outcome_pair', {})
            pair_ids = pair.get('slots', [])
            require(len(pair_ids) == 2 and len(set(pair_ids)) == 2 and set(pair_ids) <= set(covered), f'{mid}: needs two independent existing outcomes')
            if len(pair_ids) == 2 and all(s in slots for s in pair_ids):
                left, right = (slots[s] for s in pair_ids)
                require(left.get('fact_id', left.get('selector')) != right.get('fact_id', right.get('selector')),
                        f'{mid}: duplicate fact cannot form outcome pair')
                for slot in (left, right):
                    span = slot.get('incorporating_span')
                    require(bool(span) and (rank < 2 or span in prompt), f'{slot["id"]}: outcome not requested/incorporated')
            require(evidence_ok(pair, task_dir) and bool(pair.get('left_pass_right_fail')) and bool(pair.get('right_pass_left_fail')),
                    f'{mid}: independent passability needs both counterexamples')
    require(all(deciders) and len(set(deciders)) == len(deciders), 'diversity channels share or omit deciding records')
    advisory = hardness_v2_check.run(manifest, sql_text, prompt if rank >= 2 else '', surface)
    dispositions = review.get('dispositions', {})
    for finding in advisory['flags'] + advisory['unresolved']:
        key = finding['check'] + ':' + str(finding.get('node') or '-')
        disp = dispositions.get(key, {})
        if rank == 0 and finding in advisory['unresolved'] and disp.get('status') == 'deferred' and disp.get('required_at') == 'injection':
            deferred.append({'finding': key, 'required_at': 'injection'})
            continue
        require(disp.get('status') in ('accepted', 'not_applicable', 'repaired') and evidence_ok(disp, task_dir),
                key + ': warning requires substantive current disposition')
    require(not advisory.get('malformed'), 'malformed manifest cannot be dispositioned')
    if rank >= 2:
        semantic = review.get('semantic_prompt_review', {})
        require(semantic.get('leaks_solution') is False and evidence_ok(semantic, task_dir), 'semantic prompt leakage review required')
    if rank >= 3:
        coverage = review.get('coverage', {})
        rubric_rows = rubric if isinstance(rubric, list) else ((rubric or {}).get('rubrics') or (rubric or {}).get('criteria') or [])
        row_ids = {r.get('id', f'R{i}') for i, r in enumerate(rubric_rows, 1)}
        row_weights = {r.get('id', f'R{i}'): r.get('weight') for i, r in enumerate(rubric_rows, 1)}
        mapped_bands = {}
        for sid, slot in slots.items():
            entry = coverage.get(sid, {})
            direct = bool(entry.get('rubric_ids')) and set(entry['rubric_ids']) <= row_ids
            if direct:
                for rid in entry['rubric_ids']:
                    mapped_bands.setdefault(rid, []).append(WORK_BANDS.get(slot.get('work_kind'), 0))
            sampled = (slot.get('role') == 'sample' and entry.get('status') == 'sampled_out' and evidence_ok(entry, task_dir))
            not_incorporated = (entry.get('status') == 'not_incorporated' and evidence_ok(entry, task_dir) and
                                (not slot.get('incorporating_span') or slot['incorporating_span'] not in prompt))
            require(direct or sampled or not_incorporated, f'{sid}: required outcome/write lacks coverage')
        require(set(coverage) == set(slots), 'stale or incomplete coverage')
        for rid, bands in mapped_bands.items():
            weight = row_weights[rid]
            require(type(weight) is int and weight in (1, 3, 5) and weight <= max(bands),
                    f'{rid}: final weight exceeds covered work-kind band')
        # Distinct provisional slots do not prove distinct final grading. A single
        # criterion mapped to both sides collapses the intended two-outcome pair.
        # Each side needs at least one criterion that does not also grade the other.
        for mid in selected:
            pair_ids = records.get(mid, {}).get('outcome_pair', {}).get('slots', [])
            if len(pair_ids) == 2:
                left_rows, right_rows = (set(coverage.get(sid, {}).get('rubric_ids', [])) & row_ids
                                         for sid in pair_ids)
                require(bool(left_rows - right_rows) and bool(right_rows - left_rows),
                        f'{mid}: paired outcomes need independently covering final criteria')
    if stage == 'baseline':
        require(rubric is not None and builder_rubric is not None and digest(rubric) == digest(builder_rubric),
                'builder export differs from reviewed rubric')
    return {'schema_version': 1, 'verdict': 'FAIL' if blockers else 'PASS', 'blockers': blockers,
            'deferred': deferred, 'input_hashes': expected, 'advisory': advisory,
            'forecast': {'status': 'ADVISORY_UNCALIBRATED', 'value': review.get('forecast')}}
