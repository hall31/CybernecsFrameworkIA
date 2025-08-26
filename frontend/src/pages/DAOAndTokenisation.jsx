import React, { useState, useEffect } from 'react';
import {
  BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer,
  PieChart, Pie, Cell
} from 'recharts';
import { 
  FaCoins, FaVoteYea, FaPiggyBank, FaExternalLinkAlt, 
  FaEthereum, FaChartLine, FaUsers, FaLock 
} from 'react-icons/fa';

const DAOAndTokenisation = () => {
  const [daoData, setDaoData] = useState(null);
  const [loading, setLoading] = useState(true);

  // Données de démonstration
  const mockData = {
    token: {
      contract_address: "0xABC123456789DEF0",
      token_symbol: "STK123",
      valuation: "5,000,000 €",
      price_per_token: "5.00 €",
      total_supply: 1000000,
      distribution: {
        founder: 200000,
        team: 100000,
        investors: 700000
      }
    },
    dao: {
      dao_address: "0xDAO456789ABC123",
      rules: [
        "1 token = 1 vote",
        "Budget voté tous les mois",
        "Quorum minimum: 10% des tokens",
        "Délai de vote: 7 jours",
        "Décisions stratégiques: 2/3 majorité"
      ],
      voting_power: "1 token = 1 vote",
      quorum: "10% des tokens",
      voting_period: "7 jours"
    },
    treasury: {
      treasury_address: "0xTREAS789ABC456",
      funds: "2,500,000 €",
      rules: [
        "Dividendes tous les trimestres",
        "Votes sur allocation des fonds",
        "Limite de retrait: 5% par mois",
        "Audit trimestriel obligatoire",
        "Multi-signature pour gros montants"
      ],
      distribution_schedule: "Trimestriel",
      withdrawal_limit: "5% par mois"
    }
  };

  useEffect(() => {
    // Simulation du chargement des données
    setTimeout(() => {
      setDaoData(mockData);
      setLoading(false);
    }, 1500);
  }, []);

  // Données pour les graphiques
  const tokenDistributionData = [
    { name: 'Fondateur', value: mockData.token.distribution.founder, color: '#6366f1' },
    { name: 'Équipe IA', value: mockData.token.distribution.team, color: '#8b5cf6' },
    { name: 'Investisseurs', value: mockData.token.distribution.investors, color: '#06b6d4' }
  ];

  const treasuryAllocationData = [
    { name: 'Développement', value: 40, color: '#10b981' },
    { name: 'Marketing', value: 25, color: '#f59e0b' },
    { name: 'Infrastructure', value: 20, color: '#ef4444' },
    { name: 'Réserves', value: 15, color: '#8b5cf6' }
  ];

  if (loading) {
    return (
      <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 flex items-center justify-center">
        <div className="text-center">
          <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-purple-500 mx-auto"></div>
          <p className="text-white text-xl mt-4">Chargement de la DAO...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 text-white">
      {/* Header */}
      <div className="container mx-auto px-6 py-8">
        <div className="text-center mb-12">
          <h1 className="text-5xl font-bold bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent mb-4">
            🏛️ DAO & Tokenisation
          </h1>
          <p className="text-xl text-gray-300">
            Gouvernance décentralisée et tokenisation de votre startup
          </p>
        </div>

        {/* Section Token */}
        <div className="mb-12">
          <div className="bg-gradient-to-r from-blue-900/50 to-purple-900/50 rounded-2xl p-8 border border-purple-500/30">
            <div className="flex items-center mb-6">
              <FaCoins className="text-4xl text-yellow-400 mr-4" />
              <h2 className="text-3xl font-bold text-yellow-400">🪙 Token ERC20</h2>
            </div>
            
            <div className="grid md:grid-cols-2 gap-8">
              <div className="space-y-4">
                <div className="bg-black/30 rounded-lg p-4">
                  <p className="text-gray-400 text-sm">Symbole</p>
                  <p className="text-2xl font-bold text-white">{daoData.token.token_symbol}</p>
                </div>
                <div className="bg-black/30 rounded-lg p-4">
                  <p className="text-gray-400 text-sm">Valorisation</p>
                  <p className="text-2xl font-bold text-green-400">{daoData.token.valuation}</p>
                </div>
                <div className="bg-black/30 rounded-lg p-4">
                  <p className="text-gray-400 text-sm">Prix par token</p>
                  <p className="text-2xl font-bold text-blue-400">{daoData.token.price_per_token}</p>
                </div>
                <a
                  href={`https://etherscan.io/token/${daoData.token.token_address}`}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full bg-gradient-to-r from-blue-600 to-purple-600 hover:from-blue-700 hover:to-purple-700 text-white font-bold py-3 px-6 rounded-lg transition-all duration-300 flex items-center justify-center"
                >
                  <FaExternalLinkAlt className="mr-2" />
                  Voir sur Etherscan
                </a>
              </div>
              
              <div className="bg-black/30 rounded-lg p-6">
                <h3 className="text-xl font-bold mb-4 text-center">Distribution des Tokens</h3>
                <ResponsiveContainer width="100%" height={200}>
                  <PieChart>
                    <Pie
                      data={tokenDistributionData}
                      cx="50%"
                      cy="50%"
                      innerRadius={40}
                      outerRadius={80}
                      paddingAngle={5}
                      dataKey="value"
                    >
                      {tokenDistributionData.map((entry, index) => (
                        <Cell key={`cell-${index}`} fill={entry.color} />
                      ))}
                    </Pie>
                    <Tooltip />
                  </PieChart>
                </ResponsiveContainer>
                <div className="mt-4 space-y-2">
                  {tokenDistributionData.map((item, index) => (
                    <div key={index} className="flex items-center justify-between">
                      <span className="text-sm">{item.name}</span>
                      <span className="font-bold">{item.value.toLocaleString()}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Section DAO */}
        <div className="mb-12">
          <div className="bg-gradient-to-r from-purple-900/50 to-pink-900/50 rounded-2xl p-8 border border-pink-500/30">
            <div className="flex items-center mb-6">
              <FaVoteYea className="text-4xl text-pink-400 mr-4" />
              <h2 className="text-3xl font-bold text-pink-400">🏛️ Gouvernance DAO</h2>
            </div>
            
            <div className="grid md:grid-cols-2 gap-8">
              <div className="space-y-4">
                <div className="bg-black/30 rounded-lg p-4">
                  <p className="text-gray-400 text-sm">Adresse DAO</p>
                  <p className="text-lg font-mono text-white break-all">{daoData.dao.dao_address}</p>
                </div>
                <div className="bg-black/30 rounded-lg p-4">
                  <p className="text-gray-400 text-sm">Pouvoir de vote</p>
                  <p className="text-xl font-bold text-green-400">{daoData.dao.voting_power}</p>
                </div>
                <div className="bg-black/30 rounded-lg p-4">
                  <p className="text-gray-400 text-sm">Quorum</p>
                  <p className="text-xl font-bold text-blue-400">{daoData.dao.quorum}</p>
                </div>
                <a
                  href={daoData.dao.dao_address}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="w-full bg-gradient-to-r from-pink-600 to-purple-600 hover:from-pink-700 hover:to-purple-700 text-white font-bold py-3 px-6 rounded-lg transition-all duration-300 flex items-center justify-center"
                >
                  <FaExternalLinkAlt className="mr-2" />
                  Accéder à la DAO
                </a>
              </div>
              
              <div className="bg-black/30 rounded-lg p-6">
                <h3 className="text-xl font-bold mb-4 text-center">Règles de Gouvernance</h3>
                <div className="space-y-3">
                  {daoData.dao.rules.map((rule, index) => (
                    <div key={index} className="flex items-start">
                      <div className="w-2 h-2 bg-pink-400 rounded-full mt-2 mr-3 flex-shrink-0"></div>
                      <p className="text-sm text-gray-300">{rule}</p>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Section Trésorerie */}
        <div className="mb-12">
          <div className="bg-gradient-to-r from-green-900/50 to-blue-900/50 rounded-2xl p-8 border border-green-500/30">
            <div className="flex items-center mb-6">
              <FaPiggyBank className="text-4xl text-green-400 mr-4" />
              <h2 className="text-3xl font-bold text-green-400">💰 Trésorerie DAO</h2>
            </div>
            
            <div className="grid md:grid-cols-2 gap-8">
              <div className="space-y-4">
                <div className="bg-black/30 rounded-lg p-4">
                  <p className="text-gray-400 text-sm">Adresse Trésorerie</p>
                  <p className="text-lg font-mono text-white break-all">{daoData.treasury.treasury_address}</p>
                </div>
                <div className="bg-black/30 rounded-lg p-4">
                  <p className="text-gray-400 text-sm">Fonds Disponibles</p>
                  <p className="text-3xl font-bold text-green-400">{daoData.treasury.funds}</p>
                </div>
                <div className="bg-black/30 rounded-lg p-4">
                  <p className="text-gray-400 text-sm">Distribution</p>
                  <p className="text-xl font-bold text-blue-400">{daoData.treasury.distribution_schedule}</p>
                </div>
                <button className="w-full bg-gradient-to-r from-green-600 to-blue-600 hover:from-green-700 hover:to-blue-700 text-white font-bold py-3 px-6 rounded-lg transition-all duration-300 flex items-center justify-center">
                  <FaChartLine className="mr-2" />
                  Gérer la Trésorerie
                </button>
              </div>
              
              <div className="bg-black/30 rounded-lg p-6">
                <h3 className="text-xl font-bold mb-4 text-center">Allocation des Fonds</h3>
                <ResponsiveContainer width="100%" height={200}>
                  <BarChart data={treasuryAllocationData}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
                    <XAxis dataKey="name" stroke="#9ca3af" />
                    <YAxis stroke="#9ca3af" />
                    <Tooltip 
                      contentStyle={{ 
                        backgroundColor: '#1f2937', 
                        border: '1px solid #374151',
                        borderRadius: '8px'
                      }}
                    />
                    <Bar dataKey="value" fill="#10b981" radius={[4, 4, 0, 0]} />
                  </BarChart>
                </ResponsiveContainer>
                <div className="mt-4 space-y-2">
                  {treasuryAllocationData.map((item, index) => (
                    <div key={index} className="flex items-center justify-between">
                      <span className="text-sm">{item.name}</span>
                      <span className="font-bold">{item.value}%</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Section Statistiques */}
        <div className="bg-gradient-to-r from-indigo-900/50 to-purple-900/50 rounded-2xl p-8 border border-indigo-500/30">
          <h2 className="text-3xl font-bold text-center mb-8 text-indigo-400">📊 Statistiques Globales</h2>
          
          <div className="grid md:grid-cols-4 gap-6">
            <div className="text-center">
              <div className="bg-black/30 rounded-lg p-6">
                <FaUsers className="text-3xl text-blue-400 mx-auto mb-3" />
                <p className="text-2xl font-bold text-white">1,000,000</p>
                <p className="text-gray-400">Tokens Totaux</p>
              </div>
            </div>
            
            <div className="text-center">
              <div className="bg-black/30 rounded-lg p-6">
                <FaVoteYea className="text-3xl text-green-400 mx-auto mb-3" />
                <p className="text-2xl font-bold text-white">5</p>
                <p className="text-gray-400">Règles Actives</p>
              </div>
            </div>
            
            <div className="text-center">
              <div className="bg-black/30 rounded-lg p-6">
                <FaPiggyBank className="text-3xl text-yellow-400 mx-auto mb-3" />
                <p className="text-2xl font-bold text-white">2.5M €</p>
                <p className="text-gray-400">Fonds Gérés</p>
              </div>
            </div>
            
            <div className="text-center">
              <div className="bg-black/30 rounded-lg p-6">
                <FaLock className="text-3xl text-purple-400 mx-auto mb-3" />
                <p className="text-2xl font-bold text-white">3</p>
                <p className="text-gray-400">Contrats Sécurisés</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DAOAndTokenisation;