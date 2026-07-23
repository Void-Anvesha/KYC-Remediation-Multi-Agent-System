from __future__ import annotations

from typing import Any, Dict

from .base_agent import BaseAgent


class EnrichmentAgent(BaseAgent):
    """Coordinates enrichment-style checks for a case payload."""

    def __init__(self) -> None:
        super().__init__(name="enrichment_agent")

    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload = dict(payload)
        payload.setdefault("enrichment", "completed")
        return super().process(payload)
