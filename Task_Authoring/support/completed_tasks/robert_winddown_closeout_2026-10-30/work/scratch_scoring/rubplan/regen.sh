cd /tmp/claude-1000/-home-sumit-Downloads-OC-OC/a9f2273f-6832-49de-a422-8296cfdee0cc/scratchpad/rubplan
python3 draft.py rows.json draft.json >/dev/null && python3 - <<'PY'
import json,re
d=json.load(open('draft.json'))
for x in d: x['title']=re.sub(r"\) \(or a clear equivalent\)$", "; or a clear equivalent)", x['title'])
json.dump(d,open('draft.json','w'),indent=1,ensure_ascii=False)
T='/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/'
json.dump([{k:x[k] for k in ('title','category','weight','justification','evidence')} for x in d],open(T+'09_Rubrics.json','w'),indent=1,ensure_ascii=False)
json.dump(d,open(T+'Working_Files/09_Rubrics.draft_with_plan_ids.json','w'),indent=1,ensure_ascii=False)
print(len(d), sum(x['weight'] for x in d))
PY
