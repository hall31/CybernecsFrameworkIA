import React, { useState, useEffect } from 'react';
import { 
  Globe, 
  TrendingUp, 
  Target, 
  Users, 
  Zap, 
  Droplets, 
  Heart, 
  Leaf,
  Shield,
  Vote,
  BarChart3,
  Map
} from 'lucide-react';

const PlanetaryGovernance = () => {
  const [governanceData, setGovernanceData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('overview');

  useEffect(() => {
    fetchPlanetaryData();
  }, []);

  const fetchPlanetaryData = async () => {
    try {
      const response = await fetch('http://localhost:8000/planetary');
      const data = await response.json();
      setGovernanceData(data.data);
      setLoading(false);
    } catch (error) {
      console.error('Error fetching planetary data:', error);
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-900 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-500 mx-auto"></div>
          <p className="text-blue-400 mt-4 text-xl">Chargement de la gouvernance planétaire...</p>
        </div>
      </div>
    );
  }

  if (!governanceData) {
    return (
      <div className="min-h-screen bg-slate-900 flex items-center justify-center">
        <div className="text-center text-red-400">
          <p className="text-xl">Erreur lors du chargement des données</p>
          <button 
            onClick={fetchPlanetaryData}
            className="mt-4 px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            Réessayer
          </button>
        </div>
      </div>
    );
  }

  const { governance_plan, global_dao_state, summary } = governanceData;

  return (
    <div className="min-h-screen bg-slate-900 text-white">
      {/* Header */}
      <div className="bg-slate-800 border-b border-slate-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center space-x-3">
            <Globe className="h-8 w-8 text-blue-400" />
            <div>
              <h1 className="text-3xl font-bold text-white">Gouvernance Planétaire IA</h1>
              <p className="text-slate-400">Système de coordination mondiale automatisé</p>
            </div>
          </div>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="bg-slate-800 border-b border-slate-700">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <nav className="flex space-x-8">
            {[
              { id: 'overview', name: 'Vue d\'ensemble', icon: BarChart3 },
              { id: 'goals', name: 'Objectifs Mondiaux', icon: Target },
              { id: 'dao', name: 'DAO Global', icon: Vote },
              { id: 'map', name: 'Carte Interactive', icon: Map },
              { id: 'impact', name: 'Impact Global', icon: TrendingUp }
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex items-center space-x-2 py-4 px-1 border-b-2 font-medium text-sm ${
                  activeTab === tab.id
                    ? 'border-blue-500 text-blue-400'
                    : 'border-transparent text-slate-400 hover:text-slate-300 hover:border-slate-300'
                }`}
              >
                <tab.icon className="h-5 w-5" />
                <span>{tab.name}</span>
              </button>
            ))}
          </nav>
        </div>
      </div>

      {/* Main Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {activeTab === 'overview' && <OverviewTab governanceData={governanceData} />}
        {activeTab === 'goals' && <GoalsTab governancePlan={governance_plan} />}
        {activeTab === 'dao' && <DAOTab daoState={global_dao_state} />}
        {activeTab === 'map' && <MapTab sovereignFunds={governanceData.sovereign_funds_data} />}
        {activeTab === 'impact' && <ImpactTab governancePlan={governance_plan} />}
      </div>
    </div>
  );
};

// Overview Tab Component
const OverviewTab = ({ governanceData }) => {
  const { governance_plan, summary } = governanceData;
  
  return (
    <div className="space-y-8">
      {/* Planet Value Section */}
      <div className="bg-gradient-to-r from-blue-900/50 to-green-900/50 rounded-2xl p-8 border border-slate-700">
        <div className="text-center">
          <h2 className="text-4xl font-bold text-blue-400 mb-2">
            {governance_plan.planet_value}
          </h2>
          <p className="text-xl text-slate-300">Valeur Planétaire Totale</p>
          <div className="mt-4 flex justify-center space-x-4 text-sm text-slate-400">
            <span>{summary.total_countries} Pays</span>
            <span>•</span>
            <span>{summary.total_zones} Zones</span>
            <span>•</span>
            <span>{summary.global_population}</span>
          </div>
        </div>
      </div>

      {/* Allocations Chart */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div className="bg-slate-800 rounded-2xl p-6 border border-slate-700">
          <h3 className="text-xl font-semibold mb-6 flex items-center">
            <PieChart className="h-6 w-6 text-green-400 mr-2" />
            Allocations Mondiales
          </h3>
          <div className="space-y-4">
            {Object.entries(governance_plan.allocations).map(([category, percentage]) => (
              <div key={category} className="flex items-center justify-between">
                <span className="text-slate-300">{category}</span>
                <div className="flex items-center space-x-3">
                  <div className="w-32 bg-slate-700 rounded-full h-2">
                    <div 
                      className="bg-gradient-to-r from-blue-500 to-green-500 h-2 rounded-full"
                      style={{ width: percentage }}
                    ></div>
                  </div>
                  <span className="text-blue-400 font-semibold w-12 text-right">{percentage}</span>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Global Stats */}
        <div className="bg-slate-800 rounded-2xl p-6 border border-slate-700">
          <h3 className="text-xl font-semibold mb-6 flex items-center">
            <BarChart3 className="h-6 w-6 text-blue-400 mr-2" />
            Statistiques Globales
          </h3>
          <div className="grid grid-cols-2 gap-4">
            <div className="text-center p-4 bg-slate-700/50 rounded-lg">
              <div className="text-2xl font-bold text-green-400">
                {governance_plan.resources_analysis.total_energy_twh}
              </div>
              <div className="text-sm text-slate-400">TWh Énergie</div>
            </div>
            <div className="text-center p-4 bg-slate-700/50 rounded-lg">
              <div className="text-2xl font-bold text-blue-400">
                {governance_plan.resources_analysis.total_water_km3}
              </div>
              <div className="text-sm text-slate-400">km³ Eau</div>
            </div>
            <div className="text-center p-4 bg-slate-700/50 rounded-lg">
              <div className="text-2xl font-bold text-purple-400">
                {governance_plan.resources_analysis.global_health_score}
              </div>
              <div className="text-sm text-slate-400">Santé</div>
            </div>
            <div className="text-center p-4 bg-slate-700/50 rounded-lg">
              <div className="text-2xl font-bold text-yellow-400">
                {governance_plan.resources_analysis.global_agriculture_score}
              </div>
              <div className="text-sm text-slate-400">Agriculture</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

// Goals Tab Component
const GoalsTab = ({ governancePlan }) => {
  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-white mb-2">Objectifs Mondiaux IA</h2>
        <p className="text-slate-400">Sustainable Development Goals (SDGs) automatisés</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {governancePlan.global_goals.map((goal, index) => (
          <div key={index} className="bg-slate-800 rounded-xl p-6 border border-slate-700 hover:border-blue-500/50 transition-colors">
            <div className="flex items-start justify-between mb-4">
              <h3 className="text-lg font-semibold text-white">{goal.goal}</h3>
              <span className={`px-2 py-1 rounded-full text-xs font-medium ${
                goal.priority === 'High' ? 'bg-red-500/20 text-red-400' :
                goal.priority === 'Medium' ? 'bg-yellow-500/20 text-yellow-400' :
                'bg-green-500/20 text-green-400'
              }`}>
                {goal.priority}
              </span>
            </div>
            
            <div className="space-y-3">
              <div className="flex items-center justify-between text-sm">
                <span className="text-slate-400">Progression</span>
                <span className="text-blue-400 font-semibold">{goal.progress}%</span>
              </div>
              <div className="w-full bg-slate-700 rounded-full h-2">
                <div 
                  className="bg-gradient-to-r from-blue-500 to-green-500 h-2 rounded-full transition-all duration-500"
                  style={{ width: `${goal.progress}%` }}
                ></div>
              </div>
              
              <div className="flex items-center justify-between text-sm">
                <span className="text-slate-400">Objectif</span>
                <span className="text-green-400 font-semibold">{goal.target_year}</span>
              </div>
              
              <div className="flex items-center space-x-2">
                <span className={`inline-flex items-center px-2 py-1 rounded-full text-xs font-medium ${
                  goal.status === 'En cours' ? 'bg-blue-500/20 text-blue-400' : 'bg-green-500/20 text-green-400'
                }`}>
                  {goal.status}
                </span>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

// DAO Tab Component
const DAOTab = ({ daoState }) => {
  const [selectedProposal, setSelectedProposal] = useState(null);

  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-white mb-2">DAO Global</h2>
        <p className="text-slate-400">Gouvernance décentralisée mondiale</p>
      </div>

      {/* DAO Stats */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-slate-800 rounded-xl p-6 border border-slate-700 text-center">
          <div className="text-3xl font-bold text-blue-400 mb-2">{daoState.total_members}</div>
          <div className="text-slate-400">Membres</div>
        </div>
        <div className="bg-slate-800 rounded-xl p-6 border border-slate-700 text-center">
          <div className="text-3xl font-bold text-green-400 mb-2">{daoState.active_proposals}</div>
          <div className="text-slate-400">Propositions Actives</div>
        </div>
        <div className="bg-slate-800 rounded-xl p-6 border border-slate-700 text-center">
          <div className="text-3xl font-bold text-purple-400 mb-2">
            {Math.round(daoState.total_voting_power / 1000)}k
          </div>
          <div className="text-slate-400">Pouvoir de Vote</div>
        </div>
      </div>

      {/* Active Proposals */}
      <div className="bg-slate-800 rounded-xl p-6 border border-slate-700">
        <h3 className="text-xl font-semibold mb-6 flex items-center">
          <Vote className="h-6 w-6 text-green-400 mr-2" />
          Propositions Actives
        </h3>
        
        <div className="space-y-4">
          {daoState.proposals.filter(p => p.status === 'active').map((proposal) => (
            <div key={proposal.id} className="bg-slate-700/50 rounded-lg p-4">
              <div className="flex items-center justify-between mb-3">
                <h4 className="font-semibold text-white">{proposal.title}</h4>
                <span className="text-xs text-slate-400">{proposal.id}</span>
              </div>
              
              <p className="text-slate-300 text-sm mb-4">{proposal.description}</p>
              
              <div className="flex items-center justify-between">
                <div className="flex items-center space-x-4">
                  <span className="text-xs text-slate-400">{proposal.category}</span>
                  <span className="text-xs text-slate-400">
                    {new Date(proposal.created_at).toLocaleDateString()}
                  </span>
                </div>
                
                <div className="flex items-center space-x-4">
                  <div className="text-center">
                    <div className="text-sm font-semibold text-green-400">{Math.round(proposal.votes_for)}</div>
                    <div className="text-xs text-slate-400">Pour</div>
                  </div>
                  <div className="text-center">
                    <div className="text-sm font-semibold text-red-400">{Math.round(proposal.votes_against)}</div>
                    <div className="text-xs text-slate-400">Contre</div>
                  </div>
                  <div className="text-center">
                    <div className="text-sm font-semibold text-yellow-400">{Math.round(proposal.abstentions)}</div>
                    <div className="text-xs text-slate-400">Abstention</div>
                  </div>
                </div>
              </div>
              
              <div className="mt-4 flex space-x-2">
                <button className="px-4 py-2 bg-green-600 text-white rounded-lg text-sm hover:bg-green-700 transition-colors">
                  Voter Pour
                </button>
                <button className="px-4 py-2 bg-red-600 text-white rounded-lg text-sm hover:bg-red-700 transition-colors">
                  Voter Contre
                </button>
                <button className="px-4 py-2 bg-yellow-600 text-white rounded-lg text-sm hover:bg-yellow-700 transition-colors">
                  S'abstenir
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

// Map Tab Component
const MapTab = ({ sovereignFunds }) => {
  const zones = ['Europe', 'North America', 'Asia', 'Africa', 'South America', 'Oceania'];
  
  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-white mb-2">Carte Interactive Mondiale</h2>
        <p className="text-slate-400">État des ressources par zone géographique</p>
      </div>

      {/* World Map Placeholder */}
      <div className="bg-slate-800 rounded-2xl p-8 border border-slate-700 text-center">
        <Map className="h-32 w-32 text-slate-600 mx-auto mb-4" />
        <h3 className="text-xl font-semibold text-slate-400 mb-2">Carte Mondiale Interactive</h3>
        <p className="text-slate-500">Intégration Mapbox/Recharts pour visualisation géographique</p>
      </div>

      {/* Zone Analysis */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {zones.map((zone) => {
          const zoneFunds = Object.values(sovereignFunds).filter(fund => fund.zone === zone);
          const avgHealth = zoneFunds.reduce((sum, fund) => sum + fund.resources.health, 0) / zoneFunds.length;
          const avgEnergy = zoneFunds.reduce((sum, fund) => sum + fund.resources.energy, 0) / zoneFunds.length;
          
          return (
            <div key={zone} className="bg-slate-800 rounded-xl p-6 border border-slate-700">
              <h3 className="text-lg font-semibold text-white mb-4">{zone}</h3>
              
              <div className="space-y-3">
                <div className="flex items-center justify-between">
                  <span className="text-slate-400">Pays</span>
                  <span className="text-blue-400 font-semibold">{zoneFunds.length}</span>
                </div>
                
                <div className="flex items-center justify-between">
                  <span className="text-slate-400">Santé</span>
                  <span className={`font-semibold ${
                    avgHealth > 0.7 ? 'text-green-400' : 
                    avgHealth > 0.5 ? 'text-yellow-400' : 'text-red-400'
                  }`}>
                    {Math.round(avgHealth * 100)}%
                  </span>
                </div>
                
                <div className="flex items-center justify-between">
                  <span className="text-slate-400">Énergie</span>
                  <span className="text-purple-400 font-semibold">
                    {avgEnergy.toFixed(2)} TWh
                  </span>
                </div>
                
                <div className="w-full bg-slate-700 rounded-full h-2">
                  <div 
                    className="bg-gradient-to-r from-blue-500 to-green-500 h-2 rounded-full"
                    style={{ width: `${avgHealth * 100}%` }}
                  ></div>
                </div>
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

// Impact Tab Component
const ImpactTab = ({ governancePlan }) => {
  return (
    <div className="space-y-6">
      <div className="text-center mb-8">
        <h2 className="text-3xl font-bold text-white mb-2">Impact Global</h2>
        <p className="text-slate-400">Métriques et indicateurs de développement durable</p>
      </div>

      {/* Impact Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div className="bg-slate-800 rounded-xl p-6 border border-slate-700">
          <h3 className="text-xl font-semibold mb-6 flex items-center">
            <TrendingUp className="h-6 w-6 text-green-400 mr-2" />
            Indicateurs Climatiques
          </h3>
          
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <span className="text-slate-300">Risque Climatique</span>
              <span className="text-red-400 font-semibold">
                {Math.round(governancePlan.needs_analysis.climate_risk_score * 100)}%
              </span>
            </div>
            
            <div className="w-full bg-slate-700 rounded-full h-2">
              <div 
                className="bg-red-500 h-2 rounded-full"
                style={{ width: `${governancePlan.needs_analysis.climate_risk_score * 100}%` }}
              ></div>
            </div>
            
            <div className="flex items-center justify-between">
              <span className="text-slate-300">Durabilité</span>
              <span className="text-green-400 font-semibold">
                {Math.round(governancePlan.needs_analysis.sustainability_index * 100)}%
              </span>
            </div>
            
            <div className="w-full bg-slate-700 rounded-full h-2">
              <div 
                className="bg-green-500 h-2 rounded-full"
                style={{ width: `${governancePlan.needs_analysis.sustainability_index * 100}%` }}
              ></div>
            </div>
          </div>
        </div>

        <div className="bg-slate-800 rounded-xl p-6 border border-slate-700">
          <h3 className="text-xl font-semibold mb-6 flex items-center">
            <Users className="h-6 w-6 text-blue-400 mr-2" />
            Démographie & Développement
          </h3>
          
          <div className="space-y-4">
            <div className="flex items-center justify-between">
              <span className="text-slate-300">Population</span>
              <span className="text-blue-400 font-semibold">
                {governancePlan.needs_analysis.total_population_millions}M
              </span>
            </div>
            
            <div className="flex items-center justify-between">
              <span className="text-slate-300">Urbanisation</span>
              <span className="text-purple-400 font-semibold">
                {Math.round(governancePlan.needs_analysis.urbanization_rate * 100)}%
              </span>
            </div>
            
            <div className="flex items-center justify-between">
              <span className="text-slate-300">Pauvreté</span>
              <span className="text-red-400 font-semibold">
                {Math.round(governancePlan.needs_analysis.poverty_rate * 100)}%
              </span>
            </div>
          </div>
        </div>
      </div>

      {/* Charts Placeholder */}
      <div className="bg-slate-800 rounded-xl p-8 border border-slate-700 text-center">
        <BarChart3 className="h-32 w-32 text-slate-600 mx-auto mb-4" />
        <h3 className="text-xl font-semibold text-slate-400 mb-2">Graphiques d'Impact</h3>
        <p className="text-slate-500">Intégration Recharts pour visualisation des tendances</p>
      </div>
    </div>
  );
};

// Simple PieChart component
const PieChart = ({ className }) => (
  <svg className={className} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
    <circle cx="12" cy="12" r="10" strokeDasharray="31.416" strokeDashoffset="31.416" transform="rotate(-90 12 12)"/>
    <path d="M12 2a10 10 0 0 1 10 10" strokeDasharray="31.416" strokeDashoffset="15.708"/>
  </svg>
);

export default PlanetaryGovernance;