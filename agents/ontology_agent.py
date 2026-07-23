from __future__ import annotations

from typing import Any, Dict

from .base_agent import BaseAgent


class OntologyAgent(BaseAgent):
    """Normalizes incoming payloads into a consistent structure."""

    def __init__(self) -> None:
        super().__init__(name="ontology_agent")

    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        normalized = {
            key.lower().replace(" ", "_"): value
            for key, value in payload.items()
        }
        return super().process({"normalized_payload": normalized})
