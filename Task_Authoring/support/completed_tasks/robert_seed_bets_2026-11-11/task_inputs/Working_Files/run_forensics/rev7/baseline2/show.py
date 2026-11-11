#!/usr/bin/env python3
"""Read-only viewer for one baseline export (stream-json array). Event numbers are 0-based array indexes.

  show.py run-3 calls                 one line per tool call: event, context, tool, input, result event/size/error
  show.py run-3 ev 205 [--max 8000]   the event's text: tool_use inputs, tool_result text, assistant text
  show.py run-3 ev 205 --grep 'Western|8605' [--ctx 200]   only the matching snippets inside that event
  show.py run-3 grep 'Western Union' [--ctx 120] [--limit 60]   every event whose JSON matches, with a snippet
  show.py run-3 final                 the final result text
  show.py run-3 check 205 'literal quote'   is the quote a literal substring of json.dumps(event, ensure_ascii=False)?
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
EXPORT = lambda label: ROOT / "07_Baseline_Trajectories" / f"trajectory-{label} (1).json"


def load(label):
    return json.loads(EXPORT(label).read_text())


def blocks(ev):
    msg = ev.get("message") if isinstance(ev, dict) else None
    content = msg.get("content") if isinstance(msg, dict) else None
    if isinstance(content, str):
        return [{"type": "text", "text": content}]
    return content or []


def text_of(block):
    t = block.get("type")
    if t == "text":
        return block.get("text", "")
    if t == "thinking":
        return "[thinking] " + (block.get("thinking") or "")
    if t == "tool_use":
        return "[tool_use " + block.get("name", "") + " id=" + block.get("id", "")[-8:] + "] " + json.dumps(block.get("input"), ensure_ascii=False)
    if t == "tool_result":
        c = block.get("content")
        if isinstance(c, list):
            c = "\n".join(x.get("text", json.dumps(x, ensure_ascii=False)) if isinstance(x, dict) else str(x) for x in c)
        return "[tool_result for=" + str(block.get("tool_use_id", ""))[-8:] + (" ERROR" if block.get("is_error") else "") + "] " + str(c)
    return json.dumps(block, ensure_ascii=False)


def render(ev):
    head = ev.get("type", "?")
    if ev.get("parent_tool_use_id"):
        head += " (subagent of " + ev["parent_tool_use_id"][-8:] + ")"
    if ev.get("type") in ("system", "result"):
        body = json.dumps({k: v for k, v in ev.items() if k not in ("tools", "mcp_servers", "slash_commands", "agents", "skills", "plugins")}, ensure_ascii=False)
    else:
        body = "\n".join(text_of(b) for b in blocks(ev))
    return head, body


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    label, cmd = argv[0], argv[1]
    rest = argv[2:]
    def opt(name, default=None, cast=str):
        if name in rest:
            i = rest.index(name)
            value = cast(rest[i + 1])
            del rest[i:i + 2]
            return value
        return default
    mx, ctx, limit, pat = opt("--max", 6000, int), opt("--ctx", 160, int), opt("--limit", 80, int), opt("--grep")
    data = load(label)
    if cmd == "calls":
        results = {}
        for i, ev in enumerate(data):
            for b in blocks(ev):
                if b.get("type") == "tool_result":
                    results[b.get("tool_use_id")] = (i, len(text_of(b)), bool(b.get("is_error")))
        for i, ev in enumerate(data):
            for b in blocks(ev):
                if b.get("type") == "tool_use":
                    r = results.get(b.get("id"), (None, 0, False))
                    ctxname = "sub" if ev.get("parent_tool_use_id") else "main"
                    inp = json.dumps(b.get("input"), ensure_ascii=False)
                    print(f"{i}\t{ctxname}\t{b.get('name','').replace('mcp__hg__','')}\t{inp[:mx if mx != 6000 else 260]}\t-> ev {r[0]} · {r[1]} chars{' · ERROR' if r[2] else ''}")
        return 0
    if cmd == "ev":
        i = int(rest[0])
        head, body = render(data[i])
        print(f"== event {i} · {head} · {len(body)} chars")
        if pat:
            for m in list(re.finditer(pat, body, re.I))[:limit]:
                s, e = max(0, m.start() - ctx), min(len(body), m.end() + ctx)
                print(f"  @{m.start()}: …{body[s:e]}…".replace("\n", " ⏎ "))
        else:
            print(body[:mx] + (f"\n…[{len(body) - mx} more chars; raise --max or use --grep]" if len(body) > mx else ""))
        return 0
    if cmd == "grep":
        rx = re.compile(rest[0], re.I)
        n = 0
        for i, ev in enumerate(data):
            head, body = render(ev)
            ms = list(rx.finditer(body))
            if not ms:
                continue
            n += 1
            if n > limit:
                print("…limit reached")
                break
            m = ms[0]
            s, e = max(0, m.start() - ctx), min(len(body), m.end() + ctx)
            print(f"{i}\t{head}\t{len(ms)} hit(s)\t…{body[s:e]}…".replace("\n", " ⏎ "))
        return 0
    if cmd == "final":
        for i in range(len(data) - 1, -1, -1):
            if data[i].get("type") == "result":
                print(f"== event {i} result")
                print(str(data[i].get("result"))[:mx if mx != 6000 else 20000])
                return 0
        return 1
    if cmd == "check":
        i, quote = int(rest[0]), rest[1]
        ok = quote in json.dumps(data[i], ensure_ascii=False)
        print("OK" if ok else "ABSENT")
        return 0 if ok else 1
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
