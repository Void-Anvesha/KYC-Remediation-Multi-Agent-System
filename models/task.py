from enum import Enum

from pydantic import BaseModel


class TaskStatus(str, Enum):

    PENDING = "PENDING"

    RUNNING = "RUNNING"

    COMPLETED = "COMPLETED"

    FAILED = "FAILED"


class Task(BaseModel):

    task_id: str

    agent_name: str

    priority: int

    status: TaskStatus = TaskStatus.PENDING

    retries: int = 0