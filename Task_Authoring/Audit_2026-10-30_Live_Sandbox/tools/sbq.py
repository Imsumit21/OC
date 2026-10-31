import json, urllib.request, urllib.parse, sys
B="https://ta-01m67a1cfdpfzr6mwq3xpbhm9v-8081-yywwmyhop72vcg9iq3nlqvpe5.w.modal.host"
BAD=("insert","update","delete","drop","truncate","alter","create","grant","revoke","copy","vacuum","merge")
def q(sql, timeout=300):
    low=sql.strip().lower().lstrip("(")
    if not (low.startswith("select") or low.startswith("with") or low.startswith("table")):
        return {"error":"REFUSED not-read: "+sql[:60]}
    for f in BAD:
        if low.startswith(f): return {"error":"REFUSED "+f}
    data=urllib.parse.urlencode({"query":sql}).encode()
    req=urllib.request.Request(B+"/api/query",data=data)
    try:
        with urllib.request.urlopen(req,timeout=timeout) as r: return json.load(r)
    except urllib.error.HTTPError as e:
        body=e.read().decode("utf8","replace")
        try: return json.loads(body)
        except Exception: return {"error":f"HTTP {e.code}: {body[:300]}"}
    except Exception as e: return {"error":repr(e)}
def rows(sql,timeout=300):
    d=q(sql,timeout)
    if "error" in d: return None, d["error"]
    return d["rows"], None
