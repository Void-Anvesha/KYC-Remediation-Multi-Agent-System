from enum import Enum

from pydantic import BaseModel


class DecisionType(str, Enum):

    APPROVED = "APPROVED"

    ENRICH = "ENRICH"

    OUTREACH = "OUTREACH"

    ESCALATE = "ESCALATE"

    REJECT = "REJECT"


class Decision(BaseModel):

    decision: DecisionType

    reason: str

    confidence: float

    decided_by: str