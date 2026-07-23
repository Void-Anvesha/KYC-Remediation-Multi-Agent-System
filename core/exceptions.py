"""
Custom exceptions used throughout the project.
"""


class ValidationError(Exception):
    pass


class AgentExecutionError(Exception):
    pass


class RetryLimitExceeded(Exception):
    pass


class RollbackError(Exception):
    pass