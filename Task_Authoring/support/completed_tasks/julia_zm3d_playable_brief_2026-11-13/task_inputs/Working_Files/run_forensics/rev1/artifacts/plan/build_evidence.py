#!/usr/bin/env python3
"""Write Working_Files/00_V3_Authoring_Evidence.json: the scenario role review, bound to the design's normalized hash.
Run after every re-assembly of 01_Scenario_Design.md (the hash ignores pasted STAGE GATE lines). Keeps other stages' reviews."""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
WF = HERE.parent
TOOLS = WF.parent.parent / "tools"
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(TOOLS))
import design_model as M
from stage_gate import file_digest

ctx = json.loads((WF / "00_Task_Context.json").read_text())
path = WF / "00_V3_Authoring_Evidence.json"
data = json.loads(path.read_text()) if path.exists() else {}
data.update({"spec_version": "V3", "context_hash": ctx["context_hash"]})
data.setdefault("outcome_reviews", {})
B = M.BASE
data.setdefault("role_reviews", {})["scenario"] = {
    "artifact": "01_Scenario_Design.md",
    "artifact_hash": file_digest(WF / "01_Scenario_Design.md"),
    "reviewer": "claude-fable-5-2 (authoring session, /create-scenario, design D2; re-read after the coherence sweep at injection)",
    "persona_role": ctx["persona_role"],
    "rationale": (
        "The design asks Julia Lawson, Product Manager (roster role; Product function), to author the content brief and the hand-off list "
        "for the second PlayableX playable ad of Zombie Match 3D, a user-acquisition creative: Marketing and GTM work produced as Authoring. "
        "It is inside her remit on base evidence before the 2025-10-01 freeze: she wrote the storyboard and brief for the first playable in "
        f"the vendor channel on 2025-03-14 ({B['julia_dd_brief']}) and the vendor thanked her for the detailed brief "
        f"({M.VENDOR_CH}/1742063341.276529); for the second playable Brian asked her for the reference level on 2025-09-22 "
        f"({B['brian_asks_level']}); the game's design page names her as its designer ({B['gdd']}); she is a member of the vendor channel "
        f"where the start moved to 3 November ({B['vendor_nov3']}). The work is deciding what the vendor builds from (board set, enemies, "
        "rules, sound) and stating which pack lines are delivered, ready or owed; exporting or fixing an asset is never asked of her, and "
        "the ticket follow-through is limited to moving and commenting tickets in a team she belongs to (the Design team, `/team_memberships`). The requester, Frederick "
        "Stone, runs the vendor relationship in base (he chose Scenario 1 and paused development in the same channel). Nothing in the "
        "design needs a role she does not hold."),
    "source_ids": [f"slack:{B['julia_dd_brief']}", f"slack:{M.VENDOR_CH}/1742063341.276529", f"slack:{B['brian_asks_level']}",
                   f"confluence:{B['gdd']}", f"slack:{B['vendor_nov3']}", f"slack:{B['fred_scenario1']}", f"slack:{B['fred_pause']}"],
}
path.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
print("wrote", path.name, data["role_reviews"]["scenario"]["artifact_hash"])
