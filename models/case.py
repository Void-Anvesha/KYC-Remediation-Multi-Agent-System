from typing import Any

from pydantic import BaseModel, Field

from models.audit import AuditEntry
from models.decision import Decision
from models.evidence import Evidence
from models.gap import Gap
from models.task import Task


class Case(BaseModel):
    """
    Shared workflow state.
    """

    case_id: str

    customer_id: str

    account_id: str

    legal_entity_id: str

    trigger: str

    status: str = "NEW"

    raw_data: dict[str, Any] = Field(default_factory=dict)

    normalized_data: dict[str, Any] = Field(default_factory=dict)

    gaps: list[Gap] = Field(default_factory=list)

    execution_plan: list[Task] = Field(default_factory=list)

    evidence: list[Evidence] = Field(default_factory=list)

    decision: Decision | None = None

    audit_trail: list[AuditEntry] = Field(default_factory=list)

    metadata: dict[str, Any] = Field(default_factory=dict)