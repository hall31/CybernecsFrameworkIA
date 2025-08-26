import React, { useState, useEffect } from "react";
import { FaPlus, FaChartPie, FaChartLine, FaExternalLinkAlt, FaEuroSign } from "react-icons/fa";
import FundCreationForm from "./FundCreationForm";
import FundCard from "./FundCard";
import FundDetails from "./FundDetails";

const FundsPage = () => {
  const [funds, setFunds] = useState([]);
  const [selectedFund, setSelectedFund] = useState(null);
  const [showCreationForm, setShowCreationForm] = useState(false);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    fetchFunds();
  }, []);

  const fetchFunds = async () => {
    try {
      setLoading(true);
      const response = await fetch("http://localhost:8000/funds");
      const data = await response.json();
      setFunds(data.funds || []);
    } catch (error) {
      console.error("Error fetching funds:", error);
    } finally {
      setLoading(false);
    }
  };

  const handleFundCreated = (newFund) => {
    setFunds([...funds, newFund]);
    setShowCreationForm(false);
  };

  const handleFundSelect = (fund) => {
    setSelectedFund(fund);
  };

  const handleBackToList = () => {
    setSelectedFund(null);
  };

  if (selectedFund) {
    return (
      <FundDetails 
        fund={selectedFund} 
        onBack={handleBackToList}
        onUpdate={fetchFunds}
      />
    );
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex justify-between items-center">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">🏦 Fonds IA (ETF)</h1>
          <p className="text-gray-600 mt-2">
            Gestion des fonds décentralisés pour startups IA
          </p>
        </div>
        <button
          onClick={() => setShowCreationForm(true)}
          className="flex items-center gap-2 px-6 py-3 bg-blue-600 text-white rounded-xl hover:bg-blue-700 transition-all duration-200 shadow-lg hover:shadow-xl"
        >
          <FaPlus className="text-sm" />
          Créer un Fonds
        </button>
      </div>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-white rounded-2xl p-6 shadow-xl border border-gray-100">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Total Fonds</p>
              <p className="text-2xl font-bold text-gray-900">{funds.length}</p>
            </div>
            <div className="p-3 bg-blue-100 rounded-xl">
              <FaChartPie className="text-blue-600 text-xl" />
            </div>
          </div>
        </div>

        <div className="bg-white rounded-2xl p-6 shadow-xl border border-gray-100">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Fonds Actifs</p>
              <p className="text-2xl font-bold text-gray-900">
                {funds.filter(f => f.status === "active").length}
              </p>
            </div>
            <div className="p-3 bg-green-100 rounded-xl">
              <FaChartLine className="text-green-600 text-xl" />
            </div>
          </div>
        </div>

        <div className="bg-white rounded-2xl p-6 shadow-xl border border-gray-100">
          <div className="flex items-center justify-between">
            <div>
              <p className="text-sm font-medium text-gray-600">Valeur Totale</p>
              <p className="text-2xl font-bold text-gray-900">
                {funds.reduce((sum, fund) => {
                  const nav = parseFloat(fund.nav.replace(" €", ""));
                  return sum + (isNaN(nav) ? 0 : nav);
                }, 0).toFixed(2)} €
              </p>
            </div>
            <div className="p-3 bg-purple-100 rounded-xl">
              <FaEuroSign className="text-purple-600 text-xl" />
            </div>
          </div>
        </div>
      </div>

      {/* Funds List */}
      <div className="bg-white rounded-2xl shadow-xl border border-gray-100">
        <div className="p-6 border-b border-gray-100">
          <h2 className="text-xl font-semibold text-gray-900">Fonds Actifs</h2>
          <p className="text-gray-600 mt-1">
            Investissez dans des portefeuilles diversifiés de startups IA
          </p>
        </div>

        {loading ? (
          <div className="p-12 text-center">
            <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
            <p className="text-gray-600 mt-4">Chargement des fonds...</p>
          </div>
        ) : funds.length === 0 ? (
          <div className="p-12 text-center">
            <div className="w-24 h-24 bg-gray-100 rounded-full flex items-center justify-center mx-auto mb-4">
              <FaChartPie className="text-gray-400 text-3xl" />
            </div>
            <h3 className="text-lg font-medium text-gray-900 mb-2">Aucun fonds créé</h3>
            <p className="text-gray-600 mb-4">
              Créez votre premier fonds IA pour commencer à investir
            </p>
            <button
              onClick={() => setShowCreationForm(true)}
              className="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition"
            >
              Créer un Fonds
            </button>
          </div>
        ) : (
          <div className="p-6">
            <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
              {funds.map((fund) => (
                <FundCard
                  key={fund.fund_symbol}
                  fund={fund}
                  onSelect={handleFundSelect}
                />
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Fund Creation Modal */}
      {showCreationForm && (
        <FundCreationForm
          onClose={() => setShowCreationForm(false)}
          onFundCreated={handleFundCreated}
        />
      )}
    </div>
  );
};

export default FundsPage;