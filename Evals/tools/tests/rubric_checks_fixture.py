"""Small explicit measurement fixture; never use this as an arbitrary rubric grader."""
import hashlib
from pathlib import Path
import re


def fact_source():
    path=Path(__file__).parent/'fixtures/measurement_source.json'
    raw=path.read_bytes()
    return dict(id='F_SOURCE',path=str(path.resolve()),sha256=hashlib.sha256(raw).hexdigest(),
        quote=raw.decode(),visibility='VISIBLE',access='Immutable synthetic source for focused helper tests.',
        reachability='PROMPT_LINKED')


def facts_fixture(title):
    """Fixed 214 MB source; never synthesize expected facts from arbitrary titles."""
    claims=[]
    for index,match in enumerate(re.finditer(r'\b\d+(?:\.\d+)?\s*MB\b',title)):
        claims.append(dict(id='N'+str(index),quote=match.group(),start=match.start(),kind='NUMBER',
            source_ids=['F_SOURCE'],reason='Compare the title with the fixed measurement source.',
            calculation=dict(op='direct',operands=[dict(source_id='F_SOURCE',pointer='/size_mb')],
                source_unit=dict(source_id='F_SOURCE',pointer='/unit'))))
    for quote,field,kind in [('Zombie Match 3D','game','LITERAL'),('PR #10','pr10','LITERAL'),
                              ('#438','pr438','LITERAL'),('2026-02-10','merged_at','DATE'),
                              ('For Example','document_title','LITERAL')]:
        for match in re.finditer(re.escape(quote),title):
            claims.append(dict(id='L'+str(len(claims)),quote=quote,start=match.start(),kind=kind,
                source_ids=['F_SOURCE'],reason='Fixed synthetic record identity/date.',
                selection=dict(source_id='F_SOURCE',pointer='/'+field)))
    return dict(complete=True,reason='Explicit fixture facts; uncovered numbers remain unresolved.',claims=claims)


def idle_case(title):
    """Do-nothing case from the title's own syntax; a fixture, not a semantic grader."""
    from hg_rubric_checks import title_facts
    facts = title_facts(title)
    if facts["negative_action"] or facts["disguised_negative"]:
        return dict(result="ACCEPT", reason="An Agent that does nothing satisfies this prohibition or preserved state.")
    return dict(result="REJECT", quote=title, reason="An Agent that does nothing never makes the required report.")


def checks_fixture(rubric, prompt="Report the current download size."):
    from hg_rubric_checks import title_facts
    result = dict(sources=[dict(id="P1", path="Evals/task_inputs/04_Prompt.txt",
                  sha256=hashlib.sha256(prompt.encode()).hexdigest(), quote=prompt,
                  visibility="VISIBLE", access="Actual saved prompt", reachability="PROMPT_LINKED"),fact_source()],
                  rows=[], requirements=[])
    for i, row in enumerate(rubric, 1):
        rid = f"Q{i}-O1"
        req = dict(id=rid, entity=f"Build {i}", property="download size", output="Reply",
                   accepted_result="214 MB", reason="Requested measurement fixture.", authority_chain=["P1"],
                   criticality="critical", rows=[i], coverage="SUBSTANTIVE")
        for name, example in (("omission_test", "Leave out the requested download size."),
                              ("wrong_result_test", "Report 215 MB instead of 214 MB.")):
            req[name] = dict(example=example, result="REJECT", reason="The predicate requires the correct value.",
                             caught_by=[dict(row=i, quote=row["title"])])
        result["requirements"].append(req)
        result["rows"].append(dict(row=i, title=row["title"],fact_review=facts_fixture(row['title']),
            restriction_review=dict(reason='Fixture carries no additional restriction.',restrictions=[]),
            wording=dict(subject=title_facts(row["title"])["subject"], reason="Fixture reviews its explicit subject."),
            negative=dict(classification="AFFIRMATIVE", reason="Affirmative reporting requirement."),
            atomicity=dict(outcome_ids=[rid], exception=None,
                independence_test=dict(classification="ONE_RESULT", example="214 MB vs 215 MB.",
                    reason="One size measurement.", satisfied_outcome_ids=[], failed_outcome_ids=[])),
            assertion_inventory=dict(complete=True, reason="One fixture measurement.", assertions=[dict(
                id="A1", field="title", quote=row["title"], role="REQUIRED_RESULT", outcome_id=rid,
                kind="ENTITY_PROPERTY", entities=[f"Build {i}"], property="download size", reason="Requested value.")]),
            supporting_fields=dict(status="PASS", reason="Supporting fields add no constraint."),
            valid_case=dict(example="The current download size is 214.0 MB.", result="ACCEPT",
                            reason="An equivalent rendering of the requested value."),
            do_nothing_case=idle_case(row["title"])))
    result["instruction_reviews"] = [dict(source_id="P1", clauses=[dict(start=0, end=len(prompt), quote=prompt,
        role="REQUIREMENT", outcome_ids=[r["id"] for r in result["requirements"]], reason="The fixture requests each reviewed measurement.")])]
    result['alternative_review']=dict(complete=True,source_ids=['P1'],reason='Single measurement fixture has no advertised alternative branches.',branches=[])
    result['overlap_review']=dict(complete=True,reason='Fixture compares semantic outcome ownership.')
    result['final_reply_test']=dict(example='The current download size is 214 MB.', result='ACCEPT', rejecting_rows=[],
        authority='The prompt asks only for the measurement.', reason='A one-line reply with the value passes every row.')
    return result
