import json, urllib.request, sys
G="https://ta-01m67a1cfdpfzr6mwq3xpbhm9v-18765-yywwmyhop72vcg9iq3nlqvpe5.w.modal.host/mcp"
_S={"id":None}
def _post(payload, sid=None, timeout=120):
    h={"Content-Type":"application/json","Accept":"application/json, text/event-stream"}
    if sid: h["mcp-session-id"]=sid
    req=urllib.request.Request(G,data=json.dumps(payload).encode(),headers=h)
    try:
        with urllib.request.urlopen(req,timeout=timeout) as r:
            body=r.read().decode("utf8","replace")
            return r.headers.get("mcp-session-id"), body
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}: {e.read().decode('utf8','replace')[:400]}"
def _parse(body):
    for line in body.splitlines():
        line=line.strip()
        if line.startswith("data: "): line=line[6:]
        if line.startswith("{"):
            try: return json.loads(line)
            except Exception: pass
    return {"raw":body[:400]}
def session():
    if _S["id"]: return _S["id"]
    sid,body=_post({"jsonrpc":"2.0","id":1,"method":"initialize","params":{"protocolVersion":"2024-11-05","capabilities":{},"clientInfo":{"name":"probe","version":"1"}}})
    _S["id"]=sid
    _post({"jsonrpc":"2.0","method":"notifications/initialized"},sid)
    return sid
WRITE=("create","update","delete","send","add","remove","set_","move","archive","trash","post","edit","upload","copy","duplicate","assign","invite","join","leave","star","unstar","label","comment","react","merge","close","reopen","restore","rename","share","import","write","put","patch","revoke","transfer","convert","clear","append","insert","batch","draft","reply","forward","modify","toggle","subscribe","watch")
def call(tool, args=None, timeout=120, force=False):
    low=tool.split("_",1)[-1].lower()
    if not force and any(low.startswith(w) or f"_{w}" in low for w in WRITE):
        return {"REFUSED_WRITE":tool}
    sid=session()
    _,body=_post({"jsonrpc":"2.0","id":99,"method":"tools/call","params":{"name":tool,"arguments":args or {}}},sid,timeout)
    return _parse(body)
