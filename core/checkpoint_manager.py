"""
Checkpoint manager.
"""

import pickle
from datetime import datetime
from pathlib import Path

from config import CHECKPOINT_DIR


class CheckpointManager:

    @staticmethod
    def save(case):

        folder = CHECKPOINT_DIR / case.case_id
        folder.mkdir(parents=True, exist_ok=True)

        filename = datetime.now().strftime("%Y%m%d_%H%M%S_%f.pkl")

        filepath = folder / filename

        with open(filepath, "wb") as f:
            pickle.dump(case, f)

        return filepath