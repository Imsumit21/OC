#!/usr/bin/env python3
"""Base-claims coherence: what injected text says about base git branches must agree with base git + #builds.

`base_check.py` proves ids, references and dates; it never reads the base git repositories. `/prompt`'s
Cross-Service Coherence (Eval 1 §3.2) does: it opens the exported repos and runs `git branch --contains`, and a
seeded note whose branch claim the history contradicts is a count-changing FAIL (dd-2024-release-cost rev2,
/prompt attempt 6ae4e29de73a5c2bb1a35a1a: 14 pick notes off-branch, lava_fix_3 picks dated before the branch
existed). This gate runs the same reading before the Portal does.

Every release branch named in injected text (`release/<x>`, or a bare distinctive suffix such as `lava_fix_3`) is
checked against the base, read-only:

  B1 FAIL  the branch does not exist in any exported repo
  B2 FAIL  the record is dated before the branch existed (window start = first #builds build of the branch or
           its first commit not on develop, whichever is earlier)
  B3 FAIL  a positive pick claim ("picked onto / cherry-picked onto / going out on / landed on / moved the pick
           to <branch>") is dated after the branch's window closed (last #builds build or head commit, + 3 days)
  B4 FAIL  the ticket the claim is about has commits naming it (or, for a PR comment, the PR's commits) and
           none of them is on the claimed branch — `git branch --contains` disagrees with the note
  B4' WARN the same for a backed-out mention ("reverted from X", "the earlier X pick was taken off"): base git
           shows no pick on X either. Prefer putting backed-out stories on tickets with no commits.
  INFO     claims about tickets with no commit naming them can only be date-checked

The claim's subject is the last ENG id named in the same clause before the branch, else the record's own ticket
(Linear issue_id; the PR's title/head ref/body for a PR comment; a Slack GitHub-bot attachment's PR). Train-map
style text with no ticket is checked for B1/B2 only; a Trello updateCard's `old.desc` is dated by the previous
action on that card.

Usage: base_claims.py <injection.sql> [--json] [--task-dir DIR] | --self-test
Exit 0 on PASS, 1 on FAIL, 2 on usage/context errors. Read-only: runs `git` with read commands only.
"""

from __future__ import annotations

import datetime as dt
import glob
import json
import re
import subprocess
import sys
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from task_context import v2_export_root  # noqa: E402

BUNDLE = Path(__file__).resolve().parent.parent
WS = BUNDLE.parent
OTHER = v2_export_root("Other_Services", WS) / "Services_Data"
GITHUB = v2_export_root("GitHub", WS) / "Services_Data" / "github" / "data.json"
GMAIL = v2_export_root("Gmail", WS) / "Services_Data" / "gmail"
CLOCK = dt.datetime(2026, 2, 14, tzinfo=dt.timezone.utc)
DATA_CLOCK = CLOCK
BUILDS_CHANNEL = "C05433XK267"
END_GRACE = dt.timedelta(days=3)
UTC = dt.timezone.utc

BRANCH_RX = re.compile(r"(?<![\w/.-])(release/[A-Za-z0-9_.\-]*[A-Za-z0-9_])")
TICKET_RX = re.compile(r"\b(ENG-\d+)\b")
BACKED_PREV = re.compile(
    r"(earlier|sat on|had been on|been on|taken off|\boff|reverted from|backed out from|"
    r"removed from|pulled from|from)\s*$",
    re.I,
)
BACKED_NEXT = re.compile(
    r"^\W{0,3}\s*(first\b|until\b|but\b|pick (was|got)\b|was (taken off|reverted|backed out|"
    r"pulled)|got (taken off|reverted|backed out|pulled))",
    re.I,
)
POSITIVE_PREV = re.compile(
    r"(picked onto|picked to|cherry-picked onto|cherry-picked to|moved the pick to|going out on|"
    r"goes out on|landed on|now on|went in on|in on|on|onto)\s*$",
    re.I,
)
NEGATION = re.compile(
    r"\b(never|didn't|did not|doesn't|does not|wasn't|was not|isn't|not picked|no pick)\b",
    re.I,
)


# ---------------------------------------------------------------- time helpers


def _ts(v) -> dt.datetime | None:
    if v in (None, "", "NULL"):
        return None
    s = str(v).strip()
    try:
        if re.fullmatch(r"\d{9,10}(\.\d+)?", s):
            return dt.datetime.fromtimestamp(float(s), UTC)
        s = s.replace("Z", "+00:00")
        if re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}(\.\d+)?\+\d{2}", s):
            s += ":00"
        t = dt.datetime.fromisoformat(s.replace(" ", "T", 1))
        return t if t.tzinfo else t.replace(tzinfo=UTC)
    except ValueError:
        return None


def _d(t):
    return t.date().isoformat() if t else "?"


# ---------------------------------------------------------------- base: git + #builds


def _git(repo: Path, *args) -> str:
    r = subprocess.run(["git", "-C", str(repo), *args], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def repos(root: Path) -> list[Path]:
    return sorted(p.parent for p in root.glob("*/*/.git")) + sorted(
        p
        for p in root.glob("*/*")
        if (p / "HEAD").is_file() and (p / "objects").is_dir()
    )


class Base:
    def __init__(self, gh_root: Path, slack_messages: Path, data_json: Path | None):
        self.repos = [r for r in repos(gh_root)]
        self.branch_repos: dict[str, list[Path]] = defaultdict(list)
        for r in self.repos:
            for name in _git(
                r, "for-each-ref", "--format=%(refname:short)", "refs/heads"
            ).split():
                if name.startswith("release/"):
                    self.branch_repos[name].append(r)
        self.builds = self._builds(slack_messages)
        self.prs = {}
        self.pr_commits = defaultdict(set)
        if data_json and data_json.is_file():
            d = json.loads(data_json.read_text())
            for p in d.get("pull_requests", []):
                self.prs[p["id"]] = p
            for c in d.get("pull_request_commits", []):
                self.pr_commits[c["pr_id"]].add(c["commit_sha"])

    @staticmethod
    def _builds(msgs: Path) -> dict:
        out = defaultdict(list)
        for f in glob.glob(str(msgs / BUILDS_CHANNEL / "*.json")):
            try:
                rows = json.loads(Path(f).read_text())
            except ValueError:
                continue
            for m in rows:
                for a in m.get("attachments") or []:
                    r = re.search(
                        r" - #\d+ - (\S+) ",
                        (a.get("fallback") or "").split("\n")[0] + " ",
                    )
                    if r and r.group(1).startswith("release/"):
                        out[r.group(1)].append(
                            dt.datetime.fromtimestamp(float(m["ts"]), UTC)
                        )
        return out

    @lru_cache(maxsize=None)
    def window(self, branch: str):
        """(start, end, evidence) for a release branch across the repos that have it."""
        starts, ends, ev = [], [], []
        b = self.builds.get(branch)
        if b:
            starts.append(min(b))
            ends.append(max(b))
            ev.append(f"#builds {_d(min(b))}..{_d(max(b))} ({len(b)})")
        for r in self.branch_repos.get(branch, []):
            own = _git(r, "log", branch, "--not", "develop", "--format=%cI").split()
            head = _git(r, "log", "-1", branch, "--format=%cI").strip()
            if own:
                starts.append(min(_ts(x) for x in own))
                ev.append(f"{r.name} first own commit {_d(min(_ts(x) for x in own))}")
            if head:
                ends.append(_ts(head))
                ev.append(f"{r.name} head {head[:10]}")
        return (
            min(starts) if starts else None,
            max(ends) if ends else None,
            "; ".join(ev),
        )

    @lru_cache(maxsize=None)
    def reachable(self, repo: Path, branch: str) -> frozenset:
        return frozenset(_git(repo, "rev-list", branch).split())

    @lru_cache(maxsize=None)
    def ticket_index(self, repo: Path) -> dict:
        idx = defaultdict(set)
        for line in _git(repo, "log", "--all", "--format=%H%x1f%s%x1f%b%x1e").split(
            "\x1e"
        ):
            parts = line.strip().split("\x1f")
            if len(parts) >= 2:
                for t in TICKET_RX.findall(" ".join(parts[1:])):
                    idx[t].add(parts[0])
        return idx

    def commits_for(self, ticket: str, branch: str, extra: set) -> dict:
        """repo -> commits that name the ticket (plus explicit PR commits) in repos that have the branch."""
        out = {}
        for r in self.branch_repos.get(branch, []):
            cs = set(self.ticket_index(r).get(ticket, set())) | {c for c in extra if c}
            known = {c for c in cs if _git(r, "cat-file", "-t", c).strip() == "commit"}
            if known:
                out[r] = known
        return out


# ---------------------------------------------------------------- SQL → text-bearing records


def _json(v):
    if isinstance(v, (dict, list)):
        return v
    try:
        return json.loads(v) if v not in (None, "", "NULL") else None
    except (TypeError, ValueError):
        return None


def records(stmts, base: Base) -> list[dict]:
    """(where, date, text, ticket, pr_commits) for every text-bearing injected row."""
    out = []
    trello_actions = defaultdict(list)
    for s in stmts:
        if s["op"] != "insert":
            continue
        t, r, ln = s["table"], s["row"], s["line"]
        if t == "linear.linear_comments":
            out.append(
                dict(
                    line=ln,
                    where=f"linear comment on {r.get('issue_id')}",
                    date=_ts(r.get("created_at")),
                    text=r.get("body") or "",
                    ticket=r.get("issue_id"),
                    extra=set(),
                )
            )
        elif t == "github.github_pr_comments":
            pr = base.prs.get(r.get("pr_id"), {})
            tix = TICKET_RX.findall(
                " ".join(str(pr.get(k) or "") for k in ("title", "head_ref", "body"))
            )
            extra = set(base.pr_commits.get(r.get("pr_id"), set())) | {
                pr.get("head_sha")
            }
            out.append(
                dict(
                    line=ln,
                    where=f"PR comment {r.get('id')}",
                    date=_ts(r.get("created_at")),
                    text=r.get("body") or "",
                    ticket=tix[0] if tix else None,
                    extra=extra,
                )
            )
        elif t == "slack.slack_messages":
            text, tix, extra = r.get("text") or "", None, set()
            for a in _json(r.get("attachments_json")) or []:
                text += " " + " ".join(str(a.get(k) or "") for k in ("text", "pretext"))
                m = re.search(r"/pull/(\d+)", str(a.get("title") or ""))
                tt = TICKET_RX.findall(str(a.get("title") or ""))
                if m:
                    repo = re.search(
                        r"github\.com/([^/]+/[^/]+)/pull", str(a.get("title") or "")
                    )
                    pid = f"{repo.group(1)}#{m.group(1)}" if repo else None
                    pr = base.prs.get(pid, {})
                    extra |= set(base.pr_commits.get(pid, set())) | {pr.get("head_sha")}
                    tt = tt or TICKET_RX.findall(
                        " ".join(
                            str(pr.get(k) or "") for k in ("title", "head_ref", "body")
                        )
                    )
                tix = tix or (tt[0] if tt else None)
            out.append(
                dict(
                    line=ln,
                    where=f"slack {r.get('id')}",
                    date=_ts(r.get("ts") or r.get("created_at")),
                    text=text,
                    ticket=tix,
                    extra=extra,
                )
            )
        elif t == "trello.trello_cards":
            out.append(
                dict(
                    line=ln,
                    where=f"trello card {r.get('id')}",
                    date=_ts(r.get("dateLastActivity")),
                    text=r.get("desc") or "",
                    ticket=None,
                    extra=set(),
                    current=True,
                )
            )
        elif t == "trello.trello_actions":
            trello_actions[r.get("idCard")].append((_ts(r.get("date")), ln, r))
        elif t == "trello.trello_check_items":
            m = TICKET_RX.search(r.get("name") or "")
            out.append(
                dict(
                    line=ln,
                    where=f"trello check item {r.get('id')}",
                    date=None,
                    text=r.get("name") or "",
                    ticket=m.group(1) if m else None,
                    extra=set(),
                )
            )
        else:
            for col in (
                "body_text",
                "content_text",
                "body",
                "text",
                "description",
                "desc",
                "notes",
                "grid_json",
            ):
                if r.get(col):
                    out.append(
                        dict(
                            line=ln,
                            where=f"{t} {r.get('id') or r.get('document_id') or ''}".strip(),
                            date=_ts(
                                r.get("created_at")
                                or r.get("created_time")
                                or r.get("date")
                                or r.get("created")
                                or r.get("internal_date")
                            ),
                            text=str(r[col]),
                            ticket=None,
                            extra=set(),
                        )
                    )
    for card, acts in trello_actions.items():
        acts.sort(key=lambda a: a[0] or dt.datetime.min.replace(tzinfo=UTC))
        prev = None
        for when, ln, r in acts:
            data = _json(r.get("data_json")) or {}
            desc = (data.get("card") or {}).get("desc")
            text = data.get("text")
            for body, at in (
                (desc, when),
                (text, when),
                ((data.get("old") or {}).get("desc"), prev),
            ):
                if body:
                    out.append(
                        dict(
                            line=ln,
                            where=f"trello action {r.get('id')}",
                            date=at,
                            text=body,
                            ticket=None,
                            extra=set(),
                        )
                    )
            prev = when
    return out


# ---------------------------------------------------------------- claims


def mentions(text: str, known: set) -> list[tuple[int, str]]:
    found = [(m.start(), m.group(1)) for m in BRANCH_RX.finditer(text)]
    taken = {p for p, _ in found}
    suffixes = {
        b.split("/", 1)[1]: b for b in known if re.search(r"[_\-]", b.split("/", 1)[1])
    }
    for suf, full in suffixes.items():
        for m in re.finditer(rf"(?<![\w/.-]){re.escape(suf)}(?![\w-])", text):
            if m.start() not in taken and not text[
                max(0, m.start() - 8) : m.start()
            ].endswith("release/"):
                found.append((m.start(), full))
    return sorted(found)


def classify(text: str, pos: int, branch: str) -> str:
    clause_start = max(text.rfind(c, 0, pos) for c in ".;:(") + 1
    prev = text[clause_start:pos]
    nxt = text[pos + len(branch) : pos + len(branch) + 40]
    if BACKED_PREV.search(prev[-30:]) or BACKED_NEXT.search(nxt):
        return "backed"
    if NEGATION.search(prev) and not POSITIVE_PREV.search(prev[-25:]):
        return "negated"
    return (
        "positive"
        if POSITIVE_PREV.search(prev[-25:]) or re.match(r"\W{0,3}\s*(it is|->)", nxt)
        else "mention"
    )


def subject(text: str, pos: int, default):
    clause_start = max(text.rfind(c, 0, pos) for c in ".;") + 1
    tix = TICKET_RX.findall(text[clause_start:pos])
    return tix[-1] if tix else default


def check(sql: str, base: Base) -> dict:
    from base_check import parse_sql

    stmts = parse_sql(sql)
    known = set(base.branch_repos)
    # branches the SQL names: the only ones worth listing in "git shows them on …"
    mentioned = {br for rec in records(stmts, base) for _, br in mentions(rec["text"], known)} & known
    fails, warns, infos, claims = [], [], [], 0
    windows = {}
    for rec in records(stmts, base):
        for pos, br in mentions(
            rec["text"], known | set(BRANCH_RX.findall(rec["text"]))
        ):
            claims += 1
            where = f"L{rec['line']} {rec['where']}"
            quote = rec["text"][max(0, pos - 60) : pos + len(br) + 40].replace(
                "\n", " "
            )
            if br not in known:
                fails.append(
                    f'B1 {where}: names {br}, which no exported repo has — "…{quote}…"'
                )
                continue
            start, end, ev = base.window(br)
            windows[br] = f"{_d(start)}..{_d(end)} ({ev})"
            kind = classify(rec["text"], pos, br)
            if rec["date"] and start and rec["date"] < start - dt.timedelta(hours=12):
                fails.append(
                    f"B2 {where} ({_d(rec['date'])}): names {br} before it existed (window starts "
                    f'{_d(start)}) — "…{quote}…"'
                )
            subj = subject(rec["text"], pos, rec["ticket"])
            if (
                kind == "positive"
                and subj == rec["ticket"]
                and rec["date"]
                and end
                and rec["date"] > end + END_GRACE
            ):
                fails.append(
                    f"B3 {where} ({_d(rec['date'])}): pick onto {br} after its window closed ({_d(end)}) — "
                    f'"…{quote}…"'
                )
            if kind in ("positive", "backed") and subj:
                extra = rec["extra"] if subj == rec["ticket"] else set()
                cs = base.commits_for(subj, br, extra)
                if not cs:
                    infos.append(
                        f"{where}: {subj} → {br} ({kind}) has no commit naming it; date-checked only"
                    )
                    continue
                on = any(c in base.reachable(r, br) for r, cc in cs.items() for c in cc)
                if not on:
                    shown = sorted(
                        {
                            b
                            for r, cc in cs.items()
                            for b in mentioned
                            if r in base.branch_repos.get(b, [])
                            and any(c in base.reachable(r, b) for c in cc)
                        }
                    )
                    msg = (
                        f"{where}: {subj}'s commits ({', '.join(sorted(c[:8] for cc in cs.values() for c in cc))}) "
                        f'are not on {br}; git shows them on {shown or "no release branch"} — "…{quote}…"'
                    )
                    (fails if kind == "positive" else warns).append(
                        ("B4 " if kind == "positive" else "B4' ") + msg
                    )
    verdict = "PASS" if not fails else "FAIL"
    return {
        "verdict": verdict,
        "claims": claims,
        "fail": fails,
        "warn": warns,
        "info_count": len(infos),
        "info": infos[:40],
        "windows": windows,
    }


def to_text(r: dict) -> str:
    out = [
        f"BASE CLAIMS (injected text vs base git + #builds): {r['verdict']} · {r['claims']} branch mentions · "
        f"{len(r['fail'])} fail · {len(r['warn'])} warn · {r['info_count']} date-only"
    ]
    out += ["branch windows:"] + [
        f"  {b}: {w}" for b, w in sorted(r["windows"].items())
    ]
    out += [f"FAIL {f}" for f in r["fail"]] + [f"WARN {w}" for w in r["warn"]]
    return "\n".join(out)


def base_from_context() -> Base:
    gh_root = Path(GITHUB).parent / "root"
    return Base(gh_root, Path(OTHER) / "slack" / "messages", Path(GITHUB))


# ---------------------------------------------------------------- self-test


def _self_test() -> None:
    import os
    import tempfile

    tmp = Path(tempfile.mkdtemp())
    repo = tmp / "gh" / "root" / "org" / "Game"
    repo.mkdir(parents=True)
    env = dict(
        os.environ,
        GIT_AUTHOR_NAME="t",
        GIT_AUTHOR_EMAIL="t@t",
        GIT_COMMITTER_NAME="t",
        GIT_COMMITTER_EMAIL="t@t",
    )

    def g(*a, date=None):
        e = dict(env)
        if date:
            e["GIT_AUTHOR_DATE"] = e["GIT_COMMITTER_DATE"] = date
        subprocess.run(
            ["git", "-C", str(repo), *a], check=True, capture_output=True, env=e
        )

    g("init", "-q", "-b", "develop")
    g("commit", "-q", "--allow-empty", "-m", "base", date="2024-09-01T10:00:00Z")
    g(
        "commit",
        "-q",
        "--allow-empty",
        "-m",
        "Fix for ENG-1: thing",
        date="2024-09-05T10:00:00Z",
    )
    g("branch", "release/alpha")
    g("checkout", "-q", "release/alpha")
    g("commit", "-q", "--allow-empty", "-m", "bump alpha", date="2024-09-06T10:00:00Z")
    g("checkout", "-q", "develop")
    g(
        "commit",
        "-q",
        "--allow-empty",
        "-m",
        "Fix for ENG-2: other",
        date="2024-09-10T10:00:00Z",
    )
    g("branch", "release/beta_fix")
    g("checkout", "-q", "release/beta_fix")
    g("commit", "-q", "--allow-empty", "-m", "bump beta", date="2024-10-01T10:00:00Z")
    msgs = tmp / "slack"
    (msgs / BUILDS_CHANNEL).mkdir(parents=True)
    (msgs / BUILDS_CHANNEL / "2024-10.json").write_text(
        json.dumps(
            [
                {
                    "ts": "1727776800.0",
                    "attachments": [
                        {
                            "fallback": "DD iOS - #1 - release/beta_fix Success after 1 min"
                        }
                    ],
                }
            ]
        )
    )
    base = Base(tmp / "gh" / "root", msgs, None)

    def lin(issue, body, when):
        return (
            "INSERT INTO linear.linear_comments (id, issue_id, author_id, parent_id, body, is_edited, created_at, "
            f"updated_at, sequence) VALUES ('x', '{issue}', 'u', NULL, '{body}', false, '{when}', '{when}', NULL);\n"
        )

    ok = lin("ENG-1", "Picked onto release/alpha after QA.", "2024-09-07T10:00:00Z")
    r = check(ok, base)
    assert r["verdict"] == "PASS", r
    bad_branch = lin(
        "ENG-2", "Picked onto release/alpha after QA.", "2024-09-11T10:00:00Z"
    )
    r = check(bad_branch, base)
    assert any(f.startswith("B4 ") for f in r["fail"]), r
    early = lin(
        "ENG-2", "Cherry-picked to beta_fix after the QA pass.", "2024-09-02T10:00:00Z"
    )
    r = check(early, base)
    assert any(f.startswith("B2 ") for f in r["fail"]), r
    late = lin("ENG-1", "Picked onto release/alpha.", "2024-11-20T10:00:00Z")
    assert any(f.startswith("B3 ") for f in check(late, base)["fail"])
    backed = lin(
        "ENG-2",
        "Reverted from release/alpha; it goes out on release/beta_fix instead.",
        "2024-10-02T10:00:00Z",
    )
    r = check(backed, base)
    assert r["verdict"] == "PASS" and any(w.startswith("B4' ") for w in r["warn"]), r
    other = lin(
        "ENG-2",
        "Looks like ENG-1 (that one was picked onto release/alpha); here develop was enough.",
        "2024-09-11T10:00:00Z",
    )
    assert check(other, base)["verdict"] == "PASS"
    unknown = lin("ENG-1", "Picked onto release/gamma.", "2024-09-07T10:00:00Z")
    assert any(f.startswith("B1 ") for f in check(unknown, base)["fail"])
    nocommit = lin("ENG-9", "Picked onto release/alpha.", "2024-09-07T10:00:00Z")
    r = check(nocommit, base)
    assert r["verdict"] == "PASS" and r["info_count"] == 1, r
    print(
        "base_claims self-test: PASS (B1, B2, B3, B4, B4', subject attribution, date-only)"
    )


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        _self_test()
        return 0
    paths = [a for a in argv if not a.startswith("--")]
    if len(paths) != 1:
        print(__doc__, file=sys.stderr)
        return 2
    r = check(Path(paths[0]).read_text(), base_from_context())
    print(json.dumps(r, indent=2) if "--json" in argv else to_text(r))
    return 0 if r["verdict"] == "PASS" else 1


if __name__ == "__main__":
    if sys.argv[1:] in (["-h"], ["--help"]):
        print(__doc__)
        raise SystemExit(0)
    if "--self-test" in sys.argv:
        raise SystemExit(main(sys.argv[1:]))
    from runtime_context import guarded_entry

    guarded_entry(globals(), require_source=True)
    raise SystemExit(main(sys.argv[1:]))
