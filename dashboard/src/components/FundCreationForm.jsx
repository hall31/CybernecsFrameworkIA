import React, { useState, useEffect } from "react";
import { FaTimes, FaChartPie, FaCheck, FaSpinner } from "react-icons/fa";

const FundCreationForm = ({ onClose, onFundCreated }) => {
  const [selectedStartups, setSelectedStartups] = useState([]);
  const [availableStartups, setAvailableStartups] = useState([]);
  const [loading, setLoading] = useState(false);
  const [creating, setCreating] = useState(false);
  const [error, setError] = useState("");

  // Mock available startups (in real app, this would come from the API)
  useEffect(() => {
    setAvailableStartups([
      { symbol: "STK001", name: "AI Analytics Pro", sector: "Analytics" },
      { symbol: "STK002", name: "ML Platform", sector: "Machine Learning" },
      { symbol: "STK003", name: "NLP Solutions", sector: "Natural Language" },
      { symbol: "STK004", name: "Computer Vision", sector: "Vision AI" },
      { symbol: "STK005", name: "AI Chatbot", sector: "Conversational AI" },
      { symbol: "STK006", name: "Predictive Models", sector: "Predictive AI" },
      { symbol: "STK007", name: "AI Security", sector: "Cybersecurity" },
      { symbol: "STK008", name: "AI Healthcare", sector: "Health Tech" },
    ]);
  }, []);

  const handleStartupToggle = (startup) => {
    setSelectedStartups(prev => {
      const isSelected = prev.find(s => s.symbol === startup.symbol);
      if (isSelected) {
        return prev.filter(s => s.symbol !== startup.symbol);
      } else {
        return [...prev, startup];
      }
    });
  };

  const handleCreateFund = async () => {
    if (selectedStartups.length < 2) {
      setError("Sélectionnez au moins 2 startups pour créer un fonds");
      return;
    }

    setCreating(true);
    setError("");

    try {
      const response = await fetch("http://localhost:8000/funds", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          startups: selectedStartups.map(s => s.symbol)
        }),
      });

      if (!response.ok) {
        throw new Error("Erreur lors de la création du fonds");
      }

      const fund = await response.json();
      onFundCreated(fund);
    } catch (error) {
      setError("Erreur lors de la création du fonds: " + error.message);
    } finally {
      setCreating(false);
    }
  };

  const getCompositionPreview = () => {
    if (selectedStartups.length === 0) return [];
    
    const total = selectedStartups.length;
    let weights = [];
    
    if (total === 2) {
      weights = [60, 40];
    } else if (total === 3) {
      weights = [40, 30, 30];
    } else if (total === 4) {
      weights = [30, 25, 25, 20];
    } else {
      const baseWeight = Math.floor(100 / total);
      weights = Array(total).fill(baseWeight);
      weights[0] += 100 - (baseWeight * total);
    }

    return selectedStartups.map((startup, index) => ({
      ...startup,
      weight: weights[index]
    }));
  };

  const composition = getCompositionPreview();

  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div className="bg-white rounded-2xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        {/* Header */}
        <div className="p-6 border-b border-gray-100 flex justify-between items-center">
          <div>
            <h2 className="text-2xl font-bold text-gray-900">Créer un Fonds IA</h2>
            <p className="text-gray-600 mt-1">
              Sélectionnez les startups pour créer un portefeuille diversifié
            </p>
          </div>
          <button
            onClick={onClose}
            className="p-2 hover:bg-gray-100 rounded-xl transition-colors"
          >
            <FaTimes className="text-gray-500" />
          </button>
        </div>

        <div className="p-6">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-8">
            {/* Startup Selection */}
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-4">
                Sélection des Startups
              </h3>
              
              <div className="space-y-3 max-h-96 overflow-y-auto">
                {availableStartups.map((startup) => {
                  const isSelected = selectedStartups.find(s => s.symbol === startup.symbol);
                  return (
                    <div
                      key={startup.symbol}
                      onClick={() => handleStartupToggle(startup)}
                      className={`p-4 rounded-xl border-2 cursor-pointer transition-all duration-200 ${
                        isSelected
                          ? "border-blue-500 bg-blue-50"
                          : "border-gray-200 hover:border-gray-300 hover:bg-gray-50"
                      }`}
                    >
                      <div className="flex items-center justify-between">
                        <div>
                          <div className="flex items-center gap-2">
                            <span className="font-semibold text-gray-900">
                              {startup.symbol}
                            </span>
                            {isSelected && (
                              <FaCheck className="text-blue-600 text-sm" />
                            )}
                          </div>
                          <p className="text-sm text-gray-600">{startup.name}</p>
                          <span className="text-xs text-gray-500 bg-gray-100 px-2 py-1 rounded-full">
                            {startup.sector}
                          </span>
                        </div>
                      </div>
                    </div>
                  );
                })}
              </div>

              {selectedStartups.length > 0 && (
                <div className="mt-4 p-3 bg-blue-50 rounded-xl">
                  <p className="text-sm text-blue-800">
                    <strong>{selectedStartups.length}</strong> startup(s) sélectionnée(s)
                  </p>
                </div>
              )}
            </div>

            {/* Composition Preview */}
            <div>
              <h3 className="text-lg font-semibold text-gray-900 mb-4">
                Prévisualisation du Fonds
              </h3>
              
              {composition.length > 0 ? (
                <div className="space-y-4">
                  {/* Pie Chart Placeholder */}
                  <div className="bg-gray-50 rounded-xl p-6 text-center">
                    <FaChartPie className="text-4xl text-blue-600 mx-auto mb-3" />
                    <p className="text-sm text-gray-600">
                      Graphique de composition du fonds
                    </p>
                  </div>

                  {/* Composition Details */}
                  <div className="bg-white rounded-xl border border-gray-200 p-4">
                    <h4 className="font-medium text-gray-900 mb-3">Répartition</h4>
                    <div className="space-y-2">
                      {composition.map((item, index) => (
                        <div key={index} className="flex justify-between items-center">
                          <div className="flex items-center gap-2">
                            <div
                              className="w-3 h-3 rounded-full"
                              style={{
                                backgroundColor: `hsl(${index * 60}, 70%, 60%)`
                              }}
                            ></div>
                            <span className="text-sm text-gray-700">{item.symbol}</span>
                          </div>
                          <span className="font-medium text-gray-900">{item.weight}%</span>
                        </div>
                      ))}
                    </div>
                  </div>

                  {/* Fund Info */}
                  <div className="bg-blue-50 rounded-xl p-4">
                    <h4 className="font-medium text-blue-900 mb-2">Informations du Fonds</h4>
                    <div className="text-sm text-blue-800 space-y-1">
                      <p>• Symbole: ETF{Math.floor(Math.random() * 900) + 100}</p>
                      <p>• Type: Fonds diversifié IA</p>
                      <p>• Nombre de positions: {composition.length}</p>
                    </div>
                  </div>
                </div>
              ) : (
                <div className="bg-gray-50 rounded-xl p-12 text-center">
                  <FaChartPie className="text-4xl text-gray-400 mx-auto mb-3" />
                  <p className="text-gray-600">
                    Sélectionnez des startups pour voir la composition du fonds
                  </p>
                </div>
              )}
            </div>
          </div>

          {/* Error Message */}
          {error && (
            <div className="mt-6 p-4 bg-red-50 border border-red-200 rounded-xl">
              <p className="text-red-800 text-sm">{error}</p>
            </div>
          )}

          {/* Actions */}
          <div className="mt-8 flex justify-end gap-3">
            <button
              onClick={onClose}
              className="px-6 py-3 text-gray-700 bg-gray-100 rounded-xl hover:bg-gray-200 transition-colors"
            >
              Annuler
            </button>
            <button
              onClick={handleCreateFund}
              disabled={selectedStartups.length < 2 || creating}
              className={`px-6 py-3 text-white rounded-xl transition-colors flex items-center gap-2 ${
                selectedStartups.length < 2 || creating
                  ? "bg-gray-400 cursor-not-allowed"
                  : "bg-blue-600 hover:bg-blue-700"
              }`}
            >
              {creating ? (
                <>
                  <FaSpinner className="animate-spin" />
                  Création...
                </>
              ) : (
                "Créer le Fonds"
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default FundCreationForm;