from __future__ import annotations

import argparse
import logging
from pathlib import Path
from typing import List

from agent.config import AgentSettings, LeadFilter
from agent.data_sources import CompositeSource, LocalJSONSource
from agent.lead_agent import discover_leads

logging.basicConfig(level=logging.INFO)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Lead discovery agent (local baseline)")
    parser.add_argument("keywords", nargs="+", help="Keywords describing your ideal lead")
    parser.add_argument("--data", default="data/leads.json", help="Path to a JSON file of leads")
    parser.add_argument("--industries", nargs="*", help="Restrict to these industries")
    parser.add_argument("--countries", nargs="*", help="Restrict to these countries")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of leads to return")
    return parser.parse_args()


def build_settings(args: argparse.Namespace) -> AgentSettings:
    lead_filter = LeadFilter(
        industries=args.industries or None,
        countries=args.countries or None,
    )
    return AgentSettings(
        keywords=args.keywords,
        filter=lead_filter,
        limit=args.limit,
    )


def run() -> List[str]:
    args = parse_args()
    settings = build_settings(args)
    source = CompositeSource([LocalJSONSource(Path(args.data))])
    leads = discover_leads(source, settings)
    for lead in leads:
        print(f"- {lead.name} ({lead.industry or 'n/a'}) - {lead.description or 'No description'}")
    return [lead.name for lead in leads]


if __name__ == "__main__":
    run()
