from datetime import datetime

from pydantic import BaseModel


class AuditEntry(BaseModel):

    timestamp: datetime = datetime.now()

    agent: str

    action: str

    status: str

    message: str