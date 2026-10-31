"""Bind the UGT comparison to primary evidence and its visible report section.

This validates recorded evidence and declared comparisons, not the semantics of
the task. A judge must still choose a strong alternative, assess whether a cited
passage actually resolves it, and distinguish delegated choice from an option
list. Field comparison reasons deliberately allow equivalent material results
whose prose differs; string equality is not a semantic equivalence test.

BOTH_FAIR_FIGURE (Eval 1 §2.1 local override, 2026-10-17) is the one narrow
PASS for a fork no source settles: the readings share decision, writes and
destinations, differ only in one reported figure (amount, count, rate or date),
and each of the two values is cited to a visible primary record. The review
must state why each of the five checks does not settle it. Every other fork
keeps its existing resolutions.
"""
from copy import deepcopy
from html import escape
from pathlib import Path
import re

from hg_review_evidence import authority, links
from hg_source_checks import metadata_source

MATERIAL_FIELDS = ('decision', 'writes', 'destinations', 'contents')
RESOLUTIONS = {'EXCLUDED', 'SAME_MATERIAL_RESULT', 'AUTHORIZED_VARIATION',
               'UNRESOLVED_MATERIAL_DIFFERENCE', 'BOTH_FAIR_FIGURE'}
FIGURE_KINDS = {'AMOUNT', 'COUNT', 'RATE', 'DATE'}
# The five checks of Eval 1 §2.1, in its order, with their report labels.
FIGURE_CHECKS = (('newer_source', 'Newer source'), ('authority', 'Authority'),
                 ('source_identity', 'Source identity'), ('scope', 'Scope'),
                 ('same_material_result', 'Same material result'))
HEADING = '### Unique Ground Truth comparison'


def _need(ok, message):
    if not ok:
        raise ValueError('Unique Ground Truth: ' + message)


def _text(value):
    return isinstance(value, str) and bool(value.strip())


def _prompt_paths(root, context):
    paths = {(Path(root) / f['path']).resolve()
             for k in ('prompt', 'source:prompt')
             for f in context.get('inputs', {}).get(k, {}).get('files', [])}
    return paths or {(Path(root) / 'Task_Authoring/support/local_search/NO_EVAL_TASK_INPUTS/04_Prompt.txt').resolve()}


def validate_review(review, known, root, context):
    """Return a normalized copy including ``pending``; raise on invalid claims.

    ``known`` is the original result of hg_review_evidence.sources(), whose
    anchors have already been verified. Do not use premise_known: the prompt is
    primary instructional authority here, though not factual premise evidence.
    Incomplete reviews remain UNVERIFIED/null and need only reason and specific
    evidence_limits. They do not certify any optional unfinished comparison.
    """
    _need(isinstance(review, dict), 'record a dimension-specific review')
    _need(type(review.get('complete')) is bool, 'complete must be a boolean')
    _need(_text(review.get('reason')), 'explain the dimension verdict')
    limits = review.get('evidence_limits')
    _need(isinstance(limits, list) and all(_text(x) for x in limits),
          'evidence_limits must be an array of precise limitations')
    verdict, score = review.get('verdict'), review.get('score')
    if not review['complete']:
        _need(verdict == 'UNVERIFIED' and score is None,
              'an incomplete review is UNVERIFIED with no numeric score')
        _need(bool(limits), 'an incomplete review must identify evidence limits')
        return dict(complete=False, verdict='UNVERIFIED', score=None,
                    reason=review['reason'], evidence_limits=deepcopy(limits), pending=deepcopy(limits))
    _need(not limits, 'a complete review cannot have unresolved evidence limits')
    _need(type(score) is int and ((verdict == 'PASS' and score == 5) or
                                 (verdict == 'FAIL' and score in {1, 2})),
          'completed UGT supports only PASS 5 or FAIL 1/2; no NON-FAIL band')
    _need(review.get('alternative_search_complete') is True,
          'complete the search for competing readings before scoring')
    _need(_text(review.get('alternative_selection_reason')),
          'explain selection of the strongest plausible alternative')

    def evidence(entries, label):
        _need(isinstance(entries, list) and bool(entries), label + ' needs cited evidence')
        ids = []
        for entry in entries:
            _need(isinstance(entry, dict), label + ' needs source-bound quotes')
            sid = entry.get('source_id')
            _need(isinstance(sid, str) and sid in known, label + ' needs a known source_id')
            source = known[sid]
            _need(source.get('visibility') == 'VISIBLE' and not metadata_source(source, root, context),
                  label + ' requires visible primary prompt/source evidence')
            _need(_text(entry.get('quote')) and entry['quote'] in source['quote'],
                  label + ' quote must occur in the bound source passage')
            ids.append(sid)
        return ids

    readings = review.get('readings')
    _need(isinstance(readings, list) and len(readings) >= 2,
          'provide at least two concrete readings before PASS or FAIL')
    by_id = {}
    for reading in readings:
        _need(isinstance(reading, dict) and _text(reading.get('id')) and reading['id'] not in by_id,
              'readings need unique IDs')
        _need(_text(reading.get('interpretation')), 'explain each candidate reading')
        evidence(reading.get('support'), 'reading support')
        result = reading.get('material_result')
        _need(isinstance(result, dict) and set(result) == set(MATERIAL_FIELDS) and
              all(_text(result[f]) for f in MATERIAL_FIELDS),
              'each reading needs concrete decision, writes, destinations and contents')
        by_id[reading['id']] = reading
    lead_id = readings[0]['id']
    alternatives = set(by_id) - {lead_id}
    figure_labels = set()
    challenge = review.get('challenge_review')
    _need(isinstance(challenge, dict) and isinstance(challenge.get('strongest_alternative_id'), str) and
          challenge['strongest_alternative_id'] in alternatives,
          'challenge review must identify the strongest tested alternative')
    _need(_text(challenge.get('strongest_alternative_reason')),
          'challenge why this is the strongest plausible alternative, not a strawman')
    evidence(challenge.get('evidence'), 'strongest-alternative challenge')
    comparisons = review.get('comparisons')
    _need(isinstance(comparisons, list) and len(comparisons) == len(alternatives),
          'compare the leading reading with every alternative')
    compared = {}
    for comparison in comparisons:
        _need(isinstance(comparison, dict) and isinstance(comparison.get('alternative_id'), str) and
              comparison['alternative_id'] in alternatives and
              comparison['alternative_id'] not in compared, 'compare each known alternative exactly once')
        alternate = comparison['alternative_id']
        resolution = comparison.get('resolution')
        _need(isinstance(resolution, str) and resolution in RESOLUTIONS and _text(comparison.get('reason')),
              'classify and explain each comparison')
        refs = evidence(comparison.get('evidence'), 'comparison resolution')
        fields = comparison.get('field_comparison')
        _need(isinstance(fields, dict) and set(fields) == set(MATERIAL_FIELDS),
              'compare decisions, writes, destinations and contents separately')
        for name, field in fields.items():
            _need(isinstance(field, dict) and isinstance(field.get('relation'), str) and
                  field['relation'] in {'SAME', 'DIFFERENT'} and
                  _text(field.get('reason')), 'explain the material relation for ' + name)
            if field['relation'] == 'DIFFERENT':
                _need(by_id[lead_id]['material_result'][name] != by_id[alternate]['material_result'][name],
                      'a declared material difference must identify different concrete ' + name)
        differs = any(f['relation'] == 'DIFFERENT' for f in fields.values())
        if resolution == 'SAME_MATERIAL_RESULT':
            _need(not differs, 'same destination alone cannot establish the same material result')
        if resolution == 'UNRESOLVED_MATERIAL_DIFFERENCE':
            _need(differs, 'unresolved ambiguity needs a concrete material difference')
        if resolution == 'BOTH_FAIR_FIGURE':
            # Narrow local override (Eval 1 §2.1, 2026-10-17). Every condition is
            # required; nothing here relaxes any other resolution.
            _need(all(fields[f]['relation'] == 'SAME' for f in ('decision', 'writes', 'destinations')) and
                  fields['contents']['relation'] == 'DIFFERENT',
                  'BOTH_FAIR_FIGURE needs the same decision, writes and destinations (recipients included); '
                  'only contents may differ')
            # Stricter than SAME elsewhere: the narrow exception needs the identical
            # concrete outcome, not prose the reviewer calls equivalent.
            _need(all(by_id[lead_id]['material_result'][f].strip() == by_id[alternate]['material_result'][f].strip()
                      for f in ('decision', 'writes', 'destinations')),
                  'BOTH_FAIR_FIGURE readings must state the identical decision, writes and destinations')
            _need('authority_chain' not in comparison,
                  'BOTH_FAIR_FIGURE has no resolving authority; a fork an authority settles is EXCLUDED')
            figure = comparison.get('figure')
            _need(isinstance(figure, dict) and figure.get('kind') in FIGURE_KINDS and _text(figure.get('label')),
                  'BOTH_FAIR_FIGURE needs a figure with kind AMOUNT, COUNT, RATE or DATE and a label')
            label = figure['label'].strip().casefold()
            _need(label not in figure_labels, 'a both-fair figure has exactly two values; record one fork per figure')
            figure_labels.add(label)
            values = figure.get('values')
            _need(isinstance(values, list) and len(values) == 2 and all(isinstance(v, dict) for v in values) and
                  [v.get('reading_id') for v in values] == [lead_id, alternate],
                  'BOTH_FAIR_FIGURE needs exactly two values, the leading reading first, then the alternative')
            for value in values:
                _need(_text(value.get('value')), 'state each figure value')
                value_refs = evidence(value.get('evidence'), 'figure value')
                _need(all((Path(root) / known[sid]['path']).resolve() not in _prompt_paths(root, context)
                          for sid in value_refs),
                      'cite each figure value to a record the persona can open, not the prompt')
                _need(any(value['value'] in e['quote'] for e in value['evidence']) or _text(value.get('derivation')),
                      'quote the figure value or explain how it follows from the cited record')
                _need(value['value'] in by_id[value['reading_id']]['material_result']['contents'],
                      "each reading's contents must state its figure value")
            _need(values[0]['value'].strip().casefold() != values[1]['value'].strip().casefold(),
                  'BOTH_FAIR_FIGURE needs two different values')
            settled = figure.get('checks')
            _need(isinstance(settled, dict) and set(settled) == {key for key, _ in FIGURE_CHECKS},
                  'give a reason for each of the five checks')
            for key, name in FIGURE_CHECKS:
                item = settled[key]
                _need(isinstance(item, dict) and type(item.get('settles')) is bool and _text(item.get('reason')),
                      'explain the ' + name.lower() + ' check')
                _need(item['settles'] is False,
                      'the ' + name.lower() + ' check settles this fork; it is not BOTH_FAIR_FIGURE')
            _need(_text(figure.get('asks_completed')), 'show that each reading completes every explicit ask')
            _need(_text(figure.get('next_step_unchanged')),
                  'show that the figure does not change what the Agent does next')
        check = comparison.get('challenge')
        _need(isinstance(check, dict) and _text(check.get('resolution_relevance')),
              'challenge whether cited evidence resolves this actual alternative')
        evidence(check.get('evidence'), 'resolution challenge')
        expected_basis = 'EXPLICIT_AUTHORITY' if resolution == 'AUTHORIZED_VARIATION' else 'NOT_CLAIMED'
        _need(check.get('delegation_basis') == expected_basis and _text(check.get('delegation_reason')),
              'challenge actual delegation separately from merely listing options')
        if resolution in {'EXCLUDED', 'AUTHORIZED_VARIATION'} or 'authority_chain' in comparison:
            chain = comparison.get('authority_chain')
            _need(authority(chain, known, root, context), 'resolving authority must be visible')
            _need(all(not metadata_source(s, root, context) for s in links(chain, known, 'authority_chain')),
                  'authoring metadata and downstream outputs are not resolving authority')
            _need(chain[-1] in refs, 'quote the final resolving authority in comparison evidence')
        if resolution == 'AUTHORIZED_VARIATION':
            _need(isinstance(comparison.get('authority_kind'), str) and
                  comparison['authority_kind'] in {'EXPLICIT_DELEGATION', 'OBJECTIVE_ACCEPTANCE_BOUNDARY'},
                  'identify explicit delegation or objective acceptance authority')
            _need(_text(comparison.get('acceptance_boundary')),
                  'state the authorized objective acceptance boundary')
            checks = comparison.get('acceptance_checks')
            _need(isinstance(checks, dict) and set(checks) == {lead_id, alternate} and
                  all(_text(v) for v in checks.values()),
                  'show how both readings satisfy the authorized acceptance boundary')
        compared[alternate] = comparison
    _need(set(compared) == alternatives, 'every alternative must be compared')

    inventory = review.get('option_inventory')
    _need(isinstance(inventory, dict) and inventory.get('complete') is True and _text(inventory.get('reason')),
          'inventory every explicit option, or explain why no explicit option list exists')
    inventory_refs = evidence(inventory.get('evidence'), 'option inventory')
    # Even a declaration that no options occur must cite the actual prompt.
    prompt_paths = _prompt_paths(root, context)
    _need(any((Path(root) / known[sid]['path']).resolve() in prompt_paths for sid in inventory_refs),
          'option inventory must cite the actual prompt')
    options = inventory.get('options')
    _need(isinstance(options, list), 'option inventory options must be an array')
    seen = set()
    for option in options:
        _need(isinstance(option, dict) and _text(option.get('id')) and option['id'] not in seen and
              _text(option.get('option')) and _text(option.get('reason')), 'name and explain each distinct option')
        seen.add(option['id'])
        evidence([option], 'explicit option')
        ids = option.get('reading_ids')
        _need(isinstance(ids, list) and bool(ids) and all(isinstance(i, str) and i in by_id for i in ids) and
              len(ids) == len(set(ids)), 'map each option to concrete tested readings')
        _need(isinstance(option.get('disposition'), str) and option['disposition'] in {'RETAINED', 'EXCLUDED'},
              'record each option disposition')
        excluded = all(i != lead_id and compared[i]['resolution'] == 'EXCLUDED' for i in ids)
        _need((option['disposition'] == 'EXCLUDED') == excluded,
              'option disposition must agree with its compared readings')
    unresolved = [c for c in comparisons if c['resolution'] == 'UNRESOLVED_MATERIAL_DIFFERENCE']
    _need((verdict == 'FAIL') == bool(unresolved),
          'FAIL needs a supported unresolved material difference; PASS cannot retain one')
    normalized = deepcopy(review)
    normalized['pending'] = []
    return normalized


def _cell(value):
    # Reviewer-controlled passages must not create hidden HTML, headings or
    # fences inside the required visible section.
    value = escape(str(value), quote=False).replace('\\', '\\\\')
    value = re.sub(r'([`*_{}\[\]#|])', r'\\\1', value)
    return value.replace('\r\n', '\n').replace('\r', '\n').replace('\n', '<br>')


def _citations(entries, known):
    parts = []
    for entry in entries:
        source = known[entry['source_id']]
        locator = source['path']
        if 'pointer' in source:
            locator += ' pointer ' + source['pointer']
        elif 'line_start' in source:
            locator += f" lines {source['line_start']}-{source['line_end']}"
        parts.append(f"{entry['source_id']} ({locator}): \"{entry['quote']}\"")
    return '; '.join(parts)


def render_review(review, known):
    """Render a previously validated review; this function performs no grading."""
    score = review['score'] if review['score'] is not None else 'unscored'
    lines = [HEADING, '', f"Unique Ground Truth: {review['verdict']} {score}",
             '', 'Basis: ' + _cell(review['reason'])]
    if not review['complete']:
        lines += ['', 'Review incomplete. Evidence limits: ' + _cell('; '.join(review['evidence_limits']))]
        return '\n'.join(lines) + '\n'
    lines += ['', 'Alternative selection: ' + _cell(review['alternative_selection_reason']), '',
              '| Reading | Interpretation | Decision | Writes | Destinations | Contents | Supporting evidence |',
              '|---|---|---|---|---|---|---|']
    for reading in review['readings']:
        values = [reading['id'], reading['interpretation'],
                  *[reading['material_result'][f] for f in MATERIAL_FIELDS], _citations(reading['support'], known)]
        lines.append('| ' + ' | '.join(_cell(v) for v in values) + ' |')
    inventory = review['option_inventory']
    lines += ['', 'Explicit option inventory: ' + _cell(inventory['reason']),
              'Inventory evidence: ' + _cell(_citations(inventory['evidence'], known)), '',
              '| Option | Disposition | Tested readings | Reason and evidence |', '|---|---|---|---|']
    for option in inventory['options']:
        values = [option['option'], option['disposition'], ', '.join(option['reading_ids']),
                  option['reason'] + ' Evidence: ' + _citations([option], known)]
        lines.append('| ' + ' | '.join(_cell(v) for v in values) + ' |')
    if not inventory['options']:
        lines.append('| No explicit option list | Reviewed | See candidate readings | See inventory evidence |')
    for comparison in review['comparisons']:
        lines += ['', 'Compared alternative: ' + _cell(comparison['alternative_id']),
                  'Resolution: ' + comparison['resolution'] + '. ' + _cell(comparison['reason']),
                  'Resolution evidence: ' + _cell(_citations(comparison['evidence'], known)), '',
                  '| Material field | Relation | Explanation |', '|---|---|---|']
        for field in MATERIAL_FIELDS:
            item = comparison['field_comparison'][field]
            lines.append('| ' + ' | '.join(_cell(v) for v in (field, item['relation'], item['reason'])) + ' |')
        if comparison['resolution'] == 'BOTH_FAIR_FIGURE':
            figure = comparison['figure']
            lines += ['', 'Both-fair figure: ' + figure['kind'] + ', ' + _cell(figure['label'])]
            for value in figure['values']:
                line = ('Value for ' + _cell(value['reading_id']) + ': ' + _cell(value['value']) +
                        '. Evidence: ' + _cell(_citations(value['evidence'], known)))
                if _text(value.get('derivation')):
                    line += '. Derivation: ' + _cell(value['derivation'])
                lines.append(line)
            lines += [name + ' check does not settle it: ' + _cell(figure['checks'][key]['reason'])
                      for key, name in FIGURE_CHECKS]
            lines += ['Every explicit ask: ' + _cell(figure['asks_completed']),
                      'Next step unchanged: ' + _cell(figure['next_step_unchanged']),
                      'Rubric must accept: ' + ' or '.join(_cell(v['value']) for v in figure['values'])]
        if 'authority_chain' in comparison:
            lines += ['', 'Authority chain: ' + _cell(' → '.join(comparison['authority_chain']))]
        if comparison['resolution'] == 'AUTHORIZED_VARIATION':
            lines += ['Authority kind: ' + comparison['authority_kind'],
                      'Acceptance boundary: ' + _cell(comparison['acceptance_boundary'])]
            for rid in (review['readings'][0]['id'], comparison['alternative_id']):
                lines.append('Acceptance for ' + _cell(rid) + ': ' + _cell(comparison['acceptance_checks'][rid]))
        check = comparison['challenge']
        lines += ['', 'Resolution relevance challenge: ' + _cell(check['resolution_relevance']),
                  'Delegation challenge: ' + check['delegation_basis'] + '. ' + _cell(check['delegation_reason']),
                  'Challenge evidence: ' + _cell(_citations(check['evidence'], known))]
    challenge = review['challenge_review']
    lines += ['', 'Strongest-alternative challenge (' + _cell(challenge['strongest_alternative_id']) + '): ' +
              _cell(challenge['strongest_alternative_reason']),
              'Challenge evidence: ' + _cell(_citations(challenge['evidence'], known)), '',
              'Validation scope: source binding and comparison completeness are checked mechanically; '
              'alternative strength, evidence relevance and authorization remain substantive review judgments.']
    return '\n'.join(lines) + '\n'


def _visible_content(content):
    """Drop comments, raw HTML blocks and Markdown code before checking fields."""
    content = re.sub(r'<!--.*?(?:-->|\Z)', '', content, flags=re.S)
    # Raw HTML can hide or reinterpret an otherwise exact Markdown section.
    content = re.sub(r'<((?!(?:area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)\b)[a-z][a-z0-9-]*)(?=[\s/>])[^>]*>.*?(?:</\1\s*>|\Z)',
                     '', content, flags=re.S | re.I)
    # Void elements can also hide the whole block inside a multiline attribute.
    # Preserve only the exact <br> generated by _cell; escape() prevents source
    # passages from injecting any other raw tag into the required section.
    content = re.sub(r'<(?!br>)/?[a-z][a-z0-9-]*(?=[\s/>])[^>]*>', '', content, flags=re.I)
    content = re.sub(r'<[!?][^>]*>', '', content, flags=re.S)
    lines, fence = [], None
    for raw in content.splitlines(keepends=True):
        match = re.match(r'^\s{0,3}(`{3,}|~{3,})(.*)$', raw.rstrip('\r\n'))
        if match:
            marker, rest = match.groups()
            if fence is None:
                fence = marker
            elif marker[0] == fence[0] and len(marker) >= len(fence) and not rest.strip():
                fence = None
            continue
        if fence is None and not raw.startswith(('    ', '\t')):
            lines.append(raw)
    return ''.join(lines)


_LABEL = re.compile(r'\b(?:Unique\s+Ground\s+Truth|UGT)\b', re.I)
_VERDICT = re.compile(r'\b(NON-FAIL|UNVERIFIED|PENDING|PASS|FAIL)\b', re.I)


def _declarations(content):
    """Recognize displayed UGT fields/tables, not arbitrary prose or examples."""
    lines = _visible_content(content).splitlines()
    for index, raw in enumerate(lines):
        line = raw.replace('**', '').replace('__', '')
        label = _LABEL.search(line)
        if not label:
            continue
        prefix, tail = line[:label.start()], line[label.end():]
        # Field, heading, or table cell. A narrative quote about an old verdict
        # is not itself a report declaration.
        table = line.lstrip().startswith('|')
        field = bool(re.fullmatch(r'\s*(?:#{1,6}\s*|[-*]\s*)?', prefix))
        if not table and not field:
            continue
        if field and not re.match(r'\s*(?::|[-–—]|\||$|\(|PASS\b|FAIL\b|NON-FAIL\b|UNVERIFIED\b|PENDING\b|Score\s*:?[1-5])',
                                  tail, re.I) and not prefix.lstrip().startswith('#'):
            continue
        text = tail
        if field and not _VERDICT.search(text) and not re.search(r'\b[1-5](?:\s*/\s*5)?\b', text):
            for following in lines[index+1:index+4]:
                stripped = following.replace('**', '').strip()
                if not stripped:
                    continue
                if re.match(r'^(?:Verdict|Score|Result)\s*:', stripped, re.I) or re.match(r'^(?:PASS|FAIL|NON-FAIL|UNVERIFIED|PENDING)\b', stripped, re.I):
                    text += ' ' + stripped
                else:
                    break
        if table:
            # The first cells after the dimension contain its result/score;
            # explanatory prose in later cells is not another declared score.
            cells = text.split('|')
            if cells and not cells[0].strip():
                cells = cells[1:]
            text = cells[0] if cells else ''
            if len(cells) > 1 and re.fullmatch(
                    r'\s*(?:Score\s*:?\s*)?(?:PASS|FAIL|NON-FAIL|UNVERIFIED|PENDING)?\s*(?:\(?[1-5](?:\s*/\s*5)?\)?)?\s*',
                    cells[1], re.I):
                text += ' ' + cells[1]
        verdict = _VERDICT.search(text)
        explicit_score = re.search(r'\bScore\s*:?\s*([1-5])(?:\s*/\s*5)?(?![\w./])', text, re.I)
        scores = re.findall(r'(?<![\w./])([1-5])(?:\s*/\s*5)?(?![\w./])', text)
        if verdict or scores:
            yield (verdict.group(1).upper() if verdict else None,
                   int(explicit_score.group(1)) if explicit_score else int(scores[0]) if scores else None)
        elif explicit_score:
            yield None, int(explicit_score.group(1))


def has_scored_ugt(content):
    """Detect a visible definitive UGT claim, including one omitting its score.

    The historical function name also covers PASS/FAIL/NON-FAIL without a
    number: dropping the number must not bypass the comparison contract.
    """
    return any(score is not None or verdict in {'PASS', 'FAIL', 'NON-FAIL'}
               for verdict, score in _declarations(content))


def validate_report(review, known, content):
    """Require one exact visible block and consistent recognized UGT summaries."""
    block = render_review(review, known)
    _need(content.count(block) == 1 and _visible_content(content).count(block) == 1,
          'include the exact rendered comparison once, visibly outside code/comments')
    # Review text/quotes inside the bound block may discuss rejected readings.
    # Only separately authored report declarations can contradict its result.
    other = content.replace(block, '', 1)
    for verdict, score in _declarations(other):
        if verdict == 'PENDING':
            verdict = 'UNVERIFIED'
        _need((verdict is None or verdict == review['verdict']) and
              (score is None or score == review['score']),
              'report contains a contradictory UGT verdict or score')
