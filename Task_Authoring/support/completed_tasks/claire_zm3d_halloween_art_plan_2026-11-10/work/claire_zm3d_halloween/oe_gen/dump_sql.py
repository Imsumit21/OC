import json,os,sys,collections
TI='/Users/sumit/Source/OC/Task_Authoring/task_inputsN2'
sys.path.insert(0,'/Users/sumit/Source/OC/Task_Authoring/tools')
from base_check import parse_sql
S=parse_sql(open(TI+'/01_Universe_Inject.sql').read())
c=collections.Counter((x['op'],x.get('table')) for x in S)
for k,v in sorted(c.items(),key=str): print(k,v)
json.dump([{k:v for k,v in x.items()} for x in S],open('sql_rows.json','w'),default=str,indent=0)
print(S[0].keys())
