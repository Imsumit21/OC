#!/usr/bin/env python3
"""Static lint for injection SQL (Eval 0). Parses the saved SQL; never runs it.

Prints one JSON object: input hash, statement coverage and one flag per finding.
  check              rule (Eval 0 check)                                          severity
  future_date        event timestamp after the task clock (hg_universe.py) (C)   FAIL
  id_contract        value breaks a listed contract in references/schema/id_contracts.json (A)  FAIL
  drive_unreadable   injected Drive file the agent cannot open (A)               FAIL
  duplicate_account  second account for an existing person in one service (A)   FAIL
  actor_name         sender/creator id belongs to a different person than the record names (A)  FAIL
  unknown_actor      author/creator id with no account in the base or the SQL (A)   CHECK
  grader_language    injected text addressed to a solver/grader or describing the test (C)  CHECK
  padding_comment    SQL comment about tool calls, pass rate, gates, hardness... (intent)  CHECK
  generated_column   INSERT or UPDATE writes a database-computed column ("generated" in the schema) (B)  FAIL
  text_time_format   text date column (Linear *_at / *_date) not in the base format YYYY-MM-DDTHH:MM:SSZ / YYYY-MM-DD (B)  FAIL
  missing_required   INSERT leaves out a NOT NULL column that has no default (B)  FAIL
  unparsed           statement or value the lint could not evaluate; check it by hand  INFO
FAIL flags are listed-rule violations; the reviewer confirms each one and may
override a real namesake. CHECK flags need a reviewer decision. INFO marks lint
coverage limits. No flags is not a PASS: checks A-C still apply in full.

Usage: hg_injection_lint.py [--sql PATH] [--checks a,b] [--no-base] [--summary]
Default SQL is the saved injection input (Evals/task_inputs/01_Universe_Inject.sql).
"""
import argparse
import bisect
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata

import hg_universe

ROOT = Path(__file__).resolve().parents[2]
SAVED_SQL = Path('Evals/task_inputs/01_Universe_Inject.sql')
SCHEMA = Path('Evals/references/schema/injection.json')
CONTRACTS = Path('Evals/references/schema/id_contracts.json')
VERSION = 'injection-lint-v1'
CHECKS = ('future_date', 'id_contract', 'drive_unreadable', 'identities', 'grader_language', 'padding_comment',
          'generated_column', 'text_time_format', 'missing_required')

# ---------------------------------------------------------------- tokenizer

class Tok:
    __slots__ = ('kind', 'text', 'value', 'start')

    def __init__(self, kind, text, value, start):
        self.kind, self.text, self.value, self.start = kind, text, value, start

    def word(self, *words):
        return self.kind == 'word' and self.value in words

    def op(self, *ops):
        return self.kind == 'op' and self.text in ops


WORD = re.compile(r'[A-Za-z_\u0080-\uffff][A-Za-z0-9_$\u0080-\uffff]*')
NUMBER = re.compile(r'(?:\d+\.?\d*|\.\d+)(?:[eE][+-]?\d+)?')
OPS = re.compile(r'::|\|\||<=|>=|<>|!=|->>|->|=>|[(),;.=<>+\-*/%\[\]:^~!@#&|?{}]')
DOLLAR = re.compile(r'\$([A-Za-z_][A-Za-z0-9_]*)?\$')
ESCAPES = {'b': '\b', 'f': '\f', 'n': '\n', 'r': '\r', 't': '\t'}


def _quoted(text, i, quote):
    """Scan a '...' or "..." body starting after the opening quote; doubled quote escapes."""
    parts, n = [], len(text)
    while True:
        j = text.find(quote, i)
        if j < 0:
            raise ValueError('unterminated quoted text')
        parts.append(text[i:j])
        if j + 1 < n and text[j + 1] == quote:
            parts.append(quote)
            i = j + 2
            continue
        return ''.join(parts), j + 1


def _escape_string(text, i):
    """Scan an E'...' body; backslash escapes and doubled quotes."""
    out, n = [], len(text)
    while i < n:
        c = text[i]
        if c == "'":
            if i + 1 < n and text[i + 1] == "'":
                out.append("'")
                i += 2
                continue
            return ''.join(out), i + 1
        if c == '\\' and i + 1 < n:
            d = text[i + 1]
            if d in ESCAPES:
                out.append(ESCAPES[d]); i += 2
            elif d in '01234567':
                m = re.match(r'[0-7]{1,3}', text[i + 1:i + 4])
                out.append(chr(int(m.group(0), 8))); i += 1 + len(m.group(0))
            elif d == 'x' and re.match(r'[0-9A-Fa-f]', text[i + 2:i + 3]):
                m = re.match(r'[0-9A-Fa-f]{1,2}', text[i + 2:i + 4])
                out.append(chr(int(m.group(0), 16))); i += 2 + len(m.group(0))
            elif d in 'uU':
                size = 4 if d == 'u' else 8
                digits = text[i + 2:i + 2 + size]
                if re.fullmatch(r'[0-9A-Fa-f]{%d}' % size, digits):
                    out.append(chr(int(digits, 16))); i += 2 + size
                else:
                    out.append(d); i += 2
            else:
                out.append(d); i += 2
            continue
        out.append(c)
        i += 1
    raise ValueError('unterminated E string')


def tokenize(text, base=0):
    """Tokens and comments of PostgreSQL text. Offsets are relative to the file (base)."""
    toks, comments, i, n = [], [], 0, len(text)
    while i < n:
        c = text[i]
        if c.isspace():
            i += 1
            continue
        start = i
        if text.startswith('--', i):
            j = text.find('\n', i)
            j = n if j < 0 else j
            comments.append(Tok('comment', text[i:j], text[i + 2:j].strip(), base + i))
            i = j
        elif text.startswith('/*', i):
            depth, j = 1, i + 2
            while depth and j < n:
                if text.startswith('/*', j):
                    depth, j = depth + 1, j + 2
                elif text.startswith('*/', j):
                    depth, j = depth - 1, j + 2
                else:
                    j += 1
            comments.append(Tok('comment', text[i:j], text[i + 2:j - 2].strip(), base + i))
            i = j
        elif c == "'":
            value, i = _quoted(text, i + 1, "'")
            toks.append(Tok('string', text[start:i], value, base + start))
        elif c in 'eE' and text[i + 1:i + 2] == "'":
            value, i = _escape_string(text, i + 2)
            toks.append(Tok('string', text[start:i], value, base + start))
        elif c in 'uU' and text[i + 1:i + 3] == "&'":
            value, i = _quoted(text, i + 3, "'")
            toks.append(Tok('string', text[start:i], value, base + start))
        elif c in 'nNbBxX' and text[i + 1:i + 2] == "'":
            value, i = _quoted(text, i + 2, "'")
            toks.append(Tok('string', text[start:i], value, base + start))
        elif c == '"':
            value, i = _quoted(text, i + 1, '"')
            toks.append(Tok('qident', text[start:i], value.lower(), base + start))
        elif c == '$' and DOLLAR.match(text, i):
            tag = DOLLAR.match(text, i).group(0)
            j = text.find(tag, i + len(tag))
            if j < 0:
                raise ValueError('unterminated dollar quote ' + tag)
            body_start = i + len(tag)
            tok = Tok('string', text[start:j + len(tag)], text[body_start:j], base + start)
            tok.text = tag  # keep the delimiter only; the body is the value
            toks.append(tok)
            i = j + len(tag)
        else:
            m = WORD.match(text, i)
            if m:
                toks.append(Tok('word', m.group(0), m.group(0).lower(), base + start))
                i = m.end()
                continue
            m = NUMBER.match(text, i)
            if m:
                toks.append(Tok('number', m.group(0), m.group(0), base + start))
                i = m.end()
                continue
            m = OPS.match(text, i)
            if m:
                toks.append(Tok('op', m.group(0), m.group(0), base + start))
                i = m.end()
                continue
            toks.append(Tok('op', c, c, base + start))
            i += 1
    return toks, comments


def statements(toks):
    """Split on top-level semicolons."""
    out, cur = [], []
    for t in toks:
        if t.op(';'):
            if cur:
                out.append(cur)
            cur = []
        else:
            cur.append(t)
    if cur:
        out.append(cur)
    return out


def split_commas(toks):
    """Split a token list at depth-0 commas."""
    parts, cur, depth = [], [], 0
    for t in toks:
        if t.op('(', '['):
            depth += 1
        elif t.op(')', ']'):
            depth -= 1
        if depth == 0 and t.op(','):
            parts.append(cur)
            cur = []
        else:
            cur.append(t)
    parts.append(cur)
    return parts


def matching(toks, i):
    """Index of the bracket closing toks[i]."""
    depth = 0
    for j in range(i, len(toks)):
        if toks[j].op('(', '['):
            depth += 1
        elif toks[j].op(')', ']'):
            depth -= 1
            if depth == 0:
                return j
    raise ValueError('unbalanced parentheses')


def find_word(toks, words, start=0):
    """First depth-0 index of any word in words, or len(toks)."""
    depth = 0
    for j in range(start, len(toks)):
        t = toks[j]
        if t.op('(', '['):
            depth += 1
        elif t.op(')', ']'):
            depth -= 1
        elif depth == 0 and t.kind == 'word' and t.value in words:
            return j
    return len(toks)

# ---------------------------------------------------------------- values

class Val:
    """kind: str, num, null, bool, default, expr. literals: string/number literals inside an expr."""
    __slots__ = ('kind', 'value', 'literals', 'raw', 'start', 'wall_clock', 'tokens')

    def __init__(self, kind, value=None, literals=(), raw='', start=0, wall_clock=False, tokens=None):
        self.kind, self.value, self.literals, self.raw = kind, value, list(literals), raw
        self.start, self.wall_clock, self.tokens = start, wall_clock, tokens


TYPE_WORDS = {'timestamp', 'timestamptz', 'with', 'without', 'time', 'zone', 'date', 'text', 'varchar',
              'character', 'varying', 'char', 'int', 'integer', 'bigint', 'smallint', 'numeric', 'decimal',
              'double', 'precision', 'real', 'float', 'float4', 'float8', 'boolean', 'bool', 'json', 'jsonb',
              'uuid', 'interval', 'tsvector', 'bytea', 'int2', 'int4', 'int8'}
WALL_CLOCK = {'now', 'current_timestamp', 'current_date', 'localtimestamp', 'clock_timestamp',
              'transaction_timestamp', 'statement_timestamp', 'localtime', 'current_time'}


def strip_casts(toks):
    out, i = [], 0
    while i < len(toks):
        t = toks[i]
        if t.op('::'):
            i += 1
            first = True
            while i < len(toks) and (toks[i].kind in ('word', 'qident') and (first or toks[i].value in TYPE_WORDS)
                                     or toks[i].op('.') and not first):
                first = False
                i += 1
            if i < len(toks) and toks[i].op('('):
                i = matching(toks, i) + 1
            while i + 1 < len(toks) and toks[i].op('[') and toks[i + 1].op(']'):
                i += 2
            continue
        out.append(t)
        i += 1
    return out


def raw_text(toks):
    return ' '.join(t.text if t.kind != 'string' or len(t.value) < 60 else "'%s…'" % t.value[:57]
                    for t in toks)[:240]


def split_concat(toks):
    """Split at depth-0 || operators."""
    parts, cur, depth = [], [], 0
    for t in toks:
        if t.op('(', '['):
            depth += 1
        elif t.op(')', ']'):
            depth -= 1
        if depth == 0 and t.op('||'):
            parts.append(cur)
            cur = []
        else:
            cur.append(t)
    parts.append(cur)
    return parts


def evaluate(toks):
    start = toks[0].start if toks else 0
    clean = strip_casts(toks)
    if len(clean) >= 2 and clean[0].op('(') and matching(clean, 0) == len(clean) - 1:
        inner = evaluate(clean[1:-1])
        inner.start = start
        return inner
    if len(clean) == 1:
        t = clean[0]
        if t.kind == 'string':
            return Val('str', t.value, start=start)
        if t.kind == 'number':
            return Val('num', float(t.text) if any(c in t.text for c in '.eE') else int(t.text), start=start)
        if t.word('null'):
            return Val('null', start=start)
        if t.word('true', 'false'):
            return Val('bool', t.value == 'true', start=start)
        if t.word('default'):
            return Val('default', start=start)
    if len(clean) == 2 and clean[0].op('-') and clean[1].kind == 'number':
        return Val('num', -float(clean[1].text), start=start)
    if len(clean) == 4 and clean[0].word('chr') and clean[1].op('(') and clean[2].kind == 'number' \
            and clean[3].op(')'):
        return Val('str', chr(int(float(clean[2].text))), start=start)
    if len(clean) >= 4 and clean[0].word('cast') and clean[1].op('('):
        end = matching(clean, 1)
        inner = clean[2:end]
        cut = find_word(inner, {'as'})
        if end == len(clean) - 1 and cut < len(inner):
            return evaluate(inner[:cut])
    parts = split_concat(clean)
    if len(parts) > 1 and all(parts):
        values = [evaluate(part) for part in parts]
        if all(v.kind in ('str', 'num') for v in values):
            return Val('str', ''.join(v.value if v.kind == 'str' else str(v.value) for v in values), start=start)
    if len(clean) >= 3 and clean[0].word('to_timestamp') and clean[1].op('(') and matching(clean, 1) == len(clean) - 1:
        inner = evaluate(clean[2:-1])
        if inner.kind in ('num', 'str'):
            return Val('expr', None, [inner.value], raw_text(toks), start)
    literals = [t.value if t.kind == 'string' else float(t.text) for t in clean if t.kind in ('string', 'number')]
    wall = any(t.kind == 'word' and t.value in WALL_CLOCK for t in clean)
    return Val('expr', None, literals, raw_text(toks), start, wall_clock=wall, tokens=toks)


def value_token(val, start):
    """A literal token standing for an already evaluated value, or None."""
    if val.kind == 'str':
        return Tok('string', "'%s'" % val.value[:40], val.value, start)
    if val.kind == 'num':
        return Tok('number', str(val.value), str(val.value), start)
    if val.kind == 'null':
        return Tok('word', 'NULL', 'null', start)
    if val.kind == 'bool':
        return Tok('word', str(val.value).upper(), str(val.value).lower(), start)
    return None


def bind(expr, row, alias):
    """Evaluate expr with alias.col / col references replaced by the values of one source row."""
    out, i, used = [], 0, None
    while i < len(expr):
        t = expr[i]
        ref = None
        if alias and t.kind in ('word', 'qident') and t.value == alias and i + 2 < len(expr) \
                and expr[i + 1].op('.') and expr[i + 2].value in row:
            ref, step = row[expr[i + 2].value], 3
        elif t.kind in ('word', 'qident') and t.value in row and not (i + 1 < len(expr) and expr[i + 1].op('(', '.')) \
                and not (i > 0 and expr[i - 1].op('.', '::')):
            ref, step = row[t.value], 1
        if ref is not None:
            token = value_token(ref, ref.start or t.start)
            if token is not None:
                out.append(token)
                used = used or ref.start
                i += step
                continue
            if len(expr) == step:
                return ref
        out.append(t)
        i += 1
    val = evaluate(out) if out else Val('expr')
    if used and len(expr) <= 4:
        val.start = used
    return val

# ---------------------------------------------------------------- statement parser

class Row:
    __slots__ = ('table', 'op', 'start', 'cols', 'key', 'stmt')

    def __init__(self, table, op, start, cols, key=None, stmt=0):
        self.table, self.op, self.start, self.cols, self.key, self.stmt = table, op, start, cols, key, stmt


class Parser:
    def __init__(self, schema_tables):
        self.tables = schema_tables  # table name -> 'schema.table'; full names -> column lists
        self.rows, self.unparsed, self.kinds = [], [], {}
        self.extra_comments = []
        self.stmt_no = 0

    def table_name(self, parts):
        if len(parts) >= 2:
            return parts[-2] + '.' + parts[-1]
        name = parts[0] if parts else '?'
        return self.tables.get(name, name)

    def qualified(self, toks, i):
        parts = []
        while i < len(toks) and toks[i].kind in ('word', 'qident'):
            parts.append(toks[i].value)
            if i + 1 < len(toks) and toks[i + 1].op('.'):
                i += 2
            else:
                i += 1
                break
        return parts, i

    def note(self, start, reason, text=''):
        self.unparsed.append({'start': start, 'reason': reason, 'text': text[:160]})

    def statement(self, toks):
        self.stmt_no += 1
        head = toks[0]
        kind = head.value if head.kind == 'word' else head.text
        self.kinds[kind] = self.kinds.get(kind, 0) + 1
        try:
            if head.word('with', 'insert', 'update', 'delete'):
                self.dml(toks, {})
            elif head.word('do'):
                body = next((t for t in toks if t.kind == 'string'), None)
                if body is not None:
                    self.nested(body)
            elif any(t.word('insert', 'update') for t in toks):
                self.embedded(toks)
        except (ValueError, IndexError) as error:
            self.note(head.start, 'parse error: %s' % error, raw_text(toks))

    def nested(self, body):
        """Parse DML inside a DO block or function body."""
        offset = body.start + len(body.text)
        inner, comments = tokenize(body.value, base=offset)
        self.extra_comments.extend(comments)
        for stmt in statements(inner):
            self.embedded(stmt)

    def embedded(self, toks):
        """DML that does not start the statement (plpgsql blocks)."""
        i = 0
        while i < len(toks):
            if toks[i].word('insert') and i + 1 < len(toks) and toks[i + 1].word('into') \
                    or toks[i].word('update') and i + 2 < len(toks) and toks[i + 1].kind in ('word', 'qident') \
                    and any(t.word('set') for t in toks[i + 2:i + 7]):
                try:
                    self.dml(toks[i:], {})
                except (ValueError, IndexError) as error:
                    self.note(toks[i].start, 'parse error: %s' % error, raw_text(toks[i:i + 12]))
                return
            i += 1

    def dml(self, toks, ctes):
        i = 0
        if toks[0].word('with'):
            i = 1
            if toks[i].word('recursive'):
                i += 1
            while True:
                name = toks[i].value
                i += 1
                cols = None
                if toks[i].op('('):
                    end = matching(toks, i)
                    cols = [p[0].value for p in split_commas(toks[i + 1:end]) if p]
                    i = end + 1
                if not toks[i].word('as'):
                    raise ValueError('CTE without AS')
                i += 1
                while toks[i].word('not', 'materialized'):
                    i += 1
                end = matching(toks, i)
                ctes[name] = self.cte(toks[i + 1:end], cols, ctes)
                i = end + 1
                if i < len(toks) and toks[i].op(','):
                    i += 1
                    continue
                break
            toks = toks[i:]
            if not toks:
                return
        head = toks[0]
        if head.word('insert'):
            self.insert(toks, ctes)
        elif head.word('update'):
            self.update(toks, ctes)
        elif head.word('delete'):
            parts, j = self.qualified(toks, 2)
            self.rows.append(Row(self.table_name(parts), 'delete', head.start, {}, self.where_key(toks[j:]),
                                 self.stmt_no))
        elif head.word('select'):
            self.embedded(toks[1:])
        else:
            self.embedded(toks)

    def cte(self, body, cols, ctes):
        if not body:
            return []
        if body[0].word('values'):
            return self.values_rows(body[1:], cols)
        if body[0].word('insert', 'update', 'delete', 'with'):
            self.dml(body, dict(ctes))
            return []
        if body[0].word('select'):
            rows = self.select_rows(body, ctes, cols)
            return rows or []
        return []

    def values_rows(self, toks, cols):
        rows = []
        for part in split_commas(toks[:find_word(toks, {'order', 'limit', 'on', 'returning'})]):
            if not part or not part[0].op('('):
                continue
            end = matching(part, 0)
            items = [evaluate(p) for p in split_commas(part[1:end])]
            if cols:
                rows.append(dict(zip(cols, items)))
            else:
                rows.append({str(k): v for k, v in enumerate(items)})
        return rows

    def select_items(self, toks):
        """[(alias or None, expr tokens)] of one SELECT list (toks start after SELECT)."""
        if toks and toks[0].word('distinct', 'all'):
            toks = toks[1:]
        end = find_word(toks, {'from', 'where', 'union', 'except', 'intersect', 'returning', 'order',
                               'limit', 'group', 'having', 'window', 'on'})
        items = []
        for part in split_commas(toks[:end]):
            if not part:
                continue
            cut = find_word(part, {'as'})
            last = part[-1]
            if cut < len(part):
                items.append((part[cut + 1].value if cut + 1 < len(part) else None, part[:cut]))
            elif len(part) >= 2 and last.kind in ('word', 'qident') and not part[-2].op('.', '::') \
                    and last.value not in ('null', 'true', 'false', 'end', 'default') \
                    and (part[-2].kind in ('string', 'number', 'qident', 'word') or part[-2].op(')')):
                items.append((last.value, part[:-1]))
            else:
                items.append((last.value if last.kind in ('word', 'qident') else None, part))
        return items, toks[end:]

    def select_rows(self, toks, ctes, cols=None):
        """Rows produced by SELECT [... UNION ALL SELECT ...]; values from VALUES CTEs are expanded."""
        rows = []
        branches, cur = [], []
        depth = 0
        for t in toks:
            if t.op('(', '['):
                depth += 1
            elif t.op(')', ']'):
                depth -= 1
            if depth == 0 and t.word('union', 'except', 'intersect'):
                branches.append(cur)
                cur = []
                continue
            if depth == 0 and t.word('all') and not cur:
                continue
            cur.append(t)
        branches.append(cur)
        for branch in branches:
            if not branch or not branch[0].word('select'):
                if branch and branch[0].word('values'):
                    rows.extend(self.values_rows(branch[1:], cols))
                continue
            items, rest = self.select_items(branch[1:])
            source, alias = self.from_source(rest, ctes)
            names = cols or [a for a, _ in items]
            for base in (source or [None]):
                row = {}
                for k, (label, expr) in enumerate(items):
                    key = names[k] if k < len(names) and names[k] else (label or str(k))
                    if not expr:
                        row[key] = Val('expr')
                    elif base is not None:
                        row[key] = bind(expr, base, alias)
                    else:
                        row[key] = evaluate(expr)
                rows.append(row)
        return rows

    STOP = ('where', 'on', 'join', 'left', 'right', 'cross', 'inner', 'full', 'order', 'limit', 'group',
            'union', 'returning', 'natural', 'lateral')

    def from_source(self, rest, ctes):
        """(rows, alias) when FROM names a VALUES list or a CTE with known rows; else (None, None)."""
        if not rest or not rest[0].word('from') or len(rest) < 2:
            return None, None
        if rest[1].op('(') and len(rest) > 2 and rest[2].word('values'):
            close = matching(rest, 1)
            j = close + 1
            if j < len(rest) and rest[j].word('as'):
                j += 1
            alias = rest[j].value if j < len(rest) and rest[j].kind in ('word', 'qident') else None
            cols = None
            if alias and j + 1 < len(rest) and rest[j + 1].op('('):
                cols = [p[0].value for p in split_commas(rest[j + 2:matching(rest, j + 1)]) if p]
            return self.values_rows(rest[3:close], cols), alias
        parts, j = self.qualified(rest, 1)
        if parts and parts[-1] in ctes and isinstance(ctes[parts[-1]], list) and ctes[parts[-1]]:
            alias = parts[-1]
            if j < len(rest) and rest[j].word('as'):
                j += 1
            if j < len(rest) and rest[j].kind in ('word', 'qident') and rest[j].value not in self.STOP:
                alias = rest[j].value
            return ctes[parts[-1]], alias
        return None, None

    def insert(self, toks, ctes):
        parts, i = self.qualified(toks, 2)
        table = self.table_name(parts)
        if i < len(toks) and toks[i].word('as'):
            i += 2
        cols = None
        if i < len(toks) and toks[i].op('('):
            end = matching(toks, i)
            cols = [p[-1].value for p in split_commas(toks[i + 1:end]) if p]
            i = end + 1
        if cols is None:
            cols = self.tables.get('#cols:' + table)
        if i < len(toks) and toks[i].word('overriding'):
            i += 3
        start = toks[0].start
        if i >= len(toks):
            raise ValueError('INSERT without a source')
        src = toks[i:]
        conflict = find_word(src, {'on'})
        while conflict < len(src) - 1 and not src[conflict + 1].word('conflict'):
            conflict = find_word(src, {'on'}, conflict + 1)
        body, tail = src[:conflict], src[conflict:]
        returning = find_word(body, {'returning'})
        body = body[:returning]
        if body[0].word('values'):
            produced = self.values_rows(body[1:], cols)
        elif body[0].word('select') or body[0].op('('):
            if body[0].op('('):
                body = body[1:matching(body, 0)]
            produced = self.select_rows(body, ctes, cols)
            if not produced:
                self.note(start, 'INSERT ... SELECT source not evaluated', raw_text(toks[:16]))
        elif body[0].word('default'):
            produced = [{}]
        elif body[0].word('with'):
            produced = []
            self.note(start, 'INSERT with a nested WITH source not evaluated', raw_text(toks[:16]))
        else:
            raise ValueError('unknown INSERT source')
        for item in produced:
            values = {}
            for key, val in item.items():
                values[key.lower() if isinstance(key, str) else key] = val
            key = self.key_value(table, values)
            self.rows.append(Row(table, 'insert', start, values, key, self.stmt_no))
        if tail and len(tail) > 4:
            j = find_word(tail, {'set'})
            if j < len(tail):
                assigns = self.assignments(tail[j + 1:find_word(tail, {'where', 'returning'}, j + 1)])
                literal = {k: v for k, v in assigns.items() if not (v.kind == 'expr' and 'excluded' in v.raw.lower())}
                if literal:
                    for row in [r for r in self.rows if r.start == start and r.op == 'insert']:
                        self.rows.append(Row(table, 'upsert', start, literal, row.key, self.stmt_no))

    def assignments(self, toks):
        out = {}
        for part in split_commas(toks):
            if not part:
                continue
            eq = next((k for k, t in enumerate(part) if t.op('=')), None)
            if eq is None:
                continue
            lhs, rhs = part[:eq], part[eq + 1:]
            if lhs and lhs[0].op('('):
                names = [p[-1].value for p in split_commas(lhs[1:matching(lhs, 0)]) if p]
                if rhs and rhs[0].op('(') and not (len(rhs) > 1 and rhs[1].word('select')):
                    vals = [evaluate(p) for p in split_commas(rhs[1:matching(rhs, 0)])]
                    out.update(zip(names, vals))
                continue
            if lhs:
                out[lhs[-1].value] = evaluate(rhs) if rhs else Val('expr')
        return out

    def update(self, toks, ctes):
        i = 2 if toks[1].word('only') else 1
        parts, i = self.qualified(toks, i)
        table = self.table_name(parts)
        if toks[i].word('as'):
            i += 1
        if not toks[i].word('set'):
            i += 1  # table alias
        if not toks[i].word('set'):
            raise ValueError('UPDATE without SET')
        end = find_word(toks, {'from', 'where', 'returning'}, i + 1)
        assigns = self.assignments(toks[i + 1:end])
        rest = toks[end:]
        source, src_alias = self.from_source(rest, ctes)
        key = self.where_key(rest)
        if source:
            for base in source:
                values = {}
                for col, val in assigns.items():
                    values[col] = bind(val.tokens, base, src_alias) if val.tokens else val
                rkey = next((v.value for k, v in base.items() if k == 'id' and v.kind == 'str'), key)
                self.rows.append(Row(table, 'update', toks[0].start, values, rkey, self.stmt_no))
            return
        self.rows.append(Row(table, 'update', toks[0].start, assigns, key, self.stmt_no))

    KEY_COLUMNS = ('id', 'document_id', 'spreadsheet_id', 'presentation_id', 'contact_id', 'event_id',
                   'login', 'email_address', 'calendar_id', 'sha')

    def key_value(self, table, values):
        for col in self.KEY_COLUMNS:
            v = values.get(col)
            if v is not None and v.kind in ('str', 'num'):
                return str(v.value)
        return None

    def where_key(self, toks):
        for j in range(len(toks) - 2):
            if toks[j].kind in ('word', 'qident') and toks[j].value in self.KEY_COLUMNS and toks[j + 1].op('=') \
                    and toks[j + 2].kind == 'string':
                return toks[j + 2].value
        return None

# ---------------------------------------------------------------- source loading

def schema_tables(root):
    path = root / SCHEMA
    tables = {}
    if path.is_file():
        for entry in json.loads(path.read_text(encoding='utf-8')):
            full = entry['table_schema'].lower() + '.' + entry['table_name'].lower()
            tables.setdefault(entry['table_name'].lower(), full)
            tables['#cols:' + full] = [c['column'].lower() for c in sorted(entry['columns'], key=lambda c: c['position'])]
            tables['#gen:' + full] = {c['column'].lower(): c.get('note', '') for c in entry['columns'] if c.get('generated')}
            tables['#fmt:' + full] = {c['column'].lower(): c['format'] for c in entry['columns'] if c.get('format')}
            tables['#req:' + full] = [c['column'].lower() for c in sorted(entry['columns'], key=lambda c: c['position'])
                                      if c.get('nullable') == 'NO' and c.get('default') is None
                                      and not c.get('generated')]
    return tables


def read_sql(path):
    raw = path.read_bytes()
    text = raw.decode('utf-8-sig', errors='replace')
    stripped = text.strip()
    unwrapped = False
    if len(stripped) > 1 and stripped[0] == '"' and stripped[-1] == '"':
        # Pasted from a spreadsheet cell: outer quotes and every inner quote doubled.
        text = stripped[1:-1].replace('""', '"')
        unwrapped = True
    return raw, text, unwrapped


class Base:
    """Lazy, read-only view of the base exports a check needs."""

    def __init__(self, root, enabled=True, universe=None):
        self.root, self.enabled, self.loaded, self._cache = root, enabled, [], {}
        self.paths = {}
        manifest = hg_universe.manifest_path(root, universe) if enabled else None
        if enabled and manifest.is_file():
            for service, info in json.loads(manifest.read_text()).get('services', {}).items():
                self.paths[service] = root / info['path']

    def _json(self, service, name):
        key = (service, name)
        if key not in self._cache:
            path = self.paths.get(service)
            data = None
            if path is not None and (path / name).is_file():
                data = json.loads((path / name).read_text(encoding='utf-8'))
                self.loaded.append(service + '/' + name)
            self._cache[key] = data
        return self._cache[key]

    def drive_root(self):
        path = self.paths.get('gdrive')
        return path / 'root' if path is not None and (path / 'root').is_dir() else None

    def drive_bytes(self, content_path):
        root = self.drive_root()
        if root is None:
            return None
        for form in (content_path, unicodedata.normalize('NFC', content_path),
                     unicodedata.normalize('NFD', content_path)):
            candidate = root / form
            if candidate.is_file():
                return candidate.stat().st_size
        return False

    def drive_users(self):
        path = self.paths.get('gdrive')
        if path is None or not (path / 'data.json').is_file():
            return []
        if ('gdrive', 'users') not in self._cache:
            with open(path / 'data.json', 'r', encoding='utf-8') as handle:
                head = handle.read(1 << 16)
            users = []
            at = head.find('"drive_users"')
            if at >= 0:
                try:
                    users, _ = json.JSONDecoder().raw_decode(head, head.index('[', at))
                except ValueError:
                    users = (self._json('gdrive', 'data.json') or {}).get('drive_users', [])
            self.loaded.append('gdrive/data.json#drive_users')
            self._cache[('gdrive', 'users')] = users
        return self._cache[('gdrive', 'users')]

    def accounts(self, service):
        """[{id, names..., emails...}] for one service's account table, keys lowercased."""
        if not self.enabled:
            return []
        if ('accounts', service) in self._cache:
            return self._cache[('accounts', service)]
        rows = []
        if service == 'trello':
            rows = (self._json('trello', 'data.json') or {}).get('members', [])
        elif service == 'slack':
            rows = self._json('slack', 'users.json') or []
        elif service == 'linear':
            rows = (self._json('linear', 'data.json') or {}).get('users', [])
        elif service == 'github':
            rows = (self._json('github', 'data.json') or {}).get('users', [])
        elif service == 'gdrive':
            rows = self.drive_users()
        elif service == 'confluence':
            rows = (self._json('confluence', 'confluence_working.json') or {}).get('users', [])
        elif service == 'contacts':
            rows = (self._json('contacts', 'contacts.json') or {}).get('contacts', [])
        elif service == 'gmail':
            rows = [{'email_address': u.get('emailAddress'), 'name': u.get('name')}
                    for u in self._json('gmail', 'users.json') or []]
        rows = [{k.lower(): v for k, v in row.items()} for row in rows if isinstance(row, dict)]
        self._cache[('accounts', service)] = rows
        return rows

    def extra_actor_ids(self, service):
        """Actor ids the base itself uses without an account row (kept as known)."""
        if service == 'trello' and self.enabled:
            actions = (self._json('trello', 'data.json') or {}).get('actions', [])
            return {a.get('idMemberCreator') for a in actions}
        return set()

# ---------------------------------------------------------------- helpers

ISO = re.compile(r'^(\d{4})-(\d{2})-(\d{2})(?:[T ](\d{2}):(\d{2})(?::(\d{2})(?:\.(\d+))?)?)?\s*'
                 r'(Z|[+-]\d{2}(?::?\d{2})?|UTC|GMT)?$', re.I)
EPOCH = re.compile(r'^\d{9,13}(?:\.\d+)?$')


def instant(value):
    """(datetime UTC, unzoned) for a timestamp-like value, or None."""
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, (int, float)):
        number = float(value)
        if number > 1e11:
            number /= 1000.0
        if 1e8 < number < 1e10:
            return datetime.fromtimestamp(number, tz=timezone.utc), False
        return None
    text = str(value).strip()
    if EPOCH.match(text):
        return instant(float(text))
    m = ISO.match(text)
    if m:
        y, mo, d, h, mi, s, frac, zone = m.groups()
        try:
            dt = datetime(int(y), int(mo), int(d), int(h or 0), int(mi or 0), int(s or 0))
        except ValueError:
            return None
        if zone is None or zone.upper() in ('Z', 'UTC', 'GMT'):
            return dt.replace(tzinfo=timezone.utc), zone is None and h is not None
        sign = 1 if zone[0] == '+' else -1
        digits = zone[1:].replace(':', '')
        offset = timedelta(hours=int(digits[:2]), minutes=int(digits[2:4] or 0))
        return (dt - sign * offset).replace(tzinfo=timezone.utc), False
    if re.search(r'\d{1,2}:\d{2}', text) and re.search(r'[A-Za-z]{3}', text):
        try:
            dt = parsedate_to_datetime(text)
        except (TypeError, ValueError, IndexError):
            return None
        if dt is None:
            return None
        if dt.tzinfo is None:
            return dt.replace(tzinfo=timezone.utc), True
        return dt.astimezone(timezone.utc), False
    return None


def iso(dt):
    return dt.strftime('%Y-%m-%dT%H:%M:%SZ')


ANON = re.compile(r'(?:^|\[)(?:PERSON_NAME|PERSON|EMPLOYEE|SVC|SLACK_BOT|USERNAME|EMAIL|IDENTIFIER)_\d+', re.I)
COMPANY = 'harmonygames.co'


def norm_name(value):
    return ' '.join(re.findall(r'[a-z0-9]+', unicodedata.normalize('NFKD', value).casefold()))


def person_keys(account, spec):
    keys = set()
    for field in spec.get('emails', ()):
        v = account.get(field)
        if isinstance(v, str) and '@' in v and not ANON.search(v):
            keys.add(('email', v.strip().casefold()))
            local, _, domain = v.strip().casefold().partition('@')
            if domain == COMPANY:
                keys.add(('name', norm_name(local)))
    for field in spec.get('names', ()):
        if '+' in field:
            v = ' '.join(str(account.get(f) or '') for f in field.split('+')).strip()
        else:
            v = account.get(field)
        if not isinstance(v, str) or not v.strip() or ANON.search(v.strip()):
            continue
        if '@' in v:
            keys.add(('email', v.strip().casefold()))
            local, _, domain = v.strip().casefold().partition('@')
            if domain == COMPANY:
                keys.add(('name', norm_name(local)))
        elif norm_name(v):
            keys.add(('name', norm_name(v)))
    for field in spec.get('handles', ()):
        v = account.get(field)
        if isinstance(v, str) and v.strip() and not ANON.search(v.strip()) and norm_name(v):
            keys.add(('name', norm_name(v)))
    return keys


def display(account, spec):
    for field in list(spec.get('names', ())) + list(spec.get('handles', ())) + list(spec.get('emails', ())):
        if '+' in field:
            v = ' '.join(str(account.get(f) or '') for f in field.split('+')).strip()
        else:
            v = account.get(field)
        if isinstance(v, str) and v.strip():
            return v
    return str(account.get(spec['id']))


def names_agree(a, b):
    ta, tb = set(norm_name(a).split()), set(norm_name(b).split())
    if not ta or not tb:
        return True
    return bool(ta & tb)


def json_list(val):
    if val is None or val.kind != 'str':
        return []
    try:
        data = json.loads(val.value)
    except ValueError:
        return []
    return [x for x in data if isinstance(x, str)] if isinstance(data, list) else []


def snippet(text, start, end, width=90):
    lo, hi = max(0, start - width), min(len(text), end + width)
    return ('…' if lo else '') + ' '.join(text[lo:hi].split()) + ('…' if hi < len(text) else '')

# ---------------------------------------------------------------- checks

EVENT_FIELDS = {
    'contacts.contacts': ('created_at', 'updated_at'),
    'gcal.gcal_events': ('created', 'updated'),
    'gdocs.docs_documents': ('created_time', 'modified_time'),
    'gdrive.drive_files': ('created_time', 'modified_time'),
    'github.github_commits': ('authored_date', 'committed_date'),
    'github.github_issues': ('created_at', 'updated_at', 'closed_at'),
    'github.github_pr_comments': ('created_at', 'updated_at'),
    'github.github_pull_requests': ('created_at', 'updated_at', 'merged_at', 'closed_at'),
    'github.github_releases': ('created_at', 'published_at'),
    'github.github_repositories': ('created_at', 'updated_at', 'pushed_at'),
    'github.github_review_comments': ('created_at',),
    'github.github_reviews': ('submitted_at',),
    'github.github_tags': ('tagger_date',),
    'github.github_timeline_events': ('created_at',),
    'github.github_users': ('created_at', 'updated_at'),
    'gmail.gmail_messages': ('internal_date', 'date'),
    'gmail.gmail_users': ('created_at',),
    'gsheets.sheets_spreadsheets': ('created_time', 'modified_time'),
    'gslides.slides_presentations': ('created_time', 'modified_time'),
    'linear.linear_comments': ('created_at', 'updated_at'),
    'linear.linear_issues': ('created_at', 'updated_at', 'started_at', 'completed_at', 'canceled_at', 'archived_at'),
    'linear.linear_projects': ('created_at', 'updated_at'),
    'linear.linear_team_memberships': ('created_at',),
    'linear.linear_teams': ('created_at', 'updated_at'),
    'linear.linear_users': ('created_at', 'updated_at'),
    'linear.linear_attachments': (),
    'public._changelog': ('timestamp',),
    'slack.slack_channels': ('created_ts',),
    'slack.slack_drafts': ('created', 'updated'),
    'slack.slack_emojis': ('created',),
    'slack.slack_files': ('created',),
    'slack.slack_messages': ('ts', 'created_at', 'edited_ts', 'latest_reply', 'thread_ts_legacy'),
    'slack.slack_scheduled_messages': ('created',),
    'trello.trello_actions': ('date',),
    'trello.trello_attachments': ('date',),
    'trello.trello_boards': ('datelastactivity', 'datelastview'),
    'trello.trello_cards': ('datelastactivity',),
}
# Plan fields may be after the clock: gcal start/end, linear due_date / start_date / target_date,
# trello due, slack_scheduled_messages.post_at. Unlisted tables use EVENT_NAME only.
EVENT_NAME = re.compile(r'^(?:(?:created|updated|modified|sent|posted|commented|submitted|published|merged|closed|'
                        r'completed|edited|resolved|received|uploaded|deleted|archived)(?:_?(?:at|time|ts|date|on))?|'
                        r'date_?last_?activity|last_?(?:modified|updated|activity|edited)(?:_?(?:at|time|date))?|'
                        r'timestamp)$')


def event_columns(table, cols):
    listed = EVENT_FIELDS.get(table)
    if listed is not None:
        return [c for c in listed if c in cols]
    return [c for c in cols if isinstance(c, str) and EVENT_NAME.match(c)]


def check_future_dates(rows, ctx):
    flags = []
    for row in rows:
        if row.op == 'delete':
            continue
        for col in event_columns(row.table, row.cols):
            val = row.cols[col]
            if val.kind in ('null', 'default', 'bool'):
                continue
            if val.wall_clock:
                flags.append(ctx.flag('future_date', 'FAIL', row, col, val.raw,
                                      'Wall-clock function resolves to the real date when the SQL runs, '
                                      'after the %s clock. Use a fixed timestamp.' % ctx.clock_text))
                continue
            candidates = [val.value] if val.kind in ('str', 'num') else val.literals
            found = [t for t in (instant(c) for c in candidates) if t]
            if not found:
                if val.kind == 'expr':
                    ctx.info(row, col, 'time expression not evaluated: ' + val.raw)
                continue
            when, unzoned = max(found, key=lambda t: t[0])
            if when > ctx.clock:
                shown = val.value if val.kind in ('str', 'num') else val.raw
                flags.append(ctx.flag('future_date', 'FAIL', row, col, shown,
                                      'Event timestamp %s is after the fixed clock %s%s. '
                                      'Only plan fields (due, scheduled start/end, deadline) may be later.'
                                      % (iso(when), ctx.clock_text, ' (unzoned value read as UTC)' if unzoned else '')))
    return flags


def load_contracts(root):
    path = root / CONTRACTS
    if not path.is_file():
        return []
    return json.loads(path.read_text(encoding='utf-8')).get('contracts', [])


def check_id_contracts(rows, ctx):
    flags = []
    for contract in ctx.contracts:
        pattern = re.compile(contract['pattern'])
        column = contract['column']
        for row in rows:
            if row.table not in contract['tables'] or column not in row.cols or row.op == 'delete':
                continue
            val = row.cols[column]
            if val.kind in ('null', 'default'):
                if not contract.get('allow_null', True):
                    flags.append(ctx.flag('id_contract', 'FAIL', row, column, None,
                                          '%s: NULL is not allowed. %s' % (contract['id'], contract['rule'])))
                continue
            if val.kind != 'str':
                if val.kind == 'expr':
                    ctx.info(row, column, '%s not evaluated: %s' % (contract['id'], val.raw))
                    continue
            text = str(val.value)
            problem = None
            if not pattern.fullmatch(text):
                problem = 'does not match %s' % contract['pattern']
            seg = contract.get('first_segment_equals')
            if problem is None and seg:
                owner = row.cols.get(seg)
                if owner is not None and owner.kind == 'str' and text.split('/', 1)[0] != owner.value:
                    problem = 'first path segment %r is not the %s %r' % (text.split('/', 1)[0], seg, owner.value)
            if problem:
                flags.append(ctx.flag('id_contract', 'FAIL', row, column, text,
                                      '%s: %s. %s' % (contract['id'], problem, contract['rule'])))
    return flags


GOOGLE_DOC = 'application/vnd.google-apps.document'
GOOGLE_SHEET = 'application/vnd.google-apps.spreadsheet'
GOOGLE_SLIDES = 'application/vnd.google-apps.presentation'
NOT_CONTENT = {'application/vnd.google-apps.folder', 'application/vnd.google-apps.shortcut'}
DOCUMENT_MIME = re.compile(r'^(?:text/|application/(?:pdf|json|xml|rtf|msword|vnd\.ms-|vnd\.openxmlformats-officedocument|'
                           r'vnd\.oasis\.opendocument|vnd\.google-apps\.(?:document|spreadsheet|presentation)))', re.I)
DOCUMENT_EXT = re.compile(r'\.(?:txt|md|markdown|csv|tsv|pdf|docx?|xlsx?|pptx?|json|html?|rtf|xml|ya?ml|log|odt|ods)$', re.I)


def is_document(mime, name):
    """Files whose content the agent reads. Media and binary files (video, audio, images, archives,
    packages) carry metadata only: the base ships no bytes for that kind of file."""
    if mime:
        return bool(DOCUMENT_MIME.match(mime)) or (mime == 'application/octet-stream' and bool(DOCUMENT_EXT.search(name)))
    return not name or bool(DOCUMENT_EXT.search(name)) or '.' not in name


def _text(val):
    return val.value if val is not None and val.kind == 'str' else None


def _nonempty(val):
    if val is None:
        return False
    if val.kind == 'str':
        return bool(val.value.strip())
    return val.kind == 'expr' and any(isinstance(x, str) and x.strip() for x in val.literals)


def check_drive_readable(rows, ctx):
    flags = []
    docs, sheets, slides = {}, set(), set()
    for row in rows:
        if row.table == 'gdocs.docs_documents' and row.op in ('insert', 'update', 'upsert'):
            body = _nonempty(row.cols.get('body_text'))
            for key in (row.key, _text(row.cols.get('document_id')), _text(row.cols.get('drive_file_id'))):
                if key:
                    docs[key] = docs.get(key) or body
        elif row.table in ('gsheets.sheets_spreadsheets', 'gdrive.drive_sheets'):
            sheets.update(k for k in (row.key, _text(row.cols.get('spreadsheet_id')),
                                      _text(row.cols.get('drive_file_id'))) if k)
        elif row.table == 'gslides.slides_presentations':
            slides.update(k for k in (row.key, _text(row.cols.get('presentation_id')),
                                      _text(row.cols.get('drive_file_id'))) if k)
    media = []
    for row in rows:
        if row.table != 'gdrive.drive_files' or row.op != 'insert':
            continue
        mime = _text(row.cols.get('mime_type')) or ''
        if mime in NOT_CONTENT:
            continue
        fid = row.key or _text(row.cols.get('id')) or '?'
        name = _text(row.cols.get('name')) or ''
        if not is_document(mime, name):
            if not _text(row.cols.get('content_path')):
                media.append((row, name))
            continue
        path_val = row.cols.get('content_path')
        path = _text(path_val)
        content_text = _text(row.cols.get('content_text'))
        if path_val is not None and path_val.kind == 'expr':
            ctx.info(row, 'content_path', 'content_path not evaluated: ' + path_val.raw)
            continue
        if mime == GOOGLE_DOC and docs.get(fid):
            continue
        if mime == GOOGLE_SHEET and fid in sheets:
            continue
        if mime == GOOGLE_SLIDES and fid in slides:
            continue
        if path:
            bad_shape = not ctx.path_pattern.fullmatch(path) if ctx.path_pattern else False
            size = ctx.base.drive_bytes(path) if not bad_shape else False
            if size:
                continue
            if size is None and not bad_shape:
                ctx.info(row, 'content_path', 'base Drive bytes not available; content_path not verified')
                continue
            why = ('content_path %r is not in the base path format' % path if bad_shape else
                   'content_path %r points at no bytes in the base Drive export (injection cannot add bytes)' % path)
        elif mime == GOOGLE_DOC:
            why = ('Google Doc with no docs_documents row with non-empty body_text in this SQL'
                   + (' (a docs row exists but body_text is empty)' if fid in docs else ''))
        elif content_text and content_text.strip():
            why = ('null content_path; content_text alone is not served by Drive reads (task 6abc06…073709 '
                   'kept its .txt text in content_text and every read returned 503)')
        else:
            why = 'null content_path and empty content_text'
        flags.append(ctx.flag('drive_unreadable', 'FAIL', row, 'content_path', path,
                              '%s (%s, %s): %s. Make it a Google Doc with a docs_documents row, or point '
                              'content_path at real bytes in the base path format.' % (fid, name, mime or 'no mime', why)))
    if media:
        ctx.info(media[0][0], 'content_path',
                 '%d injected media/binary Drive file(s) have no bytes (metadata only), e.g. %s. Fine when the '
                 'task needs only names, folders or sizes; FAIL if a row or the OE depends on their content.'
                 % (len(media), ', '.join(n for _, n in media[:3])))
    return flags


ACCOUNT_TABLES = {
    'trello.trello_members': {'service': 'trello', 'id': 'id', 'names': ('fullname',), 'handles': ('username',)},
    'slack.slack_users': {'service': 'slack', 'id': 'id', 'names': ('real_name', 'display_name', 'name'),
                          'emails': ('email',)},
    'linear.linear_users': {'service': 'linear', 'id': 'id', 'names': ('name', 'display_name'), 'emails': ('email',)},
    'github.github_users': {'service': 'github', 'id': 'login', 'names': ('name',), 'emails': ('email',)},
    'gdrive.drive_users': {'service': 'gdrive', 'id': 'id', 'names': ('display_name',), 'emails': ('email',)},
    'confluence.confluence_users': {'service': 'confluence', 'id': 'id', 'names': ('display_name',),
                                    'emails': ('email',)},
    'contacts.contacts': {'service': 'contacts', 'id': 'contact_id', 'names': ('first_name+last_name',),
                          'emails': ('email',)},
    'gmail.gmail_users': {'service': 'gmail', 'id': 'email_address', 'names': ('name',),
                          'emails': ('email_address',)},
}
SERVICE_SPEC = {spec['service']: spec for spec in ACCOUNT_TABLES.values()}
ACTOR_REFS = {
    'trello.trello_actions': (('idmembercreator', 'trello', False),),
    'trello.trello_cards': (('idmembers_json', 'trello', True),),
    'slack.slack_messages': (('user_id', 'slack', False),),
    'slack.slack_files': (('user_id', 'slack', False),),
    'slack.slack_channels': (('creator_id', 'slack', False),),
    'linear.linear_comments': (('author_id', 'linear', False),),
    'linear.linear_issues': (('creator_id', 'linear', False), ('assignee_id', 'linear', False)),
    'linear.linear_projects': (('lead_id', 'linear', False),),
    'github.github_pr_comments': (('author_login', 'github', False),),
    'github.github_review_comments': (('author_login', 'github', False),),
    'github.github_reviews': (('author_login', 'github', False),),
    'github.github_issues': (('author_login', 'github', False),),
    'github.github_pull_requests': (('author_login', 'github', False), ('merged_by_login', 'github', False)),
    'github.github_commits': (('author_login', 'github', False), ('committer_login', 'github', False)),
    'github.github_timeline_events': (('actor_login', 'github', False),),
    'confluence.confluence_pages': (('author_id', 'confluence', False),),
    'confluence.confluence_comments': (('author_id', 'confluence', False),),
    'gmail.gmail_messages': (('user_email', 'gmail', False),),
    'gmail.gmail_threads': (('user_email', 'gmail', False),),
}
SLACK_BOT = re.compile(r'^(?:B[A-Z0-9]{6,}|USLACKBOT)$')


def check_identities(rows, ctx):
    flags = []
    inserted = {}  # service -> [(account dict, row)]
    for row in rows:
        spec = ACCOUNT_TABLES.get(row.table)
        if spec is None or row.op not in ('insert', 'upsert'):
            continue
        account = {k: v.value for k, v in row.cols.items() if v.kind in ('str', 'num')}
        account_id = account.get(spec['id'])
        keys = person_keys(account, spec)
        others = [(a, 'base') for a in ctx.base.accounts(spec['service'])] + \
                 [(a, 'SQL') for a, _ in inserted.get(spec['service'], [])]
        hits = []
        for other, origin in others:
            other_id = other.get(spec['id'])
            if other_id is None or str(other_id) == str(account_id):
                continue
            shared = keys & person_keys(other, spec)
            if shared:
                hits.append('%s account %s (%s) on %s' % (origin, other_id, display(other, spec),
                                                          ', '.join(sorted('%s %r' % k for k in shared))))
        if hits and row.op == 'insert':
            flags.append(ctx.flag('duplicate_account', 'FAIL', row, spec['id'], account_id,
                                  'Second %s account for an existing person: matches %s. One person, one account '
                                  'per service; reuse the existing id. Override only for a real namesake (cite '
                                  'the records that show two people).' % (spec['service'], '; '.join(hits[:3]))))
        inserted.setdefault(spec['service'], []).append((account, row))

    known = {}

    def known_ids(service):
        if service not in known:
            spec = SERVICE_SPEC[service]
            ids = {str(a.get(spec['id'])) for a in ctx.base.accounts(service)}
            ids |= {str(a.get(spec['id'])) for a, _ in inserted.get(service, [])}
            ids |= {str(x) for x in ctx.base.extra_actor_ids(service) if x}
            if service == 'gmail':
                ids = {i.casefold() for i in ids}
            known[service] = ids
        return known[service]

    def account_for(service, actor):
        spec = SERVICE_SPEC[service]
        pool = [a for a, _ in inserted.get(service, [])] + ctx.base.accounts(service)
        return next((a for a in pool if str(a.get(spec['id'])) == str(actor)), None), spec

    if ctx.base.enabled:
        for row in rows:
            if row.op == 'delete':
                continue
            for column, service, is_list in ACTOR_REFS.get(row.table, ()):
                val = row.cols.get(column)
                if val is None or val.kind != 'str':
                    continue
                actors = json_list(val) if is_list else [val.value]
                for actor in actors:
                    if not actor or service == 'slack' and SLACK_BOT.match(actor):
                        continue
                    probe = actor.casefold() if service == 'gmail' else actor
                    if probe not in known_ids(service):
                        hint = ''
                        if service == 'gmail' and '@' in probe:
                            first = re.split(r'[._-]', probe.split('@')[0])[0]
                            near = sorted(i for i in known_ids('gmail') if i.split('@')[0].startswith(first))
                            if near:
                                hint = ' Base Gmail mailbox(es) for that name: %s.' % ', '.join(near[:3])
                        flags.append(ctx.flag('unknown_actor', 'CHECK', row, column, actor,
                                              'No %s account in the base or this SQL has id %r. Confirm the '
                                              'actor exists; otherwise use the existing account id.%s'
                                              % (service, actor, hint)))
        # The record names a person: the id must belong to that person.
        for row in rows:
            if row.table == 'gmail.gmail_messages' and row.op != 'delete':
                sender, name = _text(row.cols.get('from_email')), _text(row.cols.get('from_name'))
                if sender and name and not ANON.search(name) and sender.casefold() in ctx.email_names():
                    expected = ctx.email_names()[sender.casefold()]
                    if not any(names_agree(name, e) for e in expected):
                        flags.append(ctx.flag('actor_name', 'FAIL', row, 'from_name', name,
                                              'from_email %s belongs to %s, but the message names %r.'
                                              % (sender, ' / '.join(sorted(expected)), name)))
            if row.table == 'trello.trello_actions' and row.op != 'delete':
                creator = _text(row.cols.get('idmembercreator'))
                data = _text(row.cols.get('data_json')) or _text(row.cols.get('data'))
                try:
                    named = (json.loads(data) or {}).get('memberCreator') if data else None
                except (ValueError, AttributeError):
                    named = None
                if creator and isinstance(named, dict):
                    account, spec = account_for('trello', creator)
                    full = named.get('fullName') or named.get('username')
                    if account and full and not ANON.search(str(full)) and \
                            not names_agree(str(full), display(account, spec)):
                        flags.append(ctx.flag('actor_name', 'FAIL', row, 'idmembercreator', creator,
                                              'idMemberCreator %s is %s, but data_json.memberCreator names %r.'
                                              % (creator, display(account, spec), full)))
            if row.table == 'github.github_commits' and row.op != 'delete':
                login, name = _text(row.cols.get('author_login')), _text(row.cols.get('author_name'))
                if login and name and not ANON.search(name):
                    account, spec = account_for('github', login)
                    shown = account and account.get('name')
                    if shown and not ANON.search(str(shown)) and not names_agree(name, str(shown)):
                        flags.append(ctx.flag('actor_name', 'FAIL', row, 'author_name', name,
                                              'author_login %s is %s, but the commit names %r.'
                                              % (login, shown, name)))
    return flags


GRADER_PATTERNS = (
    ('self_reference', re.compile(
        r"\bthis (?:description|tab|sheet|doc(?:ument)?|card|ticket|issue|record|note|message|page|thread|file|"
        r"email|comment|post|row|column|field|list|table) (?:does not|doesn't|do not|don't|will not|won't|cannot) "
        r"(?:state|say|list|include|contain|give|show|mention|specify|spell out|provide|tell)\b", re.I)),
    ('solver_address', re.compile(
        r"\b(?:the|an|any|each|your) (?:solver|grader|evaluator|llm|ai agent|ai model|language model)s?\b|"
        r"\bthe agent (?:should|must|will|needs? to|has to|cannot|can't|may not)\b|"
        r"\bfollow (?:that|this) record\b|\bfinal response\b", re.I)),
    ('test_terms', re.compile(
        r"\b(?:rubrics?|ground[- ]truth|golden (?:answer|response|solution)|answer key|expected (?:answer|output)|"
        r"test cases?|grader|pass@\d|pass rate|eval(?:uation)? criteria|scoring rule)\b", re.I)),
    ('trap_terms', re.compile(r"\b(?:decoys?|distractors?|red herrings?|gotchas?)\b", re.I)),
    ('spec_terms', re.compile(
        r"\b(?:required fields?|tie[- ]?break(?:er|ers|ing)?|break (?:a |any |every )?ties?|"
        r"resolv(?:e|ing) (?:every|all|any) ties?|deterministic(?:ally)?)\b", re.I)),
    # Capitalized workflow states defined for the reader ("Done = ...", "Todo when ..."); case-sensitive.
    ('state_rules', re.compile(r"\b(?:Done|Todo|To Do|In Progress|Backlog|Blocked|Canceled)\s*(?:=|means\b|when\b)")),
)
PADDING = re.compile(
    r"\b(?:tool[- ]?calls?|call (?:count|volume)|surface area|pass[- ]?rates?|pass@\d|gates?|hardness|harder|"
    r"difficulty|baselines?|noise|padding|filler|decoys?|distractors?|red herrings?|misleaders?|haystack|needles?|"
    r"traps?|friction|ground truth|golden|rubrics?|criteri(?:a|on)|graders?|judges?|verifiers?|the agent|solvers?|"
    r"trajector(?:y|ies)|giveaways?|every run|runs? (?:fail|pass)(?:es|ed)?)\b", re.I)


def check_grader_language(rows, ctx):
    """One flag per table/column/phrase set; later records with the same hit are listed under 'also'."""
    flags, grouped = [], {}
    for row in rows:
        if row.op == 'delete':
            continue
        for col, val in row.cols.items():
            if val.kind == 'str':
                text = val.value
            elif val.kind == 'expr':
                text = ' '.join(x for x in val.literals if isinstance(x, str))
            else:
                continue
            if len(text) < 12:
                continue
            hits = []
            for label, pattern in GRADER_PATTERNS:
                m = pattern.search(text)
                if m:
                    hits.append((label, m))
            if not hits:
                continue
            group = (row.table, col, tuple((h[0], h[1].group(0).lower()) for h in hits))
            if group in grouped:
                grouped[group]['records'].append(row.key)
                continue
            first = min(hits, key=lambda h: h[1].start())[1]
            flag = ctx.flag('grader_language', 'CHECK', row, col, snippet(text, first.start(), first.end()),
                            'Possible grader-facing text (%s: %s). Text addressed to a solver or grader, '
                            'or describing the test, fails Check C; in-world content passes.'
                            % (', '.join(h[0] for h in hits), ', '.join(repr(h[1].group(0)) for h in hits)))
            flag['records'] = [row.key]
            grouped[group] = flag
            flags.append(flag)
    for flag in flags:
        records = flag.pop('records')
        if len(records) > 1:
            flag['also'] = {'count': len(records) - 1, 'records': records[1:11]}
    return flags


def check_generated_columns(rows, tables, ctx):
    """A column the database computes itself (e.g. slack_messages.text_fts) can only be DEFAULT: the platform
    rejects any other value ("can only be updated to DEFAULT"), and in one transaction that undoes the whole script."""
    flags = []
    for row in rows:
        generated = tables.get('#gen:' + row.table) or {}
        for col, val in row.cols.items():
            name = col.lower() if isinstance(col, str) else col
            if name in generated and val.kind != 'default':
                verb = 'inserts a value into' if row.op == 'insert' else 'updates'
                flags.append(ctx.flag('generated_column', 'FAIL', row, col, val.raw or str(val.value),
                                      'The statement %s %s.%s, which the database computes itself: %s. '
                                      'The platform rejects this ("can only be updated to DEFAULT") and the whole '
                                      'script can roll back. Remove it from the statement.'
                                      % (verb, row.table, name, generated[name] or 'generated column')))
    return flags


TEXT_TIME = {
    'iso_utc': (re.compile(r'\d{4}-\d\d-\d\dT\d\d:\d\d:\d\dZ'), 'YYYY-MM-DDTHH:MM:SSZ (e.g. 2025-09-30T14:12:09Z)'),
    'date': (re.compile(r'\d{4}-\d\d-\d\d'), 'YYYY-MM-DD (e.g. 2025-10-03)'),
}
TIME_CAST = re.compile(r'::\s*(?:timestamp|timestamptz|date)\b|\bat\s+time\s+zone\b|\bto_timestamp\b|\bmake_timestamp', re.I)
STRING_AT = re.compile(r"(?:[Ee]?'(?:[^']|'')*'|(\$\w*\$).*?\1)", re.S)
CAST_AFTER = re.compile(r'\s*::\s*(?:timestamp|timestamptz|date)\b', re.I)
CAST_BEFORE = re.compile(r'\bcast\s*\(\s*$', re.I)


def cast_to_time(text, start):
    """Was the string literal at `start` cast to a timestamp/date? The parser drops casts, but in a text column
    Postgres then stores the cast's own output ('2025-09-30 14:12:09+00'), not the literal."""
    if CAST_BEFORE.search(text[max(0, start - 20):start]):
        return True
    m = STRING_AT.match(text, start)
    return bool(m and CAST_AFTER.match(text, m.end()))


def check_text_time_formats(rows, tables, ctx):
    """Linear stores its dates as text. The database keeps whatever the SQL writes, but the agent run's Linear load
    only parses the base-data format, so '2025-09-30 14:12:09+00' fails the run ("cannot parse timestamp")."""
    flags = []
    for row in rows:
        formats = tables.get('#fmt:' + row.table) or {}
        if row.op == 'delete' or not formats:
            continue
        for col, val in row.cols.items():
            name = col.lower() if isinstance(col, str) else col
            if name not in formats or val.kind in ('null', 'default'):
                continue
            pattern, shown = TEXT_TIME[formats[name]]
            if val.kind == 'str':
                bad = not pattern.fullmatch(str(val.value)) or bool(val.start and cast_to_time(ctx.text, val.start))
            elif val.wall_clock or TIME_CAST.search(val.raw or ''):
                bad = True
            elif val.kind == 'expr':
                lits = [str(x) for x in val.literals if isinstance(x, str) and re.match(r'\d{4}-\d\d-\d\d', str(x))]
                if not lits:
                    ctx.info(row, col, 'text date expression not evaluated: ' + (val.raw or ''))
                    continue
                bad = not all(pattern.fullmatch(x) for x in lits)
            else:
                bad = True
            if bad:
                flags.append(ctx.flag('text_time_format', 'FAIL', row, col, val.raw or str(val.value),
                                      '%s.%s is a text column: the value is stored exactly as written, and the agent '
                                      'run fails to load the service unless it is written as %s, the base-data format '
                                      '(no space, no +00 / +00:00, no milliseconds, no casts or now()).'
                                      % (row.table, name, shown)))
    return flags


def check_missing_required(rows, tables, ctx):
    """An INSERT must give every NOT NULL column that has no default; the platform rejects the row otherwise
    ("null value in column ... violates not-null constraint"), which can stop the rest of the script."""
    flags, seen = [], set()
    for row in rows:
        if row.op != 'insert':
            continue
        required = tables.get('#req:' + row.table) or []
        given = {c.lower() if isinstance(c, str) else c for c in row.cols}
        missing = [c for c in required if c not in given]
        nulls = [c for c in required if c in given and row.cols[c].kind == 'null']
        for col in missing + nulls:
            if (row.start, col) in seen:
                continue
            seen.add((row.start, col))
            what = 'leaves out' if col in missing else 'sets NULL in'
            flags.append(ctx.flag('missing_required', 'FAIL', row, col, None if col in missing else 'NULL',
                                  'The INSERT %s %s.%s, which is NOT NULL with no default in the platform database. '
                                  'The platform rejects it ("null value in column %s violates not-null '
                                  'constraint"). Give it a value in the base-data shape%s.'
                                  % (what, row.table, col, col,
                                     " ('[]' for a new issue)" if col == 'state_history_json' else '')))
    return flags


def check_padding_comments(comments, ctx):
    flags = []
    for comment in comments:
        words = sorted({m.group(0).lower() for m in PADDING.finditer(comment.value)})
        if words:
            flags.append({'check': 'padding_comment', 'severity': 'CHECK', 'line': ctx.line(comment.start),
                          'value': comment.value[:200],
                          'message': 'SQL comment mentions %s. Comments are evidence of intent: a record added to '
                                     'raise tool calls or lower the pass rate fails unless it has a task purpose.'
                                     % ', '.join(words)})
    return flags

# ---------------------------------------------------------------- driver

class Context:
    def __init__(self, text, base, contracts):
        self.text, self.base, self.contracts, self.infos = text, base, contracts, []
        self._lines = None
        self._email_names = None
        self._seen = set()
        path = next((c for c in contracts if c.get('column') == 'content_path'), None)
        self.path_pattern = re.compile(path['pattern']) if path else None

    def line(self, offset):
        if self._lines is None:
            self._lines = [m.start() for m in re.finditer('\n', self.text)]
        return bisect.bisect_left(self._lines, offset) + 1

    def flag(self, check, severity, row, column, value, message):
        val = row.cols.get(column)
        at = val.start if val is not None and val.start else row.start
        return {'check': check, 'severity': severity, 'line': self.line(at), 'table': row.table,
                'op': row.op, 'record': row.key, 'column': column,
                'value': value if not isinstance(value, str) or len(value) <= 240 else value[:237] + '…',
                'message': message}

    def info(self, row, column, message):
        val = row.cols.get(column)
        line = self.line(val.start if val is not None and val.start else row.start)
        key = (line, row.table, row.key, column)
        if key not in self._seen:
            self._seen.add(key)
            self.infos.append({'check': 'unparsed', 'severity': 'INFO', 'line': line, 'table': row.table,
                               'record': row.key, 'column': column, 'message': message[:240]})

    def email_names(self):
        if self._email_names is None:
            names = {}
            for service in ('slack', 'contacts', 'confluence', 'linear'):
                spec = SERVICE_SPEC[service]
                for account in self.base.accounts(service):
                    for field in spec.get('emails', ()):
                        email = account.get(field)
                        if not isinstance(email, str) or '@' not in email or ANON.search(email):
                            continue
                        shown = display(account, spec)
                        if shown and '@' not in shown and not ANON.search(shown):
                            names.setdefault(email.casefold(), set()).add(shown)
            self._email_names = names
        return self._email_names


def lint(text, root=ROOT, checks=CHECKS, use_base=True, sql_label='<text>', raw=None, unwrapped=False,
         universe=None):
    universe = hg_universe.info(root, universe)
    tables = schema_tables(root)
    toks, comments = tokenize(text)
    parser = Parser(tables)
    for stmt in statements(toks):
        parser.statement(stmt)
    comments = comments + parser.extra_comments
    base = Base(root, enabled=use_base, universe=universe['key'])
    ctx = Context(text, base, load_contracts(root))
    ctx.clock, ctx.clock_text = universe['clock'], universe['clock_text']
    rows = parser.rows
    flags = []
    if 'future_date' in checks:
        flags += check_future_dates(rows, ctx)
    if 'id_contract' in checks:
        flags += check_id_contracts(rows, ctx)
    if 'drive_unreadable' in checks:
        flags += check_drive_readable(rows, ctx)
    if 'identities' in checks:
        flags += check_identities(rows, ctx)
    if 'grader_language' in checks:
        flags += check_grader_language(rows, ctx)
    if 'padding_comment' in checks:
        flags += check_padding_comments(comments, ctx)
    if 'generated_column' in checks:
        flags += check_generated_columns(rows, tables, ctx)
    if 'text_time_format' in checks:
        flags += check_text_time_formats(rows, tables, ctx)
    if 'missing_required' in checks:
        flags += check_missing_required(rows, tables, ctx)
    infos = ctx.infos + [{'check': 'unparsed', 'severity': 'INFO', 'line': ctx.line(u['start']),
                          'message': u['reason'], 'value': u['text']} for u in parser.unparsed]
    if unwrapped:
        infos.insert(0, {'check': 'unparsed', 'severity': 'INFO', 'line': 1,
                         'message': 'Input was wrapped in spreadsheet quotes; outer quotes removed and doubled '
                                    'quotes collapsed before parsing. Confirm against the platform copy.'})
    flags.sort(key=lambda f: (f['line'], f['check']))
    per_table = {}
    for row in rows:
        per_table.setdefault(row.table, {}).setdefault(row.op, 0)
        per_table[row.table][row.op] += 1
    counts = {'FAIL': 0, 'CHECK': 0, 'INFO': len(infos), 'by_check': {}}
    for f in flags:
        counts[f['severity']] += 1
        counts['by_check'][f['check']] = counts['by_check'].get(f['check'], 0) + 1
    return {
        'tool': 'hg_injection_lint', 'version': VERSION, 'sql': sql_label,
        'sha256': hashlib.sha256(raw if raw is not None else text.encode()).hexdigest(),
        'universe': universe['key'], 'clock': iso(universe['clock']), 'checks': list(checks),
        'statements': {'total': sum(parser.kinds.values()), 'by_kind': parser.kinds},
        'rows': per_table,
        'base': {'used': base.enabled, 'loaded': base.loaded},
        'counts': counts, 'flags': flags, 'info': infos,
        'note': 'Flags are leads, not verdicts. Resolve every FAIL and CHECK in the report; checks A-C still apply.',
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    parser.add_argument('--sql', help='SQL file (default: the saved injection input)')
    parser.add_argument('--checks', help='comma-separated subset of: ' + ', '.join(CHECKS))
    parser.add_argument('--no-base', action='store_true', help='skip base-export lookups (identities, Drive bytes)')
    parser.add_argument('--summary', action='store_true', help='print counts only, without flag details')
    args = parser.parse_args(argv)
    path = Path(args.sql) if args.sql else ROOT / SAVED_SQL
    if not path.is_file():
        print(json.dumps({'error': 'SQL not found: %s' % path}))
        return 2
    checks = CHECKS
    if args.checks:
        checks = tuple(c.strip() for c in args.checks.split(',') if c.strip())
        unknown = [c for c in checks if c not in CHECKS]
        if unknown:
            print(json.dumps({'error': 'unknown checks: %s' % ', '.join(unknown)}))
            return 2
    raw, text, unwrapped = read_sql(path)
    try:
        hg_universe.selected(ROOT)
    except hg_universe.UniverseNotSelected as error:
        print(json.dumps({'error': str(error), 'question': hg_universe.QUESTION}))
        return 2
    try:
        result = lint(text, root=ROOT, checks=checks, use_base=not args.no_base, sql_label=str(path), raw=raw,
                      unwrapped=unwrapped)
    except ValueError as error:
        print(json.dumps({'error': 'could not tokenize SQL: %s' % error, 'sql': str(path)}))
        return 1
    if args.summary:
        result = {k: v for k, v in result.items() if k not in ('flags', 'info')}
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == '__main__':
    sys.exit(main())
