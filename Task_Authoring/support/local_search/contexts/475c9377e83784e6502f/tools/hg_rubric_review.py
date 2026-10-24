"""Validate review evidence completeness, not the truth of an LLM's judgments."""

from hg_rubric_assertions import validate_assertions

CHECKS = ("atomicity", "overly_specified", "self_contained", "process_supervision",
          "duplicates", "contradictory", "coverage", "accuracy_authority", "weights")
STATUSES = {"PASS", "ISSUE", "UNRESOLVED"}
RESULTS = {"ACCEPT", "REJECT", "UNRESOLVED"}
FORMAT_VERSION = 4
ATOMICITY_CLASSES = {"ONE_RESULT", "INDEPENDENT_RESULTS", "UNRESOLVED"}
ATOMIC_EXCEPTIONS = {"destination_identity", "identity_only_set",
                     "aggregate_invariant", "atomic_cell", "large_audit", "coherent_record", "same_tool_output", "shared_email_content"}
BINDING = ("review_policy", "review_iteration", "reviewed_json_sha256",
           "review_context_sha256")


def validate_record(record, proposal, receipt, publication=False, *, root):
    """Require a bound, exhaustive ledger and explicit behavioral challenges.

    A supplied case/result is a reviewer judgment, not an executed solver test.
    Publication additionally requires all recorded challenges/checks to clear.
    """
    def require(condition, message):
        if not condition:
            raise ValueError("Rubric review record: " + message)

    def obj(value, label):
        require(isinstance(value, dict), label + " must be an object")
        return value

    def string(value, label):
        require(isinstance(value, str) and bool(value.strip()), label + " needs substantive text")

    def array(value, label):
        require(isinstance(value, list) and bool(value), label + " must be a nonempty array")
        return value

    def row_ids(value, label):
        ids = array(value, label)
        require(all(type(x) is int and 1 <= x <= len(proposal) for x in ids),
                label + " contains an invalid row number")
        require(len(set(ids)) == len(ids), label + " contains duplicate rows")
        return set(ids)

    from hg_rubric_checks import title_facts
    open_items = []
    for i, row in enumerate(proposal, 1):
        facts = title_facts(row.get("title", ""))
        if facts["subject"] == "NON_AGENT" or facts["tool_names"]:
            open_items.append(f"R{i}: non-Agent subject or MCP tool identifier")

    def check(value, label):
        value = obj(value, label)
        require(isinstance(value.get("status"), str) and value["status"] in STATUSES,
                label + " needs PASS, ISSUE or UNRESOLVED")
        string(value.get("reason"), label + ".reason")
        if value["status"] != "PASS":
            open_items.append(label + ": " + value["status"])

    def case(value, label, expected):
        value = obj(value, label)
        for key in ("example", "reason"):
            string(value.get(key), label + "." + key)
        require(isinstance(value.get("result"), str) and value["result"] in RESULTS,
                label + " needs ACCEPT, REJECT or UNRESOLVED")
        if value["result"] != expected:
            open_items.append(label + ": expected " + expected)

    obj(record, "record")
    require(record.get("format_version") == FORMAT_VERSION and type(record.get("format_version")) is int,
            "unsupported format_version")
    require(all(record.get(k) == receipt.get(k) for k in BINDING),
            "binding differs from the current proposal/iteration/context")
    require(type(record.get("review_iteration")) is int, "review_iteration must be an integer")

    requirements, outcomes, covered_outcomes = {}, {}, set()
    for index, req in enumerate(array(record.get("requirements"), "requirements"), 1):
        obj(req, f"requirement {index}")
        for key in ("id", "authority", "accepted_result", "output", "source_evidence", "coverage_reason"):
            string(req.get(key), f"requirement {index}.{key}")
        rid = req["id"]
        require(rid not in requirements, "duplicate requirement " + rid)
        for outcome in array(req.get("outcomes"), rid + ".outcomes"):
            obj(outcome, rid + ".outcome")
            for key in ("id", "entity", "property", "output", "accepted_result"):
                string(outcome.get(key), rid + ".outcome." + key)
            oid = outcome["id"]
            require(oid not in outcomes, "duplicate outcome " + oid)
            outcomes[oid] = rid
        ids = row_ids(req.get("rows"), rid + ".rows")
        require(isinstance(req.get("coverage_mode"), str) and req["coverage_mode"] in {"direct", "sampled"},
                rid + " needs a coverage mode")
        if req["coverage_mode"] == "sampled":
            sample = obj(req.get("sampling"), rid + ".sampling")
            for key in ("eligibility", "limitations"):
                string(sample.get(key), rid + ".sampling." + key)
            for key in ("controls", "spot_checks"):
                require(row_ids(sample.get(key), rid + ".sampling." + key) <= ids,
                        rid + " sampling rows must be mapped to that requirement")
        requirements[rid] = req

    def outcome_ids(value, label, allowed, nonempty=True):
        require(isinstance(value, list) and (value or not nonempty), label + " must be an array" +
                (" with at least one outcome" if nonempty else ""))
        require(all(isinstance(x, str) and x in allowed for x in value), label + " references an unknown outcome")
        require(len(value) == len(set(value)), label + " repeats outcomes")
        return set(value)

    def atomicity(value, label, refs, row_number):
        check(value, label)
        allowed = {oid for oid, rid in outcomes.items() if rid in refs}
        ids = outcome_ids(value.get("outcome_ids"), label + ".outcome_ids", allowed)
        require({outcomes[oid] for oid in ids} == set(refs),
                label + " outcome links disagree with requirement_ids")
        covered_outcomes.update(ids)
        test = obj(value.get("independence_test"), label + ".independence_test")
        classification = test.get("classification")
        require(isinstance(classification, str) and classification in ATOMICITY_CLASSES,
                label + " needs ONE_RESULT, INDEPENDENT_RESULTS or UNRESOLVED")
        for key in ("example", "reason"):
            string(test.get(key), label + ".independence_test." + key)
        satisfied = outcome_ids(test.get("satisfied_outcome_ids"), label + ".satisfied_outcome_ids", ids, False)
        failed = outcome_ids(test.get("failed_outcome_ids"), label + ".failed_outcome_ids", ids, False)
        require(not satisfied & failed, label + " cannot both satisfy and fail the same outcome")
        plan = value.get("split_plan")
        require(isinstance(plan, list), label + ".split_plan must be an array")
        groups = [outcome_ids(group, label + ".split_plan group", ids) for group in plan]
        if classification == "INDEPENDENT_RESULTS":
            require(satisfied and failed and satisfied | failed == ids,
                    label + " needs a partial-success example covering its independent outcomes")
            require(all(len(group) == 1 for group in groups) and
                    len(groups) == len(ids) and set().union(*groups) == ids,
                    label + " split_plan must separate every independent outcome exactly once")
            # Even a contradictory PASS label or an exception claim cannot clear this.
            open_items.append(label + ": independently required results need splitting")
        else:
            require(not plan, label + ": split_plan is only for INDEPENDENT_RESULTS")
            if classification == "UNRESOLVED":
                open_items.append(label + ": unresolved independence test")
            elif len(ids) != 1:
                open_items.append(label + ": ONE_RESULT cannot cover multiple declared outcomes")
        require("exception" in value, label + ".exception must be null or a justified exception")
        exception = value["exception"]
        if exception is not None:
            obj(exception, label + ".exception")
            kind = exception.get("kind")
            require(isinstance(kind, str) and kind in ATOMIC_EXCEPTIONS,
                    label + ": unknown atomic exception")
            string(exception.get("reason"), label + ".exception.reason")
            if kind == "large_audit":
                require(any(requirements[rid]["coverage_mode"] == "sampled" and
                            row_number in (requirements[rid]["sampling"]["controls"] +
                                           requirements[rid]["sampling"]["spot_checks"])
                            for rid in refs),
                        label + ": large_audit needs mapped sampled controls/spot checks")

    rows = array(record.get("rows"), "rows")
    require(len(rows) == len(proposal), "one review row is required for every proposal row")
    seen = set()
    for row in rows:
        obj(row, "row")
        i = row.get("row")
        require(type(i) is int and 1 <= i <= len(proposal) and i not in seen,
                "missing, duplicate or invalid review row number")
        seen.add(i)
        label = f"R{i}"
        for key in ("predicate", "output", "source_evidence"):
            string(row.get(key), label + "." + key)
        refs = array(row.get("requirement_ids"), label + ".requirement_ids")
        require(all(isinstance(x, str) and x in requirements for x in refs),
                label + " references an unknown requirement")
        require(len(refs) == len(set(refs)), label + " repeats requirement IDs")
        expected = {rid for rid, req in requirements.items() if i in req["rows"]}
        require(set(refs) == expected, label + " disagrees with forward/reverse requirement coverage")
        case(row.get("valid_case"), label + ".valid_case", "ACCEPT")
        case(row.get("near_miss"), label + ".near_miss", "REJECT")
        atomicity(row.get("atomicity"), label + ".atomicity", refs, i)
        open_items.extend(label + ": " + item for item in
                          validate_assertions(row.get("assertion_inventory"), proposal[i-1], row["atomicity"]))
        check(row.get("supporting_fields"), label + ".supporting_fields")

    require(covered_outcomes == set(outcomes), "every declared outcome needs mapped rubric coverage")

    checks = obj(record.get("set_checks"), "set_checks")
    require(set(checks) == set(CHECKS), "set_checks must contain all nine named checks")
    for name in CHECKS:
        check(checks[name], "set_checks." + name)

    tests = obj(record.get("set_tests"), "set_tests")
    case(tests.get("valid_completion"), "set_tests.valid_completion", "ACCEPT")
    case(tests.get("final_reply"), "set_tests.final_reply", "ACCEPT")
    string(tests["final_reply"].get("authority"), "set_tests.final_reply.authority")
    mutations = array(tests.get("mutations"), "set_tests.mutations")
    tested = set()
    for index, mutation in enumerate(mutations, 1):
        label = f"set_tests.mutations[{index}]"
        case(mutation, label, "REJECT")
        rid = mutation.get("requirement_id")
        require(isinstance(rid, str) and rid in requirements, label + " needs a known requirement_id")
        tested.add(rid)
        caught = mutation.get("caught_by")
        require(isinstance(caught, list), label + ".caught_by must be an array")
        if mutation["result"] == "REJECT":
            require(row_ids(caught, label + ".caught_by") <= set(requirements[rid]["rows"]),
                    label + " cites a row not mapped to its requirement")
        else:
            require(not caught, label + " cannot claim catching rows without rejection")
    require(tested == set(requirements), "every requirement needs a whole-rubric wrong-result test")
    from hg_rubric_acceptance import validate_acceptance

    open_items.extend(validate_acceptance(record, proposal, root, receipt.get("context", {})))
    if publication:
        require(not open_items, "unresolved/failed checks block publication: " + "; ".join(open_items))
    return {"review_rows": len(rows), "review_requirements": len(requirements),
            "review_outcomes": len(outcomes),
            "review_open_items": open_items}
