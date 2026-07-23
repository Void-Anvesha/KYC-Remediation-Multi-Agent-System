"""
Guardrail Manager

Provides

✓ Validation

✓ Logging

✓ Retry

✓ Rollback

✓ Checkpointing

✓ Agent lifecycle
"""

from models.case import Case

from services.logger import logger

from core.validator import Validator

from core.retry_manager import RetryManager

from core.checkpoint_manager import CheckpointManager

from core.rollback_manager import RollbackManager


class GuardrailManager:

    @staticmethod
    def execute(agent, case: Case):

        Validator.validate_case(case)

        retries = 0

        while True:

            CheckpointManager.save(case)

            try:

                case = agent.pre_execute(case)

                case = agent.execute(case)

                case = agent.post_execute(case)

                logger.info(f"{agent.name} executed successfully.")

                return case

            except Exception as e:

                logger.error(
                    f"{agent.name} failed : {str(e)}"
                )

                case = RollbackManager.rollback(case.case_id)

                retries += 1

                if not RetryManager.can_retry(retries):

                    raise Exception(
                        f"{agent.name} exceeded retry limit."
                    )