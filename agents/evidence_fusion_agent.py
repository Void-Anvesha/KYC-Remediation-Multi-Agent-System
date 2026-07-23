from __future__ import annotations

from typing import Any, Dict

from .base_agent import BaseAgent


class EvidenceFusionAgent(BaseAgent):
    """Aggregates evidence into a structured summary."""

    def __init__(self) -> None:
        super().__init__(name="evidence_fusion_agent")

    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload = dict(payload)
        payload.setdefault("evidence_summary", "collected")
        return super().process(payload)
