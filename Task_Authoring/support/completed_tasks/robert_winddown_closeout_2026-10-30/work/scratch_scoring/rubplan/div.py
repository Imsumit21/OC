import sys; sys.argv=['x']; sys.path.insert(0,'/home/sumit/Downloads/OC/OC/Task_Authoring-2/tools')
import stage_gate as sg
from pathlib import Path
doc=sg.Doc(Path(sys.argv[1] if len(sys.argv)>1 else 'plan_draft.md'),'plan')
led=sg.Doc(Path('/home/sumit/Downloads/OC/OC/Task_Authoring-2/task_inputs/Working_Files/08_OE_Writing_Ledger.md'),'led')
facts=sg.ledger_facts(led)
A=sg.rows_in(doc,r"coverage matrix"); A2=sg.rows_in(doc,r"grading risks")
class Ctx:
    def add(self,*a): print(a[0],a[1],'\n  ',a[2])
sg.plan_diversity(Ctx(),doc,A,A2,facts)
