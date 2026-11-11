"""Local, deterministic demonstration of evidence and approval gates.

This is not an LLM and does not prove semantic entailment; the course highlights
hallucination, tools, and human review. [COURSE: 05_Week_5_Transcript.txt#lines 221-300]
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Evidence:
    evidence_id: str
    text: str
    authorized: bool


def guard_response(answer: str, cited_ids: list[str], evidence: list[Evidence]) -> dict[str, str]:
    evidence_by_id = {item.evidence_id: item for item in evidence}
    if not cited_ids:
        return {"status": "abstain", "answer": "Insufficient cited evidence."}
    if any(item_id not in evidence_by_id for item_id in cited_ids):
        return {"status": "reject", "answer": "Unknown evidence reference."}
    if any(not evidence_by_id[item_id].authorized for item_id in cited_ids):
        return {"status": "reject", "answer": "Evidence is not authorized for this user."}
    return {"status": "review", "answer": answer}


def gate_action(action: str, approved_by_human: bool) -> dict[str, str]:
    if not approved_by_human:
        return {"status": "approval_required", "action": action}
    return {"status": "approved", "action": action}


def run_demo() -> None:
    evidence = [Evidence("DOC-1", "Synthetic policy says orders need review.", True)]
    response = guard_response("Review this synthetic order.", ["DOC-1"], evidence)
    action = gate_action("route_for_review", approved_by_human=False)
    print("Guard response:", response)
    print("Action gate:", action)
    print("This demo checks citations and authorization, not semantic correctness.")


if __name__ == "__main__":
    run_demo()