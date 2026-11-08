"""Production integration of stage evidence, design review and platform handoff.

Readiness is computed from immutable stage records; it is never an upstream input.
The local gate runs without a platform, whereas platform checks consume real,
reviewed evidence and never perform deployment.
"""
from pathlib import Path
import hashlib
import json
import stage_evidence as evidence

CONFIG = 'Working_Files/00_Readiness_Config.json'
DESIGN_STAGES = {'scenario': 'scenario', 'injection': 'injection',
                 'prompt-check': 'prompt', 'rubric-check': 'rubric'}
LOCAL_STAGES = ('scenario', 'injection', 'error-async', 'prompt-writing', 'prompt-check',
                'humantime', 'oe-writing', 'oe-check', 'rubric-writing', 'rubric-check')


def read(path):
    return json.loads(Path(path).read_text())


def config(task_dir):
    value = read(Path(task_dir) / CONFIG)
    if value.get('schema_version') != 1 or not isinstance(value.get('revision'), str) or not value['revision'].strip():
        raise ValueError('readiness config requires schema_version 1 and explicit revision')
    if value.get('injection') not in ('required', 'not_used'):
        raise ValueError('readiness config needs explicit injection required/not_used')
    if value['injection'] == 'not_used' and not value.get('no_injection_reason'):
        raise ValueError('no injection requires its applicability reason')
    return value


def policy_identity(gate):
    paths = [gate.BUNDLE / 'references/v3_policy.json', gate.WS / 'Evals/references/prompt_rubric_release.json']
    return {str(p.relative_to(gate.WS)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}


def tool_identity(gate, stage):
    # A stage check implementation change merits review, never a fabricated newer-policy claim.
    names = ['stage_gate.py', 'readiness_controls.py', 'stage_evidence.py', 'v3_artifact_checks.py']
    if stage in DESIGN_STAGES:
        names += ['design_readiness.py', 'hardness_v2_check.py']
    if stage in ('allfail', 'difficulty', 'hardening', 'release'):
        names += ['trajectory_ledger.py', 'difficulty_stats.py']
    return {name: hashlib.sha256((gate.HERE / name).read_bytes()).hexdigest() for name in names}


def inputs(gate, ctx, stage):
    result = gate.certificate_digests(ctx, stage)
    cfg = config(ctx.td)
    # The revision labels this record; later baseline intake must not stale design.
    result['__injection_state__'] = evidence.content_id({k: cfg.get(k) for k in ('injection', 'no_injection_reason')})
    review = DESIGN_STAGES.get(stage)
    if review:
        path = ctx.td / f'Working_Files/hardness_reviews/{review}.json'
        result['__hardness_review__'] = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else 'missing'
    if stage == 'hardening':
        path = ctx.td / 'Working_Files/mode_b_request.json'
        result['__mode_b_request__'] = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else 'missing'
        if path.is_file():
            request = read(path)
            names = [request.get(key) for key in ('data_path', 'receipt', 'verifier')]
            names += request.get('trajectories', [])
            for name in names:
                if isinstance(name, str):
                    source = (ctx.td / name).resolve()
                    source.relative_to(ctx.td.resolve())
                    result['mode_b:' + name] = hashlib.sha256(source.read_bytes()).hexdigest() if source.is_file() else 'missing'
    return result


def parents(gate, ctx, stage):
    result = {}
    for upstream, name in gate.STAGES[stage]['upstream']:
        if name.endswith('?') and not ctx.p(name[:-1]).exists():
            continue
        record = evidence.latest(ctx.td, upstream)
        if record is None:
            raise ValueError(f'{upstream}: current stage attestation missing; historical paste cannot certify new work')
        errors = current_errors(gate, ctx, upstream, record)
        if errors:
            raise ValueError(f'{upstream}: ' + '; '.join(errors))
        result[upstream] = record['evidence_id']
    return result


def current_errors(gate, ctx, stage, record=None):
    record = record or evidence.latest(ctx.td, stage)
    errors = evidence.validate(record, task_id=evidence.task_identity(ctx.td), stage=stage,
                             inputs=inputs(gate, ctx, stage), upstream=parents(gate, ctx, stage),
                             tool_identity=tool_identity(gate, stage), policy_identity=policy_identity(gate))
    expected_producer = {'name': 'stage_gate', 'stage': stage, 'rerun': 'all', 'verdict': 'PASS'}
    if not isinstance(record, dict) or record.get('producer') != expected_producer:
        errors.append('UNVERIFIED: a full stage_gate PASS attestation is required, not an imported review')
    required = gate.STAGES[stage]['outputs'] + gate.STAGES[stage]['inputs']
    errors.extend('required artifact missing: ' + name for name in required if not ctx.p(name).exists())
    checked = {row.get('id'): row.get('outcome') for row in (record or {}).get('checks', [])}
    if any(checked.get(cid) != 'PASS' for cid in ('structure.inputs', 'structure.outputs', 'readiness.context')):
        errors.append('UNVERIFIED: required stage execution checks absent')
    # Hashes of review JSON alone cannot pin the supporting files it references.
    # This is a bounded local review check, not a repeat platform run or base scan.
    if stage in DESIGN_STAGES:
        errors.extend(design_review(gate, ctx, DESIGN_STAGES[stage])['blockers'])
    if stage == 'hardening':
        errors.extend(mode_b_review(ctx)['blockers'])
    return errors


def design_review(gate, ctx, stage):
    from design_readiness import evaluate
    cfg = config(ctx.td)
    name = '01_Hardness_Manifest.draft.json' if stage == 'scenario' else '01_Hardness_Manifest.json'
    manifest = read(ctx.p(name))
    review = read(ctx.td / f'Working_Files/hardness_reviews/{stage}.json')
    def text(name):
        path = ctx.p(name)
        return path.read_text() if path.is_file() else ''
    rubric = read(ctx.p('09_Rubrics.json')) if stage in ('rubric', 'baseline') else None
    builder = read(ctx.td / 'Working_Files/09_Builder_Export.json') if stage == 'baseline' else None
    return evaluate(stage, manifest, read(ctx.p(gate.SURFACE)), review,
                    sql_text=text('01_Universe_Inject.sql'), prompt=text('04_Prompt.txt'),
                    rubric=rubric, builder_rubric=builder, task_dir=ctx.td,
                    task_id=evidence.task_identity(ctx.td), revision=cfg['revision'],
                    difficulty_mode=ctx.context['difficulty_mode'])


def mode_b_review(ctx):
    from mode_b_report import from_request
    from trajectory_ledger import binding_bundle_hash
    request = read(ctx.td / 'Working_Files/mode_b_request.json')
    cfg = config(ctx.td)
    if request.get('task_id') != evidence.task_identity(ctx.td) or request.get('revision') != cfg['revision']:
        raise ValueError('Mode B request task/revision mismatch')
    precheck = request.get('precheck') is True
    if request.get('bundle_hash') != binding_bundle_hash(ctx.td, None if precheck else ctx.p('09_Rubrics.json'),
                                                       stage='precheck' if precheck else 'baseline'):
        raise ValueError('Mode B request bundle identity mismatch')
    return from_request(request, ctx.td, context=ctx.context)


def check_stage(gate, ctx):
    """Called by real V3 gates, not archival fixture diagnostics."""
    try:
        config(ctx.td)
        parents(gate, ctx, ctx.stage)
        ctx.add('readiness.context', True, 'explicit task/revision and current upstream evidence verified')
        if ctx.stage in DESIGN_STAGES:
            result = design_review(gate, ctx, DESIGN_STAGES[ctx.stage])
            ctx.add('readiness.hardness_review', result['verdict'] == 'PASS',
                    '; '.join(result['blockers']) or 'current evidenced review; deferred: ' + str(result['deferred']))
        if ctx.stage == 'hardening':
            result = mode_b_review(ctx)
            ctx.add('readiness.mode_b', result['verdict'] == 'PASS',
                    '; '.join(result['blockers']) or result['evidence_scope'] + ': current structured diagnosis')
        if ctx.stage in ('allfail', 'difficulty'):
            result = readiness(gate, ctx, 'platform', post_baseline=True)
            ctx.add('readiness.bound_baseline', result['ready'], '; '.join(result['errors']) or 'current bound baseline')
        if ctx.stage == 'release':
            result = readiness(gate, ctx, 'platform', post_baseline=True)
            ctx.add('readiness.platform', result['ready'], '; '.join(result['errors']) or 'current platform evidence')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        ctx.add('readiness.evidence', False, str(exc))


def attest(gate, ctx, reviewer):
    if not getattr(ctx, 'executed_gate', False) or ctx.rerun != 'all' or gate.verdict_of(ctx) != 'PASS' or ctx.selftest:
        raise ValueError('attestation requires a completed production stage_gate full PASS')
    cfg = config(ctx.td)
    checks = []
    for row in ctx.res:
        check = {'id': row['id'], 'outcome': row['status'], 'evidence_refs': row['locations']}
        if row['status'] in ('WARN', 'SKIP'):
            # Existing policy advisory findings remain advisory; mandatory hardness
            # warnings have separately checked evidence-backed dispositions.
            check['disposition'] = {'kind': 'existing-policy-advisory', 'reason': row['detail']}
        checks.append(check)
    availability = []
    if ctx.stage in DESIGN_STAGES:
        reviewed = design_review(gate, ctx, DESIGN_STAGES[ctx.stage])
        for n, item in enumerate(reviewed['deferred']):
            availability.append({'id': f'hardness:{n}', 'state': 'deferred',
                                 'required_at': item['required_at'], 'reason': str(item)})
    return evidence.attest(ctx.td, stage=ctx.stage, revision=cfg['revision'],
                           inputs=inputs(gate, ctx, ctx.stage), upstream=parents(gate, ctx, ctx.stage),
                           checks=checks, availability=availability, reviewer=reviewer,
                           producer={'name': 'stage_gate', 'stage': ctx.stage, 'rerun': 'all', 'verdict': 'PASS'},
                           tool_identity=tool_identity(gate, ctx.stage), policy_identity=policy_identity(gate))


def readiness(gate, ctx, kind='local', post_baseline=False):
    from platform_handoff import validate
    errors, stages = [], {}
    cfg = config(ctx.td)
    stages_to_check = list(LOCAL_STAGES)
    if ctx.p('01a_Hardening_Report.md').exists():
        stages_to_check.append('hardening')
    for stage in stages_to_check:
        try:
            problems = current_errors(gate, ctx, stage)
        except (OSError, ValueError, KeyError, TypeError) as exc:
            problems = [str(exc)]
        stages[stage] = 'CURRENT' if not problems else 'MISSING_OR_STALE'
        errors.extend(f'{stage}: {p}' for p in problems)
    local_ready = not errors
    if kind == 'platform':
        try:
            reviewed = design_review(gate, ctx, 'baseline')
            errors.extend(reviewed['blockers'])
            receipt = read(ctx.td / 'Working_Files/Platform_Handoff.json')
            baseline_review = read(ctx.td / 'Working_Files/hardness_reviews/baseline.json')
            decisive = {row.get('deciding_evidence', {}).get('record_id')
                        for row in baseline_review.get('mechanisms', {}).values()}
            decisive.discard(None)
            readable = set(receipt.get('readability', {}).get('decisive_records', []))
            if not decisive <= readable:
                errors.append('platform readability omits decisive records: ' + str(sorted(decisive - readable)))
            from trajectory_ledger import binding_bundle_hash, bind_verifier_exports, export_run_ids
            bundle_hash = binding_bundle_hash(ctx.td, ctx.p('09_Rubrics.json'))
            run_ids = None
            if post_baseline:
                binding_path = ctx.td / 'Working_Files/Verifier_Export_Binding.json'
                binding = bind_verifier_exports(ctx.p('10_Baseline_Verifier_Results.md'),
                    sorted(ctx.p('07_Baseline_Trajectories').glob('*.json')),
                    task_id=evidence.task_identity(ctx.td), revision=cfg['revision'], bundle_hash=bundle_hash,
                    receipt=binding_path if binding_path.exists() else None, task_dir=ctx.td)
                run_ids = []
                for path in binding['runs'].values():
                    ids = export_run_ids(path)
                    if len(ids) == 1:
                        run_ids.append(next(iter(ids)))
                    else:
                        # Export hash is an explicit, stable alternative when the
                        # platform format has no single reliable run identifier.
                        run_ids.append('sha256:' + hashlib.sha256(path.read_bytes()).hexdigest())
            sql = ctx.p('01_Universe_Inject.sql')
            if cfg['injection'] == 'required' and not sql.is_file():
                errors.append('required injection SQL is missing')
            if cfg['injection'] == 'not_used' and sql.exists():
                errors.append('no-injection choice conflicts with SQL artifact')
            errors.extend(validate(receipt, task_dir=ctx.td, task_id=evidence.task_identity(ctx.td),
                                   revision=cfg['revision'], universe=ctx.context['universe']['key'],
                                   sql_hash=hashlib.sha256(sql.read_bytes()).hexdigest() if sql.is_file() else None,
                                   bundle_hash=bundle_hash, run_ids=run_ids))
            local_release = policy_identity(gate)
            compatibility = evidence.evaluator_compatibility(local_release, receipt.get('evaluator_release'),
                                                              receipt.get('evaluator_compatibility_review'), task_dir=ctx.td)
            if compatibility['status'] not in ('MATCH', 'REVIEWED_COMPATIBLE'):
                errors.append('evaluator release: ' + compatibility['status'])
        except (OSError, ValueError, KeyError, TypeError) as exc:
            errors.append('PLATFORM_PENDING: ' + str(exc))
    return {'ready': not errors, 'local_build_ready': local_ready, 'kind': kind,
            'platform_baseline_ready': kind == 'platform' and not errors, 'stages': stages, 'errors': errors}
