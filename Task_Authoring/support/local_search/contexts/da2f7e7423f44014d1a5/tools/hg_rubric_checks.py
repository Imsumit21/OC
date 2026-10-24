"""Reconcile rubric judgments with exact titles and evidence in CREATE and AUDIT.

This validates declarations and narrow syntactic facts, not arbitrary semantics.
Unknown classifications stay incomplete; they are not fabricated rubric failures.
"""
import json
from pathlib import Path
import re

from hg_review_evidence import EvidenceReader, authority, links, sources
from hg_rubric_assertions import validate_assertions
from hg_coherent_record import verify_record_source
from hg_rubric_sampling import validate_sampling


ARTIFACT = re.compile(r"^(?:(?:the|an?|that|this|each|its)\s+"
                      r"(?:(?!agent\b)[a-z-]+\s+){0,4})?"
                      r"(?:write[- ]?up|reply|response|report|plan|artifact|document|email|message|issue|ticket|"
                      r"summary|answer|deliverable|table|spreadsheet|memo|note|output|model|assistant|chatbot|solution|"
                      r"register|workbook|worksheet|matrix|cell|column|file)\b", re.I)
AGENT = re.compile(r"^(?:the )?agent\b", re.I)
# QC spec: "Agent" + action + necessary context. "Agent …" and "The Agent …" are both standard.
STANDARD_AGENT = re.compile(r"^(?:The )?Agent ")
POSSESSIVE = re.compile(r"^(?:the )?agent['’]s\s", re.I)
BARE_ACTION = re.compile(r"^(?:reports?|identifies?|states?|creates?|sends?|lists?|includes?|provides?|"
                         r"explains?|documents?|flags?|updates?|calculates?|summarizes?|compares?|cites?|"
                         r"checks?|confirms?|verifies?|records?|writes?|addresses?|describes?)\b", re.I)
NEGATIVE_ACTION = re.compile(r"^(?:the )?agent\s+(?:does not|doesn't|do not|must not|will not|won't|never|makes no|takes no|avoids|fails to|refrains from|declines to)\b", re.I)


def title_facts(title, tool_names=()):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Rubric title must be nonempty text")
    title = title.strip()
    if POSSESSIVE.match(title):
        subject = "AGENT_POSSESSIVE"
    elif AGENT.match(title):
        subject = "AGENT_ACTION"
    elif ARTIFACT.match(title):
        subject = "NON_AGENT"
    elif BARE_ACTION.match(title):
        subject = "IMPLICIT_ACTION"
    else:
        subject = "UNRESOLVED"
    tokens = set(re.findall(r"[\w]+", title))
    tools = sorted(tokens.intersection(tool_names))
    if re.search(r"\bmcp__[\w]+", title):
        tools.append("explicit MCP tool identifier")
    return dict(subject=subject, tool_names=tools, negative_action=bool(NEGATIVE_ACTION.match(title)))


def validate_checks(checks, rubric, issues, *, root, context):
    def require(ok, message):
        if not ok:
            raise ValueError("Rubric checks: " + message)

    def text(value, label):
        require(isinstance(value, str) and bool(value.strip()), label + " needs substantive text")

    def obj(value, label):
        require(isinstance(value, dict), label + " must be an object")
        return value

    def ids(value, allowed, label, nonempty=False):
        require(isinstance(value, list) and (bool(value) or not nonempty) and
                all(type(i) is type(next(iter(allowed), "")) and i in allowed for i in value) and
                len(value) == len(set(value)), label + " needs unique known IDs")
        return set(value)

    def finding(kind, row, label, acceptance=True):
        matches = [i for i in issues if i["type"] == kind and row in i["rows"]]
        require(any(not acceptance or i.get("impact") in {"rejects_correct", "accepts_wrong"} for i in matches),
                label + ": record the demonstrated " + kind + " issue; PASS/precision-only cannot override it")

    obj(checks, "checks")
    require(isinstance(issues, list) and all(isinstance(i, dict) and isinstance(i.get("rows"), list)
            and isinstance(i.get("type"), str) for i in issues), "issues must be typed findings with row arrays")
    reader = EvidenceReader(root)
    known = sources(reader, checks.get("sources"))
    pending, wording_fail, wording_nonstandard, negative_fail = [], [], [], []
    fact_results = []
    reqs = checks.get("requirements")
    require(isinstance(reqs, list) and bool(reqs), "requirements must enumerate the requested outcomes")
    requirements, identities, missing, covered = {}, set(), {}, set()
    row_numbers = set(range(1, len(rubric) + 1))
    for req in reqs:
        obj(req, "requirement")
        for key in ("id", "entity", "property", "output", "accepted_result", "reason"):
            text(req.get(key), "requirement." + key)
        rid = req["id"]
        require(rid not in requirements, "duplicate outcome ID " + rid)
        identity = tuple(req[k].strip().casefold() for k in ("entity", "property", "output"))
        require(identity not in identities, "duplicate semantic outcome; do not count one omission twice")
        identities.add(identity)
        requirements[rid] = req
        require(req.get("criticality") in {"critical", "non_critical"}, rid + " needs criticality")
        visible = authority(req.get("authority_chain"), known, root, context)
        if not visible:
            pending.append(rid + ": unresolved/inaccessible authority")
        mapped = ids(req.get("rows"), row_numbers, rid + ".rows")
        status = req.get("coverage")
        require(status in {"SUBSTANTIVE", "MENTION_ONLY", "MISSING", "UNRESOLVED"}, rid + " needs coverage classification")
        results = []
        for name in ("omission_test", "wrong_result_test"):
            test = obj(req.get(name), rid + "." + name)
            for key in ("example", "reason"):
                text(test.get(key), rid + "." + name + "." + key)
            result = test.get("result")
            require(result in {"ACCEPT", "REJECT", "UNRESOLVED"}, rid + ": invalid mutation result")
            catches = test.get("caught_by")
            require(isinstance(catches, list), rid + ": caught_by must contain exact title predicates")
            seen = set()
            for catch in catches:
                obj(catch, "catch")
                number = catch.get("row")
                require(type(number) is int and number in mapped and number not in seen, rid + ": invalid catching row")
                seen.add(number)
                text(catch.get("quote"), rid + ": catching predicate")
                require(catch["quote"] in rubric[number-1]["title"], rid + ": catching predicate must be in the exact title, not its justification")
            require(bool(catches) == (result == "REJECT"), rid + ": mutation result contradicts catching rows")
            results.append(result)
        if not visible:
            require(status == "UNRESOLVED", rid + ": incomplete authority cannot establish missing coverage")
            pending.append(rid + ": unresolved coverage authority")
        elif "ACCEPT" in results:
            require(status in {"MENTION_ONLY", "MISSING"}, rid + ": an accepted omission/wrong result is missing substantive coverage")
            missing[rid] = req["criticality"]
            # Acceptance of an omitted/wrong substantive deliverable is not a depth preference.
            require(req["criticality"] == "critical", rid + ": accepted omission/wrong result changes acceptance; cannot downgrade to depth weakness")
        elif "UNRESOLVED" in results:
            require(status == "UNRESOLVED", rid + ": incomplete evidence cannot establish coverage")
            pending.append(rid + ": unresolved coverage tests")
        else:
            require(status == "SUBSTANTIVE", rid + ": coverage label contradicts the two mutation tests")
            covered.add(rid)

    sampling = validate_sampling(checks, requirements, known)
    pending.extend(sampling["unresolved"])

    # Every character of the actual prompt (and each used incorporated instruction
    # excerpt) is accounted for. Classification is still a semantic judgment.
    partitions = checks.get("instruction_reviews")
    require(isinstance(partitions, list) and bool(partitions), "instruction_reviews must account for the actual prompt")
    reviewed_sources, mapped_requirements = set(), set()
    for part in partitions:
        obj(part, "instruction_review")
        sid = part.get("source_id")
        source = links([sid], known, "instruction_review.source_id")[0]
        require(sid not in reviewed_sources, "duplicate instruction review")
        reviewed_sources.add(sid)
        selected = reader.quote(source)
        require(selected.strip() == source["quote"].strip(), "instruction source must quote its entire selected text; select a precise pointer/line range")
        clauses = part.get("clauses")
        require(isinstance(clauses, list) and bool(clauses), "instruction review needs clauses")
        cursor = 0
        for clause in clauses:
            obj(clause, "clause")
            start, end = clause.get("start"), clause.get("end")
            require(type(start) is int and type(end) is int and start == cursor and start < end <= len(source["quote"]),
                    "instruction clauses must partition all text without gaps or overlaps")
            require(clause.get("quote") == source["quote"][start:end], "instruction clause quote/offset mismatch")
            cursor = end
            text(clause.get("reason"), "clause.reason")
            role = clause.get("role")
            require(role in {"REQUIREMENT", "CONTEXT", "UNRESOLVED"}, "invalid instruction clause role")
            refs = ids(clause.get("outcome_ids"), set(requirements), "clause.outcome_ids", role == "REQUIREMENT")
            require(role != "CONTEXT" or not refs, "context cannot silently add required outcomes")
            require(all(sid in requirements[r]["authority_chain"] for r in refs), "clause outcome lacks that instruction in its authority chain")
            mapped_requirements.update(refs)
            if role == "UNRESOLVED":
                pending.append(sid + ": unresolved instruction clause")
        require(cursor == len(source["quote"]), "instruction review omitted prompt text")
    used = {sid for req in reqs for sid in req["authority_chain"]}
    require(used <= reviewed_sources, "review every prompt/incorporated instruction used as authority")
    require(mapped_requirements == set(requirements), "every outcome needs an instruction-clause mapping")
    # A partitioned source must include at least one actual saved-prompt anchor.
    require(bool(reviewed_sources & {r["authority_chain"][0] for r in reqs}),
            "instruction reviews need the actual saved prompt")
    for sid in {r["authority_chain"][0] for r in reqs}:
        require("line_start" not in known[sid] and "line_end" not in known[sid],
                "review the entire saved prompt, not a selected line range")

    tool_path = Path(root) / "Evals/references/tools/catalog.json"
    tool_names = {t["name"] for t in json.loads(tool_path.read_text())} if tool_path.exists() else set()
    rows = checks.get("rows")
    require(isinstance(rows, list) and len(rows) == len(rubric), "one exact-title check is required for every criterion")
    seen = set()
    for row in rows:
        obj(row, "row")
        number = row.get("row")
        require(type(number) is int and number in row_numbers and number not in seen, "invalid/duplicate check row")
        seen.add(number)
        label = f"R{number}"
        saved = rubric[number-1]
        annotations = saved.get("annotations", {})
        criterion = {**saved, **{key: saved.get(key, annotations.get(key, ""))
                               for key in ("justification", "evidence")}}
        require(row.get("title") == criterion["title"], label + ": check title differs from actual rubric")
        wording = obj(row.get("wording"), label + ".wording")
        text(wording.get("reason"), label + ".wording.reason")
        facts = title_facts(criterion["title"], tool_names)
        subject = wording.get("subject")
        require(subject in {"AGENT_ACTION", "AGENT_POSSESSIVE", "IMPLICIT_ACTION", "NON_AGENT", "UNRESOLVED"}, label + ": invalid subject")
        if facts["subject"] != "UNRESOLVED":
            require(subject == facts["subject"], label + ": subject contradicts the actual title: " + facts["subject"])
        elif subject == "IMPLICIT_ACTION":
            require(False, label + ": unfamiliar syntax cannot be relabeled IMPLICIT_ACTION")
        elif subject in {"AGENT_ACTION", "AGENT_POSSESSIVE"}:
            actor = wording.get("actor_quote")
            text(actor, label + ": unfamiliar syntax needs the actual Agent actor quote")
            require(actor in criterion["title"] and re.search(r"\bagent\b", actor, re.I),
                    label + ": actor quote must name the Agent in the title")
        if subject == "NON_AGENT" or facts["tool_names"]:
            wording_fail.append(number)
        elif subject == "UNRESOLVED":
            pending.append(label + ": unresolved Agent phrasing")
        elif subject != "AGENT_ACTION" or not STANDARD_AGENT.match(criterion["title"]):
            wording_nonstandard.append(number)
        negative = obj(row.get("negative"), label + ".negative")
        text(negative.get("reason"), label + ".negative.reason")
        framing = negative.get("classification")
        require(framing in {"AFFIRMATIVE", "DESCRIPTIVE_NEGATION", "PROHIBITION", "UNRESOLVED"}, label + ": invalid negative framing")
        if facts["negative_action"]:
            require(framing == "PROHIBITION", label + ": negative graded action is not descriptive negation")
        if framing == "UNRESOLVED":
            pending.append(label + ": unresolved negative framing")
        elif framing == "PROHIBITION":
            # hg-strict-overrides-v1: prompt authority does not rescue prohibition-only acceptance.
            negative_fail.append(number)
        atomic = obj(row.get("atomicity"), label + ".atomicity")
        oids = ids(atomic.get("outcome_ids"), set(requirements), label + ".outcome_ids", True)
        require(oids == {rid for rid, req in requirements.items() if number in req["rows"]},
                label + ": atomicity outcomes disagree with forward/reverse coverage")
        test = obj(atomic.get("independence_test"), label + ".independence_test")
        classification = test.get("classification")
        require(classification in {"ONE_RESULT", "INDEPENDENT_RESULTS", "UNRESOLVED"}, label + ": invalid atomicity class")
        for key in ("example", "reason"):
            text(test.get(key), label + ".independence_test." + key)
        satisfied = ids(test.get("satisfied_outcome_ids"), oids, label + ".satisfied_outcome_ids")
        failed = ids(test.get("failed_outcome_ids"), oids, label + ".failed_outcome_ids")
        require(not satisfied & failed, label + ": an outcome cannot both pass and fail")
        if classification == "INDEPENDENT_RESULTS" or (satisfied and failed):
            require(satisfied and failed and satisfied | failed == oids, label + ": independent results need a complete partial-success witness")
            finding("non_atomic", number, label, acceptance=False)
        elif classification == "UNRESOLVED":
            pending.append(label + ": unresolved atomicity")
        elif len(oids) != 1:
            require(False, label + ": ONE_RESULT cannot hide multiple required outcomes")
        inventory_open = validate_assertions(row.get("assertion_inventory"), criterion, atomic)
        exception = atomic.get("exception") or {}
        if exception.get("kind") == "coherent_record" and (
                classification == "UNRESOLVED" or known.get(exception.get("source_id"), {}).get("visibility") != "VISIBLE"):
            require(classification == "UNRESOLVED", label + ": unverifiable coherent-record exception needs unresolved atomicity")
            pending.append(label + ": unresolved coherent-record source")
        else:
            verify_record_source(atomic, reader, known)
        for item in inventory_open:
            if "multiple required assertions" in item or "per-entity properties" in item:
                finding("non_atomic", number, label, acceptance=False)
            elif "UNREQUESTED_REQUIREMENT" in item or "extra acceptance requirement" in item:
                finding("unauthorized", number, label)
            elif "hidden in a supporting field" in item:
                finding("not_self_contained", number, label, acceptance=False)
            else:
                pending.append(label + ": " + item)
        if any(i["type"] == "non_atomic" and number in i["rows"] and i.get("impact") == "precision_only" for i in issues):
            required_assertions = {a["id"] for a in row["assertion_inventory"]["assertions"] if a["role"] == "REQUIRED_RESULT"}
            require(len(required_assertions) > 1, label + ": precision-only bundle needs its separate assertions")
            controls = row.get("precision_controls")
            require(isinstance(controls, list), label + ": precision-only bundling needs set-wide catching controls")
            controlled = set()
            for control in controls:
                obj(control, label + ".precision_control")
                other = control.get("row")
                aid = control.get("assertion_id")
                require(type(other) is int and other in row_numbers and other != number and aid in required_assertions,
                        label + ": precision-only control must grade each component elsewhere")
                text(control.get("quote"), label + ": precision control predicate")
                text(control.get("reason"), label + ": precision control reason")
                require(control["quote"] in rubric[other-1]["title"], label + ": precision control quote missing from title")
                controlled.add(aid)
            require(controlled == required_assertions, label + ": precision-only controls must cover every bundled assertion")
        support = obj(row.get("supporting_fields"), label + ".supporting_fields")
        require(support.get("status") in {"PASS", "ISSUE", "UNRESOLVED"}, label + ": invalid supporting-fields status")
        text(support.get("reason"), label + ".supporting_fields.reason")
        if support["status"] == "ISSUE":
            text(support.get("witness"), label + ".supporting_fields.witness")
            require(any(number in i["rows"] and i["type"] in {"incorrect", "unauthorized", "not_self_contained"} for i in issues),
                    label + ": supporting-field conflict must be recorded as an issue")
        elif support["status"] == "UNRESOLVED":
            pending.append(label + ": unresolved supporting-field consistency")
        from hg_rubric_fact_binding import checked_facts
        facts_result = checked_facts(row.get('fact_review'), criterion, reader, known, root, context)
        fact_results.append({'row': number, **facts_result})
        if facts_result['mismatches']:
            finding('incorrect', number, label + ': source-derived fact mismatch')
        pending.extend(label + ': ' + item['reason'] for item in facts_result['unresolved'])

    recorded_missing = {i["outcome_id"]: i["criticality"] for i in issues if i["type"] == "missing_coverage"}
    require(recorded_missing == missing, "missing_coverage issues must exactly match the failed substantive outcome tests")
    # The AUDIT route must inspect the same restrictions and whole-set
    # alternatives as CREATE. Adapt the flat score ledger to the shared validator.
    from hg_rubric_acceptance import validate_acceptance
    acceptance_record = {**checks, 'requirements': [
        {**q, 'outcomes': [{k: q[k] for k in ('id', 'entity', 'property', 'output')}]}
        for q in checks['requirements']]}
    normalized = [{**r, **{k: r.get(k, r.get('annotations', {}).get(k, ''))
                           for k in ('justification', 'evidence')}} for r in rubric]
    pending.extend(validate_acceptance(acceptance_record, normalized, root, context,
                                      reader=reader, known=known, check_facts=False))
    for branch in checks['alternative_review']['branches']:
        if branch['validity'] == 'SUPPORTED' and branch['result'] == 'REJECT':
            for number in branch['rejecting_rows']:
                finding('incorrect', number, 'valid alternative rejected by R' + str(number))
    return dict(required_outcomes=len(requirements), covered_outcomes=len(covered),
                wording_fail_rows=wording_fail, wording_nonstandard_rows=wording_nonstandard,
                negative_fail_rows=negative_fail, unresolved=pending,
                fact_results=fact_results,
                sampling=sampling)
