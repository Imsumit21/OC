"""Validate declared sampling boundaries, not the truth of eligibility judgments.

Sampling compresses repetitive artifact checks; every supplied rubric row is
still reviewed. Missing reviewer metadata is not a new QC failure category.
"""

from hg_review_evidence import links


def validate_sampling(checks, requirements, known):
    def require(ok, message):
        if not ok:
            raise ValueError("Rubric sampling: " + message)

    def text(value, label):
        require(isinstance(value, str) and bool(value.strip()), label + " needs an explanation")

    def ids(value, label, nonempty=False):
        require(isinstance(value, list) and (bool(value) or not nonempty) and
                all(isinstance(i, str) and i in requirements for i in value) and
                len(value) == len(set(value)), label + " needs unique known outcome IDs")
        return set(value)

    groups = checks.get("sampling_groups", [])
    require(isinstance(groups, list), "sampling_groups must be an array")
    declared = set()
    for rid, req in requirements.items():
        basis = req.get("coverage_basis", "DIRECT")
        require(basis in {"DIRECT", "SPOT_CHECK"}, rid + ": invalid coverage_basis")
        if basis == "SPOT_CHECK":
            text(req.get("sampling_group"), rid + ".sampling_group")
            require(req.get("sampling_eligible") is True,
                    rid + ": a core/distinct or ineligible outcome cannot be a spot check")
            declared.add(rid)
        else:
            require("sampling_group" not in req and "sampling_eligible" not in req,
                    rid + ": sampling fields require SPOT_CHECK coverage_basis")

    seen_groups, sampled, pending, summaries = set(), set(), [], []
    for group in groups:
        require(isinstance(group, dict), "each sampling group must be an object")
        for key in ("id", "scope", "property", "output", "repetition_reason",
                    "comparable_importance_reason", "selection_reason",
                    "protected_review_reason", "edge_review_reason", "limitations"):
            text(group.get(key), "group." + key)
        gid = group["id"]
        require(gid not in seen_groups, "duplicate group ID " + gid)
        seen_groups.add(gid)
        source_refs = links(group.get("source_ids"), known, gid + ".source_ids")
        if any(s["visibility"] != "VISIBLE" for s in source_refs):
            pending.append(gid + ": unresolved/inaccessible sampling scope evidence")
        require(group.get("eligibility") in {"ELIGIBLE", "UNRESOLVED"},
                gid + ": establish sampling eligibility or leave it unresolved")
        if group["eligibility"] == "UNRESOLVED":
            pending.append(gid + ": unresolved sampling eligibility")
        controls = ids(group.get("control_outcome_ids"), gid + ".control_outcome_ids", True)
        protected = ids(group.get("protected_outcome_ids"), gid + ".protected_outcome_ids")
        require(not (controls | protected) & declared,
                gid + ": core/distinct outcomes and cohort controls require direct coverage")
        require(all(requirements[r]["output"].strip().casefold() == group["output"].strip().casefold()
                    for r in controls), gid + ": controls must address this output")
        samples = group.get("samples")
        require(isinstance(samples, list) and bool(samples), gid + ": identify the actual spot checks")
        group_samples, ordinary, edge_samples = set(), set(), set()
        for sample in samples:
            require(isinstance(sample, dict), gid + ": each sample must be an object")
            rid = sample.get("outcome_id")
            require(isinstance(rid, str) and rid in declared and rid not in sampled,
                    gid + ": samples need unique SPOT_CHECK outcome IDs")
            require(requirements[rid]["sampling_group"] == gid, rid + ": group binding differs")
            require(all(requirements[rid][key].strip().casefold() == group[key].strip().casefold()
                        for key in ("property", "output")),
                    rid + ": sample must check the same property on the same output")
            text(sample.get("reason"), rid + ": sample selection reason")
            kind = sample.get("case_kind")
            require(kind in {"ORDINARY", "EDGE"}, rid + ": identify ordinary or edge case")
            (ordinary if kind == "ORDINARY" else edge_samples).add(rid)
            group_samples.add(rid)
            sampled.add(rid)
        require(bool(ordinary), gid + ": include an ordinary representative case")

        edges = group.get("edge_cases")
        require(isinstance(edges, list), gid + ": edge_cases must be an array")
        require(type(group.get("edge_cases_complete")) is bool,
                gid + ": edge_cases_complete must be Boolean")
        if not group["edge_cases_complete"]:
            pending.append(gid + ": incomplete edge-case inventory")
        seen_edges, represented_edges = set(), set()
        for edge in edges:
            require(isinstance(edge, dict), gid + ": each edge case must be an object")
            for key in ("id", "description", "reason"):
                text(edge.get(key), gid + ".edge." + key)
            require(edge["id"] not in seen_edges, gid + ": duplicate edge-case ID")
            seen_edges.add(edge["id"])
            refs = ids(edge.get("outcome_ids"), gid + ".edge.outcome_ids", True)
            require(refs <= edge_samples | protected,
                    gid + ": each relevant edge needs an edge sample or protected direct outcome")
            represented_edges.update(refs & edge_samples)
        require(represented_edges == edge_samples,
                gid + ": every edge sample needs a corresponding edge-case explanation")
        summaries.append(dict(id=gid, controls=sorted(controls), samples=sorted(group_samples),
                              protected=sorted(protected)))
    require(sampled == declared, "every SPOT_CHECK outcome needs its sampling group and rationale")
    return dict(groups=summaries, sampled_outcomes=len(sampled), unresolved=pending)
