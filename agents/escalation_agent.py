from __future__ import annotations

from typing import Any, Dict

from .base_agent import BaseAgent


class EscalationAgent(BaseAgent):
    """Handles escalation routing for high-risk or blocked cases."""

    def __init__(self) -> None:
        super().__init__(name="escalation_agent")

    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload = dict(payload)
        payload.setdefault("escalation", "review_required")
        return super().process(payload)
