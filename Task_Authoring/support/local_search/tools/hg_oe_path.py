"""Check a source-bound OE execution model without executing workplace actions.

The reviewer maps prose to this internal model. This code checks catalog types,
source values and dependency consistency, not arbitrary semantic correctness.
"""
from dataclasses import dataclass
from decimal import Decimal
import json
from pathlib import Path
import re

from hg_review_evidence import links, authority
from hg_source_checks import metadata_source, check_absence

FEASIBILITY_FIELDS = ('data_access', 'tool_capability', 'preconditions', 'completion')


@dataclass(frozen=True)
class Symbol:
    """A future tool result, never a fabricated existing identifier."""
    name: str
    type: str


def need(ok, message):
    if not ok:
        raise ValueError('OE execution model: ' + message)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def pointer(value, path):
    need(isinstance(path, str) and (path == '' or path.startswith('/')), 'invalid JSON pointer')
    for token in path.split('/')[1:] if path else []:
        need(not re.search(r'~(?![01])', token), 'invalid pointer escape')
        token = token.replace('~1', '/').replace('~0', '~')
        if isinstance(value, list):
            need(bool(re.fullmatch(r'0|[1-9][0-9]*', token)) and int(token) < len(value), 'pointer does not resolve')
            value = value[int(token)]
        else:
            need(isinstance(value, dict) and token in value, 'pointer does not resolve')
            value = value[token]
    return value


def same(left, right):
    if isinstance(left, bool) or isinstance(right, bool):
        return type(left) is bool and type(right) is bool and left == right
    if isinstance(left, (int, float, Decimal)) and isinstance(right, (int, float, Decimal)):
        return Decimal(str(left)) == Decimal(str(right))
    if isinstance(left, list) and isinstance(right, list):
        return len(left) == len(right) and all(same(a, b) for a, b in zip(left, right))
    if isinstance(left, dict) and isinstance(right, dict):
        return left.keys() == right.keys() and all(same(left[k], right[k]) for k in left)
    return type(left) is type(right) and left == right


def type_matches(value, declared):
    kinds = {part.strip() for part in declared.split('|')}
    if isinstance(value, Symbol):
        if value.type == 'unresolved':
            return None
        return value.type in kinds or 'any' in kinds or (value.type == 'integer' and 'number' in kinds)
    checks = {'any': lambda v: True, 'null': lambda v: v is None,
              'string': lambda v: isinstance(v, str), 'boolean': lambda v: type(v) is bool,
              'integer': lambda v: type(v) is int,
              'number': lambda v: type(v) in (int, float, Decimal),
              'array': lambda v: isinstance(v, list), 'object': lambda v: isinstance(v, dict)}
    if not kinds <= checks.keys():
        return None  # A flattened catalog cannot establish an unlisted type.
    return any(checks[k](value) for k in kinds)


def unresolved(value):
    if isinstance(value, Symbol):
        return value.type == 'unresolved'
    if isinstance(value, dict):
        return any(unresolved(v) for v in value.values())
    if isinstance(value, list):
        return any(unresolved(v) for v in value)
    return False


def task_fingerprints(context):
    """Exclude the OE/receipt itself, avoiding self-referential receipt hashes."""
    from hg_store_input import SLOTS
    keys = {'prompt', 'task-details', 'injection', 'error-async'}
    paths = {f['path'] for k, entry in context['inputs'].items() if k.removeprefix('source:') in keys
             for f in entry.get('files', [])}
    paths.update('Task_Authoring/support/local_search/NO_EVAL_TASK_INPUTS/' + SLOTS[k] for k in keys)
    return {name: value for name, value in context['files'].items() if name in paths}


def validate_path(plan, record, reader, known, root, context):
    need(isinstance(plan, dict), 'path_review is required; missing reviewer metadata is not an OE defect')
    need(type(plan.get('complete')) is bool and text(plan.get('reason')), 'explain the execution-model inventory')
    result = dict(inaccurate=[], minor=[], unresolved=[], checks=[], upstream_blockers=[])

    def issue(code, node, detail, unresolved=False):
        item = dict(code=code, node=node, detail=detail)
        result['unresolved' if unresolved else 'inaccurate'].append(item)

    if not plan['complete']:
        issue('REVIEW_INCOMPLETE', None, plan['reason'], True)

    def evidence(ids, label):
        refs = links(ids, known, label)
        usable = all(s['visibility'] == 'VISIBLE' and not metadata_source(s, root, context) for s in refs)
        if not usable:
            issue('EVIDENCE_UNRESOLVED', label, 'Unavailable or non-primary evidence', True)
        return usable

    def selected(sid, selection):
        need(sid in known, 'source selection needs a known source_id')
        if not evidence([sid], sid):
            return None, False
        raw = reader.quote(known[sid])
        need(raw.strip() == known[sid]['quote'].strip(), 'value checks quote the entire selected source anchor')
        try:
            value = json.loads(raw, parse_float=Decimal)
        except json.JSONDecodeError:
            value = raw.strip()
        return pointer(value, selection), True

    # Service membership comes from the shipped service catalogs, not name prefixes.
    catalog = json.loads((Path(root) / 'Evals/references/tools/catalog.json').read_text())
    catalog = {tool['name']: tool for tool in catalog}
    services = {}
    manifest = json.loads((Path(root) / 'Evals/references/tools/manifest.json').read_text())
    for source in manifest['sources']:
        for tool in json.loads((Path(root) / 'Evals/references/tools' / source['path']).read_text()):
            services.setdefault(tool['name'], set()).add(source['service'])

    nodes = plan.get('nodes')
    need(isinstance(nodes, list), 'nodes must be an array')
    node_map, edges, outputs = {}, {}, {}
    step_ids = {step['id'] for step in record['steps']}
    mapped = set()
    for node in nodes:
        need(isinstance(node, dict) and text(node.get('id')) and re.fullmatch(r'[A-Za-z0-9_-]+', node['id'])
             and node['id'] not in node_map, 'execution node IDs must be unique simple names')
        nid = node['id']; node_map[nid] = node
        refs = node.get('step_ids')
        need(isinstance(refs, list) and refs and len(refs) == len(set(refs)) and all(r in step_ids for r in refs),
             'execution node must map to supplied OE steps')
        mapped.update(refs)
        quote = node.get('oe_quote')
        need(text(quote) and any(quote in s['quote'] and set(refs) <= set(s['step_ids']) for s in record['segments']),
             'execution node needs an exact quote from its supplied OE step')
        need(node.get('mode') in {'TOOL', 'REASONING'}, 'mode must be TOOL or REASONING')
        need(text(node.get('mapping_reason')), 'explain the faithful mapping, including descriptive tool aliases')
        deps = node.get('depends_on')
        need(isinstance(deps, list) and all(isinstance(d, str) for d in deps) and len(deps) == len(set(deps)),
             'depends_on must contain unique node IDs')
        edges[nid] = set(deps)
        params = node.get('parameters', {})
        need(isinstance(params, dict), 'parameters must be an object')

        def refs_in(value):
            if isinstance(value, dict):
                if '$ref' in value:
                    need(set(value) == {'$ref'} and isinstance(value['$ref'], str) and '.' in value['$ref'], 'invalid output reference')
                    edges[nid].add(value['$ref'].split('.', 1)[0])
                else:
                    for v in value.values(): refs_in(v)
            elif isinstance(value, list):
                for v in value: refs_in(v)
        refs_in(params)
        bindings = node.get('input_bindings', [])
        need(isinstance(bindings, list), 'input_bindings must be an array')
        for binding in bindings:
            need(isinstance(binding, dict) and text(binding.get('from_node')) and text(binding.get('output'))
                 and isinstance(binding.get('parameter_pointer'), str) and text(binding.get('reason')), 'invalid input binding')
            edges[nid].add(binding['from_node'])
    need(mapped == step_ids, 'map every supplied step; omissions in reviewer metadata are not authored missing steps')
    # Topological traversal permits descriptive OEs to list independent steps in
    # a different order. References create implicit dependencies automatically.
    ordered, visiting, visited = [], set(), set()
    def visit(nid):
        if nid in visited: return
        if nid in visiting:
            issue('DEPENDENCY_CYCLE', nid, 'The described path depends on its own future result')
            return
        visiting.add(nid)
        for dep in sorted(edges[nid]):
            if dep not in node_map:
                issue('UNKNOWN_DEPENDENCY', nid, 'Reviewer mapping has no producer ' + dep + '; establish whether the supplied OE omits a step', True)
            else: visit(dep)
        visiting.remove(nid); visited.add(nid); ordered.append(nid)
    for nid in node_map: visit(nid)

    def resolve(value, nid):
        if isinstance(value, dict) and '$ref' in value:
            ref = value['$ref']; producer, name = ref.split('.', 1)
            if (producer, name) not in outputs:
                issue('UNAVAILABLE_OUTPUT', nid, 'Reference ' + ref + ' has no available producer/output', True)
                return Symbol(ref, 'unresolved')
            return outputs[producer, name]
        if isinstance(value, dict): return {k: resolve(v, nid) for k, v in value.items()}
        if isinstance(value, list): return [resolve(v, nid) for v in value]
        return value

    for nid in ordered:
        node = node_map[nid]
        params = resolve(node.get('parameters', {}), nid)
        for binding in node.get('input_bindings', []):
            target = (binding['from_node'], binding['output'])
            actual = pointer(params, binding['parameter_pointer'])
            if target not in outputs or unresolved(outputs[target]) or unresolved(actual):
                issue('BINDING_UNRESOLVED', nid, 'The upstream output is unavailable', True)
            elif not same(actual, outputs[target]):
                issue('CHANGED_DOWNSTREAM_VALUE', nid, 'Parameter ' + binding['parameter_pointer'] + ' differs from ' + '.'.join(target))
        if node['mode'] == 'TOOL':
            tool, service = node.get('tool'), node.get('service')
            need(text(tool) and text(service), 'tool nodes need tool and service')
            style = node.get('parameter_style')
            need(style in {'LITERAL', 'DESCRIPTIVE'}, 'parameter_style must be LITERAL or DESCRIPTIVE')
            if style == 'LITERAL':
                payload = node.get('payload_quote')
                need(text(payload) and payload in node['oe_quote'], 'literal payload must quote the actual OE JSON')
                need(same(json.loads(payload), node.get('parameters', {})), 'literal payload was changed during reviewer mapping')
            schema = catalog.get(tool)
            runtime_schema = node.get('runtime_schema')
            verified_runtime_schema = False
            if runtime_schema is not None:
                need(isinstance(runtime_schema, dict), 'runtime_schema needs a source selection')
                value, available = selected(runtime_schema.get('source_id'), runtime_schema.get('pointer', ''))
                if available:
                    need(isinstance(value, dict) and value.get('name') == tool and value.get('service') == service
                         and isinstance(value.get('parameters'), dict), 'runtime schema must identify this tool/service and parameters')
                    schema = value
                    verified_runtime_schema = True
            if schema is None:
                issue('TOOL_NOT_IN_CATALOG', nid, tool + ' is not in the bundled catalog; verify an alias or current runtime schema', True)
            else:
                if not verified_runtime_schema and service not in services.get(tool, set()):
                    issue('WRONG_SERVICE', nid, tool + ' belongs to ' + ', '.join(sorted(services.get(tool, set()))))
                definitions = schema['parameters']
                aliases = node.get('parameter_aliases', {})
                need(isinstance(aliases, dict), 'parameter_aliases must be an object')
                for original, alias in aliases.items():
                    need(style == 'DESCRIPTIVE' and isinstance(alias, dict), 'only descriptive parameter names may be mapped to aliases')
                    canonical = alias.get('canonical')
                    need(original in params and canonical in definitions and canonical not in params and
                         text(alias.get('reason')) and text(alias.get('oe_quote')) and alias['oe_quote'] in node['oe_quote'],
                         'alias must identify an actual supplied parameter and supported canonical name')
                    if evidence(alias.get('source_ids'), nid + '.' + original):
                        result['minor'].append(dict(code='HARMLESS_PARAMETER_ALIAS', node=nid, detail=alias['reason']))
                        params[canonical] = params.pop(original)
                    else:
                        # Do not turn an unverified alias into a demonstrated contract error.
                        params.pop(original)
                for key, value in params.items():
                    if key not in definitions:
                        issue('UNKNOWN_PARAMETER', nid, key + ' is not accepted by the selected tool contract')
                    else:
                        matches = type_matches(value, definitions[key]['type'])
                        if matches is False: issue('PARAMETER_TYPE', nid, key + ' must be ' + definitions[key]['type'])
                        if matches is None: issue('TYPE_UNRESOLVED', nid, key + ' has an unresolved value or unsupported flattened schema type', True)
                absent = [k for k, spec in definitions.items() if spec['required'] == 'required' and k not in params]
                if style == 'LITERAL' and absent:
                    issue('MISSING_CALL_ARGUMENT', nid, 'Literal payload omits required ' + ', '.join(absent))
                # Descriptive OEs need material inputs, not complete API payloads.
                # Their omissions are judged under existing completeness checks.
                result['checks'].append(dict(node=nid, tool=tool, service=service, schema_checked=True,
                                             descriptive_unlisted_inputs=absent if style == 'DESCRIPTIVE' else []))
        out = node.get('outputs')
        need(isinstance(out, dict), 'outputs must name the data consumed downstream (an empty object is allowed)')
        for name, declaration in out.items():
            need(re.fullmatch(r'[A-Za-z0-9_-]+', name) and isinstance(declaration, dict), 'invalid output declaration')
            kind = declaration.get('kind')
            need(kind in {'SOURCE', 'GENERATED', 'UNRESOLVED'}, 'output kind must be SOURCE, GENERATED or UNRESOLVED')
            if kind == 'UNRESOLVED':
                issue('OUTPUT_UNRESOLVED', nid, declaration.get('reason', 'Output evidence unavailable'), True)
                outputs[nid, name] = Symbol(nid + '.' + name, 'unresolved')
            elif kind == 'GENERATED':
                need(declaration.get('type') in {'string','integer','number','array','object','boolean'}
                     and text(declaration.get('reason')), 'generated output needs a type and creation/derivation reason')
                available = evidence(declaration.get('source_ids'), nid + '.' + name)
                outputs[nid, name] = Symbol(nid + '.' + name, declaration['type'] if available else 'unresolved')
            else:
                value, available = selected(declaration.get('source_id'), declaration.get('pointer', ''))
                if available:
                    outputs[nid, name] = value
                    if 'expected' in declaration:
                        quote = declaration.get('expected_quote')
                        need(text(quote) and quote in node['oe_quote'], 'expected value must quote the actual OE')
                        try: quoted = json.loads(quote)
                        except json.JSONDecodeError: quoted = quote
                        need(same(quoted, declaration['expected']), 'expected value differs from the quoted OE')
                        if not same(value, declaration['expected']):
                            issue('WRONG_EXPECTED_DATA', nid, name + ' differs from the selected primary source')
                else:
                    outputs[nid, name] = Symbol(nid + '.' + name, 'unresolved')

    feasibility = plan.get('feasibility')
    need(isinstance(feasibility, dict) and set(feasibility) == set(FEASIBILITY_FIELDS), 'review data/access, capability, preconditions and completion')
    blocked = set()
    for field, check in feasibility.items():
        need(isinstance(check, dict) and text(check.get('reason')) and check.get('result') in {'SUPPORTED','BLOCKED','UNRESOLVED','INCOMPLETE'}, 'invalid feasibility check')
        if check['result'] == 'UNRESOLVED': issue('FEASIBILITY_UNRESOLVED', field, check['reason'], True)
        elif check['result'] == 'INCOMPLETE':
            need(any(r['result'] == 'MISSING' for r in record['coverage']) or
                 any(c['result'] == 'MISSING' for s in record['steps'] for c in s['checks'].values()) or
                 any(s['role'] == 'RESPONSE_DESCRIPTION' for s in record['segments']),
                 'INCOMPLETE needs a recorded authored omission, not missing reviewer evidence')
        else:
            available = evidence(check.get('source_ids'), field)
            need(check['result'] != 'BLOCKED' or check.get('evidence_check') is not None,
                 'blocked feasibility needs direct contradiction or scope-bound absence evidence')
            if check.get('evidence_check') is not None:
                gaps = check_absence(check['evidence_check'], reader, known, root, context)
                for gap in gaps: issue('FEASIBILITY_UNRESOLVED', field, gap, True)
                available = available and not gaps
            if available and check['result'] == 'BLOCKED':
                blocked.add(field); issue('INFEASIBLE_STEP', field, check['reason'])
    runtime = plan.get('runtime')
    need(isinstance(runtime, dict) and runtime.get('status') in {'NOT_NEEDED','UNAVAILABLE','OBSERVED'}
         and text(runtime.get('reason')), 'record whether targeted runtime evidence is needed')
    if runtime['status'] == 'UNAVAILABLE': issue('RUNTIME_UNRESOLVED', None, runtime['reason'], True)
    if runtime['status'] == 'OBSERVED':
        need(runtime.get('effect') == 'READ_ONLY', 'OE validation never executes workplace writes')
        receipt, available = selected(runtime.get('receipt_source_id'), runtime.get('receipt_pointer', ''))
        refs = links(runtime.get('bound_source_ids'), known, 'runtime source bindings')
        need(all(s['id'] != runtime.get('receipt_source_id') for s in refs), 'receipt cannot bind itself')
        if available:
            need(isinstance(receipt, dict), 'runtime receipt must be a source-selected JSON object')
            expected_sources = {s['path']: s['sha256'] for s in refs}
            if (receipt.get('effect') != 'READ_ONLY' or receipt.get('task_fingerprints') != task_fingerprints(context) or
                    receipt.get('source_fingerprints') != expected_sources):
                issue('STALE_RUNTIME_EVIDENCE', None, 'Receipt does not match read-only scope and current task/persona/injection/source fingerprints', True)
            evidence(runtime['bound_source_ids'], 'runtime sources')
    upstream = plan.get('upstream_blockers', [])
    need(isinstance(upstream, list), 'upstream_blockers must be an array')
    requirements = {r['id']: r for r in record['coverage']}
    for item in upstream:
        need(isinstance(item, dict) and item.get('requirement_id') in requirements and text(item.get('reason')),
             'upstream blocker must identify a prompt-authorized requirement')
        need(item.get('all_authorized_routes_ruled_out') is True and text(item.get('alternatives_reason')),
             'one failed path does not prove the task impossible; explain the authorized alternatives')
        field = item.get('feasibility_field')
        need(field in FEASIBILITY_FIELDS and feasibility[field]['result'] == 'BLOCKED',
             'upstream blocker must link to a specific blocked feasibility check')
        chain = requirements[item['requirement_id']]['authority_chain']
        authorized = authority(chain, known, root, context) and not any(metadata_source(known[s], root, context) for s in chain)
        if field not in blocked:
            issue('UPSTREAM_BLOCKER_UNRESOLVED', field, 'The claimed task-wide blocker lacks settled path evidence', True)
        elif authorized and evidence(item.get('source_ids'), 'upstream blocker'):
            result['upstream_blockers'].append(item)
    return result
