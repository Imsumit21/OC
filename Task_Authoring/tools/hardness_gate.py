#!/usr/bin/env python3
"""Hardness gate: hardness is measured, not claimed.

Cross-checks the engine's hardness manifest (task_inputs/Working_Files/01_Hardness_Manifest.json)
against the injection SQL itself, so a design that only *says* it spans 13 services,
500+ calls and dozens of traps cannot pass. Every seeded id the manifest cites must
literally appear in the SQL; every injected schema must be used by the design (no
padding); thresholds come from a profile.

Usage:
  python3 Task_Authoring/tools/hardness_gate.py \
      Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.json \
      Task_Authoring/task_inputs/01_Universe_Inject.sql [--profile extreme|normal] [--json]
  python3 Task_Authoring/tools/hardness_gate.py Task_Authoring/task_inputs/Working_Files/01_Hardness_Manifest.draft.json --design
  python3 Task_Authoring/tools/hardness_gate.py --self-test     (reruns itself inside a tools/selftest_sandbox.py
              workspace: the hg.py and persona_view caches it reaches are written only there)

The profile is the manifest's `effective_profile` (a task property, resolved once). `--profile` is only a
cross-check: a value that disagrees with the manifest FAILs check `effective_profile`.

Red team A (2026-10-05, support/examples/calibration/harness_redteam/A_scenario_injection*.md) checks:
  effective_profile        effective_profile present; Long Horizon = extreme; Normal Horizon at extreme only with a
                           profile_exception {reason, requester_confirmation}; --profile must agree
  incorporation_chains     + each fragment's `delegation_quote` is an exact substring of the text of its
                           delegated_by_record (seeded SQL row, or the base record read through tools/hg.py)
  requirement_coverage     every declared requirement is named by >= 1 incorporated fragment or anchor (requirement_ids)
  authority_incorporation  every authority is named (names_authorities [{id, quote}], quote in the fragment's own record)
  surface_requirements     every cohort surface has a declared, incorporated `requirement` and a `decides` the
                           requirement's summary states (no manufactured output columns)
  call_budget              rows with `conditional_on` count 0 toward the profile minimum (both totals shown)
  decoy_scope              each authority's decoy declares decoy_scope {dimension lot|team|game|issuer, decoy, task}
                           or is an older entry of a trap's version_records (time-ordered supersession)
  supersession_chronology  version_records timestamps read from the SQL rows / base records, strictly increasing
  independent_chains       root_cause from the Hardness_Mastery.md mechanism enum; distinct = distinct ids

Fold-hardening plan §8 (fields optional, so legacy manifests stay valid; malformed entries FAIL):
  mechanism_portfolio      one entry per solver rule: unique id, mechanism from the enum (A22/A23 are library
                           hypotheses), nodes that are trap or chain ids, requirement, natural_reading, prior_family
                           (legacy: family) and prior_family_reason (why that family's ledger evidence applies)
  artifact_fields          gradable_surface (path), solver {path, digest}, preflight {report, digest}: relative paths
                           and 64-hex sha256 digests (tools/stage_gate.py verifies the digests against the files)

Full mode (manifest + SQL) also runs the integrity layer:
  persona_reach     every seeded id cited by ask_fragments, authorities, traps, chains and cohort
                    surfaces must be provably visible to the manifest's persona (persona_view.py
                    check-sql: NO or UNVERIFIED = FAIL; unscoped services are visible to all). The only
                    exception is a `denied_probes` entry {record, reason, alternate_evidence_ids[]}: a NO
                    record cited only by traps or as a decoy, whose alternates are all YES. UNVERIFIED
                    never satisfies a dependency
  fact_consistency  tools/fact_check.py --no-leak errors (declared `facts`, home_ids leaks, unresolved ids) = FAIL
  hazard_scope      task-touched records (SQL-touched or manifest-cited) in a state/lifecycle or
                    referential hazard of universe_kb/coherence_hazards.json need an entry in
                    `hazard_acknowledgements` [{hazard_id, resolution, why_safe, requirement?}];
                    resolution: excluded (record neither modified nor cited by the design) |
                    repaired (base_check verifies the predicate on the post-SQL state) |
                    dated_claim (text claims only, never a record the SQL modifies)
  base_consistency  runs base_check with the manifest (integration_exceptions, acknowledgements)

Manifest format: references/Hardness_Manifest_Spec.md.
Exit 0 = PASS, 1 = FAIL, 2 = usage/parse error.
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from sql_lint import lint, load_schema  # noqa: E402

SERVICES = ["slack", "gmail", "gcal", "gdrive", "gdocs", "gsheets", "gslides", "contacts",
            "github", "linear", "trello", "confluence", "snowflake"]

PROFILES = {
    # The user-set default: 10+ of 13 services, 500+ necessary calls, very long injection.
    "extreme": dict(services_weight=10, services_injected=10, rows=120, anchors_max=3,
                    fragments=12, fragment_services=7, fragment_containers=10,
                    cohort=40, surfaces=3, surface_services=2, per_record_calls=300,
                    budget=500, budget_services=10, budget_max_share=0.50,
                    traps=12, trap_families=7, trap_requirements=6,
                    supersessions=4, supersession_cross_service=2, supersession_3_versions=1,
                    distractors=6, distractor_types=4, writes=4, write_services=3, shifts=4,
                    chains=3, chain_hops=3, authorities=2, rare_traps=3),
    # Normal Horizon: the golden run must stay inside 50–100 calls, so the budget is capped at 95 (margin: a
    # Normal run above 100 is a NON-FAIL; Reaching the Tool-Call Minimum, 2026-10);
    # difficulty comes from authorities, chains and traps rather than volume.
    "normal": dict(services_weight=7, services_injected=6, rows=50, anchors_max=3,
                   fragments=7, fragment_services=5, fragment_containers=6,
                   cohort=10, surfaces=2, surface_services=2, per_record_calls=25,
                   budget=60, budget_cap=95, budget_services=6, budget_max_share=0.40,
                   traps=8, trap_families=5, trap_requirements=4,
                   supersessions=2, supersession_cross_service=1, supersession_3_versions=0,
                   distractors=4, distractor_types=3, writes=2, write_services=2, shifts=2,
                   chains=2, chain_hops=3, authorities=1, rare_traps=2),
}
TRAP_FAMILIES = {"superseding", "distractor", "tool_surface", "scope_alias", "stale_summary",
                 "reuse_exclusion", "effective_date", "authority", "pagination", "exact_predicate",
                 "acl_alternate", "friction", "synthesis_omission", "eliminating_evidence",
                 "conclusion_stop", "entity_collision", "unit_or_timezone", "cross_reference_gap",
                 "near_miss_mention", "mutable_pointer", "done_gap", "completion_elsewhere"}
# Services Opus opened in fewer than half of 131 baseline runs (V0/V1 trajectory forensics).
RARELY_OPENED = {"gmail", "gsheets", "trello", "snowflake", "gslides", "gcal"}
AUTHORITY_HOMES = RARELY_OPENED | {"gdocs"}
# Mechanism ids for chains[].root_cause (references/Hardness_Mastery.md "Mechanism id enum"): A1-A21 (§0) and the
# §2.6 red-team items 2.6.1-2.6.14. Distinct root causes = distinct ids (harness red team A, R2 #6).
# A22 (cross-shard dependency: a record's value depends on evidence attached to another cohort member) and A23
# (brief-transmission loss: an exception rule homed outside the main instructions, applying to an unpredictable
# subset) are hypotheses in the library (plans/Fold_Hardening_Into_Scenario_And_Injection.md §6, §8): usable ids, not
# yet measured mechanisms. A24 (done across services: one source says finished, another service shows a required
# piece missing) and A25 (completion elsewhere: an item looks open but a record in another place shows it done) come
# from Hardness v2 (references/Docs/13_Hardness_v2_Opus55.md, Part 3 traps 1 and 9: 46 Opus 5.5 tasks); their
# families are done_gap and completion_elsewhere (Hardness_Mastery.md §13).
MECHANISM_IDS = {f"A{i}" for i in range(1, 26)} | {f"2.6.{i}" for i in range(1, 15)}
HYPOTHESIS_IDS = {"A22", "A23"}
RX_SHA256 = re.compile(r"^[0-9a-f]{64}$")
DECOY_DIMENSIONS = {"lot", "team", "game", "issuer"}
DISTRACTOR_TYPES = {"lookalike_entity", "near_duplicate_record", "non_authoritative_instruction",
                    "stale_summary", "partial_listing", "keyword_collision", "scope_adjacent",
                    "already_done", "withdrawn_ask", "other_title"}


def _code_only(sql_text: str) -> str:
    """SQL without full-line comments, so an id that appears only in a comment does not count."""
    return "\n".join(line for line in sql_text.splitlines() if not line.lstrip().startswith("--"))


def _has_token(code: str, token: str) -> bool:
    """Exact token match: the id must not be a prefix/suffix of a longer id."""
    return bool(token) and re.search(r"(?<![A-Za-z0-9_.\-])" + re.escape(token) + r"(?![A-Za-z0-9_\-])", code) is not None


def resolve_profile(manifest: dict, cli_profile: str | None = None) -> tuple:
    """(profile, problems): the manifest's effective_profile is the task's single profile (red team A, R1 #17)."""
    eff = manifest.get("effective_profile")
    horizon = manifest.get("horizon", "")
    probs = []
    if eff not in PROFILES:
        probs.append(f"effective_profile {eff!r} missing or not one of {sorted(PROFILES)}")
    if horizon not in ("Normal Horizon", "Long Horizon"):
        probs.append(f"horizon {horizon!r} is not 'Normal Horizon' or 'Long Horizon' — copy the assigned tier verbatim")
    if cli_profile and eff in PROFILES and cli_profile != eff:
        probs.append(f"--profile {cli_profile} disagrees with the manifest's effective_profile {eff}")
    if horizon == "Long Horizon" and eff == "normal":
        probs.append("Long Horizon at the normal profile fails Wrong Horizon — effective_profile must be extreme")
    if horizon == "Normal Horizon" and eff == "extreme":
        ex = manifest.get("profile_exception") or {}
        if not (isinstance(ex, dict) and str(ex.get("reason") or "").strip() and str(ex.get("requester_confirmation") or "").strip()):
            probs.append("Normal Horizon at the extreme profile (Borderline Horizon, score capped at 3) needs profile_exception "
                         "{reason, requester_confirmation} recording the requester's confirmation")
    profile = eff if eff in PROFILES else (cli_profile if cli_profile in PROFILES else "extreme")
    return profile, probs


def _declared(manifest: dict) -> dict:
    reqs = manifest.get("requirements", [])
    if isinstance(reqs, dict):
        return {str(k): str(v) for k, v in reqs.items()}
    out = {}
    for r in reqs or []:
        if isinstance(r, dict):
            out[str(r.get("id"))] = str(r.get("summary") or "")
        else:
            out[str(r)] = ""
    return out


def _norm(s: str) -> str:
    return re.sub(r"\s+", " ", str(s or "").replace("\\n", "\n")).strip()


def portfolio_check(manifest: dict, traps: list, chains: list, check) -> None:
    """mechanism_portfolio[]: one entry per solver rule (tools/oracle_kit.py matches the rules one-to-one)."""
    port = manifest.get("mechanism_portfolio")
    if port is None:
        check("mechanism_portfolio", True, "not declared (legacy manifest; /create-scenario S5a writes it for new tasks)")
        return
    nodes = {t.get("id") for t in traps} | {c.get("id") for c in chains}
    bad = []
    if not isinstance(port, list) or not port:
        bad.append("must be a non-empty list")
        port = []
    ids = [p.get("id") if isinstance(p, dict) else None for p in port]
    dup = sorted({i for i in ids if i and ids.count(i) > 1})
    if dup:
        bad.append(f"duplicate ids {dup}")
    for p in port:
        if not isinstance(p, dict) or not p.get("id"):
            bad.append("an entry without an id")
            continue
        pid = p["id"]
        if p.get("mechanism") not in MECHANISM_IDS:
            bad.append(f"{pid}: mechanism {p.get('mechanism')!r} not in the mechanism enum")
        unknown = [n for n in p.get("nodes") or [] if n not in nodes]
        if not p.get("nodes") or unknown:
            bad.append(f"{pid}: nodes {unknown or 'missing'} are not trap or chain ids")
        for f in ("requirement", "natural_reading"):
            if not str(p.get(f) or "").strip():
                bad.append(f"{pid}: {f} missing")
        if not str(p.get("prior_family") or p.get("family") or "").strip():
            bad.append(f"{pid}: prior_family missing (the ledger family the forecast takes the rule's prior from)")
        if not str(p.get("prior_family_reason") or "").strip():
            bad.append(f"{pid}: prior_family_reason missing (why that family's evidence applies to this rule)")
    hyp = sorted({p.get("mechanism") for p in port if isinstance(p, dict) and p.get("mechanism") in HYPOTHESIS_IDS})
    check("mechanism_portfolio", not bad,
          f"{len(port)} portfolio entr{'y' if len(port) == 1 else 'ies'}, each a mechanism-enum id with trap/chain nodes, "
          f"a requirement, a natural-reading fallback and a prior family with its reason"
          + (f"; hypothesis ids {hyp} (library hypotheses)" if hyp else "")
          + (f"; bad: {bad[:6]}" if bad else ""))


def artifact_fields_check(manifest: dict, check) -> None:
    """gradable_surface / solver / preflight: paths and digests (stage_gate.py verifies them against the files)."""
    bad, seen = [], []

    def path_ok(v, where):
        if not isinstance(v, str) or not v.strip() or v.startswith("/") or ".." in Path(v).parts:
            bad.append(f"{where}: path {v!r} must be relative to the manifest's folder")

    if "gradable_surface" in manifest:
        seen.append("gradable_surface")
        g = manifest["gradable_surface"]
        path_ok(g.get("path") if isinstance(g, dict) else g, "gradable_surface")
        if isinstance(g, dict) and g.get("digest") is not None and not RX_SHA256.match(str(g["digest"])):
            bad.append("gradable_surface: digest must be a 64-hex sha256")
    for field, pkey in (("solver", "path"), ("preflight", "report")):
        if field not in manifest:
            continue
        seen.append(field)
        v = manifest[field]
        if not isinstance(v, dict):
            bad.append(f"{field}: must be {{{pkey}, digest}}")
            continue
        path_ok(v.get(pkey), field)
        if not RX_SHA256.match(str(v.get("digest") or "")):
            bad.append(f"{field}: digest must be a 64-hex sha256")
    check("artifact_fields", not bad, (f"declared {seen}: paths relative, digests sha256" if seen else
                                       "none declared (legacy manifest; /create-injection writes them)")
          + (f"; bad: {bad}" if bad else ""))


def evaluate(manifest: dict, sql_text: str, profile: str | None = None, design: bool = False, records=None,
             integrity: bool = True) -> dict:
    from runtime_context import ensure_active
    ensure_active(globals(), require_source=True)
    profile, profile_probs = resolve_profile(manifest, profile)
    p = PROFILES[profile]
    checks: list[dict] = []

    sql_only = {"sql_lint_clean", "services_injected", "rows", "no_orphan_injection", "seeded_ids_exist_in_sql", "base_consistency",
                "persona_reach", "fact_consistency", "hazard_scope", "supersession_chronology"}

    def check(name: str, ok: bool, detail: str) -> None:
        if design and name in sql_only:
            checks.append({"check": name, "ok": True, "detail": "skipped (--design: no SQL yet)"})
            return
        checks.append({"check": name, "ok": bool(ok), "detail": detail})

    context = globals().get("TASK_CONTEXT")
    if context:
        expected = {k: context[k] for k in ("context_hash", "assignment_hash", "policy_hash", "freeze_utc", "difficulty_mode")}
        bound = manifest.get("assignment_context") or {}
        mismatch = [key for key, value in expected.items() if bound.get(key) != value]
        check("assignment_context", not mismatch,
              "manifest bound to current V3 assignment, freeze and policy" if not mismatch else
              "manifest assignment_context missing/stale: " + ", ".join(mismatch))
    check("effective_profile", not profile_probs,
          f"effective_profile {manifest.get('effective_profile')!r} for {manifest.get('horizon')!r} → thresholds '{profile}'"
          + (f"; {'; '.join(profile_probs)}" if profile_probs else ""))
    rt = records or RecordText(sql_text, design)

    lint_result = lint(sql_text, load_schema())
    stats = lint_result["stats"]
    injected = [s for s in stats["schemas_touched"] if s in SERVICES]

    code = _code_only(sql_text)

    def in_sql(token: str) -> bool:
        return design or _has_token(code, token)

    check("sql_lint_clean", not lint_result["errors"],
          f"{len(lint_result['errors'])} lint error(s) — run tools/sql_lint.py")
    if not design and sql_text.strip() and integrity:
        from base_check import Base, check as base_consistency  # /injection Checks A + C against the base data
        base = Base()
        bc = base_consistency(sql_text, base, manifest)
        check("base_consistency", bc["verdict"] == "PASS",
              f"/injection-style checks vs the base universe: A {len(bc['check_A'])} finding(s), C {len(bc['check_C'])} finding(s), "
              f"{len(bc.get('warnings', []))} warning(s) — run tools/base_check.py --manifest")
        # integrity layer (full mode only): persona reach, fact consistency, hazard scope
        for c in integrity_checks(manifest, sql_text, base=base, base_result=bc):
            check(c["check"], c["ok"], c["detail"])
    else:
        check("base_consistency", True, "skipped (--design: no SQL yet)")
    check("services_injected", len(injected) >= p["services_injected"],
          f"{len(injected)} schemas injected ({', '.join(injected)}); need ≥ {p['services_injected']}")
    inserts = stats.get("ops", {}).get("insert", stats["total_rows"])
    check("rows", inserts >= p["rows"],
          f"{inserts} INSERTed rows (UPDATE companions not counted; {stats['total_rows']} rows in all); need ≥ {p['rows']}")

    services = manifest.get("services", {})
    weighted = [s for s, v in services.items() if s in SERVICES and v.get("weight_reason")]
    check("services_carrying_weight", len(weighted) >= p["services_weight"],
          f"{len(weighted)} services with a weight_reason; need ≥ {p['services_weight']}")
    unused = [s for s in injected if s not in services]
    check("no_orphan_injection", not unused, f"schemas injected but absent from the design: {unused or 'none'}")

    # every seeded id cited anywhere in the manifest must exist in the SQL
    cited = []
    for section in ("ask_fragments", "traps", "authorities"):
        for item in manifest.get(section, []):
            cited += [(section, item.get("id"), sid) for sid in item.get("seeded_ids", [])]
            cited += [(section, item.get("id"), d) for d in item.get("decoy_seeded_ids", [])]
    for t in manifest.get("traps", []):
        cited += [("traps", t.get("id"), v.get("id")) for v in t.get("version_records", []) if v.get("seeded")]
    missing = [f"{sec}:{iid}:{sid}" for sec, iid, sid in cited if not in_sql(sid)]
    check("seeded_ids_exist_in_sql", cited and not missing,
          f"{len(cited)} seeded ids cited; missing from SQL: {missing[:8] or 'none'}")

    anchors = {a["id"]: a for a in manifest.get("anchors", [])}
    check("anchors", 1 <= len(anchors) <= p["anchors_max"] and all(a.get("prompt_reference") for a in anchors.values()),
          f"{len(anchors)} anchors (1–{p['anchors_max']}, each with a plain-language prompt_reference)")

    frags = manifest.get("ask_fragments", [])
    frag_ids = {f["id"] for f in frags}
    f_services = {f.get("service") for f in frags}
    f_containers = {f.get("container") for f in frags if f.get("container")}
    check("ask_fragments", len(frags) >= p["fragments"], f"{len(frags)} fragments; need ≥ {p['fragments']}")
    check("ask_fragment_services", len(f_services) >= p["fragment_services"],
          f"{len(f_services)} services carry asks; need ≥ {p['fragment_services']}")
    check("ask_fragment_containers", len(f_containers) >= p["fragment_containers"],
          f"{len(f_containers)} distinct containers; need ≥ {p['fragment_containers']}")
    broken = []
    by_id = {f["id"]: f for f in frags}

    def reaches_anchor(fid: str) -> bool:
        """Follow each fragment's immediate delegator (last link of incorporated_via) to an anchor."""
        seen, cur = set(), fid
        while cur not in anchors:
            if cur in seen or cur not in by_id:
                return False
            seen.add(cur)
            chain = by_id[cur].get("incorporated_via", [])
            if not chain:
                return False
            cur = chain[-1]
        return True

    declared = _declared(manifest)
    auth_ids = {a.get("id") for a in manifest.get("authorities", [])}
    bad_req_ids = []
    for item in list(anchors.values()) + frags:
        bad_req_ids += [f"{item.get('id')}:{r}" for r in item.get("requirement_ids", []) or [] if r not in declared]
    named_auth, bad_names = {}, []
    for f in frags:
        chain = f.get("incorporated_via", [])
        if f["id"] in chain:
            broken.append(f"{f['id']} (cites itself)")
        for link in chain:
            if link not in anchors and link not in frag_ids:
                broken.append(f"{f['id']}→{link} (unknown)")
        if not reaches_anchor(f["id"]):
            broken.append(f"{f['id']} (never reaches an anchor)")
        if not (f.get("seeded_ids") or f.get("base_pointers")):
            broken.append(f"{f['id']} (no record)")
        # The delegating words must live in the immediate delegator's own record (red team, sample_task_02:
        # a manifest label is not a delegation the agent can see).
        if chain:
            parent = chain[-1]
            src = anchors.get(parent) or by_id.get(parent) or {}
            parent_records = set(src.get("seeded_ids", [])) | set(src.get("base_pointers", [])) | {src.get("locator")}
            ev = f.get("delegated_by_record")
            quote = str(f.get("delegation_quote") or "").strip()
            if not ev:
                broken.append(f"{f['id']} (no delegated_by_record)")
            elif ev not in parent_records:
                broken.append(f"{f['id']} (delegated_by_record {ev} is not a record of {parent})")
            elif not quote:
                broken.append(f"{f['id']} (no delegation_quote: the delegating words, verbatim from {ev})")
            else:
                found, why = rt.contains(ev, quote)
                if found is False:
                    broken.append(f"{f['id']} (delegation_quote {quote[:40]!r} is not in the text of {ev}: {why})")
        # authorities this fragment names: the quote must be in the fragment's own record
        own = list(f.get("seeded_ids", []) or []) + list(f.get("base_pointers", []) or [])
        for na in f.get("names_authorities", []) or []:
            aid = na.get("id") if isinstance(na, dict) else na
            q = str(na.get("quote") or "").strip() if isinstance(na, dict) else ""
            if aid not in auth_ids:
                bad_names.append(f"{f['id']}→{aid} (unknown authority)")
            elif not q:
                bad_names.append(f"{f['id']}→{aid} (no quote naming it)")
            else:
                hits = [rt.contains(r, q) for r in own]
                if hits and all(h[0] is False for h in hits):
                    bad_names.append(f"{f['id']}→{aid} (quote {q[:40]!r} not in {own[:2]}: {hits[0][1]})")
                elif not own:
                    bad_names.append(f"{f['id']}→{aid} (fragment has no record)")
                else:
                    named_auth.setdefault(aid, []).append(f["id"])
    check("incorporation_chains", not broken and not bad_req_ids,
          f"every fragment must chain back to a prompt anchor through explicit delegations whose words "
          f"(delegation_quote) are in the delegating record; broken: {broken[:8] or 'none'}"
          + (f"; requirement_ids not declared: {bad_req_ids[:6]}" if bad_req_ids else ""))
    broken_ids = {b.split(" ", 1)[0].split("→", 1)[0] for b in broken}
    incorporated = [f for f in frags if f["id"] not in broken_ids and reaches_anchor(f["id"])]
    covered = {r for f in incorporated for r in f.get("requirement_ids", []) or []} | \
              {r for a in anchors.values() for r in a.get("requirement_ids", []) or []}
    orphan_reqs = sorted(r for r in declared if r not in covered)
    check("requirement_coverage", bool(declared) and not orphan_reqs,
          f"{len(declared)} declared requirements; each must be named (requirement_ids) by an incorporated fragment or an "
          f"anchor — orphan requirements (graded with no source the prompt reaches): {orphan_reqs[:10] or 'none'}")
    # an authority is also incorporated when an incorporated fragment's own record IS the authority's record: the chain
    # delegates to it, and that fragment's delegation_quote proves the words
    inc_records = {str(r) for f in incorporated for r in list(f.get("seeded_ids", []) or []) + list(f.get("base_pointers", []) or [])}
    for a in manifest.get("authorities", []):
        if {str(r) for r in list(a.get("seeded_ids", []) or []) + list(a.get("base_pointers", []) or [])} & inc_records:
            named_auth.setdefault(a.get("id"), []).append("delegated")
    orphan_auth = sorted(a for a in auth_ids if a not in named_auth)
    check("authority_incorporation", not orphan_auth and not bad_names,
          f"every authority must be named by a fragment's own record (names_authorities [{{id, quote}}]) or be the record an "
          f"incorporated fragment delegates to; orphan authorities: {orphan_auth or 'none'}"
          + (f"; unverified namings: {bad_names[:5]}" if bad_names else ""))

    cohort = manifest.get("cohort", {})
    surfaces = cohort.get("evidence_surfaces", [])
    s_services = {s.get("service") for s in surfaces}
    size = int(cohort.get("size", 0))
    per_record = sum(float(s.get("per_record_calls", 0)) * int(s.get("records", size)) for s in surfaces)
    per_record = int(per_record)
    check("cohort_size", int(cohort.get("size", 0)) >= p["cohort"],
          f"cohort {cohort.get('size', 0)}; need ≥ {p['cohort']} (source-defined: {bool(cohort.get('definition_source'))})")
    check("evidence_surfaces", len(surfaces) >= p["surfaces"] and len(s_services) >= p["surface_services"]
          and all(s.get("why_no_bulk") for s in surfaces)
          and (p["cohort"] < 40 or all(s.get("short_circuit") for s in surfaces)),
          f"{len(surfaces)} surfaces over {len(s_services)} services; each needs why_no_bulk and (extreme) a short_circuit "
          f"analysis — why a correct run cannot skip it once other surfaces decide the record "
          f"(missing: {[s.get('tool') for s in surfaces if not s.get('short_circuit')][:5] or 'none'})")
    inc_reqs = {r for f in incorporated for r in f.get("requirement_ids", []) or []}
    bad_surface = []
    for s in surfaces:
        r, dec = s.get("requirement"), _norm(s.get("decides")).lower()
        name = s.get("tool") or s.get("service")
        if not r or r not in declared:
            bad_surface.append(f"{name} (requirement {r!r} not declared)")
        elif r not in inc_reqs:
            bad_surface.append(f"{name} ({r} not carried by an incorporated fragment)")
        elif not dec:
            bad_surface.append(f"{name} (no `decides`: the output column or decision {r} states)")
        elif dec not in _norm(declared.get(r)).lower():
            bad_surface.append(f"{name} (decides {s.get('decides')!r} is not stated by {r}: {declared.get(r)[:60]!r})")
    check("surface_requirements", bool(surfaces) and not bad_surface,
          f"every cohort surface must serve a declared, incorporated requirement and the output column or decision it "
          f"states (`requirement`, `decides`) — no manufactured columns; bad: {bad_surface[:6] or 'none'}")
    check("per_record_calls", per_record >= p["per_record_calls"],
          f"Σ per-record calls × records each surface applies to = {per_record}; need ≥ {p['per_record_calls']}")

    budget = manifest.get("call_budget", [])
    total = sum(int(b.get("calls", 0)) for b in budget)
    # verified floor (red team A, R1 #6/15): a row that depends on unverified tool behaviour counts 0
    floor = sum(int(b.get("calls", 0)) for b in budget if not b.get("conditional_on"))
    by_service = Counter()
    for b in budget:
        by_service[b.get("service")] += int(b.get("calls", 0))
    # The share cap protects breadth in discovery/rules/writes; the per-record spine may concentrate
    # (at scale only Linear comments are honestly per-record — Hardness_Mastery §2.5).
    non_spine = Counter()
    for b in budget:
        if b.get("phase") != "per-record":
            non_spine[b.get("service")] += int(b.get("calls", 0))
    ns_total = sum(non_spine.values())
    share = max(non_spine.values()) / ns_total if ns_total else 1.0
    cap = p.get("budget_cap")
    unexplained = [f"{b.get('phase')}/{b.get('service')}" for b in budget if not b.get("reason")]
    check("call_budget", floor >= p["budget"] and (cap is None or total <= cap) and not unexplained,
          f"unconditional (verified) floor {floor} of {total} planned calls ({total - floor} conditional on unverified tool "
          f"behaviour count 0); need floor ≥ {p['budget']}" + (f" and total ≤ {cap} (Normal Horizon 50–100, with margin below the 100 NON-FAIL line)" if cap else " (Long Horizon; plan ~600 for headroom)")
          + (f"; rows without a necessity reason: {unexplained[:5]}" if unexplained else ""))
    check("call_budget_spread", len([s for s, c in by_service.items() if c > 0]) >= p["budget_services"]
          and share <= p["budget_max_share"],
          f"{len(by_service)} services in budget; largest share outside the per-record phase {share:.0%} (≤ {p['budget_max_share']:.0%})")

    traps = manifest.get("traps", [])
    families = Counter(t.get("family") for t in traps)
    bad_family = [t.get("id") for t in traps if t.get("family") not in TRAP_FAMILIES]
    reqs = {t.get("requirement") for t in traps if t.get("requirement")}
    incomplete = [t.get("id") for t in traps
                  if not (t.get("seeded_ids") or t.get("base_pointers")) or not t.get("resolver")
                  or not t.get("expected_wrong_reading")]
    check("traps", len(traps) >= p["traps"] and len(families) >= p["trap_families"] and not bad_family,
          f"{len(traps)} traps across {len(families)} families; need ≥ {p['traps']} / ≥ {p['trap_families']}; unknown family: {bad_family or 'none'}")
    check("trap_independence", len(reqs) >= p["trap_requirements"],
          f"traps hit {len(reqs)} distinct requirements; need ≥ {p['trap_requirements']} (failure-pattern diversity)")
    check("trap_completeness", not incomplete,
          f"each trap needs records, a resolver and the expected wrong reading; incomplete: {incomplete[:8] or 'none'}")

    sup = [t for t in traps if t.get("family") in ("superseding", "effective_date")]
    def _ordered(vs: list) -> bool:
        stamps = []
        for v in vs:
            try:
                stamps.append(datetime.fromisoformat(str(v.get("at", "")).replace("Z", "+00:00")))
            except ValueError:
                return False
        return all(a <= b for a, b in zip(stamps, stamps[1:]))

    no_versions = [t.get("id") for t in sup
                   if len(t.get("version_records", [])) < 2
                   or not all(v.get("service") and (v.get("id") or v.get("base_pointer")) for v in t.get("version_records", []))
                   or not _ordered(t.get("version_records", []))]
    cross = [t for t in sup if len({v.get("service") for v in t.get("version_records", [])}) >= 2]
    deep = [t for t in sup if len(t.get("version_records", [])) >= 3]
    check("supersession", len(sup) >= p["supersessions"] and len(cross) >= p["supersession_cross_service"]
          and len(deep) >= p["supersession_3_versions"] and not no_versions,
          f"{len(sup)} supersessions ({len(cross)} with versions in ≥ 2 services, {len(deep)} with ≥ 3 versions); "
          f"each needs version_records [{{service, id|base_pointer, seeded, at (ISO, oldest first)}}] ≥ 2 — missing/unordered: {no_versions[:6] or 'none'}")

    chrono_bad, n_chrono = [], 0
    if not design:
        for tr in traps:
            vs = tr.get("version_records", []) or []
            if len(vs) < 2:
                continue
            n_chrono += 1
            stamps = []
            for v in vs:
                ref = v.get("id") or v.get("base_pointer")
                when, why = rt.time_of(ref)
                if when is None:
                    chrono_bad.append(f"{tr.get('id')}:{str(ref)[:40]} (timestamp unreadable: {why})")
                    break
                stamps.append((ref, when))
            else:
                for (r1, a), (r2, b) in zip(stamps, stamps[1:]):
                    if not a < b:
                        chrono_bad.append(f"{tr.get('id')}: {str(r1)[:30]} {a:%Y-%m-%dT%H:%M:%SZ} is not before "
                                          f"{str(r2)[:30]} {b:%Y-%m-%dT%H:%M:%SZ}")
                        break
    check("supersession_chronology", not chrono_bad,
          f"{n_chrono} trap(s) with version_records; the records' own timestamps (SQL created_at/ts/date/updated_at, or the "
          f"base record) must be strictly increasing in the listed order (oldest first); bad: {chrono_bad[:6] or 'none'}")

    dis = [t for t in traps if t.get("family") == "distractor"]
    dtypes = {t.get("distractor_type") for t in dis} & DISTRACTOR_TYPES
    check("distractors", len(dis) >= p["distractors"] and len(dtypes) >= p["distractor_types"],
          f"{len(dis)} distractors of {len(dtypes)} types; need ≥ {p['distractors']} / ≥ {p['distractor_types']}")

    shifts = [t for t in traps if t.get("discovery_order")]
    check("discovery_order_proofs", len(shifts) >= p["shifts"],
          f"{len(shifts)} traps carry a discovery-order proof; need ≥ {p['shifts']}")

    chains = manifest.get("chains", [])
    bad_root = [f"{c.get('id')}:{c.get('root_cause')!r}" for c in chains if str(c.get("root_cause") or "") not in MECHANISM_IDS]
    roots = {c.get("root_cause") for c in chains if str(c.get("root_cause") or "") in MECHANISM_IDS}
    thin = [c.get("id") for c in chains
            if len(c.get("hops", [])) < p["chain_hops"] or len({h.get("service") for h in c.get("hops", [])}) < 2
            or not c.get("ends_in")]
    check("independent_chains", len(chains) >= p["chains"] and len(roots) >= p["chains"] and not thin and not bad_root,
          f"{len(chains)} chains with {len(roots)} distinct mechanism ids (Hardness_Mastery.md enum; chains sharing a mechanism "
          f"count once); need ≥ {p['chains']}, each ≥ {p['chain_hops']} hops over ≥ 2 services ending in a graded fact; "
          f"thin: {thin or 'none'}; root_cause not a mechanism id: {bad_root[:5] or 'none'}")

    portfolio_check(manifest, traps, chains, check)
    artifact_fields_check(manifest, check)

    auths = manifest.get("authorities", [])
    bad_auth = [a.get("id") for a in auths
                if a.get("home_service") not in AUTHORITY_HOMES or not a.get("decoy_service")
                or not a.get("governs")
                or not a.get("findable_query") or not (a.get("seeded_ids") or a.get("base_pointers"))
                or not (a.get("decoy_seeded_ids") or a.get("decoy_base_pointers"))]
    governed = [g for a in auths for g in a.get("governs", [])]
    overlap = len(governed) != len(set(governed))
    bad_auth += [f"{a.get('id')}:{sid} not in SQL" for a in auths for sid in a.get("seeded_ids", []) if not in_sql(sid)]
    same_service = [a.get("id") for a in auths if a.get("decoy_service") == a.get("home_service")]
    need_same = 1 if p["authorities"] >= 2 else 0
    check("hidden_authorities", len(auths) >= p["authorities"] and not bad_auth and not overlap
          and len(same_service) >= need_same,
          f"{len(auths)} authorities (need ≥ {p['authorities']}), each homed in {sorted(AUTHORITY_HOMES)} with a decoy record elsewhere (decoy_seeded_ids / decoy_base_pointers), "
          f"a findable_query, records, and NON-overlapping 'governs'; bad: {bad_auth or 'none'}; overlap: {overlap}; "
          f"same-service decoys {len(same_service)} (need ≥ {need_same}: a targeted search must also meet a decoy)")
    older = set()
    for tr in traps:
        for v in (tr.get("version_records", []) or [])[:-1]:
            older |= {str(v.get(k)) for k in ("id", "base_pointer") if v.get(k)}
    bad_decoy = []
    for a in auths:
        drecs = [str(x) for x in list(a.get("decoy_seeded_ids", []) or []) + list(a.get("decoy_base_pointers", []) or [])]
        ds = a.get("decoy_scope") or {}
        scoped = (isinstance(ds, dict) and ds.get("dimension") in DECOY_DIMENSIONS and str(ds.get("decoy") or "").strip()
                  and str(ds.get("task") or "").strip() and _norm(ds.get("decoy")).lower() != _norm(ds.get("task")).lower())
        if not scoped and not (drecs and all(d in older for d in drecs)):
            bad_decoy.append(a.get("id"))
    check("decoy_scope", not bad_decoy,
          f"each authority's decoy must apply to a different scope (decoy_scope {{dimension: {'|'.join(sorted(DECOY_DIMENSIONS))}, "
          f"decoy, task}}) or be an older entry of a trap's version_records — an identical-scope contradiction fails "
          f"Cross-Service Coherence and Unique Ground Truth; bad: {bad_decoy or 'none'}")
    rare = [t.get("id") for t in traps if set(t.get("services", [])) & RARELY_OPENED]
    check("rarely_opened_evidence", len(rare) >= p["rare_traps"],
          f"{len(rare)} traps carry decisive evidence in rarely-opened services {sorted(RARELY_OPENED)}; need ≥ {p['rare_traps']}")

    referenced = ({t.get("requirement") for t in traps if t.get("requirement")}
                  | {g for a in auths for g in a.get("governs", [])}
                  | {c.get("ends_in") for c in chains if c.get("ends_in")})
    written = {r for w in manifest.get("writes", []) for r in w.get("requirements", [])}
    referenced |= written
    undeclared = sorted(r for r in referenced if r not in declared)
    uncovered = sorted(r for r in declared if r not in referenced)
    check("requirements", len(declared) >= p["trap_requirements"] and not undeclared,
          f"{len(declared)} requirements declared; referenced but undeclared: {undeclared[:8] or 'none'}; "
          f"declared with no trap/chain/authority/write mapping: {uncovered[:8] or 'none'}")

    writes = manifest.get("writes", [])
    check("writes", len(writes) >= p["writes"] and len({w.get("service") for w in writes}) >= p["write_services"]
          and all(w.get("depends_on") for w in writes),
          f"{len(writes)} writes over {len({w.get('service') for w in writes})} services; each must depend on findings")

    notes = []
    if total != floor:
        notes.append(f"call budget: planned total {total}, unconditional floor {floor} — the conditional rows count once "
                     "their tool behaviour is verified (then drop conditional_on)")
    if manifest.get("horizon") == "Normal Horizon" and profile == "extreme" and not profile_probs:
        notes.append("Normal Horizon at the extreme profile scores Borderline Horizon (non-fail, task score capped at 3) — "
                     f"requester confirmation: {str((manifest.get('profile_exception') or {}).get('requester_confirmation'))[:80]}")

    failed = [c for c in checks if not c["ok"]]
    return {"profile": profile + (" (design)" if design else ""), "verdict": "PASS" if not failed else "FAIL", "checks": checks,
            "notes": notes,
            "lint": {"errors": len(lint_result["errors"]), "warnings": len(lint_result["warnings"]), "stats": stats}}


# ---------------------------------------------------------------- record text / time (SQL rows, base via hg.py)

KEY_COLS = ("id", "identifier", "event_id", "ical_uid", "document_id", "spreadsheet_id", "presentation_id", "object_id",
            "contact_id", "sha", "calendar_id")
CONTAINER_COLS = ("thread_id", "issue_id", "pr_id", "page_id")
TIME_COLS = ("created_at", "ts", "date", "submitted_at", "updated_at", "created", "modified_time", "created_time",
             "start_ts", "dateLastActivity")
# the time a record came into being, per table ("@id" = Trello ids, whose first 8 hex digits are the creation time);
# a Trello card's dateLastActivity moves with later comments, so it never dates the card's own version
TABLE_TIME = {"slack.slack_messages": ("ts",), "gmail.gmail_messages": ("date", "internal_date"),
              "trello.trello_cards": ("@id",), "trello.trello_actions": ("date", "@id"), "trello.trello_checklists": ("@id",),
              "linear.linear_issues": ("created_at",), "linear.linear_comments": ("created_at",),
              "github.github_pull_requests": ("created_at",), "github.github_pr_comments": ("created_at",),
              "github.github_reviews": ("submitted_at",), "github.github_review_comments": ("created_at",),
              "confluence.confluence_pages": ("created_at",), "confluence.confluence_page_versions": ("created_at",),
              "confluence.confluence_comments": ("created_at",), "gcal.gcal_events": ("updated", "created"),
              "gdocs.docs_documents": ("modified_time", "created_time"), "gsheets.sheets_spreadsheets": ("modified_time", "created_time"),
              "gslides.slides_presentations": ("modified_time", "created_time"), "gdrive.drive_files": ("modified_time", "created_time")}
RX_SLACK_REF = re.compile(r"^([CDG][A-Z0-9]{8,11})(?:\s+ts\s+|[:/]|\s+)(\d{10}\.\d{6})$")
RX_LIN = re.compile(r"^(?:linear:\s*)?(?:data\.json\s+/issues\s+)?((?:ENG|ZOM|ART|DES|EPI)-\d{1,5})$")
RX_GET = re.compile(r"^([a-z]+):\s*(\S+\.json)\s*(?:#|\s)\s*(/\S*)$")


def _ts(v):
    s = str(v or "").strip()
    if not s or s in ("None", "NULL"):
        return None
    try:
        if re.fullmatch(r"\d{10}(\.\d+)?", s):
            return datetime.fromtimestamp(float(s), tz=timezone.utc)
        if re.fullmatch(r"\d{13}", s):
            return datetime.fromtimestamp(int(s) / 1000, tz=timezone.utc)
        d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
    except ValueError:
        try:
            from email.utils import parsedate_to_datetime
            return parsedate_to_datetime(s)
        except (TypeError, ValueError):
            return None


def _strings(x, out):
    if isinstance(x, str):
        out.append(x)
    elif isinstance(x, dict):
        for v in x.values():
            _strings(v, out)
    elif isinstance(x, list):
        for v in x:
            _strings(v, out)
    return out


class RecordText:
    """Text and timestamp of a record the manifest cites: a seeded SQL row (by key, Slack 'C/ts', Gmail thread) or a base
    record read through tools/hg.py (Slack C/ts, Linear keys, Gmail mailbox/<id>, '<service>:<file> <pointer>', or a
    unique id searched in its service). Read-only; results cached per run."""

    def __init__(self, sql_text: str, design: bool = False):
        from base_check import parse_sql
        from fact_check import _field_text
        self.design, self.rows, self._base, self._hg_error = design, [], {}, ""
        for s in parse_sql(sql_text or ""):
            if s["op"] != "insert":
                continue
            r = s["row"]
            keys = {str(r[c]) for c in KEY_COLS if r.get(c) not in (None, "")}
            if s["table"] == "slack.slack_messages" and r.get("channel_id") and r.get("ts"):
                keys.add(f"{r['channel_id']}/{r['ts']}")
            cont = {str(r[c]) for c in CONTAINER_COLS if r.get(c) not in (None, "")}
            text = "\n".join(_field_text(c, v) for c, v in r.items() if isinstance(v, str) and c not in KEY_COLS)
            when = None
            for c in TABLE_TIME.get(s["table"], TIME_COLS):
                if c == "@id" and re.fullmatch(r"[0-9a-f]{24}", str(r.get("id") or "")):
                    when = datetime.fromtimestamp(int(str(r["id"])[:8], 16), tz=timezone.utc)
                elif c != "@id" and r.get(c) not in (None, ""):
                    when = _ts(r[c])
                if when:
                    break
            self.rows.append({"keys": keys, "cont": cont, "text": text, "time": when, "table": s["table"]})

    @staticmethod
    def canon(ref: str) -> str:
        ref = str(ref or "").strip()
        m = RX_SLACK_REF.match(ref)
        return f"{m.group(1)}/{m.group(2)}" if m else ref

    def seeded(self, ref):
        ref = self.canon(ref)
        own = [r for r in self.rows if ref in r["keys"]]
        return own or [r for r in self.rows if ref in r["cont"]]

    # --- base records through tools/hg.py
    def _hg(self, *args):
        import subprocess
        here = Path(__file__).resolve().parent
        try:
            r = subprocess.run([sys.executable, str(here / "hg.py"), "search", *args], cwd=str(here.parent.parent),
                               capture_output=True, text=True, timeout=300)
        except (OSError, subprocess.TimeoutExpired) as exc:
            self._hg_error = f"{type(exc).__name__}: {exc}"
            return {}
        self._hg_error = "" if r.returncode == 0 else (r.stderr or r.stdout).strip()[-400:]
        try:
            return json.loads(r.stdout)
        except ValueError:
            self._hg_error = self._hg_error or (r.stderr or r.stdout).strip()[-400:] or "hg.py returned no JSON"
            return {}

    def _get(self, svc, f, ptr):
        r = self._hg("get", svc, "--file", f, "--pointer", ptr, "--max-chars", "4000000")
        try:
            return json.loads(r.get("text") or "")
        except ValueError:
            return r.get("text")

    def _find(self, svc, token, f=None):
        """The base record object holding `token` as an exact scalar (id/ts/identifier), via hg.py search + get."""
        args = ["search", svc, token, "--limit", "20"] + (["--file", f] if f else [])
        for m in (self._hg(*args).get("matches") or []):
            if str(m.get("text")) == token and m.get("parent_pointer") is not None:
                obj = self._get(svc, m.get("service_file") or f, m["parent_pointer"])
                if obj is not None:
                    return obj
        return None

    def base(self, ref):
        """(object | text | None, why)."""
        ref = self.canon(ref)
        if ref in self._base:
            return self._base[ref]
        out = (None, "no base reader for this pointer form (use a seeded id, Slack C/ts, a Linear key, mailbox/<id> or "
                     "'<service>:<file> <json pointer>')")
        m = RX_GET.match(ref)
        ms = re.match(r"^([CDG][A-Z0-9]{8,11})/(\d{10}\.\d{6})$", ref)
        ml = RX_LIN.match(ref)
        if m:
            obj = self._get(m.group(1), m.group(2), m.group(3))
            out = (obj, "hg.py get") if obj is not None else (None, f"hg.py get {ref} returned nothing")
        elif ms:
            month = datetime.fromtimestamp(float(ms.group(2)), tz=timezone.utc).strftime("%Y-%m")
            obj = self._find("slack", ms.group(2), f"messages/{ms.group(1)}/{month}.json")
            out = (obj, "hg.py slack") if obj is not None else (None, f"no base Slack message {ref}")
        elif ml:
            obj = self._find("linear", ml.group(1), "data.json")
            out = (obj, "hg.py linear") if obj is not None else (None, f"no base Linear issue {ml.group(1)}")
        elif "@" in ref.split("/", 1)[0] and "/" in ref:
            box, rest = ref.split("/", 1)
            from base_check import Base
            idx = Base().gmail()
            tid = ref if ref in idx else next((k for k, v in idx.items() if v[0] == box and ref in v[1]), None)
            if tid:
                files = self._hg("files", "gmail", tid.rsplit("/", 1)[-1]).get("matches") or []
                if files:
                    obj = self._get("gmail", files[0]["path"], "")
                    if isinstance(obj, dict) and ref != tid:
                        obj = next((x for x in obj.get("messages", []) if x.get("id") in (ref, rest)), None)
                    out = (obj, "hg.py gmail") if obj is not None else (None, f"message {ref} not in its thread file")
            else:
                out = (None, f"no base Gmail thread/message {ref}")
        else:
            svc = ("confluence" if ref.startswith("page_") else "trello" if re.fullmatch(r"[0-9a-f]{24}", ref)
                   else "gcal" if ref.startswith("evt_") else "github" if re.search(r"#\d+", ref) else None)
            if svc:
                obj = self._find(svc, ref)
                out = (obj, f"hg.py {svc}") if obj is not None else (None, f"no base {svc} record {ref}")
        self._base[ref] = out
        return out

    def contains(self, ref, quote) -> tuple:
        """(True | False | None, why): None = not checkable now (a seeded record in --design mode)."""
        q = _norm(quote)
        rows = self.seeded(ref)
        if rows:
            ok = q in _norm("\n".join(r["text"] for r in rows))
            return ok, ("seeded row" if ok else "seeded row text does not contain it")
        if self.design:
            return None, "design mode: seeded records are checked once the SQL exists"
        obj, why = self.base(ref)
        if obj is None:
            return False, f"record text unreadable — {why}"
        text = "\n".join(_strings(obj, [])) if not isinstance(obj, str) else obj
        ok = q in _norm(text)
        return ok, (why if ok else f"base record text ({why}) does not contain it")

    def time_of(self, ref) -> tuple:
        rows = self.seeded(ref)
        if rows and rows[0]["time"]:
            return rows[0]["time"], "seeded row"
        ms = re.match(r"^([CDG][A-Z0-9]{8,11})/(\d{10}\.\d{6})$", self.canon(ref))
        if ms:
            return _ts(ms.group(2)), "Slack ts"
        if rows:
            return None, "seeded row has no created_at/ts/date/updated_at"
        obj, why = self.base(ref)
        if isinstance(obj, dict) and isinstance(obj.get("messages"), list):
            return None, "a Gmail thread has no single time — cite the message (mailbox/<Message-ID>)"
        if isinstance(obj, dict):
            for c in TIME_COLS + ("internal_date",):
                if obj.get(c) not in (None, ""):
                    w = _ts(obj[c])
                    if w:
                        return w, why
            return None, f"base record has no timestamp field ({why})"
        return None, why


# ---------------------------------------------------------------- integrity layer (full mode)

def load_bearing_ids(manifest: dict, sql_text: str) -> dict:
    """Every seeded id the design leans on -> the manifest places that cite it. Seeded = an exact token of the
    SQL (outside comments). Sources: ask_fragments, authorities, traps (any *seeded_ids list, seeded
    version_records), chains (a hop record, or tokens inside it, that equal an SQL row key; a short
    '<repo>#N#c_K' is read as harmonygames-Games/<repo>#N#c_K) and cohort evidence_surfaces[].seeded_ids."""
    from base_check import parse_sql
    code = _code_only(sql_text)
    out: dict = {}
    keys = set()  # every SQL row key: chain hops are prose, so only tokens that ARE a row key count as records
    for s in parse_sql(sql_text):
        src = s.get("row") if s["op"] == "insert" else s.get("where")
        for c in ("id", "identifier", "event_id", "ical_uid", "document_id", "spreadsheet_id", "presentation_id",
                  "object_id", "contact_id", "sha", "thread_id", "calendar_id"):
            if (src or {}).get(c):
                keys.add(str(src[c]))
        if s["table"] == "slack.slack_messages" and s["op"] == "insert":
            keys.add(f"{s['row'].get('channel_id')}/{s['row'].get('ts')}")

    def add(i, where):
        i = str(i or "").strip()
        if i and _has_token(code, i):
            out.setdefault(i, []).append(where)

    def add_hop(tok, where):
        tok = tok.strip().strip(".:'\"")
        for cand in (tok, f"harmonygames-Games/{tok}"):
            if cand in keys:
                add(cand, where)
                return
    for section in ("ask_fragments", "authorities", "traps"):
        for item in manifest.get(section, []) or []:
            for k, v in item.items():
                if k.endswith("seeded_ids") and isinstance(v, list):
                    for i in v:
                        add(i, f"{section}:{item.get('id')}:{k}")
            for v in item.get("version_records", []) or []:
                if v.get("seeded"):
                    add(v.get("id"), f"{section}:{item.get('id')}:version_records")
    for c in manifest.get("chains", []) or []:
        for h in c.get("hops", []) or []:
            rec = str(h.get("record") or "").strip()
            if rec in keys:
                add(rec, f"chains:{c.get('id')}")
            else:
                for tok in re.findall(r"[^\s,;()]+", rec):
                    add_hop(tok, f"chains:{c.get('id')}")
    for sfc in (manifest.get("cohort", {}) or {}).get("evidence_surfaces", []) or []:
        for i in sfc.get("seeded_ids", []) or []:
            add(i, f"cohort:{sfc.get('tool')}")
    return out


def persona_reach(manifest: dict, sql_text: str, lb: dict | None = None) -> dict:
    """persona_view check-sql with every load-bearing seeded id: each must be provably visible (YES)."""
    import persona_view as pv
    from base_check import parse_sql
    lb = lb if lb is not None else load_bearing_ids(manifest, sql_text)
    persona = manifest.get("persona")
    if not persona:
        return {"check": "persona_reach", "ok": False, "detail": "manifest has no persona — load-bearing visibility cannot be judged"}
    try:
        p = pv.resolve_persona(str(persona))
    except SystemExit:
        return {"check": "persona_reach", "ok": False, "detail": f"unknown persona {persona!r}"}
    # unscoped services (Linear, GitHub, Trello, Confluence, Contacts, Snowflake) are visible to every persona
    unscoped = set()
    for s in parse_sql(sql_text):
        if s["table"].split(".", 1)[0] in pv.UNSCOPED:
            src = s.get("row") or s.get("where") or {}
            unscoped |= {str(v) for k, v in src.items() if v and (k in ("id", "identifier", "contact_id", "number", "sha")
                                                                   or k.endswith("_id") and k not in ("team_id", "assignee_id", "creator_id", "author_id", "state_id", "project_id"))}
    probes = {str(d.get("record")): d for d in manifest.get("denied_probes", []) or [] if isinstance(d, dict)}
    alts = {str(a) for d in probes.values() for a in d.get("alternate_evidence_ids", []) or []}
    unscoped_rx = re.compile(r"^(?:(?:ENG|ZOM|ART|DES|EPI)-\d+|[\w.-]+/[\w.-]+#\d+.*|[0-9a-f]{24}|page_\w+|snowflake\..*|wh_\w+)$")
    scoped = {i for i in lb if i not in unscoped} | {a for a in alts if a not in unscoped and not unscoped_rx.match(a)}
    r = pv.check_sql(pv.Universe(), p, sql_text, scoped)
    verdict = {}
    rank = {"YES": 0, "INFO": 0, "UNVERIFIED": 1, "NO": 2}
    for row in r["rows"]:
        for k in row.get("keys", []):
            if k in scoped and rank.get(row["verdict"], 1) >= rank.get(verdict.get(k, ("YES", ""))[0], 0):
                verdict[k] = (row["verdict"], f"line {row['line']} {row['table']}: {row['reason']}")
    for x in r["load_bearing_base_ids"]:
        verdict.setdefault(x["id"], (x["verdict"], x["reason"]))
    def vis(x):
        return "YES" if (x in unscoped or unscoped_rx.match(x)) else verdict.get(x, ("UNVERIFIED", "not judged"))[0]
    accepted, bad = [], []
    for k, v in sorted(verdict.items()):
        if k in alts and k not in lb:
            continue                       # an alternate only matters through its probe
        if v[0] == "NO" and k in probes:
            d = probes[k]
            places = lb.get(k, [])
            lb_places = [w for w in places if not (w.startswith("traps:") or w.endswith(":decoy_seeded_ids"))]
            alt = [str(a) for a in d.get("alternate_evidence_ids", []) or []]
            not_yes = [f"{a}={vis(a)}" for a in alt if vis(a) != "YES"]
            if str(d.get("reason") or "").strip() and alt and not not_yes and not lb_places:
                accepted.append(k)
                continue
            why = ("no reason" if not str(d.get("reason") or "").strip() else "no alternate_evidence_ids" if not alt
                   else f"alternates not YES: {not_yes[:3]}" if not_yes else f"still load-bearing via {lb_places[:2]}")
            bad.append((k, ("NO", f"denied probe rejected ({why}) — {v[1]}")))
        elif v[0] in ("NO", "UNVERIFIED"):
            bad.append((k, v))
    if not p.get("usable_in_tasks", True):
        bad.insert(0, ("persona", ("NO", f"{p['persona_key']} is not usable in tasks")))
    detail = (f"{len(lb)} load-bearing seeded ids for {p['persona_key']} ({len(lb) - len(scoped)} in unscoped services = visible, "
              f"{len(scoped)} judged by persona_view check-sql); not provably visible: "
              + ("; ".join(f"{k} [{v[0]}] cited by {','.join(lb.get(k, ['?'])[:2])} — {v[1][:110]}" for k, v in bad[:8]) if bad else "none")
              + (f" … +{len(bad) - 8}" if len(bad) > 8 else "")
              + (f"; denied probes accepted (cited only by traps/decoys, alternates YES): {accepted[:4]}" if accepted else ""))
    return {"check": "persona_reach", "ok": not bad, "detail": detail, "failures": [k for k, _ in bad]}


RESOLUTIONS = ("excluded", "repaired", "dated_claim")


def hazard_scope(manifest: dict, sql_text: str, base_result: dict, base=None) -> dict:
    """State/lifecycle and referential hazards among task-touched records (SQL-touched + manifest-cited) need a verified
    resolution in hazard_acknowledgements (red team A, R1 #4): `excluded` = the record is neither modified by the SQL
    nor cited by the design; `repaired` = base_check re-evaluates the hazard predicate on the post-SQL state and it no
    longer holds (unsupported hazard types FAIL as unverifiable); `dated_claim` = the disagreement lives in seeded text
    claims only, never in a record the SQL modifies. An acknowledgement alone never changes the verdict."""
    from base_check import HAZARD_FAIL_CATEGORIES, hazard_index, id_tokens, parse_sql, repair_status
    idx, meta, _ = hazard_index()
    entries = {h["hazard_id"]: h for h in base_result.get("hazards_touched", [])}
    touched = {hid: set(h["tokens"]) for hid, h in entries.items()}
    cited = id_tokens(json.dumps({k: manifest.get(k) for k in ("anchors", "ask_fragments", "authorities", "traps", "chains", "cohort")}))
    cited_by = {}
    for tok in cited:
        for hid in idx.get(tok, ()):
            touched.setdefault(hid, set()).add(tok)
            cited_by.setdefault(hid, set()).add(tok)
    declared = _declared(manifest)
    acks, bad_acks = {}, []
    for a in manifest.get("hazard_acknowledgements", []) or []:
        hid = str((a or {}).get("hazard_id") or "")
        res = str((a or {}).get("resolution") or "").strip().lower()
        if hid not in meta:
            bad_acks.append(f"{hid or '?'} (unknown hazard id)")
        elif not str(a.get("why_safe") or "").strip():
            bad_acks.append(f"{hid} (no why_safe)")
        elif res not in RESOLUTIONS:
            bad_acks.append(f"{hid} (resolution {res or 'missing'}: must be one of {', '.join(RESOLUTIONS)})")
        elif a.get("requirement") and a["requirement"] not in declared:
            bad_acks.append(f"{hid} (requirement {a['requirement']} not declared)")
        else:
            acks[hid] = res
    fail = []
    for h in sorted(touched):
        if meta[h]["category"] not in HAZARD_FAIL_CATEGORIES:
            continue
        res, modified = acks.get(h), bool((entries.get(h) or {}).get("modified"))
        if res is None:
            fail.append((h, "no verified resolution"))
        elif res == "excluded" and (modified or h in cited_by):
            fail.append((h, "excluded, but the record is " + ("modified by the SQL" if modified else
                                                              f"cited by the design ({sorted(cited_by[h])[:2]})")))
        elif res == "dated_claim" and modified:
            fail.append((h, "dated_claim applies to text claims only; the SQL modifies the record"))
        elif res == "repaired":
            status = (entries.get(h) or {}).get("repair")
            if status is None:
                status, why = repair_status(h, touched[h], parse_sql(sql_text), base or _base())
            if status != "repaired":
                fail.append((h, f"repaired not established on the post-SQL state ({status})"))
    other = sorted(h for h in touched if h not in {f for f, _ in fail})
    detail = (f"{len(touched)} pre-existing hazard(s) among task-touched records; state/lifecycle or referential without a "
              f"verified resolution: "
              + ("; ".join(f"{h} ({meta[h]['title'][:50]}) via {sorted(touched[h])[:3]}: {why}" for h, why in fail[:6]) if fail else "none")
              + (f"; resolved/other: {other[:8]}" if other else "")
              + (f"; invalid hazard_acknowledgements: {bad_acks}" if bad_acks else ""))
    return {"check": "hazard_scope", "ok": not fail and not bad_acks, "detail": detail, "failures": [h for h, _ in fail]}


def _base():
    import base_check
    return base_check.Base()


def integrity_checks(manifest: dict, sql_text: str, base=None, fact_result: dict | None = None,
                     base_result: dict | None = None) -> list:
    """persona_reach, fact_consistency and hazard_scope (full mode only)."""
    import base_check
    import fact_check
    base = base or base_check.Base()
    br = base_result or base_check.check(sql_text, base, manifest)
    fr = fact_result or fact_check.check(sql_text, manifest, base, no_leak=True)
    out = [persona_reach(manifest, sql_text)]
    errs = fr["errors"]
    out.append({"check": "fact_consistency", "ok": not errs,
                "detail": f"fact_check: {len(errs)} error(s) ({len(manifest.get('facts', []) or [])} declared facts), "
                          f"{len(fr['warnings'])} drift warning(s); first: "
                          + ("; ".join(f"line {e['line']} {e['row']}: {e['msg'][:90]}" for e in errs[:3]) if errs else "none")
                          + " — run tools/fact_check.py --manifest --no-leak"})
    out.append(hazard_scope(manifest, sql_text, br, base))
    return out


def to_text(r: dict) -> str:
    lines = [f"HARDNESS GATE ({r['profile']}): {r['verdict']}"]
    for c in r["checks"]:
        lines.append(f"  [{'ok' if c['ok'] else 'FAIL'}] {c['check']}: {c['detail']}")
    for n in r.get("notes", []):
        lines.append(f"  [note] {n}")
    return "\n".join(lines)


def _self_test() -> None:
    sql = "-- Are you planning to inject? Yes\n" + "\n".join(
        f"INSERT INTO slack.slack_messages (id, ts, channel_id, type, text, reply_count, reply_users_count, is_activity_message, "
        f"reactions_json, files_json, attachments_json, created_at, metadata_json) VALUES ('seed{i}', '1770634800.0001', 'C1', "
        f"'message', 'x', 0, 0, false, '[]', '[]', '[]', '2026-02-09T11:00:00Z', '{{}}');" for i in range(3))
    thin = {"services": {"slack": {"weight_reason": "x"}}, "anchors": [{"id": "A1", "prompt_reference": "the list"}],
            "ask_fragments": [{"id": "K1", "service": "slack", "container": "C1", "incorporated_via": ["A1"], "seeded_ids": ["seed1"]}],
            "traps": [{"id": "T1", "family": "superseding", "seeded_ids": ["seedX"], "resolver": "r", "expected_wrong_reading": "w"}]}
    r = evaluate(thin, sql)
    assert r["verdict"] == "FAIL"
    names = {c["check"] for c in r["checks"] if not c["ok"]}
    for n in ("services_injected", "rows", "seeded_ids_exist_in_sql", "call_budget", "traps", "persona_reach", "effective_profile"):
        assert n in names, (n, names)
    n = _self_test_redteam_a()
    _self_test_integrity()
    k = _self_test_portfolio()
    _self_test_v2_ids()
    print(f"self-test: ok ({n} red-team-A planted defects each fail their own check; integrity layer incl. denied probes, "
          f"hazard resolutions and no-leak; {k} mechanism_portfolio / artifact_fields defects fail, A22/A23 accepted, "
          f"A24/A25 and their v2 trap families accepted)")


def _self_test_portfolio() -> int:
    """Fold-hardening plan §8 fields on the red-team-A fixture (SQL overlay only, no base data)."""
    man, sql, _ = _fixture_a()
    rt = RecordText(sql)

    def run(m):
        return {c["check"]: c for c in evaluate(m, sql, None, records=rt, integrity=False)["checks"]}
    by = run(man)
    assert by["mechanism_portfolio"]["ok"] and by["artifact_fields"]["ok"], (by["mechanism_portfolio"], by["artifact_fields"])
    good_port = [{"id": "late_rule", "mechanism": "A15", "nodes": ["T1"], "requirement": "R1", "natural_reading": "x",
                  "prior_family": "A15", "prior_family_reason": "same mechanism id"},
                 {"id": "brief_loss", "mechanism": "A23", "nodes": ["C1"], "requirement": "R1", "natural_reading": "y",
                  "family": "brief-transmission loss (A23)", "prior_family_reason": "the library hypothesis family"}]
    fields = {"gradable_surface": {"path": "01_Gradable_Surface.json", "digest": "a" * 64},
              "solver": {"path": "solver/solver.py", "digest": "b" * 64},
              "preflight": {"report": "01c_Preflight_Report.json", "digest": "c" * 64}}
    ok = run(dict(man, mechanism_portfolio=good_port, **fields))
    assert ok["mechanism_portfolio"]["ok"] and "A23" in ok["mechanism_portfolio"]["detail"], ok["mechanism_portfolio"]
    assert ok["artifact_fields"]["ok"], ok["artifact_fields"]
    hyp = json.loads(json.dumps(man))
    for c, rc in zip(hyp["chains"], ("A22", "A23", "A1")):
        c["root_cause"] = rc
    assert run(hyp)["independent_chains"]["ok"], run(hyp)["independent_chains"]       # hypothesis ids are valid roots

    def bad_port(f):
        p = json.loads(json.dumps(good_port))
        f(p)
        return p
    cases = [("mechanism outside the enum", dict(man, mechanism_portfolio=bad_port(lambda p: p[0].update(mechanism="A99"))),
              "mechanism_portfolio"),
             ("no prior family", dict(man, mechanism_portfolio=bad_port(lambda p: p[0].pop("prior_family"))),
              "mechanism_portfolio"),
             ("no prior-family reason", dict(man, mechanism_portfolio=bad_port(lambda p: p[1].pop("prior_family_reason"))),
              "mechanism_portfolio"),
             ("node that is no trap or chain", dict(man, mechanism_portfolio=bad_port(lambda p: p[0].update(nodes=["T9"]))),
              "mechanism_portfolio"),
             ("duplicate rule id", dict(man, mechanism_portfolio=bad_port(lambda p: p[1].update(id="late_rule"))),
              "mechanism_portfolio"),
             ("no natural-reading fallback", dict(man, mechanism_portfolio=bad_port(lambda p: p[0].pop("natural_reading"))),
              "mechanism_portfolio"),
             ("empty portfolio", dict(man, mechanism_portfolio=[]), "mechanism_portfolio"),
             ("solver digest not sha256", dict(man, **dict(fields, solver={"path": "solver/solver.py", "digest": "abc"})),
              "artifact_fields"),
             ("absolute preflight path", dict(man, **dict(fields, preflight={"report": "/tmp/x.json", "digest": "c" * 64})),
              "artifact_fields")]
    for name, m, want in cases:
        got = run(m)
        assert not got[want]["ok"], (name, got[want])
        others = [c for c in ("mechanism_portfolio", "artifact_fields") if c != want and not got[c]["ok"]]
        assert not others, (name, others)
    return len(cases)


def _self_test_v2_ids() -> None:
    """Hardness v2 (Opus 5.5): A24 (done across services) and A25 (completion elsewhere) are valid mechanism ids and
    roots, and their trap families are known (references/Hardness_Mastery.md §13)."""
    man, sql, _ = _fixture_a()
    rt = RecordText(sql)

    def run(m):
        return {c["check"]: c for c in evaluate(m, sql, None, records=rt, integrity=False)["checks"]}
    port = [{"id": "done_gap", "mechanism": "A24", "nodes": ["T1"], "requirement": "R1", "natural_reading": "x",
             "prior_family": "A24", "prior_family_reason": "same mechanism id"},
            {"id": "already_done", "mechanism": "A25", "nodes": ["C1"], "requirement": "R1", "natural_reading": "y",
             "prior_family": "A25", "prior_family_reason": "same mechanism id"}]
    by = run(dict(man, mechanism_portfolio=port))
    assert by["mechanism_portfolio"]["ok"], by["mechanism_portfolio"]
    roots = json.loads(json.dumps(man))
    for c, rc in zip(roots["chains"], ("A24", "A25", "A1")):
        c["root_cause"] = rc
    assert run(roots)["independent_chains"]["ok"], run(roots)["independent_chains"]
    fam = json.loads(json.dumps(man))
    fam["traps"][0]["family"] = "done_gap"
    fam["traps"].append(dict(fam["traps"][0], id="T2", family="completion_elsewhere"))
    assert "unknown family: none" in run(fam)["traps"]["detail"], run(fam)["traps"]


def _fixture_a():
    """A small real-anchored design whose red-team-A checks all pass (the volume thresholds are not exercised)."""
    import hashlib
    ch, ol, br = "C09R0KXFX71", "oliver.brooks@harmonygames.co", "brian.foster@harmonygames.co"
    ts1, ts2 = "1768231200.000100", "1768231300.000100"
    sid1, sid2 = (hashlib.sha256(f"{ch}|{x}".encode()).hexdigest()[:32] for x in (ts1, ts2))
    gm = f"{ol}/<k2@harmonygames.co>"
    sql = f"""-- Are you planning to inject? Yes
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at) VALUES ('{sid1}', '{ts1}', '{ch}', 'message', 'EMPLOYEE_0003_SLACK_ID', 'vendor handoff: follow the vendor budget rules in my mail thread for each vendor', '2026-01-12T15:20:00Z');
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at) VALUES ('{sid2}', '{ts2}', '{ch}', 'message', 'EMPLOYEE_0003_SLACK_ID', 'rate card for the Lot A vendors: tier 2 across the board', '2026-01-12T15:21:40Z');
INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id) VALUES ('{ol}/1890000000000000001', '{ol}', 'x', NULL);
INSERT INTO gmail.gmail_messages (id, thread_id, user_email, label_ids_json, subject, from_email, to_json, body_text, date) VALUES ('{gm}', '{ol}/1890000000000000001', '{ol}', '["INBOX"]', 'budget rules', '{br}', '["{ol}"]', 'budget rules: each vendor''s budget tier comes from the Lot B rate card on the board', '2026-01-12T16:00:00Z');
"""
    hops = [{"service": "slack", "record": f"{ch}/{ts1}", "finding": "a"}, {"service": "gmail", "record": gm, "finding": "b"},
            {"service": "linear", "record": "ENG-2280", "finding": "c"}]
    man = {"persona": "oliver_brooks", "horizon": "Long Horizon", "effective_profile": "extreme",
           "requirements": {"R1": "budget tier per vendor", "R2": "handoff list destination"},
           "anchors": [{"id": "A1", "prompt_reference": "the vendor handoff", "service": "slack", "locator": f"{ch} ts {ts1}",
                        "requirement_ids": ["R2"]}],
           "ask_fragments": [{"id": "K1", "service": "gmail", "container": f"{ol}/1890000000000000001", "kind": "requirement",
                              "incorporated_via": ["A1"], "seeded_ids": [gm], "delegated_by_record": f"{ch} ts {ts1}",
                              "delegation_quote": "follow the vendor budget rules in my mail thread", "requirement_ids": ["R1"],
                              "names_authorities": [{"id": "H1", "quote": "the Lot B rate card"}]}],
           "authorities": [{"id": "H1", "name": "the Lot B rate card", "home_service": "gmail", "decoy_service": "slack",
                            "governs": ["R1"], "findable_query": "rate card", "seeded_ids": [gm], "decoy_seeded_ids": [sid2],
                            "decoy_scope": {"dimension": "lot", "decoy": "Lot A", "task": "Lot B"}}],
           "cohort": {"definition_source": "H1", "key": "vendor", "size": 40, "evidence_surfaces": [
               {"service": "linear", "tool": "linear_list_comments", "per_record_calls": 1, "records": 40, "why_no_bulk": "x",
                "short_circuit": "x", "requirement": "R1", "decides": "budget tier"}]},
           "chains": [{"id": f"C{i}", "root_cause": rc, "hops": hops, "ends_in": "R1"} for i, rc in enumerate(("A1", "A12", "A14"), 1)],
           "traps": [{"id": "T1", "family": "superseding", "services": ["slack", "gmail"], "seeded_ids": [sid1], "requirement": "R1",
                      "resolver": "r", "expected_wrong_reading": "w",
                      "version_records": [{"service": "slack", "id": f"{ch}/{ts1}", "seeded": True, "at": "2026-01-12T15:20:00Z"},
                                          {"service": "gmail", "id": gm, "seeded": True, "at": "2026-01-12T16:00:00Z"}]}],
           "call_budget": [{"phase": "per-record", "service": "linear", "calls": 600, "reason": "x"}]}
    return man, sql, sid2


UNAVAILABLE = ("Install Universe_", "SOURCE BLOCKED", "Cannot read assignment", "No task date is saved",
               "UniverseNotSelected")


def _universe_missing(text: str = "") -> str | None:
    """The reason the selected universe's data is not installed; only then may a live self-check skip."""
    if any(marker in str(text) for marker in UNAVAILABLE):
        return str(text)[-200:]
    context = globals().get("TASK_CONTEXT")
    if context is None:
        try:
            import task_context as tc
            context = tc.load_context(tc.DEFAULT_TASK)
        except Exception:  # noqa: BLE001 - no assignment at all is not a data-install skip
            return None
    source = (context or {}).get("source") or {}
    if context and source.get("status") not in (None, "ready"):
        return source.get("reason") or f"source status {source.get('status')!r}"
    return None


def _self_test_redteam_a() -> int:
    """Red team A (2026-10-05): every mechanical item planted once; each must fail its own check and only it."""
    man, sql, decoy = _fixture_a()
    targets = ("effective_profile", "incorporation_chains", "requirement_coverage", "authority_incorporation",
               "surface_requirements", "call_budget", "decoy_scope", "supersession_chronology", "independent_chains")
    rt = RecordText(sql)

    def run(m, prof=None):
        return {c["check"]: c for c in evaluate(m, sql, prof, records=rt, integrity=False)["checks"]}
    by = run(man)
    clean = [n for n in targets if not by[n]["ok"]]
    assert not clean, [(n, by[n]["detail"]) for n in clean]

    def mut(f):
        m = json.loads(json.dumps(man))
        f(m)
        return m
    k1 = lambda m: m["ask_fragments"][0]  # noqa: E731
    cases = [
        ("item 7 no effective_profile", mut(lambda m: m.pop("effective_profile")), None, "effective_profile"),
        ("item 7 --profile disagrees with the manifest", man, "normal", "effective_profile"),
        ("item 7 Normal Horizon at extreme without requester confirmation", mut(lambda m: m.update(horizon="Normal Horizon")), None, "effective_profile"),
        ("item 7 Long Horizon at normal", mut(lambda m: (m.update(effective_profile="normal"), m["call_budget"][0].update(calls=80))), None, "effective_profile"),
        ("item 3 no delegation_quote", mut(lambda m: k1(m).pop("delegation_quote")), None, "incorporation_chains"),
        ("item 3 delegation_quote not in the delegating record", mut(lambda m: k1(m).update(delegation_quote="see the rules attached")), None, "incorporation_chains"),
        ("item 3 orphan requirement", mut(lambda m: m["requirements"].update(R3="exclusions")), None, "requirement_coverage"),
        ("item 3 undeclared requirement_ids", mut(lambda m: k1(m).update(requirement_ids=["R1", "R9"])), None, "incorporation_chains"),
        ("item 3 orphan authority", mut(lambda m: (k1(m).pop("names_authorities"), m["authorities"][0].update(seeded_ids=[decoy]))), None, "authority_incorporation"),
        ("item 3 authority naming quote not in the fragment's record", mut(lambda m: k1(m).update(names_authorities=[{"id": "H1", "quote": "the release control"}])), None, "authority_incorporation"),
        ("item 4 conditional rows lift the floor", mut(lambda m: m.update(call_budget=[
            {"phase": "per-record", "service": "linear", "calls": 400, "reason": "x"},
            {"phase": "per-record", "service": "slack", "calls": 200, "reason": "x", "conditional_on": "replies unswept"}])), None, "call_budget"),
        ("item 5 surface requirement undeclared", mut(lambda m: m["cohort"]["evidence_surfaces"][0].update(requirement="R9")), None, "surface_requirements"),
        ("item 5 surface requirement not incorporated by a fragment", mut(lambda m: m["cohort"]["evidence_surfaces"][0].update(requirement="R2", decides="destination")), None, "surface_requirements"),
        ("item 5 manufactured output column", mut(lambda m: m["cohort"]["evidence_surfaces"][0].update(decides="comment author")), None, "surface_requirements"),
        ("item 10 decoy with no scope and no supersession", mut(lambda m: m["authorities"][0].pop("decoy_scope")), None, "decoy_scope"),
        ("item 10 decoy scope identical to the task", mut(lambda m: m["authorities"][0]["decoy_scope"].update(decoy="lot b")), None, "decoy_scope"),
        ("item 11 version_records out of chronological order", mut(lambda m: m["traps"][0]["version_records"].reverse()), None, "supersession_chronology"),
        ("item 12 root_cause outside the mechanism enum", mut(lambda m: m["chains"][0].update(root_cause="authoritative-but-wrong summary")), None, "independent_chains"),
        ("item 12 three chains, one mechanism", mut(lambda m: [c.update(root_cause="A1") for c in m["chains"]]), None, "independent_chains"),
    ]
    # a fragment whose delegation is not in the text incorporates nothing, so its requirement and the surface that serves it
    # are orphaned too (the downstream cascade is the point); every other planted defect fails exactly its own check
    cascade = {"incorporation_chains": {"requirement_coverage", "surface_requirements"}}
    for name, m, prof, want in cases:
        got = run(m, prof)
        failing = [n for n in targets if not got[n]["ok"]]
        allowed = {want} | (cascade.get(want, set()) if "delegation_quote" in name else set())
        assert want in failing and set(failing) <= allowed, (name, failing, got[want]["detail"])
    # controls: an authority delegated to (its record is an incorporated fragment's record) needs no naming quote; a valid
    # exception, and a decoy that is an older supersession entry, pass their checks
    assert run(mut(lambda m: k1(m).pop("names_authorities")))["authority_incorporation"]["ok"]
    ok = mut(lambda m: m.update(horizon="Normal Horizon", profile_exception={"reason": "volume is the point",
                                                                           "requester_confirmation": "requester ok 2026-10-05"}))
    assert run(ok)["effective_profile"]["ok"]
    ok = mut(lambda m: (m["authorities"][0].pop("decoy_scope"), m["traps"][0]["version_records"].insert(
        0, {"service": "slack", "id": decoy, "seeded": True, "at": "2026-01-12T15:00:00Z"})))
    got = run(ok)
    assert got["decoy_scope"]["ok"] and not got["supersession_chronology"]["ok"]  # decoy 15:21:40 is after the 15:20 version
    ok["traps"][0]["version_records"] = [ok["traps"][0]["version_records"][1], ok["traps"][0]["version_records"][0],
                                         ok["traps"][0]["version_records"][2]]
    got = run(ok)
    assert got["decoy_scope"]["ok"] and got["supersession_chronology"]["ok"], got["supersession_chronology"]["detail"]
    # design mode: a seeded delegating record cannot be read yet (not failed), a base one is read through hg.py
    dr = RecordText("", design=True)
    assert dr.contains("C09R0KXFX71/1768231200.000100", "anything")[0] is None
    rt = RecordText("")
    base_ok = rt.contains("D04UGG61DUM/1770751702.596069", "stuck at the loading screen at 8%")
    missing = _universe_missing(rt._hg_error)
    if base_ok[0] is not True and missing:
        print(f"self-test SKIP - base Slack record text: selected universe data not installed ({missing})")
    else:
        base_no = rt.contains("D04UGG61DUM/1770751702.596069", "the hub delegates the list")
        assert base_ok[0] is True and base_no[0] is False, (base_ok, base_no)
    return len(cases)


def _self_test_integrity() -> None:
    """persona_reach / fact_consistency / hazard_scope on a tiny real-anchored fixture."""
    import hashlib
    ch, ol, br = "C09R0KXFX71", "oliver.brooks@harmonygames.co", "brian.foster@harmonygames.co"
    ts = "1768231200.000100"
    sid = hashlib.sha256(f"{ch}|{ts}".encode()).hexdigest()[:32]

    def sql_for(box):
        return f"""-- Are you planning to inject? Yes
INSERT INTO slack.slack_messages (id, ts, channel_id, type, user_id, text, created_at) VALUES ('{sid}', '{ts}', '{ch}', 'message', 'EMPLOYEE_0003_SLACK_ID', 'vendor budget is $12,500', '2026-01-12T15:20:00Z');
INSERT INTO gmail.gmail_threads (id, user_email, snippet, history_id) VALUES ('{box}/1890000000000000001', '{box}', 'x', NULL);
INSERT INTO gmail.gmail_messages (id, thread_id, user_email, label_ids_json, subject, from_email, to_json, body_text, date) VALUES ('{box}/<k2@harmonygames.co>', '{box}/1890000000000000001', '{box}', '["INBOX"]', 'budget', '{br}', '["{ol}"]', 'budget $12,500', '2026-01-12T16:00:00Z');
"""
    man = {"persona": "oliver_brooks", "facts": [{"key": "vendor budget", "value": "$12,500", "kind": "amount", "aliases": ["budget"]}],
           "ask_fragments": [{"id": "K1", "seeded_ids": [sid]}, {"id": "K2", "seeded_ids": [f"{ol}/<k2@harmonygames.co>"]}]}
    by = {c["check"]: c for c in integrity_checks(man, sql_for(ol))}
    assert by["persona_reach"]["ok"] and by["fact_consistency"]["ok"] and by["hazard_scope"]["ok"], by
    man_br = dict(man, ask_fragments=[{"id": "K1", "seeded_ids": [sid]}, {"id": "K2", "seeded_ids": [f"{br}/<k2@harmonygames.co>"]}])
    by = {c["check"]: c for c in integrity_checks(man_br, sql_for(br))}
    assert not by["persona_reach"]["ok"] and f"{br}/<k2@harmonygames.co>" in by["persona_reach"]["failures"], by["persona_reach"]
    # item 1: a denied probe is never load-bearing; it needs YES alternates and may be cited only by traps / decoys
    k2 = f"{br}/<k2@harmonygames.co>"
    probe = dict(man, ask_fragments=[{"id": "K1", "seeded_ids": [sid]}], traps=[{"id": "T9", "family": "acl_alternate", "seeded_ids": [k2]}],
                 denied_probes=[{"record": k2, "reason": "designed denial: Brian's mailbox", "alternate_evidence_ids": [sid]}])
    assert {c["check"]: c for c in integrity_checks(probe, sql_for(br))}["persona_reach"]["ok"]
    no_alt = dict(probe, denied_probes=[{"record": k2, "reason": "designed denial"}])
    assert not {c["check"]: c for c in integrity_checks(no_alt, sql_for(br))}["persona_reach"]["ok"]
    lb_probe = dict(probe, ask_fragments=[{"id": "K1", "seeded_ids": [sid]}, {"id": "K2", "seeded_ids": [k2]}])
    r = {c["check"]: c for c in integrity_checks(lb_probe, sql_for(br))}["persona_reach"]
    assert not r["ok"] and "still load-bearing" in r["detail"], r
    by = {c["check"]: c for c in integrity_checks(man, sql_for(ol).replace("budget $12,500", "budget $15,000"))}
    assert not by["fact_consistency"]["ok"], by["fact_consistency"]
    # item 8: no-leak is always on in the gate — a per-record fact stated outside its home row fails
    leak = dict(man, facts=[dict(man["facts"][0], home_ids=[f"{ol}/<k2@harmonygames.co>"])])
    r = {c["check"]: c for c in integrity_checks(leak, sql_for(ol))}["fact_consistency"]
    assert not r["ok"] and "home_ids" in r["detail"], r
    # item 2: an acknowledgement alone never clears a hazard the SQL modifies; only a verified repair does
    upd = sql_for(ol) + "UPDATE linear.linear_issues SET updated_at = '2026-01-13T09:00:00Z' WHERE id = 'ENG-2414';\n"
    by = {c["check"]: c for c in integrity_checks(man, upd)}
    assert not by["hazard_scope"]["ok"] and "L07" in by["hazard_scope"]["failures"], by["hazard_scope"]
    req = {"R1": "x"}
    for res in (None, "dated_claim", "excluded", "repaired"):
        a = {"hazard_id": "L07", "why_safe": "R1 reconciles it", "requirement": "R1"}
        if res:
            a["resolution"] = res
        r = {c["check"]: c for c in integrity_checks(dict(man, requirements=req, hazard_acknowledgements=[a]), upd)}["hazard_scope"]
        assert not r["ok"], (res, r)
    fixed = sql_for(ol) + ("UPDATE linear.linear_issues SET state_id = 'Done', completed_at = '2026-01-13T09:00:00Z', "
                           "updated_at = '2026-01-13T09:00:00Z' WHERE id = 'ENG-2414';\n")
    ack = dict(man, requirements=req, hazard_acknowledgements=[{"hazard_id": "L07", "resolution": "repaired", "why_safe": "R1 reconciles it"}])
    assert {c["check"]: c for c in integrity_checks(ack, fixed)}["hazard_scope"]["ok"]
    bad = dict(man, hazard_acknowledgements=[{"hazard_id": "L99", "why_safe": "x", "resolution": "excluded"}])
    assert not {c["check"]: c for c in integrity_checks(bad, sql_for(ol))}["hazard_scope"]["ok"]
    cited = dict(man, traps=[{"id": "T1", "base_pointers": ["linear:data.json /issues ENG-2425"]}])
    assert not {c["check"]: c for c in integrity_checks(cited, sql_for(ol))}["hazard_scope"]["ok"]  # manifest-cited L01 record
    excl = dict(cited, hazard_acknowledgements=[{"hazard_id": h, "resolution": "excluded", "why_safe": "x"} for h in ("L01", "L07")])
    assert not {c["check"]: c for c in integrity_checks(excl, sql_for(ol))}["hazard_scope"]["ok"]  # excluded yet cited


def main(argv: list[str]) -> int:
    if "--self-test" in argv:
        # base records come through tools/hg.py and persona_view, which write caches: outside a sandbox, rerun inside
        # one (tools/selftest_sandbox.py) so no shared file is written
        import selftest_sandbox as sb
        bundle = Path(__file__).resolve().parent.parent
        if not sb.in_sandbox(bundle):
            return sb.run_isolated(["hardness_gate.py", "--self-test"], source=bundle)
        _self_test()
        return 0
    profile = None
    if "--profile" in argv:
        profile = argv[argv.index("--profile") + 1]
    design = "--design" in argv
    paths = [a for a in argv if not a.startswith("--") and a not in PROFILES]
    if (profile is not None and profile not in PROFILES) or len(paths) != (1 if design else 2):
        print(__doc__, file=sys.stderr)
        return 2
    manifest = json.loads(Path(paths[0]).read_text())
    sql_text = "" if design else Path(paths[1]).read_text()
    r = evaluate(manifest, sql_text, profile, design)
    print(json.dumps(r, indent=2) if "--json" in argv else to_text(r))
    return 0 if r["verdict"] == "PASS" else 1


if __name__ == "__main__":
    from runtime_context import guarded_entry
    guarded_entry(globals(), require_source=True)
    try:
        raise SystemExit(main(sys.argv[1:]))
    except (json.JSONDecodeError, KeyError, ValueError) as error:
        print(f"hardness_gate: {error}", file=sys.stderr)
        raise SystemExit(2)
