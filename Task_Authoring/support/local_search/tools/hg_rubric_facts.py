"""Evidence-bound rubric facts, with a deliberately finite calculation language.

``validate_facts(review, criterion, reader, known)`` never accepts a separately
declared expected number or PASS: the expected value comes from an exact title
quote. Selection pointers are relative to the *entire quoted anchor selection*,
not the containing source file. Semantic judgments are labeled as judgments.
Missing evidence/coverage is unresolved; a demonstrated contradiction is a
mismatch. The caller decides QC classification and publication readiness.
"""

from datetime import date, datetime, timezone
from decimal import Decimal, InvalidOperation, localcontext, ROUND_HALF_UP, ROUND_HALF_EVEN, ROUND_DOWN
import json
import re
from zoneinfo import ZoneInfo


KINDS = {"NUMBER", "RANGE", "DATE", "LITERAL", "SEMANTIC", "UNRESOLVED", "NOT_A_CLAIM"}
OPERATIONS = {"direct", "count", "distinct_count", "sum", "min", "max", "difference", "ratio"}
ROUNDING = {"HALF_UP": ROUND_HALF_UP, "HALF_EVEN": ROUND_HALF_EVEN, "DOWN": ROUND_DOWN}
# This is an allowlist, not a user-supplied arithmetic expression or scale.
UNITS = {"B": ("bytes", Decimal(1)), "KB": ("bytes", Decimal(1000)),
         "MB": ("bytes", Decimal(1000000)), "GB": ("bytes", Decimal(1000000000)),
         "KiB": ("bytes", Decimal(1024)), "MiB": ("bytes", Decimal(1048576)),
         "GiB": ("bytes", Decimal(1073741824)), "ms": ("time", Decimal("0.001")),
         "s": ("time", Decimal(1)), "min": ("time", Decimal(60)),
         "h": ("time", Decimal(3600)), "days": ("time", Decimal(86400)),
         "%": ("ratio", Decimal("0.01")), "ratio": ("ratio", Decimal(1))}
UNIT_ALIASES = {**{unit: unit for unit in UNITS}, "byte": "B", "bytes": "B",
                "millisecond": "ms", "milliseconds": "ms", "second": "s", "seconds": "s",
                "minute": "min", "minutes": "min", "hour": "h", "hours": "h", "day": "days", "percent": "%",
                "$": "USD", "USD": "USD", "€": "EUR", "EUR": "EUR", "£": "GBP", "GBP": "GBP"}
_UNIT_PATTERN = "(?:" + "|".join(re.escape(unit) for unit in sorted(UNIT_ALIASES, key=len, reverse=True)) + ")"
UNIT_SUFFIX = re.compile(r"\s*(?P<unit>" + _UNIT_PATTERN + r")(?![\w])")
CURRENCY_PREFIX = re.compile(r"(?P<unit>[$€£]|USD|EUR|GBP)\s*$")
NUMBER = re.compile(r"(?P<prefix>[$€£])?(?P<number>[+-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?(?:[eE][+-]?\d+)?)"
                    r"(?:\s*(?P<unit>%|[A-Za-z][A-Za-z ]{0,31}))?\Z")
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}\Z")
ISO_INSTANT = re.compile(r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}(?::\d{2}(?:\.\d{1,6})?)?(?:Z|[+-]\d{2}:\d{2})\Z")
DIGIT_TOKEN = re.compile(r"\d+(?:[,.]\d+)*(?:[eE][+-]?\d+)?", re.UNICODE)
DATE_TOKEN = re.compile(r"(?<!\d)\d{4}-\d{2}-\d{2}(?:T\d{2}:\d{2}(?::\d{2}(?:\.\d+)?)?(?:Z|[+-]\d{2}:\d{2})?)?(?!\d)")
SMALL_CARDINALS = {word: value for value, word in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS_CARDINALS = dict(zip("twenty thirty forty fifty sixty seventy eighty ninety".split(), range(20, 100, 10)))
CARDINAL_SCALES = {"hundred": 100, "thousand": 1000, "million": 1000000}
CARDINAL_WORDS = set(SMALL_CARDINALS) | set(TENS_CARDINALS) | set(CARDINAL_SCALES)
UNSUPPORTED_QUANTITIES = {"billion", "billions", "trillion", "trillions", "quadrillion", "quadrillions",
                          "hundreds", "thousands", "millions", "dozen", "dozens", "half", "halves",
                          "quarter", "quarters"}
_CARDINAL_PATTERN = "(?:" + "|".join(sorted(CARDINAL_WORDS | UNSUPPORTED_QUANTITIES, key=len, reverse=True)) + ")"
_CARDINAL_START = "(?:" + "|".join(sorted(CARDINAL_WORDS | {"billion", "trillion", "quadrillion"}, key=len, reverse=True)) + ")"
SPELLED_TOKEN = re.compile(r"(?<![\w-])(?:(?:minus|negative)\s+)?" + _CARDINAL_START +
                           r"(?:(?:\s+|-)(?:and\s+|point\s+)?" + _CARDINAL_PATTERN + r")*(?![\w-])", re.I)
# Personas work on Pacific time; tools return UTC (ENVIRONMENT.md, Eval 3 §2.11).
PACIFIC = ZoneInfo("America/Los_Angeles")
DATE_COMPARISONS = {"exact", "utc_date", "pt_or_utc_date"}
_MONTHS = {name: number for number, names in enumerate((
    ("january", "jan"), ("february", "feb"), ("march", "mar"), ("april", "apr"), ("may",),
    ("june", "jun"), ("july", "jul"), ("august", "aug"), ("september", "sep", "sept"),
    ("october", "oct"), ("november", "nov"), ("december", "dec")), 1) for name in names}
_MONTH_PATTERN = "(?:" + "|".join(sorted(_MONTHS, key=len, reverse=True)) + r")\.?"
# A prose calendar date is unambiguous only with month name, day and four-digit year.
PROSE_DATE = re.compile(r"(?:(?P<month>" + _MONTH_PATTERN + r")\s+(?P<day>\d{1,2}),?\s+(?P<year>\d{4})"
                        r"|(?P<day2>\d{1,2})\s+(?P<month2>" + _MONTH_PATTERN + r"),?\s+(?P<year2>\d{4}))\Z", re.I)
# Exact keys bind as LITERAL, like numbers bind as NUMBER (Eval 3 §2.3): snake_case event or
# field keys and prefixed record IDs, ticket keys, Slack-style IDs and long hexadecimal IDs.
ID_TOKEN = re.compile(r"(?<![\w@.-])(?:[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+|[A-Z][A-Z0-9]{1,9}-\d+"
                      r"|(?=[A-Z0-9]*\d)[A-Z][A-Z0-9]{8,}"
                      r"|(?=[0-9a-f]*[a-f])(?=[0-9a-f]*\d)[0-9a-f]{12,})(?![\w-])")
# Anonymization placeholders are the source string (rubric_factual_checks.md).
ANON_TOKEN = re.compile(r"\[[A-Z]+(?:_[A-Z]+)*_\d+\]|<REDACTED(?:_[A-Z]+)*>")
REACHABLE = "PROMPT_LINKED"
REACHABILITY = {"PROMPT_LINKED", "TRASH", "ATTACHMENT_ONLY", "UNLINKED"}


def _require(condition, message):
    if not condition:
        raise ValueError("Rubric facts: " + message)


def _text(value, label):
    _require(isinstance(value, str) and bool(value.strip()), label + " must be nonempty text")
    return value


def _object(value, label, allowed=None, required=()):
    _require(isinstance(value, dict), label + " must be an object")
    _require(all(isinstance(key, str) for key in value), label + " keys must be strings")
    if allowed is not None:
        _require(set(value) <= set(allowed), label + " contains unsupported fields: " + str(sorted(set(value) - set(allowed))))
    _require(set(required) <= set(value), label + " is missing required fields")
    return value


def _decimal(value, label):
    _require(not isinstance(value, bool) and isinstance(value, (str, int, float, Decimal)), label + " must be numeric")
    _require(len(str(value)) <= 120, label + " is too large")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError) as error:
        raise ValueError("Rubric facts: " + label + " must be numeric") from error
    _require(result.is_finite(), label + " cannot be NaN or Infinity")
    _require(abs(result.adjusted()) <= 100, label + " exponent is out of bounds")
    return result


def _pointer(value, pointer):
    _require(isinstance(pointer, str) and (pointer == "" or pointer.startswith("/")), "selection pointer must be an RFC 6901 pointer")
    _require(len(pointer) <= 2048 and len(pointer.split("/")) <= 64, "selection pointer is too deep")
    for token in pointer.split("/")[1:] if pointer else []:
        _require(re.search(r"~(?![01])", token) is None, "selection pointer contains an invalid escape")
        token = token.replace("~1", "/").replace("~0", "~")
        if isinstance(value, list):
            _require(bool(re.fullmatch(r"0|[1-9]\d*", token)), "selection array index is invalid")
            index = int(token)
            _require(index < len(value), "selection pointer does not resolve")
            value = value[index]
        else:
            _require(isinstance(value, dict) and token in value, "selection pointer does not resolve")
            value = value[token]
    return value


def _anchor_value(reader, anchor):
    selected = reader.quote(anchor)
    _require(isinstance(selected, str), "evidence reader must return selected text")
    # A quote of one number inside an unrelated source does not authorize every
    # other field in that source. Exact selection avoids that scope expansion.
    _require(selected.strip() == anchor.get("quote", "").strip(),
             "executable facts must quote the entire selected anchor; narrow its pointer/line selection")
    try:
        return json.loads(selected, parse_float=Decimal, parse_int=Decimal,
                          parse_constant=lambda _: (_ for _ in ()).throw(ValueError("Non-finite source JSON")))
    except json.JSONDecodeError:
        return selected.strip()


def _same_json(left, right):
    # Avoid Python's True == 1 trap in equality filters.
    if isinstance(left, bool) or isinstance(right, bool):
        return type(left) is bool and type(right) is bool and left == right
    if isinstance(left, (Decimal, int, float)) and isinstance(right, (Decimal, int, float)):
        return _decimal(left, "filter source") == _decimal(right, "filter value")
    return type(left) is type(right) and left == right


def _select(selection, reader, known, permitted, *, records=False):
    _object(selection, "selection", {"source_id", "pointer", "filters", "field"}, {"source_id", "pointer"})
    sid = selection["source_id"]
    _require(isinstance(sid, str) and sid in permitted, "selection source must occur in claim.source_ids")
    value = _pointer(_anchor_value(reader, known[sid]), selection["pointer"])
    if "filters" in selection:
        _require(records and isinstance(value, list), "filters require an aggregate over a selected record array")
        filters = selection["filters"]
        _require(isinstance(filters, list) and 0 < len(filters) <= 20, "filters must be a nonempty equality-filter array")
        for rule in filters:
            _object(rule, "filter", {"pointer", "equals"}, {"pointer", "equals"})
            _require(not isinstance(rule["equals"], (list, dict)) and rule["equals"] is not None,
                     "filter equality value must be a non-null scalar")
            _require(isinstance(rule["equals"], (str, int, float, Decimal, bool)),
                     "filter equality value must be a JSON scalar")
            if isinstance(rule["equals"], (int, float, Decimal)) and not isinstance(rule["equals"], bool):
                _decimal(rule["equals"], "filter equality value")
            value = [item for item in value if _same_json(_pointer(item, rule["pointer"]), rule["equals"])]
    if "field" in selection:
        _require(records and isinstance(value, list), "field projection requires an aggregate over an array")
        value = [_pointer(item, selection["field"]) for item in value]
    return value


def _cardinal_group(words):
    """Parse a standard cardinal group below one thousand, without guessing."""
    _require(bool(words), "spelled quantity has an empty cardinal group")
    if "hundred" in words:
        _require(words.count("hundred") == 1 and words.index("hundred") in {0, 1},
                 "spelled quantity has a malformed hundred group")
        index = words.index("hundred")
        multiple = SMALL_CARDINALS.get(words[0], -1) if index else 1
        _require(1 <= multiple <= 9, "hundred needs a one-to-nine multiplier")
        tail = words[index + 1:]
        return multiple * 100 + (_cardinal_group(tail) if tail else 0)
    if len(words) == 1 and words[0] in SMALL_CARDINALS:
        return SMALL_CARDINALS[words[0]]
    if words[0] in TENS_CARDINALS:
        if len(words) == 1:
            return TENS_CARDINALS[words[0]]
        if len(words) == 2 and 1 <= SMALL_CARDINALS.get(words[1], -1) <= 9:
            return TENS_CARDINALS[words[0]] + SMALL_CARDINALS[words[1]]
    raise ValueError("Rubric facts: malformed or unsupported spelled quantity")


def _cardinal_value(words):
    # 'and' is a cardinal connector only following a scale. This deliberately
    # does not turn 'one and two' into an invented single quantity.
    for index, word in enumerate(words):
        if word == "and":
            _require(0 < index < len(words) - 1 and words[index - 1] in CARDINAL_SCALES,
                     "spelled quantity uses an unsupported connector")
    words = [word for word in words if word != "and"]
    total, current, previous_scale = 0, [], 1000000000
    for word in words:
        if word in {"thousand", "million"}:
            scale = CARDINAL_SCALES[word]
            _require(scale < previous_scale, "spelled quantity scales must be distinct and descending")
            _require(bool(current) or len(words) == 1, "spelled quantity needs a multiplier before each scale")
            group = _cardinal_group(current) if current else 1
            _require(0 < group < 1000, "spelled quantity scale needs a positive group below one thousand")
            total += group * scale
            previous_scale, current = scale, []
        else:
            current.append(word)
    return total + (_cardinal_group(current) if current else 0)


def _number_claim(quote):
    match = NUMBER.fullmatch(quote.strip())
    if match is not None:
        raw = match.group("number").replace(",", "")
        number = _decimal(raw, "NUMBER quote")
        return number, match.group("unit") or match.group("prefix"), max(0, -number.as_tuple().exponent)
    spelling = quote.strip()
    prefix = spelling[0] if spelling and spelling[0] in "$€£" else None
    if prefix:
        spelling = spelling[1:].lstrip()
    tokens = list(re.finditer(r"[A-Za-z]+", spelling))
    words, cursor = [], 0
    for token in tokens:
        word = token.group().casefold()
        if word not in CARDINAL_WORDS | {"and"}:
            break
        _require(bool(re.fullmatch(r"[\s-]*", spelling[cursor:token.start()])), "spelled quantity has unsupported punctuation")
        words.append(word)
        cursor = token.end()
    _require(bool(words), "NUMBER quote must contain one numeric literal or supported English cardinal")
    unit = spelling[cursor:].strip() or prefix
    _require(unit is None or bool(re.fullmatch(r"%|[A-Za-z][A-Za-z ]{0,31}|[$€£]", unit)),
             "spelled quantity has unsupported trailing text")
    _require(not unit or not ({part.casefold() for part in unit.split()} &
                             (CARDINAL_WORDS | UNSUPPORTED_QUANTITIES | {"point", "minus", "negative"})),
             "unsupported spelled quantity cannot be relabeled as a unit")
    number = Decimal(_cardinal_value(words))
    return number, unit, 0


def _quantity_context(title, start, end):
    """Read a unit from the actual title, including outside a supplied quote."""
    before, after = CURRENCY_PREFIX.search(title[:start]), UNIT_SUFFIX.match(title[end:])
    units = [UNIT_ALIASES[m.group("unit")] for m in (before, after) if m is not None]
    _require(len(set(units)) <= 1, "title quantity has conflicting adjacent units")
    final_end = end + after.end() if after else end
    unit = units[0] if units else None
    # Compound rates/powers are outside this finite unit algebra. Preserve the
    # complete token so a partial MB quote cannot silently certify MB/s.
    if after:
        compound = re.match(r"(?:\s*/\s*[A-Za-z%]+|\s+per\s+[A-Za-z%]+|\^\d+|[²³])", title[final_end:])
        if compound:
            unit += compound.group()
            final_end += compound.end()
    return unit, before.start("unit") if before else start, final_end


def _number_title_unit(title, quote, start):
    stripped = quote.strip()
    offset = start + len(quote) - len(quote.lstrip())
    number = NUMBER.fullmatch(stripped)
    if number:
        return _quantity_context(title, offset + number.start("number"), offset + number.end("number"))
    cardinal = SPELLED_TOKEN.search(stripped)
    _require(cardinal is not None, "spelled NUMBER quote must select one cardinal quantity")
    return _quantity_context(title, offset + cardinal.start(), offset + cardinal.end())


def _number(claim, reader, known, title, start):
    expected, unit, places = _number_claim(claim["quote"])
    title_unit, quantity_start, quantity_end = _number_title_unit(title, claim["quote"], start)
    calc = _object(claim.get("calculation"), "calculation",
                   {"op", "operands", "source_unit", "conversion", "rounding", "allow_empty", "empty_reason"}, {"op", "operands"})
    op = calc["op"]
    _require(isinstance(op, str) and op in OPERATIONS, "calculation operation is unsupported")
    operands = calc["operands"]
    _require(isinstance(operands, list) and len(operands) == (2 if op in {"difference", "ratio"} else 1),
             "calculation has the wrong number of operands")
    referenced = {o.get("source_id") for o in operands if isinstance(o, dict) and isinstance(o.get("source_id"), str)}
    if "source_unit" in calc:
        unit_selection = _object(calc["source_unit"], "calculation.source_unit", {"source_id", "pointer"}, {"source_id", "pointer"})
        _require(isinstance(unit_selection["source_id"], str), "calculation source unit needs a source ID")
        referenced.add(unit_selection["source_id"])
    if "conversion" in calc:
        conv = _object(calc["conversion"], "conversion", {"from", "to", "source_unit"}, {"from", "to", "source_unit"})
        unit_selection = _object(conv["source_unit"], "conversion.source_unit", {"source_id", "pointer"}, {"source_id", "pointer"})
        _require(isinstance(unit_selection["source_id"], str), "conversion source unit needs a source ID")
        referenced.add(unit_selection["source_id"])
    _require(referenced == set(claim["source_ids"]), "NUMBER source_ids must exactly match operand and source-unit sources")
    aggregate = op in {"count", "distinct_count", "sum", "min", "max"}
    values = [_select(o, reader, known, claim["source_ids"], records=aggregate) for o in operands]
    if "allow_empty" in calc:
        _require(type(calc["allow_empty"]) is bool, "allow_empty must be boolean")
    if calc.get("allow_empty"):
        _text(calc.get("empty_reason"), "empty_reason")
    elif "empty_reason" in calc:
        _require(False, "empty_reason requires allow_empty=true")
    with localcontext() as context:
        context.prec = 200
        if aggregate:
            items = values[0]
            _require(isinstance(items, list), "aggregate operand must select an array")
            _require(len(items) <= 1000000, "aggregate selection is too large; use a verified source extract")
            _require(bool(items) or (calc.get("allow_empty") and op in {"count", "distinct_count", "sum"}),
                     "empty aggregation needs explicit allow_empty and empty_reason; min/max remain undefined")
            if op == "count":
                _require("field" not in operands[0], "count counts selected records; field projection is not allowed")
                result = Decimal(len(items))
            elif op == "distinct_count":
                _require(all(isinstance(item, (str, int, float, Decimal, bool)) for item in items),
                         "distinct_count requires scalar values or a field projection")
                # Typed canonical representations keep booleans and numbers distinct.
                keys = [("number", str(_decimal(item, "distinct value").normalize()))
                        if isinstance(item, (int, float, Decimal)) and not isinstance(item, bool)
                        else (type(item).__name__, str(item)) for item in items]
                result = Decimal(len(set(keys)))
            else:
                numbers = [_decimal(item, "aggregate value") for item in items]
                result = sum(numbers, Decimal(0)) if op == "sum" else (min(numbers) if op == "min" else max(numbers))
        else:
            numbers = [_decimal(item, "operand") for item in values]
            if op == "ratio":
                _require(numbers[1] != 0, "ratio denominator cannot be zero")
                result = numbers[0] / numbers[1]
            else:
                result = numbers[0] if op == "direct" else numbers[0] - numbers[1]
        raw_result = result
        source_unit_selection = calc.get("source_unit") or calc.get("conversion", {}).get("source_unit")
        actual_unit = None
        if source_unit_selection:
            recorded = _select(source_unit_selection, reader, known, claim["source_ids"])
            _require(isinstance(recorded, str) and bool(recorded.strip()), "source unit must select a nonempty source string")
            actual_unit = UNIT_ALIASES.get(recorded)
        if title_unit and (title_unit not in set(UNIT_ALIASES.values()) or source_unit_selection is None or actual_unit is None):
            return None, {"expected": str(expected), "actual": str(result), "unit": title_unit,
                          "operation": op, "quantity_start": quantity_start, "quantity_end": quantity_end,
                          "unresolved_reason": "recognized title unit needs a source-bound calculation.source_unit with supported units"}
        if "conversion" in calc:
            conv = calc["conversion"]
            _require(all(isinstance(conv[k], str) and conv[k] in UNITS for k in ("from", "to")), "unsupported conversion unit")
            recorded_unit = _select(conv["source_unit"], reader, known, claim["source_ids"])
            _require(isinstance(recorded_unit, str) and recorded_unit == conv["from"],
                     "conversion source unit must exactly match its selected source field")
            source_unit, target_unit = UNITS[conv["from"]], UNITS[conv["to"]]
            _require(source_unit[0] == target_unit[0], "conversion units have different dimensions")
            _require(title_unit == UNIT_ALIASES.get(conv["to"]) or (title_unit is None and conv["to"] == "ratio"),
                     "conversion target must be the unit in the title quote")
            result = result * source_unit[1] / target_unit[1]
            _require(calc.get("source_unit") is None or actual_unit == UNIT_ALIASES.get(conv["from"]),
                     "calculation and conversion source units disagree")
            actual_unit = UNIT_ALIASES[conv["to"]]
        if "rounding" in calc:
            rule = _object(calc["rounding"], "rounding", {"places", "mode"}, {"places", "mode"})
            _require(type(rule["places"]) is int and 0 <= rule["places"] <= 12 and rule["places"] == places,
                     "rounding places must equal the title literal's displayed precision (0..12)")
            _require(isinstance(rule["mode"], str) and rule["mode"] in ROUNDING, "unsupported rounding mode")
            result = result.quantize(Decimal(1).scaleb(-rule["places"]), rounding=ROUNDING[rule["mode"]])
        _require(result.is_finite(), "calculation produced a non-finite value")
    return expected == result and (title_unit is None or title_unit == actual_unit), {
        "expected": str(expected), "actual": str(result), "raw_actual": str(raw_result),
        "unit": title_unit or unit, "actual_unit": actual_unit, "operation": op,
        "quantity_start": quantity_start, "quantity_end": quantity_end}


def _date(value, label, prose=False):
    _require(isinstance(value, str), label + " must be an ISO date or timezone-qualified timestamp")
    try:
        if ISO_DATE.fullmatch(value):
            return date.fromisoformat(value)
        written = PROSE_DATE.fullmatch(value.strip()) if prose else None
        if written:
            month = written["month"] or written["month2"]
            return date(int(written["year"] or written["year2"]), _MONTHS[month.rstrip(".").casefold()],
                        int(written["day"] or written["day2"]))
        _require(bool(ISO_INSTANT.fullmatch(value)), label + " must be ISO; timestamps need an explicit timezone")
        return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)
    except (ValueError, OverflowError) as error:
        raise ValueError("Rubric facts: " + label + " is not an unambiguous ISO date/instant") from error


def _range(claim, reader, known, title, start):
    """Closed numerical intervals explicitly stated in the criterion; no invented tolerance."""
    numeric = r'[+-]?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?'
    pattern = (r'(?:(?:approximately|about)\s+(?P<nominal>' + numeric + r')\s+\(band\s+)?'
               r'(?P<lower>' + numeric + r')\s*(?:–|—|-|to)\s*(?P<upper>' + numeric + r')(?P<close>\))?')
    match = re.fullmatch(pattern, claim['quote'], re.I)
    _require(match is not None, 'RANGE needs an explicit closed lower-upper interval or approximately N (band lower-upper)')
    _require(bool(match['nominal']) == bool(match['close']), 'malformed approximation band')
    lower = _decimal(match['lower'].replace(',', ''), 'range lower bound')
    upper = _decimal(match['upper'].replace(',', ''), 'range upper bound')
    _require(lower <= upper, 'range bounds are reversed')
    _require('rounding' not in claim.get('calculation', {}), 'RANGE compares the unrounded value; do not round a value into the allowed band')
    unit, _, end = _quantity_context(title, start, start + len(claim['quote']))
    # Delegate source arithmetic and unit validation to the existing calculator.
    number = {**claim, 'kind': 'NUMBER', 'quote': match['upper']}
    synthetic_title = match['upper'] + (' ' + unit if unit else '')
    _, details = _number(number, reader, known, synthetic_title, 0)
    details.update(lower=str(lower), upper=str(upper), quantity_start=start, quantity_end=end)
    if details.get('unresolved_reason'):
        return None, details
    actual = _decimal(details['actual'], 'source-derived range value')
    nominal_ok = not match['nominal'] or lower <= _decimal(match['nominal'].replace(',', ''), 'nominal value') <= upper
    return lower <= actual <= upper and nominal_ok and (unit is None or details['actual_unit'] == unit), details


def _selected_claim(claim, reader, known):
    selection = claim.get("selection")
    _object(selection, "selection", {"source_id", "pointer"}, {"source_id", "pointer"})
    _require(claim["source_ids"] == [selection["source_id"]], "selection claim needs exactly its selected source_id")
    value = _select(selection, reader, known, claim["source_ids"])
    if claim["kind"] == "LITERAL":
        _require(isinstance(value, str), "LITERAL source selection must be a string, not a number coerced to text")
        details = {"expected": claim["quote"], "actual": value}
        if claim["quote"] != value and ANON_TOKEN.search(value):
            # The tools show the placeholder, not the real name; the row must accept it as shown.
            details["anonymized_token"] = ANON_TOKEN.search(value).group()
        return claim["quote"] == value, details
    expected, actual = _date(claim["quote"], "DATE quote", prose=True), _date(value, "DATE source")
    comparison = claim.get("comparison", "exact")
    _require(isinstance(comparison, str) and comparison in DATE_COMPARISONS,
             "DATE comparison must be exact, utc_date or pt_or_utc_date")
    details = {"comparison": comparison}
    if comparison == "pt_or_utc_date":
        # A calendar day written in PT or in UTC; the clock and instant comparisons stay UTC.
        _require(not isinstance(expected, datetime), "pt_or_utc_date compares a calendar date quote, not an instant")
        details["selection"] = [selection["source_id"], selection["pointer"]]
        if isinstance(actual, datetime):
            days = {actual.date(), actual.astimezone(PACIFIC).date()}
            details.update(utc_day=actual.date().isoformat(), pt_day=actual.astimezone(PACIFIC).date().isoformat(),
                           split_day=len(days) == 2)
        else:
            days = {actual}
        return expected in days, {**details, "expected": expected.isoformat(), "actual": actual.isoformat()}
    if comparison == "utc_date":
        expected = expected.date() if isinstance(expected, datetime) else expected
        actual = actual.date() if isinstance(actual, datetime) else actual
    return type(expected) is type(actual) and expected == actual, {**details, "expected": expected.isoformat(), "actual": actual.isoformat()}


def validate_facts(review, criterion, reader, known, *, literal_tokens=False):
    """Return mismatches, unresolved items, and auditable computation details.

    Every item is an object with claim_id/reason and an exact quote when one is
    available. Unknown schema or invalid source/operation raises ValueError.
    Numeric-bearing title text omitted from the inventory remains unresolved.
    With ``literal_tokens`` (the rubric review), ID-shaped and anonymized title
    tokens likewise need LITERAL coverage or an explicit UNRESOLVED/NOT_A_CLAIM.
    A source anchor whose ``reachability`` is not PROMPT_LINKED keeps its claims
    unresolved and marks them ``unreachable``.
    """
    _object(review, "fact_review", {"complete", "reason", "claims"}, {"complete", "reason", "claims"})
    _require(type(review["complete"]) is bool, "fact_review.complete must be boolean")
    _text(review["reason"], "fact_review.reason")
    _object(criterion, "criterion")
    title = _text(criterion.get("title"), "criterion.title")
    _require(isinstance(known, dict), "known sources must be a mapping")
    _require(isinstance(review["claims"], list) and len(review["claims"]) <= 1000, "claims must be an array (maximum 1000)")
    result = {"mismatches": [], "unresolved": [], "computed": [], "non_factual": []}
    if not review["complete"]:
        result["unresolved"].append({"claim_id": None, "reason": "fact inventory is incomplete"})
    coverage, ids = [], set()
    for claim in review["claims"]:
        _object(claim, "claim", {"id", "quote", "start", "kind", "source_ids", "reason", "calculation", "selection", "comparison", "status"},
                {"id", "quote", "kind", "source_ids", "reason"})
        cid = _text(claim["id"], "claim.id")
        _require(cid not in ids, "duplicate claim ID " + cid)
        ids.add(cid)
        quote = _text(claim["quote"], cid + ".quote")
        _text(claim["reason"], cid + ".reason")
        kind = claim["kind"]
        _require(isinstance(kind, str) and kind in KINDS, cid + " has an invalid kind")
        starts = [match.start() for match in re.finditer(re.escape(quote), title)]
        if "start" in claim:
            start = claim["start"]
            _require(type(start) is int and start in starts, cid + " quote/start does not match the exact title")
        else:
            _require(len(starts) == 1, cid + " quote must match exactly once; use start for repeated text")
            start = starts[0]
        source_ids = claim["source_ids"]
        _require(isinstance(source_ids, list) and all(isinstance(sid, str) and sid in known for sid in source_ids)
                 and len(source_ids) == len(set(source_ids)), cid + " needs unique known source IDs")
        unresolved_kind = kind == "UNRESOLVED" or (kind == "SEMANTIC" and claim.get("status") == "UNRESOLVED")
        # NOT_A_CLAIM records a numeric token that is not a factual assertion at all
        # (a label under review, the row's own quantifier, a version string). It keeps
        # the token accounted for without claiming the evidence was unavailable.
        not_a_claim = kind == "NOT_A_CLAIM"
        _require(bool(source_ids) or unresolved_kind or not_a_claim, cid + " needs supporting source IDs")
        _require(not (not_a_claim and source_ids), cid + " is declared non-factual, so it must cite no source")
        expected_fields = {"NUMBER": {"calculation"}, "RANGE": {"calculation"}, "DATE": {"selection", "comparison"},
                           "LITERAL": {"selection"}, "SEMANTIC": {"status"}, "UNRESOLVED": set(),
                           "NOT_A_CLAIM": set()}[kind]
        _require(not (set(claim) & {"calculation", "selection", "comparison", "status"}) - expected_fields,
                 cid + " contains fields incompatible with its kind")
        if kind == "SEMANTIC":
            _require(isinstance(claim.get("status"), str) and claim["status"] in {"VERIFIED", "CONTRADICTED", "UNRESOLVED"}, cid + " needs a semantic status")
        unavailable, unreachable = [], []
        for sid in source_ids:
            anchor = known[sid]
            _object(anchor, "source anchor")
            _require(isinstance(anchor.get("visibility"), str) and anchor["visibility"] in {"VISIBLE", "INACCESSIBLE", "UNRESOLVED"}, "source visibility is invalid")
            if "reachability" in anchor:
                _require(anchor["reachability"] in REACHABILITY, "source reachability is invalid")
                if anchor["reachability"] != REACHABLE:
                    unreachable.append(sid + " (" + anchor["reachability"] + ")")
            if anchor["visibility"] != "VISIBLE":
                unavailable.append(sid)
            else:
                reader.quote(anchor)  # Recheck the selected evidence, even for semantic judgments.
        base = {"claim_id": cid, "quote": quote, "source_ids": source_ids, "kind": kind}
        if kind != "SEMANTIC":
            coverage.append((start, start + len(quote), kind))
        if not_a_claim:
            result["non_factual"].append({**base, "reason": claim["reason"]})
            continue
        if unreachable:
            # Eval 3 §2.4: a deciding record the Agent cannot reach from the prompt
            # (Trash/Spam, attachment-only, unlinked) cannot define a passing answer.
            result["unresolved"].append({**base, "unreachable": unreachable,
                                         "reason": "deciding record is not reachable by the Agent: " + ", ".join(unreachable)})
            continue
        if unavailable or unresolved_kind:
            reason = "source visibility is unresolved: " + ", ".join(unavailable) if unavailable else claim["reason"]
            result["unresolved"].append({**base, "reason": reason})
            continue
        try:
            if kind == "NUMBER":
                matched, details = _number(claim, reader, known, title, start)
            elif kind == "RANGE":
                matched, details = _range(claim, reader, known, title, start)
            elif kind in {"DATE", "LITERAL"}:
                matched, details = _selected_claim(claim, reader, known)
            else:
                matched = claim["status"] == "VERIFIED"
                details = {"status": claim["status"], "method": "source-backed semantic judgment; not an executable proof"}
        except (InvalidOperation, OverflowError, ZeroDivisionError) as error:
            raise ValueError("Rubric facts: invalid bounded arithmetic for " + cid) from error
        result["computed"].append({**base, **details, "matched": matched, "reason": claim["reason"]})
        if kind in {"NUMBER", "RANGE"}:
            coverage.append((details["quantity_start"], details["quantity_end"], kind))
        if matched is None:
            result["unresolved"].append({**base, **details, "reason": details["unresolved_reason"]})
        elif not matched:
            result["mismatches"].append({**base, **details, "reason": claim["reason"]})
    dates = list(DATE_TOKEN.finditer(title))
    quantities = list(SPELLED_TOKEN.finditer(title))
    for match in dates + quantities + [m for m in DIGIT_TOKEN.finditer(title)
                                       if not any(d.start() <= m.start() and d.end() >= m.end() for d in dates)]:
        is_date = match in dates
        _, quantity_start, quantity_end = (None, match.start(), match.end()) if is_date else _quantity_context(title, match.start(), match.end())
        if not any(start <= quantity_start and end >= quantity_end and
                   (not is_date or kind in {"DATE", "LITERAL", "UNRESOLVED", "NOT_A_CLAIM"}) for start, end, kind in coverage):
            result["unresolved"].append({"claim_id": None, "quote": match.group(),
                                         "reason": "numeric title token (digit or English cardinal) lacks executable NUMBER/DATE/LITERAL coverage or an explicit UNRESOLVED or NOT_A_CLAIM claim"})
    if literal_tokens:
        anonymized = list(ANON_TOKEN.finditer(title))
        keys = [m for m in ID_TOKEN.finditer(title)
                if not any(a.start() <= m.start() and a.end() >= m.end() for a in anonymized)]
        for match in anonymized + keys:
            if not any(start <= match.start() and end >= match.end() and kind in {"LITERAL", "UNRESOLVED", "NOT_A_CLAIM"}
                       for start, end, kind in coverage):
                result["unresolved"].append({"claim_id": None, "quote": match.group(),
                                             "reason": "ID-shaped or anonymized title token lacks an exact LITERAL claim "
                                                       "(or an explicit UNRESOLVED or NOT_A_CLAIM claim); SEMANTIC cannot bind it"})
    return result
