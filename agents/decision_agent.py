from __future__ import annotations

from typing import Any, Dict

from .base_agent import BaseAgent


class DecisionAgent(BaseAgent):
    """Produces a final decision for the case payload."""

    def __init__(self) -> None:
        super().__init__(name="decision_agent")

    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload = dict(payload)
        payload.setdefault("decision", "review")
        return super().process(payload)
