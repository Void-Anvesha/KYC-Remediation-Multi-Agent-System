from __future__ import annotations

from typing import Any, Dict


class PolicyEngine:
    """A lightweight policy evaluator for demonstration purposes."""

    def evaluate(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        risk_score = payload.get("risk_score", 0)
        decision = "approve" if risk_score < 0.5 else "review"
        return {"decision": decision, "risk_score": risk_score}
