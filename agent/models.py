from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Lead:
    """Representation of a potential lead or company."""

    name: str
    industry: Optional[str] = None
    country: Optional[str] = None
    employee_count: Optional[int] = None
    description: Optional[str] = None
    metadata: Dict[str, str] = field(default_factory=dict)

    def normalized_tokens(self) -> List[str]:
        tokens = []
        for field_value in (self.name, self.industry, self.description):
            if not field_value:
                continue
            tokens.extend(field_value.lower().split())
        return tokens
