# Logger stub
import logging

from pathlib import Path

from config import LOG_DIR

LOG_DIR.mkdir(exist_ok=True)

logger = logging.getLogger("KYC")

logger.setLevel(logging.INFO)

handler = logging.FileHandler(LOG_DIR / "application.log")

formatter = logging.Formatter(

"%(asctime)s | %(levelname)s | %(message)s"

)

handler.setFormatter(formatter)

logger.addHandler(handler)