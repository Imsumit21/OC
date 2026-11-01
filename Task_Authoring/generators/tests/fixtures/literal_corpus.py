"""Deterministic corpus of literal values for the validator tests.

cases(seed, n) returns exactly n Python values of the types core/ops.Op allows (None, bool, int,
decimal.Decimal, str). It deliberately covers the shapes that break naive emitters/parsers: quotes and
doubled quotes, backslashes (including a trailing backslash and the two-character sequence \\n), CR, LF,
CRLF, TAB, unicode (accents, CJK, emoji, em dash), JSON text with escaped quotes and nested arrays, the
empty string, NULL/booleans, ints and exact decimals, and SQL-looking text.

Only characters core/sqlvalue.literal accepts appear here: TAB, LF and CR are the only control characters.
"""
from __future__ import annotations

import json
import random
from decimal import Decimal

JSON_NESTED = json.dumps(
    {"a": 'quote " here', "b": [1, [2, 3], {"c": "nested"}], "d": "café — 🎮", "e": "back\\slash"},
    ensure_ascii=False,
)

FIXED = [
    # strings: quotes and doubling
    "",
    "plain",
    "O'Brien",
    "it''s",
    "''",
    "'",
    "two '' quotes and 'one'",
    "'); DROP TABLE contacts.contacts; --",
    # backslashes
    "back\\slash",
    "trailing\\",
    "\\",
    "\\\\",
    "line\\nbreak",                     # a backslash and an 'n', not a newline
    "\\n\\r\\t literal",
    "C:\\Users\\harmony\\games\\",
    # real control characters
    "\n",
    "\r",
    "\r\n",
    "\t",
    "a\tb",
    "line one\nline two",
    "cr\rhere",
    "crlf\r\nhere",
    "ends with a newline\n",
    "slash then newline \\\n",
    "\n\t\r\\ mixed \\\r\n",
    # unicode
    "café",
    "naïve résumé",
    "日本語のテキスト",
    "🎮 gamepad",
    "em — dash",
    "mixed café 日本 🎮 — ok",
    # JSON text as a column value
    JSON_NESTED,
    '{"k": "v"}',
    '[]',
    '{"n": null, "b": true, "f": 1.5}',
    # SQL-looking text
    "semi;colon",
    "-- looks like a comment",
    "/* block comment */",
    "$$ dollar body $$",
    "$tag$ tagged $tag$",
    "E'x'",
    "now()",
    "1::text",
    "' OR '1'='1",
    "\"quoted identifier\"",
    # non-strings
    None,
    True,
    False,
    0,
    -1,
    42,
    -9223372036854775808,
    9223372036854775807,
    123456789012345678901234567890,
    Decimal("-1.50"),
    Decimal("0.10"),
    Decimal("1277953.9648391008"),
    Decimal("0"),
    Decimal("-0.0001"),
    Decimal("1000000.000001"),
]

PIECES = [
    "", "a", "Z", "0", " ", "  ", "'", "''", "\\", "\\\\", "\n", "\r", "\t", "\r\n",
    ", ", ";", "--", "/*", "*/", "$$", "::", "(", ")", "NULL", "true", "E'", "O'Brien",
    "café", "日本", "🎮", "—", "\"", "{", "}", "[", "]", ":", "_", "-", "%", "\\n",
]


def cases(seed: int = 20261101, n: int = 240):
    """Deterministic list of n values; the fixed edge cases come first."""
    if n < 0:
        raise ValueError("n must be >= 0")
    out = list(FIXED)
    rng = random.Random(seed)
    seen = {repr(v) for v in out}
    attempts = 0
    while len(out) < n and attempts < n * 50:
        attempts += 1
        roll = rng.random()
        if roll < 0.70:
            value = "".join(rng.choice(PIECES) for _ in range(rng.randint(1, 4)))
        elif roll < 0.82:
            value = rng.randint(-10 ** 15, 10 ** 15)
        elif roll < 0.90:
            value = Decimal(f"{rng.randint(-2, 2)}.{rng.randint(0, 999999):06d}")
        elif roll < 0.95:
            value = rng.choice((None, True, False))
        else:
            value = json.dumps({"i": rng.randint(-50, 50), "s": rng.choice(PIECES),
                                "q": 'a "quoted" value'}, ensure_ascii=False)
        if repr(value) in seen:
            continue
        seen.add(repr(value))
        out.append(value)
    while len(out) < n:                                # pragma: no cover - only for tiny/awkward seeds
        out.append("filler %d" % len(out))
    return out[:n]
