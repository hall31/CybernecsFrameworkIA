import React, { useState, useEffect } from "react";
import { FaChartLine, FaChartPie, FaSync, FaArrowUp, FaArrowDown, FaDollarSign } from "react-icons/fa";

const HedgeFund = () => {
  const [portfolioData, setPortfolioData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [tickerPrices, setTickerPrices] = useState({});

  // Simulation des prix en temps réel
  useEffect(() => {
    const interval = setInterval(() => {
      const newPrices = {};
      const tokens = ["STK001", "STK002", "STK003", "STK004", "STK005", "ETF001", "ETF002", "ETF003"];
      
      tokens.forEach(token => {
        const basePrice = portfolioData?.portfolio?.available_tokens?.[token]?.current_price || 100;
        const change = (Math.random() - 0.5) * 0.02; // ±1% change
        newPrices[token] = {
          price: (basePrice * (1 + change)).toFixed(2),
          change: change > 0 ? "up" : "down"
        };
      });
      
      setTickerPrices(newPrices);
    }, 2000);

    return () => clearInterval(interval);
  }, [portfolioData]);

  useEffect(() => {
    fetchPortfolioData();
  }, []);

  const fetchPortfolioData = async () => {
    try {
      setLoading(true);
      const response = await fetch("http://localhost:8000/hedgefund");
      if (!response.ok) throw new Error("Failed to fetch data");
      
      const data = await response.json();
      setPortfolioData(data);
      setError(null);
    } catch (err) {
      setError(err.message);
      // Données de démonstration en cas d'erreur
      setPortfolioData(getDemoData());
    } finally {
      setLoading(false);
    }
  };

  const handleRebalance = async () => {
    try {
      const response = await fetch("http://localhost:8000/hedgefund/rebalance", {
        method: "POST"
      });
      if (response.ok) {
        fetchPortfolioData(); // Rafraîchir les données
      }
    } catch (err) {
      console.error("Rebalance failed:", err);
    }
  };

  const getDemoData = () => ({
    portfolio: {
      long_positions: [
        { token: "STK001", allocation: "25.0%", amount_usd: 250000, confidence: 0.8 },
        { token: "ETF002", allocation: "20.0%", amount_usd: 200000, confidence: 0.7 }
      ],
      short_positions: [
        { token: "STK005", allocation: "15.0%", amount_usd: 150000, confidence: 0.6 }
      ],
      cash_reserve: "40.0%",
      total_value: 1000000
    },
    performance: {
      roi: 12.5,
      volatility: 18.2,
      sharpe_ratio: 1.8,
      total_return: 125000,
      current_value: 1125000
    },
    strategy_commentary: "Nous renforçons notre position long sur les startups technologiques avec une approche momentum agressive."
  });

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (error && !portfolioData) {
    return (
      <div className="text-center text-red-600">
        <p>Erreur: {error}</p>
        <p>Utilisation des données de démonstration</p>
      </div>
    );
  }

  const { portfolio, performance, strategy_commentary } = portfolioData;

  return (
    <div className="space-y-6">
      {/* Header avec ticker */}
      <div className="bg-gray-900 text-white p-4 rounded-lg">
        <div className="flex items-center justify-between mb-4">
          <h1 className="text-2xl font-bold font-mono">💰 Hedge Fund IA</h1>
          <div className="text-sm text-gray-300">
            Dernière mise à jour: {new Date().toLocaleTimeString()}
          </div>
        </div>
        
        {/* Ticker des prix */}
        <div className="flex space-x-6 overflow-x-auto">
          {Object.entries(tickerPrices).map(([token, data]) => (
            <div key={token} className="flex items-center space-x-2 min-w-max">
              <span className="font-mono text-sm">{token}</span>
              <span className="font-mono font-bold">${data.price}</span>
              <span className={`text-xs ${data.change === 'up' ? 'text-green-400' : 'text-red-400'}`}>
                {data.change === 'up' ? <FaArrowUp /> : <FaArrowDown />}
              </span>
            </div>
          ))}
        </div>
      </div>

      {/* Section Performance */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-white p-4 rounded-lg shadow-md border-l-4 border-green-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600">Valeur Totale</p>
              <p className="text-2xl font-bold font-mono text-green-600">
                ${portfolio.total_value?.toLocaleString() || '1,000,000'}
              </p>
            </div>
            <FaDollarSign className="text-3xl text-green-500" />
          </div>
        </div>

        <div className="bg-white p-4 rounded-lg shadow-md border-l-4 border-blue-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600">ROI</p>
              <p className={`text-2xl font-bold font-mono ${performance.roi >= 0 ? 'text-green-600' : 'text-red-600'}`}>
                {performance.roi >= 0 ? '+' : ''}{performance.roi}%
              </p>
            </div>
            <FaChartLine className="text-3xl text-blue-500" />
          </div>
        </div>

        <div className="bg-white p-4 rounded-lg shadow-md border-l-4 border-purple-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600">Volatilité</p>
              <p className="text-2xl font-bold font-mono text-purple-600">
                {performance.volatility}%
              </p>
            </div>
            <FaChartPie className="text-3xl text-purple-500" />
          </div>
        </div>

        <div className="bg-white p-4 rounded-lg shadow-md border-l-4 border-orange-500">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm text-gray-600">Sharpe Ratio</p>
              <p className={`text-2xl font-bold font-mono ${performance.sharpe_ratio >= 1 ? 'text-green-600' : 'text-orange-600'}`}>
                {performance.sharpe_ratio}
              </p>
            </div>
            <div className="text-3xl text-orange-500">📊</div>
          </div>
        </div>
      </div>

      {/* Section Portefeuille */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Positions Long */}
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4 text-green-700 flex items-center">
            <FaArrowUp className="mr-2" />
            Positions Long
          </h3>
          <div className="space-y-3">
            {portfolio.long_positions?.map((position, idx) => (
              <div key={idx} className="flex items-center justify-between p-3 bg-green-50 rounded-lg">
                <div>
                  <p className="font-semibold">{position.token}</p>
                  <p className="text-sm text-gray-600">Confiance: {(position.confidence * 100).toFixed(0)}%</p>
                </div>
                <div className="text-right">
                  <p className="font-mono font-bold text-green-600">{position.allocation}</p>
                  <p className="text-sm text-gray-600">${position.amount_usd?.toLocaleString()}</p>
                </div>
              </div>
            ))}
            {(!portfolio.long_positions || portfolio.long_positions.length === 0) && (
              <p className="text-gray-500 text-center py-4">Aucune position long active</p>
            )}
          </div>
        </div>

        {/* Positions Short */}
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4 text-red-700 flex items-center">
            <FaArrowDown className="mr-2" />
            Positions Short
          </h3>
          <div className="space-y-3">
            {portfolio.short_positions?.map((position, idx) => (
              <div key={idx} className="flex items-center justify-between p-3 bg-red-50 rounded-lg">
                <div>
                  <p className="font-semibold">{position.token}</p>
                  <p className="text-sm text-gray-600">Confiance: {(position.confidence * 100).toFixed(0)}%</p>
                </div>
                <div className="text-right">
                  <p className="font-mono font-bold text-red-600">{position.allocation}</p>
                  <p className="text-sm text-gray-600">${position.amount_usd?.toLocaleString()}</p>
                </div>
              </div>
            ))}
            {(!portfolio.short_positions || portfolio.short_positions.length === 0) && (
              <p className="text-gray-500 text-center py-4">Aucune position short active</p>
            )}
          </div>
        </div>
      </div>

      {/* Section Cash et Stratégie */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Cash Reserve */}
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4 text-blue-700">💵 Réserve de Liquidités</h3>
          <div className="text-center">
            <div className="text-4xl font-bold font-mono text-blue-600 mb-2">
              {portfolio.cash_reserve}
            </div>
            <p className="text-gray-600">Disponible pour de nouvelles opportunités</p>
          </div>
        </div>

        {/* Stratégie Active */}
        <div className="bg-white p-6 rounded-lg shadow-md">
          <h3 className="text-lg font-semibold mb-4 text-purple-700">🧠 Stratégie IA Active</h3>
          <div className="bg-purple-50 p-4 rounded-lg">
            <p className="text-gray-800 italic">"{strategy_commentary}"</p>
          </div>
          <button
            onClick={handleRebalance}
            className="mt-4 w-full bg-purple-600 text-white py-2 px-4 rounded-lg hover:bg-purple-700 transition flex items-center justify-center"
          >
            <FaSync className="mr-2" />
            Rebalance Now
          </button>
        </div>
      </div>

      {/* Graphique de performance (simulé) */}
      <div className="bg-white p-6 rounded-lg shadow-md">
        <h3 className="text-lg font-semibold mb-4">📈 Performance Historique</h3>
        <div className="h-64 bg-gray-100 rounded-lg flex items-center justify-center">
          <div className="text-center text-gray-500">
            <FaChartLine className="text-4xl mx-auto mb-2" />
            <p>Graphique de performance en temps réel</p>
            <p className="text-sm">ROI cumulé: {performance.roi}%</p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HedgeFund;