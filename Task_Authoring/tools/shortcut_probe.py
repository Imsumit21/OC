#!/usr/bin/env python3
"""shortcut_probe.py - find shallow answer-bearing records that collapse a task.

A task is only as hard as its cheapest valid route. If one record the persona can open
already holds most of the rubric's acceptance values (a summary message, an export, a
cached query, a seeded recap), an agent can answer from it and skip the intended
discovery. This probe searches the whole persona-visible universe for such records.

Deterministic, read-only, stdlib only (Python 3.9). Run from the workspace root:

  python3 Task_Authoring/tools/shortcut_probe.py <persona> <values_file> [--k 3] [--services all|svc,svc]
                                                  [--sql FILE|none] [--json] [--no-cache]
  python3 Task_Authoring/tools/shortcut_probe.py --self-test

<persona>      persona_key, exact roster email or exact roster name (persona_view.resolve_persona).
<values_file>  either
               - a rubric plan (`09_Rubric_Writing_Plan.md`): the acceptance values are the
                 backticked or double-quoted literals in section A's "Values" column; an F-id in
                 that column with no literal of its own contributes the literals (else the
                 `;`-separated pieces) of its ledger row's "Expected data" cell
                 (`08_OE_Writing_Ledger.md` beside the plan). Section D rows whose "Item set" cell
                 holds two or more literals are populations (their keys).
               - a plain list: one value per line; `#` comments; a line `[population <name>]`
                 starts a population key set, `[values]` returns to plain values. Quotes or
                 backticks around a value are stripped.

What is searched (every search goes through the harness's own tools):
  scoped    gmail, slack, gcal, gdrive, gdocs, gsheets, gslides - `persona_view.search` with the
            persona's ACL applied (only YES records count; UNVERIFIED public channels are counted
            but carry no record id, see residuals).
  unscoped  contacts, github, trello, linear, snowflake, confluence - `hg.py search search-many`
            (one shared scan per service; a record is the JSON pointer cut after its last array
            index, e.g. /issues/345, /tables/3/rows/120, /query_history/17).
  SQL       the task's injection overlay (`01_Universe_Inject.sql` beside the values file, or
            --sql): every INSERT row is a record; scoped rows count only when
            `persona_view.check_sql` says YES.

A value matches a record when it occurs case-insensitively with no letter or digit on either
side. Values shorter than 3 characters are dropped (listed as SKIPPED).

Reported (each blocks `stage_gate.py rubric-writing` until dispositioned `SHORTCUT-OK: <key> - <reason>`):
  HIT         one visible record holds >= k of the acceptance values, or >= 50% of one
              population's keys;
  INCOMPLETE  a search did not finish (match limit, error, incomplete scan): absence of a
              shortcut is not established for that value on that service.

Output (paste it verbatim into the plan's section F):
  SHORTCUT PROBE as <key> <email> · values <file> (<n> values, <m> populations, sha <12 hex>) · k <k> · services <list> · sql <file|none>
  HIT <service> <record> holds <i>/<n> values (k=<k>): `v1` · `v2` ...
  HIT <service> <record> holds <i>/<n> keys of population <name> (<pct>% >= 50%)
  INCOMPLETE <service> value:"<v>" (<reason>)
  verdict: CLEAR | HITS (<n>) | INCOMPLETE (<n>)

Cache: per (persona, service, value) results under Task_Authoring/support/local_search/cache/shortcut_probe/,
keyed by the source manifests' size+mtime, so a gate re-run on unchanged data is instant.
Exit: 0 CLEAR · 1 HITS or INCOMPLETE · 2 usage.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
BUNDLE = HERE.parent
WS = BUNDLE.parent
CACHE = BUNDLE / "support" / "local_search" / "cache" / "shortcut_probe"
FIXTURES = BUNDLE / "support" / "examples" / "calibration" / "stage_gate" / "good"

SCOPED = ["gmail", "slack", "gcal", "gdrive", "gdocs", "gsheets", "gslides"]
UNSCOPED = ["contacts", "github", "trello", "linear", "snowflake", "confluence"]
ALL = SCOPED + UNSCOPED
UNSCOPED_LIMIT = 20000
POP_SHARE = 0.5
MIN_LEN = 3

# ------------------------------------------------------------------ value extraction


def _cells(line: str) -> list:
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    out, cur, tick = [], [], False
    for ch in s:
        if ch == "`":
            tick = not tick
        if ch == "|" and not tick:
            out.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
    out.append("".join(cur).strip())
    return out


def _section_tables(text: str, head_rx: str) -> list:
    """[(header_cells, [row_cells...])] for markdown tables under headings matching head_rx."""
    lines = text.splitlines()
    out, i, in_sec, level, fence = [], 0, False, 0, False
    cur = []
    for l in lines + [""]:
        if l.lstrip().startswith("```"):
            fence = not fence
        m = re.match(r"^(#{1,6})\s+(.*)$", l) if not fence else None
        if m:
            if in_sec and len(m.group(1)) <= level:
                in_sec = False
            if re.search(head_rx, m.group(2), re.I):
                in_sec, level = True, len(m.group(1))
        if in_sec and not fence and l.strip().startswith("|"):
            cur.append(l)
            continue
        if len(cur) >= 2 and re.match(r"^\|?\s*:?-{2,}", cur[1].strip()):
            out.append((_cells(cur[0]), [_cells(r) for r in cur[2:]]))
        cur = []
    return out


def _col(header, rx):
    for i, h in enumerate(header):
        if re.search(rx, h, re.I):
            return i
    return None


def literals(cell: str) -> list:
    out = []
    for a, b, c in re.findall(r"`([^`]+)`|\"([^\"]+)\"|“([^”]+)”", cell or ""):
        v = (a or b or c).strip()
        if v:
            out.append(v)
    return out


def from_plan(path: Path):
    """(values, populations, skipped) from a rubric plan and its sibling ledger."""
    text = path.read_text(errors="replace")
    ledger = path.parent / "08_OE_Writing_Ledger.md"
    expected = {}
    if ledger.exists():
        for header, rows in _section_tables(ledger.read_text(errors="replace"), r"^B\b"):
            ce = _col(header, r"expected")
            for r in rows:
                m = re.match(r"\s*(F\d+)", r[0] if r else "")
                if m and ce is not None and ce < len(r):
                    expected[m.group(1)] = r[ce]
    values, skipped = [], []
    for header, rows in _section_tables(text, r"coverage matrix"):
        cv = _col(header, r"values")
        if cv is None:
            continue
        for r in rows:
            cell = r[cv] if cv < len(r) else ""
            lits = literals(cell)
            values += lits
            if lits:
                continue
            for f in re.findall(r"\bF\d{1,3}\b", cell):
                exp = expected.get(f, "")
                got = literals(exp) or [x.strip() for x in re.split(r";", exp) if x.strip() not in ("", "—", "-")]
                values += got
    pops = {}
    for header, rows in _section_tables(text, r"spot-check"):
        ci = _col(header, r"item set")
        if ci is None:
            continue
        for r in rows:
            keys = literals(r[ci] if ci < len(r) else "")
            if len(keys) >= 2:
                pops[(r[0] or f"G{len(pops) + 1}").strip()] = keys
    return values, pops, skipped


def from_list(path: Path):
    values, pops, cur = [], {}, None
    for raw in path.read_text(errors="replace").splitlines():
        l = raw.strip()
        if not l or l.startswith("#"):
            continue
        m = re.match(r"^\[population\s+(.+?)\]$", l, re.I)
        if m:
            cur = m.group(1).strip()
            pops.setdefault(cur, [])
            continue
        if re.match(r"^\[values\]$", l, re.I):
            cur = None
            continue
        v = l.strip("`\"“” ").strip()
        if cur is None:
            values.append(v)
        else:
            pops[cur].append(v)
    return values, pops, []


def load_values(path: Path):
    values, pops, _ = (from_plan if path.suffix.lower() == ".md" else from_list)(path)
    seen, vals, skipped = set(), [], []
    for v in values:
        k = v.casefold()
        if len(v) < MIN_LEN:
            skipped.append(v)
        elif k not in seen:
            seen.add(k)
            vals.append(v)
    pops = {n: sorted({k for k in ks if len(k) >= MIN_LEN}, key=str.casefold) for n, ks in pops.items()}
    pops = {n: ks for n, ks in pops.items() if len(ks) >= 2}
    return vals, pops, skipped


def values_sha(values, pops) -> str:
    canon = json.dumps({"values": sorted(values, key=str.casefold),
                        "populations": {n: sorted(ks, key=str.casefold) for n, ks in sorted(pops.items())}},
                       ensure_ascii=False, sort_keys=True)
    return hashlib.sha256(canon.encode()).hexdigest()[:12]

# ------------------------------------------------------------------ matching


def matcher(v: str):
    return re.compile(r"(?<![A-Za-z0-9])" + re.escape(v) + r"(?![A-Za-z0-9])", re.I)


def record_of(pointer: str) -> str:
    """JSON pointer cut after its last array index (the record that holds the scalar)."""
    segs = pointer.split("/")
    idx = [i for i, s in enumerate(segs) if s.isdigit()]
    return "/".join(segs[: idx[-1] + 1]) if idx else pointer


def _fingerprint() -> str:
    h = hashlib.sha256()
    for root in sorted(WS.glob("HarmonyGames_*")):
        for f in sorted(root.glob("**/source_manifest.json")):
            try:
                st = f.stat()
            except OSError:
                continue
            h.update(f"{f}:{st.st_size}:{int(st.st_mtime)}".encode())
    return h.hexdigest()[:16]


class Searcher:
    """Wraps persona_view / hg.py with a per-(persona, service, value) cache."""

    def __init__(self, persona, use_cache=True):
        sys.path.insert(0, str(HERE))
        import persona_view  # noqa: E402
        self.pv = persona_view
        self.p = persona
        self.u = None
        self.use_cache = use_cache
        self.fp = _fingerprint() if use_cache else ""

    def universe(self):
        if self.u is None:
            self.u = self.pv.Universe()
        return self.u

    def _cache(self, svc, value):
        key = hashlib.sha256(f"{self.p['persona_key']}|{svc}|{value}|{self.fp}".encode()).hexdigest()[:24]
        return CACHE / f"{svc}_{key}.json"

    def scoped(self, svc, value):
        """{"records": {id: snippet}, "complete": bool, "note": str}"""
        c = self._cache(svc, value)
        if self.use_cache and c.exists():
            return json.loads(c.read_text())
        r = self.pv.search(self.universe(), self.p, svc, value, limit=10 ** 7, hidden=False)
        rx = matcher(value)
        recs = {}
        for h in r.get("visible", []):
            snip = " ".join(str(h.get(k) or "") for k in ("snippet", "subject", "summary", "name"))
            if rx.search(snip):
                recs[str(h["id"])] = snip[:160]
        out = {"records": recs, "complete": len(r.get("visible", [])) >= r.get("visible_total", 0),
               "note": f"visible {r.get('visible_total', 0)}, unverified {r.get('unverified', 0)}"}
        if self.use_cache:
            CACHE.mkdir(parents=True, exist_ok=True)
            c.write_text(json.dumps(out))
        return out

    def unscoped(self, svc, values):
        """{value: {"records": {...}, "complete": bool, "note": str}} via one search-many scan."""
        out, todo = {}, []
        for v in values:
            c = self._cache(svc, v)
            if self.use_cache and c.exists():
                out[v] = json.loads(c.read_text())
            else:
                todo.append(v)
        if not todo:
            return out
        req = {"service": svc, "queries": [{"id": f"q{i}", "query": v, "limit": UNSCOPED_LIMIT} for i, v in enumerate(todo)]}
        with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as fh:
            json.dump(req, fh)
            reqf = fh.name
        try:
            r = subprocess.run([sys.executable, str(HERE / "hg.py"), "search", "search-many", "--request", reqf, "--compact"],
                               capture_output=True, text=True, cwd=str(WS))
            data = json.loads(r.stdout or "{}")
        except (OSError, ValueError) as e:
            data = {"error": str(e)}
        finally:
            Path(reqf).unlink(missing_ok=True)
        qs = data.get("queries") or {}
        for i, v in enumerate(todo):
            q = qs.get(f"q{i}")
            if not isinstance(q, dict):
                out[v] = {"records": {}, "complete": False, "note": f"search-many failed: {str(data)[:120]}"}
                continue
            rx = matcher(v)
            recs = {}
            for m in q.get("matches", []):
                if rx.search(str(m.get("text") or "")):
                    recs[f"{m.get('service_file')}{record_of(m.get('pointer') or '')}"] = str(m.get("text"))[:160]
            complete = bool(q.get("scan_complete")) and not q.get("errors") and len(q.get("matches", [])) < UNSCOPED_LIMIT
            out[v] = {"records": recs, "complete": complete,
                      "note": "" if complete else (q.get("stop_reason") or f"errors {q.get('errors')}" or "scan incomplete")}
            if self.use_cache and complete:
                CACHE.mkdir(parents=True, exist_ok=True)
                self._cache(svc, v).write_text(json.dumps(out[v]))
        return out

    def sql(self, sql_text, values):
        """{(service, record): set(values)} for visible seeded INSERT rows."""
        from base_check import parse_sql  # noqa: E402
        stmts = parse_sql(sql_text)
        chk = self.pv.check_sql(self.universe(), self.p, sql_text, None, True)
        verdicts = {}
        for row in chk["rows"]:
            if row.get("op") == "insert":
                verdicts.setdefault((row["line"], row["table"]), []).append(row)
        rxs = [(v, matcher(v)) for v in values]
        out = {}
        for s in stmts:
            if s.get("op") != "insert":
                continue
            t, r = s["table"], s.get("row") or {}
            svc = t.split(".", 1)[0]
            if svc in self.pv.SCOPED:
                cands = verdicts.get((s["line"], t)) or []
                vals = {str(x) for x in r.values()}
                row = next((c for c in cands if not c.get("keys") or set(c["keys"]) & vals), None)
                if row is None or row["verdict"] != "YES":
                    continue
            blob = " \n ".join(str(x) for x in r.values() if x is not None)
            got = {v for v, rx in rxs if rx.search(blob)}
            if got:
                rid = r.get("id") or r.get("event_id") or r.get("identifier") or next(iter(r.values()), "?")
                out[(f"sql:{t}", f"L{s['line']}:{rid}")] = got
        return out

# ------------------------------------------------------------------ probe


def probe(persona, values, pops, k=3, services=None, sql_text=None, searcher=None):
    services = ALL if services is None else services
    s = searcher or Searcher(persona)
    allv = list(dict.fromkeys(values + [x for ks in pops.values() for x in ks]))
    holds, incomplete = {}, []      # (service, record) -> set(values)
    for svc in services:
        if svc in SCOPED:
            res = {v: s.scoped(svc, v) for v in allv}
        else:
            res = s.unscoped(svc, allv)
        for v, r in res.items():
            if not r.get("complete", True):
                incomplete.append((svc, v, r.get("note") or "incomplete"))
            for rec in r.get("records", {}):
                holds.setdefault((svc, rec), set()).add(v)
    if sql_text:
        for key, got in s.sql(sql_text, allv).items():
            holds.setdefault(key, set()).update(got)
    hits = []
    vset = {v.casefold() for v in values}
    for (svc, rec), got in sorted(holds.items()):
        gv = sorted((v for v in got if v.casefold() in vset), key=str.casefold)
        if values and len(gv) >= k:
            hits.append({"service": svc, "record": rec, "kind": "values", "held": gv, "of": len(values), "k": k})
        for name, keys in sorted(pops.items()):
            kk = {x.casefold() for x in keys}
            gk = sorted((v for v in got if v.casefold() in kk), key=str.casefold)
            if keys and len(gk) / len(keys) >= POP_SHARE:
                hits.append({"service": svc, "record": rec, "kind": "population", "population": name, "held": gk,
                             "of": len(keys), "pct": round(100 * len(gk) / len(keys))})
    verdict = "HITS" if hits else ("INCOMPLETE" if incomplete else "CLEAR")
    return {"persona": persona["persona_key"], "email": persona["email"], "k": k, "services": services,
            "values": values, "populations": pops, "hits": hits,
            "incomplete": [{"service": a, "value": b, "reason": c} for a, b, c in incomplete], "verdict": verdict}


def render(r, values_name, sha, sql_name, skipped=()):
    svcs = "all" if r["services"] == ALL else ",".join(r["services"])
    out = [f"SHORTCUT PROBE as {r['persona']} <{r['email']}> · values {values_name} ({len(r['values'])} values, "
           f"{len(r['populations'])} populations, sha {sha}) · k {r['k']} · services {svcs} · sql {sql_name}"]
    for h in r["hits"]:
        if h["kind"] == "values":
            out.append(f"HIT {h['service']} {h['record']} holds {len(h['held'])}/{h['of']} values (k={h['k']}): "
                       + " · ".join(f"`{v}`" for v in h["held"]))
        else:
            out.append(f"HIT {h['service']} {h['record']} holds {len(h['held'])}/{h['of']} keys of population "
                       f"{h['population']} ({h['pct']}% >= 50%)")
    for x in r["incomplete"]:
        out.append(f"INCOMPLETE {x['service']} value:\"{x['value']}\" ({x['reason']})")
    for v in skipped:
        out.append(f"SKIPPED value:\"{v}\" (shorter than {MIN_LEN} characters)")
    n = len(r["hits"]) if r["hits"] else len(r["incomplete"])
    out.append(f"verdict: {r['verdict']}" + (f" ({n})" if r["verdict"] != "CLEAR" else " (0 shortcut records)"))
    return "\n".join(out)


def run(persona_q, values_path: Path, k=3, services=None, sql=None, use_cache=True):
    sys.path.insert(0, str(HERE))
    import persona_view  # noqa: E402
    p = persona_view.resolve_persona(persona_q)
    values, pops, skipped = load_values(values_path)
    if sql is None:
        cands = [d / "01_Universe_Inject.sql" for d in (values_path.parent, values_path.parent.parent)]
        sql = next((c for c in cands if c.exists()), "none")
    sql_text = Path(sql).read_text(errors="replace") if sql != "none" else None
    r = probe(p, values, pops, k, services, sql_text, Searcher(p, use_cache))
    r["skipped"] = skipped
    sha = values_sha(values, pops)
    return r, render(r, values_path.name, sha, Path(sql).name if sql != "none" else "none", skipped)

# ------------------------------------------------------------------ self-test


class _Fake:
    """Offline searcher for the aggregation tests."""

    def __init__(self, table):
        self.t = table   # svc -> value -> {record: snippet}

    def scoped(self, svc, v):
        return {"records": self.t.get(svc, {}).get(v, {}), "complete": True}

    def unscoped(self, svc, values):
        return {v: {"records": self.t.get(svc, {}).get(v, {}), "complete": v != "huge"} for v in values}

    def sql(self, sql_text, values):
        return {}


def self_test(verbose=False) -> int:
    fails = []

    def ok(name, cond, detail=""):
        if not cond:
            fails.append(f"{name}: {detail}")
        elif verbose:
            print(f"  ok  {name}")

    p = {"persona_key": "x", "email": "x@y"}
    fake = _Fake({"slack": {"alpha": {"C1/1.0": "a"}, "beta": {"C1/1.0": "b", "C2/2.0": "b"}, "gamma": {"C1/1.0": "g"}},
                  "linear": {"k1": {"data.json/issues/3": "k1"}, "k2": {"data.json/issues/3": "k2"},
                             "k3": {"data.json/issues/9": "k3"}}})
    r = probe(p, ["alpha", "beta", "gamma", "delta"], {"G1": ["k1", "k2", "k3", "k4"]}, 3, ["slack", "linear"], None, fake)
    ok("k-values hit", [h["record"] for h in r["hits"] if h["kind"] == "values"] == ["C1/1.0"], r["hits"])
    ok("population >= 50% hit", any(h["kind"] == "population" and h["record"] == "data.json/issues/3" for h in r["hits"]), r["hits"])
    ok("population < 50% not hit", not any(h["record"] == "data.json/issues/9" for h in r["hits"]), r["hits"])
    r = probe(p, ["alpha", "beta", "gamma", "delta"], {}, 4, ["slack"], None, fake)
    ok("k=4 clears", r["verdict"] == "CLEAR", r["verdict"])
    r = probe(p, ["huge"], {}, 3, ["linear"], None, fake)
    ok("incomplete scan reported", r["verdict"] == "INCOMPLETE" and r["incomplete"], r)
    ok("boundary match", bool(matcher("0.3.309").search("to 0.3.309 and")) and not matcher("48").search("1480"),
       "word-boundary matcher")
    ok("record_of", record_of("/tables/3/rows/120/spend_usd") == "/tables/3/rows/120" and
       record_of("/issues/345/comments/2/body") == "/issues/345/comments/2", "pointer trimming")
    # value extraction from the stage_gate good fixture plan (literals + ledger fallback)
    plan = FIXTURES / "09_Rubric_Writing_Plan.md"
    if plan.exists():
        v, pops, _ = load_values(plan)
        ok("plan extraction", len(v) >= 3 and values_sha(v, pops) == values_sha(list(reversed(v)), pops), v)
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "v.txt"
        f.write_text("# acceptance values\n`0.3.309`\nloading screen\nab\n[population defects]\nENG-1\nENG-2\n[values]\napp store\n")
        v, pops, sk = load_values(f)
        ok("list parsing", v == ["0.3.309", "loading screen", "app store"] and pops == {"defects": ["ENG-1", "ENG-2"]}
           and sk == ["ab"], (v, pops, sk))
    # live: the persona's own DM holds three acceptance values (base, scoped, ACL applied)
    sys.path.insert(0, str(HERE))
    try:
        import persona_view  # noqa: E402
        pa = persona_view.resolve_persona("arthur_blake")
        s = Searcher(pa, use_cache=False)
        r = probe(pa, ["0.3.309", "loading screen", "app store"], {}, 3, ["slack"], None, s)
        ok("live slack hit (D04UGG61DUM/1770751702.596069)",
           any(h["record"] == "D04UGG61DUM/1770751702.596069" for h in r["hits"]), r["hits"][:3])
        r = probe(pa, ["leonard.hayes@harmonygames.co", "Leonard", "Hayes"], {}, 3, ["contacts"], None, s)
        ok("live unscoped hit (contacts record)", any(h["service"] == "contacts" and "/contacts/" in h["record"]
                                                      for h in r["hits"]), r["hits"][:3])
        sql = (FIXTURES / "01_Universe_Inject.sql").read_text()
        r = probe(pa, ["open defect list", "data room", "the sheet"], {}, 3, [], sql, s)
        ok("live SQL overlay hit (seeded, visible)", any(h["service"] == "sql:slack.slack_messages" for h in r["hits"]),
           r["hits"])
        r = probe(pa, ["open defect list", "data room", "the sheet", "zz-not-there"], {}, 4, [], sql, s)
        ok("SQL overlay below k clears", r["verdict"] == "CLEAR", r["hits"])
    except SystemExit as e:
        fails.append(f"live checks could not run: {e}")
    for f in fails:
        print("self-test FAIL - " + f)
    if not fails:
        print("self-test: ok (aggregation, population share, incomplete scans, matcher, pointer records, plan + list "
              "parsing, live scoped / unscoped / SQL-overlay hits)")
    return 1 if fails else 0


def main(argv) -> int:
    ap = argparse.ArgumentParser(prog="shortcut_probe.py", description="find shallow answer-bearing records (see docstring)")
    ap.add_argument("persona", nargs="?")
    ap.add_argument("values_file", nargs="?")
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--services", default="all", help="all, or a comma list of services")
    ap.add_argument("--sql", help="injection SQL overlay (default: 01_Universe_Inject.sql beside the values file); 'none' to skip")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--self-test", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        return self_test(a.verbose)
    if not a.persona or not a.values_file:
        ap.print_usage(sys.stderr)
        return 2
    services = ALL if a.services == "all" else [x.strip() for x in a.services.split(",") if x.strip()]
    bad = [x for x in services if x not in ALL]
    if bad:
        print(f"error: unknown service(s) {bad}; choose from {ALL}", file=sys.stderr)
        return 2
    vf = Path(a.values_file)
    if not vf.is_file():
        print(f"error: {vf} not found", file=sys.stderr)
        return 2
    r, text = run(a.persona, vf, a.k, services, a.sql, not a.no_cache)
    print(json.dumps(r, indent=2, ensure_ascii=False, default=sorted) if a.json else text)
    return 0 if r["verdict"] == "CLEAR" else 1


if __name__ == "__main__":
    from runtime_context import guarded_entry
    guarded_entry(globals(), require_source=True)
    raise SystemExit(main(sys.argv[1:]))
