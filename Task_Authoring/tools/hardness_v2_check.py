#!/usr/bin/env python3
"""hardness_v2_check.py - advisory Hardness v2 (Opus 5.5) self-checks for a scenario design or injection.

Hardness v2 (references/Docs/13_Hardness_v2_Opus55.md; 46 Opus 5.5 tasks under 75 %) found that Opus 5.5 settles any
correction it meets on the way to the original, and that volume and plain arithmetic no longer cost it points. This
tool answers the guideline's Part 7 self-checks (and the Part 5 design rules they test) from the manifest, the SQL
overlay, the gradable surface and the prompt:

  SAME_PLACE      (Part 7 "same-place check"; Part 2, trap 2) for every trap with two or more version_records, the
                  newest record (the correction) is compared with where an agent already is when it meets the older
                  ones. Kinds, in this order:
                    same_container      the correction shares a container with a superseded version (one Slack
                                        thread, Gmail thread, Trello card, Linear issue, GitHub PR, Confluence page,
                                        calendar event, Drive/Docs/Sheets/Slides file or warehouse table);
                    first_read          the correction sits in an anchor's container (the thread or file the prompt
                                        points at, including replies in that thread);
                    on_delegation_path  the correction sits in the container of a record that delegates, directly or
                                        through other delegations, to a superseded version (ask_fragments
                                        seeded_ids -> delegated_by_record), so the agent reads it on the way there.
                  A record whose container cannot be derived is UNRESOLVED, never CLEAN. An explicit
                  version_records[].container (same key format) overrides the derivation.
  DONE_CHECK      (Part 7 "done check"; trap 1) no A24 rule, chain root or done_gap trap.
  TWO_DECISIONS   (Part 5 rule 1) fewer than two mechanism_portfolio rules whose nodes span two or more services and
                  that decide different requirements.
  DECISION_FLIP   (Part 7 "decision flip"; Part 5 rule 3) a mechanism_portfolio rule that can flip no weight-5 slot
                  of the gradable surface (slots[].mechanisms or flipped_by). The repair is to move the evidence or
                  change the work so the rule decides 5-band work; never raise a weight (09_Rubric_Writing gate 8).
  INPUT_CHECK     (Part 7 "input check"; trap 8) a weight-5 aggregate slot that no rule or mutant can move: its
                  total is plain arithmetic on clean inputs.
  FILTER_CHECK    (Part 7 "filter check"; trap 7) no exact_predicate or near_miss_mention trap and no A17 rule.
  RULE_IN_PROMPT  (Part 8) a run of eight or more consecutive words of a trap resolver appears in the prompt; one
                  v2 task went from failing to 100 % once its rules were written into the prompt.

Container keys: slack:<channel>/<thread root ts>, gmail:<thread id>, file:<drive file id> (Docs, Sheets, Slides and
Drive share it), gcal:<ical uid or event id>, trello:<card id>, linear:<issue>, github:<repo>#<pr>,
confluence:<page id>, snowflake:<table>.

Statuses per check: FLAG, CLEAN, SKIP (input absent) or UNRESOLVED. These are advisory design warnings, not proof:
every FLAG needs a written disposition in the design or hardening report, and the response is to redesign the
difficulty (move the correction, add a done gap, move items outside the filter), never to weaken a fairness link or
raise a weight. Read-only, stdlib only, never executes SQL.

Usage:
  python3 -B Task_Authoring/tools/hardness_v2_check.py --task-dir DIR [--manifest M] [--sql SQL] [--prompt P]
      [--surface S] [--json] [--strict]
  python3 -B Task_Authoring/tools/hardness_v2_check.py --design --task-dir DIR [--manifest DRAFT]   (scenario stage:
      no SQL yet, so containers come from record ids alone and more records stay UNRESOLVED)
  python3 -B Task_Authoring/tools/hardness_v2_check.py --self-test
Exit 0 = report printed (advisory), 1 = --strict and a check is FLAG or UNRESOLVED, 2 = usage error.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

LABEL = "ADVISORY · Hardness v2 (Opus 5.5) self-checks · references/Docs/13_Hardness_v2_Opus55.md"
CHECKS = (
    "SAME_PLACE",
    "DONE_CHECK",
    "TWO_DECISIONS",
    "DECISION_FLIP",
    "INPUT_CHECK",
    "FILTER_CHECK",
    "RULE_IN_PROMPT",
)
PART = {
    "SAME_PLACE": "Part 7 same-place check / trap 2",
    "DONE_CHECK": "Part 7 done check / trap 1",
    "TWO_DECISIONS": "Part 5 rule 1",
    "DECISION_FLIP": "Part 7 decision flip / Part 5 rule 3",
    "INPUT_CHECK": "Part 7 input check / trap 8",
    "FILTER_CHECK": "Part 7 filter check / trap 7",
    "RULE_IN_PROMPT": "Part 8 / Appendix 'don't rely on rules spelled out in the prompt'",
}
FILE_TABLES = {
    "gdocs.docs_documents": "document_id",
    "gdrive.drive_files": "id",
    "gsheets.sheets_spreadsheets": "spreadsheet_id",
    "gsheets.sheets_sheets": "spreadsheet_id",
    "gdrive.drive_sheets": "spreadsheet_id",
    "gslides.slides_presentations": "presentation_id",
    "gslides.slides_pages": "presentation_id",
    "gslides.slides_page_elements": "presentation_id",
}
ID_COLS = ("id", "document_id", "spreadsheet_id", "presentation_id", "event_id")
SLACK_ID = re.compile(r"^([CDG][A-Z0-9]{8,11})/(\d{10}\.\d{6})$")
LINEAR_KEY = re.compile(r"^[A-Z][A-Z0-9]{1,6}-\d+$")
GMAIL_THREAD = re.compile(r"^[^/\s]+@[^/\s]+/\d+$")
PROMPT_SPAN = 8


# ------------------------------------------------------------------ containers from the SQL overlay


class Overlay:
    """Seeded rows by id, and the container each seeded record lives in."""

    def __init__(self, sql_text: str):
        self.rows: dict[str, list] = {}
        self.slack: dict[tuple, dict] = {}
        self.checklist_card: dict[str, str] = {}
        if not sql_text.strip():
            return
        from base_check import parse_sql

        for x in parse_sql(sql_text):
            if x["op"] != "insert":
                continue
            table, row = x["table"], x["row"]
            for col in ID_COLS:
                if row.get(col) not in (None, ""):
                    self.rows.setdefault(str(row[col]), []).append((table, row))
            if (
                table == "slack.slack_messages"
                and row.get("channel_id")
                and row.get("ts")
            ):
                self.slack[(str(row["channel_id"]), str(row["ts"]))] = row
            if table == "trello.trello_checklists" and row.get("idCard"):
                self.checklist_card[str(row["id"])] = str(row["idCard"])

    @staticmethod
    def _slack_key(row: dict) -> str:
        root = row.get("thread_ts_legacy") or row.get("ts")
        return f"slack:{row['channel_id']}/{root}"

    def _from_row(self, table: str, row: dict):
        svc = table.split(".")[0]
        if table == "slack.slack_messages":
            return self._slack_key(row) if row.get("channel_id") else None
        if table == "gmail.gmail_messages":
            return f"gmail:{row['thread_id']}" if row.get("thread_id") else None
        if table == "gmail.gmail_threads":
            return f"gmail:{row['id']}"
        if table in FILE_TABLES:
            v = row.get(FILE_TABLES[table])
            return f"file:{v}" if v else None
        if table == "gcal.gcal_events":
            return f"gcal:{row.get('ical_uid') or row.get('event_id')}"
        if table == "trello.trello_cards":
            return f"trello:{row['id']}"
        if table in ("trello.trello_actions", "trello.trello_checklists"):
            return f"trello:{row['idCard']}" if row.get("idCard") else None
        if table == "trello.trello_check_items":
            card = self.checklist_card.get(str(row.get("idChecklist")))
            return f"trello:{card}" if card else None
        if table == "linear.linear_comments":
            return f"linear:{row['issue_id']}" if row.get("issue_id") else None
        if table == "linear.linear_issues":
            return f"linear:{row.get('identifier') or row['id']}"
        if svc == "github":
            if row.get("pr_id"):
                return f"github:{row['pr_id']}"
            return (
                f"github:{row['id']}"
                if table == "github.github_pull_requests"
                else None
            )
        if svc == "confluence":
            if table == "confluence.confluence_pages":
                return f"confluence:{row['id']}"
            return f"confluence:{row['page_id']}" if row.get("page_id") else None
        return None

    def container(self, pointer, override=None):
        """Container key for a record id or base pointer, or None when it cannot be derived."""
        if override:
            return str(override)
        if not pointer:
            return None
        rid = str(pointer).strip()
        m = re.match(
            r"^(slack|gmail|gdocs|gdrive|gsheets|gslides|gcal|trello|linear|github|confluence|snowflake)"
            r":(.+)$",
            rid,
        )
        svc, rid = (m.group(1), m.group(2).strip()) if m else (None, rid)
        if svc == "snowflake":
            return f"snowflake:{rid.split()[0].upper()}"
        s = SLACK_ID.match(rid)
        if s:
            row = self.slack.get((s.group(1), s.group(2)))
            return self._slack_key(row) if row else None
        for table, row in self.rows.get(rid, []):
            key = self._from_row(table, row)
            if key:
                return key
        if LINEAR_KEY.match(rid) and svc in (None, "linear"):
            return f"linear:{rid}"
        if "#" in rid and svc in (None, "github"):
            repo, _, rest = rid.partition("#")
            return f"github:{repo}#{rest.split('#')[0]}" if rest else None
        if GMAIL_THREAD.match(rid) and svc in (None, "gmail"):
            return f"gmail:{rid}"
        if re.match(r"^[fd]_[0-9a-f]{6,}$", rid):
            return f"file:{rid}"
        return None


def _record_pointer(v: dict):
    return v.get("id") or v.get("base_pointer")


# ------------------------------------------------------------------ the checks


def _same_place(man: dict, ov: Overlay, rep: dict) -> None:
    anchors = {}
    for a in man.get("anchors") or []:
        key = ov.container(a.get("locator"))
        if key:
            anchors[key] = a.get("id")
    delegated_by = {}
    for f in man.get("ask_fragments") or []:
        for sid in f.get("seeded_ids") or []:
            if f.get("delegated_by_record"):
                delegated_by.setdefault(str(sid), set()).add(
                    str(f["delegated_by_record"])
                )

    def path(rid) -> dict:
        """Containers of every record that delegates to rid, transitively: {container: delegating record}."""
        out, seen, todo = {}, set(), [str(rid)]
        while todo:
            cur = todo.pop()
            for parent in delegated_by.get(cur, ()):
                if parent in seen:
                    continue
                seen.add(parent)
                key = ov.container(parent)
                if key:
                    out.setdefault(key, parent)
                todo.append(parent)
        return out

    judged = 0
    for t in man.get("traps") or []:
        versions = [v for v in t.get("version_records") or [] if isinstance(v, dict)]
        if len(versions) < 2:
            continue
        judged += 1
        tid = t.get("id")
        *earlier, newest = versions
        corr = ov.container(_record_pointer(newest), newest.get("container"))
        olds = [
            (v, ov.container(_record_pointer(v), v.get("container"))) for v in earlier
        ]
        node = {"correction": corr, "earlier": [k for _, k in olds]}
        hit = None
        if corr:
            same = [k for _, k in olds if k and k == corr]
            if same:
                hit = (
                    "same_container",
                    f"the correction and a superseded version share {corr}",
                )
            elif corr in anchors:
                hit = (
                    "first_read",
                    f"the correction sits in {corr}, the container of anchor {anchors[corr]}",
                )
            else:
                for v, _ in olds:
                    via = path(_record_pointer(v))
                    if corr in via:
                        hit = (
                            "on_delegation_path",
                            f"the correction sits in {corr}, which holds {via[corr]}, the "
                            f"record that delegates to the superseded {_record_pointer(v)}",
                        )
                        break
        if hit:
            node["same_place"] = "FLAG"
            rep["flags"].append(
                {"check": "SAME_PLACE", "node": tid, "kind": hit[0], "detail": hit[1]}
            )
        elif corr is None or any(k is None for _, k in olds):
            node["same_place"] = "UNRESOLVED"
            missing = [_record_pointer(newest)] if corr is None else []
            missing += [_record_pointer(v) for v, k in olds if k is None]
            for p in missing:
                rep["unresolved"].append(
                    {
                        "check": "SAME_PLACE",
                        "node": tid,
                        "pointer": p,
                        "reason": "container not derivable from the SQL overlay or the id; read it "
                        "through tools/hg.py or declare version_records[].container",
                    }
                )
        else:
            node["same_place"] = "CLEAN"
        rep["nodes"][tid] = node
    st = [n["same_place"] for n in rep["nodes"].values()]
    rep["checks"]["SAME_PLACE"] = (
        "SKIP"
        if not judged
        else "FLAG"
        if "FLAG" in st
        else "UNRESOLVED"
        if "UNRESOLVED" in st
        else "CLEAN"
    )
    rep["details"]["SAME_PLACE"] = (
        f"{judged} trap(s) with two or more version records; "
        f"{st.count('FLAG')} flagged, {st.count('UNRESOLVED')} unresolved"
    )


def _mechanisms(man: dict) -> set:
    out = {
        str(p.get("mechanism"))
        for p in man.get("mechanism_portfolio") or []
        if isinstance(p, dict)
    }
    out |= {
        str(c.get("root_cause")) for c in man.get("chains") or [] if isinstance(c, dict)
    }
    out |= {
        str(t.get("mechanism"))
        for t in man.get("traps") or []
        if isinstance(t, dict) and t.get("mechanism")
    }
    return out


def _families(man: dict) -> set:
    return {str(t.get("family")) for t in man.get("traps") or [] if isinstance(t, dict)}


def _flag_if(rep, name, bad, node, detail_bad, detail_ok):
    rep["checks"][name] = "FLAG" if bad else "CLEAN"
    rep["details"][name] = detail_bad if bad else detail_ok
    if bad:
        rep["flags"].append(
            {"check": name, "node": node, "kind": None, "detail": detail_bad}
        )


def _design_checks(man: dict, rep: dict) -> None:
    mech, fam = _mechanisms(man), _families(man)
    _flag_if(
        rep,
        "DONE_CHECK",
        not ("A24" in mech or "done_gap" in fam),
        None,
        "no A24 rule, chain root or done_gap trap: no source says 'done' while another service shows a "
        "required piece missing (v2's costliest trap)",
        "an A24 / done_gap node exists",
    )
    _flag_if(
        rep,
        "FILTER_CHECK",
        not ({"exact_predicate", "near_miss_mention"} & fam or "A17" in mech),
        None,
        "no exact_predicate / near_miss_mention trap and no A17 rule: the obvious search returns every in-scope "
        "item, so the list is volume only",
        "an in-scope item sits outside the obvious filter",
    )
    services = {}
    for t in man.get("traps") or []:
        if isinstance(t, dict):
            services[t.get("id")] = set(t.get("services") or [])
    for c in man.get("chains") or []:
        if isinstance(c, dict):
            services[c.get("id")] = {
                h.get("service") for h in c.get("hops") or [] if isinstance(h, dict)
            }
    cross = {}
    for p in man.get("mechanism_portfolio") or []:
        if not isinstance(p, dict):
            continue
        svc = (
            set().union(*(services.get(n, set()) for n in p.get("nodes") or []))
            if p.get("nodes")
            else set()
        )
        if len(svc - {None}) >= 2 and p.get("requirement"):
            cross.setdefault(p["requirement"], []).append(p.get("id"))
    _flag_if(
        rep,
        "TWO_DECISIONS",
        len(cross) < 2,
        None,
        f"{len(cross)} requirement(s) decided by a cross-source rule ({cross or 'none'}); need two separate "
        f"decisions that each need checking across sources",
        f"cross-source rules decide {len(cross)} requirements: {cross}",
    )


def _surface_checks(man: dict, surface, rep: dict) -> None:
    port = [
        p
        for p in man.get("mechanism_portfolio") or []
        if isinstance(p, dict) and p.get("id")
    ]
    if not isinstance(surface, dict) or not isinstance(surface.get("slots"), list):
        for name in ("DECISION_FLIP", "INPUT_CHECK"):
            rep["checks"][name] = "SKIP"
            rep["details"][name] = (
                "no gradable surface (Working_Files/01_Gradable_Surface.json)"
            )
        return
    slots = [s for s in surface["slots"] if isinstance(s, dict)]

    def movers(s) -> set:
        out = set(map(str, s.get("mechanisms") or []))
        fb = s.get("flipped_by")
        if isinstance(fb, dict):
            out |= set(map(str, fb))
        elif isinstance(fb, (list, tuple)):
            out |= set(map(str, fb))
        elif fb:
            out.add(str(fb))
        return out

    if not port:
        rep["checks"]["DECISION_FLIP"] = "SKIP"
        rep["details"]["DECISION_FLIP"] = "no mechanism_portfolio"
    else:
        weak = []
        for p in port:
            weights = [s.get("weight") for s in slots if p["id"] in movers(s)]
            if 5 not in weights:
                weak.append(p["id"])
                rep["flags"].append(
                    {
                        "check": "DECISION_FLIP",
                        "node": p["id"],
                        "kind": None,
                        "detail": f"rule {p['id']} ({p.get('mechanism')}) can flip slots of weight "
                        f"{sorted(set(w for w in weights if w)) or 'none'}, no weight-5 slot",
                    }
                )
        rep["checks"]["DECISION_FLIP"] = "FLAG" if weak else "CLEAN"
        rep["details"]["DECISION_FLIP"] = (
            f"{len(port) - len(weak)} of {len(port)} rules can flip a weight-5 slot"
            + (f"; not: {weak}" if weak else "")
        )
    totals = [
        s for s in slots if s.get("class") == "aggregate" and s.get("weight") == 5
    ]
    clean = [s.get("id") for s in totals if not movers(s)]
    for sid in clean:
        rep["flags"].append(
            {
                "check": "INPUT_CHECK",
                "node": sid,
                "kind": None,
                "detail": f"weight-5 total {sid} has no rule or mutant that changes its inputs",
            }
        )
    rep["checks"]["INPUT_CHECK"] = "FLAG" if clean else "CLEAN"
    rep["details"]["INPUT_CHECK"] = (
        f"{len(totals)} weight-5 total(s); {len(totals) - len(clean)} with an input a "
        f"rule can change"
    )


def _words(text: str) -> list:
    return re.findall(r"[a-z0-9_]+", re.sub(r"['\u2019]s\b", "", str(text).lower()))


def _prompt_check(man: dict, prompt: str, rep: dict) -> None:
    if not prompt.strip():
        rep["checks"]["RULE_IN_PROMPT"] = "SKIP"
        rep["details"]["RULE_IN_PROMPT"] = "no prompt (04_Prompt.txt) yet"
        return
    pw = _words(prompt)
    grams = {tuple(pw[i : i + PROMPT_SPAN]) for i in range(len(pw) - PROMPT_SPAN + 1)}
    hits = []
    for t in man.get("traps") or []:
        if not isinstance(t, dict):
            continue
        rw = _words(t.get("resolver") or "")
        for i in range(len(rw) - PROMPT_SPAN + 1):
            g = tuple(rw[i : i + PROMPT_SPAN])
            if g in grams:
                hits.append(t.get("id"))
                rep["flags"].append(
                    {
                        "check": "RULE_IN_PROMPT",
                        "node": t.get("id"),
                        "kind": None,
                        "detail": f"the prompt repeats the resolver words '{' '.join(g)}'",
                    }
                )
                break
    rep["checks"]["RULE_IN_PROMPT"] = "FLAG" if hits else "CLEAN"
    rep["details"]["RULE_IN_PROMPT"] = (
        f"{len(hits)} trap resolver(s) stated in the prompt"
        if hits
        else f"no run of {PROMPT_SPAN} resolver words in the prompt"
    )


def run(man: dict, sql_text: str = "", prompt: str = "", surface=None) -> dict:
    man = man if isinstance(man, dict) else {}
    rep = {
        "tool": "hardness_v2_check",
        "label": LABEL,
        "checks": {},
        "details": {},
        "flags": [],
        "unresolved": [],
        "nodes": {},
    }
    _same_place(man, Overlay(sql_text or ""), rep)
    _design_checks(man, rep)
    _surface_checks(man, surface, rep)
    _prompt_check(man, prompt or "", rep)
    rep["checks"] = {k: rep["checks"][k] for k in CHECKS}
    return rep


def to_text(rep: dict) -> str:
    lines = [rep["label"], ""]
    for name in CHECKS:
        lines.append(
            f"  {rep['checks'][name]:<10} {name:<15} {rep['details'].get(name, '')}  [{PART[name]}]"
        )
    if rep["flags"]:
        lines += [
            "",
            "Flags (each needs a written disposition; redesign the difficulty, never weaken a fairness link "
            "or raise a weight):",
        ]
        for f in rep["flags"]:
            kind = f" ({f['kind']})" if f.get("kind") else ""
            lines.append(f"  {f['check']} {f['node'] or '-'}{kind}: {f['detail']}")
    if rep["unresolved"]:
        lines += ["", "Unresolved (never a pass):"]
        lines += [
            f"  {u['check']} {u['node']}: {u['pointer']} - {u['reason']}"
            for u in rep["unresolved"]
        ]
    return "\n".join(lines)


# ------------------------------------------------------------------ self-test and CLI


def _self_test() -> None:
    ch = "C0SELFTEST1"
    sql = (
        f"INSERT INTO slack.slack_messages (id, ts, channel_id, text, thread_ts_legacy) VALUES "
        f"('p', '1700000000.000100', '{ch}', 'see the doc', '1700000000.000100');\n"
        "INSERT INTO gmail.gmail_messages (id, thread_id, user_email, body_text) VALUES "
        "('u@x.co/<a@x>', 'u@x.co/1', 'u@x.co', 'method in the doc');\n"
        "INSERT INTO gmail.gmail_messages (id, thread_id, user_email, body_text) VALUES "
        "('u@x.co/<b@x>', 'u@x.co/1', 'u@x.co', 'one change');\n"
        "INSERT INTO gdocs.docs_documents (document_id, title, body_text) VALUES ('f_abcdef1', 'Method', 'old');\n"
        "INSERT INTO trello.trello_actions (id, type, \"idCard\") VALUES ('a1', 'createCard', 'card9');\n"
        "INSERT INTO trello.trello_actions (id, type, \"idCard\") VALUES ('a2', 'updateCard', 'card9');\n"
    )
    man = {
        "anchors": [{"id": "A1", "locator": f"{ch}/1700000000.000100"}],
        "ask_fragments": [
            {
                "id": "K1",
                "delegated_by_record": f"{ch}/1700000000.000100",
                "seeded_ids": ["u@x.co/<a@x>"],
            },
            {
                "id": "K2",
                "delegated_by_record": "u@x.co/<a@x>",
                "seeded_ids": ["f_abcdef1"],
            },
        ],
        "traps": [
            {
                "id": "T1",
                "family": "superseding",
                "services": ["gdocs", "gmail"],
                "version_records": [
                    {"service": "gdocs", "id": "f_abcdef1"},
                    {"service": "gmail", "id": "u@x.co/<b@x>"},
                ],
            },
            {
                "id": "T2",
                "family": "superseding",
                "services": ["trello"],
                "version_records": [
                    {"service": "trello", "id": "a1"},
                    {"service": "trello", "id": "a2"},
                ],
            },
            {
                "id": "T3",
                "family": "superseding",
                "services": ["gmail"],
                "version_records": [
                    {"service": "gdocs", "id": "f_abcdef1"},
                    {"service": "gmail", "id": "nobody@x.co/<z@x>"},
                ],
            },
        ],
    }
    rep = run(man, sql)
    kinds = {f["node"]: f["kind"] for f in rep["flags"] if f["check"] == "SAME_PLACE"}
    assert kinds == {"T1": "on_delegation_path", "T2": "same_container"}, kinds
    assert (
        rep["nodes"]["T3"]["same_place"] == "UNRESOLVED"
        and rep["checks"]["SAME_PLACE"] == "FLAG"
    ), rep["nodes"]
    assert (
        rep["checks"]["DONE_CHECK"] == "FLAG"
        and rep["checks"]["DECISION_FLIP"] == "SKIP"
    ), rep["checks"]
    print(
        "self-test: ok (same_container, on_delegation_path, UNRESOLVED never clean, done check, surface SKIP)"
    )


def main(argv) -> int:
    ap = argparse.ArgumentParser(
        prog="hardness_v2_check.py",
        description="advisory Hardness v2 self-checks (see docstring)",
    )
    ap.add_argument("--task-dir", type=Path)
    ap.add_argument("--manifest", type=Path)
    ap.add_argument("--sql", type=Path)
    ap.add_argument("--prompt", type=Path)
    ap.add_argument("--surface", type=Path)
    ap.add_argument("--design", action="store_true", help="no SQL yet (scenario stage)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument(
        "--strict",
        action="store_true",
        help="exit 1 when a check is FLAG or UNRESOLVED",
    )
    ap.add_argument("--self-test", action="store_true")
    a = ap.parse_args(argv)
    if a.self_test:
        _self_test()
        return 0
    td = a.task_dir
    wf = td / "Working_Files" if td else None
    names = (
        ("01_Hardness_Manifest.draft.json", "01_Hardness_Manifest.json")
        if a.design
        else ("01_Hardness_Manifest.json", "01_Hardness_Manifest.draft.json")
    )
    man = a.manifest or (
        next((wf / n for n in names if (wf / n).is_file()), None) if wf else None
    )
    sql = (
        None if a.design else (a.sql or (td / "01_Universe_Inject.sql" if td else None))
    )
    prompt = a.prompt or (td / "04_Prompt.txt" if td else None)
    surface = a.surface or (wf / "01_Gradable_Surface.json" if wf else None)
    if (
        not man
        or not Path(man).is_file()
        or (sql is not None and not Path(sql).is_file())
    ):
        print(
            "hardness_v2_check: need --manifest (or --task-dir) and, unless --design, an existing --sql",
            file=sys.stderr,
        )
        return 2
    rep = run(
        json.loads(Path(man).read_text()),
        Path(sql).read_text() if sql else "",
        Path(prompt).read_text() if prompt and Path(prompt).is_file() else "",
        json.loads(Path(surface).read_text())
        if surface and Path(surface).is_file()
        else None,
    )
    rep.update(
        manifest=str(man),
        sql=str(sql) if sql else None,
        prompt=str(prompt) if prompt and Path(prompt).is_file() else None,
        surface=str(surface) if surface and Path(surface).is_file() else None,
        design=a.design,
    )
    print(json.dumps(rep, indent=1, ensure_ascii=False) if a.json else to_text(rep))
    if a.strict and any(v in ("FLAG", "UNRESOLVED") for v in rep["checks"].values()):
        return 1
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (ValueError, KeyError, json.JSONDecodeError) as error:
        print(f"hardness_v2_check: {error}", file=sys.stderr)
        raise SystemExit(2)
