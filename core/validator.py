"""
Validation utilities.
"""

from models.case import Case
from core.exceptions import ValidationError


class Validator:

    @staticmethod
    def validate_case(case: Case):

        if not case.case_id:
            raise ValidationError("Case ID missing.")

        if not case.customer_id:
            raise ValidationError("Customer ID missing.")

        if not case.account_id:
            raise ValidationError("Account ID missing.")

        return True

    @staticmethod
    def validate_confidence(score: float):

        if score < 0 or score > 1:
            raise ValidationError(
                "Confidence score must be between 0 and 1."
            )

        return True