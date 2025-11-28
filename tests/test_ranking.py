from agent.config import AgentSettings, LeadFilter
from agent.data_sources import MemorySource
from agent.lead_agent import discover_leads
from agent.models import Lead


def test_discover_leads_filters_and_ranks():
    leads = [
        Lead(name="Alpha", industry="Marketing", description="outbound ia"),
        Lead(name="Beta", industry="Fintech", description="payments"),
        Lead(name="Gamma", industry="Marketing", description="growth outbound ia"),
    ]
    source = MemorySource(leads)
    settings = AgentSettings(keywords=["outbound", "ia"], filter=LeadFilter(industries=["Marketing"]), limit=2)

    results = discover_leads(source, settings)

    assert [lead.name for lead in results] == ["Alpha", "Gamma"]
    assert len(results) == 2
