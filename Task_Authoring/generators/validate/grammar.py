"""Restricted-grammar checker for the generators' injection SQL (pure text, no tokenizer).

This module is one of the *independent* validators: it never imports the emitter (core/sqlvalue), the
eval tokenizer (Evals/tools/hg_injection_lint.py) or Task_Authoring/tools/sql_lint.py. It reads the SQL as
characters and accepts exactly this shape:

    line 1                    -- Are you planning to inject? Yes      (when require_marker)
    blank lines
    comment lines             starting with "-- "
    BEGIN; / COMMIT;
    statements, one per line, exactly one of

    INSERT INTO <ident>.<ident> (<ident>, <ident>, ...) VALUES (<lit>, <lit>, ...);
    UPDATE <ident>.<ident> SET <ident> = <lit>[, <ident> = <lit>]* WHERE <ident> = <lit>[ AND <ident> = <lit>]*;

<ident> is [a-z_][a-z0-9_]* or a quoted name ("dateLastActivity", and the literal "<name>" form is also
accepted). <lit> is NULL, true, false, -?digits[.digits], a standard '...' string ('' doubling; a backslash
is an ordinary character) or an E'...' string whose backslash escapes are limited to \\ \\n \\r \\t ('' doubling
also allowed). Separators are exactly ", " and single spaces. Column count must equal value count and a
column may not repeat.

check_sql returns a list of GrammarError, one per offending line; an empty list means the text is in the
grammar. split_literals is a small helper for tests that returns the raw literal texts of a VALUES list.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

MARKER = "-- Are you planning to inject? Yes"

# [0-9] not \d: the grammar is ASCII, and Python's \d also matches non-ASCII digits.
_PLAIN_IDENT = re.compile(r"[a-z_][a-z0-9_]*")
_QUOTED_IDENT = re.compile(r'"[A-Za-z_][A-Za-z0-9_]*"')
_NUMBER = re.compile(r"-?[0-9]+(?:\.[0-9]+)?")
_WORDS = ("NULL", "true", "false")


@dataclass(frozen=True)
class GrammarError(Exception):
    """One line that breaks the grammar; also raised by split_literals on a malformed value list."""
    line: int
    message: str

    def __str__(self) -> str:      # pragma: no cover - convenience only
        return f"line {self.line}: {self.message}"


class _Syntax(Exception):
    """Internal: a line does not match the grammar."""


class _Scanner:
    __slots__ = ("s", "i", "line")

    def __init__(self, text: str, line: int = 1):
        self.s, self.i, self.line = text, 0, line

    # -- position helpers -------------------------------------------------
    def fail(self, message: str) -> None:
        raise _Syntax(f"column {self.i + 1}: {message}")

    def at_end(self) -> bool:
        return self.i >= len(self.s)

    def peek(self, text: str) -> bool:
        return self.s.startswith(text, self.i)

    def rest(self) -> str:
        return self.s[self.i:]

    def found(self, width: int = 18) -> str:
        chunk = self.s[self.i:self.i + width]
        return repr(chunk) if chunk else "end of line"

    def guard(self) -> None:
        probe = self.s[self.i:].lstrip(" \t")
        if probe.startswith("--") or probe.startswith("/*"):
            self.fail("a comment is not allowed inside a statement")

    def expect(self, text: str, what: str | None = None) -> None:
        self.guard()
        if not self.peek(text):
            self.fail(f"expected {what or repr(text)}, found {self.found()}")
        self.i += len(text)

    # -- tokens -----------------------------------------------------------
    def ident(self) -> str:
        self.guard()
        m = _QUOTED_IDENT.match(self.s, self.i)
        if m:
            self.i = m.end()
            return m.group(0)
        m = _PLAIN_IDENT.match(self.s, self.i)
        if m:
            self.i = m.end()
            return m.group(0)
        self.fail("expected an identifier ([a-z_][a-z0-9_]* or a quoted name), "
                  f"found {self.found()}")

    def literal(self) -> str:
        self.guard()
        c = self.s[self.i:self.i + 1]
        if not c:
            self.fail("expected a literal, found end of line")
        if c == "'":
            return self._string(escape=False)
        if c in "Ee" and self.s[self.i + 1:self.i + 2] == "'":
            return self._string(escape=True)
        if c in "-0123456789":
            m = _NUMBER.match(self.s, self.i)
            if m:
                self.i = m.end()
                nxt = self.s[self.i:self.i + 1]
                if nxt.isalnum() or nxt in (".", "_"):
                    self.fail(f"malformed number {m.group(0)!r}; exponents and trailing dots are not allowed")
                return m.group(0)
            self.fail(f"malformed number near {self.found()}")
        for word in _WORDS:
            if self.peek(word):
                end = self.i + len(word)
                nxt = self.s[end:end + 1]
                if not (nxt.isalnum() or nxt == "_"):
                    self.i = end
                    return word
        self.fail("expected a literal (NULL, true, false, a number or a quoted string); casts, "
                  f"functions and comments are not allowed inside a statement, found {self.found()}")

    def _string(self, escape: bool) -> str:
        start = self.i
        self.i += 2 if escape else 1
        while True:
            if self.i >= len(self.s):
                self.fail("unterminated string literal")
            ch = self.s[self.i]
            if escape and ch == "\\":
                nxt = self.s[self.i + 1:self.i + 2]
                if not nxt:
                    self.fail("unterminated E'' string (a trailing backslash)")
                if nxt not in ("\\", "n", "r", "t"):
                    self.fail(f"E'' string: unsupported backslash escape \\{nxt}; "
                              "only \\\\ \\n \\r \\t are allowed")
                self.i += 2
                continue
            if ch == "'":
                if self.s[self.i + 1:self.i + 2] == "'":
                    self.i += 2
                    continue
                self.i += 1
                return self.s[start:self.i]
            self.i += 1


def _end_of_line(sc: _Scanner) -> None:
    if sc.at_end():
        return
    rest = sc.rest()
    if ";" in rest or rest.startswith(("INSERT ", "UPDATE ", "BEGIN;", "COMMIT;")):
        sc.fail(f"unexpected text after the statement, found {rest!r} "
                "(one statement per line, one ';' at the end)")
    sc.fail(f"unexpected text after the statement, found {rest!r}")


def _name_list(sc: _Scanner, what: str) -> list[str]:
    names = [sc.ident()]
    while True:
        sc.guard()
        if sc.peek(", "):
            sc.i += 2
            names.append(sc.ident())
        elif sc.peek(")"):
            sc.i += 1
            return names
        else:
            sc.fail(f"expected ', ' or ')' after {what}, found {sc.found()}")


def _literal_list(sc: _Scanner) -> list[str]:
    values = [sc.literal()]
    while True:
        sc.guard()
        if sc.peek(", "):
            sc.i += 2
            values.append(sc.literal())
        elif sc.peek(")"):
            sc.i += 1
            return values
        else:
            hint = " (casts are not allowed)" if sc.peek("::") else ""
            sc.fail(f"expected ', ' or ')' after a value, found {sc.found()}{hint}")


def _no_duplicates(sc: _Scanner, names: list[str], what: str) -> None:
    seen: set[str] = set()
    for name in names:
        key = name.strip('"').strip("<>").lower()
        if key in seen:
            sc.fail(f"duplicate {what} {name}")
        seen.add(key)


def _assign(sc: _Scanner) -> tuple[str, str]:
    name = sc.ident()
    sc.expect(" = ")
    return name, sc.literal()


def _insert_line(sc: _Scanner) -> None:
    sc.expect("INSERT INTO ")
    sc.ident()
    sc.expect(".")
    sc.ident()
    sc.expect(" (")
    columns = _name_list(sc, "column")
    sc.expect(" VALUES (")
    values = _literal_list(sc)
    sc.expect(";", "';' at the end of the statement")
    _end_of_line(sc)
    _no_duplicates(sc, columns, "column")
    if len(columns) != len(values):
        raise _Syntax(f"column count {len(columns)} does not match value count {len(values)}")


def _update_line(sc: _Scanner) -> None:
    sc.expect("UPDATE ")
    sc.ident()
    sc.expect(".")
    sc.ident()
    sc.expect(" SET ")
    assignments = [_assign(sc)]
    while True:
        sc.guard()
        if sc.peek(", "):
            sc.i += 2
            assignments.append(_assign(sc))
        elif sc.peek(" WHERE "):
            sc.i += len(" WHERE ")
            break
        elif sc.peek(";"):
            sc.fail("UPDATE requires a WHERE clause")
        else:
            sc.fail(f"expected ', ' or ' WHERE ' after an assignment, found {sc.found()}")
    conditions = [_assign(sc)]
    while True:
        sc.guard()
        if sc.peek(" AND "):
            sc.i += len(" AND ")
            conditions.append(_assign(sc))
        elif sc.peek(";"):
            sc.i += 1
            break
        else:
            sc.fail(f"expected ' AND ' or ';' after the WHERE condition, found {sc.found()}")
    _end_of_line(sc)
    _no_duplicates(sc, [c for c, _ in assignments], "SET column")
    _no_duplicates(sc, [c for c, _ in conditions], "WHERE column")


def _check_line(line: str, number: int) -> GrammarError | None:
    sc = _Scanner(line, number)
    try:
        if line.startswith("INSERT "):
            _insert_line(sc)
        elif line.startswith("UPDATE "):
            _update_line(sc)
        elif line.startswith(("insert ", "update ", "Insert ", "Update ")):
            raise _Syntax("SQL keywords must be upper case: INSERT / UPDATE / SET / WHERE / VALUES / INTO")
        else:
            raise _Syntax("not an INSERT or UPDATE statement in the restricted grammar "
                          "(one statement per line, exact form)")
    except _Syntax as error:
        return GrammarError(number, str(error))
    return None


def check_sql(text: str, *, require_marker: bool = True) -> list[GrammarError]:
    """Return every line that breaks the restricted grammar (empty list: clean)."""
    if not isinstance(text, str):
        raise TypeError(f"check_sql expects str, not {type(text).__name__}")
    errors: list[GrammarError] = []
    lines = text.split("\n")
    start = 0
    if require_marker:
        start = 1
        if lines[0] != MARKER:
            shown = lines[0] if lines[0] else "(empty line)"
            errors.append(GrammarError(1, f"line 1 must be exactly {MARKER!r}, found {shown!r}"))
    for offset in range(start, len(lines)):
        line, number = lines[offset], offset + 1
        if line == "":
            continue
        if line.endswith("\r"):
            errors.append(GrammarError(number, "line ends with a carriage return; write LF line endings"))
            continue
        if line.startswith("-- "):
            continue
        if line in ("BEGIN;", "COMMIT;"):
            continue
        if line.startswith("--"):
            errors.append(GrammarError(number, "a comment line must start with '-- ' (dash dash space)"))
            continue
        error = _check_line(line, number)
        if error is not None:
            errors.append(error)
    return errors


def split_literals(values_text: str) -> list[str]:
    """Raw literal texts of a VALUES list: "(1, 'a', E'x\\n')", "VALUES (...)" or "1, 'a', NULL"."""
    if not isinstance(values_text, str):
        raise TypeError(f"split_literals expects str, not {type(values_text).__name__}")
    source = values_text.strip()
    if source[:7].upper() == "VALUES ":
        source = source[7:].lstrip()
    sc = _Scanner(source, 1)
    try:
        wrapped = sc.peek("(")
        if wrapped:
            sc.i += 1
        out = [sc.literal()]
        while True:
            sc.guard()
            if sc.peek(", "):
                sc.i += 2
                out.append(sc.literal())
            elif wrapped and sc.peek(")"):
                sc.i += 1
                if sc.peek(";"):
                    sc.i += 1
                break
            elif not wrapped and sc.at_end():
                break
            else:
                sc.fail(f"expected ', ' or ')' after a value, found {sc.found()}")
        if not sc.at_end():
            sc.fail(f"unexpected text after the value list, found {sc.found(24)}")
        return out
    except _Syntax as error:
        raise GrammarError(sc.line, str(error)) from None
