from __future__ import annotations

import math
from collections import Counter
from typing import Iterable, List, Sequence, Tuple

from .models import Lead


def _tokenize_keywords(keywords: Sequence[str]) -> List[str]:
    tokens: List[str] = []
    for kw in keywords:
        kw = kw.lower().strip()
        if not kw:
            continue
        tokens.extend(kw.split())
    return tokens


def keyword_score(lead: Lead, keywords: Sequence[str]) -> float:
    """Compute a simple relevance score using token overlap.

    The scoring is cosine similarity between keyword tokens and lead tokens,
    which provides a fast, dependency-free baseline. External LLM reranking can
    be layered on top of this score later.
    """

    keyword_tokens = _tokenize_keywords(keywords)
    lead_tokens = lead.normalized_tokens()
    if not keyword_tokens or not lead_tokens:
        return 0.0

    keyword_counter = Counter(keyword_tokens)
    lead_counter = Counter(lead_tokens)

    dot_product = sum(keyword_counter[t] * lead_counter[t] for t in keyword_counter)
    if dot_product == 0:
        return 0.0

    keyword_norm = math.sqrt(sum(v * v for v in keyword_counter.values()))
    lead_norm = math.sqrt(sum(v * v for v in lead_counter.values()))
    if keyword_norm == 0 or lead_norm == 0:
        return 0.0
    return dot_product / (keyword_norm * lead_norm)


def rerank(leads: Iterable[Lead], keywords: Sequence[str], limit: int) -> List[Tuple[Lead, float]]:
    scored: List[Tuple[Lead, float]] = []
    for lead in leads:
        score = keyword_score(lead, keywords)
        if score == 0:
            continue
        scored.append((lead, score))
    scored.sort(key=lambda pair: pair[1], reverse=True)
    return scored[:limit]
