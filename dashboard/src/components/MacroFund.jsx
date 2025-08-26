import React, { useState, useEffect } from 'react';
import { 
  PieChart, 
  Pie, 
  Cell, 
  LineChart, 
  Line, 
  XAxis, 
  YAxis, 
  CartesianGrid, 
  Tooltip, 
  Legend,
  ResponsiveContainer,
  BarChart,
  Bar
} from 'recharts';

const MacroFund = () => {
  const [portfolioData, setPortfolioData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Couleurs pour les graphiques
  const colors = {
    'IA Startups': '#3B82F6',    // Bleu
    'ETF IA': '#1E40AF',         // Bleu foncé
    'Crypto': '#F59E0B',         // Orange
    'Stocks': '#10B981',         // Vert
    'Commodities': '#FCD34D',    // Jaune
    'Cash': '#6B7280'            // Gris
  };

  // Données de performance simulées (30 jours)
  const performanceData = Array.from({ length: 30 }, (_, i) => ({
    date: new Date(Date.now() - (29 - i) * 24 * 60 * 60 * 1000).toLocaleDateString(),
    nav: 50000000 + Math.random() * 5000000,
    performance: (Math.random() - 0.5) * 0.1
  }));

  useEffect(() => {
    fetchMacroFundData();
  }, []);

  const fetchMacroFundData = async () => {
    try {
      setLoading(true);
      const response = await fetch('http://localhost:8000/macrofund');
      if (!response.ok) {
        throw new Error('Failed to fetch macro fund data');
      }
      const data = await response.json();
      setPortfolioData(data);
    } catch (err) {
      setError(err.message);
      // Utiliser des données simulées en cas d'erreur
      setPortfolioData({
        portfolio_value: "50,000,000 €",
        allocations: {
          "IA Startups": 0.40,
          "ETF IA": 0.20,
          "Crypto": 0.25,
          "Stocks": 0.10,
          "Commodities": 0.05
        },
        hedges: {
          "Short Nasdaq ETF": {"active": true, "size": 0.05},
          "Long Gold": {"active": true, "size": 0.03}
        },
        recent_arbitrages: [
          {
            timestamp: "2024-01-15T10:30:00",
            action: "SELL",
            asset: "ETF IA",
            amount: "2,500,000 €",
            reason: "Macro rebalancing - decrease allocation from 20%"
          },
          {
            timestamp: "2024-01-15T10:25:00",
            action: "BUY",
            asset: "Crypto",
            amount: "4,000,000 €",
            reason: "Macro rebalancing - increase allocation to 25%"
          }
        ],
        performance_ytd: 0.18,
        sharpe_ratio: 1.25,
        max_drawdown: -0.08
      });
    } finally {
      setLoading(false);
    }
  };

  const executeMacroFund = async () => {
    try {
      const response = await fetch('http://localhost:8000/macrofund/execute', {
        method: 'POST'
      });
      if (response.ok) {
        await fetchMacroFundData(); // Rafraîchir les données
      }
    } catch (err) {
      console.error('Error executing macro fund:', err);
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-96">
        <div className="animate-spin rounded-full h-32 w-32 border-b-2 border-blue-500"></div>
      </div>
    );
  }

  if (error && !portfolioData) {
    return (
      <div className="text-center py-8">
        <div className="text-red-500 text-xl mb-4">Error: {error}</div>
        <button 
          onClick={fetchMacroFundData}
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
        >
          Retry
        </button>
      </div>
    );
  }

  // Préparer les données pour le pie chart
  const pieData = Object.entries(portfolioData.allocations).map(([name, value]) => ({
    name,
    value: value * 100
  }));

  return (
    <div className="min-h-screen bg-gray-900 text-white p-6">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-4xl font-bold text-white mb-2">Macro Fund</h1>
        <p className="text-gray-300 text-lg">Portfolio multi-actifs global avec arbitrages intelligents</p>
        
        <div className="mt-4 flex gap-4">
          <button
            onClick={executeMacroFund}
            className="bg-gradient-to-r from-blue-500 to-purple-600 hover:from-blue-600 hover:to-purple-700 text-white font-bold py-3 px-6 rounded-lg transition-all duration-200 transform hover:scale-105"
          >
            🚀 Exécuter Macro Fund
          </button>
          <button
            onClick={fetchMacroFundData}
            className="bg-gray-700 hover:bg-gray-600 text-white font-bold py-3 px-6 rounded-lg transition-all duration-200"
          >
            🔄 Actualiser
          </button>
        </div>
      </div>

      {/* Section Allocation */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
        {/* Pie Chart Allocations */}
        <div className="bg-gray-800 rounded-xl p-6 shadow-xl">
          <h2 className="text-2xl font-bold mb-6 text-center">Allocation du Portefeuille</h2>
          <div className="h-80">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={pieData}
                  cx="50%"
                  cy="50%"
                  labelLine={false}
                  label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                  outerRadius={120}
                  fill="#8884d8"
                  dataKey="value"
                >
                  {pieData.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={colors[entry.name] || '#6B7280'} />
                  ))}
                </Pie>
                <Tooltip formatter={(value) => [`${value.toFixed(1)}%`, 'Allocation']} />
              </PieChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Carte Valeur Totale */}
        <div className="bg-gradient-to-br from-blue-600 to-purple-700 rounded-xl p-6 shadow-xl">
          <h2 className="text-2xl font-bold mb-6 text-center">Valeur Totale (NAV)</h2>
          <div className="text-center">
            <div className="text-5xl font-bold mb-4">{portfolioData.portfolio_value}</div>
            <div className="text-xl text-blue-100 mb-4">
              Performance YTD: <span className="text-green-400">+{(portfolioData.performance_ytd * 100).toFixed(1)}%</span>
            </div>
            <div className="grid grid-cols-2 gap-4 text-sm">
              <div>
                <div className="text-gray-200">Sharpe Ratio</div>
                <div className="text-xl font-semibold">{portfolioData.sharpe_ratio.toFixed(2)}</div>
              </div>
              <div>
                <div className="text-gray-200">Max Drawdown</div>
                <div className="text-xl font-semibold text-red-400">{(portfolioData.max_drawdown * 100).toFixed(1)}%</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Section Arbitrages */}
      <div className="bg-gray-800 rounded-xl p-6 shadow-xl mb-8">
        <h2 className="text-2xl font-bold mb-6">Derniers Arbitrages</h2>
        <div className="space-y-4">
          {portfolioData.recent_arbitrages.map((arbitrage, index) => (
            <div 
              key={index}
              className={`p-4 rounded-lg border-l-4 ${
                arbitrage.action === 'BUY' 
                  ? 'border-green-500 bg-green-900/20' 
                  : 'border-red-500 bg-red-900/20'
              }`}
            >
              <div className="flex items-center justify-between">
                <div className="flex items-center gap-3">
                  <span className={`text-2xl ${
                    arbitrage.action === 'BUY' ? 'text-green-400' : 'text-red-400'
                  }`}>
                    {arbitrage.action === 'BUY' ? '📈' : '📉'}
                  </span>
                  <div>
                    <div className="font-semibold text-lg">
                      {arbitrage.action} {arbitrage.asset}
                    </div>
                    <div className="text-gray-300 text-sm">{arbitrage.reason}</div>
                  </div>
                </div>
                <div className="text-right">
                  <div className="text-xl font-bold">{arbitrage.amount}</div>
                  <div className="text-gray-400 text-sm">
                    {new Date(arbitrage.timestamp).toLocaleString()}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Section Hedging */}
      <div className="bg-gray-800 rounded-xl p-6 shadow-xl mb-8">
        <h2 className="text-2xl font-bold mb-6">Positions de Hedge</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {Object.entries(portfolioData.hedges).map(([hedge, data]) => (
            <div 
              key={hedge}
              className={`p-4 rounded-lg border-2 ${
                data.active 
                  ? 'border-green-500 bg-green-900/20' 
                  : 'border-gray-500 bg-gray-700/20'
              }`}
            >
              <div className="flex items-center justify-between mb-3">
                <h3 className="text-lg font-semibold">{hedge}</h3>
                <span className={`px-3 py-1 rounded-full text-xs font-bold ${
                  data.active 
                    ? 'bg-green-500 text-white' 
                    : 'bg-gray-500 text-gray-200'
                }`}>
                  {data.active ? 'ACTIF' : 'INACTIF'}
                </span>
              </div>
              <div className="text-2xl font-bold text-center">
                {(data.size * 100).toFixed(1)}%
              </div>
              <div className="text-gray-400 text-sm text-center">
                Taille de la position
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Section Performance */}
      <div className="bg-gray-800 rounded-xl p-6 shadow-xl">
        <h2 className="text-2xl font-bold mb-6">Performance NAV (30 jours)</h2>
        <div className="h-80">
          <ResponsiveContainer width="100%" height="100%">
            <LineChart data={performanceData}>
              <CartesianGrid strokeDasharray="3 3" stroke="#374151" />
              <XAxis 
                dataKey="date" 
                stroke="#9CA3AF"
                tick={{ fontSize: 12 }}
                interval="preserveStartEnd"
              />
              <YAxis 
                stroke="#9CA3AF"
                tick={{ fontSize: 12 }}
                tickFormatter={(value) => `${(value / 1000000).toFixed(0)}M`}
              />
              <Tooltip 
                formatter={(value) => [`${(value / 1000000).toFixed(2)}M €`, 'NAV']}
                labelStyle={{ color: '#111827' }}
                contentStyle={{ 
                  backgroundColor: '#1F2937', 
                  border: '1px solid #374151',
                  borderRadius: '8px'
                }}
              />
              <Legend />
              <Line 
                type="monotone" 
                dataKey="nav" 
                stroke="#3B82F6" 
                strokeWidth={3}
                dot={{ fill: '#3B82F6', strokeWidth: 2, r: 4 }}
                activeDot={{ r: 6, stroke: '#3B82F6', strokeWidth: 2 }}
              />
            </LineChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
};

export default MacroFund;