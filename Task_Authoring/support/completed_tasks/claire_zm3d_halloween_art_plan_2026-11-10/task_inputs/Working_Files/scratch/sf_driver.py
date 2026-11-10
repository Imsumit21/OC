import json,subprocess,sys
def read(ptr,mc=9000):
    off=0;parts=[]
    for _ in range(80):
        r=subprocess.run(["python3","Task_Authoring/tools/hg.py","search","get","snowflake","--file","snowflake.json","--pointer",ptr,"--max-chars",str(mc),"--offset",str(off),"--compact"],capture_output=True,text=True)
        try: o=json.loads(r.stdout)
        except Exception: return None
        if "text" not in o: return None
        parts.append(o["text"])
        if not o.get("truncated"): break
        off=o["next_offset"]
    try: return json.loads("".join(parts))
    except Exception: return None
rows=[]
for i in range(0,45):
    rec=read(f"/tables/{i}")
    print(i, (rec or {}).get("name"), flush=True)
    if rec is None: break
    rows.append(rec)
json.dump(rows,open("Task_Authoring/task_inputsN2/Working_Files/scratch/sf_tables2.json","w"))
print("DONE",len(rows),flush=True)
