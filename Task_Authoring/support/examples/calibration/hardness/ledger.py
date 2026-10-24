#!/usr/bin/env python3
"""Scratch: turn a Claude-Code stream-json trajectory into a compact tool-call ledger.

Usage: python3 ledger.py <trajectory.json> <out.md> [--result-chars N]
Writes one line per tool call: seq · agent(main/sub:<id>) · tool · input · result head.
Assistant narration (text blocks) is interleaved as '> ' lines. Read-only on the input.
"""
import json, sys, collections

def short(s, n):
    s = s if isinstance(s, str) else json.dumps(s, ensure_ascii=False)
    s = s.replace("\\n", " ").replace("\n", " ")
    return s if len(s) <= n else s[:n] + f" …[+{len(s)-n}]"

def result_text(c):
    if isinstance(c, list):
        return " ".join(x.get("text", "") if isinstance(x, dict) else str(x) for x in c)
    return c if isinstance(c, str) else json.dumps(c, ensure_ascii=False)

def main():
    src, out = sys.argv[1], sys.argv[2]
    n = int(sys.argv[sys.argv.index("--result-chars") + 1]) if "--result-chars" in sys.argv else 600
    d = json.load(open(src))
    init = next((e for e in d if e.get("type") == "system"), {})
    res_events = [e for e in d if e.get("type") == "result"]
    final = res_events[0] if res_events else {}
    post_final = res_events[1:]
    calls, results, order, texts = {}, {}, [], []
    models = collections.Counter()
    for i, e in enumerate(d):
        m = e.get("message") or {}
        if e.get("type") == "assistant":
            models[m.get("model")] += 1
            for blk in m.get("content", []) or []:
                if blk.get("type") == "tool_use":
                    calls[blk["id"]] = (blk["name"], blk.get("input"), e.get("parent_tool_use_id"))
                    order.append(("call", blk["id"]))
                elif blk.get("type") == "text" and blk.get("text", "").strip():
                    order.append(("text", (e.get("parent_tool_use_id"), blk["text"])))
        elif e.get("type") == "user":
            cont = m.get("content")
            if isinstance(cont, list):
                for blk in cont:
                    if isinstance(blk, dict) and blk.get("type") == "tool_result":
                        results[blk["tool_use_id"]] = (result_text(blk.get("content")), blk.get("is_error"))
    sub_ids = {}
    lines = []
    seq = 0
    tool_counter = collections.Counter()
    errors = 0
    for kind, v in order:
        if kind == "text":
            parent, t = v
            who = "main" if not parent else f"sub{sub_ids.setdefault(parent, len(sub_ids)+1)}"
            lines.append(f"> [{who}] {short(t, 900)}")
            continue
        name, inp, parent = calls[v]
        seq += 1
        who = "main" if not parent else f"sub{sub_ids.setdefault(parent, len(sub_ids)+1)}"
        res, err = results.get(v, ("<no result>", None))
        if err:
            errors += 1
        tool_counter[name.replace("mcp__hg__", "")] += 1
        lines.append(f"{seq:4d} [{who}] {name.replace('mcp__hg__','')} {short(inp, 400)}\n      => {'ERR ' if err else ''}{short(res, n)}")
    head = [
        f"# Ledger: {src}",
        f"model(init)={init.get('model')} assistant-models={dict(models)}",
        f"tool_calls={seq} errored_results={errors} turns={final.get('num_turns')} duration_ms={final.get('duration_ms')} result_subtype={final.get('subtype')} is_error={final.get('is_error')}",
        f"subagents={len(sub_ids)} subagent_models={sorted({(e.get('message') or {}).get('model') for e in d if e.get('type')=='assistant' and e.get('parent_tool_use_id')} - {None})} post_final_result_events={len(post_final)} compaction={'yes' if any('continued from a previous conversation' in json.dumps(e)[:20000] for e in d if e.get('type')=='user') else 'no'}",
        "tool counts: " + ", ".join(f"{k}={c}" for k, c in tool_counter.most_common()),
        "",
    ]
    tail = ["", "## FINAL RESPONSE (first result event)", final.get("result", "<none>") or "<none>"]
    if post_final:
        tail += ["", f"## POST-FINAL RESULT EVENTS ({len(post_final)}) — background work that reported after the final answer"]
        tail += [f"- turns={e.get('num_turns')} ms={e.get('duration_ms')}: {short(e.get('result') or '', 400)}" for e in post_final]
    open(out, "w").write("\n".join(head + lines + tail))
    print(head[1]); print(head[2]); print(head[3]); print(head[4][:600])

if __name__ == "__main__":
    main()
