"""Independent parse-back of the generators' injection SQL, built on the eval's own tokenizer.

The point of this module is independence: it does not import the emitter (core/sqlvalue), the emitters'
own parser, or Task_Authoring/tools/sql_lint.py. It loads Evals/tools/hg_injection_lint.py (the tokenizer
the eval uses, read-only) from bytes it hashes and compiles itself, parses INSERT/UPDATE statements itself
from that tokenizer's tokens, and returns generators.core.ops.Op records that compare.py can check against
the intended ops.

Everything fails closed with ParseBackError: statements that are not INSERT/UPDATE/BEGIN/COMMIT, anything
the eval parser could not evaluate, a value that is not a plain literal, a column/value count mismatch
(the eval's values_rows zips silently), an UPDATE whose SET/WHERE is not `col = literal` pairs, and a
column that is not in the schema.

Known eval-tokenizer limits wrapped here:
  * values_rows zips columns and values, so a count mismatch is invisible: we count split_commas parts.
  * where_key keeps one key column: we parse every WHERE pair ourselves.
  * quoted identifiers are lower-cased: we restore the schema's exact case.
  * negative numbers become float: we rebuild the number from the literal text (int or Decimal).
"""
from __future__ import annotations

import hashlib
import json
import sys
import types
from decimal import Decimal, InvalidOperation
from pathlib import Path

from generators.core.ops import INSERT, UPDATE, Op

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_EVALS_TOOLS = REPO_ROOT / "Evals" / "tools"

_PARSERS: dict[str, "EvalParser"] = {}
_SCHEMAS: dict[str, "_Schema"] = {}


class ParseBackError(Exception):
    """The text is outside the grammar, or the eval tokenizer cannot be trusted for it."""

    def __init__(self, message: str, line: int = 0):
        self.message = message
        self.line = int(line or 0)
        super().__init__(f"line {self.line}: {message}" if self.line else message)


class EvalParser:
    """The eval's tokenizer/parser, loaded from Evals/tools, plus the hashes of the files it came from."""

    def __init__(self, directory: Path, module, pins: dict[str, str]):
        self.directory = Path(directory)
        self.module = module
        self.pins = dict(pins)
        self.VERSION = getattr(module, "VERSION", "unversioned")
        self.ROOT = module.ROOT
        self.tokenize = module.tokenize
        self.statements = module.statements
        self.split_commas = module.split_commas
        self.matching = module.matching
        self.find_word = module.find_word
        self.evaluate = module.evaluate
        self.schema_tables = module.schema_tables
        self.Parser = module.Parser
        self._table_index: dict | None = None

    @property
    def table_index(self) -> dict:
        """The eval's own table map (schema_tables(ROOT)); built once."""
        if self._table_index is None:
            self._table_index = self.schema_tables(self.ROOT)
        return self._table_index

    def line_of(self, text: str, offset: int) -> int:
        return text.count("\n", 0, max(0, offset)) + 1


def _load_module(name: str, path: Path, source: bytes):
    """Execute exactly `source` (the bytes that were hashed) as module `name`; nothing is written to disk."""
    module = types.ModuleType(name)
    module.__file__ = str(path)
    previous = sys.modules.get(name)
    sys.modules[name] = module
    try:
        # dont_inherit: compiled with the eval file's own __future__ flags, as the eval runs it, not this module's
        exec(compile(source, str(path), "exec", dont_inherit=True), module.__dict__)  # noqa: S102 - pinned tokenizer
    except BaseException:
        if previous is None:
            sys.modules.pop(name, None)
        else:
            sys.modules[name] = previous
        raise
    return module


def load_eval_parser(evals_tools: Path | None = None) -> EvalParser:
    """Load Evals/tools/hg_injection_lint.py (and its hg_universe) from bytes read once, hashed and compiled — no
    bytecode under Evals/, and the pins always describe the code in use; cached by that content."""
    directory = Path(evals_tools).resolve() if evals_tools is not None else DEFAULT_EVALS_TOOLS.resolve()
    lint_path = directory / "hg_injection_lint.py"
    universe_path = directory / "hg_universe.py"
    sources = {}
    for path in (lint_path, universe_path):
        try:
            sources[path.name] = path.read_bytes()
        except OSError:
            raise ParseBackError(f"eval tokenizer not found: {path}") from None
    pins = {name: hashlib.sha256(data).hexdigest() for name, data in sources.items()}
    key = f"{directory}|{pins[lint_path.name]}|{pins[universe_path.name]}"
    cached = _PARSERS.get(key)
    if cached is not None:
        return cached
    previous_universe = sys.modules.get("hg_universe")
    _load_module("hg_universe", universe_path, sources[universe_path.name])
    try:
        module = _load_module("hg_injection_lint", lint_path, sources[lint_path.name])
    finally:
        if previous_universe is not None:
            sys.modules["hg_universe"] = previous_universe
    parser = EvalParser(directory, module, pins)
    _PARSERS[key] = parser
    return parser


def _ident(token) -> tuple[str, bool]:
    """(the name PostgreSQL resolves, quoted?): a quoted identifier keeps its exact spelling (the eval tokenizer
    lower-cases it, so it is re-read from the token text); an unquoted one folds to lower case."""
    if token.kind == "qident":
        return token.text[1:-1].replace('""', '"'), True
    return token.value, False


def _case_hint(name: str, quoted: bool, candidates) -> str:
    hits = [c for c in candidates if c.lower() == name.lower()]
    if not hits:
        return ""
    return f" (the schema has {hits[0]!r}: " + ("quoted identifiers are case-sensitive)" if quoted
                                                 else "write it quoted, unquoted names fold to lower case)")


class _Schema:
    """The live universe schema; names are matched exactly as PostgreSQL would resolve them."""

    def __init__(self, path: Path, raw: bytes):
        self.path = Path(path)
        try:
            entries = json.loads(raw.decode("utf-8"))
        except ValueError as error:
            raise ParseBackError(f"schema {self.path} is not JSON: {error}") from None
        if not isinstance(entries, list):
            raise ParseBackError(f"schema {self.path} must be a list of tables")
        self.tables: dict[str, tuple[str, tuple[str, ...]]] = {}
        for entry in entries:
            full = f"{entry['table_schema']}.{entry['table_name']}"
            columns = tuple(c["column"] for c in sorted(entry["columns"], key=lambda c: c["position"]))
            self.tables[full] = (full, columns)

    def table(self, schema_tok, table_tok, line: int) -> tuple[str, tuple[str, ...]]:
        (s, sq), (t, tq) = _ident(schema_tok), _ident(table_tok)
        entry = self.tables.get(f"{s}.{t}")
        if entry is None:
            raise ParseBackError(f"table {s}.{t} is not in the universe schema"
                                 + _case_hint(f"{s}.{t}", sq or tq, self.tables), line)
        return entry

    def column(self, table: str, columns: tuple[str, ...], token, line: int) -> str:
        name, quoted = _ident(token)
        if name not in columns:
            raise ParseBackError(f"{table}: column {name!r} is not in the universe schema"
                                 + _case_hint(name, quoted, columns), line)
        return name


def _schema(path: Path | str) -> _Schema:
    """The schema, cached by file content: the bytes are read once, hashed and parsed (a changed file is read again)."""
    resolved = Path(path).resolve()
    try:
        raw = resolved.read_bytes()
    except OSError as error:
        raise ParseBackError(f"cannot read schema {resolved}: {error}") from None
    key = f"{resolved}|{hashlib.sha256(raw).hexdigest()}"
    loaded = _SCHEMAS.get(key)
    if loaded is None:
        loaded = _SCHEMAS[key] = _Schema(resolved, raw)
    return loaded


# ---------------------------------------------------------------- literal values

def _number_from_text(text: str, line: int):
    try:
        if "." in text or "e" in text.lower():
            return Decimal(text)
        return int(text)
    except (InvalidOperation, ValueError):
        raise ParseBackError(f"cannot read number literal {text!r}", line) from None


def _literal_text(token, line: int) -> str:
    """The literal text of a string token, without trusting the eval's dollar/binary forms."""
    if token.kind != "string":
        raise ParseBackError(f"value is not a literal: {token.text!r}", line)
    head = token.text[:2].lower()
    if token.text.startswith("'") or head == "e'":
        return token.text
    raise ParseBackError(f"only standard and E'' string literals are allowed, found {token.text!r}", line)


def _value(tokens, text: str, parser: EvalParser, line: int):
    """Typed Python value for one value token group; raises on anything that is not a plain literal."""
    if not tokens:
        raise ParseBackError("empty value in a value list", line)
    if len(tokens) == 1:
        token = tokens[0]
        if token.kind == "string":
            _literal_text(token, line)
            return token.value
        if token.kind == "number":
            return _number_from_text(token.text, line)
        if token.kind == "word" and token.value == "null":
            return None
        if token.kind == "word" and token.value in ("true", "false"):
            return token.value == "true"
        raise ParseBackError(f"value is not a literal (NULL, true, false, a number or a quoted string): "
                             f"{token.text!r}", line)
    if len(tokens) == 2 and tokens[0].op("-") and tokens[1].kind == "number":
        return _number_from_text("-" + tokens[1].text, line)
    shown = " ".join(t.text for t in tokens)[:80]
    raise ParseBackError(f"value is not a plain literal (expressions, casts and functions are not "
                         f"allowed): {shown!r}", line)


# ---------------------------------------------------------------- token helpers

def _qualified(toks, i: int) -> tuple[list, int]:
    """The name tokens of a qualified name and the index after it, as the eval parser walks it."""
    parts: list = []
    while i < len(toks) and toks[i].kind in ("word", "qident"):
        parts.append(toks[i])
        if i + 1 < len(toks) and toks[i + 1].op("."):
            i += 2
        else:
            i += 1
            break
    return parts, i


def _find_word(toks, words: set[str], start: int = 0) -> int:
    """First depth-0 index of any of words, or len(toks)."""
    depth = 0
    for j in range(start, len(toks)):
        token = toks[j]
        if token.op("(", "["):
            depth += 1
        elif token.op(")", "]"):
            depth -= 1
        elif depth == 0 and token.kind == "word" and token.value in words:
            return j
    return len(toks)


def _identifier(tokens, what: str, line: int):
    if len(tokens) != 1 or tokens[0].kind not in ("word", "qident"):
        shown = " ".join(t.text for t in tokens)[:60]
        raise ParseBackError(f"{what} is not a plain column name: {shown!r}", line)
    return tokens[0]


def _pairs(tokens, text: str, parser: EvalParser, line: int, what: str) -> list[tuple[object, object]]:
    """Parse `col = literal` groups (comma separated for SET, AND separated for WHERE): (name token, value)."""
    out: list[tuple[object, object]] = []
    for group in tokens:
        if not group:
            raise ParseBackError(f"empty {what} assignment", line)
        if len(group) < 3 or not group[1].op("="):
            shown = " ".join(t.text for t in group)[:80]
            raise ParseBackError(f"{what} must be `column = literal`, found {shown!r}", line)
        name = _identifier([group[0]], what, line)
        out.append((name, _value(group[2:], text, parser, line)))
    return out


def _split_at(toks, word: str) -> list[list]:
    parts: list[list] = [[]]
    depth = 0
    for token in toks:
        if token.op("(", "["):
            depth += 1
        elif token.op(")", "]"):
            depth -= 1
        if depth == 0 and token.kind == "word" and token.value == word:
            parts.append([])
        else:
            parts[-1].append(token)
    return parts


# ---------------------------------------------------------------- statements

def _statement(text: str, toks, parser: EvalParser, schema: _Schema) -> Op | None:
    line = parser.line_of(text, toks[0].start)
    head = toks[0]
    if head.kind == "word" and head.value in ("begin", "commit"):
        if len(toks) != 1:
            raise ParseBackError(f"{head.text.upper()}; must stand alone", line)
        return None
    if head.kind != "word":
        raise ParseBackError(f"statement must start with INSERT or UPDATE, found {head.text!r}", line)
    if head.value == "insert":
        return _insert(text, toks, parser, schema, line)
    if head.value == "update":
        return _update(text, toks, parser, schema, line)
    raise ParseBackError(f"statement is not INSERT/UPDATE/BEGIN/COMMIT: {head.text!r}", line)


def _insert(text: str, toks, parser: EvalParser, schema: _Schema, line: int) -> Op:
    if len(toks) < 2 or not toks[1].word("into"):
        raise ParseBackError("INSERT without INTO", line)
    parts, i = _qualified(toks, 2)
    if len(parts) != 2:
        shown = ".".join(t.text for t in parts) or "?"
        raise ParseBackError(f"table must be schema-qualified as schema.table, found {shown!r}", line)
    table, schema_columns = schema.table(parts[0], parts[1], line)
    if i >= len(toks) or not toks[i].op("("):
        raise ParseBackError("INSERT without a column list", line)
    close = parser.matching(toks, i)
    column_groups = parser.split_commas(toks[i + 1:close])
    columns = [schema.column(table, schema_columns, _identifier(g, "column", line), line)
               for g in column_groups]
    i = close + 1
    if i >= len(toks) or not toks[i].word("values"):
        raise ParseBackError("INSERT without a VALUES source", line)
    i += 1
    if i >= len(toks) or not toks[i].op("("):
        raise ParseBackError("INSERT ... VALUES without a parenthesized value list", line)
    close = parser.matching(toks, i)
    value_groups = parser.split_commas(toks[i + 1:close])
    values = [_value(group, text, parser, line) for group in value_groups]
    i = close + 1
    if i != len(toks):
        shown = " ".join(t.text for t in toks[i:i + 8])[:80]
        raise ParseBackError(f"unexpected tokens after the INSERT value list: {shown!r}", line)
    if len(columns) != len(values):
        raise ParseBackError(f"column count {len(columns)} does not match value count {len(values)} "
                             f"(the eval parser zips these silently)", line)
    try:
        return Op(table=table, op=INSERT, cols=tuple(zip(columns, values)))
    except (TypeError, ValueError) as error:
        raise ParseBackError(f"{table}: {error}", line) from None


def _update(text: str, toks, parser: EvalParser, schema: _Schema, line: int) -> Op:
    parts, i = _qualified(toks, 1)
    if len(parts) != 2:
        shown = ".".join(t.text for t in parts) or "?"
        raise ParseBackError(f"table must be schema-qualified as schema.table, found {shown!r}", line)
    table, schema_columns = schema.table(parts[0], parts[1], line)
    if i >= len(toks) or not toks[i].word("set"):
        raise ParseBackError("UPDATE without SET", line)
    where_at = _find_word(toks, {"where"}, i + 1)
    if where_at == len(toks):
        raise ParseBackError("UPDATE without WHERE", line)
    set_groups = parser.split_commas(toks[i + 1:where_at])
    assignments = _pairs(set_groups, text, parser, line, "SET")
    if not assignments:
        raise ParseBackError("UPDATE with an empty SET", line)
    where_groups = _split_at(toks[where_at + 1:], "and")
    conditions = _pairs(where_groups, text, parser, line, "WHERE")
    if not conditions:
        raise ParseBackError("UPDATE with an empty WHERE", line)
    columns = [schema.column(table, schema_columns, name, line) for name, _ in assignments]
    keys = [schema.column(table, schema_columns, name, line) for name, _ in conditions]
    try:
        return Op(table=table, op=UPDATE,
                  cols=tuple(zip(columns, [v for _, v in assignments])),
                  where=tuple(zip(keys, [v for _, v in conditions])))
    except (TypeError, ValueError) as error:
        raise ParseBackError(f"{table}: {error}", line) from None


def parse_ops(text: str, *, schema_path) -> list[Op]:
    """Parse the whole injection script into ops; fail closed with ParseBackError on anything unexpected."""
    if not isinstance(text, str):
        raise TypeError(f"parse_ops expects str, not {type(text).__name__}")
    parser = load_eval_parser()
    schema = _schema(schema_path)

    try:
        toks, _comments = parser.tokenize(text)
    except ValueError as error:
        raise ParseBackError(f"the eval tokenizer could not read the text: {error}") from None
    statements = parser.statements(toks)

    # The eval's own statement parser must not have found anything it could not evaluate.
    evaluator = parser.Parser(parser.table_index)
    for tokens in statements:
        evaluator.statement(tokens)
    if evaluator.unparsed:
        note = evaluator.unparsed[0]
        line = parser.line_of(text, int(note.get("start") or 0))
        raise ParseBackError(f"the eval parser could not evaluate a statement: {note.get('reason')}", line)

    ops: list[Op] = []
    for tokens in statements:
        line = parser.line_of(text, tokens[0].start)
        try:
            op = _statement(text, tokens, parser, schema)
        except ParseBackError:
            raise
        except (ValueError, IndexError, KeyError) as error:
            raise ParseBackError(f"cannot parse the statement: {error}", line) from None
        if op is not None:
            ops.append(op)
    return ops
