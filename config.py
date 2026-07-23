from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).resolve().parent


class Settings(BaseSettings):

    APP_NAME: str = "KYC Remediation Multi-Agent"

    MAX_RETRIES: int = 3

    AGENT_TIMEOUT: int = 15

    MIN_CONFIDENCE: float = 0.75

    class Config:
        env_file = ".env"


settings = Settings()

DATA_DIR = BASE_DIR / "data"

LOG_DIR = BASE_DIR / "logs"

CHECKPOINT_DIR = BASE_DIR / "checkpoints"

LOG_DIR.mkdir(exist_ok=True)

CHECKPOINT_DIR.mkdir(exist_ok=True)