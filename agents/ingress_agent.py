from __future__ import annotations

from typing import Any, Dict

from .base_agent import BaseAgent


class IngressAgent(BaseAgent):
    """Accepts incoming case payloads and prepares them for processing."""

    def __init__(self) -> None:
        super().__init__(name="ingress_agent")

    def process(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        payload = dict(payload)
        payload.setdefault("status", "received")
        return super().process(payload)
