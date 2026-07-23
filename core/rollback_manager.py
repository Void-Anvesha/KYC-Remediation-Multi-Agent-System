from pathlib import Path
import pickle

from config import CHECKPOINT_DIR


class RollbackManager:

    @staticmethod
    def rollback(case_id: str):

        folder = CHECKPOINT_DIR / case_id

        files = sorted(folder.glob("*.pkl"))

        if not files:
            raise Exception("No checkpoint found.")

        latest = files[-1]

        with open(latest, "rb") as f:
            return pickle.load(f)