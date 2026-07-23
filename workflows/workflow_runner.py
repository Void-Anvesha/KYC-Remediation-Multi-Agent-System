from __future__ import annotations

from typing import Any, Dict

from agents.ingress_agent import IngressAgent
from agents.gap_detection_agent import GapDetectionAgent
from agents.registry_agent import RegistryAgent
from agents.document_agent import DocumentAgent
from agents.ownership_agent import OwnershipAgent
from agents.sanctions_agent import SanctionsAgent
from agents.evidence_fusion_agent import EvidenceFusionAgent
from agents.decision_agent import DecisionAgent


class WorkflowRunner:
    """A simple orchestrator that runs the main workflow stages sequentially."""

    def __init__(self) -> None:
        self.agents = {
            "ingress": IngressAgent(),
            "gap_detection": GapDetectionAgent(),
            "registry": RegistryAgent(),
            "document": DocumentAgent(),
            "ownership": OwnershipAgent(),
            "sanctions": SanctionsAgent(),
            "evidence_fusion": EvidenceFusionAgent(),
            "decision": DecisionAgent(),
        }

    def run(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        result = payload
        for name, agent in self.agents.items():
            result = agent.process(result)
        return result
