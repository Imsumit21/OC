#!/usr/bin/env python3
"""Optional independent red-team review of design artifacts by external reviewer models.

It sends design artifacts (dossier, manifest, brief — never asks it to write the
prompt, Oracle Events or criteria) with a red-team instruction to any standard
`/v1/chat/completions` endpoint and saves the reply. Local use only — the eval sandbox has no key.
Configuration comes only from the environment; the key is never printed or written:
  REDTEAM_BASE_URL       endpoint base URL (".../v1" is appended when missing)
  REDTEAM_API_KEY        key for that endpoint
  REDTEAM_MODEL          primary reviewer model (or --model)
  REDTEAM_SECOND_MODEL   second reviewer, from a different model family (for --dual)

Usage:
  python3 Task_Authoring/tools/redteam_review.py --mode redteam \
      --in Task_Authoring/task_inputs/Working_Files/01_Grounding_Dossier.md \
      --in Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json \
      --out Task_Authoring/task_inputs/Working_Files/01b_Redteam_Review.md [--effort high|xhigh|medium] [--model M]
  python3 Task_Authoring/tools/redteam_review.py ... --dual        # also run REDTEAM_SECOND_MODEL → <out>.second.md
  python3 Task_Authoring/tools/redteam_review.py [--model M] --ping
"""
from __future__ import annotations

import json
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

MODES = {
    "harness": (
        "You are red-teaming a task-AUTHORING HARNESS (playbooks, gates, tools) used by an AI model to build "
        "evaluation tasks for agentic models. Goal of the harness: tasks that are extremely hard for frontier "
        "agents (500+ necessary tool calls, 10+ services) yet fully VALID under the supplied QC rules and evals "
        "(unique ground truth, prompt incorporation, persona ACL reach, cross-service coherence, rubric quality). "
        "Find concrete ways an authoring model could follow these documents and pass every gate while still "
        "producing (a) an invalid task, (b) an easy task, or (c) a shallow artifact; contradictions between "
        "documents; rules that are unenforceable or gameable; and missing gates. For each finding give: the exact "
        "location, the exploit or gap, why the current gates miss it, and a concrete mechanical fix (a check, a "
        "field, a rule). Rank by severity. Never draft a task prompt, Oracle Event text, or rubric criterion text."
    ),
    "redteam": (
        "You are an adversarial evaluator of agentic benchmark tasks. A frontier agent (Claude Opus class) "
        "will attempt this task with MCP tools over 13 services (Slack, Gmail, Google Calendar/Drive/Docs/Sheets/"
        "Slides, Contacts, GitHub, Linear, Trello, Confluence, Snowflake) as one fixed persona whose Gmail, Slack, "
        "Calendar and Drive-family reads are scoped. Your job is to BREAK the design. Report, with specific record "
        "references from the material: (1) every shortcut a strong agent could take — a bulk call or single source "
        "that substitutes for the intended per-record work, a search that lands directly on the answer, a seeded "
        "record that states a conclusion; (2) every trap that a careful reader defeats trivially, and why; "
        "(3) Unique-Ground-Truth risks — two defensible final states, act-vs-defer splits, unresolvable source "
        "conflicts; (4) requirements that are not validly incorporated by the prompt through an explicit "
        "delegation chain (they would be unauthorized); (5) feasibility/ACL risks; (6) places where the claimed "
        "tool-call volume would collapse (bulk listings, cached results) or would count as padding; (7) the three "
        "highest-leverage changes that would make strong agents fail more often WITHOUT creating ambiguity or "
        "padding. Be concrete and terse. Do not write prompt text, Oracle Events or rubric criteria."
    ),
    "ideas": (
        "You are designing difficulty for an agentic benchmark over a fictional mobile-game studio's 13 workplace "
        "services. Given the universe digest and constraints, propose concrete, grounded difficulty mechanisms "
        "that make strong agents fail even after complete retrieval and careful reading: scope/alias boundaries, "
        "dual-regime rules with effective dates, per-record evidence that no bulk call returns, superseding chains "
        "across services, authoritative-but-wrong summaries met first, reuse-versus-create decisions, exact "
        "predicates with exclusions over large cohorts. Each mechanism must keep one unambiguous final state and "
        "be incorporated through explicit delegation from a short natural request. Do not write the request text."
    ),
}


def endpoint() -> tuple[str, str]:
    base, key = os.environ.get("REDTEAM_BASE_URL", "").rstrip("/"), os.environ.get("REDTEAM_API_KEY", "")
    if not base or not key:
        raise SystemExit("redteam_review: set REDTEAM_BASE_URL and REDTEAM_API_KEY")
    return (base if base.endswith("/v1") else base + "/v1"), key


def model_from_env(var: str) -> str:
    model = os.environ.get(var, "")
    if not model:
        raise SystemExit(f"redteam_review: set {var} or pass --model")
    return model


def _read_stream(resp) -> dict:
    """Read an SSE chat-completions stream (keeps long high-effort calls from idling out) or a plain JSON body."""
    parts, usage, model, raw = [], {}, None, b""
    for line in resp:
        raw += line if len(raw) < 2_000_000 else b""
        text = line.decode("utf-8", "replace").strip()
        if not text.startswith("data:"):
            continue
        payload = text[5:].strip()
        if payload == "[DONE]":
            break
        chunk = json.loads(payload)
        model = chunk.get("model", model)
        usage = chunk.get("usage") or usage
        for choice in chunk.get("choices", []):
            delta = choice.get("delta") or choice.get("message") or {}
            if delta.get("content"):
                parts.append(delta["content"])
    if not parts and raw.strip().startswith(b"{"):
        return json.loads(raw)  # endpoint ignored stream=True
    return {"model": model, "usage": usage, "choices": [{"message": {"content": "".join(parts)}}]}


def call(system: str, user: str, model: str, effort: str, timeout: int = 1800) -> str:
    base, key = endpoint()
    body = {"model": model, "messages": [{"role": "system", "content": system}, {"role": "user", "content": user}],
            "reasoning_effort": effort}
    req = urllib.request.Request(base + "/chat/completions", data=json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    for attempt in range(3):  # transient network drops (connect timeouts, DNS) are common on long calls
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = _read_stream(resp)
            break
        except (urllib.error.URLError, TimeoutError, ConnectionError, socket.timeout) as error:
            if attempt == 2 or isinstance(error, urllib.error.HTTPError) and error.code < 500:
                raise
            print(f"redteam_review: network error ({type(error).__name__}); retrying in {30 * (attempt + 1)} s", file=sys.stderr)
            time.sleep(30 * (attempt + 1))
    return data["choices"][0]["message"]["content"].rstrip() + "\n"


def main(argv: list[str]) -> int:
    model, effort, mode, ins, out = None, "high", "redteam", [], None
    if "--model" in argv:  # honour --model wherever it appears (e.g. with --ping)
        model = argv[argv.index("--model") + 1]
    dual = "--dual" in argv
    argv = [a for a in argv if a != "--dual"]
    i = 0
    while i < len(argv):
        a = argv[i]
        if a == "--ping":
            print(call("Reply with the single word: ready", "ping", model or model_from_env("REDTEAM_MODEL"), "low",
                       120).strip().splitlines()[0])
            return 0
        if a in ("--model", "--effort", "--mode", "--in", "--out"):
            val = argv[i + 1]
            if a == "--model":
                model = val
            elif a == "--effort":
                effort = val
            elif a == "--mode":
                mode = val
            elif a == "--in":
                ins.append(Path(val))
            else:
                out = Path(val)
            i += 2
            continue
        i += 1
    if not ins or not out or mode not in MODES:
        print(__doc__, file=sys.stderr)
        return 2
    user = "\n\n".join(f"=== {p.name} ===\n{p.read_text()}" for p in ins)
    out.write_text(call(MODES[mode], user, model or model_from_env("REDTEAM_MODEL"), effort))
    print(f"wrote {out}")
    if dual:  # same inputs, a second model family; reconcile both reports in the dossier
        second = out.with_name(out.stem + ".second" + out.suffix)
        second.write_text(call(MODES[mode], user, model_from_env("REDTEAM_SECOND_MODEL"), effort))
        print(f"wrote {second}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", "replace")
        detail = re.sub(r"(?i)(bearer\s+|key[\"'=:\s]+)\S+", r"\1***", detail)  # never echo key material
        kind = "budget exhausted" if "budget" in detail.lower() else "request rejected"
        print(f"redteam_review: HTTP {error.code} ({kind}): {detail[:300]}", file=sys.stderr)
        raise SystemExit(3)
