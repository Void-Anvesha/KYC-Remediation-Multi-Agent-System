from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from config import DATA_DIR


class CaseRepository:
    """Simple repository wrapper around CSV-backed case data."""

    def __init__(self, data_dir: Path | None = None) -> None:
        self.data_dir = data_dir or DATA_DIR

    def list_cases(self) -> List[str]:
        return sorted([path.stem for path in self.data_dir.glob("*.csv")])

    def load_case(self, name: str) -> Dict[str, Any]:
        path = self.data_dir / f"{name}.csv"
        if not path.exists():
            raise FileNotFoundError(f"Case data not found: {path}")
        return {"name": name, "path": str(path)}
