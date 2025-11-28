from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, Sequence


@dataclass
class LeadFilter:
    """Selection rules for filtering generated leads.

    Attributes:
        industries: Optional list of industry names to keep (case-insensitive).
        countries: Optional list of target countries or regions.
        min_employee_count: Minimum company size to keep, if known.
        max_employee_count: Maximum company size to keep, if known.
    """

    industries: Optional[Sequence[str]] = None
    countries: Optional[Sequence[str]] = None
    min_employee_count: Optional[int] = None
    max_employee_count: Optional[int] = None


@dataclass
class AgentSettings:
    """Top-level configuration for the lead discovery agent."""

    keywords: Sequence[str]
    filter: LeadFilter = field(default_factory=LeadFilter)
    limit: int = 20
    dedupe: bool = True
    llm_model: Optional[str] = None
    embedding_model: Optional[str] = None
    openai_api_key: Optional[str] = None

    def normalized_keywords(self) -> List[str]:
        return [kw.strip().lower() for kw in self.keywords if kw.strip()]
