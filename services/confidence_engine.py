from __future__ import annotations

from typing import Any, Dict


class ConfidenceEngine:
    """Assigns a simple confidence score based on evidence presence."""

    def score(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        evidence = payload.get("evidence", [])
        score = min(1.0, 0.25 + (0.1 * len(evidence)))
        return {"confidence_score": round(score, 2)}
