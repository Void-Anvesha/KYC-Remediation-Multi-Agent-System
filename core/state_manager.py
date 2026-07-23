"""
Workflow state manager.
"""

from models.case import Case


class StateManager:

    @staticmethod
    def update_status(case: Case, status: str):

        case.status = status

        return case