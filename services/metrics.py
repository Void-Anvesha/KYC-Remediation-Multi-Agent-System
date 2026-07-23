from __future__ import annotations

from typing import Dict, List


class MetricsService:
    """Tracks simple workflow metrics in memory."""

    def __init__(self) -> None:
        self.metrics: Dict[str, List[float]] = {}

    def record(self, name: str, value: float) -> None:
        self.metrics.setdefault(name, []).append(value)

    def snapshot(self) -> Dict[str, float]:
        return {name: sum(values) / len(values) if values else 0.0 for name, values in self.metrics.items()}
