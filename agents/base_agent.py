"""
Base class for all KYC workflow agents.
"""

from abc import ABC, abstractmethod
from typing import Any

from models.case import Case
from services.logger import logger


class BaseAgent(ABC):
    """
    Every agent in the system inherits from this class.

    Workflow:

    pre_execute()
            ↓
    execute()
            ↓
    post_execute()
    """

    def __init__(self):

        self.name = self.__class__.__name__

    # --------------------------------------------------

    def pre_execute(self, case: Case) -> Case:
        """
        Runs before execute().
        Override if required.
        """

        logger.info(f"[{self.name}] Starting execution.")

        return case

    # --------------------------------------------------

    @abstractmethod
    def execute(self, case: Case) -> Case:
        """
        Main business logic.
        Must be implemented.
        """
        pass

    # --------------------------------------------------

    def post_execute(self, case: Case) -> Case:
        """
        Runs after execute().
        Override if required.
        """

        logger.info(f"[{self.name}] Finished execution.")

        return case

    # --------------------------------------------------

    def log(self, message: str):

        logger.info(f"[{self.name}] {message}")