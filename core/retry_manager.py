"""
Retry manager.
"""

from config import settings


class RetryManager:

    @staticmethod
    def can_retry(retries: int):

        return retries < settings.MAX_RETRIES