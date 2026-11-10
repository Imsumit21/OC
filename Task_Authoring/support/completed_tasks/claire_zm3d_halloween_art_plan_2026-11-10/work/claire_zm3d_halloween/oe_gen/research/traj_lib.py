"""Read-only loader for the seven Opus trajectories. Produces call records."""
import json, re, os
ROOT = "/Users/sumit/Source/OC/Task_Authoring/task_inputsN2"
RUNS = {f"B{i}": f"{ROOT}/07_Baseline_Trajectories/trajectory-run-{i}.json" for i in range(1, 7)}
RUNS["PC"] = f"{ROOT}/06_PreCheck_Trajectory/trajectory-run-1 (1).json"

def strip(name):
    return re.sub(r"^mcp__.*?__", "", name)

def flat(content):
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        out = []
        for b in content:
            if isinstance(b, dict):
                if b.get("type") == "text":
                    out.append(b.get("text", ""))
                else:
                    out.append(json.dumps(b, ensure_ascii=False))
            else:
                out.append(str(b))
        return "\n".join(out)
    return json.dumps(content, ensure_ascii=False)

def load(run):
    ev = json.load(open(RUNS[run]))
    calls, idx = [], {}
    for n, e in enumerate(ev):
        msg = e.get("message") if isinstance(e, dict) else None
        if not isinstance(msg, dict):
            continue
        c = msg.get("content")
        if not isinstance(c, list):
            continue
        for b in c:
            if not isinstance(b, dict):
                continue
            if b.get("type") == "tool_use":
                rec = dict(run=run, ev=n, seq=len(calls), id=b.get("id"), raw=b.get("name"),
                           name=strip(b.get("name", "")), input=b.get("input"), out=None, err=None)
                calls.append(rec); idx[b.get("id")] = rec
            elif b.get("type") == "tool_result":
                r = idx.get(b.get("tool_use_id"))
                if r is not None:
                    r["out"] = flat(b.get("content")); r["err"] = b.get("is_error")
    return ev, calls

def all_calls():
    return {r: load(r)[1] for r in RUNS}

def unwrap(out):
    """Return parsed payload for {"result": "<json>"} outputs, else None."""
    if out is None:
        return None
    try:
        o = json.loads(out)
    except Exception:
        return None
    if isinstance(o, dict) and set(o.keys()) == {"result"}:
        r = o["result"]
        if isinstance(r, str):
            try:
                return json.loads(r)
            except Exception:
                return r
        return r
    return o

def text(out):
    """Output with the {"result": ...} wrapper removed, as a printable string."""
    if out is None:
        return ""
    try:
        o = json.loads(out)
        if isinstance(o, dict) and set(o.keys()) == {"result"} and isinstance(o["result"], str):
            return o["result"]
    except Exception:
        pass
    return out
