"""dd-q4-claims-register solver.

Truth owner for the 13-claim Q4 claims register (Julia Lawson, Product, Normal Horizon).
Parses the injection SQL as data through tools/base_check.parse_sql; never executes SQL.
The classification is the design's intended truth; base records are routed for the golden check.
"""
import collections

KEY_REGEX = r"C\d{2}"
FIELDS = ["claim_id", "claim", "feature", "scope", "status", "decision", "qualifier",
          "evidence", "evidence_date", "conflict", "owner", "action"]
CLASS_FIELD = "status"
GROUPS_FIELD = "groups"
REVISIONS = ("r1",)

DRAFT = "f_5a1b2c3d4e5f60718293a4"
TRELLO_COLLECTIBLES = "67ec1f6021f4291d45f9c21e"
GDD = "page_domino_gdd"
LIVEOPS = "page_live_ops_engine"

CLAIMS = {
    "C01": ("Weekly Quests run every week.", "Weekly Quests", "player-facing", "LIVE", "KEEP", "none", "cmt_eng2369_1", "2025-09-29T10:00:00Z", "none", "Live Ops"),
    "C02": ("Weekly Leaderboards are automated.", "Weekly Leaderboards", "player-facing", "LIVE", "KEEP", "none", "cmt_eng1874_1", "2025-09-29T10:10:00Z", "none", "Live Ops"),
    "C03": ("Win & Collect runs every day.", "Win & Collect", "player-facing", "LIVE", "QUALIFY", "runs Mon/Wed/Fri, not daily", "cmt_eng1385_1", "2025-09-29T10:20:00Z", "none", "Live Ops"),
    "C04": ("River Rush is live.", "River Rush", "player-facing", "LIVE", "KEEP", "none", "cmt_eng2373_1", "2025-09-30T10:30:00Z", "none", "Live Ops"),
    "C05": ("Axe Arena and Streak Fever are live.", "Axe Arena and Streak Fever", "player-facing", "LIVE", "KEEP", "none", "cmt_eng2374_1", "2025-09-29T17:10:00Z", "none", "Live Ops"),
    "C06": ("Season Pass is live on Domino Delights (shipped in #1755, ticket ENG-2136).", "Season Pass", "player-facing", "NOT_LIVE", "DROP", "flag default-off; replaced by the $0.99 starter pack on the out-of-moves screen", "cmt_eng2136_1", "2025-09-28T16:00:00Z", "claims draft says live; readiness P0 and config comment say not live - config comment governs", "Commerce"),
    "C07": ("Collectibles ship in October.", "Collectibles", "player-facing", "NOT_LIVE", "DROP", "no build slot this quarter", "dce0ca4cfe773cf514fdda4b59176f73", "2025-09-30T17:00:00.000400Z", "none", "Product"),
    "C08": ("Rewarded ads and remove-ads IAP are live.", "Rewarded ads", "player-facing", "LIVE", "KEEP", "none", "cmt_eng2372_1", "2025-09-28T17:00:00Z", "none", "Monetization"),
    "C09": ("Five coin bundles and a starter pack are live in the shop.", "coin bundles", "player-facing", "LIVE", "QUALIFY", "four coin bundles plus the starter pack", "cmt_eng2371_1", "2025-09-26T13:20:00Z", "none", "Commerce"),
    "C10": ("Hero Offers rotate every 48 hours.", "Hero Offers", "player-facing", "TESTING", "QUALIFY", "in testing at a 10% cohort; the 48-hour rotation is the enabled behaviour", "cmt_eng2323_1", "2025-09-28T16:20:00Z", "none", "Commerce"),
    "C11": ("The live-ops event engine is live.", "live-ops event engine", "internal tooling", "OUT_OF_SCOPE", "DROP", "internal tooling, not a player-facing claim", "page_live_ops_engine", "2024-08-15T16:07:58Z", "none", "Platform"),
    "C12": ("5,000 handcrafted levels are live.", "levels", "player-facing", "LIVE", "QUALIFY", "4,755 live; 245 planned", "page_domino_gdd", "2025-09-15T14:39:52Z", "none", "Design"),
    "C13": ("Domino Delights launched on 14 April 2025.", "launched", "player-facing", "LIVE", "QUALIFY", "US soft launch 11 April 2025; worldwide 6 May 2025; 14 April unsupported", "page_domino_gdd", "2025-09-15T14:39:52Z", "claims draft says 14 April; readiness says 23 April; GDD governs", "Product"),
}

EVIDENCE = {k: [v[6]] for k, v in CLAIMS.items()}
DATE_EVIDENCE = {k: [v[6]] for k, v in CLAIMS.items()}
CLAIM_EVIDENCE = {k: [DRAFT] for k in CLAIMS}

RULES = {
    "M1_status": {"mechanism": "A1", "family": "wrong summary + thread past its conclusion (A1)", "requirement": "R1",
                  "nodes": ["T1", "T5", "C1"], "decides": ["status", "decision"], "controls": ["C01", "C02", "C04"],
                  "over_application": "over:all-not-live", "source": "claims-draft",
                  "natural_reading": "trust the claims draft's all-live summary"},
    "M2_flag": {"mechanism": "A15", "family": "A15", "requirement": "R1", "nodes": ["T2", "C2"],
                "decides": ["status", "decision"], "controls": ["C01", "C02", "C08"],
                "over_application": "over:all-testing", "source": "live-standard",
                "natural_reading": "Done plus merged means live"},
    "M3_live_standard": {"mechanism": "A12", "family": "A12", "requirement": "R1", "nodes": ["T2"],
                         "decides": ["status", "decision"], "controls": ["C01"],
                         "over_application": "over:engineering-page-rejects", "source": "live-standard",
                         "natural_reading": "use the first release-status page found"},
    "M4_wording": {"mechanism": "A12", "family": "A12", "requirement": "R2", "nodes": ["T3"],
                   "decides": ["decision", "qualifier"], "controls": ["C01", "C02"],
                   "over_application": "over:all-in-testing", "source": "wording-rules",
                   "natural_reading": "anything shipped may be called live"},
    "M5_scope": {"mechanism": "A7", "family": "A7", "requirement": "R3", "nodes": ["T4", "T11", "C4"],
                 "decides": ["scope", "status"], "controls": ["C01", "C04"],
                 "over_application": "over:all-out-of-scope", "source": "scope-note",
                 "natural_reading": "a live feature is in scope"},
    "M6_conflict": {"mechanism": "A16", "family": "A16", "requirement": "R5", "nodes": ["T5", "C5"],
                    "decides": ["conflict", "decision"], "controls": ["C01", "C02"],
                    "over_application": "over:all-conflict", "source": "claims-draft",
                    "natural_reading": "pick the more recent of two sources silently"},
    "M7_counts": {"mechanism": "A19", "family": "A19", "requirement": "R7", "nodes": ["T6", "T7", "C1"],
                  "decides": ["decision", "qualifier"], "controls": ["C01", "C02"],
                  "over_application": "over:count-runs", "source": "claims-draft",
                  "natural_reading": "count rows or repeat card numbers"},
}

DEGRADES = {
    "over:all-not-live": "over-apply the live rule to every claim",
    "over:all-testing": "over-apply the flag rule to every claim",
    "over:engineering-page-rejects": "over-apply the Engineering release definition to a live claim",
    "over:all-in-testing": "over-apply the testing wording to every claim",
    "over:all-out-of-scope": "over-apply the scope rule to every claim",
    "over:all-conflict": "over-apply the conflict rule to every claim",
    "over:count-runs": "over-apply the count rule to every claim",
    "slip:claims": "a claim slips from the evidence to the draft framing",
    "skip:pr": "the PR thread is skipped on the two contested claims",
    "skip:scope": "the scope note is skipped on the internal-tooling claim",
}

CHANNELS = {
    "scale:claims": {"kind": "scale", "degrade": "slip:claims", "members": list(CLAIMS), "latent": "member",
                     "family": "scale", "description": "a per-claim classification slips"},
    "tool_surface:pr": {"kind": "tool_surface", "degrade": "skip:pr", "members": ["C06", "C10"], "latent": "member",
                        "family": "tool_surface", "description": "the PR conversation is skipped"},
    "delegation:scope": {"kind": "delegation", "degrade": "skip:scope", "members": ["C11"], "latent": "member",
                         "family": "delegation", "description": "the scope note is not applied"},
}

BASE_ROUTES = {
    "67ec1f6021f4291d45f9c21e": {"service": "trello", "file": "data.json", "pointer": "/cards", "field": "id"},
    "page_domino_gdd": {"service": "confluence", "file": "confluence_working.json", "pointer": "/pages", "field": "id"},
    "page_live_ops_engine": {"service": "confluence", "file": "confluence_working.json", "pointer": "/pages", "field": "id"},
    "ENG-2136": {"service": "linear", "file": "data.json", "pointer": "/issues", "field": "identifier"},
    "ENG-2323": {"service": "linear", "file": "data.json", "pointer": "/issues", "field": "identifier"},
    "f_c57724584820a26f3bbe54": {"service": "gdocs", "file": "data.json", "pointer": "/docs_documents", "field": "document_id"},
}


def load_state(sql_text, revision=None):
    try:
        from base_check import parse_sql
    except ImportError:  # direct use outside the tool bundle
        import pathlib, sys
        sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[3] / "tools"))
        from base_check import parse_sql
    rows = [x["row"] for x in parse_sql(sql_text) if x["op"] == "insert"]
    ids = {str(r.get("id")) for r in rows if r.get("id")}
    return {"rows": rows, "ids": ids, "revision": revision or "r1"}


def keys():
    return list(CLAIMS)


def _off(spec, name, key):
    for d in spec:
        if isinstance(d, tuple):
            if d[0] == name and key in d[1]:
                return True
        elif d == name:
            return True
    return False


def _mk(key):
    c = CLAIMS[key]
    return {"claim_id": key, "claim": c[0], "feature": c[1], "scope": c[2], "status": c[3],
            "decision": c[4], "qualifier": c[5], "evidence": c[6], "evidence_date": c[7],
            "conflict": c[8], "owner": c[9], "action": "none", "groups": []}


SQL_EVIDENCE = {k: v[6] for k, v in CLAIMS.items() if k not in ("C11", "C12", "C13")}

def _present(state, key):
    ids = state.get("ids") if isinstance(state, dict) else None
    if not ids:
        return True
    ev = SQL_EVIDENCE.get(key)
    return ev in ids if ev else True


def solve(state, disable=frozenset(), degrade=frozenset(), keys_=None):
    out = {}
    ids = state.get("ids") if isinstance(state, dict) else None
    draft_present = (not ids) or (DRAFT in ids)
    wording_present = (not ids) or ("68d672304f5e6d7a8b9c0d11" in ids)
    for k in (keys_ or keys()):
        r = _mk(k)
        if not draft_present:
            r["status"] = "LIVE"; r["decision"] = "KEEP"; r["qualifier"] = "none"
            out[k] = r
            continue
        if not wording_present:
            r["decision"] = "KEEP"; r["qualifier"] = "none"
            out[k] = r
            continue
        if not _present(state, k):
            r["status"] = "LIVE"; r["decision"] = "KEEP"; r["qualifier"] = "none"
            out[k] = r
            continue
        # rule ablations
        if _off(disable, "M1_status", k):
            r["status"] = "LIVE"; r["decision"] = "KEEP"; r["qualifier"] = "none"
        if _off(disable, "M2_flag", k):
            if k in ("C06", "C10"):
                r["status"] = "LIVE"; r["decision"] = "KEEP"; r["qualifier"] = "none"
        if _off(disable, "M3_live_standard", k):
            if k == "C06":
                r["status"] = "LIVE"; r["decision"] = "KEEP"; r["qualifier"] = "none"
        if _off(disable, "M4_wording", k):
            r["decision"] = "KEEP"; r["qualifier"] = "none"
        if _off(disable, "M5_scope", k):
            if k == "C11":
                r["scope"] = "player-facing"; r["status"] = "LIVE"; r["decision"] = "KEEP"; r["qualifier"] = "none"
        if _off(disable, "M6_conflict", k):
            if k in ("C06", "C13"):
                r["conflict"] = "none"
            if k == "C13":
                r["decision"] = "KEEP"; r["qualifier"] = "none"
        if _off(disable, "M7_counts", k):
            if k in ("C03", "C09", "C12"):
                r["decision"] = "KEEP"; r["qualifier"] = "none"
        # over-application operators (control members)
        if _off(degrade, "over:all-not-live", k):
            r["status"] = "NOT_LIVE"; r["decision"] = "DROP"; r["qualifier"] = "not live"
        if _off(degrade, "over:all-testing", k):
            r["status"] = "TESTING"; r["decision"] = "QUALIFY"; r["qualifier"] = "in testing"
        if _off(degrade, "over:engineering-page-rejects", k) and k == "C01":
            r["status"] = "NOT_LIVE"; r["decision"] = "DROP"; r["qualifier"] = "not live"
        if _off(degrade, "over:all-in-testing", k):
            r["qualifier"] = "in testing"; r["decision"] = "QUALIFY"
        if _off(degrade, "over:all-out-of-scope", k):
            r["scope"] = "internal tooling"; r["status"] = "OUT_OF_SCOPE"; r["decision"] = "DROP"
        if _off(degrade, "over:all-conflict", k):
            r["conflict"] = "conflict"
        if _off(degrade, "over:count-runs", k):
            r["decision"] = "QUALIFY"; r["qualifier"] = "count mismatch"
        # declared channels
        if _off(degrade, "slip:claims", k) and k in ("C06", "C10", "C11", "C13"):
            r["status"] = "LIVE"; r["decision"] = "KEEP"; r["qualifier"] = "none"
        if _off(degrade, "skip:pr", k) and k in ("C06", "C10"):
            r["status"] = "LIVE"; r["decision"] = "KEEP"; r["qualifier"] = "none"
        if _off(degrade, "skip:scope", k) and k == "C11":
            r["scope"] = "player-facing"; r["status"] = "LIVE"; r["decision"] = "KEEP"; r["qualifier"] = "none"
        out[k] = r
    return out


def aggregates(rows):
    return {"classes": dict(collections.Counter(v["status"] for v in rows.values())), "groups": {}}


def evidence(rows, key, field):
    if field in ("status", "decision", "qualifier", "conflict", "scope", "owner", "action", "claim", "feature"):
        if field in ("claim", "feature"):
            return [DRAFT]
        return []
    if field == "evidence":
        return EVIDENCE.get(key, [])
    if field == "evidence_date":
        return DATE_EVIDENCE.get(key, [])
    if field == "claim_id":
        return []
    return []


TOUCHED = {
    "M1_status": list(CLAIMS),
    "M2_flag": ["C06", "C10"],
    "M3_live_standard": ["C06"],
    "M4_wording": list(CLAIMS),
    "M5_scope": ["C11"],
    "M6_conflict": ["C06", "C13"],
    "M7_counts": ["C03", "C09", "C12"],
}

def touched(state, rule):
    return set(TOUCHED.get(rule, []))


def deciding(state, rule, key):
    if rule == "M1_status":
        return [DRAFT]
    if rule == "M4_wording":
        return ["68d672304f5e6d7a8b9c0d11"]
    return EVIDENCE.get(key, [])


def base_route(record_id):
    return BASE_ROUTES.get(record_id)
