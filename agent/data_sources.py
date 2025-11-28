from __future__ import annotations

import json
from pathlib import Path
from typing import Iterable, List, Sequence

from .models import Lead


class LeadSource:
    """Interface for all lead providers."""

    def fetch(self) -> Iterable[Lead]:
        raise NotImplementedError


class LocalJSONSource(LeadSource):
    """Reads leads from a JSON file for fast iteration and offline testing."""

    def __init__(self, path: Path):
        self.path = path

    def fetch(self) -> Iterable[Lead]:
        if not self.path.exists():
            return []
        with self.path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        for entry in data:
            yield Lead(**entry)


class CompositeSource(LeadSource):
    """Aggregates multiple sources as a single iterator."""

    def __init__(self, sources: Sequence[LeadSource]):
        self.sources = sources

    def fetch(self) -> Iterable[Lead]:
        for source in self.sources:
            yield from source.fetch()


class MemorySource(LeadSource):
    """In-memory source for synthetic or test data."""

    def __init__(self, leads: List[Lead]):
        self.leads = leads

    def fetch(self) -> Iterable[Lead]:
        return list(self.leads)
