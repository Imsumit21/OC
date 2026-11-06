"""Anchor pool for the local /oe review record: exact evidence anchors (path + line or JSON pointer + quote).

Every anchor is re-read from the file with the same rules as Evals/tools/hg_review_evidence.EvidenceReader, so a
quote that is not in its selected text raises here, before the record is validated.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path('/Users/sumitkumar/Source/Outlier/OC')
OS_ = 'Universe_SynthCut/SynthCut_HarmonyGames_Other_Services/Services_Data/'
SQL = 'Evals/task_inputs/01_Universe_Inject.sql'
PROMPT = 'Evals/task_inputs/04_Prompt.txt'
_cache = {}


def _file(path):
    if path not in _cache:
        raw = (ROOT / path).read_bytes()
        _cache[path] = (hashlib.sha256(raw).hexdigest(), raw.decode('utf-8-sig'))
    return _cache[path]


def _json(path):
    key = ('json', path)
    if key not in _cache:
        _cache[key] = json.loads(_file(path)[1])
    return _cache[key]


def selected_text(path, pointer=None, line=None):
    sha, text = _file(path)
    if line is not None:
        lines = text.splitlines(keepends=True)
        a, b = line if isinstance(line, tuple) else (line, line)
        return ''.join(lines[a - 1:b])
    if pointer is not None:
        value = _json(path)
        for tok in pointer.split('/')[1:] if pointer else []:
            tok = tok.replace('~1', '/').replace('~0', '~')
            value = value[int(tok)] if isinstance(value, list) else value[tok]
        return value if isinstance(value, str) else json.dumps(value, ensure_ascii=False, sort_keys=True)
    return text


class Pool:
    def __init__(self):
        self.sources = {}
        self.by_key = {}

    def add(self, sid_hint, path, quote, pointer=None, line=None, access='', **extra):
        text = selected_text(path, pointer, line)
        if quote not in text:
            raise ValueError(f'quote not in {path} {pointer or line}: {quote[:80]!r}')
        key = (path, pointer, line, quote)
        if key in self.by_key:
            return self.by_key[key]
        sid = sid_hint
        n = 2
        while sid in self.sources:
            sid = f'{sid_hint}_{n}'
            n += 1
        src = dict(id=sid, path=path, sha256=_file(path)[0], quote=quote, visibility='VISIBLE',
                   access=access or 'Readable by vincent_parker (see access rules in the record notes).')
        if pointer is not None:
            src['pointer'] = pointer
        if line is not None:
            a, b = line if isinstance(line, tuple) else (line, line)
            src['line_start'], src['line_end'] = a, b
        src.update(extra)
        self.sources[sid] = src
        self.by_key[key] = sid
        return sid

    # convenience -------------------------------------------------------------------------------------------
    def sql_line_of(self, needle, start=1):
        text = _file(SQL)[1].splitlines()
        for i, l in enumerate(text, 1):
            if i >= start and needle in l:
                return i
        return None

    def sql(self, needle, quote=None, access='Seeded record (injection SQL overlay); persona visibility proven by '
            'persona_view check-sql (verdict PASS, 0 load-bearing rows not visible).', **extra):
        """Anchor on the first SQL physical line containing `needle` (quote defaults to the needle)."""
        ln = self.sql_line_of(needle)
        if ln is None:
            raise ValueError('needle not in SQL: ' + needle[:80])
        return self.add('sql_L%d' % ln, SQL, quote or needle, line=ln, access=access, **extra)
