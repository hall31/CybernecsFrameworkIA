import React, { useState, useEffect } from "react";
import ReactMarkdown from "react-markdown";

const ConstitutionPage = () => {
  const [constitution, setConstitution] = useState(null);
  const [loading, setLoading] = useState(true);
  const [expandedArticles, setExpandedArticles] = useState({});
  const [activeTab, setActiveTab] = useState("preamble");

  useEffect(() => {
    fetchConstitution();
  }, []);

  const fetchConstitution = async () => {
    try {
      setLoading(true);
      // En mode développement, utiliser les données statiques
      const response = await fetch("/src/data/constitution.json");
      const data = await response.json();
      setConstitution(data);
    } catch (error) {
      console.error("Erreur lors du chargement de la constitution:", error);
      // Fallback vers les données statiques
      try {
        const staticData = await import("../data/constitution.json");
        setConstitution(staticData.default);
      } catch (fallbackError) {
        console.error("Erreur lors du chargement des données statiques:", fallbackError);
      }
    } finally {
      setLoading(false);
    }
  };

  const toggleArticle = (articleId) => {
    setExpandedArticles(prev => ({
      ...prev,
      [articleId]: !prev[articleId]
    }));
  };

  const handleVote = (amendmentId, vote) => {
    // Simulation de vote - à connecter avec le système CoDAO
    console.log(`Vote ${vote} pour l'amendement ${amendmentId}`);
  };

  const getPriorityColor = (priority) => {
    switch (priority) {
      case "Critique": return "text-red-600 bg-red-50";
      case "Élevée": return "text-orange-600 bg-orange-50";
      case "Moyenne": return "text-blue-600 bg-blue-50";
      default: return "text-gray-600 bg-gray-50";
    }
  };

  const getCategoryIcon = (category) => {
    switch (category) {
      case "droits_humains": return "⚖️";
      case "devoirs_ia": return "🤖";
      case "gouvernance": return "🧑‍🤝‍🧑";
      default: return "📋";
    }
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
      </div>
    );
  }

  if (!constitution) {
    return (
      <div className="text-center py-12">
        <p className="text-gray-500">Impossible de charger la constitution</p>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-white to-purple-50">
      {/* Header */}
      <div className="bg-white shadow-sm border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
          <div className="flex items-center space-x-4">
            <div className="flex-shrink-0">
              <div className="w-16 h-16 bg-gradient-to-r from-blue-600 to-purple-600 rounded-2xl flex items-center justify-center">
                <span className="text-3xl text-white">⚖️</span>
              </div>
            </div>
            <div>
              <h1 className="text-3xl font-bold text-gray-900">
                Constitution IA Globale
              </h1>
              <p className="text-lg text-gray-600">
                Version {constitution.constitution.metadata.version} • 
                Dernière modification: {constitution.constitution.metadata.last_amended}
              </p>
            </div>
          </div>
        </div>
      </div>

      {/* Navigation Tabs */}
      <div className="bg-white border-b border-gray-200">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <nav className="flex space-x-8">
            {[
              { id: "preamble", name: "Préambule", icon: "📜" },
              { id: "articles", name: "Articles", icon: "📋" },
              { id: "amendments", name: "Amendements", icon: "✏️" },
              { id: "governance", name: "Gouvernance", icon: "🏛️" },
              { id: "history", name: "Historique", icon: "📚" }
            ].map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`py-4 px-1 border-b-2 font-medium text-sm flex items-center space-x-2 ${
                  activeTab === tab.id
                    ? "border-blue-500 text-blue-600"
                    : "border-transparent text-gray-500 hover:text-gray-700 hover:border-gray-300"
                }`}
              >
                <span>{tab.icon}</span>
                <span>{tab.name}</span>
              </button>
            ))}
          </nav>
        </div>
      </div>

      {/* Content */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Préambule Tab */}
        {activeTab === "preamble" && (
          <div className="bg-white rounded-2xl shadow-lg p-8 border border-gray-100">
            <div className="text-center mb-8">
              <h2 className="text-2xl font-bold text-gray-900 mb-4">📜 Préambule</h2>
              <div className="w-24 h-1 bg-gradient-to-r from-blue-500 to-purple-500 mx-auto rounded-full"></div>
            </div>
            <div className="prose prose-lg max-w-none">
              <ReactMarkdown>{constitution.constitution.preamble}</ReactMarkdown>
            </div>
          </div>
        )}

        {/* Articles Tab */}
        {activeTab === "articles" && (
          <div className="space-y-6">
            {Object.entries({
              "droits_humains": "⚖️ Droits des Humains",
              "devoirs_ia": "🤖 Devoirs des IA",
              "gouvernance": "🧑‍🤝‍🧑 Gouvernance"
            }).map(([categoryId, categoryName]) => (
              <div key={categoryId} className="bg-white rounded-2xl shadow-lg border border-gray-100">
                <div className="px-6 py-4 bg-gradient-to-r from-gray-50 to-gray-100 rounded-t-2xl">
                  <h3 className="text-xl font-semibold text-gray-900">{categoryName}</h3>
                </div>
                <div className="p-6">
                  {constitution.constitution.articles
                    .filter(article => article.category === categoryId)
                    .map(article => (
                      <div key={article.id} className="mb-6 last:mb-0">
                        <div className="flex items-start space-x-4">
                          <div className="flex-shrink-0 mt-1">
                            <div className="w-8 h-8 bg-blue-100 rounded-full flex items-center justify-center">
                              <span className="text-sm font-medium text-blue-600">
                                {article.id.split('-')[1]}
                              </span>
                            </div>
                          </div>
                          <div className="flex-1">
                            <div className="flex items-center space-x-3 mb-2">
                              <h4 className="text-lg font-semibold text-gray-900">
                                {article.title}
                              </h4>
                              <span className={`px-3 py-1 rounded-full text-xs font-medium ${getPriorityColor(article.priority)}`}>
                                {article.priority}
                              </span>
                            </div>
                            <p className="text-gray-700 leading-relaxed">
                              {article.content}
                            </p>
                          </div>
                        </div>
                      </div>
                    ))}
                </div>
              </div>
            ))}
          </div>
        )}

        {/* Amendements Tab */}
        {activeTab === "amendments" && (
          <div className="bg-white rounded-2xl shadow-lg border border-gray-100">
            <div className="px-6 py-4 bg-gradient-to-r from-green-50 to-green-100 rounded-t-2xl">
              <h3 className="text-xl font-semibold text-gray-900">✏️ Amendements Proposés</h3>
            </div>
            <div className="p-6">
              {constitution.constitution.amendments.map(amendment => (
                <div key={amendment.id} className="mb-6 last:mb-0 p-4 border border-gray-200 rounded-xl">
                  <div className="flex items-start justify-between mb-3">
                    <h4 className="text-lg font-semibold text-gray-900">{amendment.title}</h4>
                    <span className="px-3 py-1 bg-yellow-100 text-yellow-800 text-xs font-medium rounded-full">
                      {amendment.status}
                    </span>
                  </div>
                  <p className="text-gray-700 mb-4">{amendment.description}</p>
                  <div className="flex items-center justify-between">
                    <div className="text-sm text-gray-500">
                      <span>Majorité requise: {amendment.required_majority}</span>
                      <span className="mx-2">•</span>
                      <span>Votes: {amendment.votes_for} pour, {amendment.votes_against} contre</span>
                    </div>
                    <div className="flex space-x-2">
                      <button
                        onClick={() => handleVote(amendment.id, "for")}
                        className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-colors"
                      >
                        👍 Voter Pour
                      </button>
                      <button
                        onClick={() => handleVote(amendment.id, "against")}
                        className="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors"
                      >
                        👎 Voter Contre
                      </button>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          </div>
        )}

        {/* Gouvernance Tab */}
        {activeTab === "governance" && (
          <div className="bg-white rounded-2xl shadow-lg border border-gray-100">
            <div className="px-6 py-4 bg-gradient-to-r from-purple-50 to-purple-100 rounded-t-2xl">
              <h3 className="text-xl font-semibold text-gray-900">🏛️ Mécanismes de Gouvernance</h3>
            </div>
            <div className="p-6">
              <div className="grid md:grid-cols-2 gap-6">
                <div>
                  <h4 className="text-lg font-semibold text-gray-900 mb-3">Structure</h4>
                  <p className="text-gray-700 mb-4">{constitution.constitution.governance.structure}</p>
                  <p className="text-gray-700">{constitution.constitution.governance.voting_mechanism}</p>
                </div>
                <div>
                  <h4 className="text-lg font-semibold text-gray-900 mb-3">Seuils de Décision</h4>
                  <div className="space-y-2">
                    {Object.entries(constitution.constitution.governance.decision_thresholds).map(([decision, threshold]) => (
                      <div key={decision} className="flex justify-between items-center">
                        <span className="text-gray-700 capitalize">{decision.replace('_', ' ')}:</span>
                        <span className="font-medium text-gray-900">{threshold}</span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
              
              <div className="mt-6">
                <h4 className="text-lg font-semibold text-gray-900 mb-3">Parties Prenantes</h4>
                <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
                  {constitution.constitution.governance.stakeholders.map((stakeholder, index) => (
                    <div key={index} className="px-3 py-2 bg-gray-50 rounded-lg text-gray-700 text-sm">
                      {stakeholder}
                    </div>
                  ))}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* Historique Tab */}
        {activeTab === "history" && (
          <div className="bg-white rounded-2xl shadow-lg border border-gray-100">
            <div className="px-6 py-4 bg-gradient-to-r from-indigo-50 to-indigo-100 rounded-t-2xl">
              <h3 className="text-xl font-semibold text-gray-900">📚 Historique des Versions</h3>
            </div>
            <div className="p-6">
              <div className="space-y-4">
                <div className="flex items-center space-x-4 p-4 border border-green-200 bg-green-50 rounded-xl">
                  <div className="w-3 h-3 bg-green-500 rounded-full"></div>
                  <div className="flex-1">
                    <h4 className="font-semibold text-gray-900">Version 1.0.0</h4>
                    <p className="text-sm text-gray-600">Constitution initiale générée automatiquement</p>
                    <p className="text-xs text-gray-500">{constitution.constitution.generated_at}</p>
                  </div>
                  <span className="px-3 py-1 bg-green-100 text-green-800 text-xs font-medium rounded-full">
                    Actuelle
                  </span>
                </div>
                
                <div className="text-center py-8 text-gray-500">
                  <p>L'historique des versions sera disponible au fur et à mesure des amendements</p>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Download Button */}
      <div className="fixed bottom-6 right-6">
        <button
          onClick={() => {
            const blob = new Blob([constitution.markdown], { type: 'text/markdown' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'constitution-ia-globale.md';
            a.click();
            URL.revokeObjectURL(url);
          }}
          className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-3 rounded-full shadow-lg transition-all duration-200 flex items-center space-x-2"
        >
          <span>📥</span>
          <span>Télécharger</span>
        </button>
      </div>
    </div>
  );
};

export default ConstitutionPage;