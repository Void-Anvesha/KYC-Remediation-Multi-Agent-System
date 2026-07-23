from __future__ import annotations

from typing import Any, Dict

from .base_agent import BaseAgent


class OutreachAgent(BaseAgent):
    """Represents the outreach workflow step."""

    def __init__(self) -> None:
        super().__init__(name="outreach_agent")

    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload = dict(payload)
        payload.setdefault("outreach", "pending")
        return super().process(payload)
