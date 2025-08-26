import React, { useState, useEffect } from "react";
import { PieChart, Pie, Cell, ResponsiveContainer, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from "recharts";
import { FaLightbulb, FaHospital, FaRoad, FaSeedling, FaVoteYea, FaChartLine } from "react-icons/fa";

const SovereignFundDashboard = () => {
  const [sovereignData, setSovereignData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [activeProposal, setActiveProposal] = useState(null);

  useEffect(() => {
    fetchSovereignData();
  }, []);

  const fetchSovereignData = async () => {
    try {
      const response = await fetch("http://localhost:8000/sovereign");
      const data = await response.json();
      setSovereignData(data);
    } catch (error) {
      console.error("Error fetching sovereign data:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleVote = (proposalId, vote) => {
    // Simulate voting
    console.log(`Voted ${vote ? 'FOR' : 'AGAINST'} proposal ${proposalId}`);
    // In real implementation, this would call the API
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (!sovereignData) {
    return (
      <div className="text-center text-gray-500 py-8">
        Erreur lors du chargement des données du fonds souverain
      </div>
    );
  }

  // Prepare data for charts
  const allocationData = Object.entries(sovereignData.allocations).map(([sector, percentage]) => ({
    name: sector,
    value: parseFloat(percentage.replace('%', '')),
    sector: sector
  }));

  const COLORS = {
    "Startups IA": "#3B82F6",
    "Énergie": "#F59E0B",
    "Santé": "#10B981",
    "Infrastructures": "#6366F1",
    "Agriculture": "#8B5CF6"
  };

  const impactData = [
    { name: "Population couverte santé", value: 95, unit: "%" },
    { name: "Autosuffisance énergétique", value: 60, unit: "%" },
    { name: "Routes intelligentes", value: 1000, unit: "km" },
    { name: "Fermes modernisées", value: 5000, unit: "fermes" }
  ];

  const proposals = [
    {
      id: "PROP-001",
      title: "Augmentation allocation énergie renouvelable",
      description: "Réallouer 5% vers les énergies renouvelables",
      votesFor: 156,
      votesAgainst: 89,
      deadline: "2024-12-31"
    },
    {
      id: "PROP-002",
      title: "Nouveau hub médical IA",
      description: "Investir 2B€ dans un centre médical de pointe",
      votesFor: 203,
      votesAgainst: 67,
      deadline: "2024-12-31"
    }
  ];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-2xl p-6">
        <h1 className="text-3xl font-bold mb-2">🏛️ Fonds Souverain IA</h1>
        <p className="text-blue-100">Gouvernance participative et investissements stratégiques nationaux</p>
      </div>

      {/* Section Valeur du Fonds */}
      <div className="grid md:grid-cols-2 gap-6">
        <div className="bg-white rounded-2xl p-6 shadow-lg">
          <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
            <FaChartLine className="text-blue-600" />
            Valeur du Fonds
          </h2>
          <div className="text-center">
            <div className="text-4xl font-bold text-blue-600 mb-2">
              {sovereignData.fund_value}
            </div>
            <p className="text-gray-600">Capital total sous gestion</p>
          </div>
        </div>

        <div className="bg-white rounded-2xl p-6 shadow-lg">
          <h2 className="text-xl font-semibold mb-4">Répartition sectorielle</h2>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={allocationData}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={({ name, value }) => `${name}: ${value}%`}
                  outerRadius={80}
                  fill="#8884d8"
                  dataKey="value"
                >
                  {allocationData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[entry.sector]} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Section Objectifs stratégiques */}
      <div className="bg-white rounded-2xl p-6 shadow-lg">
        <h2 className="text-xl font-semibold mb-4">🎯 Objectifs stratégiques</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
          {sovereignData.long_term_goals.map((goal, index) => (
            <div key={index} className="bg-gray-50 rounded-xl p-4 border-l-4 border-blue-500">
              <div className="flex items-center gap-3">
                {goal.includes("énergie") && <FaLightbulb className="text-yellow-500 text-xl" />}
                {goal.includes("santé") && <FaHospital className="text-green-500 text-xl" />}
                {goal.includes("Smart cities") && <FaRoad className="text-blue-500 text-xl" />}
                {goal.includes("Agriculture") && <FaSeedling className="text-purple-500 text-xl" />}
                {!goal.includes("énergie") && !goal.includes("santé") && !goal.includes("Smart cities") && !goal.includes("Agriculture") && 
                  <FaLightbulb className="text-blue-500 text-xl" />
                }
                <span className="font-medium text-gray-800">{goal}</span>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Section DAO */}
      <div className="bg-white rounded-2xl p-6 shadow-lg">
        <h2 className="text-xl font-semibold mb-4 flex items-center gap-2">
          <FaVoteYea className="text-green-600" />
          Gouvernance participative (DAO)
        </h2>
        <div className="space-y-4">
          {proposals.map((proposal) => (
            <div key={proposal.id} className="border rounded-xl p-4">
              <h3 className="font-semibold text-lg mb-2">{proposal.title}</h3>
              <p className="text-gray-600 mb-3">{proposal.description}</p>
              
              <div className="flex items-center gap-4 mb-4">
                <div className="flex-1">
                  <div className="flex justify-between text-sm mb-1">
                    <span>Votes pour</span>
                    <span className="font-medium">{proposal.votesFor}</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div 
                      className="bg-green-500 h-2 rounded-full" 
                      style={{ width: `${(proposal.votesFor / (proposal.votesFor + proposal.votesAgainst)) * 100}%` }}
                    ></div>
                  </div>
                </div>
                
                <div className="flex-1">
                  <div className="flex justify-between text-sm mb-1">
                    <span>Votes contre</span>
                    <span className="font-medium">{proposal.votesAgainst}</span>
                  </div>
                  <div className="w-full bg-gray-200 rounded-full h-2">
                    <div 
                      className="bg-red-500 h-2 rounded-full" 
                      style={{ width: `${(proposal.votesAgainst / (proposal.votesFor + proposal.votesAgainst)) * 100}%` }}
                    ></div>
                  </div>
                </div>
              </div>

              <div className="flex gap-2">
                <button
                  onClick={() => handleVote(proposal.id, true)}
                  className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition"
                >
                  Voter OUI
                </button>
                <button
                  onClick={() => handleVote(proposal.id, false)}
                  className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition"
                >
                  Voter NON
                </button>
              </div>
              
              <div className="text-sm text-gray-500 mt-2">
                Échéance: {proposal.deadline}
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Section Impact */}
      <div className="bg-white rounded-2xl p-6 shadow-lg">
        <h2 className="text-xl font-semibold mb-4">📊 Impact et indicateurs</h2>
        <div className="h-64">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={impactData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="name" />
              <YAxis />
              <Tooltip />
              <Legend />
              <Bar dataKey="value" fill="#3B82F6" />
            </BarChart>
          </ResponsiveContainer>
        </div>
        
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-4 mt-6">
          <div className="text-center">
            <div className="text-2xl font-bold text-green-600">95%</div>
            <div className="text-sm text-gray-600">Couverture santé</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-yellow-600">60%</div>
            <div className="text-sm text-gray-600">Autosuffisance énergétique</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-blue-600">1000km</div>
            <div className="text-sm text-gray-600">Routes intelligentes</div>
          </div>
          <div className="text-center">
            <div className="text-2xl font-bold text-purple-600">5000</div>
            <div className="text-sm text-gray-600">Fermes modernisées</div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default SovereignFundDashboard;