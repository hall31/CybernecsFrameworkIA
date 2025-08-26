import React, { useState, useEffect } from 'react';
import { BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, PieChart, Pie, Cell } from 'recharts';
import { 
  FaBrain, 
  FaUsers, 
  FaBalanceScale, 
  FaHistory, 
  FaChartPie,
  FaVoteYea,
  FaClock,
  FaCheckCircle
} from 'react-icons/fa';

const CoGovernanceBoard = () => {
  const [currentDecision, setCurrentDecision] = useState(null);
  const [decisionHistory, setDecisionHistory] = useState([]);
  const [boardMembers, setBoardMembers] = useState({ ai_members: [], human_members: [] });
  const [weighting, setWeighting] = useState({ AI: 50, Human: 50 });
  const [loading, setLoading] = useState(true);

  // Mock data for demonstration
  const mockCurrentDecision = {
    decision_topic: "Budget eau 2030",
    ai_vote: "Augmenter de 20%",
    human_vote: "Augmenter de 30%",
    final_decision: "Augmenter de 25%",
    weighting: { AI: 50, Human: 50 },
    timestamp: new Date().toISOString()
  };

  const mockDecisionHistory = [
    {
      decision_topic: "Réduction émissions CO2 2024",
      ai_vote: "Réduire de 40%",
      human_vote: "Réduire de 45%",
      final_decision: "Réduire de 42.5%",
      weighting: { AI: 50, Human: 50 },
      timestamp: "2024-01-15T10:30:00Z"
    },
    {
      decision_topic: "Investissement santé publique",
      ai_vote: "Investir 3% du PIB",
      human_vote: "Investir 3.5% du PIB",
      final_decision: "Investir 3.25% du PIB",
      weighting: { AI: 50, Human: 50 },
      timestamp: "2024-01-10T14:20:00Z"
    },
    {
      decision_topic: "Protection biodiversité marine",
      ai_vote: "Augmenter budget de 25%",
      human_vote: "Augmenter budget de 35%",
      final_decision: "Augmenter budget de 30%",
      weighting: { AI: 50, Human: 50 },
      timestamp: "2024-01-05T09:15:00Z"
    }
  ];

  const mockBoardMembers = {
    ai_members: ["PlanetaryAgent", "MacroFundAgent", "SovereignFundAgent", "ClimateAgent", "EconomicAgent"],
    human_members: ["Citizens", "Governments", "NGOs", "Experts", "Indigenous Communities", "Business Leaders"]
  };

  useEffect(() => {
    // Simulate API calls
    setTimeout(() => {
      setCurrentDecision(mockCurrentDecision);
      setDecisionHistory(mockDecisionHistory);
      setBoardMembers(mockBoardMembers);
      setLoading(false);
    }, 1000);
  }, []);

  const handleWeightingChange = (newWeighting) => {
    setWeighting(newWeighting);
  };

  const chartData = [
    { name: 'Vote IA', value: currentDecision?.ai_vote || 'N/A', fill: '#3B82F6' },
    { name: 'Vote Humains', value: currentDecision?.human_vote || 'N/A', fill: '#10B981' },
    { name: 'Décision Finale', value: currentDecision?.final_decision || 'N/A', fill: '#8B5CF6' }
  ];

  const weightingData = [
    { name: 'IA', value: weighting.AI, fill: '#3B82F6' },
    { name: 'Humains', value: weighting.Human, fill: '#10B981' }
  ];

  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-screen">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 p-6">
      <div className="max-w-7xl mx-auto">
        {/* Header */}
        <div className="text-center mb-8">
          <h1 className="text-4xl font-bold text-slate-800 mb-2">
            Co-Governance Board
          </h1>
          <p className="text-lg text-slate-600">
            Gouvernance hybride IA + Humains pour un avenir équilibré
          </p>
        </div>

        {/* Current Decision Section */}
        <div className="bg-white rounded-2xl shadow-xl p-6 mb-8">
          <div className="flex items-center mb-6">
            <FaBalanceScale className="text-3xl text-purple-600 mr-3" />
            <h2 className="text-2xl font-bold text-slate-800">Décision en Cours</h2>
          </div>
          
          <div className="grid md:grid-cols-2 gap-6">
            <div className="space-y-4">
              <div className="bg-blue-50 rounded-lg p-4">
                <div className="flex items-center mb-2">
                  <FaBrain className="text-blue-600 mr-2" />
                  <h3 className="font-semibold text-blue-800">Vote IA</h3>
                </div>
                <p className="text-2xl font-bold text-blue-600">{currentDecision?.ai_vote}</p>
              </div>
              
              <div className="bg-green-50 rounded-lg p-4">
                <div className="flex items-center mb-2">
                  <FaUsers className="text-green-600 mr-2" />
                  <h3 className="font-semibold text-green-800">Vote Humains</h3>
                </div>
                <p className="text-2xl font-bold text-green-600">{currentDecision?.human_vote}</p>
              </div>
            </div>
            
            <div className="bg-purple-50 rounded-lg p-6 text-center">
              <h3 className="text-lg font-semibold text-purple-800 mb-3">Décision Finale</h3>
              <p className="text-3xl font-bold text-purple-600">{currentDecision?.final_decision}</p>
              <div className="mt-4 text-sm text-purple-600">
                <p>Pondération: IA {weighting.AI}% | Humains {weighting.Human}%</p>
              </div>
            </div>
          </div>
          
          <div className="mt-6">
            <h4 className="font-semibold text-slate-700 mb-3">Sujet de la Décision</h4>
            <p className="text-lg text-slate-800 bg-slate-50 rounded-lg p-4">
              {currentDecision?.decision_topic}
            </p>
          </div>
        </div>

        {/* Weighting Section */}
        <div className="bg-white rounded-2xl shadow-xl p-6 mb-8">
          <div className="flex items-center mb-6">
            <FaChartPie className="text-3xl text-indigo-600 mr-3" />
            <h2 className="text-2xl font-bold text-slate-800">Pondération IA vs Humains</h2>
          </div>
          
          <div className="grid md:grid-cols-2 gap-8">
            <div>
              <h3 className="text-lg font-semibold text-slate-700 mb-4">Ajuster la Pondération</h3>
              <div className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    IA: {weighting.AI}%
                  </label>
                  <input
                    type="range"
                    min="0"
                    max="100"
                    value={weighting.AI}
                    onChange={(e) => {
                      const aiValue = parseInt(e.target.value);
                      handleWeightingChange({ AI: aiValue, Human: 100 - aiValue });
                    }}
                    className="w-full h-2 bg-blue-200 rounded-lg appearance-none cursor-pointer"
                  />
                </div>
                
                <div>
                  <label className="block text-sm font-medium text-slate-700 mb-2">
                    Humains: {weighting.Human}%
                  </label>
                  <input
                    type="range"
                    min="0"
                    max="100"
                    value={weighting.Human}
                    onChange={(e) => {
                      const humanValue = parseInt(e.target.value);
                      handleWeightingChange({ AI: 100 - humanValue, Human: humanValue });
                    }}
                    className="w-full h-2 bg-green-200 rounded-lg appearance-none cursor-pointer"
                  />
                </div>
              </div>
            </div>
            
            <div className="flex justify-center">
              <ResponsiveContainer width={200} height={200}>
                <PieChart>
                  <Pie
                    data={weightingData}
                    cx="50%"
                    cy="50%"
                    innerRadius={60}
                    outerRadius={80}
                    paddingAngle={5}
                    dataKey="value"
                  >
                    {weightingData.map((entry, index) => (
                      <Cell key={`cell-${index}`} fill={entry.fill} />
                    ))}
                  </Pie>
                  <Tooltip />
                </PieChart>
              </ResponsiveContainer>
            </div>
          </div>
        </div>

        {/* Decision History Section */}
        <div className="bg-white rounded-2xl shadow-xl p-6 mb-8">
          <div className="flex items-center mb-6">
            <FaHistory className="text-3xl text-amber-600 mr-3" />
            <h2 className="text-2xl font-bold text-slate-800">Historique des Décisions</h2>
          </div>
          
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="border-b border-slate-200">
                  <th className="text-left p-3 font-semibold text-slate-700">Sujet</th>
                  <th className="text-left p-3 font-semibold text-slate-700">Vote IA</th>
                  <th className="text-left p-3 font-semibold text-slate-700">Vote Humains</th>
                  <th className="text-left p-3 font-semibold text-slate-700">Décision Finale</th>
                  <th className="text-left p-3 font-semibold text-slate-700">Date</th>
                </tr>
              </thead>
              <tbody>
                {decisionHistory.map((decision, index) => (
                  <tr key={index} className="border-b border-slate-100 hover:bg-slate-50">
                    <td className="p-3 text-slate-800 font-medium">{decision.decision_topic}</td>
                    <td className="p-3">
                      <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-blue-100 text-blue-800">
                        <FaBrain className="mr-1" />
                        {decision.ai_vote}
                      </span>
                    </td>
                    <td className="p-3">
                      <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
                        <FaUsers className="mr-1" />
                        {decision.human_vote}
                      </span>
                    </td>
                    <td className="p-3">
                      <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-purple-100 text-purple-800">
                        <FaCheckCircle className="mr-1" />
                        {decision.final_decision}
                      </span>
                    </td>
                    <td className="p-3 text-sm text-slate-600">
                      {new Date(decision.timestamp).toLocaleDateString('fr-FR')}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>

        {/* Board Members Section */}
        <div className="bg-white rounded-2xl shadow-xl p-6">
          <div className="flex items-center mb-6">
            <FaUsers className="text-3xl text-emerald-600 mr-3" />
            <h2 className="text-2xl font-bold text-slate-800">Membres du Conseil</h2>
          </div>
          
          <div className="grid md:grid-cols-2 gap-8">
            <div>
              <h3 className="text-lg font-semibold text-slate-700 mb-4 flex items-center">
                <FaBrain className="text-blue-600 mr-2" />
                Membres IA
              </h3>
              <div className="space-y-2">
                {boardMembers.ai_members.map((member, index) => (
                  <div key={index} className="flex items-center p-3 bg-blue-50 rounded-lg">
                    <div className="w-3 h-3 bg-blue-500 rounded-full mr-3"></div>
                    <span className="text-blue-800 font-medium">{member}</span>
                  </div>
                ))}
              </div>
            </div>
            
            <div>
              <h3 className="text-lg font-semibold text-slate-700 mb-4 flex items-center">
                <FaUsers className="text-green-600 mr-2" />
                Membres Humains
              </h3>
              <div className="space-y-2">
                {boardMembers.human_members.map((member, index) => (
                  <div key={index} className="flex items-center p-3 bg-green-50 rounded-lg">
                    <div className="w-3 h-3 bg-green-500 rounded-full mr-3"></div>
                    <span className="text-green-800 font-medium">{member}</span>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default CoGovernanceBoard;