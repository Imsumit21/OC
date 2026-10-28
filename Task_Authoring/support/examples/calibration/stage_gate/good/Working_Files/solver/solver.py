"""Stage-gate fixture solver: the tools/oracle_kit.py contract on the one-row fixture universe.

The hub post is seeded once (b759cf...); trap T1's resolver is ENG-2280. The rule `stale_count` is the mechanism node T1:
with it the defect list reads as open (ENG-2280 governs); its natural-reading fallback takes the hub post's framing.
Parses the SQL as data through tools/base_check.parse_sql; never executes it.
"""
import collections

KEY_REGEX = r"defect list"
FIELDS = ["item", "status"]
CLASS_FIELD, GROUPS_FIELD = "status", "groups"
POST = "b759cfabc37fef15d3b8d50fb4aeb564"
RULES = {"stale_count": {"mechanism": "A1", "family": "A1", "requirement": "R1", "nodes": ["T1"], "decides": ["status"],
                         "natural_reading": "take the hub post's framing of the list instead of ENG-2280's state",
                         "authority": [POST], "source": "hub"}}


def load_state(sql_text, revision=None):
    from base_check import parse_sql
    return {"rows": [x["row"] for x in parse_sql(sql_text) if x["op"] == "insert"], "revision": revision or "r1"}


def keys():
    return ["defect list"]


def _off(spec, name, key):
    return any(d == name or (isinstance(d, tuple) and d[0] == name and key in d[1]) for d in spec)


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    post = next((r for r in state["rows"] if r.get("id") == POST), None)
    out = {}
    for k in keys_ or keys():
        if post is None:
            status = None
        elif _off(disable, "stale_count", k):
            status = "stale"
        else:
            status = "open" if "open defect list" in post.get("text", "") else "unknown"
        out[k] = {"item": k, "status": status, "groups": [], "evidence": {"post": post["id"] if post else None}}
    return out


def aggregates(rows):
    return {"classes": dict(collections.Counter(v["status"] for v in rows.values())), "groups": {}}


def evidence(rows, key, field):
    return [rows[key]["evidence"]["post"]] if rows[key]["evidence"]["post"] else []


def touched(state, rule):
    return set(keys())


def deciding(state, rule, key):
    return [POST]
