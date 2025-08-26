import React, { useState, useEffect } from "react";
import { 
  LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer,
  BarChart, Bar, PieChart, Pie, Cell
} from "recharts";
import { 
  FaChartLine, FaCoins, FaTrendingUp, FaTrendingDown, 
  FaEye, FaShoppingCart, FaDollarSign, FaChartBar,
  FaGlobe, FaIndustry, FaRocket, FaSeedling
} from "react-icons/fa";
import { API_CONFIG, CHART_CONFIG, MARKET_CONFIG } from "../config";

const GlobalMarket = () => {
  const [marketData, setMarketData] = useState(null);
  const [selectedToken, setSelectedToken] = useState(null);
  const [loading, setLoading] = useState(true);
  const [timeframe, setTimeframe] = useState(7);

  // Couleurs pour les graphiques
  const COLORS = CHART_CONFIG.COLORS;

  useEffect(() => {
    fetchMarketData();
  }, []);

  const fetchMarketData = async () => {
    try {
      setLoading(true);
      const response = await fetch(`${API_CONFIG.MARKETPLACE_API}${API_CONFIG.ENDPOINTS.MARKET}`);
      const data = await response.json();
      
      if (data.success) {
        setMarketData(data.data);
        // Sélectionner le premier token par défaut
        if (data.data.listed_tokens.length > 0) {
          setSelectedToken(data.data.listed_tokens[0]);
        }
      }
    } catch (error) {
      console.error('Erreur lors de la récupération des données:', error);
    } finally {
      setLoading(false);
    }
  };

  const getChangeColor = (change) => {
    return change >= 0 ? 'text-green-500' : 'text-red-500';
  };

  const getChangeIcon = (change) => {
    return change >= 0 ? <FaTrendingUp className="inline" /> : <FaTrendingDown className="inline" />;
  };

  const getSectorIcon = (sector) => {
    const icons = {
      'SaaS': <FaGlobe />,
      'CleanTech': <FaIndustry />,
      'HealthTech': <FaRocket />,
      'FinTech': <FaDollarSign />,
      'Artificial Intelligence': <FaChartBar />
    };
    return icons[sector] || <FaCoins />;
  };

  const getStageColor = (stage) => {
    const colors = {
      'Seed': 'bg-yellow-100 text-yellow-800',
      'Series A': 'bg-blue-100 text-blue-800',
      'Series B': 'bg-green-100 text-green-800'
    };
    return colors[stage] || 'bg-gray-100 text-gray-800';
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (!marketData) {
    return (
      <div className="text-center text-gray-500">
        Erreur lors du chargement des données du marché
      </div>
    );
  }

  return (
    <div className="space-y-6">
      {/* Header du marché */}
      <div className="bg-gradient-to-r from-blue-900 to-purple-900 rounded-2xl p-6 text-white">
        <div className="flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold mb-2">🌐 Global Market</h1>
            <p className="text-blue-200">Startup Tokenization Exchange</p>
          </div>
          <div className="text-right">
            <div className="text-2xl font-bold">
              {marketData.market_stats.total_listed} Tokens
            </div>
            <div className="text-blue-200">
              {marketData.market_stats.total_market_cap.toLocaleString()} € Market Cap
            </div>
          </div>
        </div>
      </div>

      {/* Statistiques globales */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-white rounded-xl p-4 shadow-sm border">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600">Total Volume 24h</p>
              <p className="text-xl font-bold">{marketData.market_stats.total_volume_24h.toLocaleString()} €</p>
            </div>
            <FaChartLine className="text-blue-600 text-2xl" />
          </div>
        </div>
        
        <div className="bg-white rounded-xl p-4 shadow-sm border">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600">Sentiment</p>
              <p className="text-xl font-bold">{marketData.market_stats.market_sentiment}</p>
            </div>
            <FaTrendingUp className="text-green-600 text-2xl" />
          </div>
        </div>
        
        <div className="bg-white rounded-xl p-4 shadow-sm border">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600">Market Address</p>
              <p className="text-sm font-mono text-gray-800 truncate">{marketData.market_address}</p>
            </div>
            <FaCoins className="text-purple-600 text-2xl" />
          </div>
        </div>
        
        <div className="bg-white rounded-xl p-4 shadow-sm border">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600">Dernière MAJ</p>
              <p className="text-sm font-mono text-gray-800">
                {new Date(marketData.market_stats.last_updated).toLocaleTimeString()}
              </p>
            </div>
            <FaChartBar className="text-orange-600 text-2xl" />
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Tableau principal des tokens */}
        <div className="lg:col-span-2">
          <div className="bg-white rounded-2xl shadow-sm border overflow-hidden">
            <div className="p-6 border-b">
              <h2 className="text-xl font-bold text-gray-800">📊 Marché des Startups</h2>
              <p className="text-gray-600">Tokens listés sur l'exchange</p>
            </div>
            
            <div className="overflow-x-auto">
              <table className="w-full">
                <thead className="bg-gray-50">
                  <tr>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Token
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Prix
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      24h %
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Volume
                    </th>
                    <th className="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
                      Actions
                    </th>
                  </tr>
                </thead>
                <tbody className="bg-white divide-y divide-gray-200">
                  {marketData.listed_tokens.map((token, index) => (
                    <tr 
                      key={token.symbol}
                      className={`hover:bg-gray-50 cursor-pointer transition-colors ${
                        selectedToken?.symbol === token.symbol ? 'bg-blue-50' : ''
                      }`}
                      onClick={() => setSelectedToken(token)}
                    >
                      <td className="px-6 py-4 whitespace-nowrap">
                        <div className="flex items-center">
                          <div className="flex-shrink-0 h-10 w-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center text-white font-bold">
                            {token.symbol.slice(0, 2)}
                          </div>
                          <div className="ml-4">
                            <div className="text-sm font-medium text-gray-900">{token.symbol}</div>
                            <div className="text-sm text-gray-500">{token.name}</div>
                            <div className="flex items-center gap-2 mt-1">
                              {getSectorIcon(token.sector)}
                              <span className="text-xs text-gray-500">{token.sector}</span>
                              <span className={`px-2 py-1 text-xs rounded-full ${getStageColor(token.stage)}`}>
                                {token.stage}
                              </span>
                            </div>
                          </div>
                        </div>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <div className="text-sm font-medium text-gray-900">{token.price_eur}</div>
                        <div className="text-sm text-gray-500">€{token.price}</div>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <span className={`text-sm font-medium ${getChangeColor(token.change_24h)}`}>
                          {getChangeIcon(token.change_24h)} {token.change_24h}%
                        </span>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <div className="text-sm text-gray-900">{token.volume_formatted}</div>
                        <div className="text-sm text-gray-500">€</div>
                      </td>
                      <td className="px-6 py-4 whitespace-nowrap">
                        <div className="flex gap-2">
                          <button className="px-3 py-1 bg-green-600 text-white text-xs rounded-lg hover:bg-green-700 transition">
                            Acheter
                          </button>
                          <button className="px-3 py-1 bg-red-600 text-white text-xs rounded-lg hover:bg-red-700 transition">
                            Vendre
                          </button>
                        </div>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </div>
        </div>

        {/* Détails du token sélectionné */}
        <div className="lg:col-span-1">
          {selectedToken ? (
            <div className="bg-white rounded-2xl shadow-sm border p-6">
              <div className="flex items-center gap-3 mb-4">
                <div className="h-12 w-12 bg-gradient-to-br from-blue-500 to-purple-600 rounded-lg flex items-center justify-center text-white font-bold text-lg">
                  {selectedToken.symbol.slice(0, 2)}
                </div>
                <div>
                  <h3 className="text-lg font-bold text-gray-900">{selectedToken.symbol}</h3>
                  <p className="text-sm text-gray-600">{selectedToken.name}</p>
                </div>
              </div>

              <div className="space-y-4">
                <div className="border-b pb-4">
                  <div className="flex justify-between items-center mb-2">
                    <span className="text-sm text-gray-600">Prix actuel</span>
                    <span className="text-lg font-bold text-gray-900">{selectedToken.price_eur}</span>
                  </div>
                  <div className="flex justify-between items-center">
                    <span className="text-sm text-gray-600">Variation 24h</span>
                    <span className={`text-sm font-medium ${getChangeColor(selectedToken.change_24h)}`}>
                      {getChangeIcon(selectedToken.change_24h)} {selectedToken.change_24h}%
                    </span>
                  </div>
                </div>

                <div className="space-y-3">
                  <div className="flex justify-between">
                    <span className="text-sm text-gray-600">Volume 24h</span>
                    <span className="text-sm font-medium">{selectedToken.volume_formatted} €</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-sm text-gray-600">Market Cap</span>
                    <span className="text-sm font-medium">{selectedToken.market_cap.toLocaleString()} €</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-sm text-gray-600">Secteur</span>
                    <span className="text-sm font-medium">{selectedToken.sector}</span>
                  </div>
                  <div className="flex justify-between">
                    <span className="text-sm text-gray-600">Stage</span>
                    <span className={`px-2 py-1 text-xs rounded-full ${getStageColor(selectedToken.stage)}`}>
                      {selectedToken.stage}
                    </span>
                  </div>
                </div>

                <div className="pt-4 border-t">
                  <h4 className="text-sm font-medium text-gray-900 mb-3">Actions rapides</h4>
                  <div className="grid grid-cols-2 gap-2">
                    <button className="w-full py-2 bg-green-600 text-white text-sm rounded-lg hover:bg-green-700 transition">
                      Acheter {selectedToken.symbol}
                    </button>
                    <button className="w-full py-2 bg-red-600 text-white text-sm rounded-lg hover:bg-red-700 transition">
                      Vendre {selectedToken.symbol}
                    </button>
                  </div>
                </div>
              </div>
            </div>
          ) : (
            <div className="bg-white rounded-2xl shadow-sm border p-6 text-center text-gray-500">
              Sélectionnez un token pour voir les détails
            </div>
          )}
        </div>
      </div>

      {/* Graphiques */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Graphique des prix */}
        <div className="bg-white rounded-2xl shadow-sm border p-6">
          <div className="flex items-center justify-between mb-4">
            <h3 className="text-lg font-bold text-gray-800">📈 Évolution des Prix</h3>
            <div className="flex gap-2">
              {[7, 30].map((days) => (
                <button
                  key={days}
                  onClick={() => setTimeframe(days)}
                  className={`px-3 py-1 text-sm rounded-lg transition ${
                    timeframe === days
                      ? 'bg-blue-600 text-white'
                      : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                  }`}
                >
                  {days}j
                </button>
              ))}
            </div>
          </div>
          
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <LineChart data={marketData.listed_tokens.slice(0, 5).map((token, index) => ({
                name: token.symbol,
                prix: token.price,
                volume: token.volume / 1000
              }))}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Line type="monotone" dataKey="prix" stroke="#3B82F6" strokeWidth={2} />
              </LineChart>
            </ResponsiveContainer>
          </div>
        </div>

        {/* Graphique des volumes */}
        <div className="bg-white rounded-2xl shadow-sm border p-6">
          <h3 className="text-lg font-bold text-gray-800 mb-4">📊 Volume par Startup</h3>
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <BarChart data={marketData.listed_tokens.map(token => ({
                name: token.symbol,
                volume: token.volume / 1000
              }))}>
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Bar dataKey="volume" fill="#10B981" />
              </BarChart>
            </ResponsiveContainer>
          </div>
        </div>
      </div>

      {/* Répartition du portefeuille */}
      <div className="bg-white rounded-2xl shadow-sm border p-6">
        <h3 className="text-lg font-bold text-gray-800 mb-4">🥧 Répartition du Portefeuille</h3>
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 items-center">
          <div className="h-64">
            <ResponsiveContainer width="100%" height="100%">
              <PieChart>
                <Pie
                  data={marketData.listed_tokens.map((token, index) => ({
                    name: token.symbol,
                    value: token.market_cap,
                    color: COLORS[index % COLORS.length]
                  }))}
                  cx="50%"
                  cy="50%"
                  outerRadius={80}
                  fill="#8884d8"
                  dataKey="value"
                  label={({ name, percent }) => `${name} ${(percent * 100).toFixed(0)}%`}
                >
                  {marketData.listed_tokens.map((entry, index) => (
                    <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                  ))}
                </Pie>
                <Tooltip />
              </PieChart>
            </ResponsiveContainer>
          </div>
          
          <div className="space-y-3">
            {marketData.listed_tokens.map((token, index) => (
              <div key={token.symbol} className="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
                <div className="flex items-center gap-3">
                  <div 
                    className="w-4 h-4 rounded-full"
                    style={{ backgroundColor: COLORS[index % COLORS.length] }}
                  ></div>
                  <span className="font-medium">{token.symbol}</span>
                </div>
                <span className="text-sm text-gray-600">
                  {(token.market_cap / marketData.market_stats.total_market_cap * 100).toFixed(1)}%
                </span>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default GlobalMarket;