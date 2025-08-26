from utils.logger import log_event
from typing import Dict, List, Optional
import random
from datetime import datetime

class SovereignFundAgent:
    """Agent représentant un fonds souverain d'un pays/zone"""
    def __init__(self, country: str, zone: str):
        self.country = country
        self.zone = zone
        self.resources = {
            "energy": random.uniform(0.1, 1.0),  # TWh
            "water": random.uniform(0.5, 2.0),   # km³
            "health": random.uniform(0.3, 0.9),  # score 0-1
            "agriculture": random.uniform(0.2, 0.8),  # score 0-1
            "population": random.uniform(1, 100),  # millions
            "gdp": random.uniform(0.1, 5.0)  # trillion €
        }
        self.status = "active"
    
    def get_status(self) -> Dict:
        return {
            "country": self.country,
            "zone": self.zone,
            "resources": self.resources,
            "status": self.status
        }

class GlobalDAO:
    """DAO mondiale pour la gouvernance décentralisée"""
    def __init__(self):
        self.members = []
        self.proposals = []
        self.votes = {}
        self.total_voting_power = 0
        log_event("GlobalDAO", "Initialized")
    
    def add_member(self, country: str, voting_power: float):
        """Ajoute un membre avec son pouvoir de vote"""
        member = {
            "country": country,
            "voting_power": voting_power,
            "joined_at": datetime.now().isoformat()
        }
        self.members.append(member)
        self.total_voting_power += voting_power
        log_event("GlobalDAO", f"Added member: {country} with {voting_power} voting power")
    
    def create_proposal(self, title: str, description: str, category: str) -> str:
        """Crée une nouvelle proposition"""
        proposal_id = f"PROP-{len(self.proposals) + 1:03d}"
        proposal = {
            "id": proposal_id,
            "title": title,
            "description": description,
            "category": category,
            "created_at": datetime.now().isoformat(),
            "status": "active",
            "votes_for": 0,
            "votes_against": 0,
            "abstentions": 0
        }
        self.proposals.append(proposal)
        log_event("GlobalDAO", f"Created proposal: {title}")
        return proposal_id
    
    def vote(self, proposal_id: str, country: str, vote: str):
        """Vote sur une proposition"""
        if vote not in ["for", "against", "abstain"]:
            return False
        
        # Trouver le membre et sa proposition
        member = next((m for m in self.members if m["country"] == country), None)
        proposal = next((p for p in self.proposals if p["id"] == proposal_id), None)
        
        if not member or not proposal:
            return False
        
        # Mettre à jour les votes
        if vote == "for":
            proposal["votes_for"] += member["voting_power"]
        elif vote == "against":
            proposal["votes_against"] += member["voting_power"]
        else:
            proposal["abstentions"] += member["voting_power"]
        
        log_event("GlobalDAO", f"Vote recorded: {country} voted {vote} on {proposal_id}")
        return True
    
    def get_active_proposals(self) -> List[Dict]:
        """Retourne les propositions actives"""
        return [p for p in self.proposals if p["status"] == "active"]
    
    def get_dao_state(self) -> Dict:
        """Retourne l'état global du DAO"""
        return {
            "total_members": len(self.members),
            "total_voting_power": self.total_voting_power,
            "active_proposals": len(self.get_active_proposals()),
            "members": self.members,
            "proposals": self.proposals
        }

class PlanetaryAgent:
    """Agent de coordination globale pour la gouvernance planétaire IA"""
    
    def __init__(self):
        self.name = "Planetary Agent"
        self.global_dao = GlobalDAO()
        self.sovereign_funds = {}
        self.planet_value = 0
        self.allocations = {}
        self.global_goals = []
        
        # Initialiser les fonds souverains par zone
        self._initialize_sovereign_funds()
        self._initialize_global_dao()
        
        log_event(self.name, "Initialized - Global Governance AI System Active")
    
    def _initialize_sovereign_funds(self):
        """Initialise les fonds souverains par zone géographique"""
        zones = {
            "Europe": ["France", "Germany", "UK", "Italy", "Spain"],
            "North America": ["USA", "Canada", "Mexico"],
            "Asia": ["China", "Japan", "India", "South Korea", "Singapore"],
            "Africa": ["South Africa", "Nigeria", "Egypt", "Kenya", "Morocco"],
            "South America": ["Brazil", "Argentina", "Chile", "Colombia", "Peru"],
            "Oceania": ["Australia", "New Zealand"]
        }
        
        for zone, countries in zones.items():
            for country in countries:
                fund = SovereignFundAgent(country, zone)
                self.sovereign_funds[country] = fund
        
        log_event(self.name, f"Initialized {len(self.sovereign_funds)} sovereign funds")
    
    def _initialize_global_dao(self):
        """Initialise le DAO global avec les membres"""
        for country, fund in self.sovereign_funds.items():
            voting_power = fund.resources["gdp"] * 100  # Pondération basée sur le PIB
            self.global_dao.add_member(country, voting_power)
        
        # Créer quelques propositions initiales
        self.global_dao.create_proposal(
            "Budget eau en Afrique 2025",
            "Allocation de 50 milliards € pour l'accès à l'eau potable en Afrique",
            "Water & Agriculture"
        )
        self.global_dao.create_proposal(
            "Transition énergétique mondiale",
            "Plan de 200 milliards € pour la neutralité carbone d'ici 2050",
            "Climate"
        )
        self.global_dao.create_proposal(
            "Santé mondiale universelle",
            "Fonds de 100 milliards € pour l'accès aux soins de santé",
            "Global Health"
        )
    
    def _analyze_global_resources(self) -> Dict:
        """Analyse les ressources globales"""
        total_energy = sum(f.resources["energy"] for f in self.sovereign_funds.values())
        total_water = sum(f.resources["water"] for f in self.sovereign_funds.values())
        avg_health = sum(f.resources["health"] for f in self.sovereign_funds.values()) / len(self.sovereign_funds)
        avg_agriculture = sum(f.resources["agriculture"] for f in self.sovereign_funds.values()) / len(self.sovereign_funds)
        total_population = sum(f.resources["population"] for f in self.sovereign_funds.values())
        total_gdp = sum(f.resources["gdp"] for f in self.sovereign_funds.values())
        
        return {
            "total_energy_twh": round(total_energy, 2),
            "total_water_km3": round(total_water, 2),
            "global_health_score": round(avg_health, 3),
            "global_agriculture_score": round(avg_agriculture, 3),
            "total_population_millions": round(total_population, 1),
            "total_gdp_trillion_euro": round(total_gdp, 2)
        }
    
    def _analyze_human_needs(self) -> Dict:
        """Analyse les besoins humains globaux"""
        # Calculer les indicateurs de développement
        population = sum(f.resources["population"] for f in self.sovereign_funds.values())
        urbanization_rate = 0.65  # Taux d'urbanisation mondial estimé
        poverty_rate = 0.15  # Taux de pauvreté mondial estimé
        climate_risk = 0.7  # Risque climatique global (0-1)
        
        return {
            "total_population_millions": round(population, 1),
            "urbanization_rate": urbanization_rate,
            "poverty_rate": poverty_rate,
            "climate_risk_score": climate_risk,
            "sustainability_index": round(1 - climate_risk, 3)
        }
    
    def _generate_global_governance_plan(self) -> Dict:
        """Génère le plan de gouvernance mondiale IA"""
        resources = self._analyze_global_resources()
        needs = self._analyze_human_needs()
        
        # Calculer la valeur planétaire totale
        self.planet_value = resources["total_gdp_trillion_euro"] * 1000  # Conversion en milliards
        
        # Définir les allocations basées sur l'analyse
        self.allocations = {
            "Climat": "30%",
            "Énergie": "25%",
            "Santé mondiale": "20%",
            "Eau & Agriculture": "15%",
            "Paix & Coopération": "10%"
        }
        
        # Définir les objectifs globaux
        self.global_goals = [
            {
                "goal": "Zéro pauvreté",
                "status": "En cours",
                "progress": 65,
                "target_year": 2030,
                "priority": "High"
            },
            {
                "goal": "Énergie propre universelle",
                "status": "En cours",
                "progress": 45,
                "target_year": 2050,
                "priority": "High"
            },
            {
                "goal": "Accès santé pour tous",
                "status": "En cours",
                "progress": 70,
                "target_year": 2035,
                "priority": "Medium"
            },
            {
                "goal": "Autosuffisance alimentaire",
                "status": "En cours",
                "progress": 80,
                "target_year": 2040,
                "priority": "Medium"
            },
            {
                "goal": "Neutralité carbone",
                "status": "En cours",
                "progress": 30,
                "target_year": 2050,
                "priority": "High"
            }
        ]
        
        return {
            "planet_value": f"{self.planet_value:.1f} Milliards €",
            "allocations": self.allocations,
            "global_goals": self.global_goals,
            "resources_analysis": resources,
            "needs_analysis": needs
        }
    
    def run(self) -> Dict:
        """Exécute l'analyse planétaire et génère le plan de gouvernance"""
        log_event(self.name, "Starting global governance analysis")
        
        # Récupérer tous les SovereignFundAgents actifs
        active_funds = {
            country: fund.get_status() 
            for country, fund in self.sovereign_funds.items() 
            if fund.status == "active"
        }
        
        # Analyser les ressources et besoins
        resources_analysis = self._analyze_global_resources()
        needs_analysis = self._analyze_human_needs()
        
        # Générer le plan de gouvernance mondiale
        governance_plan = self._generate_global_governance_plan()
        
        # Obtenir l'état du DAO global
        dao_state = self.global_dao.get_dao_state()
        
        result = {
            "timestamp": datetime.now().isoformat(),
            "active_sovereign_funds": len(active_funds),
            "sovereign_funds_data": active_funds,
            "governance_plan": governance_plan,
            "global_dao_state": dao_state,
            "summary": {
                "total_countries": len(active_funds),
                "total_zones": len(set(f["zone"] for f in active_funds.values())),
                "global_population": f"{resources_analysis['total_population_millions']:.1f} millions",
                "total_gdp": f"{resources_analysis['total_gdp_trillion_euro']:.2f} trillion €"
            }
        }
        
        log_event(self.name, "Plan mondial IA défini")
        log_event(self.name, f"Valeur planétaire: {governance_plan['planet_value']}")
        
        return result
    
    def get_planetary_status(self) -> Dict:
        """Retourne le statut planétaire actuel"""
        return {
            "planet_value": self.planet_value,
            "allocations": self.allocations,
            "global_goals": self.global_goals,
            "active_funds_count": len([f for f in self.sovereign_funds.values() if f.status == "active"]),
            "dao_members_count": len(self.global_dao.members),
            "active_proposals_count": len(self.global_dao.get_active_proposals())
        }