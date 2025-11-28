from __future__ import annotations

import logging
from typing import Iterable, List

from .config import AgentSettings
from .data_sources import LeadSource
from .models import Lead
from .ranking import rerank

logger = logging.getLogger(__name__)


def _apply_filter(leads: Iterable[Lead], settings: AgentSettings) -> Iterable[Lead]:
    lower_industries = [i.lower() for i in settings.filter.industries] if settings.filter.industries else []
    for lead in leads:
        if settings.filter.industries:
            if not lead.industry or lead.industry.lower() not in lower_industries:
                continue
        if settings.filter.countries:
            if not lead.country or lead.country.lower() not in [c.lower() for c in settings.filter.countries]:
                continue
        if settings.filter.min_employee_count and lead.employee_count:
            if lead.employee_count < settings.filter.min_employee_count:
                continue
        if settings.filter.max_employee_count and lead.employee_count:
            if lead.employee_count > settings.filter.max_employee_count:
                continue
        yield lead


def _deduplicate(leads: Iterable[Lead]) -> List[Lead]:
    seen = set()
    unique: List[Lead] = []
    for lead in leads:
        key = lead.name.lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(lead)
    return unique


def discover_leads(source: LeadSource, settings: AgentSettings) -> List[Lead]:
    """Discover and rerank leads from the provided source.

    The function is intentionally modular: keyword-based scoring is used as a
    baseline, and you can later insert an LLM reranking stage by swapping the
    ``rerank`` implementation.
    """

    raw_leads = source.fetch()
    filtered = _apply_filter(raw_leads, settings)
    if settings.dedupe:
        filtered = _deduplicate(filtered)
    scored = rerank(filtered, settings.normalized_keywords(), settings.limit)
    logger.info("Found %d relevant leads", len(scored))
    return [lead for lead, _ in scored]
