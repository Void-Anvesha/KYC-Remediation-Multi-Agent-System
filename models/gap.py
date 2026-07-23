from enum import Enum
from pydantic import BaseModel, Field


class GapSeverity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class Gap(BaseModel):
    """
    Represents a missing or stale KYC requirement.
    """

    gap_id: str
    gap_name: str
    description: str

    severity: GapSeverity = GapSeverity.MEDIUM

    resolved: bool = False

    source_agent: str | None = None