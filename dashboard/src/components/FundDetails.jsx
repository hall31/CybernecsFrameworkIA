import React, { useState } from "react";
import { FaArrowLeft, FaChartPie, FaChartLine, FaExternalLinkAlt, FaEuroSign, FaCalendar, FaCog } from "react-icons/fa";

const FundDetails = ({ fund, onBack, onUpdate }) => {
  const [activeTab, setActiveTab] = useState("overview");
  const [investmentAmount, setInvestmentAmount] = useState("");

  const tabs = [
    { id: "overview", label: "Vue d'ensemble", icon: FaChartPie },
    { id: "performance", label: "Performance", icon: FaChartLine },
    { id: "composition", label: "Composition", icon: FaCog },
  ];

  const generateMockPerformanceData = () => {
    const data = [];
    const baseValue = parseFloat(fund.nav.replace(" €", ""));
    
    for (let i = 30; i >= 0; i--) {
      const date = new Date();
      date.setDate(date.getDate() - i);
      
      // Simulate some volatility
      const variation = (Math.random() - 0.5) * 0.1; // ±5% variation
      const value = baseValue * (1 + variation);
      
      data.push({
        date: date.toISOString().split('T')[0],
        value: value.toFixed(2)
      });
    }
    
    return data;
  };

  const performanceData = generateMockPerformanceData();

  const handleInvest = () => {
    if (!investmentAmount || parseFloat(investmentAmount) <= 0) return;
    
    // Simulate investment
    alert(`Investissement de ${investmentAmount}€ dans ${fund.fund_symbol} effectué !`);
    setInvestmentAmount("");
  };

  const handleSell = () => {
    // Simulate selling
    alert(`Vente de vos parts de ${fund.fund_symbol} effectuée !`);
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex items-center gap-4">
        <button
          onClick={onBack}
          className="p-2 hover:bg-gray-100 rounded-xl transition-colors"
        >
          <FaArrowLeft className="text-gray-600" />
        </button>
        
        <div>
          <h1 className="text-3xl font-bold text-gray-900">{fund.fund_symbol}</h1>
          <p className="text-gray-600">Fonds IA Startup - Détails</p>
        </div>
      </div>

      {/* Fund Overview Card */}
      <div className="bg-white rounded-2xl shadow-xl border border-gray-100 p-6">
        <div className="grid grid-cols-1 md:grid-cols-4 gap-6">
          <div className="text-center">
            <div className="text-2xl font-bold text-gray-900">{fund.nav}</div>
            <div className="text-sm text-gray-600">Valeur actuelle (NAV)</div>
          </div>
          
          <div className="text-center">
            <div className="text-2xl font-bold text-blue-600">{fund.composition.length}</div>
            <div className="text-sm text-gray-600">Startups incluses</div>
          </div>
          
          <div className="text-center">
            <div className="text-2xl font-bold text-green-600">
              {fund.status === "active" ? "🟢" : "⚫"} {fund.status}
            </div>
            <div className="text-sm text-gray-600">Statut</div>
          </div>
          
          <div className="text-center">
            <div className="text-2xl font-bold text-purple-600">
              {new Date(fund.created_at).toLocaleDateString()}
            </div>
            <div className="text-sm text-gray-600">Date de création</div>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="bg-white rounded-2xl shadow-xl border border-gray-100">
        <div className="border-b border-gray-100">
          <nav className="flex space-x-8 px-6">
            {tabs.map((tab) => {
              const Icon = tab.icon;
              return (
                <button
                  key={tab.id}
                  onClick={() => setActiveTab(tab.id)}
                  className={`flex items-center gap-2 py-4 px-1 border-b-2 font-medium text-sm transition-colors ${
                    activeTab === tab.id
                      ? "border-blue-500 text-blue-600"
                      : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
                  }`}
                >
                  <Icon className="text-sm" />
                  {tab.label}
                </button>
              );
            })}
          </nav>
        </div>

        <div className="p-6">
          {/* Overview Tab */}
          {activeTab === "overview" && (
            <div className="space-y-6">
              <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                {/* Composition Chart */}
                <div className="bg-gray-50 rounded-xl p-6">
                  <h3 className="text-lg font-semibold text-gray-900 mb-4">Composition du Fonds</h3>
                  <div className="space-y-3">
                    {fund.composition.map((item, index) => (
                      <div key={index} className="flex items-center justify-between">
                        <div className="flex items-center gap-3">
                          <div
                            className="w-4 h-4 rounded-full"
                            style={{
                              backgroundColor: `hsl(${index * 60}, 70%, 60%)`
                            }}
                          ></div>
                          <span className="font-medium text-gray-900">{item.token}</span>
                        </div>
                        <span className="text-lg font-bold text-gray-900">{item.weight}</span>
                      </div>
                    ))}
                  </div>
                </div>

                {/* Investment Actions */}
                <div className="space-y-4">
                  <h3 className="text-lg font-semibold text-gray-900">Actions</h3>
                  
                  {/* Invest */}
                  <div className="bg-green-50 rounded-xl p-4 border border-green-200">
                    <h4 className="font-medium text-green-900 mb-3">Investir</h4>
                    <div className="flex gap-2">
                      <input
                        type="number"
                        value={investmentAmount}
                        onChange={(e) => setInvestmentAmount(e.target.value)}
                        placeholder="Montant en €"
                        className="flex-1 px-3 py-2 border border-green-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                      />
                      <button
                        onClick={handleInvest}
                        disabled={!investmentAmount || parseFloat(investmentAmount) <= 0}
                        className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:bg-gray-400 disabled:cursor-not-allowed transition-colors"
                      >
                        Investir
                      </button>
                    </div>
                  </div>

                  {/* Sell */}
                  <div className="bg-red-50 rounded-xl p-4 border border-red-200">
                    <h4 className="font-medium text-red-900 mb-3">Vendre</h4>
                    <button
                      onClick={handleSell}
                      className="w-full px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors"
                    >
                      Vendre mes parts
                    </button>
                  </div>
                </div>
              </div>

              {/* Contract Information */}
              <div className="bg-blue-50 rounded-xl p-4 border border-blue-200">
                <h3 className="font-medium text-blue-900 mb-3">Informations du Smart Contract</h3>
                <div className="flex items-center justify-between">
                  <span className="text-sm text-blue-800">Adresse du contrat:</span>
                  <a
                    href={`https://etherscan.io/address/${fund.fund_address}`}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="flex items-center gap-2 text-blue-600 hover:text-blue-700 transition-colors text-sm"
                  >
                    {fund.fund_address}
                    <FaExternalLinkAlt className="text-xs" />
                  </a>
                </div>
              </div>
            </div>
          )}

          {/* Performance Tab */}
          {activeTab === "performance" && (
            <div className="space-y-6">
              <h3 className="text-lg font-semibold text-gray-900">Évolution de la valeur (30 jours)</h3>
              
              {/* Performance Chart */}
              <div className="bg-gray-50 rounded-xl p-6">
                <div className="h-64 flex items-center justify-center">
                  <div className="text-center">
                    <FaChartLine className="text-4xl text-blue-600 mx-auto mb-3" />
                    <p className="text-gray-600">Graphique d'évolution du NAV</p>
                    <p className="text-sm text-gray-500 mt-2">
                      Données de performance sur 30 jours
                    </p>
                  </div>
                </div>
              </div>

              {/* Performance Data */}
              <div className="bg-white rounded-xl border border-gray-200 p-4">
                <h4 className="font-medium text-gray-900 mb-3">Données de performance</h4>
                <div className="space-y-2 max-h-48 overflow-y-auto">
                  {performanceData.slice(-10).map((data, index) => (
                    <div key={index} className="flex justify-between items-center text-sm">
                      <span className="text-gray-600">{data.date}</span>
                      <span className="font-medium text-gray-900">{data.value} €</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          )}

          {/* Composition Tab */}
          {activeTab === "composition" && (
            <div className="space-y-6">
              <h3 className="text-lg font-semibold text-gray-900">Détails de la composition</h3>
              
              <div className="grid gap-4">
                {fund.composition.map((item, index) => (
                  <div key={index} className="bg-gray-50 rounded-xl p-4">
                    <div className="flex items-center justify-between mb-2">
                      <h4 className="font-medium text-gray-900">{item.token}</h4>
                      <span className="text-lg font-bold text-blue-600">{item.weight}</span>
                    </div>
                    
                    <div className="w-full bg-gray-200 rounded-full h-2">
                      <div
                        className="bg-blue-600 h-2 rounded-full transition-all duration-300"
                        style={{ width: `${item.percentage}%` }}
                      ></div>
                    </div>
                    
                    <div className="mt-2 text-sm text-gray-600">
                      Poids dans le portefeuille: {item.percentage}%
                    </div>
                  </div>
                ))}
              </div>

              <div className="bg-blue-50 rounded-xl p-4 border border-blue-200">
                <h4 className="font-medium text-blue-900 mb-2">Diversification</h4>
                <p className="text-sm text-blue-800">
                  Ce fonds offre une diversification automatique sur {fund.composition.length} startups IA,
                  réduisant le risque de concentration sur une seule entreprise.
                </p>
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default FundDetails;